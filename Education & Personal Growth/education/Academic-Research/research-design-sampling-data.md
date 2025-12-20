---
category: education
related_templates:
- education/Academic-Research/research-design-foundation.md
- education/Academic-Research/research-design-analysis-quality.md
- education/Academic-Research/research-design-overview.md
tags:
- sampling-strategy
- data-collection
- recruitment-planning
- instrumentation
- sampling-readiness
- data-collection-readiness
title: Research Sampling & Data Collection Readiness Assessment
use_cases:
- Evaluating readiness to recruit participants and collect high-quality data
- Identifying sampling, instrument, and fieldwork risks before launch
- Designing feasible data collection protocols with quality control
- Producing sampling and data collection plans suitable for IRB, grants, or theses
industries:
- education
- government
- healthcare
- nonprofit
type: framework
difficulty: intermediate
slug: research-design-sampling-data
---

# Research Sampling & Data Collection Readiness Assessment

## Purpose
Comprehensively assess readiness to recruit participants and collect defensible data across six dimensions: Population & Eligibility Clarity, Sampling Strategy & Adequacy, Recruitment & Retention Feasibility, Instrument & Measurement Fit, Data Collection Operations & Quality Control, and Data Management & Security. This framework helps you reduce avoidable bias, improve data quality, and prevent fieldwork failures.

## 🚀 Quick Prompt

> Assess **sampling and data collection readiness** for **{STUDY_CONTEXT}** using **{SAMPLING_APPROACH}** and collecting data via **{DATA_COLLECTION_PLAN}**. Evaluate across: (1) **Population & eligibility**—are inclusion/exclusion rules and the sampling frame explicit and testable? (2) **Sampling adequacy**—is the sample size (power/saturation) defensible and aligned to the inference goal? (3) **Recruitment feasibility**—are channels, incentives, and timeline realistic, with retention strategies? (4) **Measurement fit**—are instruments valid/reliable and feasible for the setting and population? (5) **Operations & QC**—are SOPs, training, pilots, and quality checks defined? (6) **Data management**—are privacy, storage, access control, backups, and versioning operational? Provide 1–5 scores, top risks, and a launch checklist.

**Usage:** Replace the curly-brace placeholders with your specifics. Use as a prompt to an AI assistant for rapid readiness evaluation.

---

## Template

Conduct a comprehensive sampling and data collection readiness assessment for {STUDY_CONTEXT} using {SAMPLING_APPROACH} and executing {DATA_COLLECTION_PLAN}.

Assess readiness across six dimensions, scoring each 1–5:

**1. POPULATION & ELIGIBILITY CLARITY READINESS**
Evaluate whether “who counts” is unambiguous by assessing whether the target population is defined with clear boundaries, inclusion/exclusion criteria can be applied consistently, and the sampling frame or access pathway is specified. Examine whether the definition prevents scope creep, supports equity and representation goals where relevant, and anticipates practical constraints such as language access, schedules, gatekeepers, and documentation needed to verify eligibility.

**2. SAMPLING STRATEGY & ADEQUACY READINESS**
Evaluate whether the sampling plan supports the inference goal by assessing whether the sampling method matches the design (probability vs non-probability, stratification, clustering, purposive criteria), whether sample size logic is defensible (power analysis for quantitative work, information power/saturation logic for qualitative work), and whether design effects, attrition, and subgroup analyses are considered. Examine whether the plan is robust to recruitment variability and whether stopping rules and reporting commitments are defined.

**3. RECRUITMENT & RETENTION FEASIBILITY READINESS**
Evaluate whether recruitment can actually happen by assessing whether recruitment channels are feasible and ethical, whether incentives are proportional and non-coercive, and whether the timeline matches expected response rates. Examine whether you have a plan for tracking outreach, screening, scheduling, follow-up, and no-shows, whether barriers (transport, childcare, technology) are addressed, and whether retention strategies exist for longitudinal or multi-touch designs.

**4. INSTRUMENT & MEASUREMENT FIT READINESS**
Evaluate whether measurement will be credible by assessing whether instruments are valid for the population and context, whether reliability expectations are realistic, and whether the operationalization of constructs matches the research questions. Examine whether instruments are appropriately translated/adapted, whether administration burden is acceptable, whether measurement timing aligns to outcomes, and whether you have a plan for piloting, cognitive testing, or expert review where needed.

