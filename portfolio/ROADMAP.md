# Knowledge Guardian — Product Roadmap

**Status:** Draft
**Version:** 0.1
**Updated:** 2026-08-02

## Roadmap principles

- Organize work by validated outcomes, not component completion.
- Treat near-term items as higher-confidence commitments.
- Treat later items as strategic direction until discovery reduces uncertainty.
- Preserve a complete vertical slice before expanding analytical breadth.

## North Star

**Trusted Knowledge Findings Rate**

Percentage of reported findings accepted by a qualified human reviewer as correct, relevant, and actionable.

## Now — v0.1: Deterministic knowledge discovery

**Confidence:** High

### Outcome

A maintainer can scan a Markdown-based repository and receive a reproducible report about its knowledge structure and basic governance gaps.

### Scope

- repository and Markdown discovery;
- document classification;
- entry-point detection;
- metadata parsing and validation;
- internal-link validation;
- orphan document detection;
- structured finding model;
- Markdown and JSON reports;
- read-only execution;
- initial Knowledge Guardian and Meu PDI profiles.

### Exit criteria

- complete scan works on Knowledge Guardian;
- complete scan works on Meu PDI;
- deterministic findings are reproducible;
- findings contain rule, evidence, location, severity and remediation;
- reviewer acceptance rate is measured;
- false positives are catalogued.

## Next — v0.2: Canonical sources and semantic consistency

**Confidence:** Medium

### Outcome

A maintainer can identify competing definitions, ambiguous terminology, and unclear authority boundaries without the tool silently resolving conflicts.

### Candidate scope

- glossary and terminology extraction;
- canonical-source policies;
- duplicate-definition detection;
- conceptual, specification, executable and operational classification;
- semantic conflict candidates;
- confidence and evidence policies;
- human review workflow.

### Discovery gates

- define acceptable semantic false-positive rate;
- compare deterministic, embedding and LLM-assisted approaches;
- establish evaluation datasets;
- define cost and privacy boundaries.

## Later — v0.3: Documentation graph

**Confidence:** Medium-Low

### Outcome

Teams and agents can navigate repository knowledge through an explicit, queryable document graph.

### Candidate scope

- typed document relationships;
- graph export;
- graph diffs;
- weak navigation detection;
- Obsidian-compatible output;
- visualization examples.

## Later — v0.4: Configurable governance

**Confidence:** Low

### Outcome

Different repositories can adopt Knowledge Guardian through profiles, schemas and reusable rule packs without changing the core.

### Candidate scope

- project profiles;
- custom rule configuration;
- versioned schemas;
- severity policies;
- rule authoring API;
- reusable governance packs.

## Later — v0.5: CLI and CI/CD

**Confidence:** Low

### Outcome

Knowledge governance checks run locally and in pull requests with predictable performance and actionable feedback.

### Candidate scope

- stable CLI;
- baseline and incremental scans;
- pull request annotations;
- governance quality gates;
- SARIF or equivalent integration;
- report artifacts;
- suppression and waiver workflow.

## Future — v1.0: Community-ready framework

**Confidence:** Directional

### Outcome

Knowledge Guardian is a stable, extensible framework for humans and AI agents to govern repository knowledge.

### Candidate scope

- stable rule API;
- plugin architecture;
- documented extension model;
- community rule packs;
- multi-agent workflows;
- compatibility and migration policy.
