# Golden Baseline — Batch 02 Validation

**Status:** Structural validation complete — human review pending  
**Version:** 0.1  
**Date:** 2026-08-02

## Purpose

Record validation evidence for `GB-005` through `GB-008` against finding contract `knowledge-guardian-finding@0.1.0` and the product validity rules.

## Method

`GB-005.finding.json`, `GB-006.finding.json`, and `GB-007.finding.json` were reviewed field by field against `schemas/finding.schema.json`.

The review covered required fields, enums, conditional rules for interpretative findings, fingerprint format, location semantics, authority, additional-property restrictions, and mandatory human review.

`GB-008.candidate.json` was evaluated against the finding validity criteria rather than forced through the finding schema. It intentionally has no authority source and therefore is not a valid finding.

This is manual structural validation, not an automated regression test.

## Results

| Case | Artifact type | Schema result | Product validity result |
|---|---|---|---|
| `GB-005` | Interpretative finding | Structurally valid | Pending human review |
| `GB-006` | Interpretative finding | Structurally valid | Pending human review |
| `GB-007` | Normative finding | Structurally valid | Classification intentionally requires revision |
| `GB-008` | Candidate analysis | Not applicable | Correctly rejected before finding emission |

**Positive-fixture structural conformance:** `3 / 3 = 100%`.

## Case notes

### GB-005

- canonical authority is explicit;
- observation and inference are structurally separated;
- inference contains statement and rationale;
- interpretative review is required;
- medium confidence is allowed;
- all fields conform to contract `0.1.0`.

### GB-006

- canonical current/future-state authority is explicit;
- observation does not claim runtime absence as fact;
- inference is bounded by unknown runtime state;
- review is mandatory;
- potential impact and medium confidence are structurally valid.

### GB-007

- missing metadata evidence is deterministic and structurally valid;
- critical impact, confirmed-critical treatment, and blocking recommendation are allowed values;
- schema validity does not imply product classification quality;
- the fixture correctly demonstrates why human review and policy validation are required beyond JSON Schema.

### GB-008

- no authority source exists;
- the finding contract requires authority for every emitted finding;
- the candidate must be rejected before finding creation;
- counting it as a schema failure would be incorrect because suppression is the intended result.

## Evidence supported

- interpretative findings can express explicit inference and mandatory review;
- the contract can structurally represent a finding whose classification is later revised by a human;
- schema validation and product acceptance are distinct controls;
- invalid candidates should be suppressed before finding emission when authority is absent.

## Open product question

The baseline now distinguishes:

1. pre-finding rejection of an invalid candidate;
2. post-emission cancellation of a validly structured finding.

The current evidence does not justify adding a second public candidate-analysis contract in v0.1. The distinction may remain an internal pipeline rule unless later workflow evidence shows a need for durable candidate records.

## Remaining gate

The human Tech Lead must decide:

- `GB-005`: accept, request revision, or cancel;
- `GB-006`: accept, request revision, or cancel;
- `GB-007`: confirm `revision_requested` and state the correction required;
- `GB-008`: confirm pre-finding rejection and whether candidate records remain internal for v0.1.

Delivery remains blocked until these decisions and any resulting ambiguity records are captured.
