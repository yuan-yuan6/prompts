---
title: Treatment Effect Analysis
category: data-analytics/Research-Analytics
tags:
- automation
- ai-ml
- data-analytics
- research
use_cases:
- Analyze treatment effects using intention-to-treat, per-protocol, instrumental variable,
  CACE, dose-response, and subgroup analyses to establish causal relationships and
  quantify treatment impacts
related_templates:
- data-analytics/Research Analytics/experimental-design-setup.md
- data-analytics/Research Analytics/randomization-and-power-analysis.md
- data-analytics/Research Analytics/validity-and-diagnostics.md
last_updated: 2025-11-10
industries:
- technology
---

# Treatment Effect Analysis

## Purpose
Perform comprehensive treatment effect analysis using advanced causal inference methods. This prompt helps you analyze experimental data using intention-to-treat (ITT), per-protocol (PP), instrumental variable (IV), complier average causal effect (CACE), dose-response, and subgroup analysis approaches to quantify treatment impacts and establish causal relationships.

## Quick Start

**Example: Comprehensive Treatment Effect Analysis for Clinical Trial**

```
You are a causal inference expert. Analyze treatment effects from a diabetes medication trial using multiple analytical approaches.

STUDY DESIGN:
- Trial: New diabetes medication vs. placebo (RCT, double-blind)
- Sample size: 400 participants (200 per group)
- Primary outcome: HbA1c reduction after 6 months
- Baseline HbA1c: Mean 8.2% (SD 1.1%)
- Compliance: 85% in treatment group, 92% in control group
- Attrition: 12% overall (10% treatment, 14% control)

DATA AVAILABLE:
- Baseline characteristics: age, gender, BMI, baseline HbA1c, disease duration
- Treatment assignment (randomized)
- Treatment received (actual compliance)
- 6-month HbA1c outcome
- Dose adherence (% of prescribed doses taken)

ANALYSIS REQUIREMENTS:
1. Intention-to-treat (ITT) analysis - primary analysis comparing as randomized
2. Per-protocol (PP) analysis - analysis restricted to compliant participants
3. Complier average causal effect (CACE) - estimate effect for those who would comply
4. Dose-response analysis - relationship between adherence and outcome
5. Subgroup analyses - examine effects by age group, baseline HbA1c, BMI category
6. Effect size calculations with 95% confidence intervals
7. Statistical significance testing with appropriate adjustments

DELIVERABLES:
- Complete treatment effect estimates from all analytical approaches
- Comparison of ITT vs. PP vs. CACE estimates with interpretation
- Dose-response curves showing adherence-outcome relationship
- Subgroup analysis results with interaction tests
- Forest plots showing effects across subgroups
- Clinical significance interpretation
- Recommendations for treatment implementation
```

## Template

