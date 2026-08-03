# Knowledge Guardian — Decision Log

**Status:** Active
**Version:** 0.2
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

### KGD-015 — Approve KG-003 shaping with bounded discovery boundaries

**Date:** 2026-08-02
**Type:** Technical and delivery governance
**Status:** `approved_with_boundaries`

**Context:** KG-003 requires a deterministic, read-only inventory of Markdown resources. Six unresolved boundaries affected observable scanner behavior: Git context, unreadable files, checksums, symlinks, hidden directories and `.mdx` handling.

**Decision:** Approve the KG-003 shaping proposal with the six boundaries recorded in `portfolio/KG_003_SHAPING.md`:

- caller supplies repository context explicitly;
- unreadable files produce bounded diagnostics and no incomplete resource;
- SHA-256 is optional and enabled by default for readable files;
- symlinks are not followed or inventoried;
- hidden directories are included except `.git` and configured ignore paths;
- `.mdx` is inventoried as Markdown without parsing.

**Authority:** Human Tech Lead/Product assessment provided in the project execution workflow.

**Consequences:** A delivery plan may be prepared for the bounded inventory slice. Scanner implementation remains unauthorized until a separate `approved_for_discovery_delivery` decision. KG-004, parsing, classification, relationships, findings and reports remain blocked.

**Review trigger:** Review the delivery plan before implementation.

### KGD-014 — Accept KG-002 contract delivery for merge

**Date:** 2026-08-02
**Type:** Delivery
**Status:** Accepted

**Context:** KG-002 contract delivery completed with executable validation evidence: 14 valid fixtures passed, 14 invalid fixtures were rejected, unexpected failures were zero, and local schema references resolved deterministically.

**Decision:** Accept the bounded KG-002 contract-and-test increment for merge to `main`.

**Authority:** Human Tech Lead acceptance in the execution workflow.

**Consequences:** The repository-document contracts and related governance evidence may be merged. KG-003 remains blocked and requires a separate shaping and delivery authorization.

**Review trigger:** Reassess after merge verification and before any KG-003 implementation.

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

### KGD-009 — Findings use a six-group treatment matrix under human authority

**Date:** 2026-08-02  
**Type:** Product and governance  
**Status:** Accepted

**Context:** Impact and confidence need to produce an operational treatment without collapsing uncertainty into a single severity value. At the same time, Knowledge Guardian must preserve its proposal-first nature and must never silently convert analysis into an autonomous decision.

**Decision:** Findings are classified into six treatment groups derived from impact and confidence:

1. `confirmed_critical`;
2. `confirmed_actionable`;
3. `probable_risk`;
4. `investigative`;
5. `routine_improvement`;
6. `informational`.

The treatment group is a recommendation produced by the system. It does not authorize remediation, rejection, gate blocking, or any other final action by itself.

Every finding must expose a human decision state:

- `pending_review`;
- `accepted`;
- `revision_requested`;
- `cancelled`.

Only a human reviewer may move a finding from `pending_review` to another state.

**Rationale:** The matrix preserves prioritization and urgency while separating machine analysis from accountable human judgment.

**Consequences:**

- impact, confidence and treatment remain distinct;
- interpretative findings always require human review;
- audit data records who decided, when and why;
- reports distinguish system recommendation from human decision.

**Evidence and confidence:** Approved jointly by the human Tech Lead and Virtual Product Manager. Confidence: high.

**Review trigger:** Reassess after the golden baseline and first reviewer workflow test.

### KGD-010 — Harden the finding contract before baseline validation

**Date:** 2026-08-02  
**Type:** Product and technical  
**Status:** Accepted

**Context:** Review of KG-001 found ambiguity around fact versus inference, identity across scans, contract compatibility and evidence location.

**Decision:** Before constructing the golden baseline, the finding contract must:

1. separate observation and inference;
2. require a deterministic fingerprint;
3. declare contract version within each finding;
4. require exact or explicitly justified location semantics.

**Rationale:** These changes are prerequisites for reliable testing. Remaining questions require representative cases and human review.

**Consequences:** The model and schema were hardened before baseline execution, while matrix coherence and workflow usability remained baseline questions.

**Evidence and confidence:** Approved jointly by the human Tech Lead and Virtual Product Manager. Confidence: high.

### KGD-011 — Candidate analysis remains internal-only in v0.1

**Date:** 2026-08-02  
**Type:** Product and governance  
**Status:** Accepted

**Context:** Batch 02 showed that a suspected semantic conflict may fail validity before becoming a finding when no explicit authority exists. The product needed to distinguish pre-finding rejection from cancellation of a valid emitted finding.

**Considered options:**

1. force authority-less candidates into the finding contract and cancel them later;
2. create a separate public candidate-analysis schema in v0.1;
3. keep candidate analysis as internal pipeline state and emit only valid findings.

**Decision:** Candidate analysis remains internal-only in v0.1. A candidate without an explicit authority is rejected before finding emission. The public finding contract continues to represent only valid, authority-backed findings.

**Rationale:** Forcing invalid candidates into the finding schema would weaken the authority rule. Creating another public contract now would expand scope without demonstrated integration or user value.

**Consequences:**

- `GB-008` is recorded as `rejected_before_finding_emission`;
- pre-finding rejection is distinct from `review.status: cancelled`;
- no public candidate schema is created in v0.1;
- durable candidate records may be reconsidered if future debugging, observability or reviewer workflows require them;
- `GB-007` confirms that schema-valid findings may still require human revision when classification exceeds evidence.

**Evidence and confidence:** Human Tech Lead decisions for Batch 02: `GB-005 accepted`, `GB-006 accepted`, `GB-007 revision_requested`, `GB-008 rejected before finding emission`, and candidate analysis internal-only. Confidence: high.

**Review trigger:** Reassess after scanner implementation or when candidate-level observability becomes a demonstrated product requirement.
