---
category: data-analytics
description: Assess experimental validity through randomization checks, covariate balance, attrition analysis, compliance evaluation, contamination detection, and statistical assumptions
title: Experimental Validity and Diagnostics
tags:
- experimental-validity
- randomization-check
- research-analytics
- causal-inference
use_cases:
- Verifying randomization success and covariate balance before analyzing treatment effects
- Detecting differential attrition that could bias experimental results
- Assessing compliance patterns and treatment contamination risks
- Checking statistical assumptions for valid inference
related_templates:
- data-analytics/Research-Analytics/experimental-design-implementation.md
- data-analytics/Research-Analytics/randomization-and-power-analysis.md
- data-analytics/Research-Analytics/treatment-effect-analysis.md
industries:
- healthcare
- technology
- education
- government
- finance
type: framework
difficulty: intermediate
slug: validity-and-diagnostics
---

# Experimental Validity and Diagnostics

## Purpose
Perform comprehensive validity assessment and diagnostic checks for experimental studies. This framework covers randomization verification, covariate balance assessment, attrition analysis, compliance evaluation, contamination detection, temporal effects, statistical assumption testing, and external validity assessment to ensure reliable causal inference from experimental data.

## Template

Conduct comprehensive validity assessment for {EXPERIMENT_DESCRIPTION}, evaluating {VALIDITY_CONCERNS} to ensure {ANALYSIS_OBJECTIVES}.

**1. Randomization Success Verification**

