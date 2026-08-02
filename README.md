# Knowledge Guardian

> AI-native knowledge governance for software repositories.

**Knowledge Guardian** is a reusable framework and agent skill for analyzing, validating, and improving the knowledge architecture of a software repository.

It helps teams keep documentation, architecture decisions, ontologies, glossaries, specifications, runbooks, and agent context consistent, trustworthy, and navigable.

The project does not treat documentation as a secondary artifact.

It treats knowledge as part of the system architecture.

---

## Why Knowledge Guardian exists

Modern repositories are consumed by both humans and AI agents.

However, most repositories contain:

- duplicated sources of truth;
- inconsistent terminology;
- stale architecture documents;
- undocumented decisions;
- orphaned files;
- broken references;
- missing trust signals;
- conceptual models that diverge from runtime;
- specifications that no longer match implementation;
- agent instructions spread across unrelated files.

These problems create a form of **knowledge debt**.

Knowledge debt reduces engineering velocity, weakens governance, increases onboarding cost, and causes AI agents to operate with incomplete or conflicting context.

Knowledge Guardian identifies these problems and produces actionable improvement proposals.

---

## Mission

> Transform repository documentation into trustworthy, consistent, navigable, and AI-ready knowledge.

---

## What Knowledge Guardian is

Knowledge Guardian is designed as a layered project.

```text
Knowledge Guardian
├── Governance Framework
├── Reusable Agent Skill
├── Rule Engine
├── Project Profiles
├── Metadata and Trust-Signal Analysis
├── Documentation Graph Analysis
├── Semantic Consistency Analysis
├── Reporting
└── Future CLI and CI/CD Integrations
```

The initial implementation focuses on the reusable agent skill.

The architecture allows the same governance model to later support:

- command-line execution;
- pull request review;
- CI/CD quality gates;
- repository dashboards;
- Obsidian-compatible knowledge graphs;
- IDE integrations;
- multi-agent workflows.

---

## Core principles

### Knowledge is architecture

Documentation, decisions, terminology, specifications, and operational context influence how software is designed and changed.

They must be governed with the same discipline as code.

### Canonical sources must be explicit

A repository should clearly state which document is authoritative for each subject.

### Evidence matters more than declarations

A document saying that something exists does not prove that it is implemented, configured, executed, or verified.

### Humans remain decision makers

Knowledge Guardian proposes improvements.

It does not silently rewrite governance, architecture, or product decisions.

### Semantic consistency is a quality attribute

The same term should not represent different concepts without an explicit distinction.

### Runtime and intent are different layers

Conceptual models, specifications, and runtime models should be related, but never silently treated as identical.

### Governance should be extensible

Rules should be configured through reusable policies and project profiles, not hard-coded for a single repository.

---

## Main capabilities

### Repository knowledge discovery

Knowledge Guardian maps the documentation structure of a repository and identifies:

- entry-point documents;
- governance files;
- product vision;
- architecture documents;
- ADRs;
- specifications;
- ontologies;
- glossaries;
- runbooks;
- agent context;
- operational documentation.

---

### Metadata governance

The skill reviews structured metadata and can propose fields such as:

```yaml
type: ArchitectureDecision
title: Decision title
description: Short description
owner: platform-team
status: active
version: 1.0.0
generated:
  by: agent-name
  at: 2026-08-02T18:00:00-03:00
verified:
  by: human-reviewer
  at: 2026-08-02T19:00:00-03:00
sources:
  - id: source-name
    resource: path/to/source.md
stale_after: 2026-11-02
```

The exact metadata schema is configurable.

Knowledge Guardian does not assume that every repository must use the same fields.

---

### Trust-signal analysis

The framework can evaluate whether a document provides enough information to determine:

- who created it;
- who verified it;
- when it was last reviewed;
- which sources support it;
- whether it is active, deprecated, draft, or archived;
- when it should be reviewed again;
- whether it describes runtime, intent, or future design.

---

### Documentation graph analysis

Knowledge Guardian can analyze links and relationships between documents.

It identifies:

- orphaned documents;
- missing entry points;
- broken links;
- circular navigation;
- duplicated navigation blocks;
- documents without parent context;
- references to deprecated files;
- weak or ambiguous reading paths.

The output can be used by tools such as Obsidian to visualize the repository as a knowledge graph.

