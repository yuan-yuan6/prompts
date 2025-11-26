```markdown
---
title: Statistical Experimentation & A/B Testing Framework
category: data-analytics
tags:
- data-analytics
- ab-testing
- experimentation
- statistics
use_cases:
- Creating comprehensive experimentation framework covering A/B testing, multivariate
  testing, causal inference, and statistical analysis to drive data-driven decision
  making with rigorous methodology.
- Product feature experimentation
- Marketing campaign optimization
- Pricing and conversion optimization
related_templates:
- data-analytics/dashboard-design-patterns.md
- data-analytics/predictive-modeling-framework.md
- data-analytics/Advanced-Analytics/time-series-analysis.md
last_updated: 2025-11-25
industries:
- e-commerce
- finance
- healthcare
- retail
- technology
type: template
difficulty: intermediate
slug: statistical-experimentation
---

# Statistical Experimentation & A/B Testing Framework

## Purpose
Comprehensive experimentation framework covering A/B testing, multivariate testing, causal inference, and statistical analysis to drive data-driven decision making with rigorous methodology and reliable results.

## Quick Experimentation Prompt
> Design an A/B test for [feature/change] measuring [primary metric]. Users: [sample size]. Duration: [timeline]. Include: (1) Hypothesis and success criteria, (2) Sample size calculation with MDE, (3) Randomization and segmentation strategy, (4) Analysis plan with statistical tests and guardrail metrics.

## Quick Start

Run experiments in 4 steps:

1. **Define Hypothesis**: Formulate clear hypothesis (e.g., "Adding product reviews will increase conversion rate by 5%"), define primary metric, secondary metrics, and guardrail metrics (metrics that should not degrade).

2. **Calculate Sample Size**: Determine minimum detectable effect (MDE), set significance level (α = 0.05) and power (1-β = 0.80), calculate required sample size, and estimate experiment duration.

3. **Design & Implement**: Set up randomization (user-level, session-level), define control and treatment groups, implement tracking, run A/A test to validate setup, then launch experiment.

4. **Analyze & Decide**: Check for sample ratio mismatch, calculate test statistics and confidence intervals, assess practical significance (not just statistical), document learnings, and make go/no-go decision.

## Template

Design experiment for [EXPERIMENT_NAME] testing [HYPOTHESIS] with [SAMPLE_SIZE] users over [DURATION], targeting [MDE]% minimum detectable effect on [PRIMARY_METRIC] with [CONFIDENCE]% confidence.

### 1. Experiment Definition

| **Component** | **Specification** | **Details** | **Rationale** |
|--------------|------------------|-------------|--------------|
| Experiment Name | [EXPERIMENT_NAME] | [EXP_DESCRIPTION] | [EXP_RATIONALE] |
| Hypothesis | [HYPOTHESIS] | [HYPOTHESIS_DETAILS] | [HYPOTHESIS_BASIS] |
| Primary Metric | [PRIMARY_METRIC] | [PRIMARY_DEFINITION] | [PRIMARY_RATIONALE] |
| Secondary Metrics | [SECONDARY_METRICS] | [SECONDARY_DEFINITIONS] | [SECONDARY_RATIONALE] |
| Guardrail Metrics | [GUARDRAIL_METRICS] | [GUARDRAIL_DEFINITIONS] | [GUARDRAIL_RATIONALE] |
| Success Criteria | [SUCCESS_CRITERIA] | [CRITERIA_DETAILS] | [CRITERIA_RATIONALE] |

### 2. Statistical Design

**Power Analysis & Sample Size:**
```
Parameters:
- Baseline Conversion Rate: [BASELINE_RATE]%
- Minimum Detectable Effect (MDE): [MDE]%
- Significance Level (α): [ALPHA] (typically 0.05)
- Statistical Power (1-β): [POWER] (typically 0.80)
- Test Type: [TEST_TYPE] (one-tailed, two-tailed)
- Multiple Comparisons: [COMPARISONS]

Sample Size Calculation:
- Per Variant: [SAMPLE_PER_VARIANT]
- Total Sample: [TOTAL_SAMPLE]
- Daily Traffic: [DAILY_TRAFFIC]
- Required Duration: [DURATION_DAYS] days

