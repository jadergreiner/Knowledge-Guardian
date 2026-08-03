# Knowledge Guardian — Product Backlog

**Status:** Active
**Version:** 0.5
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

**Evidence:** seven versioned contracts, positive and negative fixtures, deterministic contract tests and human acceptance.

### KG-003 — Build Markdown repository discovery

**Type:** Delivery  
**Status:** `approved_for_discovery_delivery` — implementation authorized within bounded scope

**Outcome:** An explicitly selected repository root produces a deterministic, read-only inventory of Markdown resources represented by valid `RepositorySnapshot` and `Resource` records.

**Shaping artifact:** `portfolio/KG_003_SHAPING.md`.

**Delivery plan:** `portfolio/KG_003_DELIVERY_PLAN.md`.

**Approved boundaries:**

- caller supplies Git/repository context;
- unreadable files create diagnostics and no incomplete resource;
- SHA-256 is optional and enabled by default;
- symlinks are neither followed nor inventoried;
- hidden directories are included except `.git` and configured ignores;
- `.mdx` is inventoried as Markdown without parsing.

**Planned deliverables:**

- configuration interface;
- deterministic inventory operation;
- diagnostic representation and stable codes;
- normalized paths and deterministic identities;
- KG-002 contract-compliant snapshot/resources;
- deterministic unit and integration tests;
- repeated-run determinism evidence;
- observability and rollback documentation.

**Explicit exclusions:** Git discovery, Markdown/YAML/MDX parsing, classification, relationships, entry-point or orphan analysis, rule execution, findings, reports, CI/CD and KG-004 onward.

**Decision:** `KGD-016` — `approved_for_discovery_delivery`.

**Next action:** Implement the bounded read-only inventory in a dedicated delivery branch and return with the required evidence. KG-004 onward remains blocked.

### KG-004 — Detect entry points and orphan documents

**Type:** Delivery  
**Status:** Blocked — depends on KG-003 delivery completion and separate authorization

### KG-005 — Validate internal Markdown references

**Type:** Delivery  
**Status:** Blocked — depends on KG-003 and separate shaping

### KG-006 — Parse and validate document metadata

**Type:** Delivery  
**Status:** Blocked — depends on KG-003 and separate shaping

### KG-007 — Produce Markdown and JSON reports

**Type:** Delivery  
**Status:** Blocked — depends on finding generation and report shaping

### KG-008 — Create the Knowledge Guardian project profile

**Type:** Product validation  
**Status:** Planned — depends on KG-002 contract boundaries and discovery behavior

### KG-009 — Create the Meu PDI project profile

**Type:** Product validation  
**Status:** Planned — depends on KG-002, KG-003 and KG-008 learning

### KG-010 — Establish the v0.1 evaluation baseline

**Type:** Quality and discovery validation  
**Status:** Complete — initial manual baseline

**Result:** 12 cases versioned and reviewed; positive-fixture conformance `7/7`; negative-case protection `4/4`.

## Discovery queue

- `KG-D01` — Determine acceptable false-positive threshold using real scans.
- `KG-D02` — Validate minimum metadata users will maintain.
- `KG-D03` — Evaluate report formats in engineering workflows.
- `KG-D04` — Compare semantic-analysis strategies for v0.2.
- `KG-D05` — Define waiver, suppression and expiration semantics.

## Explicitly deferred

- KG-003 implementation before `approved_for_discovery_delivery`;
- KG-004 or later items before separate shaping and authorization;
- automatic file rewriting;
- autonomous canonical-source selection;
- broad source-code analysis;
- external-link crawling;
- semantic blocking gates;
- CI/CD enforcement before executable quality evidence.
