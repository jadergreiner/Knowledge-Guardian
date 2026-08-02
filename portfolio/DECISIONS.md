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

### KGD-007 — Findings require an explicit authority source

**Date:** 2026-08-02  
**Type:** Product and governance  
**Status:** Accepted

**Context:** A finding must not represent an undocumented preference or an unsupported opinion from an AI agent. The product needs to state which authority establishes the expected state used in the comparison.

**Decision:** Every finding must reference one explicit authority source from the following model:

1. native framework rule;
2. project profile rule;
3. formal schema or executable contract;
4. repository-declared canonical source.

The first three sources produce **normative findings** when the evidence is deterministic. Canonical-source comparisons and other semantic interpretations produce **interpretative findings**, which must expose confidence and require human review before being treated as confirmed divergence.

**Rationale:** This separation prevents probabilistic semantic claims from receiving the same authority as broken references, schema violations or explicit policy failures.

**Consequences:**

- the finding contract must include authority type and authority reference;
- native rules must be configurable when they are not universal;
- interpretative findings cannot silently become blocking quality gates;
- confidence and review state are mandatory for interpretative findings;
- findings without an identifiable authority source are invalid.

**Evidence and confidence:** Approved jointly by the human Tech Lead and Virtual Product Manager during the finding-model discovery session. Confidence: high.

**Review trigger:** Reassess after the first golden baseline and the first scan of Meu PDI.

### KGD-008 — Impact is mandatory in the finding contract

**Date:** 2026-08-02  
**Type:** Product and governance  
**Status:** Accepted

**Context:** A finding describes a divergence, but without impact it is difficult to prioritize remediation, explain relevance to stakeholders, assess risk to AI agents, or distinguish cosmetic inconsistency from material knowledge debt.

**Decision:** Every finding in v0.1 must include an `impact` section. The impact must not be invented when repository context is insufficient. It must declare one of these states:

- `known`;
- `potential`;
- `unknown`;
- `not_applicable`.

When impact is `known` or `potential`, the finding should identify relevant dimensions where evidence allows, including engineering, agent behavior, governance, operations, onboarding, compliance, or product.

**Rationale:** Keeping impact from the beginning preserves the connection between detection and product value while allowing uncertainty to remain explicit.

**Consequences:**

- `impact` becomes a required field in `finding.schema.json`;
- unknown impact is valid when accompanied by a reason;
- severity must not be justified by unsupported impact claims;
- reports may use impact dimensions to support prioritization and stakeholder communication;
- human reviewers can refine impact without changing the underlying factual evidence.

**Evidence and confidence:** Approved jointly by the human Tech Lead and Virtual Product Manager after review of prioritization, agent-risk, governance and remediation use cases. Confidence: high.

**Review trigger:** Reassess the impact taxonomy after the golden baseline and initial reviewer feedback.