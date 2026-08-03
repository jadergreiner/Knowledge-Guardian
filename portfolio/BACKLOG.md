# Knowledge Guardian — Product Backlog

**Status:** Active
**Version:** 0.4
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
**Status:** Accepted for merge to `main`
**Outcome:** Documents can be consistently discovered, classified and related without conflating paths, authority, metadata or knowledge layers.

**Shaping artifact:** `portfolio/REPOSITORY_DOCUMENT_MODEL.md`.

**Decision:** `portfolio/decisions/KGD-013.md`.

**Delivery plan:** `portfolio/KG_002_DELIVERY_PLAN.md`.

**Authorized deliverables:**

- versioned JSON Schemas for `RepositorySnapshot`, `Resource`, `Document`, `Classification`, `Relationship`, `EntryPoint` and `Exception`;
- positive and negative fixtures;
- deterministic contract tests;
- validation instructions and evidence;
- compatibility and limitation documentation.

**Acceptance criteria:**

- [x] seven versioned schemas exist;
- [x] each schema maps to the approved conceptual model;
- [x] schemas use consistent IDs and semantic versions;
- [x] valid and invalid fixtures cover every schema;
- [x] executable tests validate all fixtures deterministically;
- [x] intended invalid cases fail for the expected reason;
- [x] no scanner, parser, graph traversal, finding or report logic is introduced;
- [x] unresolved ambiguities are recorded;
- [x] Tech Lead records a quality disposition: accepted for merge to `main`.

**Explicit exclusions:** filesystem scanning, Markdown/YAML parsing, repository traversal, relationship discovery, rule execution, finding generation, report generation and `KG-003`.

**Next bounded increment:** Shape KG-003 only after separate authorization. The KG-002 contract-and-test slice is accepted for merge to `main`.

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

- KG-003 before KG-002 completion and separate authorization;
- automatic file rewriting;
- autonomous canonical-source selection;
- broad source-code analysis;
- external-link crawling;
- semantic blocking gates;
- CI/CD enforcement before executable quality evidence.
