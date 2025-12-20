---
category: data-analytics
tags:
- research-analytics
- network-analysis
- graph-data
- data-preparation
- data-quality
- readiness-assessment
title: Network Analysis Data Preparation Readiness Assessment
use_cases:
- Loading and preprocessing network data from various formats
- Cleaning and validating network structure and attributes
- Creating subnetworks and filtering nodes/edges by criteria
- Preparing temporal network snapshots for evolution analysis
related_templates:
- data-analytics/Research-Analytics/network-analysis-centrality-community.md
- data-analytics/Research-Analytics/network-analysis-paths-temporal.md
- data-analytics/Research-Analytics/network-analysis-visualization.md
industries:
- technology
- social-media
- finance
- healthcare
type: framework
difficulty: intermediate
slug: network-analysis-data-preparation
---

# Network Analysis Data Preparation Readiness Assessment

## Purpose
Assess readiness to prepare graph data for network analysis, including identity resolution, edge construction, and quality validation.

## Quick Prompt

> Assess graph data prep readiness for [GRAPH] built from sources [SOURCES]. Score readiness (1–5) across: (1) Source quality, (2) Entity resolution, (3) Edge construction rules, (4) Validation & QA, (5) Versioning & lineage, (6) Automation & operations. Provide a scorecard and a prep pipeline plan.

## Readiness Scorecard (1–5)

### 1) Source Quality
- 1 — Initial: Sources inconsistent; missing critical fields.
- 3 — Defined: Source inventory; required fields; quality checks defined.
- 5 — Optimized: Source quality is monitored; changes are managed with contracts.

### 2) Entity Resolution
- 1 — Initial: Duplicates unresolved; identities inconsistent.
- 3 — Defined: Matching rules and review process; confidence thresholds.
- 5 — Optimized: Resolution is reliable and monitored; errors are reduced systematically.

### 3) Edge Construction Rules
- 1 — Initial: Edges ad-hoc; semantics unclear.
- 3 — Defined: Edge definitions and time windows documented; rules tested.
- 5 — Optimized: Edge rules are stable and versioned; impacts are predictable.

### 4) Validation & QA
- 1 — Initial: No QA; graph errors discovered late.
- 3 — Defined: Validation checks (degree distributions, connectivity) and sampling.
- 5 — Optimized: QA is automated; issues detected early and prevented.

### 5) Versioning & Lineage
- 1 — Initial: No versioning; lineage unknown.
- 3 — Defined: Graph builds versioned; lineage tracked to sources.
- 5 — Optimized: Versioning supports reproducibility and safe rollbacks.

### 6) Automation & Operations
- 1 — Initial: Manual builds; brittle processes.
- 3 — Defined: Automated pipeline; schedules; runbooks.
- 5 — Optimized: Operations are mature; monitoring and incident response exist.

## Deliverables
- Graph prep readiness scorecard and gap list
- Entity resolution rules and QA plan
- Edge semantics and construction spec
- Validation checks and sampling approach
- Versioning/lineage and automation plan

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [GRAPH]: Graph name
- [SOURCES]: Source systems
- [MATCH_RULES]: Match rules
- [EDGE_RULES]: Edge rules
- [VALIDATION]: Validation checks
- [BUILD_CADENCE]: Build cadence

## Example (Condensed)
- Graph: Customer interactions across CRM + support tickets
- Scores (1–5): Sources 2; Resolution 2; Edge rules 3; QA 2; Versioning 2; Ops 2
- 90-day priorities: Define match rules; automate QA; version builds and add lineage; operationalize scheduling

