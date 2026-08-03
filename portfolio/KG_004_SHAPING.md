# KG-004 — Entry Points and Orphan Documents Shaping

**Status:** Approved with boundaries — reachability delivery plan approved; implementation pending
**Version:** 0.1
**Date:** 2026-08-03
**Backlog item:** `KG-004`
**Depends on:** merged KG-003 inventory and a separately authorized relationship-input boundary

## 1. Problem

KG-003 now produces a deterministic inventory of repository resources, but the product cannot safely say where a human or agent should begin reading, or whether a resource is unreachable, without explicit entry-point authority and relationship evidence.

## 2. Target consumer and outcome

**Primary consumer:** a Tech Lead reviewing repository navigation evidence and future KG-005 link-validation output.

**Expected outcome:** represent configured or convention-based entry points as valid `EntryPoint` records and expose orphan candidates only when the reachability inputs and authority are explicit.

## 3. Evidence and authority

- `portfolio/REPOSITORY_DOCUMENT_MODEL.md` defines entry-point sources, audiences, priority and the rule that multiple entry points are not inherently a problem.
- `schemas/document-model/0.1.0/entry-point.schema.json` defines the executable `EntryPoint` contract.
- KG-003 emits the resource inventory but intentionally does not parse content or discover relationships.
- `portfolio/OPERATING_MODEL.md` requires evidence/inference separation and forbids silent authority selection.

## 4. Proposed bounded slice

### Included

- accept KG-003 resources and snapshot context as input;
- accept explicit project-profile entry-point declarations;
- apply a small, documented native-convention table only when enabled by configuration;
- emit schema-valid `EntryPoint` records with source, audience, path and optional priority;
- report missing configured entry-point targets as bounded diagnostics or normative candidates, without emitting findings;
- accept an externally supplied relationship/reachability set for orphan-candidate calculation;
- distinguish `unreachable_candidate` from confirmed orphan status;
- preserve deterministic ordering and evidence references.

### Excluded

- Markdown, MDX, YAML or front-matter parsing;
- discovering entry points from document content;
- internal-link extraction or validation;
- relationship discovery or graph construction;
- canonical-source selection;
- finding generation or report rendering;
- automatic file changes;
- KG-005, KG-006 and later items;
- CI/CD or blocking behavior.

## 5. Entry-point authority boundary

Supported sources in this slice:

| Source | Input | Authority |
|---|---|---|
| `project_profile` | explicit caller/profile declaration | normative configuration |
| `native_convention` | enabled, versioned convention table | deterministic rule |
| `explicit_metadata` | deferred until a parser/metadata slice exists | not available in KG-004 |

The approved precedence is:

```text
project_profile
      ↓
native_conventions
      ↓
no_entry_point
```

`project_profile` declarations have authority. Native conventions may complement the profile, but they must not silently override it. When candidates conflict, the system must preserve the conflict as deterministic evidence and must not select one automatically. If no source supplies an entry point, the absence is emitted as evidence and is not silently corrected.

The implementation must not infer an entry point from arbitrary document content or silently promote `README.md` to canonical authority. A native convention identifies a starting location only; it does not establish subject authority.

## 6.1 Recorded decision — entry-point sources

**Disposition:** `approved_with_boundaries`.

**Decision:** use `project_profile`, then enabled `native_conventions`, then explicit `no_entry_point` evidence, with the precedence and conflict rules above.

**Authority:** Tech Lead decision recorded in the project evolution workflow.

**Still blocked:** implementation, relationship discovery, orphan findings and automatic conflict resolution.

## 7. Recorded decision — orphan states and native conventions

**Disposition:** `approved_with_boundaries` for delivery-plan shaping.

The v0.1 output states are:

| State | Meaning |
|---|---|
| `reachable` | An explicit path exists from a resolved entry point. |
| `candidate_orphan` | No path exists after complete evaluation; this is review evidence, not a finding. |
| `excluded` | The project profile or policy excludes the resource. |
| `not_evaluated` | The resource did not participate in analysis. |
| `indeterminate` | Errors or incomplete evidence prevent a conclusion. |

`unreachable` must never be promoted to confirmed `orphan`. A resource may be `candidate_orphan` only when it is inventoried, is not an entry point, is not excluded, all required resources were evaluated, and no structural error makes the graph incomplete. If no entry point is resolved, resources are `no_entry_point` evidence and are not classified as `candidate_orphan`.

The v0.1 native-convention table is limited to exact, case-sensitive files at the repository root:

| Path | Audience |
|---|---|
| `README.md` | `human`, `contributor` |
| `AGENTS.md` | `agent` |
| `CONTRIBUTING.md` | `contributor` |
| `SECURITY.md` | `contributor`, `security` |
| `CODE_OF_CONDUCT.md` | `contributor` |
| `CLAUDE.md` | `agent` |
| `GEMINI.md` | `agent` |

Subdirectory `README.md`, `index.md`, `docs/`, `SUMMARY.md`, tool configuration files, content inference, approximate names, case-insensitive matching and link-count heuristics are excluded. The profile may add, remove or replace conventions. Multiple entry points remain valid; conventions do not establish canonicality.

For each evaluated resource, reachability evidence must include the resource, state, resolved entry point when applicable, deterministic path or reason. Paths are selected by shortest distance, then `entry_point_id`, then lexicographic path sequence.

## 8. Orphan boundary

An inventory alone cannot prove reachability. KG-004 must use one of these explicit modes:

1. **Relationship-input mode:** accept externally supplied typed relationships and calculate reachability from declared entry points without discovering or validating those relationships. This is the recommended delivery mode.
2. **Entry-point-only mode:** may emit `no_entry_point` or `not_evaluated` evidence, but must not classify resources as `candidate_orphan` without explicit relationship input.

The delivery plan must select one mode or implement both with separate outputs. A missing relationship input is not evidence that a document is orphaned.

## 9. Acceptance criteria

- [ ] Entry-point declarations require an explicit snapshot and repository-relative path.
- [ ] Every emitted `EntryPoint` validates against the KG-002 schema.
- [ ] Profile declarations preserve audience, source and priority deterministically.
- [ ] Native conventions are versioned, opt-in and documented.
- [ ] Explicit metadata is not used before a parser/metadata authorization.
- [ ] Missing targets do not produce incomplete `EntryPoint` records.
- [ ] Multiple entry points remain valid unless an explicit rule says otherwise.
- [ ] Orphan output is clearly labeled as candidate evidence, not a confirmed finding.
- [ ] Reachability calculations use only supplied relationships and declared entry points.
- [ ] No link parser, relationship discovery, finding, report or graph engine is introduced.
- [ ] Deterministic tests cover empty inventory, configured entries, missing targets, duplicate entries, native conventions and unreachable candidates.
- [ ] KG-003 regression remains green.

## 10. Open decisions before delivery

1. Confirm the exact relationship input schema and producer before delivery implementation.
2. Confirm whether missing configured targets are diagnostics only in v0.1.
3. Confirm duplicate declaration handling: deterministic merge or separate evidence records.

These decisions change public behavior and require a separate Tech Lead delivery decision.

## 11. Decision gate

This artifact authorizes the bounded reachability delivery plan. It does not authorize KG-004 implementation, orphan findings, link parsing or relationship discovery.

**Next gate:** implementation authorization after the remaining input-contract decisions are closed.
