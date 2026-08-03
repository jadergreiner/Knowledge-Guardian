# Knowledge Guardian — Product Backlog

**Status:** Active
**Version:** 0.1
**Updated:** 2026-08-02

## Prioritization model

Items are prioritized using user impact, evidence strength, uncertainty reduction, dependency value, effort, and false-confidence risk.

## Now — v0.1 foundation

### KG-001 — Define the trusted finding contract

**Type:** Product foundation  
**Status:** Complete baseline curated — final negative-case review pending  
**Outcome:** Reviewers can understand, reproduce and decide on every finding.

**Completed outputs:**

- `portfolio/FINDING_MODEL.md`;
- `schemas/finding.schema.json`;
- explicit authority, observation/inference, impact, confidence, treatment, recommendation and review models;
- deterministic fingerprint and versioned contract;
- deterministic Batch 01 with four accepted findings;
- interpretative Batch 02 with two accepted findings, one revision request and one pre-finding rejection;
- candidate analysis retained as internal-only in v0.1;
- Batch 03 expected non-findings curated with suppression rationales.

**Acceptance criteria:**

- [x] stable logical identity, human-facing ID and rule ID;
- [x] explicit category, type, confidence and treatment;
- [x] reproducible resource, location and evidence semantics;
- [x] observation separated from inference;
- [x] mandatory traceable authority;
- [x] mandatory impact with explicit uncertainty;
- [x] proposal-first recommendation;
- [x] human review and disposition;
- [x] versioned schema and contract;
- [x] deterministic findings validated;
- [x] interpretative findings validated;
- [x] revision-request workflow exercised;
- [x] authority-less candidate rejected before emission;
- [~] expected non-findings curated, pending human confirmation;
- [~] all 12 golden cases versioned, final review pending;
- [ ] regression tests protect rule behavior.

**Validation dependency:** `KG-010 — Establish the v0.1 evaluation baseline`.

**Exit condition:** KG-001 may be marked validated only after Batch 03 review and incorporation of any required contract changes.

### KG-002 — Define the repository document model

**Type:** Technical foundation  
**Status:** Not started — gated by final KG-001 decision  
**Outcome:** Documents can be consistently discovered and classified.

**Acceptance criteria:**

- supported document types are enumerated;
- document identity and path rules are defined;
- metadata and relationship models are versioned;
- conceptual, specification, executable, operational and agent-context layers are represented.

### KG-003 — Build Markdown repository discovery

**Type:** Delivery  
**Status:** Not started  
**Outcome:** A repository scan produces a deterministic document inventory.

### KG-004 — Detect entry points and orphan documents

**Type:** Delivery  
**Status:** Not started  
**Outcome:** Maintainers can identify documents that are not reachable through intended navigation.

### KG-005 — Validate internal Markdown references

**Type:** Delivery  
**Status:** Not started  
**Outcome:** Broken repository knowledge links are reported with reproducible evidence.

### KG-006 — Parse and validate document metadata

**Type:** Delivery  
**Status:** Not started  
**Outcome:** Project-specific governance metadata can be checked without enforcing one universal schema.

### KG-007 — Produce Markdown and JSON reports

**Type:** Delivery  
**Status:** Not started  
**Outcome:** Humans and automation can consume the same scan results.

### KG-008 — Create the Knowledge Guardian project profile

**Type:** Product validation  
**Status:** Not started  
**Outcome:** The framework can govern its own repository using explicit policies.

### KG-009 — Create the Meu PDI project profile

**Type:** Product validation  
**Status:** Not started  
**Outcome:** v0.1 is validated against a complex AI-native repository.

### KG-010 — Establish the v0.1 evaluation baseline

**Type:** Quality and discovery validation  
**Status:** In progress — all 12 cases versioned, Batch 03 review pending  
**Outcome:** Product quality can be measured before CI/CD integration.

**Completed:**

- [x] baseline purpose, scope, catalogue and reviewer rubric defined;
- [x] controlled snapshots selected;
- [x] `GB-001` through `GB-004` accepted;
- [x] `GB-005` and `GB-006` accepted;
- [x] `GB-007` received `revision_requested`;
- [x] `GB-008` rejected before finding emission;
- [x] candidate analysis classified as internal-only;
- [x] `GB-009` through `GB-012` versioned with explicit suppression rationales.

**Remaining:**

- [ ] human review of `GB-009` through `GB-012`;
- [ ] negative-case pass rate recorded;
- [ ] false-positive and ambiguity result finalized;
- [ ] final KG-001 validation decision;
- [ ] explicit decision whether KG-002 may enter shaping;
- [ ] regression-test strategy implemented after delivery authorization.

**Next bounded increment:** Human review of Batch 03 and final baseline decision. Do not start KG-002 or scanner implementation before that decision.

## Discovery queue

- `KG-D01` — acceptable false-positive threshold;
- `KG-D02` — minimum metadata fields users will maintain;
- `KG-D03` — report formats for engineering workflows;
- `KG-D04` — semantic-analysis strategies for v0.2;
- `KG-D05` — waiver, suppression and expiration semantics.

## Explicitly deferred

- automatic file rewriting;
- autonomous canonical-source selection;
- broad source-code analysis;
- external-link crawling;
- semantic drift claims without an evaluation baseline;
- pull-request blocking before precision is established.