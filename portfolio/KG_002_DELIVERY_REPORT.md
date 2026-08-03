# KG-002 — Contract Delivery Report

**Status:** Ready for Tech Lead quality review
**Version:** 0.1  
**Date:** 2026-08-02

## Scope delivered

The bounded KG-002 delivery slice contains:

- seven JSON Schema draft 2020-12 contracts;
- shared definitions for contract version, identifiers, confidence and repository-relative paths;
- two valid and two invalid fixture cases per contract;
- a deterministic Python validation runner using `jsonschema` and `referencing`;
- schema ownership, compatibility and local-validation documentation.

## Contracts

- `RepositorySnapshot`;
- `Resource`;
- `Classification`;
- `Document`;
- `Relationship`;
- `EntryPoint`;
- `Exception`.

## Fixture inventory

| Measure | Count |
|---|---:|
| Contract schemas | 7 |
| Valid fixtures | 14 |
| Invalid fixtures | 14 |
| Shared definition schemas | 1 |
| Validation runners | 1 |

## Intended validation command

```bash
python -m pip install jsonschema referencing
python tests/validate_document_model_contracts.py
```

Expected success output must report:

```json
{
  "valid_passed": 14,
  "invalid_rejected": 14,
  "unexpected": 0
}
```

## Execution evidence

Validation was executed locally on 2026-08-02 at `2026-08-02T23:21:44.7245755-03:00`.

| Field | Result |
|---|---|
| Operating system | Microsoft Windows 11 Pro |
| Python | 3.11.9 |
| jsonschema | 4.26.0 |
| referencing | 0.37.0 |
| Command | `python tests/validate_document_model_contracts.py` |
| Valid fixtures passed | 14 |
| Invalid fixtures rejected | 14 |
| Unexpected failures | 0 |
| Local reference resolution | Passed; 16 local registry entries, no external `$ref` |

The runner output was:

```json
{
  "valid_passed": 14,
  "invalid_rejected": 14,
  "unexpected": 0
}
```

Additional deterministic checks also passed:

- Unix and Windows absolute paths rejected;
- parent traversal rejected;
- incorrect contract version rejected;
- unknown enum rejected while formal `unknown` values remain supported;
- unsupported additional properties rejected;
- nested repository-relative identifiers accepted;
- all schemas and fixtures parsed as valid JSON and use draft 2020-12.

## Static contract review

The delivered contracts preserve the approved boundaries:

- repository-relative paths reject Unix absolute paths, Windows drive paths, backslashes and parent traversal;
- `unknown` is valid for type, layer, provenance and confidence where uncertainty is legitimate;
- observed metadata remains separate from normalized metadata and classifications;
- unsupported additional properties are rejected in contract-owned structures;
- schema references are local and version-scoped;
- no scanner, parser, traversal, finding or report behavior was introduced.

## Corrections applied

The shared identifier definition now accepts `/` so resource and document IDs derived from normalized repository-relative paths (for example, `resource:docs/architecture.md`) validate consistently with the approved model and existing valid fixtures. This is a corrective compatibility fix within `0.1.0`; it does not change path normalization rules.

## Ambiguities and limitations

- The model describes `document_id` as snapshot identity plus resource ID, while the current fixtures use the stable form `document:<relative-path>`. The isolated schema cannot enforce the cross-object identity composition; this remains an application-level decision for a future aggregate validator.
- Target document existence, collection uniqueness, document/resource path equality, rename continuity and repository path case policy remain application- or snapshot-level invariants.
- JSON Schema validates structure and local formats; it does not implement scanning, parsing, traversal, rule execution or finding generation.

## Known application-level invariants

The following cannot be fully enforced by isolated JSON Schema files and remain deferred to snapshot/application validation:

- target document existence;
- uniqueness across collections;
- document/resource path equality;
- rename continuity;
- case-sensitive path policy;
- cross-object identity integrity.

## Gate

KG-002 is not complete until:

1. the runner executes successfully;
2. all valid fixtures pass;
3. all invalid fixtures fail for intended boundaries;
4. local schema references resolve deterministically;
5. unexpected failures are zero;
6. the Tech Lead records a quality disposition.

KG-003 remains blocked.
