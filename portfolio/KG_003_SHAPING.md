# KG-003 — Markdown Repository Discovery Shaping

**Status:** Approved with boundaries — delivery authorization pending
**Version:** 0.1
**Date:** 2026-08-02
**Backlog item:** `KG-003`
**Depends on:** accepted KG-002 contracts and `KGD-014`

## 1. Problem

Knowledge Guardian has stable `RepositorySnapshot` and `Resource` contracts, but it has no deterministic way to inventory Markdown resources from a repository root. Without that inventory, later document classification, entry-point analysis, link validation and orphan analysis have no reproducible input boundary.

## 2. Target consumer and outcome

**Primary consumer:** the future KG-004 through KG-006 delivery slices and the human Tech Lead reviewing repository evidence.

**Expected outcome:** given an explicitly selected repository root and capture context, produce a deterministic, read-only inventory of supported Markdown resources with normalized repository-relative paths and enough observed metadata to populate KG-002 contracts.

## 3. Evidence and authority

- `portfolio/OPERATING_MODEL.md` requires deterministic checks before semantic analysis and read-only operation by default.
- `portfolio/REPOSITORY_DOCUMENT_MODEL.md` defines repository-relative resource identity, path normalization, supported formats and snapshot traceability.
- `portfolio/decisions/KGD-014.md` accepts KG-002 contracts as the dependency baseline.
- `schemas/document-model/0.1.0/repository-snapshot.schema.json` and `resource.schema.json` provide the executable contract boundary.
- `portfolio/ROADMAP.md` identifies deterministic repository and Markdown discovery as the v0.1 outcome.

## 4. Proposed bounded slice

### Included

- accept an explicit repository root as input;
- capture repository/ref/commit context when supplied by the caller;
- enumerate regular files under the selected root;
- include `.md` and `.mdx` resources only;
- normalize separators and repository-relative paths;
- reject or report paths that escape the selected root;
- emit `RepositorySnapshot` and `Resource` records using KG-002 contracts;
- preserve deterministic ordering by normalized path;
- record observed size and checksum only when calculated by the implementation;
- operate read-only and produce reproducible validation evidence.

### Excluded

- Markdown or YAML parsing;
- front matter or metadata extraction;
- document classification;
- relationship or link discovery;
- entry-point or orphan analysis;
- graph construction;
- rule execution or finding generation;
- report rendering;
- automatic file changes;
- CI/CD integration;
- KG-004, KG-005, KG-006 or any later item.

## 5. Acceptance criteria

- [x] Explicit repository root is required; no implicit current-directory authority.
- [ ] Only regular `.md` and `.mdx` files are included in this slice.
- [ ] Output contains one valid `RepositorySnapshot` and one valid `Resource` per included file.
- [ ] Every resource path is normalized, repository-relative and stable across equivalent separator forms.
- [ ] Absolute paths, parent traversal and paths outside the selected root are rejected or recorded as deterministic exclusions.
- [ ] Output ordering is deterministic and independent of filesystem enumeration order.
- [x] Missing Git context is represented as unavailable evidence, not invented values.
- [ ] Repeated execution over an unchanged input produces equivalent contract records.
- [ ] Tests cover empty repositories, nested paths, mixed extensions, excluded files, traversal attempts and deterministic ordering.
- [x] No parser, classifier, relationship detector, finding generator or report renderer is introduced.
- [ ] Delivery documentation records commands, versions, evidence, limitations and rollback.

## 6. Approved boundaries

The following decisions were approved by the human Tech Lead/Product assessment and are part of the KG-003 shaping baseline:

| Boundary | Approved behavior |
|---|---|
| Git context | `repository`, `ref`, `commit_sha` (optional) and `captured_at` are supplied explicitly by the caller. Automatic Git discovery and `.git` inspection are outside this slice. |
| Unreadable files | Continue processing other files; record a bounded diagnostic; do not emit an incomplete `Resource`; do not generate a finding. |
| Checksum | Calculate optional SHA-256 for readable files by default, with configuration to disable it. The checksum is observed content metadata, not primary identity. |
| Symlinks | `follow_symlinks = false`; do not follow or inventory symlinked Markdown; record it as ignored. |
| Hidden directories | Include by default, always exclude `.git`, and support an explicit configurable ignore-path list. |
| `.mdx` | Include in the inventory as `format: markdown`; preserve the `.mdx` path; do not parse JSX, imports, front matter or metadata. |

These boundaries resolve the six shaping questions. Delivery must still define the deterministic diagnostic representation and configuration interface without expanding into findings or parsing.

## 7. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Filesystem order produces unstable evidence | Sort normalized paths before emission |
| Symlinks escape the selected root | Define and test a no-follow policy before delivery |
| Git context is mistaken for repository truth | Treat supplied context and observed context as distinct evidence |
| Hidden files or ignored files change inventory unexpectedly | Make scope policy explicit and test it |
| Scanner slice expands into parser or rule engine | Keep contract output limited to snapshot and resource records |
| Platform path behavior diverges | Test Unix and Windows absolute/traversal forms against one normalization policy |

## 8. Decision gate

This artifact authorizes the bounded discovery-delivery proposal only. It does not authorize scanner implementation. Delivery may begin after a bounded delivery plan is recorded and the Tech Lead records `approved_for_discovery_delivery`.

**Next authorized action:** Create the KG-003 delivery plan, including the diagnostic representation and configuration interface, for a separate Tech Lead delivery decision.