Sensitivity Analysis:
- At 80% power: [SAMPLE_80] users
- At 90% power: [SAMPLE_90] users
- At 95% power: [SAMPLE_95] users
```

| **Scenario** | **MDE** | **Sample Size** | **Duration** | **Power** | **Trade-off** |
|-------------|--------|----------------|-------------|----------|--------------|
| Aggressive | [AGG_MDE]% | [AGG_SAMPLE] | [AGG_DURATION] | [AGG_POWER] | [AGG_TRADE] |
| Balanced | [BAL_MDE]% | [BAL_SAMPLE] | [BAL_DURATION] | [BAL_POWER] | [BAL_TRADE] |
| Conservative | [CON_MDE]% | [CON_SAMPLE] | [CON_DURATION] | [CON_POWER] | [CON_TRADE] |

### 3. Randomization Strategy

**Assignment Method:**
```
Randomization Unit:
- Unit Type: [RAND_UNIT] (user, session, device, cookie)
- Identifier: [RAND_ID]
- Consistency: [CONSISTENCY] (sticky assignment)
- Hash Function: [HASH_FUNCTION]

Traffic Allocation:
- Control: [CONTROL_PERCENT]%
- Treatment(s): [TREATMENT_PERCENT]%
- Holdout: [HOLDOUT_PERCENT]%
- Ramp-up Schedule: [RAMP_SCHEDULE]

Segmentation:
- Stratification Variables: [STRAT_VARS]
- Blocking: [BLOCKING]
- Pre-assignment Covariates: [COVARIATES]