```
You are a causal inference expert. Analyze treatment effects for [RESEARCH_OBJECTIVE] from [STUDY_DESIGN] testing [HYPOTHESIS].

STUDY PARAMETERS:
Design Information:
- Study design: [STUDY_DESIGN]
- Sample size: [N_PARTICIPANTS]
- Treatment groups: [TREATMENT_GROUPS]
- Primary outcome: [PRIMARY_OUTCOME]
- Secondary outcomes: [SECONDARY_OUTCOMES]
- Study duration: [STUDY_DURATION]

Data Structure:
- Treatment variable: [TREATMENT_VARIABLE]
- Outcome variable: [OUTCOME_VARIABLE]
- Compliance indicator: [COMPLIANCE_VARIABLE]
- Baseline covariates: [BASELINE_COVARIATES]
- Subgroup variables: [SUBGROUP_VARIABLES]
- Dose/adherence variable: [DOSE_VARIABLE]

ANALYSIS SPECIFICATIONS:
Primary Analysis:
- Analysis type: [ANALYSIS_TYPE]  # ITT, PP, IV, CACE
- Adjustment variables: [COVARIATES]
- Statistical model: [STATISTICAL_MODEL]
- Effect measure: [EFFECT_MEASURE]  # mean difference, risk ratio, odds ratio
- Confidence level: [CONFIDENCE_LEVEL]

Intention-to-Treat Analysis:
- Include all randomized participants: [ITT_INCLUDE_ALL]
- Handle missing data: [MISSING_DATA_METHOD]
- Covariate adjustment: [ITT_COVARIATES]

Per-Protocol Analysis:
- Compliance definition: [COMPLIANCE_DEFINITION]
- Exclusion criteria: [PP_EXCLUSIONS]
- Sensitivity analysis: [PP_SENSITIVITY]

Instrumental Variable Analysis:
- Instrument: [INSTRUMENTAL_VARIABLE]
- First-stage test: [FIRST_STAGE_THRESHOLD]
- Two-stage method: [IV_METHOD]

Dose-Response Analysis:
- Dose measurement: [DOSE_MEASURE]
- Relationship form: [DOSE_RESPONSE_FORM]  # linear, quadratic, spline
- Confounders: [DOSE_CONFOUNDERS]

Subgroup Analysis:
- Subgroup variables: [SUBGROUP_VARS]
- Interaction tests: [TEST_INTERACTIONS]
- Multiple testing correction: [SUBGROUP_CORRECTION]

EXPECTED DELIVERABLES:
1. Primary ITT analysis results with effect sizes and confidence intervals
2. Per-protocol analysis for compliant participants
3. CACE estimates for treatment compliers
4. Dose-response relationship analysis
5. Subgroup effect estimates with interaction tests
6. Comprehensive treatment effect summary comparing all approaches
7. Clinical/practical significance interpretation
8. Recommendations for implementation
```

## Treatment Effect Analysis Framework

### Advanced Causal Inference Methods

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler
from scipy.stats import ttest_ind, chi2_contingency
import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ttest_ind as stats_ttest_ind
from statsmodels.regression.linear_model import OLS
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