Begin by verifying that randomization successfully created comparable groups at baseline. For each key baseline covariate—demographics, prior outcomes, risk factors, and prognostic variables—compare distributions between treatment and control groups. Use t-tests for continuous variables and chi-square tests for categorical variables, but recognize that p-values alone are misleading with large samples (any trivial difference becomes significant) or small samples (meaningful imbalances may not reach significance). Calculate standardized differences (Cohen's d or standardized mean difference) as the primary balance metric—differences below 0.1 indicate excellent balance, 0.1-0.25 acceptable balance, and above 0.25 problematic imbalance requiring adjustment. Create a comprehensive balance table showing means or proportions by group, raw differences, standardized differences, and balance assessment for every baseline variable. Overall randomization success requires acceptable balance across the majority of covariates with no severe imbalances on key prognostic factors.

**2. Covariate Balance Assessment**

Conduct detailed covariate balance analysis beyond simple hypothesis tests. Calculate standardized differences for all baseline characteristics—for continuous variables, divide the mean difference by the pooled standard deviation; for binary variables, divide the proportion difference by the pooled standard error under independence. Visualize balance using Love plots showing standardized differences with reference lines at ±0.1 and ±0.25 thresholds. For any variables with standardized differences exceeding 0.25, investigate the source—chance imbalance, failed randomization implementation, or systematic issues. Document which variables show imbalance and their magnitude. Plan covariate adjustment in the primary analysis for variables with substantial imbalance, but recognize that adjusting for many covariates can introduce instability. Prioritize adjustment for strong prognostic factors that are also imbalanced, as these pose the greatest confounding threat.

**3. Attrition Analysis and Missing Data Assessment**

Analyze patterns of attrition (dropout, loss to follow-up, missing outcomes) that could bias results. Calculate overall attrition rate and compare rates between treatment and control groups—differential attrition is more concerning than equal attrition. Test for differential attrition using chi-square tests comparing dropout rates across arms. Beyond rates, examine whether attrition is related to baseline characteristics (selective attrition) by comparing completers to dropouts on all baseline variables within each arm. If certain types of participants disproportionately drop out from one arm, intention-to-treat estimates become biased. Assess whether attrition might be related to treatment itself (e.g., participants dropping out because the treatment is burdensome or ineffective). Document the pattern—is attrition random (MCAR), related to observed variables (MAR), or related to unobserved factors including outcomes themselves (MNAR)? Plan sensitivity analyses under different missing data assumptions.

**4. Compliance and Treatment Fidelity Evaluation**

Assess whether participants actually received the treatment as assigned. Calculate compliance rates in each arm—what proportion of treatment-assigned participants received treatment, and what proportion of control-assigned participants remained unexposed? Identify compliance types: compliers (follow assignment), always-takers (receive treatment regardless of assignment), never-takers (refuse treatment regardless of assignment), and defiers (do opposite of assignment—rare). For treatment arm, measure treatment fidelity—was the intervention delivered as designed? Document dose, duration, and quality of treatment delivery. For control arm, verify that participants did not receive the active treatment or close substitutes. Low compliance attenuates ITT estimates toward null; characterize the extent of this dilution. Calculate the proportion of variance in treatment receipt explained by random assignment—if assignment is a weak predictor of receipt, IV/CACE estimates may be unstable.

**5. Contamination and Spillover Detection**

Investigate whether control group participants were exposed to treatment elements, contaminating the comparison. Check for direct contamination—control participants somehow receiving the active treatment (crossed over, sought treatment elsewhere, shared materials with treatment participants). Assess indirect contamination through spillover—treatment effects spreading to controls via social networks, shared environments, or information diffusion. This is particularly concerning in cluster-randomized trials with incomplete cluster isolation or individual randomization within connected groups. Look for telltale signs: control group outcomes improving more than expected, treatment effect estimates smaller than pilot studies suggested, control participants reporting exposure to treatment elements. Examine intermediate outcomes or mechanism variables that should only change with treatment exposure. If contamination is detected, quantify its extent and plan analysis strategies—CACE estimation treats contamination as non-compliance, bounds analysis can estimate effects under different contamination scenarios.

**6. Temporal and Implementation Effects**

Assess time-related factors that could threaten validity. Check for temporal trends in enrollment—were earlier versus later enrollees systematically different, and did treatment assignment procedures remain consistent throughout? Examine whether treatment effects vary by enrollment timing or implementation phase. Look for maturation effects (participants changing naturally over time independent of treatment) and history effects (external events affecting outcomes differently across groups). In phased implementations, assess whether staggered rollout creates time-based confounding. Check for testing effects if repeated measurement occurred—did baseline assessment itself affect subsequent outcomes? Examine novelty and disruption effects that may inflate initial treatment impacts but fade over time. Document the implementation timeline and any deviations from protocol. For ongoing studies, assess whether interim analyses or unblinding events could have affected behavior.

**7. Statistical Assumption Verification**

Test assumptions underlying planned statistical analyses before proceeding. For t-tests and ANOVA, check normality of outcome distributions within each group using Shapiro-Wilk tests and visual inspection (histograms, Q-Q plots)—with large samples, modest non-normality is tolerable due to Central Limit Theorem. Test homogeneity of variance using Levene's test—unequal variances require Welch's correction or robust standard errors. For regression analyses, examine residual distributions for normality and homoscedasticity, check for influential observations and outliers, assess linearity of relationships. For clustered designs, verify that appropriate cluster-robust methods are planned and that number of clusters is sufficient (generally need 30+ clusters for reliable cluster-robust inference). If assumptions are violated, identify appropriate remedies—transformations, robust methods, non-parametric alternatives, or bootstrap inference.

**8. External Validity and Generalizability Assessment**

Evaluate the extent to which findings can generalize beyond the study sample and setting. Compare sample characteristics to target population on key dimensions—who was excluded by eligibility criteria, who declined participation, who dropped out? Calculate participation rates and characterize non-participants if data available. Assess setting representativeness—was the study conducted in specialized academic centers, typical clinical practices, or real-world conditions? Evaluate treatment implementation fidelity relative to how the intervention would be delivered at scale. Consider outcome measure relevance—do primary endpoints capture what matters clinically or practically? Examine whether treatment effects are likely context-dependent based on effect modification analyses. Document the specific population, setting, treatment implementation, and outcome definitions to which results directly apply, and reason carefully about extrapolation to other contexts.

Deliver your validity assessment as:

1. **Balance table** showing all baseline covariates with group means, standardized differences, and balance assessment
2. **Randomization verdict** with overall balance score and identification of any problematic imbalances
3. **Attrition report** with overall and differential rates, selective attrition tests, and missing data pattern assessment
4. **Compliance summary** documenting treatment receipt rates, compliance types, and fidelity assessment
5. **Contamination assessment** with evidence for or against spillover and cross-group exposure
6. **Temporal check** identifying any time-related threats to validity
7. **Assumption verification** confirming or flagging statistical assumption violations with recommended remedies
8. **Validity scorecard** with overall threat assessment and specific recommendations for analysis adjustments

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{EXPERIMENT_DESCRIPTION}` | Study design, sample, and outcome | "cluster-RCT of 40 schools testing math curriculum with 2,000 students and end-of-year test scores" |
| `{VALIDITY_CONCERNS}` | Specific validity threats to assess | "randomization at school level, 15% student attrition, variable implementation fidelity across classrooms" |
| `{ANALYSIS_OBJECTIVES}` | What valid inference requires | "unbiased ITT estimate with appropriate cluster adjustment and sensitivity to missing data assumptions" |

---

## Usage Examples

### Example 1: Clinical Trial Validity Check
**Prompt:** "Conduct comprehensive validity assessment for {EXPERIMENT_DESCRIPTION: double-blind RCT of 500 heart failure patients randomized to new medication versus placebo measuring 6-minute walk distance at 12 weeks}, evaluating {VALIDITY_CONCERNS: baseline imbalance on ejection fraction and NYHA class, 12% overall dropout with higher attrition in treatment arm, protocol deviations in 8% of patients}, to ensure {ANALYSIS_OBJECTIVES: valid primary efficacy analysis with appropriate handling of missing outcomes and non-compliance}."

**Expected Output:** Balance table showing 15 baseline covariates with standardized differences—ejection fraction shows 0.31 SD imbalance favoring control (problematic), NYHA class balanced (SD=0.08). Attrition analysis revealing 15% treatment vs 9% control dropout (differential, p=0.04), with dropouts having lower baseline walk distance. Compliance assessment showing 92% treatment receipt in active arm, 3% control crossover. Recommendation to adjust primary analysis for ejection fraction, conduct tipping point sensitivity analysis for missing outcomes assuming worse outcomes in treatment dropouts, and report both ITT and per-protocol results with caveats.

### Example 2: A/B Test Validity Assessment
**Prompt:** "Conduct comprehensive validity assessment for {EXPERIMENT_DESCRIPTION: website A/B test with 100,000 users randomized to new homepage versus control measuring 7-day conversion rate}, evaluating {VALIDITY_CONCERNS: potential bot traffic, users clearing cookies and re-randomizing, spillover through shared accounts}, to ensure {ANALYSIS_OBJECTIVES: clean treatment effect estimate with appropriate exclusions and variance estimation}."

**Expected Output:** Balance check on user characteristics showing excellent balance (all standardized differences <0.05) as expected with large sample and proper randomization. Bot detection analysis identifying 3.2% suspicious traffic patterns with similar rates across arms—recommend excluding. Cookie clearing assessment finding 2.1% of user IDs appearing in both arms over test period—violates stable unit treatment value assumption. Spillover check through shared household IP addresses finding minimal cross-arm correlation. Recommendations: exclude bot traffic, use first-assignment analysis for re-randomized users, cluster standard errors by household IP, report sensitivity with and without exclusions.

### Example 3: Educational Intervention Validity
**Prompt:** "Conduct comprehensive validity assessment for {EXPERIMENT_DESCRIPTION: cluster-randomized trial of 60 classrooms (30 treatment, 30 control) testing reading intervention with 1,500 students measuring reading scores at semester end}, evaluating {VALIDITY_CONCERNS: teacher-level randomization but student-level outcomes, 20% student mobility during semester, treatment teachers sharing materials with control teachers in same school}, to ensure {ANALYSIS_OBJECTIVES: valid cluster-adjusted treatment effect with appropriate handling of contamination and student mobility}."

**Expected Output:** Balance table at classroom level showing teacher experience, class size, and baseline reading scores—acceptable balance with largest imbalance on class size (SD=0.22). Student mobility analysis showing 18% treatment and 22% control students transferred (differential, p=0.08), with movers having lower baseline scores. Contamination investigation revealing 4 schools with both treatment and control classrooms—survey data suggests 25% of control teachers in mixed schools accessed intervention materials. ICC estimate of 0.15 requiring cluster adjustment. Recommendations: primary analysis excluding mixed schools with sensitivity including them, account for clustering with cluster-robust SEs (sufficient clusters), conduct bounds analysis for contamination effects, adjust for baseline reading and class size.

---

## Cross-References

- [experimental-design-implementation.md](experimental-design-implementation.md) - Designing experiments to minimize validity threats
- [randomization-and-power-analysis.md](randomization-and-power-analysis.md) - Proper randomization methods and sample sizing
- [treatment-effect-analysis.md](treatment-effect-analysis.md) - Analyzing effects accounting for validity issues
- [statistical-analysis.md](statistical-analysis.md) - Hypothesis testing and inference methods
