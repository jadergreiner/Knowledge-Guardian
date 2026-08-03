# Knowledge Guardian — Product Status

**Date:** 2026-08-03
**Overall status:** KG-003 merged; KG-004 reachability delivery plan approved, implementation gate pending
**Confidence:** High

## Current position

The finding contract is validated for v0.1 use and the initial manual baseline is complete. KG-002 contract delivery has executable evidence: 14 valid fixtures passed, 14 invalid fixtures were rejected and unexpected failures were zero. KG-003 read-only Markdown inventory is merged to `main`.

`KG-003 — Markdown Repository Discovery` has completed shaping with six human-approved boundaries. A bounded delivery plan now defines configuration, diagnostics, deterministic tests, observability, rollback and acceptance evidence.

No Markdown/MDX parser, relationship engine, finding engine or report renderer has been started.

## Operating-model position

```text
SENSE → FRAME → DISCOVER → DECIDE → SHAPE
                                              ↑
                              KG-004 delivery plan approved; implementation not authorized
```

## KG-003 delivered scope

The merged increment is limited to:

- explicit repository root and caller-supplied repository context;
- read-only enumeration of regular `.md` and `.mdx` files;
- hidden-directory inclusion except `.git` and configured ignores;
- no-follow/no-inventory symlink behavior;
- normalized repository-relative paths;
- deterministic ordering;
- optional SHA-256 enabled by default;
- valid `RepositorySnapshot` and `Resource` records;
- bounded operational diagnostics;
- deterministic tests, observability and rollback evidence.

Shaping: `portfolio/KG_003_SHAPING.md`.

Delivery plan: `portfolio/KG_003_DELIVERY_PLAN.md`.

Decision: `KGD-015` records the approved shaping boundaries.

KG-004 shaping: `portfolio/KG_004_SHAPING.md`.

KG-004 delivery plan: `portfolio/KG_004_DELIVERY_PLAN.md`. Relationship input proposal: `portfolio/KG_004_RELATIONSHIP_INPUT_SHAPING.md`. The plan remains limited to reachability evidence from explicit caller-supplied relationships; implementation is not authorized.

## Diagnostic boundary

Diagnostics are operational evidence, not findings. They cover ignored paths, symlinks, invalid paths, unreadable files, stat failures and checksum failures. They must not contain file contents, stack traces or durable absolute paths.

## Explicitly not authorized

- KG-004 or later implementation;
- Git command execution or `.git` inspection;
- Markdown, MDX, YAML, JSX or front-matter parsing;
- classification or metadata extraction;
- relationship, link, entry-point or orphan discovery;
- rule execution;
- finding or report generation;
- CI/CD enforcement;
- automatic repository modification.

## Delivery authorization

`approved_for_discovery_delivery` was recorded in `KGD-016`, and `approved_for_merge` was recorded in `KGD-017`. The merge approval applies only to the bounded read-only inventory defined in `KG_003_DELIVERY_PLAN.md`.

## Next checkpoint

KG-003 is merged and its delivery evidence is complete. KG-004 reachability delivery planning is approved; implementation awaits the relationship-input contract and the remaining bounded decisions.
