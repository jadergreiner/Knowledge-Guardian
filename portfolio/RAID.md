# Knowledge Guardian — RAID Log

**Status:** Active
**Version:** 0.1
**Updated:** 2026-08-02

## Risks

| ID | Risk | Probability | Impact | Response | Status |
|---|---|---:|---:|---|---|
| R-001 | Findings generate excessive false positives | Medium | High | Start with deterministic rules, golden baselines and reviewer acceptance metrics | Open |
| R-002 | Product scope expands into a generic code-analysis platform | High | High | Maintain explicit non-goals and repository-knowledge boundary | Open |
| R-003 | Semantic analysis creates unsupported claims of conflict | Medium | High | Separate observations from inferences and require confidence/evidence | Open |
| R-004 | The framework imposes one governance model on every repository | Medium | High | Use configurable profiles and schemas | Open |
| R-005 | Reports are technically correct but not actionable | Medium | High | Define trusted finding contract and test with maintainers | Open |
| R-006 | AI-native positioning lacks evidence beyond conventional documentation linting | Medium | Medium | Validate agent-behavior impact with conflicting versus governed context | Open |
| R-007 | Performance degrades on large repositories | Medium | Medium | Define supported repository segment and measure scan performance | Open |
| R-008 | CI/CD integration is introduced before quality is established | Medium | High | Keep v0.1 local/read-only and gate automation on precision targets | Open |

## Assumptions

| ID | Assumption | Validation | Status |
|---|---|---|---|
| A-001 | Maintainers value explicit canonical-source governance | Repository audits and interviews | Unvalidated |
| A-002 | Deterministic structural checks provide sufficient v0.1 value | Knowledge Guardian and Meu PDI scans | Unvalidated |
| A-003 | Markdown is the correct first supported repository-knowledge format | Repository sample analysis | Partially validated |
| A-004 | Proposal-first operation lowers adoption risk | Workflow test with maintainers | Unvalidated |
| A-005 | Users will maintain project profiles when value is clear | Profile usability test | Unvalidated |

## Issues

| ID | Issue | Impact | Owner | Next action | Status |
|---|---|---|---|---|---|
| I-001 | No implemented scanner exists yet | Product cannot produce evidence | Tech Lead | Implement first vertical slice | Open |
| I-002 | No versioned finding schema exists | Reports lack stable contract | Product + Tech Lead | Complete KG-001 | Open |
| I-003 | No evaluation baseline exists | Precision cannot be measured | Product + Tech Lead | Complete KG-010 | Open |
| I-004 | License is not yet selected | Public contribution and adoption remain ambiguous | Product Owner | Decide before first public release | Open |

## Dependencies

| ID | Dependency | Needed for | Strategy | Status |
|---|---|---|---|---|
| D-001 | Access to representative repositories | Product validation | Use Knowledge Guardian and Meu PDI first | Available |
| D-002 | Human reviewers with repository context | Finding acceptance measurement | Define review rubric and sample set | Open |
| D-003 | Markdown parser and path-resolution strategy | v0.1 scanner | Technical spike and library selection | Open |
| D-004 | Versioned JSON schemas | Stable integrations | Design before report implementation | Open |
| D-005 | Clear repository profiles | Context-aware governance | Create generic, Knowledge Guardian and Meu PDI profiles | Open |

## Review policy

- Review the RAID log weekly.
- Every high-impact risk must have an active response.
- Assumptions must be converted into evidence, rejected, or explicitly accepted.
- Issues must identify one next action.
- Dependencies must be represented in roadmap and backlog sequencing.
