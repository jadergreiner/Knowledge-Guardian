# Knowledge Guardian — Discovery

**Status:** Active  
**Version:** 0.3  
**Updated:** 2026-08-02

## Discovery objective

Validate that repository maintainers and AI-agent teams experience material knowledge-governance problems and that Knowledge Guardian can produce findings they trust enough to act on.

## Primary users

- maintainers of documentation-heavy repositories;
- Tech Leads and architects responsible for repository governance;
- teams operating AI coding agents;
- open-source maintainers;
- platform and developer-experience teams.

## Core assumptions

| ID | Assumption | Risk if false | Validation method | Current status |
|---|---|---|---|---|
| A-001 | Teams cannot reliably identify canonical knowledge sources | Product value decreases | Repository audit and maintainer interview | Open |
| A-002 | Broken navigation and stale knowledge materially affect engineering work | Findings become cosmetic | Incident, onboarding and rework examples | Open |
| A-003 | AI agents amplify the cost of conflicting context | AI-native positioning weakens | Compare agent behavior with clean and conflicting context | Open |
| A-004 | Maintainers will accept proposal-first, read-only analysis | Adoption barrier increases | Prototype workflow test | Partially supported by Tech Lead review |
| A-005 | Deterministic checks deliver enough initial value | v0.1 value is insufficient | Scan real repositories and review findings | Open |
| A-006 | Users will configure repository profiles | Generic-only product may be required | Profile creation usability test | Open |
| A-007 | The hardened finding contract can represent realistic positive and negative cases | Baseline validation fails | Golden baseline and reviewer workflow | Open |

## Key discovery questions

1. Which repository knowledge failures cause real rework, incorrect implementation, or onboarding delay?
2. Who owns knowledge quality today, and how is it reviewed?
3. What evidence is required before a finding is trusted?
4. Which finding categories are actionable without semantic AI analysis?
5. What level of false positives causes users to stop reviewing reports?
6. Which outputs fit existing workflows: Markdown, JSON, SARIF, PR comments, dashboards, or IDE feedback?
7. How should waivers, exceptions and intentional duplication be represented?
8. What repository sizes and structures define the first supported segment?

## Initial research activities

### D-001 — Knowledge Guardian self-audit

Run the future v0.1 rules against this repository and record expected findings manually before implementation.

**Status:** Shaped — deterministic case curation ready  
**Output:** golden baseline and acceptance examples.  
**Shaping artifact:** `portfolio/GOLDEN_BASELINE.md`.

### D-002 — Meu PDI repository audit

Use Meu PDI as the first complex repository case, with emphasis on `.ai`, `apos`, `knowledge`, `docs`, agent instructions and architectural sources.

**Status:** Planned  
**Output:** prioritized problem inventory and project profile requirements.

### D-003 — Maintainer workflow interview

Document one concrete episode where conflicting, stale, missing or orphaned knowledge caused delay or error.

**Status:** Planned  
**Output:** verified jobs, pains and current workarounds.

### D-004 — Finding trust test

Present sample findings with evidence, confidence, impact, treatment and remediation to reviewers.

**Status:** In progress — contract hardened, fixture review pending  
**Output:** minimum trusted finding contract.

### D-005 — Competitive and adjacent-tool analysis

Compare documentation linters, link checkers, knowledge graphs, architecture governance tools, code-quality platforms and AI context systems.

**Status:** Planned  
**Output:** differentiation and build-versus-integrate decisions.

## Discovery evidence log

### E-001 — Finding-model pairing session

**Date:** 2026-08-02  
**Context:** Knowledge Guardian product discovery session between the Virtual Product Manager and the human Tech Lead.  
**Related activity:** D-004 — Finding trust test.  
**Source:** Pair discussion and explicit human approvals recorded during the session.

#### Observation 1 — Findings require an explicit authority source

