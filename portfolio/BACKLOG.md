# Knowledge Guardian — Product Backlog

**Status:** Active
**Version:** 0.2
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
**Status:** Authorized for shaping — delivery not authorized  
**Outcome:** Documents can be consistently discovered and classified.

**Definition-of-Ready requirements:**

- clear problem statement and consumers;
- expected outcome;
- supported document types;
- identity and path rules;
- metadata model;
- relationship model;
- conceptual, specification, executable, operational and agent-context layers;
- explicit dependencies and risks;
- testable acceptance criteria;
- bounded implementation scope.

**Next bounded increment:** Shape KG-002 and present it for a separate Tech Lead delivery decision.

### KG-003 — Build Markdown repository discovery

**Type:** Delivery  
**Status:** Blocked — depends on KG-002 and delivery authorization

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
**Status:** Planned — depends on KG-002 profile boundaries

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

- scanner implementation before KG-002 readiness;
- automatic file rewriting;
- autonomous canonical-source selection;
- broad source-code analysis;
- external-link crawling;
- semantic blocking gates;
- CI/CD enforcement before executable quality evidence.
