"""Bounded entry-point resolution and reachability evidence for KG-004.

This module consumes KG-003 resources and caller-supplied Relationship
records. It does not parse documents, discover links, or emit findings.
"""

from __future__ import annotations

import hashlib
import json
from collections import deque
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Iterable, Optional

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource


CONTRACT_VERSION = "0.1.0"
DEFAULT_NATIVE_CONVENTIONS = (
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "CLAUDE.md",
    "GEMINI.md",
)
NATIVE_AUDIENCES = {
    "README.md": ("human", "contributor"),
    "AGENTS.md": ("agent",),
    "CONTRIBUTING.md": ("contributor",),
    "SECURITY.md": ("contributor", "operator"),
    "CODE_OF_CONDUCT.md": ("contributor",),
    "CLAUDE.md": ("agent",),
    "GEMINI.md": ("agent",),
}
ALLOWED_AUDIENCES = {"human", "agent", "contributor", "operator"}


@dataclass(frozen=True)
class ReachabilityConfig:
    """Caller-supplied policy; no repository content is inferred."""

    project_profile_entry_points: tuple[dict, ...] = ()
    native_conventions: Optional[tuple[str, ...]] = None
    excluded_paths: tuple[str, ...] = ()


@dataclass(frozen=True)
class ReachabilityDiagnostic:
    code: str
    level: str
    path: Optional[str]
    message: str
    cause_type: Optional[str] = None

    @property
    def diagnostic_id(self) -> str:
        payload = {
            "code": self.code,
            "path": self.path,
            "message": self.message,
            "cause_type": self.cause_type,
        }
        digest = hashlib.sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()[:24]
        return f"diagnostic:{digest}"

    def to_dict(self) -> dict:
        return {
            "diagnostic_id": self.diagnostic_id,
            "code": self.code,
            "level": self.level,
            "path": self.path,
            "message": self.message,
            "cause_type": self.cause_type,
        }


@dataclass
class ReachabilityResult:
    entry_points: list[dict]
    states: list[dict]
    diagnostics: list[ReachabilityDiagnostic]
    summary: dict

    def to_dict(self) -> dict:
        return {
            "entry_points": self.entry_points,
            "states": self.states,
            "diagnostics": [item.to_dict() for item in self.diagnostics],
            "summary": self.summary,
        }


def _normalize_path(value: str) -> str:
    candidate = value.replace("\\", "/")
    path = PurePosixPath(candidate)
    if path.is_absolute() or any(part in ("", "..") for part in path.parts):
        raise ValueError("path must be repository-relative")
    normalized = path.as_posix()
    if normalized in ("", "."):
        raise ValueError("path must not be empty")
    return normalized


def _diagnostic(code: str, level: str, path: Optional[str], message: str, cause_type: Optional[str] = None):
    return ReachabilityDiagnostic(code, level, path, message, cause_type)


def _entry_point(snapshot_id: str, path: str, audience: Iterable[str], source: str, priority: Optional[int]) -> dict:
    item = {
        "contract": {"name": "knowledge-guardian-entry-point", "version": CONTRACT_VERSION},
        "entry_point_id": f"entry:{source}:{path}",
        "snapshot_id": snapshot_id,
        "path": path,
        "audience": sorted(set(audience)),
        "source": source,
    }
    if priority is not None:
        item["priority"] = priority
    return item


def _relationship_validator() -> Draft202012Validator:
    from pathlib import Path

    schema_dir = Path(__file__).resolve().parents[1] / "schemas" / "document-model" / CONTRACT_VERSION
    schemas = {
        path.name: json.loads(path.read_text(encoding="utf-8"))
        for path in schema_dir.glob("*.schema.json")
    }
    registry = Registry()
    for name, schema in schemas.items():
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
        registry = registry.with_resource(name, Resource.from_contents(schema))
    return Draft202012Validator(
        schemas["relationship.schema.json"],
        registry=registry,
        format_checker=FormatChecker(),
    )


def _resolve_target(target: dict, by_id: dict[str, dict], by_path: dict[str, dict]) -> Optional[dict]:
    if target["kind"] == "document_id":
        return by_id.get(target["value"])
    if target["kind"] == "relative_path":
        try:
            return by_path.get(_normalize_path(target["value"]))
        except ValueError:
            return None
    return None


def _best_paths(entry_points: list[dict], adjacency: dict[str, set[str]], by_path: dict[str, dict]):
    paths: dict[str, list[tuple[str, tuple[str, ...]]]] = {}
    for entry in entry_points:
        start = by_path[entry["path"]]["resource_id"]
        queue = deque([(start, (start,))])
        seen = {start}
        while queue:
            current, path = queue.popleft()
            candidate = (entry["entry_point_id"], path)
            paths.setdefault(current, []).append(candidate)
            for target_id in sorted(adjacency.get(current, ())):
                if target_id not in seen:
                    seen.add(target_id)
                    queue.append((target_id, path + (target_id,)))
    return {
        resource_id: sorted(candidates, key=lambda item: (len(item[1]), item[0], item[1]))[0]
        for resource_id, candidates in paths.items()
    }


