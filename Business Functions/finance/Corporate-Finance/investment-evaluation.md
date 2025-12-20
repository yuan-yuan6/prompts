---
category: finance
related_templates:
- strategy/okr-implementation-framework.md
- strategy/digital-transformation-roadmap.md
- operations/lean-six-sigma-implementation.md
tags:
- investment-evaluation
- roi-analysis
- npv-irr
- capital-allocation
- readiness-assessment
title: Investment Evaluation Readiness Assessment
use_cases:
- Assess readiness to evaluate capital investments using consistent financial and risk criteria.
- Standardize investment memos for investment committee decisions.
- Improve post-investment tracking and lessons learned.
industries:
- education
- finance
- government
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: investment-evaluation-readiness-assessment
---

# Investment Evaluation Readiness Assessment

## Purpose
Assess how ready your organization is to evaluate investments (capex, M&A, product/R&D, technology) with consistent financial modeling, risk analysis, governance, and post-investment accountability.

## Quick Prompt
Score your current investment evaluation process for a typical $[INVESTMENT_AMOUNT] initiative with a $[CASH_FLOW_IMPACT]/year impact over [HORIZON_YEARS] years. Include: governance, model standards, data quality, risk/sensitivity, decision criteria, and post-investment review.

## Readiness Scorecard (1–5 each)
Rate each dimension from 1 (ad hoc) to 5 (disciplined and repeatable). Total score is the sum across 6 dimensions (max 30).

1) Governance & Decision Rights
- 1: No clear owner; approvals vary by requester.
- 3: Investment committee exists; escalation is inconsistent.
- 5: Clear RACI, thresholds, and documentation requirements; audit-ready decisions.

2) Strategic Fit & Value Thesis
- 1: Benefits are narrative-only; weak linkage to strategy.
- 3: Value drivers documented; trade-offs discussed.
- 5: Explicit value thesis, alternatives compared, and strategic constraints captured.

3) Financial Modeling & Assumptions
- 1: Spreadsheet varies by analyst; assumptions undocumented.
- 3: Standard model exists; key assumptions tracked.
- 5: Versioned model standards, assumption library, and review/QA checklist.

4) Risk, Sensitivity & Scenarios
- 1: Risks listed, not quantified.
- 3: Sensitivity on 2–3 variables; basic scenarios.
- 5: Scenarios tied to risk drivers; mitigations mapped to leading indicators.

5) Data, Tools & Evidence
- 1: Inputs are manual and untraceable.
- 3: Source data referenced; evidence stored in a shared location.
- 5: Traceable inputs, consistent data definitions, and reproducible calculations.

6) Monitoring & Post-Investment Review
- 1: No measurement after approval.
- 3: KPIs tracked for large projects.
- 5: Benefits realization plan, stage gates, and post-mortems feed a learning loop.

## Deliverables
- One-page investment memo (value thesis, alternatives, decision)
- Financial model summary (NPV/IRR/payback + key assumptions)
- Risk register with quantified sensitivities/scenarios
- Implementation milestones and benefit-realization metrics
- Post-investment review plan (timing, owner, metrics)

## Maturity Scale
- Level 1: Reactive — inconsistent approvals and models.
- Level 2: Documented — templates exist but not enforced.
- Level 3: Repeatable — governance and modeling standards used for most decisions.
- Level 4: Managed — quantified risk/scenario analysis and benefits tracking are standard.
- Level 5: Optimizing — continuous learning improves hurdle rates, assumptions, and portfolio choices.

## Variables
- [COMPANY_NAME]
- [INVESTMENT_TYPE] (capex, acquisition, product, technology, R&D)
- [INVESTMENT_AMOUNT]
- [HORIZON_YEARS]
- [WACC_PERCENT]
- [HURDLE_RATE_PERCENT]
- [KEY_VALUE_DRIVERS] (volume, price, margin, adoption, utilization)
- [TOP_RISKS] (market, execution, regulatory, technology)

## Example (Condensed)
Investment: $5M facility expansion; horizon 10 years; WACC 10%; hurdle 14%.
- Governance: committee threshold $1M; required memo + model QA checklist.
- Value thesis: capacity unlocks $2M/year revenue at 40% margin.
- Modeling: base NPV/IRR with documented assumptions + implementation timeline.
- Risk/scenarios: demand ±10%, capex +15%, ramp delay 6 months.
- Evidence: inputs tied to sales forecast and cost benchmarks.
- Monitoring: quarterly benefits tracking; post-review at month 18.

