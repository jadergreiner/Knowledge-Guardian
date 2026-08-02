# Knowledge Guardian — Tech Lead + Product Operating Model

**Status:** Active
**Version:** 0.1
**Updated:** 2026-08-02

## Purpose

This document applies the Tech Lead + Product Management framework to Knowledge Guardian.

The operating loop is:

```text
SENSE → FRAME → DISCOVER → DECIDE → SHAPE → DELIVER → MEASURE → LEARN
```

## Product governance

### Product direction

The PRD defines the problem, users, value proposition, scope, success criteria, and product boundaries.

### Discovery track

Discovery reduces uncertainty before implementation commitments. It includes repository interviews, competitive analysis, rule validation, prototype scans, false-positive analysis, and technical spikes.

Discovery outputs are evidence, decisions, rejected alternatives, and shaped opportunities. Discovery work is not automatically a delivery commitment.

### Delivery track

Delivery converts validated product decisions into executable increments. Each increment must define acceptance criteria, evidence, observability, and documentation impact.

## Decision boundaries

| Decision | Primary owner | Required evidence |
|---|---|---|
| Problem, user and outcome | Product | User or repository evidence |
| Priority and scope | Product | Expected value, risk and dependency |
| Architecture and implementation | Tech Lead | Technical analysis and trade-offs |
| Quality and release readiness | Tech Lead | Tests, checks and operational evidence |
| Product acceptance | Product | Acceptance criteria and outcome evidence |

The same person may temporarily perform both roles, but every decision must remain classified as product, technical, hypothesis, or delivery commitment.

## Core artifacts

| Artifact | Purpose |
|---|---|
| `PRD.md` | Product direction and requirements |
| `ROADMAP.md` | Outcome-oriented sequencing and confidence |
| `DISCOVERY.md` | Questions, hypotheses and evidence |
| `BACKLOG.md` | Shaped and prioritized work |
| `DECISIONS.md` | Product and technical decision record |
| `RAID.md` | Risks, assumptions, issues and dependencies |
| `STATUS.md` | Current state and next action |

## Cadence

### Continuous

- capture signals and findings;
- update RAID items;
- record material decisions;
- keep backlog traceable to PRD outcomes.

### Weekly product review

- review evidence and open hypotheses;
- decide what moves from discovery to delivery;
- reassess priorities and confidence;
- update status and roadmap.

### Release review

- verify acceptance criteria;
- measure product and quality metrics;
- record lessons and remaining risks;
- update the roadmap based on evidence.

## Definition of ready

A delivery item is ready when it has:

- a clear problem statement;
- target user or consumer;
- expected outcome;
- acceptance criteria;
- dependencies and risks;
- evidence or explicit hypothesis;
- a bounded implementation scope.

## Definition of done

A delivery item is done when:

- acceptance criteria are verified;
- tests and quality checks pass;
- findings include reproducible evidence;
- documentation and contracts are updated;
- operational or usage signals can be measured;
- known limitations are recorded.

## Guardrails

- Knowledge Guardian is proposal-first and read-only by default.
- Findings must distinguish evidence from inference.
- The product must not silently choose a canonical source when authority is ambiguous.
- Deterministic checks should precede probabilistic semantic analysis.
- Human approval remains required for governance-changing actions.
