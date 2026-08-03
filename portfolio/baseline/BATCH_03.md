# Golden Baseline — Batch 03

**Status:** Curated — pending human review  
**Version:** 0.1  
**Date:** 2026-08-02

## Purpose

Exercise expected non-findings and false-positive protection after deterministic and interpretative baseline cases.

This batch remains discovery and quality validation. It does not authorize KG-002 or scanner delivery.

## Snapshot

Controlled fixture snapshot:

```text
fixtures/golden-baseline/batch-03/repository.yaml
```

Snapshot ID:

```text
kg-golden-baseline-batch-03-v1
```

## Cases

| Case | Expected result | Suppression principle |
|---|---|---|
| `GB-009` | `no_finding` | Alternative wording without explicit terminology authority is not a violation |
| `GB-010` | `no_finding` | Future-state documentation does not prove or deny current runtime behavior |
| `GB-011` | `no_finding` | Explicit project-profile exemption prevents an orphan-document finding |
| `GB-012` | `no_finding` | Matching stable fingerprint suppresses duplicate emission |

## Product assessment

### GB-009 — Undocumented wording preference

Two documents use `Professional` and `User`, but no rule or canonical source establishes one required term or proves semantic identity.

**Suppression rationale:** Emitting a semantic inconsistency would convert an undocumented preference into a finding.

### GB-010 — Aspirational documentation

A vision document states that pull-request blocking will exist in the future.

**Suppression rationale:** The statement does not claim that the capability is active. Absence of runtime evidence must not be treated as evidence of contradiction.

### GB-011 — Intentional standalone document

The resource is not reachable through navigation, but the project profile explicitly exempts it with a reason.

**Suppression rationale:** The exemption is applicable authority and prevents a false orphan-document finding.

### GB-012 — Duplicate candidate

The candidate and an active finding share the same stable fingerprint.

**Suppression rationale:** The existing finding represents the logical issue. A second emission would inflate report volume and corrupt lifecycle tracking.

## Measurement

All four cases are expected non-findings.

```text
negative_case_pass_rate = correctly_suppressed_cases / 4
```

The target for this manually curated batch is `4/4 = 100%` after human review.

## Human review questions

For each case, the Tech Lead should decide whether the suppression rationale is correct and sufficient.

Allowed review outcomes for Batch 03:

- `confirmed_non_finding`;
- `revision_requested`;
- `finding_expected`.

A reason is required when the expected suppression is rejected or requires revision.

## Known limitation

These artifacts document expected behavior. They do not prove that an implemented scanner or rule engine will suppress the cases correctly.

## Gate

The batch advances when:

1. the human Tech Lead reviews `GB-009` through `GB-012`;
2. the negative-case pass rate is recorded;
3. false-positive or ambiguity findings are catalogued;
4. Product makes the final `KG-001` and `KG-010` decision;
5. authorization to shape `KG-002` is explicitly recorded or denied.

Delivery remains blocked until that final decision.