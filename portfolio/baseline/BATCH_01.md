# Golden Baseline — Batch 01

**Status:** Human-reviewed — accepted  
**Version:** 0.2  
**Date:** 2026-08-02

## Purpose

Exercise the hardened finding contract with four deterministic normative cases before interpretative cases or scanner delivery begin.

## Snapshot decision

Repository anchor commit:

```text
aafb24cade649753b6f525600808b3a06a440270
```

Controlled fixture snapshot:

```text
fixtures/golden-baseline/batch-01/repository.yaml
```

The controlled snapshot was used because the live repository did not contain enough explicit policies and intentionally invalid artifacts to produce all four normative cases without inventing authority.

## Reviewed cases

| Case | Expected finding | Structural validation | Human disposition |
|---|---|---|---|
| `GB-001` | Broken internal Markdown reference | Pass | `accepted` |
| `GB-002` | Missing required owner metadata | Pass | `accepted` |
| `GB-003` | Enum violation against declared JSON Schema | Pass | `accepted` |
| `GB-004` | Missing configured repository entry point | Pass | `accepted` |

**Reviewer:** Jader Raul Greiner — Human Tech Lead  
**Reviewed at:** 2026-08-02T21:04:00-03:00

## Measurements

```text
structural_conformance_rate = 4 / 4 = 100%
reviewer_acceptance_rate = 4 / 4 = 100%
```

No revision request, cancellation, ambiguity or contract gap was recorded in this deterministic batch.

## Evidence supported

- contract `knowledge-guardian-finding@0.1.0` represents the four deterministic cases;
- native-rule, project-profile and formal-contract authorities are understandable and applicable;
- exact and justified non-exact locations are usable;
- impact, confidence, treatment and recommendation were accepted as proportional for these cases;
- proposal-first recommendations and human disposition remain distinct.

## Evidence not yet supported

- interpretative findings;
- expected non-findings and false-positive protection;
- revision-requested and cancelled workflows;
- automated schema regression;
- stable fingerprint generation by executable implementation;
- scanner discovery of the same evidence.

## Gate result

Batch 01 passed its structural and human-review gate.

This authorizes continuation of the golden baseline with interpretative, disagreement and negative cases. It does not authorize scanner implementation or mark `KG-001` fully validated.
