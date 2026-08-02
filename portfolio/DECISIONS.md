# Knowledge Guardian — Decision Log

**Status:** Active
**Version:** 0.1
**Updated:** 2026-08-02

## Decision record format

Each material decision should record:

- identifier and date;
- decision type: product, technical, governance, or delivery;
- context and problem;
- considered options;
- decision and rationale;
- evidence and confidence;
- consequences and review trigger.

## Decisions

### KGD-001 — Knowledge is part of system architecture

**Date:** 2026-08-02  
**Type:** Product  
**Status:** Accepted

**Decision:** Treat documentation, decisions, terminology, specifications, operational context and agent instructions as governed architectural knowledge rather than secondary documentation.

**Rationale:** These artifacts influence both human engineering decisions and AI-agent behavior.

**Consequence:** Product scope includes knowledge relationships, trust signals, authority and semantic consistency, but remains bounded away from generic code linting.

### KGD-002 — Proposal-first and read-only by default

**Date:** 2026-08-02  
**Type:** Governance  
**Status:** Accepted

**Decision:** Knowledge Guardian may report and propose changes, but it must not silently rewrite governance, product or architecture knowledge.

**Rationale:** Repository authority and intent require human accountability.

**Consequence:** Automatic remediation is deferred and must require explicit authorization.

### KGD-003 — Deterministic checks before semantic analysis

**Date:** 2026-08-02  
**Type:** Product and technical  
**Status:** Accepted

**Decision:** v0.1 will prioritize repository discovery, metadata, references and navigation checks that can be reproduced deterministically.

**Rationale:** The product needs an evidence baseline and trusted finding contract before introducing probabilistic semantic claims.

**Consequence:** Semantic consistency becomes a v0.2 outcome subject to discovery and evaluation gates.

### KGD-004 — Profiles extend the core

**Date:** 2026-08-02  
**Type:** Architecture  
**Status:** Accepted

**Decision:** Repository-specific entry points, terminology, schemas, canonical sources and exceptions belong in project profiles rather than hard-coded core behavior.

**Rationale:** Governance differs by repository and organization.

**Consequence:** The core model and rule engine must support configuration and versioning.

### KGD-005 — Knowledge Guardian and Meu PDI are initial validation repositories

**Date:** 2026-08-02  
**Type:** Product  
**Status:** Accepted

**Decision:** Use Knowledge Guardian for self-governance validation and Meu PDI as the first complex AI-native repository case.

**Rationale:** Together they provide a small controlled repository and a larger repository with multiple knowledge domains and agent contexts.

**Consequence:** v0.1 exit criteria require reviewed scans for both repositories.

### KGD-006 — Trusted Knowledge Findings Rate is the initial North Star

**Date:** 2026-08-02  
**Type:** Product  
**Status:** Accepted provisionally

**Decision:** Measure the percentage of findings accepted by qualified human reviewers as correct, relevant and actionable.

**Rationale:** Report volume does not represent value; trusted actionable findings do.

**Review trigger:** Reassess after the first two repository baselines and reviewer workflow tests.
