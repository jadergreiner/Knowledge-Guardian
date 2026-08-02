# Knowledge Guardian — Finding Model

**Status:** Hardened draft — pending golden-baseline validation  
**Contract version:** 0.1.0  
**Updated:** 2026-08-02

## 1. Purpose

This document defines what constitutes a valid finding in Knowledge Guardian.

A finding is not an opinion, an undocumented preference, or an autonomous decision. It is a structured analysis result supported by evidence and tied to an explicit authority source.

Knowledge Guardian analyzes, classifies, and recommends. A human reviewer remains responsible for accepting, requesting revision, or cancelling the finding.

## 2. Definition

> A finding is a structured, evidence-backed statement that identifies a divergence between an observed repository state and an explicitly defined rule, policy, contract, or canonical expectation.

A valid finding must answer:

1. What was observed?
2. Where was it observed, or why does the observation apply to the resource as a whole?
3. Which authority defines the expected state?
4. What evidence supports the observation?
5. What inference, if any, is derived from that evidence?
6. What impact is known, potential, unknown, or not applicable?
7. How confident is the system in the conclusion?
8. What treatment is recommended?
9. What is the human review status?

## 3. Contract version

Every finding must declare the finding-contract version used to produce and validate it.

The v0.1 contract identifier is:

```yaml
contract:
  name: knowledge-guardian-finding
  version: 0.1.0
```

Contract versions follow semantic versioning:

- patch: clarification or compatible validation correction;
- minor: backward-compatible field or rule extension;
- major: incompatible contract change.

Historical findings remain interpretable against the version they declare.

## 4. Non-findings

The following must not be emitted as findings:

- unsupported opinions;
- undocumented style preferences;
- recommendations without a detected divergence;
- conclusions without a traceable authority source;
- runtime claims inferred only from aspirational documentation;
- semantic claims presented as facts without confidence and human review;
- impact statements invented without supporting context;
- duplicated findings representing the same rule, subject, authority and observed condition.

## 5. Finding types

### 5.1 Normative finding

A normative finding is produced when the expected state is explicit and the divergence can be reproduced deterministically.

Typical authority sources:

- native framework rule;
- project profile rule;
- formal schema or executable contract.

Examples:

- broken internal link;
- required metadata is absent;
- document violates a JSON Schema;
- configured entry point does not exist.

A normative finding may omit an inference when the observation itself establishes the divergence and consequence claims are not needed.

### 5.2 Interpretative finding

An interpretative finding is produced when detecting or explaining the divergence requires contextual or semantic interpretation.

Typical authority sources:

- repository-declared canonical source;
- semantic comparison between documents;
- conceptual-versus-runtime analysis;
- inferred terminology conflict.

Interpretative findings:

- must contain an explicit inference;
- must expose confidence;
- must require human review;
- must not become blocking gates automatically;
- must distinguish evidence, observation and inference.

## 6. Authority model

Every finding must identify exactly one primary authority source.

### 6.1 Native framework rule

A general rule supplied by Knowledge Guardian.

Example: an internal link must resolve to an existing target.

Native rules must be configurable or disableable when they are not universal.

### 6.2 Project profile rule

A repository-specific policy declared in a Knowledge Guardian profile.

Example: every active Architecture Decision must declare an owner.

### 6.3 Formal schema or executable contract

A machine-verifiable contract such as JSON Schema, OpenAPI, YAML Schema, front-matter schema, event contract, or ontology schema.

Example: the `status` field is required and must contain an allowed value.

### 6.4 Repository-declared canonical source

A document or artifact explicitly declared authoritative for a concept, definition, policy, or model.

Example: a glossary declares `Professional` as the canonical term while another active specification uses `User` for the same concept.

## 7. Required structure

A finding must contain:

- `contract`;
- `id`;
- `fingerprint`;
- `rule_id`;
- `type`;
- `category`;
- `title`;
- `description`;
- `authority`;
- `subject`;
- `evidence`;
- `analysis`;
- `impact`;
- `confidence`;
- `treatment`;
- `recommendation`;
- `review`;
- `generated_at`.

