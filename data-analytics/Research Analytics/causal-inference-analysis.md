---
title: Causal Inference Analysis Template
category: data-analytics/Research Analytics
tags: ['causal-inference', 'econometrics', 'statistics', 'research']
use_cases:
  - Perform causal inference using instrumental variables, regression discontinuity, synthetic controls, and advanced econometric methods.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Causal Inference Analysis Template

## Purpose
Perform causal inference using instrumental variables, regression discontinuity, synthetic controls, and advanced econometric methods.

## Quick Start

### For Researchers

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific perform needs
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine as needed

**Common Use Cases:**
- Perform causal inference using instrumental variables, regression discontinuity, synthetic controls, and advanced econometric methods.
- Project-specific implementations
- Research and analysis workflows



## Template

---
title: Experimental Design and Testing Template
category: data-analytics/Research Analytics
tags: [automation, data-analytics, data-science, design, machine-learning, research, security, template]
use_cases:
  - Creating design, implement, and analyze controlled experiments including a/b testing, randomized controlled trials, and causal inference studies to establish causal relationships and measure treatment effects with statistical rigor.

  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---


## Purpose
Design, implement, and analyze controlled experiments including A/B testing, randomized controlled trials, and causal inference studies to establish causal relationships and measure treatment effects with statistical rigor.


- Causal question: [CAUSAL_QUESTION]

Advanced Causal Inference Methods:
```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler
from scipy.stats import ttest_ind, chi2_contingency
import pandas as pd
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
            formula = f'[OUTCOME_VAR] ~ [DOSE_VAR] + ' + ' + '.join(covariates)
        else:
            formula = f'[OUTCOME_VAR] ~ [DOSE_VAR]'

        linear_model = ols(formula, data=self.data).fit()

        # Quadratic dose-response
        self.data['dose_squared'] = self.data[dose_var] ** 2
        if covariates:
            quad_formula = f'[OUTCOME_VAR] ~ [DOSE_VAR] + dose_squared + ' + ' + '.join(covariates)
        else:
            quad_formula = f'[OUTCOME_VAR] ~ [DOSE_VAR] + dose_squared'

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

        formula = f'[OUTCOME_VAR] ~ [TREATMENT_VAR] + ' + ' + '.join(covariates)
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

        formula = f'[TREATMENT_VAR] ~ [INSTRUMENT_VAR]'
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

        formula = f'[OUTCOME_VAR] ~ [TREATMENT_VAR] * C([SUBGROUP_VAR])'
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


   - Complier average causal effect

6. **Causal Inference**

   - Causal identification strategy

   - Instrumental variable analysis (if applicable)

   - Counterfactual reasoning

### Research Design Variables
- [RESEARCH_OBJECTIVE] - Primary research objective
- [PRIMARY_HYPOTHESIS] - Main hypothesis being tested
- [SECONDARY_HYPOTHESES] - Additional hypotheses
- [RESEARCH_QUESTION] - Core research question
- [CAUSAL_QUESTION] - Specific causal question
- [TARGET_POPULATION] - Population of interest
- [EXPERIMENTAL_CONTEXT] - Context/setting of experiment
- [STUDY_DURATION] - Duration of the study
- [BUDGET_LIMITATIONS] - Budget constraints


### Causal Inference Variables
- [IDENTIFICATION_STRATEGY] - Causal identification strategy
- [INSTRUMENTAL_VARIABLE] - Instrumental variable (if applicable)
- [MEDIATOR_VARIABLES] - Variables that mediate the effect
- [MODERATOR_VARIABLES] - Variables that moderate the effect
- [CONFOUNDING_VARIABLES] - Potential confounding variables
- [ASSIGNMENT_MECHANISM] - Treatment assignment mechanism
- [SELECTION_BIAS_CONTROLS] - Controls for selection bias


## Customization Options

1. **Experimental Design Type**
   - Randomized controlled trials
   - A/B testing and digital experiments
   - Factorial designs
   - Crossover designs
   - Cluster randomized trials
   - Quasi-experimental designs

2. **Analysis Approach**
   - Intention-to-treat analysis
   - Per-protocol analysis
   - Instrumental variable methods
   - Causal mediation analysis
   - Bayesian experimental design

3. **Application Domain**
   - Clinical trials and medical research
   - Digital product testing
   - Educational interventions
   - Marketing experiments
   - Policy evaluation studies

4. **Complexity Level**
   - Simple two-group comparisons
   - Multi-arm trials
   - Factorial experiments
   - Adaptive designs
   - Platform trials

5. **Output Focus**
   - Regulatory submission format
   - Academic publication
   - Business decision support
   - Policy recommendation
   - Technical implementation guide

## Variables

[The template includes 400+ comprehensive variables covering all aspects of experimental design and analysis...]

## Best Practices

1. **Focus**: Concentrate on the specific aspect covered by this template
2. **Integration**: Combine with related templates for comprehensive solutions
3. **Iteration**: Start simple and refine based on results
4. **Documentation**: Track your parameters and customizations

## Tips for Success

- Begin with the Quick Start section
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This focused template is part of a comprehensive collection designed for improved usability.
