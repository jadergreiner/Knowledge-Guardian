# Golden Baseline — Batch 02

**Status:** Human-reviewed — gate closed  
**Version:** 0.2  
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

## Structural validation

Manual validation is recorded in `portfolio/baseline/BATCH_02_VALIDATION.md`.

- positive fixtures: `GB-005`, `GB-006`, `GB-007`;
- structural conformance: `3/3 = 100%`;
- `GB-008` is outside the finding schema because it lacks authority.

## Human decisions

**Reviewer:** Jader Raul Greiner — Human Tech Lead  
**Reviewed at:** 2026-08-02T22:33:00-03:00

| Case | Decision | Result |
|---|---|---|
| `GB-005` | `accepted` | Canonical-term divergence, medium confidence and informational treatment accepted |
| `GB-006` | `accepted` | Future-versus-current interpretation and bounded uncertainty accepted |
| `GB-007` | `revision_requested` | Divergence accepted; critical impact, urgent treatment and global blocking rejected as disproportionate |
| `GB-008` | `rejected_before_finding_emission` | Candidate has no explicit authority and must not become a finding |

## Revision learning from GB-007

The case confirms that schema conformance is necessary but insufficient.

The valid observation is:

```text
The required owner field is absent.
```

The rejected classification asserted repository-wide critical governance failure and recommended blocking all changes. The Tech Lead requested revision because those conclusions exceed the available evidence.

The expected corrected direction is:

- bounded potential governance impact;
- normal remediation or backlog treatment;
- no repository-wide blocking recommendation.

The intentionally overstated fixture remains versioned with `review.status: revision_requested` as baseline evidence. It must not be silently rewritten into an accepted finding.

## Candidate-analysis decision

Candidate analysis remains **internal-only in v0.1**.

The product distinguishes:

1. **pre-finding rejection** — validity criteria fail before emission;
2. **post-emission cancellation** — a valid emitted finding is later cancelled by a human.

`GB-008` covers pre-finding rejection. No public candidate schema will be added in v0.1 without further workflow evidence.

## Batch result

```text
Positive fixture conformance: 3/3 — 100%
Accepted findings:           2
Revision requested:          1
Pre-finding rejections:      1
Contract-breaking gaps:      0
Product-learning decisions:  2
```

## Gate outcome

Batch 02 is complete.

Authorized next increment:

- curate `GB-009` through `GB-012` as expected non-findings;
- document suppression rationale and false-positive protection;
- do not start KG-002 or scanner implementation.
