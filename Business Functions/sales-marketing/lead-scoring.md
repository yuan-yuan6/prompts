---
category: sales-marketing
related_templates:
- sales-marketing/market-research.md
- sales-marketing/campaign-development.md
- sales-marketing/lead-generation.md
tags:
- lead-scoring
- qualification-criteria
- sales-readiness
- conversion-probability
- readiness-assessment
title: Lead Scoring Readiness Assessment
use_cases:
- Prioritize sales follow-up and resource allocation
- Improve lead-to-customer conversion rates
- Align sales and marketing on lead quality
- Automate lead qualification and routing
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
slug: lead-scoring
---

# Lead Scoring Readiness Assessment

## Purpose
Assess readiness to design, implement, and govern a lead scoring system that improves conversion and sales efficiency through reliable signals, clear thresholds, and measurable outcomes.

## Quick Prompt

> Assess lead scoring readiness for [COMPANY_TYPE] with [LEAD_VOLUME] leads/month and CRM [CRM_PLATFORM]. Score readiness (1–5) across: (1) ICP & qualification definition, (2) Signal design (fit + intent), (3) Data quality & tracking, (4) Model governance & calibration, (5) Routing & workflow, (6) Monitoring & continuous improvement. Provide a scorecard, top gaps, and a 60-day implementation plan.

## Readiness Scorecard (1–5)

### 1) ICP & Qualification Definition
- 1 — Initial: No clear ICP; qualification is subjective; teams disagree on “good leads.”
- 3 — Defined: ICP, personas, and disqualifiers documented; thresholds mapped to outcomes.
- 5 — Optimized: ICP is continuously refined; qualification rules are evidence-based and aligned across teams.

### 2) Signal Design (Fit + Intent)
- 1 — Initial: Signals are arbitrary; weights are guessed; scoring doesn’t reflect buying intent.
- 3 — Defined: Fit and intent signals defined; negative signals included; scoring logic is documented.
- 5 — Optimized: Signals are validated; weights are calibrated; scoring reflects conversion probability reliably.

### 3) Data Quality & Tracking
- 1 — Initial: Key fields missing; tracking inconsistent; identity resolution is weak.
- 3 — Defined: Required fields and event tracking defined; enrichment in place; QA routines exist.
- 5 — Optimized: Data is reliable and monitored; integration issues are detected quickly; attribution is consistent enough for calibration.

### 4) Model Governance & Calibration
- 1 — Initial: No ownership; changes are ad-hoc; score inflation/decay unmanaged.
- 3 — Defined: Owner and change process; calibration cadence; clear score thresholds.
- 5 — Optimized: Governance is embedded; drift is monitored; calibration improves outcomes over time.

### 5) Routing & Workflow
- 1 — Initial: No SLAs; routing is inconsistent; sales follow-up is slow.
- 3 — Defined: Routing rules and SLAs; handoff logic by segment; feedback loops exist.
- 5 — Optimized: Routing is automated and reliable; speed-to-lead is predictable; workflows adapt by territory/product.

### 6) Monitoring & Continuous Improvement
- 1 — Initial: No reporting; scoring isn’t evaluated against outcomes.
- 3 — Defined: Dashboards for stage conversion and SLA compliance; learnings captured.
- 5 — Optimized: Experimentation improves signals and weights; scoring is tied to pipeline and revenue outcomes.

## Deliverables
- Lead scoring readiness scorecard with evidence notes
- ICP and qualification definitions (fit + intent, disqualifiers)
- Signal library and scoring rules (including negative scoring)
- Routing rules and SLAs by segment/territory
- Monitoring dashboard spec and calibration cadence

## Maturity Scale
- 1.0–1.9: Initial (ad-hoc, minimal capabilities)
- 2.0–2.9: Developing (some capabilities, significant gaps)
- 3.0–3.9: Defined (solid foundation, scaling challenges)
- 4.0–4.9: Managed (mature capabilities, optimization focus)
- 5.0: Optimized (industry-leading, continuous improvement)

## Variables
- [COMPANY_TYPE]: Organization type
- [LEAD_VOLUME]: Monthly lead volume
- [CRM_PLATFORM]: CRM/marketing automation platform
- [HOT_THRESHOLD]: Score threshold for sales routing
- [DISQUALIFIERS]: Non-ICP signals or negative events
- [SLA_HOURS]: Speed-to-lead SLA

## Example (Condensed)
- Company: B2B software
- Scores (1–5): ICP 3; Signals 2; Data 2; Governance 2; Routing 3; Monitoring 2
- Top gaps: Missing intent tracking; unclear calibration process; weak feedback loop
- 60-day priorities: Define signal library; fix tracking fields; implement calibration cadence and closed-loop reporting

