---
category: data-analytics
tags:
- research-analytics
- power-analysis
- sample-size
- randomization
- experimental-design
- readiness-assessment
title: Randomization & Power Analysis Readiness Assessment
use_cases:
- Calculating required sample sizes for statistical power
- Designing randomization procedures for valid treatment allocation
- Determining minimum detectable effects for given resources
- Planning experiments with proper statistical foundations
related_templates:
- data-analytics/Research-Analytics/experimental-design-setup.md
- data-analytics/Research-Analytics/treatment-effect-analysis.md
- data-analytics/Research-Analytics/validity-and-diagnostics.md
industries:
- technology
- healthcare
- finance
- retail
type: framework
difficulty: intermediate
slug: randomization-and-power-analysis
---

# Randomization & Power Analysis Readiness Assessment

## Purpose
Assess readiness to design experiments with valid randomization, adequate statistical power, and operational execution that supports credible inference.

## Quick Assessment Prompt

> Assess experiment design readiness for [EXPERIMENT] with outcome [PRIMARY_METRIC]. Score readiness (1–5) across: (1) Hypothesis & metrics, (2) Randomization/unit assignment, (3) Power & sample sizing, (4) Data quality & instrumentation, (5) Execution & monitoring, (6) Analysis plan & governance. Provide a scorecard and a launch checklist.

## Readiness Scorecard (1–5)

### 1) Hypothesis & Metrics
- 1 — Initial: Hypothesis vague; metrics not well-defined.
- 3 — Defined: Primary/secondary metrics defined; success criteria documented.
- 5 — Optimized: Metrics are stable; decision thresholds align to business impact.

### 2) Randomization & Unit Assignment
- 1 — Initial: Randomization unclear; interference likely.
- 3 — Defined: Unit of randomization chosen; assignment method documented.
- 5 — Optimized: Randomization is robust; interference minimized and validated.

### 3) Power & Sample Sizing
- 1 — Initial: No power analysis; sample size arbitrary.
- 3 — Defined: MDE, baseline, and variance estimated; power calculated.
- 5 — Optimized: Sizing is reliable; monitoring ensures adequate power at decision time.

### 4) Data Quality & Instrumentation
- 1 — Initial: Data incomplete; tracking changes unlogged.
- 3 — Defined: Instrumentation plan; QA checks; logging and versioning.
- 5 — Optimized: Data is trusted; issues detected early; changes are governed.

### 5) Execution & Monitoring
- 1 — Initial: Execution ad-hoc; ramp and guardrails missing.
- 3 — Defined: Ramp plan, guardrails, and monitoring dashboards.
- 5 — Optimized: Execution is controlled; anomalies are handled quickly.

### 6) Analysis Plan & Governance
- 1 — Initial: No pre-analysis plan; p-hacking risk high.
- 3 — Defined: Pre-analysis plan and decision rules; stakeholder alignment.
- 5 — Optimized: Governance enforces rigor; learnings are reusable across experiments.

## Deliverables
- Experiment readiness scorecard and risks
- Randomization plan and assignment spec
- Power analysis with sample size and MDE
- Instrumentation and QA checklist
- Pre-analysis plan and decision rules

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [EXPERIMENT]: Experiment name
- [PRIMARY_METRIC]: Primary metric
- [BASELINE]: Baseline rate/value
- [MDE]: Minimum detectable effect
- [ALPHA]: Significance level
- [POWER]: Target power

## Example (Condensed)
- Experiment: Checkout UI change with metric conversion rate
- Scores (1–5): Hypothesis 3; Randomization 2; Power 2; Data 2; Execution 3; Governance 2
- 90-day priorities: Define unit and guardrails; compute power; validate instrumentation; write pre-analysis plan

