# Knowledge Guardian — Product Status

**Date:** 2026-08-02  
**Overall status:** KG-002 accepted; KG-003 approved for merge
**Confidence:** High

## Current position

The finding contract is validated for v0.1 use and the initial manual baseline is complete. KG-002 contract delivery has executable evidence: 14 valid fixtures passed, 14 invalid fixtures were rejected and unexpected failures were zero.

`KG-003 — Markdown Repository Discovery` has completed shaping with six human-approved boundaries. A bounded delivery plan now defines configuration, diagnostics, deterministic tests, observability, rollback and acceptance evidence.

No filesystem scanner, parser, traversal engine or finding engine has been started.

## Operating-model position

```text
SENSE → FRAME → DISCOVER → DECIDE → SHAPE → DELIVER
                                              ↑
                              KG-003 delivery accepted; merge authorized
```

## KG-003 planned scope

The authorized increment is limited to:

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

Implementation returned with executable test evidence, schema-validation results, repeated-run determinism evidence, diagnostics exercised, scope verification and rollback confirmation. The Tech Lead approved the bounded delivery for merge. KG-004 remains separately gated.