## 8. Observation and inference model

The contract separates three concepts:

### 8.1 Evidence

The source material that can be inspected again, such as a path, line, value, excerpt, checksum or repository snapshot.

### 8.2 Observation

A factual statement describing what the evidence shows.

Example:

```yaml
analysis:
  observation: AGENTS.md references docs/agent-policy.md, which does not exist in the repository snapshot.
```

### 8.3 Inference

A conclusion derived from the observation. It must include a rationale and must not be presented as direct evidence.

Example:

```yaml
analysis:
  inference:
    statement: Agents may fail to load mandatory operating guidance.
    rationale: AGENTS.md is declared as an agent entry point and the referenced target is unavailable.
```

Rules:

- `analysis.observation` is mandatory for every finding;
- `analysis.inference` is mandatory for interpretative findings;
- inference is optional for normative findings;
- impact statements may use an inference, but they must not rewrite the inference as a confirmed fact unless supported by direct evidence.

## 9. Evidence model

Evidence must be reproducible and traceable.

Each evidence item must identify:

- evidence type;
- resource path or identifier;
- location scope;
- observed value or excerpt;
- expected value when applicable;
- optional checksum or snapshot reference.

A finding without evidence is invalid.

## 10. Location model

Every subject and evidence item must declare a location scope.

Allowed location scopes:

- `exact`: a precise line, column, JSON pointer or section is available;
- `resource_level`: the observation applies to the resource as a whole;
- `relationship_level`: the observation concerns a relation between resources rather than one exact position;
- `not_available`: the analyzer cannot obtain a more precise location.

Rules:

- `exact` requires at least one locator such as line, JSON pointer or section;
- all non-exact scopes require a reason;
- `not_available` must not be used when a deterministic analyzer could reasonably provide an exact location;
- absence of location data without an explicit scope and reason is invalid.

## 11. Impact model

Impact is mandatory from v0.1.

### 11.1 Impact status

Allowed states:

- `known`: the consequence is supported by direct evidence;
- `potential`: the consequence is plausible and supported, but not confirmed;
- `unknown`: repository context is insufficient to determine the consequence;
- `not_applicable`: the finding has no meaningful downstream consequence beyond the violation itself.

When impact is `unknown`, the finding must explain why.

### 11.2 Impact level

Allowed levels:

- `critical`;
- `high`;
- `medium`;
- `low`;
- `none`;
- `unknown`.

### 11.3 Impact dimensions

A finding may affect one or more dimensions:

- `engineering`;
- `agent_behavior`;
- `governance`;
- `operational`;
- `onboarding`;
- `compliance`;
- `product`.

The system must not infer dimensions without evidence or a documented rationale.

## 12. Confidence model

Confidence represents the strength of the conclusion, not the size of the consequence.

Allowed levels:

- `high`;
- `medium`;
- `low`.

A confidence rationale is mandatory.

## 13. Treatment matrix

Impact level and confidence determine a recommended treatment group.

| Group | Typical impact | Typical confidence | Recommended treatment |
|---|---|---|---|
| `confirmed_critical` | critical | high | urgent human decision; may justify a gate after approval |
| `confirmed_actionable` | high | high | prioritize remediation |
| `probable_risk` | high or critical | medium | prioritized human review |
| `investigative` | high or critical | low | investigate before accepting the conclusion |
| `routine_improvement` | medium or low | high | add to normal backlog |
| `informational` | low or medium | low | expose as information without urgency |

The JSON Schema validates allowed values. A separate deterministic policy validator will validate matrix coherence. The matrix recommends treatment; it does not authorize autonomous remediation, rejection or blocking.

## 14. Human review model

The final decision always belongs to a human reviewer.

Allowed decision states:

- `pending_review`;
- `accepted`;
- `revision_requested`;
- `cancelled`.

A cancellation should record a reason to improve rules and evaluation datasets.

## 15. Recommendation model

A recommendation describes a proposed next action. It must not be phrased as an autonomous command unless a previously approved policy explicitly permits automation.