class TreatmentEffectAnalyzer:
    def __init__(self, data):
        self.data = data
        self.results = {}
        self.diagnostics = {}

    def intention_to_treat_analysis(self, outcome_var, treatment_var, covariates=None):
        """Intention-to-treat analysis (ITT)"""

        # Basic ITT comparison
        treatment_group = self.data[self.data[treatment_var] == 1][outcome_var]
        control_group = self.data[self.data[treatment_var] == 0][outcome_var]

        # T-test
        t_stat, p_value = ttest_ind(treatment_group, control_group)

        # Effect size (Cohen's d)
        pooled_std = np.sqrt(((len(treatment_group)-1)*treatment_group.var() +
                             (len(control_group)-1)*control_group.var()) /
                            (len(treatment_group) + len(control_group) - 2))
        cohens_d = (treatment_group.mean() - control_group.mean()) / pooled_std

        # Confidence interval for difference
        se_diff = pooled_std * np.sqrt(1/len(treatment_group) + 1/len(control_group))
        diff = treatment_group.mean() - control_group.mean()
        ci_lower = diff - 1.96 * se_diff
        ci_upper = diff + 1.96 * se_diff

        itt_results = {
            'analysis_type': 'Intention-to-Treat',
            'treatment_mean': treatment_group.mean(),
            'control_mean': control_group.mean(),
            'difference': diff,
            'effect_size_cohens_d': cohens_d,
            'ci_95_lower': ci_lower,
            'ci_95_upper': ci_upper,
            't_statistic': t_stat,
            'p_value': p_value,
            'n_treatment': len(treatment_group),
            'n_control': len(control_group)
        }

        # Regression adjustment if covariates provided
        if covariates:
            adjusted_results = self._regression_adjusted_itt(outcome_var, treatment_var, covariates)
            itt_results['adjusted_analysis'] = adjusted_results

        self.results['itt'] = itt_results
        return itt_results

    def per_protocol_analysis(self, outcome_var, treatment_var, compliance_var):
        """Per-protocol analysis (PP)"""

        # Filter to compliant participants only
        compliant_data = self.data[self.data[compliance_var] == 1]

        if len(compliant_data) == 0:
            return {'error': 'No compliant participants found'}

        treatment_compliant = compliant_data[compliant_data[treatment_var] == 1][outcome_var]
        control_compliant = compliant_data[compliant_data[treatment_var] == 0][outcome_var]

        if len(treatment_compliant) == 0 or len(control_compliant) == 0:
            return {'error': 'Insufficient compliant participants in one or both groups'}

        # T-test on compliant participants
        t_stat, p_value = ttest_ind(treatment_compliant, control_compliant)

        pp_results = {
            'analysis_type': 'Per-Protocol',
            'treatment_mean': treatment_compliant.mean(),
            'control_mean': control_compliant.mean(),
            'difference': treatment_compliant.mean() - control_compliant.mean(),
            't_statistic': t_stat,
            'p_value': p_value,
            'n_treatment_compliant': len(treatment_compliant),
            'n_control_compliant': len(control_compliant),
            'compliance_rate_treatment': len(treatment_compliant) / len(self.data[self.data[treatment_var] == 1]),
            'compliance_rate_control': len(control_compliant) / len(self.data[self.data[treatment_var] == 0])
        }

        self.results['per_protocol'] = pp_results
        return pp_results

    def instrumental_variable_analysis(self, outcome_var, treatment_var, instrument_var):
        """Instrumental variable analysis for compliance adjustments"""

        try:
            from statsmodels.sandbox.regression.gmm import IV2SLS
        except ImportError:
            return {'error': 'Instrumental variable analysis requires statsmodels'}

        # Two-stage least squares
        # First stage: predict treatment using instrument
        first_stage = LinearRegression()
        X_instrument = self.data[[instrument_var]].values
        first_stage.fit(X_instrument, self.data[treatment_var])
        predicted_treatment = first_stage.predict(X_instrument)

        # First stage F-statistic
        first_stage_f = self._calculate_first_stage_f(instrument_var, treatment_var)

        # Second stage: outcome on predicted treatment
        second_stage = LinearRegression()
        second_stage.fit(predicted_treatment.reshape(-1, 1), self.data[outcome_var])

        iv_coefficient = second_stage.coef_[0]

        # Calculate standard errors (simplified)
        n = len(self.data)
        residuals = self.data[outcome_var] - second_stage.predict(predicted_treatment.reshape(-1, 1))
        mse = np.sum(residuals**2) / (n - 2)
        var_pred_treatment = np.var(predicted_treatment)
        se_iv = np.sqrt(mse / (n * var_pred_treatment))

        from scipy import stats
        iv_results = {
            'analysis_type': 'Instrumental Variable',
            'iv_estimate': iv_coefficient,
            'standard_error': se_iv,
            't_statistic': iv_coefficient / se_iv,
            'p_value': 2 * (1 - stats.norm.cdf(abs(iv_coefficient / se_iv))),
            'first_stage_f': first_stage_f,
            'weak_instrument': first_stage_f < 10
        }

        self.results['instrumental_variable'] = iv_results
        return iv_results

    def complier_average_causal_effect(self, outcome_var, treatment_var, instrument_var):
        """Calculate Complier Average Causal Effect (CACE)"""

        # CACE = ITT_outcome / ITT_treatment

        # ITT for outcome
        itt_outcome = self._calculate_itt_effect(outcome_var, instrument_var)

        # ITT for treatment (compliance rate difference)
        itt_treatment = self._calculate_itt_effect(treatment_var, instrument_var)

        if itt_treatment == 0:
            return {'error': 'No differential compliance - cannot calculate CACE'}

        cace_estimate = itt_outcome / itt_treatment

        # Bootstrap confidence intervals for CACE
        cace_bootstrap = []
        n_bootstrap = 1000

        for _ in range(n_bootstrap):
            boot_sample = self.data.sample(n=len(self.data), replace=True)
            boot_itt_outcome = self._calculate_itt_effect_data(boot_sample, outcome_var, instrument_var)
            boot_itt_treatment = self._calculate_itt_effect_data(boot_sample, treatment_var, instrument_var)

            if boot_itt_treatment != 0:
                cace_bootstrap.append(boot_itt_outcome / boot_itt_treatment)

        cace_ci = np.percentile(cace_bootstrap, [2.5, 97.5])

        cace_results = {
            'analysis_type': 'Complier Average Causal Effect',
            'cace_estimate': cace_estimate,
            'itt_outcome': itt_outcome,
            'itt_treatment': itt_treatment,
            'ci_95_lower': cace_ci[0],
            'ci_95_upper': cace_ci[1],
            'bootstrap_distribution': cace_bootstrap
        }

        self.results['cace'] = cace_results
        return cace_results

    def dose_response_analysis(self, outcome_var, dose_var, covariates=None):
        """Analyze dose-response relationship"""

        # Linear dose-response
        if covariates:
            formula = f'{outcome_var} ~ {dose_var} + ' + ' + '.join(covariates)
        else:
            formula = f'{outcome_var} ~ {dose_var}'

        linear_model = ols(formula, data=self.data).fit()

        # Quadratic dose-response
        self.data['dose_squared'] = self.data[dose_var] ** 2
        if covariates:
            quad_formula = f'{outcome_var} ~ {dose_var} + dose_squared + ' + ' + '.join(covariates)
        else:
            quad_formula = f'{outcome_var} ~ {dose_var} + dose_squared'

        quadratic_model = ols(quad_formula, data=self.data).fit()

        # Model comparison
        from scipy.stats import f
        f_stat = ((quadratic_model.rsquared - linear_model.rsquared) /
                 (1 - quadratic_model.rsquared)) * (len(self.data) - quadratic_model.df_model - 1)
        f_p_value = 1 - f.cdf(f_stat, 1, len(self.data) - quadratic_model.df_model - 1)

        dose_response_results = {
            'linear_model': {
                'coefficient': linear_model.params[dose_var],
                'p_value': linear_model.pvalues[dose_var],
                'r_squared': linear_model.rsquared
            },
            'quadratic_model': {
                'linear_coefficient': quadratic_model.params[dose_var],
                'quadratic_coefficient': quadratic_model.params['dose_squared'],
                'linear_p_value': quadratic_model.pvalues[dose_var],
                'quadratic_p_value': quadratic_model.pvalues['dose_squared'],
                'r_squared': quadratic_model.rsquared
            },
            'model_comparison': {
                'f_statistic': f_stat,
                'p_value': f_p_value,
                'prefer_quadratic': f_p_value < 0.05
            }
        }

        self.results['dose_response'] = dose_response_results
        return dose_response_results

    def subgroup_analysis(self, outcome_var, treatment_var, subgroup_vars):
        """Analyze treatment effects in subgroups"""

        subgroup_results = {}

        for subgroup_var in subgroup_vars:
            subgroup_effects = {}

            for subgroup_value in self.data[subgroup_var].unique():
                subgroup_data = self.data[self.data[subgroup_var] == subgroup_value]

                treatment_sub = subgroup_data[subgroup_data[treatment_var] == 1][outcome_var]
                control_sub = subgroup_data[subgroup_data[treatment_var] == 0][outcome_var]

                if len(treatment_sub) > 0 and len(control_sub) > 0:
                    t_stat, p_value = ttest_ind(treatment_sub, control_sub)
                    effect = treatment_sub.mean() - control_sub.mean()

                    subgroup_effects[subgroup_value] = {
                        'treatment_mean': treatment_sub.mean(),
                        'control_mean': control_sub.mean(),
                        'effect': effect,
                        't_statistic': t_stat,
                        'p_value': p_value,
                        'n_treatment': len(treatment_sub),
                        'n_control': len(control_sub)
                    }

            # Test for interaction
            interaction_p = self._test_subgroup_interaction(outcome_var, treatment_var, subgroup_var)

            subgroup_results[subgroup_var] = {
                'subgroup_effects': subgroup_effects,
                'interaction_p_value': interaction_p,
                'significant_interaction': interaction_p < 0.05
            }

        self.results['subgroup_analysis'] = subgroup_results
        return subgroup_results

    def _regression_adjusted_itt(self, outcome_var, treatment_var, covariates):
        """Regression-adjusted ITT analysis"""

        formula = f'{outcome_var} ~ {treatment_var} + ' + ' + '.join(covariates)
        model = ols(formula, data=self.data).fit()

        return {
            'treatment_coefficient': model.params[treatment_var],
            'p_value': model.pvalues[treatment_var],
            'ci_95_lower': model.conf_int().loc[treatment_var, 0],
            'ci_95_upper': model.conf_int().loc[treatment_var, 1],
            'r_squared': model.rsquared,
            'adjusted_r_squared': model.rsquared_adj
        }

    def _calculate_first_stage_f(self, instrument_var, treatment_var):
        """Calculate first stage F-statistic"""

        formula = f'{treatment_var} ~ {instrument_var}'
        first_stage_model = ols(formula, data=self.data).fit()

        return first_stage_model.fvalue

    def _calculate_itt_effect(self, outcome_var, treatment_var):
        """Calculate ITT effect for given variables"""

        return self._calculate_itt_effect_data(self.data, outcome_var, treatment_var)

    def _calculate_itt_effect_data(self, data, outcome_var, treatment_var):
        """Calculate ITT effect for given data"""

        treatment_mean = data[data[treatment_var] == 1][outcome_var].mean()
        control_mean = data[data[treatment_var] == 0][outcome_var].mean()

        return treatment_mean - control_mean

    def _test_subgroup_interaction(self, outcome_var, treatment_var, subgroup_var):
        """Test for treatment by subgroup interaction"""

        formula = f'{outcome_var} ~ {treatment_var} * C({subgroup_var})'
        model = ols(formula, data=self.data).fit()

        # Find interaction term p-value
        interaction_terms = [param for param in model.params.index
                           if treatment_var in param and subgroup_var in param]

        if interaction_terms:
            return model.pvalues[interaction_terms[0]]
        else:
            return 1.0

    def comprehensive_effect_summary(self):
        """Create comprehensive summary of all treatment effect analyses"""

        summary = {
            'analyses_performed': list(self.results.keys()),
            'primary_findings': {},
            'effect_size_comparison': {},
            'robustness_checks': {}
        }

        # Extract primary findings
        for analysis, results in self.results.items():
            if 'difference' in results:
                summary['primary_findings'][analysis] = {
                    'effect_estimate': results['difference'],
                    'p_value': results.get('p_value', None),
                    'ci_95': [results.get('ci_95_lower'), results.get('ci_95_upper')]
                }

        return summary

