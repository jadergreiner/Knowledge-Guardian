# Knowledge Guardian — Discovery

**Status:** Active
**Version:** 0.1
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

| ID | Assumption | Risk if false | Validation method |
|---|---|---|---|
| A-001 | Teams cannot reliably identify canonical knowledge sources | Product value decreases | Repository audit and maintainer interview |
| A-002 | Broken navigation and stale knowledge materially affect engineering work | Findings become cosmetic | Incident, onboarding and rework examples |
| A-003 | AI agents amplify the cost of conflicting context | AI-native positioning weakens | Compare agent behavior with clean and conflicting context |
| A-004 | Maintainers will accept proposal-first, read-only analysis | Adoption barrier increases | Prototype workflow test |
| A-005 | Deterministic checks deliver enough initial value | v0.1 value is insufficient | Scan real repositories and review findings |
| A-006 | Users will configure repository profiles | Generic-only product may be required | Profile creation usability test |

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

**Output:** golden baseline and acceptance examples.

### D-002 — Meu PDI repository audit

Use Meu PDI as the first complex repository case, with emphasis on `.ai`, `apos`, `knowledge`, `docs`, agent instructions and architectural sources.

**Output:** prioritized problem inventory and project profile requirements.

### D-003 — Maintainer workflow interview

Document one concrete episode where conflicting, stale, missing or orphaned knowledge caused delay or error.

**Output:** verified jobs, pains and current workarounds.

### D-004 — Finding trust test

Present sample findings with evidence, confidence, severity and remediation to reviewers.

**Output:** minimum trusted finding contract.

### D-005 — Competitive and adjacent-tool analysis

Compare documentation linters, link checkers, knowledge graphs, architecture governance tools, code-quality platforms and AI context systems.

**Output:** differentiation and build-versus-integrate decisions.

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

## Current priority

Validate the minimum finding contract and construct the golden baseline for deterministic v0.1 scans.
