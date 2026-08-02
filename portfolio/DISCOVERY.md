# Knowledge Guardian — Discovery

**Status:** Active  
**Version:** 0.2  
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

**Status:** Planned  
**Output:** golden baseline and acceptance examples.

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

**Status:** In progress  
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

## Discovery conclusions from E-001

### Supported conclusions

The current evidence supports the following draft product conclusions:

1. Reviewers need every finding to identify the authority behind the expected state.
2. Findings must separate factual observation from interpretation and recommendation.
3. Impact is required for prioritization, but uncertainty about impact must remain explicit.
4. Confidence represents evidence strength and must not be conflated with consequence.
5. A six-group treatment matrix is understandable and useful to the human Tech Lead reviewer.
6. Human disposition is a core product boundary, not merely an implementation preference.
7. The finding model is sufficiently defined to be materialized as a draft schema and tested through a golden baseline.

### Conclusions not yet validated

The session does **not** yet prove that:

- other maintainers will understand or accept the same model;
- the six treatment groups remain usable at report scale;
- the impact taxonomy covers all relevant repositories;
- the schema produces acceptable precision or low review effort;
- deterministic v0.1 rules deliver sufficient standalone value;
- the reviewer workflow is usable outside a paired discovery session.

These questions require the golden baseline, self-audit, Meu PDI audit and additional reviewer evidence.

## Shaping outputs produced

The discovery conclusions were materialized as draft product artifacts:

- `portfolio/FINDING_MODEL.md`;
- `schemas/finding.schema.json`;
- decisions `KGD-007`, `KGD-008` and `KGD-009` in `portfolio/DECISIONS.md`.

These artifacts are **draft outputs pending baseline validation**, not proof that the finding model is production-ready.

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
- schema validation against all baseline fixtures;
- explicit false-positive and false-negative review;
- confirmation that treatment groups and review states remain understandable at report scale.

## Current priority

Construct the Knowledge Guardian golden baseline for deterministic v0.1 scans and use it to validate the draft finding contract before implementation expands.
