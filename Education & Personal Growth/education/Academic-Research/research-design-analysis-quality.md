---
title: Research Analysis & Quality Assurance Readiness Assessment
category: education
tags:
- analysis-planning
- validity-reliability
- statistical-strategy
- quality-assurance
- analysis-readiness
- reproducible-research
use_cases:
- Evaluating readiness to execute a credible data analysis plan
- Identifying methodological risks and quality assurance gaps before analysis begins
- Planning reproducible quantitative, qualitative, or mixed-methods analysis workflows
- Producing analysis deliverables suitable for thesis, IRB, grant, or journal submission
related_templates:
- education/Academic-Research/research-design-sampling-data.md
- education/Academic-Research/research-design-foundation.md
- education/Academic-Research/research-design-overview.md
industries:
- education
- government
- healthcare
- manufacturing
type: framework
difficulty: intermediate
slug: research-design-analysis-quality
---

# Research Analysis & Quality Assurance Readiness Assessment

## Purpose
Comprehensively assess readiness to run a defensible analysis and quality assurance workflow across six dimensions: Question-to-Estimand Fit, Data & Measurement Readiness, Method & Assumption Fit, Validity/Reliability/Trustworthiness, Reproducibility & Auditability, and Interpretation & Reporting. This framework helps you prevent avoidable analysis errors, reduce rework, and produce outputs that withstand peer review.

## Template