Recommendations should be proportional, reversible where practical, traceable to the evidence and explicit about human approval.

## 16. Stable identity and deduplication

Every finding must contain a deterministic `fingerprint` derived from at least:

- `rule_id`;
- normalized subject resource;
- normalized location scope and locator;
- normalized authority type and reference;
- normalized observed condition.

The same logical divergence in the same repository state must produce the same fingerprint across repeated scans.

The human-facing `id` may be derived from the fingerprint or stored separately. The `id` is for presentation; the fingerprint is the logical identity used for deduplication, history and comparison across scans.

## 17. Validity criteria

A finding is valid only when:

- it declares the contract version;
- it has a deterministic fingerprint;
- it has an explicit authority source;
- it identifies a concrete subject;
- subject and evidence locations are explicit or justified;
- it contains reproducible evidence;
- observation is explicit and separate from inference;
- interpretative findings contain an inference and require review;
- impact is present and uncertainty is explicit;
- confidence is declared with rationale;
- treatment is derived from the approved matrix;
- recommendation is proportional to evidence;
- review state is present.

## 18. Invalidity criteria

A finding must be rejected or cancelled when:

- authority cannot be identified;
- evidence cannot be reproduced;
- the rule does not apply to the subject;
- the fingerprint is absent or unstable;
- location is omitted without an explicit scope and reason;
- observation and inference are conflated;
- an interpretative finding has no explicit inference;
- the finding duplicates another active finding;
- the impact is fabricated or overstated;
- the conclusion exceeds the available evidence;
- the canonical source is not actually declared authoritative;
- the issue has already been resolved or superseded;
- the observation is merely a preference not configured by the project.

## 19. Example

```yaml
contract:
  name: knowledge-guardian-finding
  version: 0.1.0

id: KGF-8A3D9F
fingerprint: sha256:8a3d9f0b18e1b27a
rule_id: KG-LINK-001
type: normative
category: broken_reference
title: Broken internal reference in agent entry point
description: AGENTS.md references a file that does not exist.

authority:
  type: native_rule
  reference: KG-LINK-001

subject:
  resource: AGENTS.md
  location:
    scope: exact
    line_start: 42
    line_end: 42

evidence:
  - type: unresolved_reference
    resource: AGENTS.md
    location:
      scope: exact
      line_start: 42
      line_end: 42
    observed: docs/agent-policy.md
    expected: existing repository resource

analysis:
  observation: AGENTS.md references docs/agent-policy.md, which does not exist in the analyzed repository snapshot.
  inference:
    statement: Agents and contributors may fail to load mandatory operating guidance.
    rationale: AGENTS.md is declared as an entry point and the referenced guidance is unavailable.

impact:
  status: potential
  level: high
  dimensions:
    - agent_behavior
    - onboarding
  statement: Agents and contributors may fail to load mandatory operating guidance.

confidence:
  level: high
  rationale: The referenced path does not exist in the analyzed repository snapshot.

treatment:
  group: confirmed_actionable
  recommended_action: prioritize_remediation

recommendation:
  summary: Correct the reference or restore the missing target after human validation.

review:
  required: true
  status: pending_review

generated_at: 2026-08-02T20:49:00-03:00
```

## 20. Product principles preserved

- evidence matters more than declarations;
- findings require explicit authority;
- deterministic and interpretative claims remain distinguishable;
- observations and inferences remain separate;
- impact is retained from the beginning;
- uncertainty must be visible;
- findings have stable logical identity;
- the treatment matrix supports prioritization, not autonomous decision-making;
- humans retain final authority;
- accepted, revised and cancelled findings become product-learning signals.

## 21. Next validation step

Create a golden baseline containing 10 to 20 reviewed cases covering:

- valid normative findings;
- valid interpretative findings;
- exact, resource-level and relationship-level locations;
- unknown impact;
- high-impact, low-confidence investigation;
- stable fingerprint behavior across repeated cases;
- accepted findings;
- revision requests;
- cancelled findings;
- examples that must not generate findings.
