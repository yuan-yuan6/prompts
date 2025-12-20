---
category: data-analytics
description: Analyze treatment effects using ITT, per-protocol, instrumental variable, CACE, dose-response, and subgroup analyses for causal inference
title: Treatment Effect Analysis
tags:
- treatment-effect
- causal-inference
- itt-analysis
- research-analytics
use_cases:
- Analyzing randomized controlled trial outcomes with intention-to-treat and per-protocol approaches
- Estimating complier average causal effects when treatment compliance varies
- Conducting dose-response analysis to understand adherence-outcome relationships
- Performing subgroup analyses to identify differential treatment effects
related_templates:
- data-analytics/Research-Analytics/experimental-design-implementation.md
- data-analytics/Research-Analytics/randomization-and-power-analysis.md
- data-analytics/Research-Analytics/statistical-analysis.md
industries:
- healthcare
- technology
- finance
- education
- government
type: framework
difficulty: advanced
slug: treatment-effect-analysis
---

# Treatment Effect Analysis

## Purpose
Perform comprehensive treatment effect analysis using advanced causal inference methods. This framework covers intention-to-treat (ITT), per-protocol (PP), instrumental variable (IV), complier average causal effect (CACE), dose-response, and subgroup analysis approaches to quantify treatment impacts and establish causal relationships from experimental data.

## Template

Conduct comprehensive treatment effect analysis for {EXPERIMENT_DESCRIPTION}, comparing {TREATMENT_COMPARISON} to inform {DECISION_CONTEXT}.

**1. Analysis Framework and Primary Approach**

Begin by establishing the analysis framework aligned with your study design and objectives. Intention-to-treat (ITT) analysis serves as the primary approach for randomized experiments—analyze all participants according to their randomized assignment regardless of whether they actually received or adhered to treatment. ITT preserves randomization's protection against confounding and provides a conservative estimate of treatment effect under real-world conditions where non-compliance occurs. Define your primary outcome measure, specify the effect metric (mean difference for continuous outcomes, risk ratio or odds ratio for binary outcomes, hazard ratio for time-to-event), and determine covariate adjustment strategy. Pre-specify all analyses before examining outcome data to maintain validity.

**2. Intention-to-Treat Analysis Execution**

Execute the ITT analysis comparing outcomes between randomized groups. Calculate descriptive statistics for each group including means, standard deviations, and sample sizes for continuous outcomes or proportions and counts for binary outcomes. Perform the primary statistical test—t-test or ANCOVA for continuous outcomes, chi-square or logistic regression for binary outcomes, log-rank test or Cox regression for survival outcomes. Calculate the treatment effect estimate with 95% confidence interval. Compute effect size using Cohen's d for continuous outcomes (small=0.2, medium=0.5, large=0.8) or number needed to treat (NNT) for binary outcomes. Handle missing outcome data using appropriate methods—complete case analysis as primary with sensitivity analyses using multiple imputation or worst-case scenarios. Report both statistical significance (p-value) and practical significance (effect size interpretation).

**3. Per-Protocol and Compliance-Adjusted Analyses**

Conduct secondary analyses that account for actual treatment received. Per-protocol analysis restricts to participants who completed treatment as specified—define compliance criteria clearly (e.g., received ≥80% of prescribed doses, attended all sessions). Compare compliant treatment participants to compliant control participants. Recognize that per-protocol analysis breaks randomization and can introduce selection bias—compliers may differ systematically from non-compliers. Use per-protocol results as a sensitivity analysis showing the effect under ideal compliance, not as the primary finding. Calculate compliance rates in each arm and characterize completers versus non-completers on baseline variables to assess potential bias.

**4. Instrumental Variable and CACE Estimation**

Estimate treatment effects for compliers using instrumental variable methods when compliance varies. In randomized trials, random assignment serves as an instrument for actual treatment receipt—it affects the outcome only through its effect on treatment. Calculate the Complier Average Causal Effect (CACE) as the ratio of ITT effect on the outcome to ITT effect on treatment receipt (compliance differential between arms). CACE estimates the effect for participants who would comply when assigned to treatment but not receive treatment when assigned to control. Verify instrument strength—the first-stage F-statistic should exceed 10 to avoid weak instrument bias. Report CACE alongside ITT, interpreting CACE as the efficacy estimate (effect if taken) versus ITT as the effectiveness estimate (effect of offering treatment).

