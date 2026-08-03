"""Bounded, read-only Markdown resource inventory for KG-003.

This module deliberately inventories paths and observed file metadata only. It
does not parse document contents, classify documents, discover relationships,
or generate findings.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat as stat_module
import time
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Optional


CONTRACT_VERSION = "0.1.0"
DEFAULT_EXTENSIONS = (".md", ".mdx")


@dataclass(frozen=True)
class InventoryConfig:
    """Caller-supplied context and bounded inventory policy."""

    repository_root: Path
    repository: str
    ref: str
    captured_at: str
    commit_sha: Optional[str] = None
    include_extensions: tuple[str, ...] = DEFAULT_EXTENSIONS
    ignore_paths: tuple[str, ...] = ()
    calculate_checksum: bool = True
    follow_symlinks: bool = False
    include_hidden_directories: bool = True


@dataclass(frozen=True)
class DiscoveryDiagnostic:
    code: str
    level: str
    path: Optional[str]
    operation: str
    message: str
    cause_type: Optional[str] = None

    @property
    def diagnostic_id(self) -> str:
        payload = {
            "code": self.code,
            "path": self.path,
            "operation": self.operation,
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
            "operation": self.operation,
            "message": self.message,
            "cause_type": self.cause_type,
        }


@dataclass
class InventoryResult:
    snapshot: dict
    resources: list[dict]
    diagnostics: list[DiscoveryDiagnostic]
    summary: dict

    def to_dict(self) -> dict:
        return {
            "snapshot": self.snapshot,
            "resources": self.resources,
            "diagnostics": [item.to_dict() for item in self.diagnostics],
            "summary": self.summary,
        }


class LocalFileSystem:
    """Small seam around filesystem operations for deterministic tests."""

    def resolve_root(self, path: Path) -> Path:
        return path.resolve(strict=True)

    def walk(self, root: Path) -> Iterable[tuple[Path, list[str], list[str]]]:
        for current, directories, files in os.walk(root, topdown=True, followlinks=False):
            directories.sort()
            files.sort()
            yield Path(current), directories, files

    def is_symlink(self, path: Path) -> bool:
        return path.is_symlink()

    def stat(self, path: Path):
        return path.stat()

    def read_bytes(self, path: Path) -> bytes:
        return path.read_bytes()


def _normalize_relative_path(value: str) -> str:
    candidate = value.replace("\\", "/")
    while candidate.startswith("./"):
        candidate = candidate[2:]
    path = PurePosixPath(candidate)
    if path.is_absolute() or any(part == ".." for part in path.parts):
        raise ValueError("path is absolute or escapes the repository root")
    normalized = path.as_posix()
    if normalized in ("", "."):
        return ""
    return normalized


def _relative_path(root: Path, path: Path) -> str:
    try:
        relative = path.relative_to(root).as_posix()
    except ValueError as exc:
        raise ValueError("path is outside the repository root") from exc
    return _normalize_relative_path(relative)


def _resource_id(relative_path: str) -> str:
    # The path remains the observed evidence. The identifier preserves its
    # case and path shape, which requires the shared identifier contract to
    # accept repository-relative path characters.
    return f"resource:{relative_path}"


def _checksum(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _snapshot(config: InventoryConfig) -> dict:
    identity = {
        "repository": config.repository,
        "ref": config.ref,
        "commit_sha": config.commit_sha,
        "captured_at": config.captured_at,
    }
    digest = hashlib.sha256(
        json.dumps(identity, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()[:32]
    snapshot = {
        "contract": {
            "name": "knowledge-guardian-repository-snapshot",
            "version": CONTRACT_VERSION,
        },
        "snapshot_id": f"snapshot:{digest}",
        "repository": config.repository,
        "ref": config.ref,
        "captured_at": config.captured_at,
    }
    if config.commit_sha is not None:
        snapshot["commit_sha"] = config.commit_sha
    return snapshot


def _diagnostic(
    code: str,
    level: str,
    path: Optional[str],
    operation: str,
    message: str,
    cause_type: Optional[str] = None,
) -> DiscoveryDiagnostic:
    return DiscoveryDiagnostic(code, level, path, operation, message, cause_type)


def _validate_config(config: InventoryConfig, filesystem: LocalFileSystem) -> Path:
    root = Path(config.repository_root)
    if not root.is_absolute():
        raise ValueError("repository_root must be an absolute path")
    if not config.repository or not config.ref or not config.captured_at:
        raise ValueError("repository, ref and captured_at are required")
    if config.follow_symlinks:
        raise ValueError("follow_symlinks cannot be enabled in KG-003")
    extensions = tuple(extension.lower() for extension in config.include_extensions)
    if not extensions or any(not extension.startswith(".") for extension in extensions):
        raise ValueError("include_extensions must contain dot-prefixed extensions")
    for ignore_path in config.ignore_paths:
        _normalize_relative_path(ignore_path)
    resolved = filesystem.resolve_root(root)
    if not resolved.is_dir():
        raise ValueError("repository_root must resolve to a directory")
    return resolved


def _ignored(relative_path: str, ignore_paths: set[str]) -> bool:
    return any(
        relative_path == ignored or relative_path.startswith(f"{ignored}/")
        for ignored in ignore_paths
    )


def inventory_markdown_resources(
    config: InventoryConfig,
    *,
    filesystem: Optional[LocalFileSystem] = None,
) -> InventoryResult:
    """Inventory supported Markdown resources beneath an explicit root."""

    fs = filesystem or LocalFileSystem()
    root = _validate_config(config, fs)
    snapshot = _snapshot(config)
    diagnostics: list[DiscoveryDiagnostic] = []
    resources: list[dict] = []
    ignore_paths = {_normalize_relative_path(path) for path in config.ignore_paths}
    extensions = {extension.lower() for extension in config.include_extensions}
    started = time.perf_counter()
    files_examined = 0

    for current, directories, files in fs.walk(root):
        current_relative = _relative_path(root, current)
        kept_directories: list[str] = []
        for directory in directories:
            candidate = f"{current_relative}/{directory}" if current_relative else directory
            candidate = _normalize_relative_path(candidate)
            directory_path = current / directory
            if fs.is_symlink(directory_path):
                diagnostics.append(
                    _diagnostic("SYMLINK_IGNORED", "info", candidate, "enumerate", "Symlink ignored")
                )
                continue
            if candidate == ".git" or candidate.startswith(".git/"):
                diagnostics.append(
                    _diagnostic("PATH_IGNORED", "info", candidate, "enumerate", "Path ignored")
                )
                continue
            if not config.include_hidden_directories and directory.startswith("."):
                diagnostics.append(
                    _diagnostic("PATH_IGNORED", "info", candidate, "enumerate", "Hidden path ignored")
                )
                continue
            if _ignored(candidate, ignore_paths):
                diagnostics.append(
                    _diagnostic("PATH_IGNORED", "info", candidate, "enumerate", "Path ignored")
                )
                continue
            kept_directories.append(directory)
        directories[:] = kept_directories

        for filename in files:
            files_examined += 1
            candidate_path = current / filename
            try:
                relative_path = _relative_path(root, candidate_path)
            except ValueError:
                diagnostics.append(
                    _diagnostic(
                        "PATH_OUTSIDE_ROOT",
                        "error",
                        None,
                        "normalize",
                        "Path is outside the repository root",
                    )
                )
                continue
            if fs.is_symlink(candidate_path):
                diagnostics.append(
                    _diagnostic("SYMLINK_IGNORED", "info", relative_path, "enumerate", "Symlink ignored")
                )
                continue
            if _ignored(relative_path, ignore_paths) or relative_path == ".git":
                diagnostics.append(
                    _diagnostic("PATH_IGNORED", "info", relative_path, "enumerate", "Path ignored")
                )
                continue
            if Path(filename).suffix.lower() not in extensions:
                diagnostics.append(
                    _diagnostic(
                        "UNSUPPORTED_EXTENSION",
                        "info",
                        relative_path,
                        "enumerate",
                        "File extension is outside the configured inventory",
                    )
                )
                continue
            try:
                metadata = fs.stat(candidate_path)
                if not stat_module.S_ISREG(metadata.st_mode):
                    diagnostics.append(
                        _diagnostic("PATH_IGNORED", "info", relative_path, "stat", "Non-regular file ignored")
                    )
                    continue
            except OSError as exc:
                diagnostics.append(
                    _diagnostic("FILE_STAT_FAILED", "warning", relative_path, "stat", "File metadata unavailable", type(exc).__name__)
                )
                continue
            try:
                content = fs.read_bytes(candidate_path)
            except OSError as exc:
                diagnostics.append(
                    _diagnostic("FILE_UNREADABLE", "warning", relative_path, "read", "File could not be read", type(exc).__name__)
                )
                continue
            resource = {
                "contract": {"name": "knowledge-guardian-resource", "version": CONTRACT_VERSION},
                "resource_id": _resource_id(relative_path),
                "snapshot_id": snapshot["snapshot_id"],
                "path": relative_path,
                "format": "markdown",
                "size_bytes": metadata.st_size,
            }
            if config.calculate_checksum:
                try:
                    resource["checksum"] = f"sha256:{_checksum(content)}"
                except Exception as exc:  # pragma: no cover - defensive boundary for injected filesystems
                    diagnostics.append(
                        _diagnostic("CHECKSUM_FAILED", "error", relative_path, "checksum", "Checksum failed", type(exc).__name__)
                    )
                    continue
            resources.append(resource)

    resources.sort(key=lambda item: item["path"])
    diagnostics.sort(key=lambda item: (item.path or "", item.code, item.operation))
    diagnostic_codes = (
        "PATH_IGNORED", "SYMLINK_IGNORED", "UNSUPPORTED_EXTENSION", "PATH_OUTSIDE_ROOT",
        "PATH_NORMALIZATION_FAILED", "FILE_UNREADABLE", "FILE_STAT_FAILED", "CHECKSUM_FAILED",
    )
    counts = {code: sum(item.code == code for item in diagnostics) for code in diagnostic_codes}
    summary = {
        "files_examined": files_examined,
        "resources_emitted": len(resources),
        "ignored_paths": counts["PATH_IGNORED"],
        "unreadable_files": counts["FILE_UNREADABLE"],
        "symlinks_ignored": counts["SYMLINK_IGNORED"],
        "checksum_failures": counts["CHECKSUM_FAILED"],
        "duration_ms": int((time.perf_counter() - started) * 1000),
        "diagnostic_counts": counts,
    }
    return InventoryResult(snapshot, resources, diagnostics, summary)
