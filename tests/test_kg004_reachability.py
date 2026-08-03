from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from knowledge_guardian.reachability import ReachabilityConfig, evaluate_reachability


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "document-model" / "0.1.0"


def snapshot() -> dict:
    return {
        "contract": {"name": "knowledge-guardian-repository-snapshot", "version": "0.1.0"},
        "snapshot_id": "snapshot:test",
        "repository": "example/repository",
        "ref": "main",
        "captured_at": "2026-08-03T12:00:00-03:00",
    }


def resources(*paths: str) -> list[dict]:
    return [
        {
            "contract": {"name": "knowledge-guardian-resource", "version": "0.1.0"},
            "resource_id": f"resource:{path}",
            "snapshot_id": "snapshot:test",
            "path": path,
            "format": "markdown",
        }
        for path in paths
    ]


def relationship(source: str, target: str, relationship_id: str = "r1") -> dict:
    return {
        "contract": {"name": "knowledge-guardian-relationship", "version": "0.1.0"},
        "relationship_id": relationship_id,
        "snapshot_id": "snapshot:test",
        "source_document_id": f"resource:{source}",
        "target": {"kind": "relative_path", "value": target},
        "type": "links_to",
        "provenance": "explicit_link",
    }


def entry_point_validator() -> Draft202012Validator:
    schemas = {
        path.name: json.loads(path.read_text(encoding="utf-8"))
        for path in SCHEMA_DIR.glob("*.schema.json")
    }
    registry = Registry()
    for name, schema in schemas.items():
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
        registry = registry.with_resource(name, Resource.from_contents(schema))
    return Draft202012Validator(schemas["entry-point.schema.json"], registry=registry, format_checker=FormatChecker())


class KG004ReachabilityTests(unittest.TestCase):
    def test_profile_and_native_entries_are_schema_valid_and_paths_are_deterministic(self) -> None:
        result = evaluate_reachability(
            snapshot(),
            resources("README.md", "AGENTS.md", "docs/guide.md", "docs/legacy.md"),
            [relationship("README.md", "docs/guide.md")],
            config=ReachabilityConfig(
                project_profile_entry_points=({"path": "README.md", "audience": ["human"], "priority": 0},),
            ),
        )

        self.assertEqual([item["path"] for item in result.entry_points], ["AGENTS.md", "README.md"])
        self.assertTrue(all(not list(entry_point_validator().iter_errors(item)) for item in result.entry_points))
        states = {item["resource_id"]: item for item in result.states}
        self.assertEqual(states["resource:README.md"]["state"], "reachable")
        self.assertEqual(states["resource:docs/guide.md"]["state"], "reachable")
        self.assertEqual(states["resource:docs/guide.md"]["distance"], 1)
        self.assertEqual(states["resource:docs/legacy.md"]["state"], "candidate_orphan")

    def test_no_relationship_input_is_not_evaluated(self) -> None:
        result = evaluate_reachability(
            snapshot(),
            resources("README.md", "docs/guide.md"),
            None,
            config=ReachabilityConfig(native_conventions=("README.md",)),
        )
        self.assertEqual({item["state"] for item in result.states}, {"not_evaluated"})
        self.assertFalse(result.summary["relationships_complete"])

    def test_no_entry_point_prevents_candidate_orphan(self) -> None:
        result = evaluate_reachability(
            snapshot(),
            resources("docs/guide.md"),
            [],
            config=ReachabilityConfig(native_conventions=()),
        )
        self.assertEqual(result.states[0]["state"], "no_entry_point")
        self.assertNotIn("candidate_orphan", {item["state"] for item in result.states})

    def test_invalid_relationship_makes_source_indeterminate(self) -> None:
        invalid = relationship("README.md", "missing.md")
        result = evaluate_reachability(
            snapshot(),
            resources("README.md", "docs/guide.md"),
            [invalid],
            config=ReachabilityConfig(native_conventions=("README.md",)),
        )
        states = {item["resource_id"]: item["state"] for item in result.states}
        self.assertEqual(states["resource:README.md"], "indeterminate")
        self.assertEqual(states["resource:docs/guide.md"], "candidate_orphan")
        self.assertEqual(result.diagnostics[0].code, "RELATIONSHIP_TARGET_MISSING")

    def test_profile_exclusion_is_explicit(self) -> None:
        result = evaluate_reachability(
            snapshot(),
            resources("README.md", "docs/legacy.md"),
            [],
            config=ReachabilityConfig(native_conventions=("README.md",), excluded_paths=("docs/legacy.md",)),
        )
        states = {item["resource_id"]: item["state"] for item in result.states}
        self.assertEqual(states["resource:docs/legacy.md"], "excluded")


if __name__ == "__main__":
    unittest.main()