Quality Checks:
- A/A Test: [AA_TEST]
- Sample Ratio Mismatch (SRM): [SRM_CHECK]
- Covariate Balance: [COV_BALANCE]
```

### 4. Experiment Variants

| **Variant** | **Name** | **Description** | **Traffic** | **Implementation** | **Status** |
|------------|---------|-----------------|------------|-------------------|-----------|
| Control | [CTRL_NAME] | [CTRL_DESC] | [CTRL_TRAFFIC]% | [CTRL_IMPL] | [CTRL_STATUS] |
| Treatment A | [TREAT_A_NAME] | [TREAT_A_DESC] | [TREAT_A_TRAFFIC]% | [TREAT_A_IMPL] | [TREAT_A_STATUS] |
| Treatment B | [TREAT_B_NAME] | [TREAT_B_DESC] | [TREAT_B_TRAFFIC]% | [TREAT_B_IMPL] | [TREAT_B_STATUS] |
| Treatment C | [TREAT_C_NAME] | [TREAT_C_DESC] | [TREAT_C_TRAFFIC]% | [TREAT_C_IMPL] | [TREAT_C_STATUS] |

### 5. Metric Definitions

**Primary Metric:**
```
Metric: [PRIMARY_METRIC]
Definition: [PRIMARY_DEFINITION]
Formula: [PRIMARY_FORMULA]
Data Source: [PRIMARY_SOURCE]
Aggregation: [PRIMARY_AGG] (user-level, session-level)
Attribution Window: [ATTRIBUTION_WINDOW]
Expected Direction: [EXPECTED_DIRECTION]
Practical Significance: [PRACTICAL_SIG]
```

**Secondary & Guardrail Metrics:**
| **Metric** | **Type** | **Definition** | **Formula** | **Threshold** | **Direction** |
|-----------|---------|---------------|------------|--------------|--------------|
| [METRIC_1] | [TYPE_1] | [DEF_1] | [FORMULA_1] | [THRESH_1] | [DIR_1] |
| [METRIC_2] | [TYPE_2] | [DEF_2] | [FORMULA_2] | [THRESH_2] | [DIR_2] |
| [METRIC_3] | [TYPE_3] | [DEF_3] | [FORMULA_3] | [THRESH_3] | [DIR_3] |
| [METRIC_4] | [TYPE_4] | [DEF_4] | [FORMULA_4] | [THRESH_4] | [DIR_4] |
| [METRIC_5] | [TYPE_5] | [DEF_5] | [FORMULA_5] | [THRESH_5] | [DIR_5] |

### 6. Statistical Analysis Plan

**Analysis Methods:**
```
Primary Analysis:
- Test: [PRIMARY_TEST] (t-test, chi-square, Mann-Whitney)
- Confidence Level: [CONFIDENCE]%
- Effect Size: [EFFECT_SIZE] (Cohen's d, odds ratio)
- Confidence Interval: [CI_METHOD]

Multiple Testing Correction:
- Method: [CORRECTION_METHOD] (Bonferroni, Holm, FDR)
- Family-wise Error Rate: [FWER]
- Adjusted Alpha: [ADJ_ALPHA]

Variance Reduction:
- CUPED: [CUPED] (Controlled Using Pre-Experiment Data)
- Stratification: [STRATIFICATION]
- Regression Adjustment: [REGRESSION_ADJ]
- Expected Variance Reduction: [VAR_REDUCTION]%

Sequential Analysis:
- Method: [SEQ_METHOD] (optional)
- Alpha Spending: [ALPHA_SPENDING]
- Interim Looks: [INTERIM_LOOKS]
- Stopping Rules: [STOPPING_RULES]
```

### 7. Pre-Experiment Validation

| **Validation Step** | **Method** | **Criteria** | **Result** | **Action if Failed** |
|--------------------|-----------|-------------|-----------|---------------------|
| A/A Test | [AA_METHOD] | [AA_CRITERIA] | [AA_RESULT] | [AA_ACTION] |
| Instrumentation | [INST_METHOD] | [INST_CRITERIA] | [INST_RESULT] | [INST_ACTION] |
| Covariate Balance | [COV_METHOD] | [COV_CRITERIA] | [COV_RESULT] | [COV_ACTION] |
| Sample Ratio | [SRM_METHOD] | [SRM_CRITERIA] | [SRM_RESULT] | [SRM_ACTION] |
| Metric Logging | [LOG_METHOD] | [LOG_CRITERIA] | [LOG_RESULT] | [LOG_ACTION] |

### 8. Results Analysis

**Summary Statistics:**
| **Metric** | **Control** | **Treatment** | **Absolute Diff** | **Relative Diff** | **95% CI** | **P-Value** | **Significant** |
|-----------|------------|--------------|------------------|------------------|-----------|------------|-----------------|
| [PRIMARY_METRIC] | [CTRL_PRIMARY] | [TREAT_PRIMARY] | [ABS_PRIMARY] | [REL_PRIMARY]% | [CI_PRIMARY] | [P_PRIMARY] | [SIG_PRIMARY] |
| [METRIC_1] | [CTRL_M1] | [TREAT_M1] | [ABS_M1] | [REL_M1]% | [CI_M1] | [P_M1] | [SIG_M1] |
| [METRIC_2] | [CTRL_M2] | [TREAT_M2] | [ABS_M2] | [REL_M2]% | [CI_M2] | [P_M2] | [SIG_M2] |
| [METRIC_3] | [CTRL_M3] | [TREAT_M3] | [ABS_M3] | [REL_M3]% | [CI_M3] | [P_M3] | [SIG_M3] |

**Segment Analysis:**
| **Segment** | **N (Control)** | **N (Treatment)** | **Control Rate** | **Treatment Rate** | **Lift** | **P-Value** |
|------------|----------------|------------------|-----------------|-------------------|---------|------------|
| [SEG_1] | [N_CTRL_1] | [N_TREAT_1] | [RATE_CTRL_1] | [RATE_TREAT_1] | [LIFT_1]% | [P_1] |
| [SEG_2] | [N_CTRL_2] | [N_TREAT_2] | [RATE_CTRL_2] | [RATE_TREAT_2] | [LIFT_2]% | [P_2] |
| [SEG_3] | [N_CTRL_3] | [N_TREAT_3] | [RATE_CTRL_3] | [RATE_TREAT_3] | [LIFT_3]% | [P_3] |
| [SEG_4] | [N_CTRL_4] | [N_TREAT_4] | [RATE_CTRL_4] | [RATE_TREAT_4] | [LIFT_4]% | [P_4] |

### 9. Causal Inference Extensions

**Beyond A/B Testing:**
```
Difference-in-Differences:
- Use Case: [DID_USECASE]
- Parallel Trends: [PARALLEL_TRENDS]
- Pre-Period: [PRE_PERIOD]
- Post-Period: [POST_PERIOD]
- Estimated Effect: [DID_EFFECT]

Regression Discontinuity:
- Running Variable: [RUNNING_VAR]
- Cutoff: [CUTOFF]
- Bandwidth: [BANDWIDTH]
- Local Effect: [RD_EFFECT]

Instrumental Variables:
- Instrument: [INSTRUMENT]
- Relevance: [RELEVANCE]
- Exclusion: [EXCLUSION]
- IV Estimate: [IV_ESTIMATE]

Propensity Score Matching:
- Covariates: [PS_COVARIATES]
- Matching Method: [MATCHING_METHOD]
- Balance Check: [BALANCE_CHECK]
- ATT Estimate: [ATT_ESTIMATE]

Synthetic Control:
- Donor Pool: [DONOR_POOL]
- Pre-Treatment Fit: [PRETREAT_FIT]
- Synthetic Unit: [SYNTHETIC_UNIT]
- Effect Estimate: [SC_EFFECT]
```

### 10. Decision Framework

**Experiment Outcome:**
```
Decision Matrix:
- Statistical Significance: [STAT_SIG] (Yes/No)
- Practical Significance: [PRAC_SIG] (Yes/No)
- Guardrails Passed: [GUARDRAILS] (Yes/No)
- Segment Consistency: [SEGMENT_CONSIST] (Yes/No)

Recommendation:
- Decision: [DECISION] (Ship, Iterate, Kill)
- Confidence: [DECISION_CONF]
- Rationale: [DECISION_RATIONALE]
- Next Steps: [NEXT_STEPS]

Rollout Plan:
- Rollout Strategy: [ROLLOUT_STRATEGY]
- Ramp Schedule: [RAMP_SCHEDULE]
- Monitoring: [ROLLOUT_MONITORING]
- Rollback Criteria: [ROLLBACK_CRITERIA]

Documentation:
- Experiment Report: [REPORT_LINK]
- Code/Config: [CODE_LINK]
- Data: [DATA_LINK]
- Learnings: [LEARNINGS]
```

### 11. Common Pitfalls & Mitigations

| **Pitfall** | **Description** | **Detection** | **Mitigation** | **Prevention** |
|------------|-----------------|--------------|---------------|---------------|
| Peeking | [PEEK_DESC] | [PEEK_DETECT] | [PEEK_MITIGATE] | [PEEK_PREVENT] |
| SRM | [SRM_DESC] | [SRM_DETECT] | [SRM_MITIGATE] | [SRM_PREVENT] |
| Novelty Effect | [NOV_DESC] | [NOV_DETECT] | [NOV_MITIGATE] | [NOV_PREVENT] |
| Interference | [INT_DESC] | [INT_DETECT] | [INT_MITIGATE] | [INT_PREVENT] |
| Selection Bias | [SEL_DESC] | [SEL_DETECT] | [SEL_MITIGATE] | [SEL_PREVENT] |
| Simpson's Paradox | [SIMP_DESC] | [SIMP_DETECT] | [SIMP_MITIGATE] | [SIMP_PREVENT] |

### 12. Experimentation Maturity

**Organizational Capabilities:**
```
Platform:
- Experiment Platform: [PLATFORM]
- Randomization Engine: [RAND_ENGINE]
- Metric Pipeline: [METRIC_PIPELINE]
- Analysis Tools: [ANALYSIS_TOOLS]
- Automation Level: [AUTOMATION]

Process:
- Experiment Review: [REVIEW_PROCESS]
- Launch Checklist: [CHECKLIST]
- Documentation Standards: [DOC_STANDARDS]
- Knowledge Repository: [KNOWLEDGE_REPO]

Culture:
- Experiment Velocity: [VELOCITY] experiments/quarter
- Win Rate: [WIN_RATE]%
- Decision Time: [DECISION_TIME]
- Learning Culture: [LEARNING_CULTURE]
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[EXPERIMENT_NAME]` | Name of experiment | "Checkout Flow Redesign", "Homepage Hero Test" |
| `[HYPOTHESIS]` | Clear hypothesis statement | "Adding trust badges will increase conversion by 3%" |
| `[PRIMARY_METRIC]` | Main success metric | "Conversion rate", "Revenue per user", "Engagement time" |
| `[BASELINE_RATE]` | Current metric value | "2.5%", "4.0%", "$12.50" |
| `[MDE]` | Minimum detectable effect | "5%", "10%", "3%" |
| `[ALPHA]` | Significance level | "0.05", "0.01", "0.10" |
| `[POWER]` | Statistical power | "0.80", "0.90", "0.95" |
| `[DURATION_DAYS]` | Experiment length | "14", "21", "28" |
| `[SAMPLE_PER_VARIANT]` | Users per variant | "10,000", "50,000", "100,000" |
| `[CORRECTION_METHOD]` | Multiple testing correction | "Bonferroni", "Holm-Bonferroni", "Benjamini-Hochberg" |

## Usage Examples

### Example 1: E-commerce Checkout Optimization
```
Experiment: Simplified checkout flow
Hypothesis: Reducing steps from 5 to 3 increases conversion
Primary Metric: Checkout completion rate
Baseline: 65% completion
MDE: 3% relative lift
Sample Size: 50,000 per variant
Duration: 14 days
Result: +4.2% lift (p=0.003), shipped
```

### Example 2: Feature Rollout Test
```
Experiment: New recommendation algorithm
Hypothesis: ML-based recs increase engagement
Primary Metric: Items viewed per session
Guardrails: Page load time, error rate
Segments: New vs returning users
A/A Validation: 7-day pre-test
Sequential Testing: 3 interim analyses
Result: +8% engagement, no guardrail violations
```

### Example 3: Pricing Experiment
```
Experiment: Dynamic pricing test
Hypothesis: Personalized pricing increases revenue
Primary Metric: Revenue per visitor
Secondary: Conversion rate, average order value
Ethical Review: Fairness assessment completed
Sample: 100,000 users (stratified by segment)
Duration: 21 days (full business cycle)
Result: +12% revenue, fairness metrics stable
```

## Best Practices

1. **Pre-register hypotheses** - Define success criteria before looking at data
2. **Calculate sample size upfront** - Don't stop early based on results
3. **Run A/A tests** - Validate instrumentation before every major experiment
4. **Check for SRM** - Sample ratio mismatch indicates implementation bugs
5. **Use guardrail metrics** - Protect core business metrics from degradation
6. **Account for multiple comparisons** - Adjust for testing multiple hypotheses
7. **Consider practical significance** - Statistical significance ≠ business impact
8. **Document everything** - Future you will thank present you
9. **Share learnings widely** - Failed experiments teach as much as successes
10. **Build experimentation culture** - Make data-driven decisions the norm

## Related Resources

- **[Dashboard Design Patterns](../dashboard-design-patterns.md)** - Visualize experiment results
- **[Predictive Modeling Framework](../predictive-modeling-framework.md)** - ML for experiment analysis
- **[Time Series Analysis](time-series-analysis.md)** - Temporal effects in experiments

## Customization Options

### 1. Experiment Type
- A/B Test (two variants)
- A/B/n Test (multiple variants)
- Multivariate Test (MVT)
- Bandit Optimization
- Quasi-experiment

### 2. Analysis Approach
- Frequentist
- Bayesian
- Sequential
- Causal Inference

### 3. Traffic Level
- Low traffic (< 10K/day)
- Medium traffic (10K-100K/day)
- High traffic (100K-1M/day)
- Very high traffic (> 1M/day)

### 4. Risk Level
- Low risk (UI changes)
- Medium risk (feature changes)
- High risk (pricing, core flows)
- Critical (revenue-impacting)
```
