# Golden Baseline — Batch 01

**Status:** Structurally validated — pending human review  
**Version:** 0.2  
**Date:** 2026-08-02

## Purpose

Exercise the hardened finding contract with four deterministic normative cases before interpretative cases or scanner delivery begin.

## Snapshot decision

The repository state used to anchor product and contract context is:

```text
aafb24cade649753b6f525600808b3a06a440270
```

The repository did not yet contain enough explicit project policies and intentionally invalid artifacts to produce all four normative cases without inventing authority. Therefore, Batch 01 uses a controlled, versioned fixture snapshot stored at:

```text
fixtures/golden-baseline/batch-01/repository.yaml
```

This fixture decision preserves reproducibility and prevents aspirational README examples from being treated as observed repository failures.

## Curated cases

| Case | Rule authority | Expected finding | Fixture |
|---|---|---|---|
| GB-001 | Native rule `KG-LINK-001` | Broken internal Markdown reference | `GB-001.finding.json` |
| GB-002 | Project profile `KG-META-001` | Missing required owner metadata | `GB-002.finding.json` |
| GB-003 | Formal contract `KG-SCHEMA-001` | Enum violation against declared JSON Schema | `GB-003.finding.json` |
| GB-004 | Project profile `KG-ENTRY-001` | Missing configured repository entry point | `GB-004.finding.json` |

All four findings:

- declare contract `knowledge-guardian-finding@0.1.0`;
- use deterministic fingerprints;
- contain explicit authority;
- identify exact or justified location;
- separate evidence from analysis observation;
- retain human disposition as `pending_review`;
- make recommendations without authorizing automatic modification.

## Structural validation result

The four fixtures were manually reviewed against `schemas/finding.schema.json`.

| Case | Result |
|---|---|
| GB-001 | Structurally valid |
| GB-002 | Structurally valid |
| GB-003 | Structurally valid |
| GB-004 | Structurally valid |

**Structural conformance rate:** `100%`.

Detailed evidence is recorded in:

```text
portfolio/baseline/BATCH_01_VALIDATION.md
```

This result is manual structural evidence. Automated schema execution and regression protection remain pending.

## Product assessment

### Supported

- the contract can structurally represent all four intended deterministic authority patterns in this batch;
- missing-resource findings can use `location.scope: not_available` with a reason;
- evidence, impact, confidence, treatment and recommendation remain structurally distinct;
- controlled fixtures are necessary while the live repository lacks deliberate invalid states;
- all four fixtures are ready for human product review.

### Not yet demonstrated

- automated JSON Schema execution;
- policy-level coherence between impact, confidence and treatment;
- human acceptance of impact and recommendations;
- stable fingerprint generation by implementation;
- scanner ability to discover the same evidence;
- interpretative and negative-case behavior.

## Review rubric

The human Tech Lead should evaluate each case for:

1. correctness of observation;
2. applicability of authority;
3. proportionality of impact;
4. coherence of confidence and treatment;
5. usefulness and safety of recommendation.

Allowed decisions remain:

- `accepted`;
- `revision_requested`;
- `cancelled`.

A reason is required for revision or cancellation.

## Gate

Batch 01 does not authorize KG-002 or scanner implementation.

The remaining gate requires:

1. obtain human review decisions for GB-001 through GB-004;
2. log ambiguity or contract gaps;
3. update KG-001 and KG-010 status;
4. decide whether to continue with interpretative and negative cases, revise the contract, or reshape the baseline.