**5. Dose-Response Analysis**

Analyze the relationship between treatment dose or adherence and outcomes. Define the dose measure—percentage of prescribed doses taken, number of sessions attended, treatment duration, or measured biomarker of exposure. Fit linear dose-response models estimating outcome change per unit increase in dose. Test for non-linear relationships by adding quadratic terms or using spline models; compare model fit using F-tests or information criteria. Recognize that dose-response analysis is observational even within a trial—adherence is not randomized, so confounding by indication or healthy adherer bias may affect estimates. Adjust for baseline confounders that predict both adherence and outcomes. Visualize the dose-response curve with confidence bands and identify any threshold effects or saturation points.

**6. Subgroup Analysis and Effect Modification**

Examine whether treatment effects differ across participant subgroups. Pre-specify subgroup variables based on scientific rationale—characteristics that might modify treatment response such as disease severity, demographics, genetic markers, or baseline risk. Estimate treatment effects within each subgroup level, calculating effect size and confidence interval. Critically, test for statistical interaction between treatment and subgroup variable rather than comparing p-values across subgroups—a significant effect in one subgroup and non-significant in another does not demonstrate differential effects. Apply appropriate multiple testing corrections (Bonferroni, Benjamini-Hochberg) given the number of subgroups examined. Present results in forest plots showing point estimates and confidence intervals across subgroups with overall effect and interaction p-value. Interpret subgroup findings cautiously—they are hypothesis-generating unless the study was powered for subgroup differences.

**7. Sensitivity Analyses and Robustness Checks**

Conduct sensitivity analyses to assess robustness of primary findings. Test alternative outcome definitions if ambiguity exists. Compare results with and without covariate adjustment to assess consistency. Perform per-protocol analysis and CACE estimation as described to bound the treatment effect under different assumptions about compliance. Handle missing data through multiple approaches—complete case, multiple imputation, last observation carried forward, worst-case imputation—to assess sensitivity to missing data assumptions. Test for baseline imbalance despite randomization and adjust if substantial differences exist. Assess the impact of outliers by analyzing with and without extreme values. Document all sensitivity analyses and whether conclusions remain consistent across approaches.

**8. Clinical Significance and Practical Interpretation**

Translate statistical findings into clinically or practically meaningful conclusions. Distinguish statistical significance (reliable difference from zero) from clinical significance (difference large enough to matter). Interpret effect sizes using domain-specific benchmarks—what constitutes a meaningful improvement for this outcome in this population? Calculate number needed to treat (NNT) for beneficial outcomes or number needed to harm (NNH) for adverse effects to communicate in absolute terms. Compare treatment effect to minimal clinically important difference (MCID) if established for the outcome. Consider treatment burden, cost, and risk alongside efficacy when drawing conclusions. Frame results in terms of the proportion of patients who would benefit, the expected magnitude of benefit, and the confidence in these estimates. Provide clear recommendations for clinical practice or policy implementation based on the totality of evidence.

Deliver your treatment effect analysis as:

