# Knowledge Guardian — RAID Log

**Status:** Active
**Version:** 0.4
**Updated:** 2026-08-02

## Risks

| ID | Risk | Probability | Impact | Response | Status |
|---|---|---:|---:|---|---|
| R-001 | Findings generate excessive false positives | Medium | High | Preserve negative fixtures and measure real-repository precision | Mitigated manually; open for delivery |
| R-002 | Product scope expands into a generic code-analysis platform | High | High | Maintain explicit non-goals and repository-knowledge boundary | Open |
| R-003 | Semantic analysis creates unsupported conflict claims | Medium | High | Require authority, inference, confidence and human review | Mitigated by baseline |
| R-004 | Framework imposes one governance model on every repository | Medium | High | Use configurable profiles, schemas and exemptions | Open |
| R-005 | Reports are technically correct but not actionable | Medium | High | Retain reviewer rubric and revision workflow | Partially mitigated |
| R-006 | AI-native positioning lacks evidence beyond documentation linting | Medium | Medium | Validate agent-behavior impact in real repositories | Open |
| R-007 | Performance degrades on large repositories | Medium | Medium | Define supported segment and measure scanner performance | Open |
| R-008 | CI/CD integration begins before quality is established | Medium | High | Keep delivery and enforcement separately gated | Controlled |
| R-009 | Golden cases fit the contract rather than challenge it | Medium | High | Add real-repository and external-review evidence | Reduced, still open |
| R-010 | A single reviewer creates false confidence | High | Medium | Treat baseline as initial evidence and add reviewers later | Open |
| R-011 | Repository document model becomes a universal document ontology | Medium | High | Bound vocabulary to v0.1 scanner and reporting use cases | Controlled in shaping |
| R-012 | Heuristic classification is presented as explicit repository truth | Medium | High | Require provenance, confidence and `unknown` state | Mitigated in model; delivery pending |
| R-013 | Path-based identity loses continuity across renames | High | Medium | Explicitly defer rename continuity and preserve snapshot identity | Accepted limitation |
| R-014 | Relationship vocabulary expands without downstream value | Medium | Medium | Require a rule, report or profile use case for each relationship | Open for delivery review |

## Assumptions

| ID | Assumption | Validation | Status |
|---|---|---|---|
| A-001 | Maintainers value explicit canonical-source governance | Repository audits and interviews | Unvalidated broadly |
| A-002 | Deterministic checks provide sufficient v0.1 value | Knowledge Guardian and Meu PDI scans | Unvalidated |
| A-003 | Markdown is the correct first supported format | Repository sample analysis | Partially validated |
| A-004 | Proposal-first operation lowers adoption risk | Tech Lead review workflow | Partially supported |
| A-005 | Users will maintain project profiles | Profile usability test | Unvalidated |
| A-006 | Finding contract represents realistic positive and negative cases | 12-case manual golden baseline | Supported for shaping |
| A-007 | One primary document type and one primary knowledge layer are sufficient for v0.1 | Contract fixtures and first repository inventory | Open |
| A-008 | Repository-relative path is sufficient physical identity for v0.1 | Contract tests and rename scenarios | Accepted provisionally |

## Issues

| ID | Issue | Impact | Owner | Next action | Status |
|---|---|---|---|---|---|
| I-001 | No parser or relationship-discovery engine exists | KG-004 cannot prove content reachability or validate links | Tech Lead | Shape KG-004 and KG-005 separately | Open, intentionally deferred |
| I-002 | Finding contract lacked hardening semantics | Ambiguous evidence | Product + Tech Lead | KGD-010 hardening | Resolved |
| I-003 | No evaluation baseline existed | Trust could not be assessed | Product + Tech Lead | Complete 12-case baseline | Resolved manually |
| I-004 | License not selected | Public adoption ambiguous | Product Owner | Decide before first public release | Open |
| I-005 | No executable fixture validator or regression suite | Manual evidence cannot prevent regressions | Tech Lead | Preserve validator output as regression evidence | Resolved in KG-002 delivery |
| I-006 | Repository document model has no executable schema | KG-003 cannot depend on stable contracts | Tech Lead | Preserve accepted contracts as the dependency baseline | Resolved by KG-002 acceptance |

## Dependencies

| ID | Dependency | Needed for | Strategy | Status |
|---|---|---|---|---|
| D-001 | Representative repositories | Product validation | Knowledge Guardian and Meu PDI | Available |
| D-002 | Repository-aware reviewers | Acceptance measurement | Expand beyond initial Tech Lead later | Initial reviewer available |
| D-003 | Markdown parser and path-resolution strategy | Scanner | Technical spike after KG-002 contract delivery | Open |
| D-004 | Versioned finding schema | Stable integration | Use contract `0.1.0` | Available |
| D-005 | Repository profiles | Context-aware governance | Shape against KG-002 model | Open |
| D-006 | Stable baseline snapshots | Reproducible manual evidence | Three controlled snapshots | Available |
| D-007 | Executable JSON Schema validator | Regression evidence | Select during delivery planning | Open |
| D-008 | Versioned repository-document contracts | KG-003 through KG-006 | Bounded KG-002 delivery slice | Pending Tech Lead decision |
| D-009 | Case-sensitivity and path-normalization policy | Stable resource identity | Encode repository policy in contracts and tests | Shaped, not implemented |

## Review policy

- Review weekly and at every product checkpoint.
- Every high-impact risk must have an active response.
- Assumptions must become evidence, rejection or explicit acceptance.
- Issues must identify one next action.
- Resolved issues remain visible when they explain material decisions.
