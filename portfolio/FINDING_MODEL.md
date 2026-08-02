# Knowledge Guardian — Finding Model

**Status:** Draft for implementation  
**Version:** 0.1  
**Updated:** 2026-08-02

## 1. Purpose

This document defines what constitutes a valid finding in Knowledge Guardian.

A finding is not an opinion, an undocumented preference, or an autonomous decision. It is a structured analysis result supported by evidence and tied to an explicit authority source.

Knowledge Guardian analyzes, classifies, and recommends. A human reviewer remains responsible for accepting, requesting revision, or cancelling the finding.

## 2. Definition

> A finding is a structured, evidence-backed statement that identifies a divergence between an observed repository state and an explicitly defined rule, policy, contract, or canonical expectation.

A valid finding must answer:

1. What was observed?
2. Where was it observed?
3. Which authority defines the expected state?
4. What evidence supports the conclusion?
5. What impact is known, potential, unknown, or not applicable?
6. How confident is the system in the conclusion?
7. What treatment is recommended?
8. What is the human review status?

## 3. Non-findings

The following must not be emitted as findings:

- unsupported opinions;
- undocumented style preferences;
- recommendations without a detected divergence;
- conclusions without a traceable authority source;
- runtime claims inferred only from aspirational documentation;
- semantic claims presented as facts without confidence and human review;
- impact statements invented without supporting context;
- duplicated findings representing the same rule, subject, and evidence.

## 4. Finding types

### 4.1 Normative finding

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

### 4.2 Interpretative finding

An interpretative finding is produced when detecting the divergence requires contextual or semantic interpretation.

Typical authority sources:

- repository-declared canonical source;
- semantic comparison between documents;
- conceptual-versus-runtime analysis;
- inferred terminology conflict.

Interpretative findings:

- must expose confidence;
- must require human review;
- must not become blocking gates automatically;
- must distinguish evidence from inference.

## 5. Authority model

Every finding must identify exactly one primary authority source.

### 5.1 Native framework rule

A general rule supplied by Knowledge Guardian.

Example: an internal link must resolve to an existing target.

Native rules must be configurable or disableable when they are not universal.

### 5.2 Project profile rule

A repository-specific policy declared in a Knowledge Guardian profile.

Example: every active Architecture Decision must declare an owner.

### 5.3 Formal schema or executable contract

A machine-verifiable contract such as JSON Schema, OpenAPI, YAML Schema, front-matter schema, event contract, or ontology schema.

Example: the `status` field is required and must contain an allowed value.

### 5.4 Repository-declared canonical source

A document or artifact explicitly declared authoritative for a concept, definition, policy, or model.

Example: a glossary declares `Professional` as the canonical term while another active specification uses `User` for the same concept.

## 6. Required structure

A finding must contain:

- `id`;
- `rule_id`;
- `type`;
- `category`;
- `title`;
- `description`;
- `authority`;
- `subject`;
- `evidence`;
- `impact`;
- `confidence`;
- `treatment`;
- `recommendation`;
- `review`;
- `generated_at`.

## 7. Evidence model

Evidence must be reproducible and traceable.

Each evidence item should identify:

- evidence type;
- resource path or identifier;
- location when available;
- observed value or excerpt;
- expected value when applicable;
- optional checksum or snapshot reference.

Evidence and interpretation must remain separate.

A finding without evidence is invalid.

## 8. Impact model

Impact is mandatory from v0.1.

### 8.1 Impact status

Allowed states:

- `known`: the consequence is supported by direct evidence;
- `potential`: the consequence is plausible and supported, but not confirmed;
- `unknown`: repository context is insufficient to determine the consequence;
- `not_applicable`: the finding has no meaningful downstream consequence beyond the violation itself.

When impact is `unknown`, the finding must explain why.

### 8.2 Impact level

Allowed levels:

- `critical`;
- `high`;
- `medium`;
- `low`;
- `none`;
- `unknown`.

### 8.3 Impact dimensions

A finding may affect one or more dimensions:

- `engineering`;
- `agent_behavior`;
- `governance`;
- `operational`;
- `onboarding`;
- `compliance`;
- `product`.

