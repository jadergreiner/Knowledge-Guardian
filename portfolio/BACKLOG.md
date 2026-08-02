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
**Status:** Draft complete — contract hardening approved, then golden-baseline validation  
**Outcome:** Reviewers can understand, reproduce and decide on every finding.

**Completed outputs:**

- `portfolio/FINDING_MODEL.md`;
- `schemas/finding.schema.json`;
- authority-source model for native rules, project profiles, schemas/contracts and canonical sources;
- distinction between normative and interpretative findings;
- mandatory impact model with explicit uncertainty states;
- confidence model and six treatment groups;
- explicit human decision states: `pending_review`, `accepted`, `revision_requested` and `cancelled`.

**Contract hardening required before baseline:**

- [ ] add explicit observation and inference structures;
- [ ] make deterministic `fingerprint` mandatory for logical identity and deduplication;
- [ ] add explicit finding contract name and semantic version;
- [ ] require exact location or an explicit resource-level/not-applicable rationale.

**Acceptance criteria:**

- [~] finding contains stable ID and rule ID; `id` and `rule_id` exist, but mandatory fingerprint is pending;
- [x] category, type, confidence and treatment group are explicit;
- [~] repository resource, location and reproducible evidence are provided; location semantics require hardening;
- [~] observation is separated from inference; conceptual rule exists, schema structure is pending;
- [x] authority source is mandatory and traceable;
- [x] impact is mandatory and may explicitly be `known`, `potential`, `unknown` or `not_applicable`;
- [x] recommendation is actionable without becoming an automatic decision at the conceptual level;
- [x] human review and final disposition are represented;
- [~] JSON schema is versioned; schema standard and `$id` exist, explicit contract version is pending;
- [ ] golden baseline validates representative findings and non-findings;
- [ ] reviewer feedback confirms that the contract is understandable, reproducible and actionable;
- [ ] false-positive, ambiguity and cancellation cases are exercised.

**Validation dependency:** `KG-010 — Establish the v0.1 evaluation baseline`.

**Exit condition:** KG-001 may be marked validated only after contract hardening is complete, the golden baseline is reviewed by the human Tech Lead, and any required contract revisions are incorporated.

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

**Entry dependency:** KG-001 contract hardening completed.

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
