# Knowledge Guardian — Product Status

**Date:** 2026-08-02  
**Overall status:** KG-002 approved for bounded contract delivery  
**Confidence:** Medium

## Current position

The finding contract is validated for v0.1 use and the initial manual baseline is complete.

`KG-002 — Repository Document Model` completed shaping, satisfies the operating-model Definition of Ready and has been approved by the human Tech Lead for a bounded contract-and-test delivery slice.

No filesystem scanner, parser, traversal engine or finding engine has been started.

## Operating-model position

```text
SENSE → FRAME → DISCOVER → DECIDE → SHAPE → DELIVER
                                                    ↑
                                      KG-002 contract slice only
```

## Authorized scope

The authorized increment creates:

- versioned contracts for `RepositorySnapshot`, `Resource`, `Document`, `Classification`, `Relationship`, `EntryPoint` and `Exception`;
- representative valid and invalid fixtures;
- deterministic contract tests;
- local validation instructions;
- compatibility, limitation and validation evidence.

Decision: `portfolio/decisions/KGD-013.md`.

Plan: `portfolio/KG_002_DELIVERY_PLAN.md`.

## Delivery acceptance evidence

The increment must return with:

1. seven versioned schemas;
2. positive and negative fixtures for every schema;
3. executable validation output;
4. validator, version and command used;
5. deterministic schema-reference resolution;
6. documented contract gaps and limitations;
7. confirmation that no scanner behavior was introduced;
8. Tech Lead quality disposition.

## Explicitly not authorized

- filesystem scanning;
- Markdown or YAML parsing;
- repository traversal;
- relationship discovery from repository content;
- rule execution;
- finding or report generation;
- `KG-003` implementation;
- CI/CD enforcement;
- automatic repository modification.

## Active risks

- JSON Schema may not express every cross-resource invariant;
- contract decomposition may create reference complexity;
- path case sensitivity remains profile dependent;
- relationship target integrity may require snapshot-level validation;
- implementation feedback may expose a material model ambiguity.

Any material ambiguity returns to shaping rather than being silently decided during implementation.

## Next checkpoint

KG-002 reaches its delivery checkpoint when all contract schemas and tests are executable, evidence is recorded and the Tech Lead decides whether the increment is accepted, requires revision or is rejected. `KG-003` remains blocked until a separate authorization.