The system must not infer dimensions without evidence or a documented rationale.

## 9. Confidence model

Confidence represents the strength of the conclusion, not the size of the consequence.

Allowed levels:

- `high`;
- `medium`;
- `low`.

A confidence rationale is mandatory.

Typical interpretation:

- `high`: direct and reproducible evidence with little ambiguity;
- `medium`: evidence is meaningful but context or interpretation remains incomplete;
- `low`: evidence is weak, indirect, or requires investigation.

## 10. Treatment matrix

Impact level and confidence determine a recommended treatment group.

| Group | Typical impact | Typical confidence | Recommended treatment |
|---|---|---|---|
| `confirmed_critical` | critical | high | urgent human decision; may justify a gate after approval |
| `confirmed_actionable` | high | high | prioritize remediation |
| `probable_risk` | high or critical | medium | prioritized human review |
| `investigative` | high or critical | low | investigate before accepting the conclusion |
| `routine_improvement` | medium or low | high | add to normal backlog |
| `informational` | low or medium | low | expose as information without urgency |

The matrix recommends treatment. It does not authorize autonomous remediation, rejection, or blocking.

## 11. Human review model

The final decision always belongs to a human reviewer.

Allowed decision states:

- `pending_review`;
- `accepted`;
- `revision_requested`;
- `cancelled`.

### 11.1 Accepted

The reviewer confirms that the finding is correct, relevant, and actionable.

### 11.2 Revision requested

The reviewer considers the finding potentially useful but requires changes to evidence, impact, confidence, classification, or recommendation.

### 11.3 Cancelled

The reviewer rejects the finding as incorrect, irrelevant, duplicated, superseded, or unsupported.

A cancellation should record a reason to improve rules and evaluation datasets.

## 12. Recommendation model

A recommendation describes a proposed next action. It must not be phrased as an autonomous command unless a previously approved policy explicitly permits automation.

Examples:

- correct a broken reference;
- identify and approve one canonical source;
- add missing metadata;
- investigate whether the document is still active;
- compare the specification with runtime evidence;
- request review from the responsible owner.

## 13. Validity criteria

A finding is valid only when:

- it has an explicit authority source;
- it identifies a concrete subject;
- it contains reproducible evidence;
- impact is present and uncertainty is explicit;
- confidence is declared with rationale;
- treatment is derived from the approved matrix;
- recommendation is proportional to evidence;
- review state is present;
- normative and interpretative claims are not conflated.

## 14. Invalidity criteria

A finding must be rejected or cancelled when:

- authority cannot be identified;
- evidence cannot be reproduced;
- the rule does not apply to the subject;
- the finding duplicates another active finding;
- the impact is fabricated or overstated;
- the conclusion exceeds the available evidence;
- the canonical source is not actually declared authoritative;
- the issue has already been resolved or superseded;
- the observation is merely a preference not configured by the project.

## 15. Stable identity and deduplication

The implementation should derive a stable fingerprint from at least:

- `rule_id`;
- subject resource;
- normalized location;
- normalized authority reference;
- normalized observed condition.

This fingerprint supports deduplication and comparison across scans.

The human-facing `id` may be generated from this fingerprint or stored separately.

## 16. Example

```yaml
id: KGF-8A3D9F
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
    line_start: 42
    line_end: 42

evidence:
  - type: unresolved_reference
    resource: AGENTS.md
    observed: docs/agent-policy.md
    expected: existing repository resource

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

generated_at: 2026-08-02T20:36:00-03:00
```

## 17. Product principles preserved

- evidence matters more than declarations;
- findings require explicit authority;
- deterministic and interpretative claims remain distinguishable;
- impact is retained from the beginning;
- uncertainty must be visible;
- the treatment matrix supports prioritization, not autonomous decision-making;
- humans retain final authority;
- accepted, revised, and cancelled findings become product-learning signals.

## 18. Next validation step

Create a golden baseline containing 10 to 20 reviewed cases covering:

- valid normative findings;
- valid interpretative findings;
- unknown impact;
- high-impact, low-confidence investigation;
- accepted findings;
- revision requests;
- cancelled findings;
- examples that must not generate findings.