Conduct a comprehensive research analysis and quality assurance readiness assessment for {STUDY_CONTEXT} using {DATA_TYPE} to address {ANALYSIS_GOALS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. QUESTION-TO-ESTIMAND FIT READINESS**
Evaluate whether the analysis is anchored to explicit questions by assessing whether primary and secondary questions are stated in testable terms, whether the target estimand or inference goal is clear, and whether inclusion/exclusion logic and subgroup intentions are pre-specified rather than discovered during analysis. Examine whether the analysis distinguishes confirmatory from exploratory work, defines what “success” would look like for key outcomes, and clarifies how contradictory evidence will be handled so interpretation does not drift with the data.

**2. DATA & MEASUREMENT READINESS**
Evaluate whether the data can support the planned inferences by assessing whether key variables are defined unambiguously, measurement quality is understood, coding rules are documented, and a data dictionary exists that matches the actual dataset. Examine whether missing data mechanisms are hypothesized and tracked, whether outliers and invalid values have a handling policy, whether timing and units are consistent, and whether any derived variables can be recreated deterministically from raw sources.

**3. METHOD & ASSUMPTION FIT READINESS**
Evaluate whether the chosen methods are appropriate by assessing whether statistical tests or models match the design and data-generating process, whether assumptions are named and checkable, and whether alternative methods are planned when assumptions fail. For qualitative work, assess whether the analytic approach (thematic, content, grounded, narrative) matches the research purpose, and whether the coding process is specified with a plan for reflexivity and iteration. For mixed methods, examine whether integration strategy is explicit, with a plan for resolving conflicts between strands.

**4. VALIDITY, RELIABILITY & TRUSTWORTHINESS READINESS**
Evaluate whether major threats to credibility are identified and mitigated by assessing internal validity risks (selection bias, confounding, attrition, measurement artifacts) and the specific safeguards you will apply. For quantitative measures, examine reliability evidence (inter-rater, test-retest, internal consistency) and whether measurement error is considered in interpretation. For qualitative data, assess planned credibility strategies such as triangulation, member checking where appropriate, peer debriefing, negative case analysis, and an audit trail that supports confirmability.

**5. REPRODUCIBILITY & AUDITABILITY READINESS**
Evaluate whether someone else could reasonably follow your analysis by assessing whether a scripted workflow exists (or is planned) with clear inputs/outputs, version control, and deterministic data processing steps. Examine whether you have a plan for storing raw vs cleaned data, documenting transformations, logging decisions, and producing a minimal “analysis package” (scripts, README, codebook, output tables/figures) that matches your privacy constraints while still enabling audit and reuse.

**6. INTERPRETATION & REPORTING READINESS**
Evaluate whether results can be communicated responsibly by assessing whether you will report uncertainty (confidence intervals/credible intervals, sensitivity analyses), effect sizes and practical relevance, and limitations tied to design and measurement. Examine whether claims are bounded to what the data support, whether multiple comparisons and exploratory findings will be labeled honestly, and whether you have identified reporting standards or venue expectations that shape structure, terminology, and required disclosures.

---

## Required Output Format

Structure your assessment as:

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, go/no-go recommendation for analysis start, top 3 risks

2. **DIMENSION SCORECARD** - Table with each dimension, score (X.X/5), key gap, and the single highest-impact fix

3. **ANALYSIS BLUEPRINT** - The planned steps from raw data to final outputs (cleaning → transformations → primary analyses → secondary → sensitivity → visuals)

4. **QUALITY ASSURANCE PLAN** - Specific checks, thresholds, and review points (data checks, assumption checks, IRR targets, audit trail, peer review)

5. **RISK REGISTER** - Top 5 failure modes (e.g., missingness, assumption violations, coding drift, confounding) with mitigations

6. **DELIVERABLES & TIMELINE** - What you will produce (tables, figures, appendices, code) and when (weeks)

Use this maturity scale:
- **1.0–1.9: Ad hoc** (methods and QA unclear; high risk of invalid conclusions)
- **2.0–2.9: Developing** (some plan exists; gaps in checks, documentation, or fit)
- **3.0–3.9: Defined** (solid plan; targeted improvements needed for robustness)
- **4.0–4.9: Managed** (strong QA, reproducibility, and reporting discipline)
- **5.0: Exemplary** (best-in-class rigor, transparency, and defensible inference)

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{STUDY_CONTEXT}` | What study/project the analysis supports (design + topic) | "Quasi-experimental evaluation of a nurse staffing policy across 12 hospitals" |
| `{DATA_TYPE}` | The kind of data and approach (quant/qual/mixed) | "Administrative panel data + interviews (mixed-methods)" |
| `{ANALYSIS_GOALS}` | The primary questions and decisions the analysis must support | "Estimate policy impact on turnover and explain mechanisms from qualitative themes" |

---

## Usage Example

**Input:**
"{STUDY_CONTEXT}: Mixed-methods study of teacher retention across 50 schools"
"{DATA_TYPE}: Survey (n=520) + semi-structured interviews (n=36)"
"{ANALYSIS_GOALS}: Identify predictors of retention and triangulate quantitative predictors with qualitative explanations"

**Output (abridged):**
- Overall Readiness: **2.7/5.0 (Developing)**
- Recommendation: **CONDITIONAL GO** (start analysis after a 2-week QA and specification sprint)
- Top Risks: unclear primary estimand and subgroup plan, missing-data strategy not defined, qualitative coding process lacks IRR and audit trail

Dimension Scorecard:
- Question-to-Estimand Fit: 2.5/5 (write a 1-page analysis specification; label confirmatory vs exploratory)
- Data & Measurement: 2.8/5 (create codebook, missingness report, and variable derivation log)
- Method & Assumption Fit: 2.7/5 (predefine model family + assumption checks; add sensitivity analyses)
- Validity/Reliability/Trustworthiness: 2.4/5 (add confounder plan; set IRR target κ ≥ 0.75; plan negative cases)
- Reproducibility & Auditability: 3.0/5 (move to scripted pipeline; version datasets; write analysis README)
- Interpretation & Reporting: 2.9/5 (predefine effect size reporting and claim boundaries)

Two-week plan:
- Week 1: Finalize estimands, analysis plan, missingness strategy, and coding protocol.
- Week 2: Pilot code qualitative data with IRR check; implement scripted cleaning + first-pass models.

---

## Related Resources

- **[Research Design - Sampling & Data](research-design-sampling-data.md)** - Aligns measurement, sampling, and data collection choices to analysis needs
- **[Research Design - Foundation](research-design-foundation.md)** - Supports research question refinement, theory alignment, and design selection
- **[Research Design - Overview](research-design-overview.md)** - Integrates the full research design workflow across modules
