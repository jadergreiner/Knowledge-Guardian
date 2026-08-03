# Knowledge Guardian — v0.1 Golden Baseline Result

**Status:** Complete — product decision recorded  
**Version:** 0.1  
**Date:** 2026-08-02

## Scope

The baseline contains 12 reviewed cases across three controlled batches:

- `GB-001` through `GB-004`: deterministic normative findings;
- `GB-005` through `GB-008`: interpretative findings, revision workflow, and pre-finding rejection;
- `GB-009` through `GB-012`: expected non-findings and false-positive protection.

## Results

| Measure | Result |
|---|---:|
| Positive finding fixtures structurally valid | `7/7` |
| Accepted findings | `6` |
| Revision requested | `1` |
| Pre-finding rejection | `1` |
| Expected non-findings confirmed | `4/4` |
| Contract gaps requiring immediate schema revision | `0` |

### Positive-fixture conformance

```text
7 / 7 = 100%
```

### Negative-case protection

```text
4 / 4 = 100%
```

## Product conclusions

The reviewed evidence supports the following bounded conclusions:

1. Contract `knowledge-guardian-finding@0.1.0` can represent the curated normative and interpretative findings.
2. Human review can distinguish schema validity from classification quality, as demonstrated by `GB-007`.
3. Authority-less candidates must be rejected before finding emission.
4. Candidate analysis remains internal-only in v0.1.
5. Expected non-findings protect against undocumented preferences, unsupported runtime claims, ignored exemptions, and duplicate emission.

## Limitations

This baseline is manually curated and reviewed by one repository-aware Tech Lead. It does not prove:

- scanner correctness;
- automated schema validation or regression behavior;
- real-repository precision and recall;
- usability across multiple reviewers;
- acceptable performance at repository scale.

These limitations move into delivery evidence and external validation; they do not invalidate the finding contract for shaping the next foundation increment.

## Product decision

- `KG-001` is **validated for v0.1 shaping and implementation use**, subject to regression tests and real-repository validation during delivery.
- `KG-010` is **complete as the initial manual evaluation baseline**.
- `KG-002` is **authorized for shaping only**.
- Scanner implementation remains unauthorized until KG-002 meets the Definition of Ready and receives a separate delivery decision.
