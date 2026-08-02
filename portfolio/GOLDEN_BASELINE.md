# Knowledge Guardian — Golden Baseline Plan

**Status:** Shaped — ready for curation  
**Version:** 0.1  
**Updated:** 2026-08-02

## 1. Purpose

The golden baseline validates whether the draft finding contract can represent realistic repository-governance cases without confusing evidence, inference, impact, treatment, recommendation, and human disposition.

This is a discovery and quality artifact. It is not an implemented scanner and does not authorize delivery expansion.

## 2. Related work

- `KG-001` — Define the trusted finding contract;
- `KG-010` — Establish the v0.1 evaluation baseline;
- `D-001` — Knowledge Guardian self-audit;
- `D-004` — Finding trust test;
- `portfolio/FINDING_MODEL.md`;
- `schemas/finding.schema.json`.

## 3. Target consumer and outcome

**Primary reviewer:** Human Tech Lead with repository context.  
**Secondary consumer:** Product Manager assessing trust, usability, and decision quality.

**Expected outcome:** Reviewers can understand, reproduce, classify, and decide on representative findings and non-findings using the versioned contract.

## 4. Bounded scope

The first baseline contains 12 manually curated cases from the Knowledge Guardian repository.

| Case group | Count | Purpose |
|---|---:|---|
| Normative valid findings | 4 | Exercise deterministic authority and evidence |
| Interpretative valid findings | 2 | Exercise explicit inference, confidence, and mandatory review |
| Revision-requested findings | 1 | Test partial disagreement without full rejection |
| Cancelled findings | 1 | Test false positive, unsupported, duplicate, or irrelevant cases |
| Expected non-findings | 4 | Protect against undocumented preferences and unsupported conclusions |

The baseline may expand to 20 cases only when a discovered contract gap requires another representative fixture.

## 5. Required case format

Each case must contain:

- `case_id`;
- `case_type`: `positive_finding` or `expected_non_finding`;
- repository snapshot or commit reference;
- source resources and locations;
- rule or authority under test;
- expected result;
- rationale;
- expected human disposition;
- relevant risk or assumption;
- fixture file when the expected result is a finding.

Positive finding fixtures must conform to `schemas/finding.schema.json` and declare contract version `0.1.0`.

## 6. Initial case catalogue

| ID | Case | Expected result | Coverage |
|---|---|---|---|
| GB-001 | Internal Markdown reference points to a missing target | Normative finding | Native rule, exact location, high confidence |
| GB-002 | Required profile metadata is absent | Normative finding | Project-profile authority |
| GB-003 | JSON or YAML artifact violates a declared schema | Normative finding | Formal-contract authority |
| GB-004 | Configured repository entry point does not exist | Normative finding | Deterministic repository policy |
| GB-005 | Active document diverges from a declared canonical term | Interpretative finding | Canonical authority, explicit inference |
| GB-006 | Document appears to describe future behavior as current behavior | Interpretative finding | Potential impact, medium or low confidence |
| GB-007 | Evidence is correct but impact is overstated | Revision requested | Human correction of analysis |
| GB-008 | Suspected conflict lacks a declared authority source | Cancelled | Unsupported finding |
| GB-009 | Alternative wording with no configured terminology rule | Expected non-finding | Undocumented preference |
| GB-010 | Aspirational documentation lacks runtime confirmation | Expected non-finding | No unsupported runtime claim |
| GB-011 | Intentional standalone document is explicitly exempted | Expected non-finding | Exception handling |
| GB-012 | Duplicate evidence represents an existing active finding | Expected non-finding | Fingerprint and deduplication |

The catalogue defines test intent. Specific repository evidence must be captured during curation rather than invented.

## 7. Reviewer rubric

The human reviewer evaluates each positive finding across five dimensions.

| Dimension | Question | Pass condition |
|---|---|---|
| Correctness | Does the observation match the repository snapshot? | Evidence is reproducible |
| Authority | Does the cited authority define the expected state? | Authority is explicit and applicable |
| Interpretation | Does the inference remain within the evidence? | No hypothesis is presented as fact |
| Actionability | Is the recommendation proportional and useful? | A responsible human can decide the next action |
| Classification | Are impact, confidence, and treatment coherent? | Classification reflects evidence and consequence |

### Human dispositions

- `accepted`: all material dimensions pass;
- `revision_requested`: the underlying divergence may be valid, but one or more material dimensions require correction;
- `cancelled`: the finding is unsupported, inapplicable, duplicated, superseded, or irrelevant;
- `pending_review`: no human decision has yet been recorded.

A reviewer reason is mandatory for `revision_requested` and `cancelled`.

## 8. Measurement

### 8.1 Contract conformance

```text
schema_conformance_rate = valid_positive_fixtures / total_positive_fixtures
```

Entry target: `100%`. A positive fixture that cannot conform represents either a fixture defect or a contract gap.

### 8.2 Reviewer acceptance

```text
reviewer_acceptance_rate = accepted_findings / reviewed_positive_findings
```

This first baseline establishes a measurement, not a release threshold. Results must not be optimized by removing difficult cases.

### 8.3 Negative-case protection

```text
negative_case_pass_rate = correctly_suppressed_non_findings / total_expected_non_findings
```

Entry target: `100%` for the manually curated baseline.

### 8.4 Ambiguity log

Every case that requires interpretation not represented by the current contract must create an ambiguity record containing:

- case ID;
- missing or unclear concept;
- reviewer impact;
- proposed contract change;
- decision: revise now, defer, or reject.

## 9. Dependencies and risks

### Dependencies

- hardened finding contract `0.1.0`;
- repository snapshot with stable commit reference;
- human reviewer with repository context;
- a mechanism to validate fixtures against JSON Schema.

### Risks

- cases may be designed to fit the contract rather than challenge it;
- one reviewer may not represent broader maintainer behavior;
- interpretative fixtures may introduce unsupported evidence;
- manual validation may hide implementation constraints.

### Responses

- include expected non-findings and cancellation cases;
- preserve difficult and ambiguous cases;
- record inference and confidence explicitly;
- treat the result as initial evidence, not general validation.

## 10. Entry criteria

Curation may begin when:

- the contract hardening approved in `KGD-010` is present in both model and schema;
- backlog and status reflect the completed hardening;
- the case structure and reviewer rubric are approved;
- the repository snapshot is selected.

## 11. Exit criteria

The baseline checkpoint is complete when:

- 12 representative cases are versioned;
- every positive fixture passes schema validation;
- all expected non-findings include a documented suppression rationale;
- human dispositions and reasons are recorded;
- false-positive, ambiguity, and contract-gap observations are catalogued;
- product records whether `KG-001` is validated or requires revision.

Completion of this checkpoint permits the project to decide whether to start `KG-002`. It does not automatically authorize implementation.

## 12. Next action

Select a stable Knowledge Guardian commit and curate `GB-001` through `GB-004` as the first deterministic batch. Do not create interpretative fixtures until the deterministic evidence pattern is reviewed.