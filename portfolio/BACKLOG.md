# Knowledge Guardian — Product Backlog

**Status:** Active
**Version:** 0.3
**Updated:** 2026-08-02

## Prioritization model

Items are prioritized using user impact, evidence strength, uncertainty reduction, dependency value, effort and false-confidence risk.

## Now — v0.1 foundation

### KG-001 — Define the trusted finding contract

**Type:** Product foundation  
**Status:** Validated for v0.1 shaping and implementation use  
**Outcome:** Reviewers can understand, reproduce and decide on findings.

**Evidence:**

- contract `knowledge-guardian-finding@0.1.0`;
- seven positive fixtures structurally valid;
- six accepted findings;
- one revision-request workflow;
- one pre-finding rejection;
- four expected non-findings confirmed;
- no immediate schema revision required.

**Remaining delivery requirements:** executable validation, regression tests, real-repository precision and broader reviewer evidence.

### KG-002 — Define the repository document model

**Type:** Technical foundation  
**Status:** Shaped — Definition of Ready complete, delivery decision pending  
**Outcome:** Documents can be consistently discovered, classified and related without conflating paths, authority, metadata or knowledge layers.

**Shaping artifact:** `portfolio/REPOSITORY_DOCUMENT_MODEL.md`.

**Definition of Ready:**

- [x] clear problem statement and consumers;
- [x] expected outcome;
- [x] bounded scope and exclusions;
- [x] supported resource formats;
- [x] resource and document identity rules;
- [x] repository-relative path normalization;
- [x] document-type vocabulary;
- [x] knowledge-layer vocabulary;
- [x] lifecycle model;
- [x] metadata model and precedence;
- [x] classification provenance and confidence;
- [x] trust-signal observations;
- [x] relationship model;
- [x] entry-point representation;
- [x] exception representation;
- [x] explicit dependencies and risks;
- [x] testable acceptance criteria;
- [x] bounded implementation scope.

**Proposed delivery slice:** versioned data contracts and contract tests for `RepositorySnapshot`, `Resource`, `Document`, `Classification`, `Relationship`, `EntryPoint` and `Exception`.

**Explicitly excluded from the proposed slice:** filesystem scanning, Markdown parsing, graph traversal, rule execution, finding generation and report rendering.

**Next bounded increment:** Tech Lead reviews the model and decides `approved_for_contract_delivery`, `revision_requested` or `rejected`.

### KG-003 — Build Markdown repository discovery

**Type:** Delivery  
**Status:** Blocked — depends on KG-002 delivery completion and separate authorization

### KG-004 — Detect entry points and orphan documents

**Type:** Delivery  
**Status:** Blocked — depends on KG-002 and KG-003

### KG-005 — Validate internal Markdown references

**Type:** Delivery  
**Status:** Blocked — depends on KG-002 and KG-003

### KG-006 — Parse and validate document metadata

**Type:** Delivery  
**Status:** Blocked — depends on KG-002 and KG-003

### KG-007 — Produce Markdown and JSON reports

**Type:** Delivery  
**Status:** Blocked — depends on finding generation and report shaping

### KG-008 — Create the Knowledge Guardian project profile

**Type:** Product validation  
**Status:** Planned — depends on KG-002 contract boundaries

### KG-009 — Create the Meu PDI project profile

**Type:** Product validation  
**Status:** Planned — depends on KG-002 and KG-008 learning

### KG-010 — Establish the v0.1 evaluation baseline

**Type:** Quality and discovery validation  
**Status:** Complete — initial manual baseline

**Result:**

- 12 cases versioned and reviewed;
- positive-fixture conformance: `7/7`;
- negative-case protection: `4/4`;
- baseline decision recorded in `portfolio/baseline/BASELINE_RESULT.md`;
- product decision recorded in `portfolio/decisions/KGD-012.md`.

## Discovery queue

- `KG-D01` — Determine acceptable false-positive threshold using real scans.
- `KG-D02` — Validate minimum metadata users will maintain.
- `KG-D03` — Evaluate report formats in engineering workflows.
- `KG-D04` — Compare semantic-analysis strategies for v0.2.
- `KG-D05` — Define waiver, suppression and expiration semantics.

## Explicitly deferred

- KG-002 implementation before Tech Lead approval;
- scanner implementation before KG-002 delivery completion;
- automatic file rewriting;
- autonomous canonical-source selection;
- broad source-code analysis;
- external-link crawling;
- semantic blocking gates;
- CI/CD enforcement before executable quality evidence.