---

### Semantic consistency analysis

The skill searches for terms that may be ambiguous, overloaded, or inconsistently defined.

Examples:

```text
User ≠ Account ≠ Professional Profile
Plan ≠ Development Cycle
Task ≠ Step
Consent ≠ Authorization
Absence ≠ Denial
Specification ≠ Implementation
Spec-Driven Development ≠ Software Design Document
```

The analysis should always preserve project-specific language and explicit human decisions.

---

### Canonical-source detection

Knowledge Guardian helps answer:

```text
Where is the authoritative source for this concept?
```

It can detect competing definitions across:

- README files;
- product vision;
- ontologies;
- ADRs;
- specifications;
- agent instructions;
- code comments;
- wiki pages;
- runtime models.

When sources conflict, the tool reports the divergence instead of selecting one silently.

---

### Conceptual versus executable models

Knowledge Guardian distinguishes between:

| Layer | Purpose |
|---|---|
| Conceptual | Describes business concepts and strategic intent |
| Specification | Defines expected behavior and constraints |
| Executable knowledge | Represents code, schemas, tests, and runtime contracts |
| Operational | Describes deployment, incidents, monitoring, and support |
| Agent context | Defines how AI agents should navigate and act |

This distinction prevents agents from treating aspirational documents as implemented behavior.

---

### Governance reports

A typical report may contain:

- repository knowledge map;
- source-of-truth conflicts;
- missing metadata;
- broken references;
- semantic inconsistencies;
- stale documents;
- orphaned documents;
- trust-signal gaps;
- recommended navigation;
- prioritized improvement proposals;
- suggested pull request scope.

---

## Operating model

Knowledge Guardian should follow a proposal-first workflow:

```text
Discover
    ↓
Classify
    ↓
Analyze
    ↓
Compare
    ↓
Report
    ↓
Propose
    ↓
Human approval
    ↓
Apply
    ↓
Verify
```

By default, the skill should not modify files without explicit authorization.

---

## Layers

### 1. Core framework

Defines:

- document model;
- metadata model;
- relationship model;
- finding categories;
- confidence levels;
- evidence requirements;
- report structure.

---

### 2. Rule engine

Rules are reusable and configurable.

Examples:

- required metadata by document type;
- naming conventions;
- canonical terminology;
- allowed document relationships;
- stale-document thresholds;
- source-of-truth policies;
- required trust signals;
- navigation requirements.

---

### 3. Agent skill

The skill guides an AI agent through:

- repository discovery;
- document classification;
- semantic analysis;
- metadata review;
- relationship analysis;
- proposal generation;
- validation.

---

### 4. Project profiles

Profiles adapt the generic framework to a repository.

Example:

```yaml
profile:
  name: meu-pdi
  entry_points:
    - README.md
    - AGENTS.md
    - AI_CONTEXT.md
    - ONTOLOGY.md

  canonical_sources:
    product_vision: docs/product/PRODUCT_VISION.md
    ontology_runtime: knowledge/ontology/professional.ontology
    governance: AGENTS.md

  terminology:
    SDD: Spec-Driven Development
```

Profiles should extend the framework without changing its core.

---

### 5. CLI

Planned command-line capabilities:

```bash
knowledge-guardian scan .
knowledge-guardian metadata .
knowledge-guardian graph .
knowledge-guardian semantic-check .
knowledge-guardian report .
```

---

### 6. CI/CD integration

Future integrations may support:

- pull request comments;
- governance quality gates;
- semantic drift detection;
- broken-link validation;
- stale-document warnings;
- metadata validation;
- documentation graph diffs.

---

## Example use cases

### Review a single document

```text
Analyze this architecture document.
Identify missing metadata, weak trust signals,
ambiguous terminology, and missing navigation.
Propose changes but do not apply them.
```

### Review repository knowledge architecture

```text
Map all governance, product, architecture, ontology,
specification, runbook, and agent-context files.
Identify canonical sources and conflicts.
```

### Prepare documentation for AI agents

```text
Evaluate whether an AI agent can determine:
- where to start;
- which sources are authoritative;
- what is current;
- what is conceptual;
- what is implemented;
- which decisions are human-approved.
```

### Review semantic drift

```text
Find terms that have multiple definitions across
documentation, code, ontologies, and specifications.
```

