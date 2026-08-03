# Knowledge Guardian — Repository Document Model

**Status:** Shaped — pending Tech Lead delivery decision  
**Version:** 0.1  
**Date:** 2026-08-02  
**Backlog item:** `KG-002`

## 1. Purpose

Define the minimum repository-document model required for Knowledge Guardian to discover, classify and relate knowledge artifacts consistently before scanner implementation begins.

This artifact is a shaping output. It defines product and architectural boundaries, invariants and acceptance criteria. It does not authorize implementation and is not yet a public executable schema.

## 2. Problem

Repository files cannot be safely analyzed only as paths and extensions. The product must distinguish:

- a physical resource from its logical document identity;
- document type from knowledge layer;
- declared metadata from inferred classification;
- navigation relationships from authority relationships;
- current repository state from future or conceptual intent;
- explicit project policy from framework defaults.

Without these distinctions, later rules for entry points, orphan detection, metadata validation and canonical sources may generate inconsistent findings or false confidence.

## 3. Consumers

### Primary

- repository discovery and inventory;
- entry-point and reachability analysis;
- metadata validation;
- internal-link validation;
- project-profile evaluation;
- report generation.

### Secondary

- human Tech Leads and maintainers reviewing repository knowledge;
- AI agents selecting safe context;
- future graph and semantic-analysis capabilities.

## 4. Bounded scope

### Included in KG-002

- logical document identity;
- repository-relative resource identity;
- supported resource formats;
- document types;
- knowledge layers;
- metadata representation;
- relationship representation;
- classification provenance and confidence;
- explicit exceptions;
- lifecycle state;
- invariants and validation examples.

### Excluded from KG-002

- filesystem scanning implementation;
- Markdown parsing implementation;
- graph traversal algorithms;
- rule execution;
- finding generation;
- report rendering;
- semantic embeddings or ontology induction;
- multi-repository identity;
- persistent database design.

## 5. Core entities

```text
RepositorySnapshot
    ├── Resource
    │     └── Document
    │           ├── Metadata
    │           ├── Classification
    │           └── TrustSignals
    ├── Relationship
    ├── EntryPoint
    └── Exception
```

### 5.1 RepositorySnapshot

Represents the immutable repository state used by one analysis run.

Required concepts:

- repository identifier;
- repository-relative root;
- branch, tag or ref when available;
- commit SHA when available;
- capture timestamp;
- profile identifier and version;
- include and exclude scope.

A document observation must always be traceable to one snapshot.

### 5.2 Resource

Represents a physical repository object addressed by normalized repository-relative path.

Minimum attributes:

- `resource_id`;
- `path`;
- `format`;
- `extension`;
- `size_bytes` when available;
- `checksum` when available;
- `modified_at` when reliable;
- `included`;
- `exclusion_reason` when excluded.

### 5.3 Document

Represents a resource interpreted as a knowledge-bearing artifact.

Minimum attributes:

- `document_id`;
- `resource_id`;
- `title` when declared or extractable;
- `document_type`;
- `knowledge_layer`;
- `lifecycle_status`;
- `classification_provenance`;
- `classification_confidence`;
- `metadata`;
- `trust_signals`.

A resource may exist without being classified as a document. A document must reference exactly one physical resource in v0.1.

## 6. Identity and path rules

### 6.1 Resource identity

For v0.1:

```text
resource_id = normalized repository-relative path
```

Path normalization rules:

- use `/` as separator;
- remove leading `./`;
- collapse redundant separators;
- resolve `.` segments;
- reject paths escaping the repository root through `..`;
- preserve path case in stored evidence;
- compare case according to repository-filesystem policy;
- do not use absolute local paths as durable identity.

### 6.2 Document identity

For v0.1:

```text
document_id = repository snapshot identity + resource_id
```

Logical identity across renames is explicitly deferred. A rename produces a new `document_id` unless future evidence justifies content- or metadata-based continuity.

### 6.3 Location identity

Locations within a document may use:

- line range;
- section or heading;
- YAML/JSON pointer;
- resource-level rationale;
- relationship-level rationale.

Location semantics must remain compatible with the validated finding contract.

## 7. Supported formats

### v0.1 primary formats

- Markdown: `.md`;
- MDX: `.mdx`, parsed conservatively as Markdown-compatible content;
- YAML: `.yaml`, `.yml` when used as profile, metadata or knowledge contract;
- JSON: `.json` when explicitly included by profile or recognized as schema/contract.

### Advisory formats

Other text files may be inventoried as `unknown_text` when explicitly included, but they must not receive unsupported structural classifications.

