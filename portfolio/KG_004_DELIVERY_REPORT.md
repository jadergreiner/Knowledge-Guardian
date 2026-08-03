# KG-004 — Reachability Delivery Report

**Status:** Ready for review
**Date:** 2026-08-03
**Branch:** `feature/kg-004-shaping`
**Implementation commit:** `2c91529`
**Authorized disposition:** `approved_for_implementation`

## Scope delivered

- caller-supplied `ReachabilityConfig` for profile entries, exact native conventions and exclusions;
- schema validation of caller-supplied `Relationship` records against `relationship.schema.json@0.1.0`;
- bounded entry-point emission for `project_profile` and `native_convention`;
- deterministic reachability over internal `links_to` relationships with `explicit_link` provenance;
- states `reachable`, `candidate_orphan`, `excluded`, `not_evaluated`, `indeterminate` and `no_entry_point`;
- bounded diagnostics for invalid, missing, mismatched and conflicting evidence;
- deterministic shortest-path evidence and tie-breaking;
- no parser, link extraction, findings, reports, graph persistence or KG-005 behavior.

## Evidence

Commands executed:

```text
python -m unittest discover -s tests -p 'test_kg00*.py'
python tests/validate_document_model_contracts.py
git diff --check
```

Results:

- 12 tests passed: 7 KG-003 regression tests and 5 KG-004 tests;
- KG-002 contract regression: 14 valid passed, 14 invalid rejected, 0 unexpected;
- bounded runtime sample: 72 files examined, 30 resources emitted;
- runtime sample reachability: 1 resolved native entry point, 30 resources evaluated, 29 `candidate_orphan`, 1 `reachable`;
- absolute-path leakage check: false;
- no relationship extraction executed.

## Acceptance and limitations

The delivered slice consumes an explicit relationship iterable supplied by the caller. An eventual parser/producer remains outside this increment and belongs to separately shaped KG-005 work.

The conceptual model still describes fields not required by the executable relationship schema (`authority_reference`, `confidence`, `target_exists`). This compatibility gap is documented and not silently changed.

Rollback is a branch/commit reversal; no persistent runtime state or repository file mutation was introduced.

**Recommendation:** `approved_for_review`; merge remains subject to human Tech Lead quality acceptance.
