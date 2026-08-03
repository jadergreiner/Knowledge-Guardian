# KG-004 — Relationship Input and Producer Shaping

**Status:** Technical proposal — human decision pending
**Version:** 0.1
**Date:** 2026-08-03
**Backlog item:** `KG-004`
**Parent plan:** `portfolio/KG_004_DELIVERY_PLAN.md`

## 1. Observed evidence

- The executable contract already exists at `schemas/document-model/0.1.0/relationship.schema.json`.
- The contract requires `contract`, `relationship_id`, `snapshot_id`, `source_document_id`, `target`, `type` and `provenance`.
- The contract supports target kinds `document_id`, `relative_path`, `external_uri` and `unresolved`.
- The contract includes relationship types such as `links_to`, `references`, `supersedes`, `implements`, `governs` and `unknown`.
- `portfolio/REPOSITORY_DOCUMENT_MODEL.md` describes a broader conceptual shape with `source_resource_id`, `target_resource_id`, `target_exists`, `authority_reference` and `confidence`; those fields are not currently required by the executable schema.
- KG-003 does not parse content or discover relationships.

## 2. Proposed schema decision

Reuse `relationship.schema.json` version `0.1.0` as the input contract for KG-004. Do not add fields or create a second relationship envelope in this slice.

The delivery adapter must accept:

```yaml
snapshot_id: snapshot:<id>
relationships:
  - <schema-valid Relationship record>
```

Every relationship must belong to the supplied snapshot. KG-004 must validate the record against the existing schema and perform application-level checks for snapshot consistency and repository-relative target resolution.

The conceptual model/schema difference is recorded as a compatibility risk, not silently resolved. `authority_reference`, `confidence`, inverse derivation and `target_exists` remain deferred until a separately authorized contract revision or adapter projection.

## 3. Proposed producer boundary

The producer is an explicit caller-supplied `RelationshipProvider` adapter. It may be backed by fixtures, a project profile or a future parser, but the producer mechanism must be declared by the caller and identified in evidence.

```text
caller
  └── RelationshipProvider(snapshot_id)
        └── schema-valid Relationship records
              └── KG-004 validation and reachability calculation
```

KG-004 is a consumer and validator, not a relationship extractor. It must not read Markdown/MDX content, execute link parsing, inspect Git or infer relationships from names, link counts or semantic similarity.

The future internal-link parser belongs to a separately shaped KG-005 producer. Its eventual output may use `provenance: explicit_link`, but KG-005 is not authorized by this artifact.

## 4. Reachability projection

For v0.1 reachability, only relationships satisfying all of these conditions are traversable:

- `type: links_to`;
- `provenance: explicit_link` or another explicitly approved deterministic source;
- target kind `document_id` or `relative_path`;
- source and resolved target are present in the KG-003 inventory;
- relationship and snapshot identifiers are valid.

`external_uri` and `unresolved` targets are retained as input evidence but cannot create an internal reachability edge. Invalid, incomplete or non-traversable inputs produce bounded diagnostics and affected `indeterminate` or `not_evaluated` states; they never prove `candidate_orphan`.

## 5. Acceptance criteria for the proposal

- [ ] Tech Lead confirms reuse of `relationship.schema.json` `0.1.0`.
- [ ] Tech Lead confirms `RelationshipProvider` as the explicit producer boundary.
- [ ] The producer identifies snapshot and provenance for every input batch.
- [ ] KG-004 validates schema, snapshot consistency and internal target resolution.
- [ ] No relationship extraction or content parsing is introduced.
- [ ] Only approved internal deterministic edges participate in reachability.
- [ ] Contract/model differences are documented and not silently patched.
- [ ] KG-003 and KG-002 regressions remain unaffected.

## 6. Decision gate

This artifact is a shaping proposal. It authorizes neither schema modification nor implementation.

**Recommended decision:** approve the existing executable schema and caller-supplied producer boundary for the KG-004 delivery plan.

**Next gate:** `approved_for_implementation`, `revision_requested` or `rejected`.
