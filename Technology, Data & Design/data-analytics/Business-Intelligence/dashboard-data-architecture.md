---
category: data-analytics
title: Dashboard Data Architecture Readiness Assessment
tags:
- business-intelligence
- data-architecture
- etl
- data-modeling
- readiness-assessment
use_cases:
- Designing data pipelines for dashboards with multiple source systems
- Building ETL/ELT workflows for dashboard refresh from operational databases
- Creating data models that support summary and drill-down reporting
- Implementing data quality frameworks for reliable analytics
related_templates:
- data-analytics/Business-Intelligence/dashboard-strategy-requirements.md
- data-analytics/Business-Intelligence/dashboard-technical-implementation.md
- data-analytics/Analytics-Engineering/pipeline-development.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: dashboard-data-architecture
---

# Dashboard Data Architecture Readiness Assessment

## Purpose
Assess readiness to build a dashboard data architecture that is reliable, governed, performant, and aligned to business decision-making.

## Quick Prompt

> Assess readiness to deliver dashboard [DASHBOARD] for stakeholders [AUDIENCE]. Score readiness (1–5) across: (1) KPI definitions, (2) Source data & lineage, (3) Modeling layer, (4) Data quality & governance, (5) Performance & cost, (6) Delivery & maintenance. Provide a scorecard and a recommended architecture.

## Readiness Scorecard (1–5)

### 1) KPI Definitions & Semantics
- 1 — Initial: KPIs ambiguous; definitions differ across teams.
- 3 — Defined: Definitions documented; owners and calculation logic agreed.
- 5 — Optimized: KPIs are standardized; changes are governed and communicated.

### 2) Source Data & Lineage
- 1 — Initial: Sources unclear; lineage missing.
- 3 — Defined: Sources and lineage documented; access patterns defined.
- 5 — Optimized: Lineage is automated; changes are detected and managed reliably.

### 3) Modeling Layer
- 1 — Initial: No consistent model; ad-hoc SQL in dashboards.
- 3 — Defined: Semantic model exists; curated datasets and dimensions/facts defined.
- 5 — Optimized: Model is reusable and stable across dashboards; supports self-service safely.

### 4) Data Quality & Governance
- 1 — Initial: Quality issues frequent; no ownership.
- 3 — Defined: Quality checks and ownership; incident response defined.
- 5 — Optimized: Quality is monitored with SLAs; governance supports audits and scale.

### 5) Performance & Cost
- 1 — Initial: Dashboards slow; costs unpredictable.
- 3 — Defined: Performance budgets and optimization practices defined.
- 5 — Optimized: Performance is consistently fast; costs are optimized and predictable.

### 6) Delivery & Maintenance
- 1 — Initial: Releases ad-hoc; breakages common.
- 3 — Defined: Deployment/release process; documentation and runbooks.
- 5 — Optimized: Maintenance is mature with automated testing, monitoring, and versioning.

## Deliverables
- Readiness scorecard and gap list
- KPI dictionary and ownership map
- Proposed data model (facts/dimensions/semantic layer)
- Data quality checks and monitoring plan
- Performance/cost plan and maintenance runbook

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [DASHBOARD]: Dashboard name
- [AUDIENCE]: Audience
- [KPIS]: Key KPIs
- [SOURCES]: Source systems
- [MODEL]: Modeling approach
- [SLA]: SLA targets

## Example (Condensed)
- Dashboard: Executive revenue and retention dashboard
- Scores (1–5): KPI 2; Lineage 2; Model 3; Quality 2; Perf 3; Maintenance 2
- 90-day priorities: Standardize KPI definitions; add lineage and tests; implement semantic model and monitoring

