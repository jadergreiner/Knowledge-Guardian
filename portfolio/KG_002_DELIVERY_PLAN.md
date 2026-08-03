# KG-002 — Contract Delivery Plan

**Status:** Ready for bounded delivery  
**Version:** 0.1  
**Date:** 2026-08-02

## Objective

Convert the shaped repository document model into versioned, machine-validatable contracts without introducing repository scanning or parsing behavior.

## Deliverables

### Schemas

Create versioned JSON Schemas for:

- `repository-snapshot.schema.json`;
- `resource.schema.json`;
- `document.schema.json`;
- `classification.schema.json`;
- `relationship.schema.json`;
- `entry-point.schema.json`;
- `exception.schema.json`.

All contracts must:

- use JSON Schema draft 2020-12;
- declare stable `$id`, title and semantic contract version;
- reject unsupported additional properties unless explicitly extensible;
- preserve repository-relative normalized paths;
- represent `unknown` classifications without invented certainty;
- separate observed metadata from normalized classifications;
- avoid embedding scanner or parser behavior.

### Fixtures

For every schema, provide:

- at least one minimal valid fixture;
- at least one representative valid fixture;
- at least one invalid fixture for a required-field failure;
- at least one invalid fixture for an enum, identity or invariant failure where applicable.

### Contract tests

Tests must verify:

- every valid fixture passes;
- every invalid fixture fails for the intended reason;
- contract versions are consistent;
- referenced schemas resolve locally and deterministically;
- duplicate or conflicting identity inputs are rejected where represented by the contract;
- no absolute local path is accepted as durable resource identity.

### Documentation

Update or create:

- schema index and contract ownership;
- local validation instructions;
- versioning and compatibility policy;
- mapping from `REPOSITORY_DOCUMENT_MODEL.md` concepts to schema files;
- known limitations and deferred semantics.

## Acceptance criteria

- [ ] seven versioned schemas exist;
- [ ] each schema maps to an approved model concept;
- [ ] schemas use consistent identifiers and versioning;
- [ ] positive and negative fixtures cover every schema;
- [ ] executable tests validate all fixtures deterministically;
- [ ] failures identify the intended contract boundary;
- [ ] no scanner, parser, traversal or finding logic is introduced;
- [ ] documentation explains how to validate locally;
- [ ] unresolved model ambiguities are recorded rather than silently resolved;
- [ ] Tech Lead reviews validation evidence and records quality disposition.

## Delivery sequence

1. define shared identifiers, path and contract-version definitions;
2. implement `RepositorySnapshot` and `Resource` contracts;
3. implement `Classification` and `Document` contracts;
4. implement `Relationship`, `EntryPoint` and `Exception` contracts;
5. create fixtures alongside each contract;
6. create deterministic validation tests;
7. run complete validation and record evidence;
8. update documentation and RAID;
9. submit for Tech Lead quality decision.

## Observability and evidence

The delivery report must record:

- validator and version;
- command used;
- number of valid fixtures passed;
- number of invalid fixtures correctly rejected;
- unexpected failures;
- schema-reference resolution result;
- contract gaps or changes made during implementation.

## Risks

- schema decomposition may create circular references;
- identity invariants may require application-level validation beyond JSON Schema;
- path case sensitivity may remain repository-policy dependent;
- relationship targets may require snapshot-level integrity checks outside individual schemas;
- over-generalization may make contracts difficult to use.

## Gate

This plan authorizes bounded contract implementation only. `KG-003` remains blocked until `KG-002` passes executable tests and receives a separate Tech Lead completion decision.