def evaluate_reachability(
    snapshot: dict,
    resources: Iterable[dict],
    relationships: Optional[Iterable[dict]],
    *,
    config: ReachabilityConfig = ReachabilityConfig(),
) -> ReachabilityResult:
    """Resolve entry points and calculate bounded reachability evidence."""

    snapshot_id = snapshot.get("snapshot_id")
    if not snapshot_id:
        raise ValueError("snapshot.snapshot_id is required")
    resource_list = sorted(resources, key=lambda item: item.get("path", ""))
    by_id = {item.get("resource_id"): item for item in resource_list if item.get("resource_id")}
    by_path = {item.get("path"): item for item in resource_list if item.get("path")}
    excluded = set()
    diagnostics: list[ReachabilityDiagnostic] = []
    for path in config.excluded_paths:
        try:
            excluded.add(_normalize_path(path))
        except ValueError:
            diagnostics.append(_diagnostic("INVALID_EXCLUSION", "error", None, "Invalid excluded path"))

    entry_points: list[dict] = []
    profile_paths: set[str] = set()
    for declaration in config.project_profile_entry_points:
        try:
            path = _normalize_path(declaration["path"])
            audience = declaration["audience"]
            if (
                not isinstance(audience, list)
                or not audience
                or len(set(audience)) != len(audience)
                or not set(audience).issubset(ALLOWED_AUDIENCES)
            ):
                raise ValueError("audience must be a unique non-empty list of allowed values")
            priority = declaration.get("priority")
            if priority is not None and (not isinstance(priority, int) or priority < 0):
                raise ValueError("priority must be a non-negative integer")
        except (KeyError, TypeError, ValueError) as exc:
            diagnostics.append(_diagnostic("INVALID_ENTRY_POINT", "error", None, "Invalid project profile entry point", type(exc).__name__))
            continue
        profile_paths.add(path)
        if path not in by_path:
            diagnostics.append(_diagnostic("ENTRY_POINT_MISSING", "warning", path, "Configured entry point is absent from inventory"))
            continue
        if path in excluded:
            diagnostics.append(_diagnostic("ENTRY_POINT_EXCLUDED", "warning", path, "Configured entry point is excluded"))
            continue
        entry_points.append(_entry_point(snapshot_id, path, audience, "project_profile", priority))

    native_paths = DEFAULT_NATIVE_CONVENTIONS if config.native_conventions is None else config.native_conventions
    for path in sorted(set(native_paths)):
        if path in profile_paths:
            diagnostics.append(_diagnostic("ENTRY_POINT_SOURCE_CONFLICT", "info", path, "Project profile takes precedence over native convention"))
            continue
        if path in excluded or path not in by_path:
            continue
        entry_points.append(_entry_point(snapshot_id, path, NATIVE_AUDIENCES.get(path, ("human",)), "native_convention", None))

    entry_points.sort(key=lambda item: (item["path"], item["source"], item["entry_point_id"]))
    relationship_list = None if relationships is None else list(relationships)
    validator = _relationship_validator()
    adjacency: dict[str, set[str]] = {}
    invalid_sources: set[str] = set()
    relationships_complete = relationship_list is not None
    if relationship_list is not None:
        for relationship in relationship_list:
            errors = list(validator.iter_errors(relationship))
            source_id = relationship.get("source_document_id") if isinstance(relationship, dict) else None
            source_resource = by_id.get(source_id)
            source_path = source_resource.get("path") if source_resource else None
            if errors:
                invalid_sources.add(source_id or "")
                diagnostics.append(_diagnostic("RELATIONSHIP_INVALID", "error", source_path, "Relationship failed schema validation"))
                continue
            if relationship["snapshot_id"] != snapshot_id:
                invalid_sources.add(source_id)
                diagnostics.append(_diagnostic("RELATIONSHIP_SNAPSHOT_MISMATCH", "error", source_path, "Relationship belongs to another snapshot"))
                continue
            if source_resource is None:
                diagnostics.append(_diagnostic("RELATIONSHIP_SOURCE_MISSING", "error", None, "Relationship source is absent from inventory"))
                continue
            target_resource = _resolve_target(relationship["target"], by_id, by_path)
            if target_resource is None:
                invalid_sources.add(source_id)
                diagnostics.append(_diagnostic("RELATIONSHIP_TARGET_MISSING", "warning", source_path, "Relationship target is absent or not internal"))
                continue
            if relationship["type"] == "links_to" and relationship["provenance"] == "explicit_link":
                adjacency.setdefault(source_id, set()).add(target_resource["resource_id"])

    best_paths = _best_paths(entry_points, adjacency, by_path) if entry_points else {}
    states: list[dict] = []
    for resource in resource_list:
        resource_id = resource["resource_id"]
        path = resource["path"]
        if path in excluded:
            state = "excluded"
            evidence = {"reason": "project_profile_exclusion"}
        elif not entry_points:
            state = "no_entry_point"
            evidence = {"reason": "no_resolved_entry_point"}
        elif resource_id in invalid_sources:
            state = "indeterminate"
            evidence = {"reason": "relationship_evidence_incomplete"}
        elif relationship_list is None:
            state = "not_evaluated"
            evidence = {"reason": "relationship_input_not_supplied"}
        elif resource_id in best_paths:
            entry_id, path_ids = best_paths[resource_id]
            state = "reachable"
            evidence = {"entry_point_id": entry_id, "path": list(path_ids), "distance": len(path_ids) - 1}
        else:
            state = "candidate_orphan"
            evidence = {"evaluated_entry_points": [item["entry_point_id"] for item in entry_points], "reason": "no_explicit_path"}
        states.append({"resource_id": resource_id, "state": state, **evidence})

    diagnostics.sort(key=lambda item: (item.path or "", item.code, item.message))
    state_counts = {state: sum(item["state"] == state for item in states) for state in (
        "reachable", "candidate_orphan", "excluded", "not_evaluated", "indeterminate", "no_entry_point"
    )}
    summary = {
        "resources_evaluated": len(states),
        "entry_points_resolved": len(entry_points),
        "relationships_supplied": 0 if relationship_list is None else len(relationship_list),
        "relationships_complete": relationships_complete,
        "state_counts": state_counts,
        "diagnostic_counts": {code: sum(item.code == code for item in diagnostics) for code in sorted({item.code for item in diagnostics})},
    }
    return ReachabilityResult(entry_points, states, diagnostics, summary)
