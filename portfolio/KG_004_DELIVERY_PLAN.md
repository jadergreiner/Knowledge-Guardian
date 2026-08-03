# KG-004 — Reachability Delivery Plan

**Status:** Approved for planning — implementation authorization pending
**Version:** 0.1
**Date:** 2026-08-03
**Shaping:** `portfolio/KG_004_SHAPING.md`
**Relationship input shaping:** `portfolio/KG_004_RELATIONSHIP_INPUT_SHAPING.md`
**Depends on:** merged KG-003 inventory and KG-002 EntryPoint/Resource contracts

## 1. Delivery objective

Produce deterministic, read-only reachability evidence from the KG-003 inventory, resolved entry points and an externally supplied set of explicit internal relationships.

The output may contain `reachable`, `candidate_orphan`, `excluded`, `not_evaluated`, `indeterminate` and `no_entry_point` evidence. `candidate_orphan` is a review candidate, never a confirmed orphan and never a finding.

## 2. Authorized scope for the proposed slice

### Included

- accept a KG-003 `RepositorySnapshot` and its resources;
- resolve entry points using `project_profile` first, exact root native conventions second and explicit `no_entry_point` evidence otherwise;
- preserve multiple entry points and record profile/convention conflicts without automatic selection;
- accept externally supplied typed relationships without discovering or validating them;
- calculate reachability only over resources and supplied relationships;
- emit deterministic per-resource state and bounded evidence paths;
- emit diagnostics for missing targets, invalid relationship references and incomplete evaluation;
- validate emitted `EntryPoint` records against the KG-002 schema;
- provide deterministic unit and integration tests.

### Excluded

- Markdown, MDX, YAML or front-matter parsing;
- link extraction, link validation or relationship discovery;
- canonical-source selection;
- findings, reports, graph persistence or CI/CD blocking;
- automatic file changes;
- external repository access or Git discovery;
- KG-005, KG-006 and later delivery items.

## 3. Input boundary

The delivery must require explicit inputs:

```text
RepositorySnapshot
Resource inventory
Project profile / entry-point declarations
Versioned native-convention configuration
Typed relationship set
```

The relationship set must follow the existing `relationship.schema.json` `0.1.0` contract and be supplied by an explicit caller-owned `RelationshipProvider`. A missing or invalid relationship input makes affected results `indeterminate`; it must not be treated as proof of orphanhood. KG-004 does not extract relationships.

## 4. Deterministic rules

- match native conventions by exact repository-relative path and casing;
- include only files present in the KG-003 inventory;
- let the profile add, remove or replace native conventions;
- preserve all valid entry points; do not infer canonicality;
- classify `candidate_orphan` only after complete evaluation with no structural error;
- select an evidence path by shortest distance, then `entry_point_id`, then lexicographic path sequence;
- sort emitted records and diagnostics by stable repository-relative identity and stable diagnostic code;
- never emit a finding for any reachability state.

## 5. Diagnostics and incomplete evidence

Diagnostics must be bounded, deterministic and repository-relative. At minimum, the plan must cover:

- configured entry point missing from inventory;
- duplicate or conflicting entry-point declarations;
- relationship source or target missing from inventory;
- malformed or duplicate relationship input;
- incomplete evaluation caused by an upstream error.

An affected resource becomes `indeterminate` or `not_evaluated` according to whether it was entered into the evaluation set. No incomplete `EntryPoint` or false `candidate_orphan` may be emitted.

## 6. Test and evidence plan

Tests must cover:

- empty inventory and `no_entry_point` evidence;
- profile entry points and profile replacement of conventions;
- exact root conventions and rejection of subdirectory/approximate matches;
- multiple entry points and deterministic conflict evidence;
- missing configured targets;
- valid, malformed, duplicate and incomplete relationship inputs;
- reachable path selection and tie-breaking;
- `candidate_orphan`, `excluded`, `not_evaluated` and `indeterminate` states;
- schema validation for every emitted `EntryPoint`;
- repeated-run determinism;
- KG-002 and KG-003 regression suites.

Required evidence includes test output, `git diff --check`, scope verification and a bounded runtime sample with no absolute-path leakage.

## 7. Rollback and observability

The delivery must remain read-only with no persistent runtime state. Rollback is branch/commit reversal only; no migration or external data mutation is authorized. Observability records counts by state and diagnostic code without document contents, stack traces or durable absolute paths.

## 8. Acceptance gate

Delivery may proceed only after a separate decision confirms:

1. reuse of `relationship.schema.json` `0.1.0` and the caller-supplied `RelationshipProvider`;
2. missing-target handling as diagnostic-only or another explicitly bounded behavior;
3. duplicate declaration handling;
4. the final native-convention version owner.

Approval must remain limited to reachability evidence. Parsing, relationship extraction, findings, reports and KG-005 remain blocked.

**Recorded disposition:** `approved_for_reachability_delivery_plan`.