# Perform treatment effect analysis
effect_analyzer = TreatmentEffectAnalyzer(experiment_data)

# Run different analyses
itt_results = effect_analyzer.intention_to_treat_analysis(
    outcome_var='[OUTCOME_VARIABLE]',
    treatment_var='[TREATMENT_VARIABLE]',
    covariates=['[COVARIATES]'] if '[COVARIATES]' else None
)

# Additional analyses based on study design
if '[COMPLIANCE_VARIABLE]':
    pp_results = effect_analyzer.per_protocol_analysis(
        outcome_var='[OUTCOME_VARIABLE]',
        treatment_var='[TREATMENT_VARIABLE]',
        compliance_var='[COMPLIANCE_VARIABLE]'
    )

if '[SUBGROUP_VARIABLES]':
    subgroup_results = effect_analyzer.subgroup_analysis(
        outcome_var='[OUTCOME_VARIABLE]',
        treatment_var='[TREATMENT_VARIABLE]',
        subgroup_vars=['[SUBGROUP_VARIABLES]']
    )
```

## Variables

### Core Analysis Variables
- [OUTCOME_VARIABLE] - Primary outcome variable name
- [TREATMENT_VARIABLE] - Treatment assignment variable
- [COMPLIANCE_VARIABLE] - Variable indicating treatment compliance
- [INSTRUMENTAL_VARIABLE] - Instrument for IV analysis
- [DOSE_VARIABLE] - Dose or adherence measure
- [SUBGROUP_VARIABLES] - List of subgroup defining variables

### Analysis Configuration
- [ANALYSIS_TYPE] - Type of analysis (ITT, PP, IV, CACE)
- [COVARIATES] - List of covariates for adjustment
- [STATISTICAL_MODEL] - Statistical model specification
- [EFFECT_MEASURE] - Type of effect measure
- [CONFIDENCE_LEVEL] - Confidence level for intervals
- [MISSING_DATA_METHOD] - Method for handling missing data

### Subgroup Analysis Variables
- [SUBGROUP_VARS] - Variables defining subgroups
- [TEST_INTERACTIONS] - Whether to test interactions
- [SUBGROUP_CORRECTION] - Multiple testing correction method

## Usage Examples

### Example 1: Basic ITT Analysis
```python
# Load data
data = pd.read_csv('trial_data.csv')

