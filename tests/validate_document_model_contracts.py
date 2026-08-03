#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas" / "document-model" / "0.1.0"
FIXTURE_DIR = ROOT / "fixtures" / "document-model" / "0.1.0"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    registry = Registry()
    schemas = {}
    for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        schema = load(path)
        schemas[path.name] = schema
        registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
        registry = registry.with_resource(path.name, Resource.from_contents(schema))

    valid_passed = invalid_rejected = unexpected = 0
    for fixture_path in sorted(FIXTURE_DIR.glob("*.cases.json")):
        suite = load(fixture_path)
        schema = schemas[suite["schema"]]
        validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
        for case in suite["valid"]:
            errors = list(validator.iter_errors(case))
            if errors:
                unexpected += 1
                print(f"UNEXPECTED VALID FAILURE {fixture_path.name}: {errors[0].message}")
            else:
                valid_passed += 1
        for case in suite["invalid"]:
            errors = list(validator.iter_errors(case["value"]))
            if errors:
                invalid_rejected += 1
            else:
                unexpected += 1
                print(f"UNEXPECTED INVALID PASS {fixture_path.name}: {case['name']}")

    print(json.dumps({"valid_passed": valid_passed, "invalid_rejected": invalid_rejected, "unexpected": unexpected}, indent=2))
    return 1 if unexpected else 0


if __name__ == "__main__":
    raise SystemExit(main())
