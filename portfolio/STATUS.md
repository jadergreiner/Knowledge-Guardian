# Knowledge Guardian — Product Status

**Date:** 2026-08-02  
**Overall status:** KG-002 shaped — Tech Lead delivery decision pending  
**Confidence:** Medium

## Current position

The finding contract is validated for v0.1 use and the initial manual baseline is complete.

`KG-002 — Repository Document Model` now satisfies the operating-model Definition of Ready. Its shaping artifact defines resource and document identity, path normalization, document types, knowledge layers, lifecycle, metadata, trust signals, relationships, entry points, exceptions, invariants, risks and a bounded delivery slice.

No KG-002 implementation, scanner or executable rule engine has been started.

## Operating-model position

```text
SENSE → FRAME → DISCOVER → DECIDE → SHAPE → [DELIVERY DECISION GATE]
                                                    ↓
                                                DELIVER
```

## KG-002 shaping result

| Dimension | Result |
|---|---|
| Problem and consumers | Defined |
| Scope and exclusions | Defined |
| Resource/document identity | Defined |
| Path semantics | Defined |
| Document types | Defined |
| Knowledge layers | Defined |
| Metadata and lifecycle | Defined |
| Classification provenance | Defined |
| Trust signals | Defined |
| Relationships | Defined |
| Entry points and exceptions | Defined |
| Invariants | Defined |
| Acceptance criteria | Defined |
| Delivery slice | Bounded to contracts and tests |

Evidence: `portfolio/REPOSITORY_DOCUMENT_MODEL.md`.

## Proposed delivery scope

Subject to Tech Lead approval, the first delivery increment creates versioned contracts and contract tests for:

- `RepositorySnapshot`;
- `Resource`;
- `Document`;
- `Classification`;
- `Relationship`;
- `EntryPoint`;
- `Exception`.

It excludes scanning, parsing, traversal, rules, findings and reports.

## Required decision

The Tech Lead must record one disposition:

- `approved_for_contract_delivery`;
- `revision_requested`;
- `rejected`.

Approval authorizes only the bounded contract-and-test slice. It does not authorize KG-003 or scanner implementation.

## Remaining risks

- the vocabulary may be too broad before implementation feedback;
- cross-rename document identity is deferred;
- case-sensitive path comparison depends on repository policy;
- relationship types may expand without downstream use;
- metadata usability remains unvalidated with external maintainers;
- executable contract and regression evidence do not yet exist.

## Explicitly not authorized

- filesystem scanner;
- Markdown parser;
- graph traversal;
- finding generation;
- report generation;
- CI/CD enforcement;
- automatic repository modification.

## Next checkpoint

After the Tech Lead decision, Product records approval or requested revisions. If approved, delivery planning must define exact schema files, fixtures, tests, observability and documentation impact before code begins.