**5. DATA COLLECTION OPERATIONS & QUALITY CONTROL READINESS**
Evaluate whether fieldwork will produce consistent data by assessing whether procedures are standardized via SOPs, data collectors are trained and calibrated, and pilots are planned to test the hardest parts of execution. Examine whether quality controls exist (completeness checks, protocol adherence, inter-rater reliability for observations/coding, device checks), whether incident handling and escalation paths are defined, and whether documentation supports auditability.

**6. DATA MANAGEMENT, PRIVACY & SECURITY READINESS**
Evaluate whether data will be protected and usable by assessing how data move from collection to storage to analysis, what identifiers are collected, and how de-identification and access control are enforced. Examine whether storage locations, backups, retention, and disposal are specified, whether versioning prevents accidental overwrites, whether permissions match team roles, and whether sharing plans (repositories, supplements) are consistent with consent and institutional requirements.

---

## Required Output Format

Structure your assessment as:

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, launch recommendation (go / revise-first), top 3 risks

2. **DIMENSION SCORECARD** - Table with each dimension, score (X.X/5), key gap, and the single highest-impact fix

3. **SAMPLING PLAN SUMMARY** - Population definition, eligibility rules, sampling method, sample size rationale (power/saturation), attrition assumptions

4. **RECRUITMENT & RETENTION PLAN** - Channels, scripts, incentives, tracking, retention tactics, timeline and volume targets

5. **DATA COLLECTION SOP OUTLINE** - Step-by-step procedure, training plan, pilot plan, QC checks and thresholds

6. **DATA FLOW & SECURITY PLAN** - Data flow diagram narrative, storage locations, permissions, de-identification, retention/disposal

Use this maturity scale:
- **1.0–1.9: Ad hoc** (unclear population/sampling; high risk of bias and unusable data)
- **2.0–2.9: Developing** (basic plan exists; major execution, measurement, or privacy gaps)
- **3.0–3.9: Defined** (credible plan; targeted improvements needed before launch)
- **4.0–4.9: Managed** (strong SOPs, QC, and governance; likely to execute reliably)
- **5.0: Exemplary** (best-in-class rigor, equity, and operational discipline)

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{STUDY_CONTEXT}` | What study you’re running (topic + design + setting) | "Cluster trial of a literacy intervention across 20 classrooms" |
| `{SAMPLING_APPROACH}` | How you will select participants or units | "Cluster sampling with stratification by school; target n=600 students" |
| `{DATA_COLLECTION_PLAN}` | What data you will collect and how | "Pre/post assessments + teacher observations + weekly attendance pulls" |

---

## Usage Example

**Input:**
"{STUDY_CONTEXT}: Qualitative study of patient experiences with telehealth follow-ups"
"{SAMPLING_APPROACH}: Purposive maximum-variation sampling; target 25–35 interviews until saturation"
"{DATA_COLLECTION_PLAN}: Semi-structured interviews (45 min) via video; optional short survey"

**Output (abridged):**
- Overall Readiness: **2.8/5.0 (Developing)**
- Recommendation: **REVISE-FIRST** (launch after a 1–2 week pilot and governance tightening)
- Top Risks: eligibility rules too vague (who qualifies as “telehealth follow-up”), interview guide not piloted for comprehension, data storage and de-identification workflow unspecified

Dimension Scorecard:
- Population & Eligibility: 2.5/5 (write testable eligibility checklist + screening script)
- Sampling Adequacy: 3.0/5 (define stopping rule + saturation reporting plan)
- Recruitment Feasibility: 2.7/5 (secure clinic recruitment workflow; reduce scheduling friction)
- Measurement Fit: 2.9/5 (pilot interview guide; add language access plan)
- Operations & QC: 2.6/5 (train interviewers; add interview QA checklist and audit trail)
- Data Management: 3.0/5 (define storage, access control, and de-identification SOP)

---

## Related Resources

- **[Research Design Foundation Readiness Assessment](research-design-foundation.md)** - Aligns theory, questions, and design choices before sampling decisions
- **[Research Analysis & Quality Assurance Readiness Assessment](research-design-analysis-quality.md)** - Aligns QA, reproducibility, and analysis plans with collected data
- **[Research Design - Overview](research-design-overview.md)** - Navigates the full research design readiness suite
