# KG-003 — Markdown Repository Discovery Delivery Plan

**Status:** `approved_for_discovery_delivery`
**Version:** 0.1  
**Date:** 2026-08-02  
**Backlog item:** `KG-003`  
**Depends on:** accepted KG-002 contracts, `KGD-014`, and approved KG-003 boundaries in `KGD-015`

## 1. Objective

Implement a deterministic, read-only inventory of regular `.md` and `.mdx` files beneath an explicitly supplied repository root. The increment emits one `RepositorySnapshot`, zero or more valid `Resource` records, and bounded diagnostics. It must not parse document contents or execute governance rules.

## 2. Consumers and outcome

**Primary consumers:** later KG-004 through KG-006 increments and the Tech Lead reviewing repository evidence.

**Expected outcome:** the same unchanged filesystem input and caller context produce equivalent, schema-valid, deterministically ordered inventory records.

## 3. Authorized delivery scope

### Included

- explicit repository-root input;
- caller-supplied repository, ref, optional commit SHA and capture timestamp;
- recursive enumeration of regular `.md` and `.mdx` files;
- inclusion of hidden directories except `.git` and configured ignores;
- no-follow and no-inventory behavior for symlinks;
- normalized repository-relative paths using `/` separators;
- deterministic sorting by normalized path;
- observed file size;
- optional SHA-256 checksum, enabled by default;
- `RepositorySnapshot` and `Resource` records conforming to KG-002 schemas;
- bounded diagnostics for excluded, unreadable or invalid paths;
- deterministic tests and delivery evidence.

### Excluded

- Git command execution or `.git` inspection;
- Markdown, MDX, YAML, JSX or front-matter parsing;
- metadata extraction;
- document classification;
- relationship or link discovery;
- entry-point and orphan analysis;
- graph construction;
- rule execution;
- finding generation;
- report rendering;
- automatic file modification;
- CI/CD integration;
- KG-004 and later backlog items.

## 4. Proposed implementation boundary

The delivery slice should expose one application-level operation equivalent to:

```text
inventory_markdown_resources(config) -> InventoryResult
```

The exact language-level API is a Tech Lead implementation choice, but behavior must remain consistent with this plan.

### 4.1 Configuration interface

Required fields:

```yaml
repository_root: absolute local path
repository: owner/name or caller-defined repository identifier
ref: caller-supplied snapshot ref
captured_at: RFC 3339 timestamp
```

Optional fields and defaults:

```yaml
commit_sha: null
include_extensions: [".md", ".mdx"]
ignore_paths: []
calculate_checksum: true
follow_symlinks: false
include_hidden_directories: true
```

Invariants:

- `repository_root` is required and must resolve to an existing directory;
- callers cannot enable symlink traversal in v0.1;
- `.git` is always ignored and cannot be re-enabled;
- extensions are matched case-insensitively, while the original path casing is preserved;
- ignore paths are interpreted relative to the repository root after normalization;
- caller-supplied Git context is evidence and must not be inferred or altered.

## 5. Output model

### 5.1 Inventory result

```yaml
snapshot: RepositorySnapshot
resources: Resource[]
diagnostics: DiscoveryDiagnostic[]
summary:
  files_examined: integer
  resources_emitted: integer
  ignored_paths: integer
  unreadable_files: integer
  symlinks_ignored: integer
  checksum_failures: integer
  duration_ms: integer
```

`resources` must be sorted by normalized path.

### 5.2 Diagnostic representation

Diagnostics are operational evidence, not findings.

```yaml
diagnostic_id: deterministic identifier
code: enum
level: info | warning | error
path: normalized repository-relative path or null
operation: enumerate | normalize | stat | read | checksum
message: bounded human-readable description
cause_type: stable technical category or null
```

Initial diagnostic codes:

- `PATH_IGNORED`;
- `SYMLINK_IGNORED`;
- `UNSUPPORTED_EXTENSION`;
- `PATH_OUTSIDE_ROOT`;
- `PATH_NORMALIZATION_FAILED`;
- `FILE_UNREADABLE`;
- `FILE_STAT_FAILED`;
- `CHECKSUM_FAILED`.

Rules:

- diagnostics must not contain file contents, secrets, stack traces or absolute paths;
- unreadable files produce `FILE_UNREADABLE` and no incomplete `Resource`;
- a checksum failure produces `CHECKSUM_FAILED` and no `Resource`, because checksum is enabled by default and the observed record would otherwise be incomplete for the selected configuration;
- ignored symlinks produce `SYMLINK_IGNORED`;
- expected exclusions do not abort the inventory;
- invalid root configuration fails before snapshot emission.

## 6. Identity and normalization

- `snapshot_id` is derived deterministically from caller-supplied repository context according to KG-002 contracts;
- `resource_id` is derived from the normalized repository-relative path;
- checksum is observed metadata, not identity;
- absolute local paths must not appear in emitted records or diagnostics;
- parent traversal and resolved paths outside the repository root are rejected;
- path separators are normalized to `/`;
- equivalent separator forms yield the same resource identity;
- rename continuity remains outside this slice.

## 7. Delivery sequence

