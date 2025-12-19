---
category: data-analytics
tags:
- research-analytics
- statistical-analysis
- hypothesis-testing
- inference
- effect-size
- readiness-assessment
title: Statistical Analysis Readiness Assessment
use_cases:
- Testing hypotheses and drawing valid conclusions from data
- Estimating parameters with confidence intervals
- Comparing groups and measuring effect sizes
- Selecting and validating appropriate statistical methods
related_templates:
- data-analytics/Research-Analytics/randomization-and-power-analysis.md
- data-analytics/Research-Analytics/experimental-design-setup.md
- data-analytics/Research-Analytics/treatment-effect-analysis.md
industries:
- healthcare
- technology
- finance
- education
- government
type: framework
difficulty: intermediate
slug: statistical-analysis
---

# Statistical Analysis Readiness Assessment

## Purpose
Assess readiness to run statistical analyses with correct assumptions, reproducible workflows, and results that support reliable decisions.

## Quick Assessment Prompt

> Assess statistical analysis readiness for question [QUESTION] using dataset [DATASET]. Score readiness (1–5) across: (1) Problem framing & hypotheses, (2) Data readiness, (3) Method selection & assumptions, (4) Reproducibility, (5) Interpretation & communication, (6) Governance & review. Provide a scorecard and an analysis plan.

## Readiness Scorecard (1–5)

### 1) Problem Framing & Hypotheses
- 1 — Initial: Question ambiguous; hypotheses undefined.
- 3 — Defined: Hypotheses, metrics, and decision criteria defined.
- 5 — Optimized: Framing is precise; results map directly to decisions.

### 2) Data Readiness
- 1 — Initial: Data quality issues unknown; missingness unmanaged.
- 3 — Defined: Data cleaned; missingness and outliers handled with documented rules.
- 5 — Optimized: Data quality is monitored; pipelines support reliable reuse.

### 3) Method Selection & Assumptions
- 1 — Initial: Methods chosen by habit; assumptions unchecked.
- 3 — Defined: Appropriate methods selected; assumptions checked and documented.
- 5 — Optimized: Method selection is standardized; robustness checks are routine.

### 4) Reproducibility
- 1 — Initial: Analysis is manual; steps not tracked.
- 3 — Defined: Code-based workflow; versioned data and notebooks; reproducible outputs.
- 5 — Optimized: Reproducibility is enforced with automation and reviews.

### 5) Interpretation & Communication
- 1 — Initial: Results are overconfident; uncertainty ignored.
- 3 — Defined: Effect sizes, uncertainty, and limitations communicated clearly.
- 5 — Optimized: Communication drives correct decisions; stakeholders understand tradeoffs.

### 6) Governance & Review
- 1 — Initial: No peer review; errors slip through.
- 3 — Defined: Review process for methods and results; documentation standards.
- 5 — Optimized: Governance is mature; quality is consistently high.

## Deliverables
- Analysis readiness scorecard and gap list
- Analysis plan (methods, assumptions, robustness checks)
- Data cleaning and feature specification
- Reproducible code workflow and artifacts
- Results narrative with uncertainty and limitations

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [QUESTION]: Research question
- [DATASET]: Dataset name
- [METRICS]: Metrics
- [ASSUMPTIONS]: Assumptions
- [ROBUSTNESS_CHECKS]: Robustness checks
- [DECISION_CRITERIA]: Decision criteria

## Example (Condensed)
- Question: Does onboarding reduce churn for new users?
- Scores (1–5): Framing 3; Data 2; Methods 3; Repro 2; Comms 3; Review 2
- 60-day priorities: Improve data QA; implement reproducible workflow; add peer review and robustness checks

