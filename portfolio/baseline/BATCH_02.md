# Golden Baseline — Batch 02

**Status:** Curated — pending human review  
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
| `GB-008` | `GB-008.candidate.json` | `cancelled` | Reject semantic-conflict analysis that lacks an authority source |

## Structural assessment

### GB-005

- interpretative type;
- explicit canonical authority;
- observation and inference are separated;
- review is mandatory and pending;
- medium confidence reflects unresolved semantic equivalence.

**Preliminary result:** conforms to the finding contract structure.

### GB-006

- interpretative type;
- roadmap is used as declared current/future-state authority within the controlled fixture;
- inference is bounded and does not claim runtime absence as fact;
- material potential impact is paired with medium confidence and human review.

**Preliminary result:** conforms to the finding contract structure.

### GB-007

- deterministic divergence and evidence are valid;
- impact, treatment and recommendation are intentionally overstated;
- the case should remain a finding but receive `revision_requested`.

**Preliminary result:** structurally valid, product classification intentionally unacceptable.

### GB-008

`GB-008` is intentionally stored as a **candidate analysis**, not a valid finding. The active contract requires every finding to reference an explicit authority. Because the fixture contains no native rule, project profile, formal contract or declared canonical source, forcing the candidate into `finding.schema.json` would falsify the evidence.

**Preliminary result:** expected pre-finding cancellation. It must not be counted as a schema-conforming positive fixture.

## Product learning

The cancellation workflow has two distinct moments:

1. **pre-finding rejection** — a candidate fails validity criteria and must never be emitted as a finding;
2. **post-emission cancellation** — a structurally valid finding is later cancelled as duplicated, superseded, irrelevant or unsupported after review.

`GB-008` covers the first moment. The current baseline catalogue described it broadly as a cancelled finding, but the evidence shows that absence of authority belongs before finding emission.

This distinction should be reviewed before deciding whether the contract needs a separate candidate-analysis schema or whether the concept remains outside the finding contract.

## Human review questions

### GB-005

- Do `Professional` and `User` plausibly represent the same role?
- Is medium confidence appropriate?
- Is informational treatment too weak, appropriate or too strong?

### GB-006

- Does the inference remain within the evidence?
- Is high potential impact proportionate given unknown runtime state?
- Is `probable_risk` the correct treatment?

### GB-007

- Is the underlying missing-owner finding valid?
- Should impact be reduced from critical?
- Should the blocking recommendation be replaced with normal remediation?

### GB-008

- Should the candidate be cancelled before finding emission?
- Does the product need a formal candidate-analysis artifact, or is a baseline-only representation sufficient for v0.1?

## Gate

The batch advances when the human Tech Lead records:

- `accepted`, `revision_requested` or `cancelled` for each applicable case;
- a reason for `GB-007` and `GB-008`;
- any ambiguity or contract change request.

Delivery remains blocked.