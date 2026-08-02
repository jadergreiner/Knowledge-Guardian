# Knowledge Guardian — Product Backlog

**Status:** Active
**Version:** 0.1
**Updated:** 2026-08-02

## Prioritization model

Items are prioritized using:

- user and engineering impact;
- evidence strength;
- reduction of product or technical uncertainty;
- dependency value;
- implementation effort;
- risk of false confidence or incorrect findings.

## Now — v0.1 foundation

### KG-001 — Define the trusted finding contract

**Type:** Product foundation
**Outcome:** Reviewers can understand, reproduce and decide on every finding.

**Acceptance criteria:**

- finding contains stable ID and rule ID;
- category, severity and confidence are explicit;
- repository path and evidence are provided;
- observation is separated from inference;
- remediation is actionable;
- suppression or exception can be represented;
- JSON schema is versioned.

### KG-002 — Define the repository document model

**Type:** Technical foundation
**Outcome:** Documents can be consistently discovered and classified.

**Acceptance criteria:**

- supported document types are enumerated;
- document identity and path rules are defined;
- metadata and relationship models are versioned;
- conceptual, specification, executable, operational and agent-context layers are represented.

### KG-003 — Build Markdown repository discovery

**Type:** Delivery
**Outcome:** A repository scan produces a deterministic document inventory.

**Acceptance criteria:**

- include and exclude rules are configurable;
- ignored, generated and vendor paths are handled;
- inventory output is stable across repeated scans;
- malformed files produce bounded errors rather than scan failure.

### KG-004 — Detect entry points and orphan documents

**Type:** Delivery
**Outcome:** Maintainers can identify documents that are not reachable through intended navigation.

**Acceptance criteria:**

- configured entry points are supported;
- repository-root entry points are detected;
- reachability is calculated from internal links;
- intentional standalone documents can be exempted;
- findings contain the navigation evidence.

### KG-005 — Validate internal Markdown references

**Type:** Delivery
**Outcome:** Broken repository knowledge links are reported with reproducible evidence.

**Acceptance criteria:**

- relative file links are validated;
- anchors are validated where technically reliable;
- external links are excluded from v0.1 or handled separately;
- generated findings identify source and unresolved target.

### KG-006 — Parse and validate document metadata

**Type:** Delivery
**Outcome:** Project-specific governance metadata can be checked without enforcing one universal schema.

**Acceptance criteria:**

- YAML front matter is parsed;
- metadata requirements vary by document type and profile;
- invalid or missing fields produce structured findings;
- repositories without metadata policy can run in advisory mode.

### KG-007 — Produce Markdown and JSON reports

**Type:** Delivery
**Outcome:** Humans and automation can consume the same scan results.

**Acceptance criteria:**

- both outputs derive from the same finding model;
- summary counts and detailed findings are included;
- report identifies profile, tool version, timestamp and scan scope;
- deterministic ordering supports diff review.

### KG-008 — Create the Knowledge Guardian project profile

**Type:** Product validation
**Outcome:** The framework can govern its own repository using explicit policies.

**Acceptance criteria:**

- entry points and canonical areas are configured;
- document classifications and metadata policies are declared;
- known exceptions are documented;
- baseline report is reviewed by a human.

### KG-009 — Create the Meu PDI project profile

**Type:** Product validation
**Outcome:** v0.1 is validated against a complex AI-native repository.

**Acceptance criteria:**

- `.ai`, `apos`, `knowledge`, `docs` and agent instructions are mapped;
- canonical-source policies are declared where known;
- unsupported semantic checks are identified, not simulated;
- findings are manually reviewed and classified.

### KG-010 — Establish the v0.1 evaluation baseline

**Type:** Quality
**Outcome:** Product quality can be measured before CI/CD integration.

**Acceptance criteria:**

- golden repositories or fixtures exist;
- expected findings and non-findings are versioned;
- precision and reviewer acceptance are measured;
- false positives and false negatives are catalogued;
- regression tests protect rule behavior.

## Discovery queue

### KG-D01 — Determine the acceptable false-positive threshold

### KG-D02 — Validate the minimum metadata fields users will maintain

### KG-D03 — Evaluate report formats used in existing engineering workflows

### KG-D04 — Compare semantic-analysis strategies for v0.2

### KG-D05 — Define waiver, suppression and expiration semantics

## Explicitly deferred

- automatic file rewriting;
- autonomous canonical-source selection;
- broad source-code analysis;
- external-link crawling;
- semantic drift claims without an evaluation baseline;
- pull request blocking gates before precision is established.