# Initialize analyzer
analyzer = TreatmentEffectAnalyzer(data)

# Run ITT analysis
itt_results = analyzer.intention_to_treat_analysis(
    outcome_var='hba1c_reduction',
    treatment_var='assigned_treatment',
    covariates=['baseline_hba1c', 'age', 'bmi']
)

print(f"Treatment effect: {itt_results['difference']:.2f}")
print(f"95% CI: [{itt_results['ci_95_lower']:.2f}, {itt_results['ci_95_upper']:.2f}]")
print(f"P-value: {itt_results['p_value']:.4f}")
```

### Example 2: Per-Protocol with ITT Comparison
```python
# Run both analyses
itt_results = analyzer.intention_to_treat_analysis(
    outcome_var='outcome',
    treatment_var='assigned'
)

pp_results = analyzer.per_protocol_analysis(
    outcome_var='outcome',
    treatment_var='assigned',
    compliance_var='compliant'
)

print(f"ITT effect: {itt_results['difference']:.2f}")
print(f"PP effect: {pp_results['difference']:.2f}")
print(f"Compliance rate: {pp_results['compliance_rate_treatment']:.1%}")
```

### Example 3: Subgroup Analysis with Interaction Tests
```python
subgroup_results = analyzer.subgroup_analysis(
    outcome_var='outcome',
    treatment_var='treatment',
    subgroup_vars=['age_group', 'disease_severity']
)