The Tech Lead initially requested additional context before accepting the proposed four authority origins. After reviewing concrete examples, the Tech Lead approved the following authority model:

1. native framework rule;
2. project profile rule;
3. formal schema or executable contract;
4. repository-declared canonical source.

**Inference:** A finding is more trustworthy when the expected state is traceable to an explicit authority rather than an undocumented preference or model-generated opinion.

**Confidence:** High.  
**Impact on product decisions:**

- findings without an identifiable authority source are invalid;
- the product distinguishes `normative` from `interpretative` findings;
- canonical-source and semantic comparisons require confidence disclosure and human review;
- decision recorded as `KGD-007`.

#### Observation 2 — Impact is necessary from v0.1

The Tech Lead requested concrete use cases before deciding whether `impact` should be mandatory. Examples involving prioritization, agent behavior, governance, onboarding and remediation clarified its value. The Tech Lead approved retaining impact from the first version.

**Inference:** A divergence alone is insufficient for prioritization and stakeholder communication. The finding contract must also express the consequence or explicitly state that it cannot yet be determined.

**Confidence:** High.  
**Impact on product decisions:**

- `impact` is mandatory in every finding;
- allowed states are `known`, `potential`, `unknown` and `not_applicable`;
- unsupported consequences must not be invented;
- unknown impact requires an explanation;
- decision recorded as `KGD-008`.

#### Observation 3 — Impact and confidence should produce treatment groups

The Tech Lead proposed grouping findings through a matrix rather than interpreting impact, confidence and severity as isolated fields. Six treatment groups were reviewed and approved:

- `confirmed_critical`;
- `confirmed_actionable`;
- `probable_risk`;
- `investigative`;
- `routine_improvement`;
- `informational`.

**Inference:** A treatment matrix provides more actionable prioritization while preserving the distinction between potential consequence and evidence strength.

**Confidence:** High.  
**Impact on product decisions:**

- treatment group becomes a derived classification in the finding contract;
- high-impact, low-confidence findings remain visible but cannot be treated as confirmed blockers;
- `severity` is not sufficient as an isolated product concept and is replaced by explicit impact level plus confidence and treatment;
- decision recorded as `KGD-009`.

#### Observation 4 — Human authority is a non-negotiable product principle

The Tech Lead explicitly reinforced that Knowledge Guardian generates analysis and recommendations, but the final decision must always remain with a human reviewer.

**Inference:** Treatment classification must never be confused with autonomous disposition or governance authority.

**Confidence:** High.  
**Impact on product decisions:**

- the review workflow uses `pending_review`, `accepted`, `revision_requested` and `cancelled`;
- the system may recommend an action but cannot accept, revise or cancel a finding on behalf of the reviewer;
- interpretative findings always require human review;
- no treatment group independently authorizes repository modification or policy enforcement.

### E-002 — Finding-contract hardening and baseline shaping

**Date:** 2026-08-02  
**Context:** Acceptance-criteria review of KG-001 by the Virtual Product Manager and human Tech Lead.  
**Related activities:** D-001 and D-004.  
**Source:** Direct comparison of `portfolio/FINDING_MODEL.md`, `schemas/finding.schema.json`, `portfolio/BACKLOG.md`, and the operating-model guardrails.

#### Observation 1 — The conceptual model exceeded the executable schema

The review found that the model required stable identity, observation/inference separation, explicit versioning, and reproducible location semantics, while the schema did not fully enforce those concepts.

**Inference:** A conceptually sound contract can still produce ambiguous fixtures when required distinctions are not represented structurally.

**Confidence:** High.  
**Impact on product decisions:**

- decision `KGD-010` required contract hardening before baseline curation;
- `fingerprint` became mandatory;
- finding contract name and semantic version became mandatory;
- `analysis.observation` and interpretative inference became explicit;
- exact or justified location semantics became mandatory.

#### Observation 2 — Hardening was applied consistently to model and schema

