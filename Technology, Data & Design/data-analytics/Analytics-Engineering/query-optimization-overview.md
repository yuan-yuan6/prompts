---
category: data-analytics
title: Query Optimization Readiness Assessment
tags:
- query-optimization
- performance-tuning
- database-diagnostics
- readiness-assessment
use_cases:
- Selecting the right optimization approach based on performance symptoms
- Planning systematic database performance improvement projects
- Routing to specialized optimization modules
related_templates:
- data-analytics/Analytics-Engineering/query-optimization.md
- data-analytics/Analytics-Engineering/query-optimization-baseline-analysis.md
- data-analytics/Analytics-Engineering/query-optimization-indexing-strategies.md
- data-analytics/Analytics-Engineering/query-optimization-query-rewriting.md
- data-analytics/Analytics-Engineering/query-optimization-monitoring-tuning.md
- data-analytics/Analytics-Engineering/query-optimization-resource-concurrency.md
industries:
- technology
- finance
- healthcare
- retail
type: framework
difficulty: intermediate
slug: query-optimization-overview
---

# Query Optimization Readiness Assessment

## Purpose
Assess readiness to optimize analytical queries and workloads through profiling, indexing/partitioning, governance, and performance monitoring.

## Quick Assessment Prompt

> Assess query optimization readiness for workload [WORKLOAD] on platform [PLATFORM]. Score readiness (1–5) across: (1) Workload understanding, (2) Data modeling & partitioning, (3) Query patterns & standards, (4) Performance monitoring, (5) Cost governance, (6) Continuous optimization process. Provide a scorecard and a 60-day optimization plan.

## Readiness Scorecard (1–5)

### 1) Workload Understanding
- 1 — Initial: No profiling; performance issues are reactive.
- 3 — Defined: Top queries and workloads identified; profiling routine exists.
- 5 — Optimized: Workloads are understood; performance is predictable and managed.

### 2) Data Modeling & Partitioning
- 1 — Initial: Models inconsistent; partitions/indexes absent or wrong.
- 3 — Defined: Modeling standards; partitioning/indexing strategy defined.
- 5 — Optimized: Design is optimized; changes are validated by metrics.

### 3) Query Patterns & Standards
- 1 — Initial: Queries inconsistent; anti-patterns common.
- 3 — Defined: Standard patterns and linting; reviews for critical queries.
- 5 — Optimized: Patterns are mature; performance regressions are prevented.

### 4) Performance Monitoring
- 1 — Initial: No monitoring; spikes unnoticed until incidents.
- 3 — Defined: Dashboards and alerts for latency and resource usage.
- 5 — Optimized: Monitoring drives proactive tuning and stable SLAs.

### 5) Cost Governance
- 1 — Initial: Costs unmanaged; runaway queries common.
- 3 — Defined: Budgets, quotas, and cost visibility per team/workload.
- 5 — Optimized: Costs are optimized continuously with governance and automation.

### 6) Continuous Optimization Process
- 1 — Initial: Optimization is one-off; learnings not shared.
- 3 — Defined: Backlog and cadence; owners assigned; change validation.
- 5 — Optimized: Continuous optimization reduces latency and cost over time.

## Deliverables
- Query optimization readiness scorecard and top bottlenecks
- Workload profile and top query list
- Modeling/partitioning recommendations
- Monitoring dashboard and alert spec
- Optimization backlog and cadence

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [WORKLOAD]: Workload name
- [PLATFORM]: Data platform
- [TOP_QUERIES]: Top queries
- [LATENCY_SLA]: Latency SLA
- [COST_BUDGET]: Cost budget
- [OPTIMIZATION_BACKLOG]: Backlog

## Example (Condensed)
- Workload: BI dashboards with unpredictable latency and cost spikes
- Scores (1–5): Understanding 2; Modeling 2; Patterns 2; Monitoring 2; Cost 2; Process 2
- 60-day priorities: Profile top queries; implement partitioning; add dashboards/alerts and cost controls; start weekly optimization cadence