Binary files are outside the initial document model except as referenced resources.

## 8. Document types

The initial controlled vocabulary is:

| Type | Meaning |
|---|---|
| `product_vision` | Product purpose, outcomes, strategy or scope |
| `governance` | Policies, operating rules, contribution or decision authority |
| `architecture` | System structure, boundaries and technical design |
| `architecture_decision` | A recorded decision such as an ADR |
| `specification` | Required behavior, constraints or acceptance conditions |
| `ontology` | Explicit domain concepts and semantic relationships |
| `glossary` | Defined terminology and canonical meanings |
| `runbook` | Operational procedure for repeatable execution or recovery |
| `agent_context` | Instructions, boundaries or context intended for AI agents |
| `operational` | Deployment, monitoring, incident or support knowledge |
| `schema_contract` | Machine-readable data or metadata contract |
| `project_profile` | Knowledge Guardian repository-specific configuration |
| `report` | Generated or curated analytical output |
| `general_documentation` | Knowledge artifact not matching a more specific type |
| `unknown` | Insufficient evidence for classification |

### Type rules

- each document has one primary type in v0.1;
- secondary tags may be retained but do not replace the primary type;
- profile declarations override filename heuristics;
- explicit document metadata overrides heuristics when valid;
- conflicting explicit declarations create analysis evidence rather than silent selection;
- `unknown` is valid and preferable to unsupported certainty.

## 9. Knowledge layers

The initial vocabulary is:

| Layer | Meaning |
|---|---|
| `conceptual` | Business concepts, purpose, principles and intended model |
| `specification` | Expected behavior, constraints and approved requirements |
| `executable_knowledge` | Schemas, contracts, tests or machine-readable definitions |
| `operational` | Runtime operation, deployment, monitoring and support |
| `agent_context` | Instructions and context governing AI-agent operation |
| `unknown` | Layer cannot be determined with sufficient evidence |

### Layer rules

- type and layer are independent dimensions;
- a document has one primary layer in v0.1;
- profile or explicit metadata outranks heuristic inference;
- future-state conceptual text must not be classified as executable evidence;
- a document may link across layers without being reclassified.

## 10. Lifecycle status

Controlled values:

- `draft`;
- `active`;
- `deprecated`;
- `archived`;
- `superseded`;
- `unknown`.

The model must retain:

- declared lifecycle value;
- normalized lifecycle value;
- source of the value;
- confidence when inferred.

Absence of lifecycle metadata results in `unknown`, not `active`.

## 11. Metadata model

Metadata is project-configurable and divided into three levels:

- `required`;
- `recommended`;
- `optional`.

Core normalized fields supported by the model:

```yaml
title:
description:
owner:
status:
version:
document_type:
knowledge_layer:
generated:
  by:
  at:
verified:
  by:
  at:
sources: []
stale_after:
canonical_for: []
supersedes: []
superseded_by: []
```

Rules:

- the model does not require every repository to use these fields;
- raw metadata must be preserved separately from normalized metadata;
- invalid metadata must not be silently normalized into a valid value;
- missing metadata only becomes a finding when an explicit authority requires it;
- generated and human-verified states remain distinct;
- profile rules may vary by document type and path scope.

## 12. Classification provenance

Every type, layer and lifecycle classification must record one provenance:

- `project_profile`;
- `document_metadata`;
- `native_rule`;
- `path_heuristic`;
- `content_heuristic`;
- `human_override`;
- `unknown`.

Every inferred classification must record confidence:

- `high`;
- `medium`;
- `low`.

Explicit declarations do not automatically prove correctness; they prove only what was declared.

## 13. Trust signals

The document model records observed signals without declaring overall trustworthiness automatically.

Supported observations:

- owner declared;
- author or generator declared;
- human verifier declared;
- generated timestamp declared;
- verification timestamp declared;
- source references declared;
- lifecycle declared;
- version declared;
- freshness boundary declared;
- canonical subject declared.

Trust signals must distinguish:

- present and valid;
- present but invalid;
- absent;
- not required;
- unknown.

## 14. Relationship model

A relationship connects two resources or documents and records evidence and provenance.

Minimum structure:

```yaml
relationship_id:
type:
source_resource_id:
target_resource_id:
source_location:
target_exists:
provenance:
authority_reference:
confidence:
```

### Initial relationship types

