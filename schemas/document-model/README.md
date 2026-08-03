# Repository Document Model Contracts

Contract owner: KG-002.

Current version: `0.1.0`.

## Files

- `repository-snapshot.schema.json` → RepositorySnapshot
- `resource.schema.json` → Resource
- `classification.schema.json` → Classification
- `document.schema.json` → Document
- `relationship.schema.json` → Relationship
- `entry-point.schema.json` → EntryPoint
- `exception.schema.json` → Exception

Shared path, identifier, confidence and version definitions are in `common.schema.json`.

## Local validation

```bash
python -m pip install jsonschema referencing
python tests/validate_document_model_contracts.py
```

The runner resolves references locally, validates all positive cases and confirms that every negative case is rejected.

## Compatibility

Patch releases may clarify descriptions or add non-breaking optional fields. New required properties, enum removals or semantic changes require a minor or major contract version and a parallel version directory.

## Boundaries

These contracts represent data only. They do not scan repositories, parse Markdown/YAML, infer relationships, execute rules, produce findings or render reports.

Cross-document referential integrity, rename identity, path case policy and relationship target existence remain application-level or snapshot-level concerns.

Resource and document identifiers may preserve repository-relative path casing and spaces so IDs derived from observed paths remain compatible with the model's path-identity rule.