`portfolio/FINDING_MODEL.md` and `schemas/finding.schema.json` now represent the four approved hardening decisions under contract version `0.1.0`.

**Inference:** KG-001 has sufficient structural maturity to enter baseline validation, but it is not yet validated for usability, precision, or representative cases.

**Confidence:** High.  
**Impact on product decisions:**

- the contract-hardening dependency for KG-010 is satisfied;
- KG-002 and delivery work remain gated;
- product focus moves to evidence generation rather than additional abstract contract design.

#### Observation 3 — The baseline needs a bounded challenge set and review rubric

Proceeding directly to ad hoc examples would risk selecting cases that merely fit the contract. A 12-case catalogue was shaped with normative findings, interpretative findings, revision requests, cancellation, and expected non-findings.

**Inference:** Positive fixtures alone cannot validate trust. Negative cases and human disagreement are required to test overreach and false confidence.

**Confidence:** High.  
**Impact on product decisions:**

- `portfolio/GOLDEN_BASELINE.md` defines the baseline structure;
- deterministic cases GB-001 through GB-004 form the first bounded batch;
- schema conformance, reviewer acceptance, and negative-case protection are measured separately;
- ambiguity records must be retained rather than forced into the current contract.

## Discovery conclusions

### Supported conclusions

The current evidence supports the following draft product conclusions:

1. Reviewers need every finding to identify the authority behind the expected state.
2. Findings must separate factual observation from interpretation and recommendation.
3. Impact is required for prioritization, but uncertainty about impact must remain explicit.
4. Confidence represents evidence strength and must not be conflated with consequence.
5. A six-group treatment matrix is understandable and useful to the human Tech Lead reviewer.
6. Human disposition is a core product boundary, not merely an implementation preference.
7. Stable identity, explicit contract version and location semantics are required for reproducible baseline evidence.
8. The hardened finding model is sufficiently defined for golden-baseline testing.
9. Negative cases, cancellations and revision requests are necessary to test product trust.

### Conclusions not yet validated

The evidence does **not** yet prove that:

- other maintainers will understand or accept the same model;
- the six treatment groups remain usable at report scale;
- the impact taxonomy covers all relevant repositories;
- the schema produces acceptable precision or low review effort;
- deterministic v0.1 rules deliver sufficient standalone value;
- the reviewer workflow is usable outside a paired discovery session;
- the 12 shaped cases can be represented without further contract changes;
- the eventual scanner can generate the same evidence deterministically.

These questions require the golden baseline, self-audit, Meu PDI audit, executable validation and additional reviewer evidence.

## Shaping outputs produced

The discovery conclusions are materialized in:

- `portfolio/FINDING_MODEL.md`;
- `schemas/finding.schema.json`;
- `portfolio/GOLDEN_BASELINE.md`;
- decisions `KGD-007` through `KGD-010` in `portfolio/DECISIONS.md`.

These artifacts are **shaped outputs pending evidence**, not proof that the finding model or product is production-ready.

## Evidence standard

Every discovery conclusion must identify:

- source;
- date;
- repository or user context;
- observation;
- inference;
- confidence;
- impact on product decisions.

## Discovery-to-delivery gate

An opportunity may enter delivery when:

- the problem is supported by concrete evidence;
- the target user and expected outcome are explicit;
- success can be measured;
- major dependencies are understood;
- acceptance criteria are testable;
- the scope fits a bounded increment.

For the finding contract, the gate additionally requires:

- a manually reviewed golden baseline;
- positive and negative examples;
- schema validation against all positive fixtures;
- explicit false-positive and false-negative review;
- confirmation that treatment groups and review states remain understandable at report scale;
- a recorded product decision that KG-001 is validated or requires revision.

## Current priority

Select a stable Knowledge Guardian commit and curate GB-001 through GB-004 as the first deterministic baseline batch. Do not start KG-002 or scanner implementation before the batch is schema-valid and human-reviewed.