1. define configuration and result types;
2. define diagnostic type and stable codes;
3. implement root validation and path normalization;
4. implement deterministic filesystem enumeration;
5. apply `.git`, configured-ignore and extension policies;
6. enforce no-follow/no-inventory symlink behavior;
7. collect file size and optional SHA-256;
8. emit KG-002 snapshot/resource records;
9. sort outputs deterministically;
10. add deterministic fixtures and tests;
11. validate outputs against KG-002 schemas;
12. record execution evidence and limitations;
13. submit for Tech Lead quality review.

## 8. Deterministic test plan

### Configuration

- missing repository root fails;
- nonexistent root fails;
- file supplied as root fails;
- caller context is preserved exactly;
- checksum can be disabled;
- symlink following cannot be enabled.

### Inclusion and exclusion

- empty repository emits one snapshot and zero resources;
- root-level `.md` is included;
- nested `.md` and `.mdx` are included;
- uppercase extension variants are included;
- non-Markdown files are excluded;
- `.git` is always excluded;
- `.ai` and `.github` are included unless configured otherwise;
- configured ignore paths are excluded;
- symlinked files and directories are ignored.

### Paths and identity

- paths are repository-relative;
- separators normalize to `/`;
- parent traversal is rejected;
- resolved paths outside root are rejected;
- resources are ordered lexicographically by normalized path;
- repeated runs over unchanged input produce equivalent snapshot/resource data, excluding measured duration.

### Failure behavior

- unreadable file produces one diagnostic and no resource;
- stat failure is bounded;
- checksum failure is bounded;
- one file failure does not suppress valid resources from other files;
- emitted diagnostics contain no absolute paths or file contents.

### Contract validation

- every snapshot validates against `repository-snapshot.schema.json`;
- every resource validates against `resource.schema.json`;
- invalid generated records fail tests;
- existing KG-002 contract tests continue to pass.

### Cross-platform evidence

At minimum, tests must run on the implementation environment and include deterministic cases representing Windows and POSIX separator/path inputs. A second operating system is recommended before release but is not an entry condition for this bounded increment.

## 9. Observability

The implementation must expose or record:

- start and completion timestamps;
- duration;
- configured root represented without persisting the absolute path in durable output;
- file counts examined, included, ignored and failed;
- checksum enabled/disabled;
- diagnostic counts by code;
- schema-validation result;
- unexpected exceptions.

No telemetry may include file contents. Operational logs must remain separable from the contract output.

## 10. Rollback

The delivery must remain isolated from later rules and integrations.

Rollback procedure:

1. stop invoking the inventory operation;
2. revert the KG-003 delivery commits or PR;
3. preserve KG-002 schemas and tests unchanged;
4. delete generated ephemeral inventory output if present;
5. record the defect and return to shaping if observable behavior or a boundary must change.

No repository source file is modified by the scanner, so rollback requires no content restoration.

## 11. Acceptance criteria

- [x] explicit root and caller context are required;
- [x] only regular `.md`/`.mdx` resources are emitted;
- [x] hidden directories follow the approved policy;
- [x] symlinks are neither followed nor inventoried;
- [x] `.git` is always ignored;
- [x] paths and IDs are normalized and deterministic;
- [x] output contains one valid snapshot and valid resources;
- [x] checksum is SHA-256, optional and enabled by default;
- [x] unreadable or failed files emit diagnostics without incomplete resources;
- [x] output ordering is deterministic;
- [x] unchanged input yields equivalent records across repeated runs;
- [x] deterministic tests cover configuration, scope, paths, failures and ordering;
- [x] KG-002 contract tests remain green;
- [x] observability evidence is recorded;
- [ ] rollback is documented and tested at process level;
- [x] no parser, classifier, relationship, finding or reporting logic is introduced;
- [ ] Tech Lead records a separate quality disposition before merge.

## 12. Delivery evidence required

The execution report must record:

- branch and commits;
- operating system and runtime versions;
- test commands;
- KG-002 regression result;
- KG-003 test counts and failures;
- repeated-run determinism result;
- schema-validation result;
- diagnostic scenarios exercised;
- `git diff --check` result;
- scope verification;
- known limitations;
- rollback verification.

## 13. Risks and responses

| Risk | Response |
|---|---|
| Filesystem differences produce unstable output | Normalize paths, sort output and test platform-specific forms |
| Ignore rules become a hidden profile engine | Support only explicit relative ignore paths in this slice |
| Diagnostics evolve into findings | Keep separate type, lifecycle and output collection |
| Checksum increases cost | Make optional and measure duration/counts |
| Symlinks escape root | Never follow or inventory them |
| File changes during scan produce inconsistent metadata | Document snapshot as best-effort filesystem observation; atomic filesystem snapshotting is deferred |
| Permission tests differ by OS | Use injectable filesystem seams or deterministic fakes where direct permission manipulation is unreliable |

## 14. Quality gate

The Tech Lead recorded the following disposition:

`approved_for_discovery_delivery`

This approval authorizes only the bounded read-only inventory described here. It does not authorize KG-004, parsing, classification, findings, reports or CI/CD integration.

**Authority:** Human Tech Lead decision recorded in `KGD-016`.