---

## Finding categories

Knowledge Guardian may classify findings as:

| Category | Description |
|---|---|
| Missing metadata | Required governance metadata is absent |
| Weak trust signal | Verification, source, owner, or freshness is unclear |
| Semantic inconsistency | A term has conflicting meanings |
| Source conflict | Multiple documents claim authority |
| Documentation drift | Documentation diverges from runtime |
| Broken reference | A link or target does not exist |
| Orphan document | A document has no discoverable navigation path |
| Stale knowledge | Content has not been reviewed within policy |
| Duplicate knowledge | The same definition is maintained in multiple places |
| Architectural ambiguity | Boundaries between concepts or layers are unclear |
| Agent-context gap | Agents cannot determine how to operate safely |
| Improvement opportunity | A non-blocking enhancement |

---

## Severity model

```text
Critical
High
Medium
Low
Informational
```

Severity should consider:

- impact on engineering decisions;
- impact on AI behavior;
- risk of incorrect implementation;
- governance risk;
- operational risk;
- ease of remediation;
- whether the issue affects a canonical source.

---

## Suggested repository structure

```text
Knowledge-Guardian/
├── README.md
├── LICENSE
├── AGENTS.md
├── skill/
│   ├── SKILL.md
│   ├── workflows/
│   ├── prompts/
│   └── templates/
├── core/
│   ├── models/
│   ├── rules/
│   ├── analyzers/
│   └── reporters/
├── profiles/
│   ├── generic/
│   └── examples/
├── schemas/
│   ├── metadata.schema.json
│   ├── profile.schema.json
│   └── report.schema.json
├── examples/
│   ├── sample-repository/
│   └── sample-report/
├── tests/
├── docs/
│   ├── architecture.md
│   ├── rule-authoring.md
│   ├── profiles.md
│   └── roadmap.md
└── pyproject.toml
```

This structure is an initial proposal and may evolve.

---

## Initial roadmap

### v0.1 — Knowledge discovery

- repository scanning;
- document classification;
- entry-point detection;
- basic metadata review;
- broken-link detection;
- governance report.

### v0.2 — Semantic consistency

- glossary detection;
- conflicting-term analysis;
- canonical-source comparison;
- conceptual versus runtime classification.

### v0.3 — Knowledge graph

- relationship extraction;
- orphan detection;
- graph export;
- Obsidian-compatible output.

### v0.4 — Configurable governance

- project profiles;
- custom rules;
- metadata schemas;
- severity configuration.

### v0.5 — CLI and automation

- local CLI;
- structured reports;
- pull request integration;
- CI/CD checks.

### v1.0 — Community-ready framework

- stable rule API;
- reusable agent skill;
- plugin architecture;
- documented extension model;
- community rule packs;
- multi-agent workflow support.

---

## Non-goals

Knowledge Guardian is not intended to:

- replace human architecture decisions;
- automatically rewrite product strategy;
- declare documentation correct without evidence;
- infer runtime behavior from documentation alone;
- force a single metadata standard on every project;
- turn every document into the same template;
- become a generic code linter.

---

## Design philosophy

A repository should make it possible to answer:

```text
What is this project?
Where should I start?
Which document is authoritative?
What is current?
What is conceptual?
What is implemented?
What has been verified?
Who made the decision?
What should be read next?
```

If humans or AI agents cannot answer these questions, the repository has a knowledge governance problem.

---

## Status

Knowledge Guardian is currently in its initial design phase.

The first milestone is a reusable agent skill capable of reviewing a document or repository and producing a structured governance proposal.

---

## Contributing

Contributions are welcome in areas such as:

- governance rules;
- metadata schemas;
- semantic analysis;
- documentation graphs;
- agent workflows;
- project profiles;
- CLI implementation;
- CI/CD integrations;
- examples and case studies.

Before submitting a contribution, document:

- the problem;
- expected behavior;
- evidence;
- proposed rule;
- false-positive risks;
- validation strategy.

---

## License

Choose an open-source license before the first public release.

Common options include:

- Apache License 2.0;
- MIT License.

Apache 2.0 may be preferable if the project evolves into a framework with plugins and commercial adoption.

---

## Repository

**Knowledge Guardian**

AI-native knowledge governance for repositories, humans, and autonomous agents.