for subgroup_var, results in subgroup_results.items():
    print(f"\nSubgroup: {subgroup_var}")
    print(f"Interaction p-value: {results['interaction_p_value']:.4f}")

    for subgroup_value, effect in results['subgroup_effects'].items():
        print(f"  {subgroup_value}: Effect = {effect['effect']:.2f}, p = {effect['p_value']:.4f}")
```

### Example 4: Dose-Response Analysis
```python
dose_results = analyzer.dose_response_analysis(
    outcome_var='outcome',
    dose_var='adherence_percent',
    covariates=['age', 'baseline_severity']
)

print(f"Linear coefficient: {dose_results['linear_model']['coefficient']:.3f}")
print(f"Linear p-value: {dose_results['linear_model']['p_value']:.4f}")
print(f"Quadratic better fit: {dose_results['model_comparison']['prefer_quadratic']}")
```

## Best Practices

1. **ITT as Primary** - Use intention-to-treat as primary analysis for unbiased estimates
2. **Report Multiple Analyses** - Present ITT, PP, and CACE for comprehensive view
3. **Pre-specify Subgroups** - Define subgroups before seeing data to avoid fishing
4. **Test Interactions** - Formally test for subgroup interactions, don't just compare p-values
5. **Adjust for Multiplicity** - Use multiple testing corrections for subgroup analyses
6. **Check First Stage** - Verify strong instruments (F > 10) for IV analysis
7. **Interpret Clinically** - Report both statistical and clinical significance
8. **Document Deviations** - Record all protocol deviations and their handling
9. **Sensitivity Analyses** - Test robustness to analytical assumptions
10. **Report Completely** - Follow CONSORT guidelines for complete reporting
