# Knowledge Guardian — RAID Log

**Status:** Active
**Version:** 0.2
**Updated:** 2026-08-02

## Risks

| ID | Risk | Probability | Impact | Response | Status |
|---|---|---:|---:|---|---|
| R-001 | Findings generate excessive false positives | Medium | High | Start with deterministic rules, golden baselines and reviewer acceptance metrics | Open |
| R-002 | Product scope expands into a generic code-analysis platform | High | High | Maintain explicit non-goals and repository-knowledge boundary | Open |
| R-003 | Semantic analysis creates unsupported claims of conflict | Medium | High | Separate observations from inferences and require confidence/evidence | Mitigated in contract; validation pending |
| R-004 | The framework imposes one governance model on every repository | Medium | High | Use configurable profiles and schemas | Open |
| R-005 | Reports are technically correct but not actionable | Medium | High | Apply the reviewer rubric to golden-baseline cases | Open |
| R-006 | AI-native positioning lacks evidence beyond conventional documentation linting | Medium | Medium | Validate agent-behavior impact with conflicting versus governed context | Open |
| R-007 | Performance degrades on large repositories | Medium | Medium | Define supported repository segment and measure scan performance | Open |
| R-008 | CI/CD integration is introduced before quality is established | Medium | High | Keep v0.1 local/read-only and gate automation on baseline evidence | Controlled by operating gate |
| R-009 | Golden cases are designed to fit the contract instead of challenging it | Medium | High | Include cancellations, expected non-findings, ambiguities and difficult cases | Open |
| R-010 | A single reviewer creates false confidence about broader usability | High | Medium | Treat first baseline as initial evidence and add external reviewer tests later | Open |

## Assumptions

| ID | Assumption | Validation | Status |
|---|---|---|---|
| A-001 | Maintainers value explicit canonical-source governance | Repository audits and interviews | Unvalidated |
| A-002 | Deterministic structural checks provide sufficient v0.1 value | Knowledge Guardian and Meu PDI scans | Unvalidated |
| A-003 | Markdown is the correct first supported repository-knowledge format | Repository sample analysis | Partially validated |
| A-004 | Proposal-first operation lowers adoption risk | Workflow test with maintainers | Partially supported by Tech Lead review |
| A-005 | Users will maintain project profiles when value is clear | Profile usability test | Unvalidated |
| A-006 | The hardened finding contract can represent realistic positive and negative cases | Golden baseline | Unvalidated |

## Issues

| ID | Issue | Impact | Owner | Next action | Status |
|---|---|---|---|---|---|
| I-001 | No implemented scanner exists yet | Product cannot produce automated evidence | Tech Lead | Keep gated until contract validation | Open, intentionally deferred |
| I-002 | Finding contract lacked explicit identity, inference, version and location semantics | Baseline evidence would be ambiguous | Product + Tech Lead | Apply KGD-010 hardening | Resolved |
| I-003 | No evaluation baseline exists | Precision and trust cannot be measured | Product + Tech Lead | Curate GB-001 through GB-004 | Open |
| I-004 | License is not yet selected | Public contribution and adoption remain ambiguous | Product Owner | Decide before first public release | Open |
| I-005 | No fixture validation mechanism is selected | Schema conformance cannot be reproduced | Tech Lead | Choose validator before first fixture review | Open |

## Dependencies

| ID | Dependency | Needed for | Strategy | Status |
|---|---|---|---|---|
| D-001 | Access to representative repositories | Product validation | Use Knowledge Guardian and Meu PDI first | Available |
| D-002 | Human reviewers with repository context | Finding acceptance measurement | Use human Tech Lead for first baseline; expand later | Available for initial baseline |
| D-003 | Markdown parser and path-resolution strategy | v0.1 scanner | Technical spike and library selection | Deferred until contract gate |
| D-004 | Versioned JSON schemas | Stable fixtures and integrations | Use finding contract `0.1.0` | Available |
| D-005 | Clear repository profiles | Context-aware governance | Create Knowledge Guardian and Meu PDI profiles | Open |
| D-006 | Stable repository snapshot | Reproducible baseline evidence | Select one commit before curation | Open |
| D-007 | JSON Schema fixture validator | Baseline conformance measurement | Select a deterministic local validator | Open |

## Review policy

- Review the RAID log weekly and at every product checkpoint.
- Every high-impact risk must have an active response.
- Assumptions must be converted into evidence, rejected, or explicitly accepted.
- Issues must identify one next action.
- Dependencies must be represented in roadmap and backlog sequencing.
- Resolved issues remain visible when they explain a material product decision.
