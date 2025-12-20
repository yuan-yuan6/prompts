---
category: data-analytics
tags:
- research-analytics
- network-analysis
- graph-theory
- social-network-analysis
- centrality
- readiness-assessment
title: Network Analysis Readiness Assessment
use_cases:
- Understanding relationship structures and influence patterns in connected data
- Identifying key actors, communities, and information flow paths
- Analyzing network robustness and structural vulnerabilities
- Tracking network evolution and dynamics over time
related_templates:
- data-analytics/Research-Analytics/network-analysis-data-preparation.md
- data-analytics/Research-Analytics/network-analysis-centrality-community.md
- data-analytics/Research-Analytics/network-analysis-paths-temporal.md
- data-analytics/Research-Analytics/network-analysis-visualization.md
industries:
- technology
- social-media
- finance
- healthcare
- telecommunications
type: framework
difficulty: intermediate
slug: network-analysis
---

# Network Analysis Readiness Assessment

## Purpose
Assess readiness to perform network analysis with correct graph modeling, data preparation, methods, and interpretation.

## Quick Prompt

> Assess network analysis readiness for problem [PROBLEM] using entities [NODES] and relationships [EDGES]. Score readiness (1–5) across: (1) Graph model & scope, (2) Data preparation, (3) Method selection, (4) Computation & scalability, (5) Visualization & interpretation, (6) Governance & reproducibility. Provide a scorecard and analysis plan.

## Readiness Scorecard (1–5)

### 1) Graph Model & Scope
- 1 — Initial: Graph definition unclear; nodes/edges inconsistent.
- 3 — Defined: Graph schema defined; scope and assumptions documented.
- 5 — Optimized: Graph model is stable and validated; aligns to decisions.

### 2) Data Preparation
- 1 — Initial: Relationship data noisy; duplicates unresolved.
- 3 — Defined: Cleaning, deduping, and identity resolution plan.
- 5 — Optimized: Data prep is automated and validated; quality monitored.

### 3) Method Selection
- 1 — Initial: Methods chosen arbitrarily; no baseline.
- 3 — Defined: Methods selected for question; baselines and checks defined.
- 5 — Optimized: Method selection is standardized; robustness checks are routine.

### 4) Computation & Scalability
- 1 — Initial: Tooling unstable; performance issues common.
- 3 — Defined: Tooling and compute approach defined; scalability tested.
- 5 — Optimized: Scalable pipelines and reproducible runs support larger graphs.

### 5) Visualization & Interpretation
- 1 — Initial: Results are hard to interpret; visuals misleading.
- 3 — Defined: Visualization plan; summaries and narratives defined.
- 5 — Optimized: Interpretation is rigorous; insights map to actions.

### 6) Governance & Reproducibility
- 1 — Initial: No versioning; analyses not repeatable.
- 3 — Defined: Code-based workflow; graph versions; review process.
- 5 — Optimized: Governance ensures repeatable, reliable insights over time.

## Deliverables
- Network analysis readiness scorecard and gap list
- Graph schema and assumptions document
- Data prep pipeline and validation checks
- Method selection and evaluation plan
- Visualization and interpretation report

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [PROBLEM]: Problem statement
- [NODES]: Node types
- [EDGES]: Edge types
- [GRAPH_SCHEMA]: Schema
- [TOOLS]: Tools/libraries
- [SCALE]: Graph size

## Example (Condensed)
- Problem: Detect fraud rings using transaction relationships
- Scores (1–5): Model 3; Prep 2; Methods 2; Scale 2; Viz 2; Repro 2
- 90-day priorities: Stabilize schema; improve identity resolution; define evaluation and scalable pipeline; add visualization standards

