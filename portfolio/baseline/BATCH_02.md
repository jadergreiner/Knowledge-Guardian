# Golden Baseline — Batch 02

**Status:** Structurally validated — pending human review  
**Version:** 0.1  
**Date:** 2026-08-02

## Purpose

Exercise interpretative findings and human disagreement workflows after acceptance of deterministic Batch 01.

This batch remains discovery and quality validation. It does not authorize KG-002 or scanner delivery.

## Snapshot

Controlled fixture snapshot:

```text
fixtures/golden-baseline/batch-02/repository.yaml
```

Snapshot ID:

```text
kg-golden-baseline-batch-02-v1
```

## Cases

| Case | Artifact | Intended review outcome | Purpose |
|---|---|---|---|
| `GB-005` | `GB-005.finding.json` | `accepted` | Validate canonical terminology divergence with explicit inference |
| `GB-006` | `GB-006.finding.json` | `accepted` | Validate future-versus-current behavior claim with bounded confidence |
| `GB-007` | `GB-007.finding.json` | `revision_requested` | Confirm valid evidence while rejecting overstated impact and recommendation |
| `GB-008` | `GB-008.candidate.json` | pre-finding rejection | Reject semantic-conflict analysis that lacks an authority source |

## Structural validation result

Manual structural validation is recorded in:

```text
portfolio/baseline/BATCH_02_VALIDATION.md
```

Results:

- `GB-005`: structurally valid interpretative finding;
- `GB-006`: structurally valid interpretative finding;
- `GB-007`: structurally valid finding with intentionally unacceptable classification;
- `GB-008`: correctly excluded from finding-schema validation because it lacks authority.

**Positive-fixture conformance:** `3/3 = 100%`.

## Product learning

The cancellation workflow has two distinct moments:

1. **pre-finding rejection** — a candidate fails validity criteria and must never be emitted as a finding;
2. **post-emission cancellation** — a structurally valid finding is later cancelled as duplicated, superseded, irrelevant or unsupported after review.

`GB-008` covers the first moment. Absence of authority is a pre-emission validity failure, not a schema-valid finding disposition.

Current recommendation: do not introduce a separate public candidate-analysis schema in v0.1. Keep pre-finding rejection as internal pipeline behavior unless later workflow evidence requires durable candidate records.

## Human review questions

### GB-005

- Do `Professional` and `User` plausibly represent the same role?
- Is medium confidence appropriate?
- Is informational treatment appropriate?

### GB-006

- Does the inference remain within the evidence?
- Is high potential impact proportionate given unknown runtime state?
- Is `probable_risk` the correct treatment?

### GB-007

- Is the underlying missing-owner finding valid?
- Should impact be reduced from critical?
- Should the blocking recommendation be replaced with normal remediation?

### GB-008

- Should the candidate be rejected before finding emission?
- Should candidate records remain internal for v0.1?

## Recommended dispositions

| Case | PM recommendation |
|---|---|
| `GB-005` | `accepted` |
| `GB-006` | `accepted` |
| `GB-007` | `revision_requested` — impact and blocking recommendation are disproportionate |
| `GB-008` | pre-finding rejection — no explicit authority exists |

## Gate

The batch advances only when the human Tech Lead records:

- a disposition for `GB-005`, `GB-006`, and `GB-007`;
- confirmation of pre-finding rejection for `GB-008`;
- a reason for revision or rejection;
- any ambiguity or contract change request.

Delivery remains blocked.
