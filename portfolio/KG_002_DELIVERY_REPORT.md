# KG-002 — Contract Delivery Report

**Status:** Implemented on delivery branch — executable validation pending  
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

An attempt was made to clone the delivery branch into the execution environment and run the validator. The environment could not resolve `github.com`:

```text
fatal: unable to access 'https://github.com/jadergreiner/Knowledge-Guardian.git/':
Could not resolve host: github.com
```

Therefore:

- executable contract validation is **not yet proven**;
- no claim of `14/14` passing fixtures is made;
- the failure is recorded as an environment/network limitation, not as a contract result;
- the Tech Lead quality gate remains open.

## Static contract review

The delivered contracts preserve the approved boundaries:

- repository-relative paths reject Unix absolute paths, Windows drive paths, backslashes and parent traversal;
- `unknown` is valid for type, layer, provenance and confidence where uncertainty is legitimate;
- observed metadata remains separate from normalized metadata and classifications;
- unsupported additional properties are rejected in contract-owned structures;
- schema references are local and version-scoped;
- no scanner, parser, traversal, finding or report behavior was introduced.

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

1. the runner executes successfully in a network-capable checkout or CI environment;
2. all valid fixtures pass;
3. all invalid fixtures fail for intended boundaries;
4. local schema references resolve deterministically;
5. unexpected failures are zero;
6. the Tech Lead records a quality disposition.

KG-003 remains blocked.