| Relationship | Meaning |
|---|---|
| `links_to` | Navigational or contextual link |
| `references` | Non-navigational citation or dependency |
| `declares_canonical_for` | Source claims authority for a subject |
| `supersedes` | Source replaces target |
| `superseded_by` | Inverse supersession relationship |
| `implements` | Executable artifact claims implementation of a specification |
| `specified_by` | Artifact points to governing specification |
| `derived_from` | Artifact identifies source material |
| `verifies` | Artifact or actor provides verification evidence |
| `governs` | Governance document applies to target scope |
| `entry_point_for` | Resource is configured as reading or agent entry point |
| `exempted_from` | Profile exempts a resource from a rule |
| `related_to` | Explicit but otherwise untyped relationship |

### Relationship rules

- link existence does not imply authority;
- authority relationships require an explicit authority source;
- inferred semantic relationships are outside deterministic v0.1 delivery;
- missing targets may still produce relationship records with `target_exists: false`;
- inverse relationships may be derived but must retain derivation provenance;
- a relationship must never silently select one canonical source among conflicts.

## 15. Entry points

Entry points are resources declared or detected as starting locations.

Sources:

- project profile;
- native filename rule;
- explicit metadata;
- human override.

Entry-point attributes:

- resource ID;
- intended consumer: `human`, `agent` or `both`;
- scope;
- priority or order when declared;
- provenance;
- required or optional state.

A missing required configured entry point is a valid normative condition. Multiple entry points are not inherently a problem unless an applicable rule requires ordering or hierarchy.

## 16. Exceptions

Exceptions are first-class profile-controlled records.

Minimum attributes:

- exception ID;
- applicable rule or relationship;
- resource or path scope;
- reason;
- authority reference;
- optional expiration;
- optional owner.

An exception suppresses a finding only when:

- it applies to the exact rule and scope;
- its authority is valid;
- it is not expired;
- evidence of the exception is retained.

## 17. Invariants

1. Every document belongs to exactly one repository snapshot.
2. Every document references exactly one resource in v0.1.
3. Resource paths are repository-relative and normalized.
4. Unknown classification is valid; unsupported certainty is not.
5. Type and knowledge layer are separate dimensions.
6. Declared metadata is preserved separately from normalized values.
7. A link does not imply canonical authority.
8. Missing metadata is not a finding without an applicable authority.
9. Future-state documentation is not runtime evidence.
10. Exceptions require explicit scope, reason and authority.
11. Relationships retain evidence and provenance.
12. Human overrides are auditable and never represented as machine inference.

## 18. Acceptance criteria

KG-002 shaping is ready for delivery decision when:

- [x] problem and consumers are defined;
- [x] bounded scope and exclusions are explicit;
- [x] resource and document identity rules are defined;
- [x] path normalization rules are defined;
- [x] supported formats are bounded;
- [x] initial document-type vocabulary is defined;
- [x] knowledge-layer vocabulary is defined;
- [x] lifecycle model is defined;
- [x] metadata representation and precedence are defined;
- [x] classification provenance and confidence are defined;
- [x] trust-signal observations are defined;
- [x] relationship vocabulary and invariants are defined;
- [x] entry points and exceptions are represented;
- [x] dependencies and risks are recorded;
- [x] implementation scope can be bounded independently.

## 19. Proposed delivery slice

Subject to a separate Tech Lead authorization, the first implementation slice should create only versioned data contracts and tests for:

1. `RepositorySnapshot`;
2. `Resource`;
3. `Document`;
4. `Classification`;
5. `Relationship`;
6. `EntryPoint`;
7. `Exception`.

The slice must not include filesystem scanning, Markdown parsing, graph traversal or finding generation.

## 20. Dependencies

- validated finding contract `0.1.0`;
- project-profile boundaries;
- repository path-normalization policy;
- future parser and scanner decisions;
- fixture strategy for contract validation.

## 21. Risks and responses

| Risk | Response |
|---|---|
| Model becomes a universal document ontology | Keep vocabulary bounded to v0.1 use cases |
| Classification heuristics create false certainty | Preserve provenance, confidence and `unknown` |
| Path identity fails across renames | Explicitly defer cross-rename identity |
| Relationship vocabulary expands without use | Require one downstream rule or report use case per relationship |
| Metadata model becomes mandatory globally | Keep requirements profile-controlled |
| Conceptual documents are treated as runtime evidence | Preserve independent knowledge-layer classification |
| Schema implementation starts before model approval | Require separate Tech Lead delivery decision |

## 22. Product recommendation

Approve KG-002 as **Definition-of-Ready complete for a bounded contract-only delivery slice**.

Do not authorize scanner implementation. The next decision should determine whether to implement versioned document-model schemas and contract tests, or request revisions to this model first.
