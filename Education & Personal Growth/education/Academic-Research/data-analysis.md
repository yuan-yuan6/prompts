---
category: education
title: Data Analysis Readiness Assessment
tags:
- research-data-analysis
- statistical-methods
- qualitative-analysis
- mixed-methods
- readiness-assessment
use_cases:
- Determining whether a study is ready for preregistration, analysis start, or final reporting
- Identifying analysis plan gaps (methods, assumptions, QA, reproducibility)
- Producing a concise analysis blueprint aligned to research questions and data constraints
- Reducing rework by clarifying decisions before touching the data
related_templates:
- education/Academic-Research/research-design-analysis-quality.md
- education/Academic-Research/research-design.md
- education/curriculum-development.md
- education/curriculum-development-framework.md
industries:
- education
- government
- manufacturing
- technology
type: framework
difficulty: intermediate
slug: data-analysis
---

# Data Analysis Readiness Assessment

## Purpose
Assess whether you are ready to run and defend your analysis by scoring six dimensions: Question→Method Fit, Data Readiness, Modeling & Assumptions, Robustness & Validity Checks, Reproducibility & QA, and Reporting & Interpretation. Use this to produce a clear **analysis blueprint** and a **revise-first** checklist.

## Template

Conduct a data analysis readiness assessment for {STUDY_CONTEXT} using {DATA_TYPE} to achieve {ANALYSIS_GOALS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. QUESTION → METHOD FIT READINESS**
Evaluate whether the analysis answers the actual questions by mapping each research question/hypothesis to an estimand or qualitative claim, the corresponding variables/constructs, and the planned method. Confirm that outcomes/exposures are operationally defined, comparison groups (if any) are explicit, and the analysis will yield interpretable conclusions.

**2. DATA READINESS**
Evaluate whether the data can support the plan by assessing completeness, missingness mechanisms, measurement quality, timing, and linkage/integration constraints. Confirm you have clear rules for inclusion/exclusion, deduplication, outliers, and a plan for data documentation (data dictionary, provenance, transformations).

**3. MODELING & ASSUMPTIONS READINESS**
Evaluate whether method assumptions and diagnostics are planned: distributional assumptions, independence, collinearity, confounding, measurement error, and model specification choices. For qualitative/mixed methods, confirm the analytic stance (inductive/deductive), coding approach, and a clear path from raw data to claims.

**4. ROBUSTNESS & VALIDITY CHECKS READINESS**
Evaluate whether you will stress-test conclusions: sensitivity analyses, alternative specifications, subgroup checks (pre-specified), multiple comparisons strategy, and checks against overfitting. For qualitative work, include credibility strategies (triangulation, negative cases, peer debrief) and boundary conditions.

**5. REPRODUCIBILITY & QA READINESS**
Evaluate whether analysis can be repeated and audited: versioning of data and code, environment capture, logging, and an analysis “audit trail.” Confirm code review, spot-check procedures, and conventions for file organization, naming, and outputs.

**6. REPORTING & INTERPRETATION READINESS**
Evaluate whether reporting will be honest and aligned to standards: effect size reporting, uncertainty, assumption violations, limitations, and what constitutes practical significance. Confirm a plan for tables/figures, preregistration alignment (if applicable), and how you will handle null or ambiguous results.

---

## Required Output Format

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, go/revise-first recommendation, top 3 risks

2. **DIMENSION SCORECARD** - Table: dimension, score (1–5), evidence, biggest gap, highest-impact fix

3. **ANALYSIS BLUEPRINT (ONE PAGE)**
- Questions → variables → method (bullet map)
- Primary analysis (what, why, how)
- Secondary / exploratory analyses (clearly labeled)
- Decision rules (missing data, exclusions, outliers)

4. **QA & REPRO CHECKLIST**
- Data version + code version
- Environment capture
- Review/verification steps
- Output folder conventions

5. **NEXT 7 DAYS** - Prioritized actions with owners and due dates

---

## Maturity Scale (1–5)
- **1 — Initial:** Unclear mapping from questions to methods; ad-hoc cleaning; low auditability.
- **2 — Developing:** Basic plan exists; major gaps in assumptions, QA, or reporting discipline.
- **3 — Defined:** Coherent plan; documented decisions; key checks planned; moderate execution risk.
- **4 — Managed:** Strong diagnostics/robustness; reproducible workflows; reporting aligned to standards.
- **5 — Optimized:** Highly reliable, reusable analysis system; fast iteration with strong governance.

---

## Variables (Use Max 3)

| Variable | What to include | Example |
|---|---|---|
| `{STUDY_CONTEXT}` | Design + population + setting + key question | “Observational cohort of ICU patients; predict 30-day readmission” |
| `{DATA_TYPE}` | Sources + structure + constraints | “EHR tables + notes; missing labs; de-identified dataset” |
| `{ANALYSIS_GOALS}` | What decisions/claims the analysis must support | “Estimate association + build calibrated risk model + explain drivers” |

---

## Example (Filled)

**Input**
- `{STUDY_CONTEXT}`: “Mixed-methods evaluation of a new training program for nurses across 3 hospitals.”
- `{DATA_TYPE}`: “Survey (Likert), performance metrics, and 20 semi-structured interviews.”
- `{ANALYSIS_GOALS}`: “Quantify outcome change; understand barriers; generate implementation recommendations.”

**Output (abridged)**
- Executive summary: 3.4/5 (Defined), **revise-first**
- Biggest gaps: missing data rules (survey nonresponse), qualitative trustworthiness plan, multiple comparisons strategy
- Next 7 days: draft estimand map + preregister primary outcomes; create codebook + coding protocol; define sensitivity analyses and reporting templates

---

## Best Practices (8)

1. Write down the question→method mapping before cleaning the data.
2. Separate confirmatory vs exploratory analyses and label them clearly.
3. Predefine decision rules (exclusions, missingness, transformations) to avoid bias.
4. Prefer interpretable outputs; only add complexity if it changes decisions.
5. Always plan diagnostics and what you’ll do if assumptions fail.
6. Treat reproducibility as a feature: versions, scripts, and a clean audit trail.
7. Use robustness checks to test conclusions, not to fish for significance.
8. Report limitations and uncertainty without hedging away the core finding.

---

## Related Resources
- Use the suite module for analysis rigor and QA patterns: `research-design-analysis-quality.md`
- Use the master router to align design and analysis choices: `research-design.md`
