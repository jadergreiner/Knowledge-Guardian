# Golden Baseline — Batch 01 Validation

**Status:** Structural validation complete — human review pending  
**Version:** 0.1  
**Date:** 2026-08-02

## Purpose

Record the validation evidence for `GB-001` through `GB-004` against `schemas/finding.schema.json` contract version `0.1.0`.

## Method

The four fixtures were reviewed field by field against the active JSON Schema on the repository default branch.

This was a manual structural validation. It verified required properties, enums, conditional requirements, additional-property restrictions, fingerprint format, location semantics, contract version, and review state.

It is not an automated regression test and does not prove that a future validator implementation will behave identically.

## Results

| Case | Contract | Required fields | Conditional rules | Additional properties | Result |
|---|---|---|---|---|---|
| `GB-001` | `0.1.0` | Pass | Pass | Pass | Structurally valid |
| `GB-002` | `0.1.0` | Pass | Pass | Pass | Structurally valid |
| `GB-003` | `0.1.0` | Pass | Pass | Pass | Structurally valid |
| `GB-004` | `0.1.0` | Pass | Pass | Pass | Structurally valid |

**Structural conformance rate:** `4 / 4 = 100%`.

## Validation notes

### GB-001

- normative finding;
- exact line location present;
- fingerprint matches the schema pattern;
- no inference is required for a normative finding;
- impact, confidence and treatment use allowed values.

### GB-002

- project-profile authority is explicit;
- exact front-matter section location is present;
- missing-field evidence is represented as structured observed and expected values;
- treatment is structurally valid.

### GB-003

- formal-contract authority is explicit;
- JSON Pointer satisfies exact-location requirements;
- enum evidence is represented without unsupported inference;
- known impact is permitted without an `impact.reason` field.

### GB-004

- absent subject uses `location.scope: not_available`;
- a reason is present as required for non-exact location scopes;
- evidence points to the exact profile section declaring the missing entry point;
- project-profile authority and treatment values are valid.

## What this evidence supports

- the hardened contract can structurally represent the first four deterministic cases;
- exact and justified non-exact location semantics work for the curated fixtures;
- the schema does not require interpretative inference for normative findings;
- all four fixtures can proceed to human product review.

## What this evidence does not support

- automated JSON Schema execution or regression protection;
- correctness of the underlying repository observations beyond the controlled fixtures;
- coherence of impact, confidence and treatment as a business policy;
- usefulness or proportionality of recommendations;
- acceptance of the cases by the human Tech Lead;
- validation of interpretative findings or expected non-findings.

## Remaining gate

The human Tech Lead must decide for each case:

- `accepted`;
- `revision_requested`;
- `cancelled`.

A reason is required for revision or cancellation. Delivery remains blocked until these decisions and any resulting ambiguity records are captured.