1. **Primary ITT results** with effect estimate, 95% CI, p-value, and effect size interpretation
2. **Per-protocol results** as sensitivity analysis with compliance rates documented
3. **CACE estimate** if compliance varies meaningfully between arms
4. **Dose-response analysis** showing adherence-outcome relationship with visualization
5. **Subgroup forest plot** with interaction tests and appropriate caveats
6. **Sensitivity summary** showing consistency of findings across analytical approaches
7. **Clinical interpretation** with NNT/NNH, comparison to MCID, and practical significance
8. **Recommendations** for treatment implementation based on findings

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{EXPERIMENT_DESCRIPTION}` | Study design, sample, and outcome | "double-blind RCT of 400 diabetes patients measuring HbA1c reduction at 6 months" |
| `{TREATMENT_COMPARISON}` | Treatment and control conditions | "new GLP-1 agonist versus placebo with standard care" |
| `{DECISION_CONTEXT}` | How results will inform decisions | "formulary inclusion decision and prescribing guidelines" |

---

## Usage Examples

### Example 1: Clinical Trial Analysis
**Prompt:** "Conduct comprehensive treatment effect analysis for {EXPERIMENT_DESCRIPTION: phase 3 RCT of 800 patients with moderate depression randomized to digital CBT app versus waitlist control measuring PHQ-9 at 8 weeks}, comparing {TREATMENT_COMPARISON: app-based cognitive behavioral therapy with coach support versus usual care waitlist}, to inform {DECISION_CONTEXT: health plan coverage decision and clinical pathway integration}."

**Expected Output:** ITT analysis showing mean PHQ-9 reduction of 4.2 points greater in treatment arm (95% CI: 3.1-5.3, p<0.001, Cohen's d=0.62). Compliance analysis showing 68% completed ≥6 of 8 modules; per-protocol effect of 5.8 points (compliers only). CACE estimate of 6.2 points representing efficacy among engagers. Dose-response showing linear relationship (0.7 point improvement per module completed, p<0.001). Subgroup analysis finding larger effects in moderate versus mild depression (interaction p=0.03) but similar effects across age groups. NNT of 4 for clinically meaningful response (≥50% PHQ-9 reduction). Recommendation supporting coverage with engagement monitoring.

### Example 2: A/B Test Treatment Effects
**Prompt:** "Conduct comprehensive treatment effect analysis for {EXPERIMENT_DESCRIPTION: 50,000-user A/B test of new checkout flow measuring 30-day purchase conversion and average order value}, comparing {TREATMENT_COMPARISON: streamlined 2-step checkout versus existing 4-step checkout}, to inform {DECISION_CONTEXT: product launch decision and expected revenue impact}."

**Expected Output:** ITT analysis showing 12.3% relative lift in conversion (8.4% vs 7.5% baseline, 95% CI: 8.9%-15.8%, p<0.001). AOV unchanged ($67.20 vs $66.80, p=0.42). Per-protocol analysis excluding users who abandoned before reaching checkout shows 18.2% lift among engaged shoppers. Subgroup analysis revealing mobile users show 22% lift while desktop shows 6% lift (interaction p<0.001), new users benefit more than returning users. No dose-response applicable. Expected revenue impact of $2.4M annually at current traffic. Recommendation to launch with mobile-first priority and monitoring for desktop segment.

### Example 3: Educational Intervention Analysis
**Prompt:** "Conduct comprehensive treatment effect analysis for {EXPERIMENT_DESCRIPTION: cluster-randomized trial of 120 classrooms (2,400 students) testing math tutoring software measuring standardized test score gains over one semester}, comparing {TREATMENT_COMPARISON: adaptive AI tutoring with 30 min/day usage requirement versus standard curriculum}, to inform {DECISION_CONTEXT: district-wide adoption decision and implementation requirements}."

**Expected Output:** ITT analysis (cluster-adjusted) showing 0.18 SD improvement in test scores (95% CI: 0.08-0.28, p<0.001). Per-protocol restricting to classrooms achieving ≥80% usage compliance shows 0.31 SD effect. CACE estimated at 0.35 SD for complying classrooms. Dose-response analysis showing diminishing returns above 25 min/day with threshold effect below 15 min/day (minimal benefit). Subgroup analysis finding largest effects for students starting below grade level (0.32 SD) versus at/above grade level (0.11 SD, interaction p=0.02). Cost-effectiveness of $180 per 0.1 SD gain. Recommendations supporting adoption with 20-30 min daily usage targets and priority deployment for struggling students.

---

## Cross-References

- [experimental-design-implementation.md](experimental-design-implementation.md) - Designing experiments for causal inference
- [randomization-and-power-analysis.md](randomization-and-power-analysis.md) - Sample size and randomization methods
- [statistical-analysis.md](statistical-analysis.md) - Hypothesis testing and inference
- [validity-and-diagnostics.md](validity-and-diagnostics.md) - Assessing experimental validity
