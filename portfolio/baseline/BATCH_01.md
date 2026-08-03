# Golden Baseline — Batch 01

**Status:** Curated — pending schema execution and human review  
**Version:** 0.1  
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

## Preliminary product assessment

### Supported

- the contract can represent all four intended deterministic authority types used in this batch;
- missing-resource findings can use `location.scope: not_available` with a reason;
- evidence, impact, confidence, treatment and recommendation remain structurally distinct;
- controlled fixtures are necessary while the live repository lacks deliberate invalid states.

### Not yet demonstrated

- executable conformance against `schemas/finding.schema.json`;
- policy-level coherence between impact, confidence and treatment;
- human acceptance of the impact and recommendations;
- stable fingerprint generation by implementation;
- scanner ability to discover the same evidence.

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

The next gate requires:

1. execute JSON Schema validation for all four finding fixtures;
2. record validation evidence;
3. obtain human review decisions;
4. log ambiguity or contract gaps;
5. update KG-001 and KG-010 status.
