from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from knowledge_guardian.discovery import InventoryConfig, LocalFileSystem, inventory_markdown_resources


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "document-model" / "0.1.0"


def validators() -> tuple[Draft202012Validator, Draft202012Validator]:
    schemas = {
        path.name: json.loads(path.read_text(encoding="utf-8"))
        for path in SCHEMA_DIR.glob("*.schema.json")
    }
    registry = Registry()
    for name, schema in schemas.items():
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
        registry = registry.with_resource(name, Resource.from_contents(schema))
    return (
        Draft202012Validator(schemas["repository-snapshot.schema.json"], registry=registry, format_checker=FormatChecker()),
        Draft202012Validator(schemas["resource.schema.json"], registry=registry, format_checker=FormatChecker()),
    )


def config(root: Path, **overrides) -> InventoryConfig:
    values = {
        "repository_root": root,
        "repository": "jadergreiner/Knowledge-Guardian",
        "ref": "main",
        "captured_at": "2026-08-02T23:00:00-03:00",
    }
    values.update(overrides)
    return InventoryConfig(**values)


class FailingReadFileSystem(LocalFileSystem):
    def read_bytes(self, path: Path) -> bytes:
        if path.name == "Unreadable.md":
            raise OSError("permission denied")
        return super().read_bytes(path)


class SymlinkMarkedFileSystem(LocalFileSystem):
    def is_symlink(self, path: Path) -> bool:
        return path.name == "link.md"


class FailingStatFileSystem(LocalFileSystem):
    def stat(self, path: Path):
        if path.name == "StatFail.md":
            raise OSError("stat failed")
        return super().stat(path)


class KG003DiscoveryTests(unittest.TestCase):
    def test_inventory_is_filtered_sorted_and_schema_valid(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("readme", encoding="utf-8")
            (root / "docs").mkdir()
            (root / "docs" / "Guide.MDX").write_text("guide", encoding="utf-8")
            (root / ".github").mkdir()
            (root / ".github" / "workflow.md").write_text("workflow", encoding="utf-8")
            (root / ".git").mkdir()
            (root / ".git" / "ignored.md").write_text("ignored", encoding="utf-8")
            (root / "notes.txt").write_text("not inventoried", encoding="utf-8")

            result = inventory_markdown_resources(config(root))
            snapshot_validator, resource_validator = validators()

            self.assertEqual([item["path"] for item in result.resources], [
                ".github/workflow.md", "README.md", "docs/Guide.MDX"
            ])
            self.assertEqual(result.summary["resources_emitted"], 3)
            self.assertEqual(result.summary["symlinks_ignored"], 0)
            self.assertFalse(any(item["path"] == ".git/ignored.md" for item in result.resources))
            self.assertFalse(list(snapshot_validator.iter_errors(result.snapshot)))
            for resource in result.resources:
                self.assertFalse(list(resource_validator.iter_errors(resource)), resource)
            self.assertTrue(all("/" not in diagnostic.message or "\\" not in diagnostic.message for diagnostic in result.diagnostics))

    def test_checksum_can_be_disabled_and_context_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_bytes(b"content")
            result = inventory_markdown_resources(config(root, calculate_checksum=False, commit_sha="a1b2c3d"))

            self.assertEqual(result.snapshot["commit_sha"], "a1b2c3d")
            self.assertNotIn("checksum", result.resources[0])
            self.assertEqual(result.resources[0]["size_bytes"], 7)

    def test_ignore_paths_and_invalid_configuration_are_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "ignored.md").write_text("ignored", encoding="utf-8")
            (root / "keep.md").write_text("keep", encoding="utf-8")
            result = inventory_markdown_resources(config(root, ignore_paths=("docs",)))

            self.assertEqual([item["path"] for item in result.resources], ["keep.md"])
            self.assertTrue(any(item.code == "PATH_IGNORED" for item in result.diagnostics))
            with self.assertRaises(ValueError):
                inventory_markdown_resources(config(root, follow_symlinks=True))
            with self.assertRaises(ValueError):
                inventory_markdown_resources(config(root, repository_root=Path("relative")))

    def test_unreadable_file_does_not_abort_other_resources(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Unreadable.md").write_text("secret", encoding="utf-8")
            (root / "Readable.md").write_text("readable", encoding="utf-8")
            result = inventory_markdown_resources(config(root), filesystem=FailingReadFileSystem())

            self.assertEqual([item["path"] for item in result.resources], ["Readable.md"])
            self.assertEqual(result.summary["unreadable_files"], 1)
            self.assertEqual([item.code for item in result.diagnostics], ["FILE_UNREADABLE"])

    def test_repeated_runs_have_equivalent_records_except_duration(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("stable", encoding="utf-8")
            first = inventory_markdown_resources(config(root)).to_dict()
            second = inventory_markdown_resources(config(root)).to_dict()
            first["summary"].pop("duration_ms")
            second["summary"].pop("duration_ms")
            self.assertEqual(first, second)

    def test_symlink_is_ignored_without_platform_specific_filesystem_setup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.md"
            target.write_text("target", encoding="utf-8")
            link = root / "link.md"
            link.write_text("link", encoding="utf-8")
            result = inventory_markdown_resources(config(root), filesystem=SymlinkMarkedFileSystem())

            self.assertEqual([item["path"] for item in result.resources], ["target.md"])
            self.assertEqual(result.summary["symlinks_ignored"], 1)

    def test_stat_and_checksum_failures_are_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "StatFail.md").write_text("stat", encoding="utf-8")
            (root / "ChecksumFail.md").write_bytes(b"checksum")
            (root / "Readable.md").write_text("readable", encoding="utf-8")

            def checksum(content: bytes) -> str:
                if content == b"checksum":
                    raise OSError("checksum failed")
                return "0" * 64

            with patch("knowledge_guardian.discovery._checksum", side_effect=checksum):
                result = inventory_markdown_resources(config(root), filesystem=FailingStatFileSystem())

            self.assertEqual([item["path"] for item in result.resources], ["Readable.md"])
            self.assertEqual(result.summary["diagnostic_counts"]["FILE_STAT_FAILED"], 1)
            self.assertEqual(result.summary["diagnostic_counts"]["CHECKSUM_FAILED"], 1)


if __name__ == "__main__":
    unittest.main()
