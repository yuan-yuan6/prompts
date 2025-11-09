---
title: DOE Analysis & Statistical Methods
category: data-analytics/Research Analytics
tags: [automation, data-analytics, data-science, research, statistics, template]
use_cases:
  - Analyzing experimental data using ANOVA and regression methods
  - Implementing treatment effect estimation techniques
  - Conducting causal inference analyses including ITT and per-protocol
  - Performing dose-response and subgroup analyses
related_templates:
  - experimental-design-overview.md
  - factorial-designs.md
  - experiment-results-interpretation.md
last_updated: 2025-11-09
---

# DOE Analysis & Statistical Methods

## Purpose
Analyze experimental data using appropriate statistical methods including ANOVA, regression, treatment effect estimation, and causal inference techniques to draw valid conclusions from designed experiments.

## Template

```
You are an experimental data analysis expert. Analyze experiment data for [RESEARCH_OBJECTIVE] using [ANALYSIS_METHOD] to estimate treatment effects on [OUTCOME_VARIABLE], accounting for [COVARIATES] and testing [HYPOTHESES].

ANALYSIS FRAMEWORK:

Study Configuration:
- Outcome variable: [OUTCOME_VARIABLE]
- Treatment variable: [TREATMENT_VARIABLE]
- Covariates: [COVARIATES]
- Analysis population: [ANALYSIS_POPULATION]
- Primary hypothesis: [PRIMARY_HYPOTHESIS]

### Analysis Approaches

1. **Intention-to-Treat (ITT)**: Analyze as randomized
2. **Per-Protocol (PP)**: Analyze compliant participants only
3. **As-Treated**: Analyze based on actual treatment received
4. **Instrumental Variables**: Handle non-compliance
5. **CACE**: Complier Average Causal Effect

IMPLEMENTATION:
```python
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.regression.linear_model import OLS
from sklearn.linear_model import LinearRegression, LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns

class TreatmentEffectAnalyzer:
    """
    Comprehensive treatment effect analysis for experimental data
    """

    def __init__(self, data):
        """
        Initialize analyzer with experimental data

        Parameters:
        -----------
        data : DataFrame
            Experimental data with outcomes, treatments, and covariates
        """
        self.data = data
        self.results = {}
        self.diagnostics = {}

    def intention_to_treat_analysis(self, outcome_var, treatment_var, covariates=None):
        """
        Intention-to-Treat (ITT) Analysis

        Gold standard for RCTs - analyzes participants as randomized
        regardless of compliance or protocol deviations

        Parameters:
        -----------
        outcome_var : str
            Name of outcome variable
        treatment_var : str
            Name of treatment variable (0/1 or control/treatment)
        covariates : list, optional
            Covariates for adjusted analysis

        Returns:
        --------
        dict : ITT analysis results
        """

        # Basic ITT comparison
        treatment_group = self.data[self.data[treatment_var] == 1][outcome_var]
        control_group = self.data[self.data[treatment_var] == 0][outcome_var]

        # T-test
        t_stat, p_value = stats.ttest_ind(treatment_group, control_group)

        # Effect size (Cohen's d)
        pooled_std = np.sqrt(((len(treatment_group)-1)*treatment_group.var() +
                             (len(control_group)-1)*control_group.var()) /
                            (len(treatment_group) + len(control_group) - 2))

        cohens_d = (treatment_group.mean() - control_group.mean()) / pooled_std if pooled_std > 0 else 0

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
            'n_control': len(control_group),
            'statistically_significant': p_value < 0.05
        }

        # Regression adjustment if covariates provided
        if covariates:
            adjusted_results = self._regression_adjusted_itt(outcome_var, treatment_var, covariates)
            itt_results['adjusted_analysis'] = adjusted_results

        self.results['itt'] = itt_results

        self._print_itt_summary(itt_results)

        return itt_results

    def per_protocol_analysis(self, outcome_var, treatment_var, compliance_var):
        """
        Per-Protocol Analysis

        Analyzes only compliant participants
        May introduce selection bias but estimates efficacy under ideal conditions

        Parameters:
        -----------
        outcome_var : str
            Outcome variable
        treatment_var : str
            Treatment variable
        compliance_var : str
            Binary variable indicating compliance (0/1)

        Returns:
        --------
        dict : Per-protocol results
        """

        # Filter to compliant participants only
        compliant_data = self.data[self.data[compliance_var] == 1]

        if len(compliant_data) == 0:
            return {'error': 'No compliant participants found'}

        treatment_compliant = compliant_data[compliant_data[treatment_var] == 1][outcome_var]
        control_compliant = compliant_data[compliant_data[treatment_var] == 0][outcome_var]

        if len(treatment_compliant) == 0 or len(control_compliant) == 0:
            return {'error': 'Insufficient compliant participants in one or both groups'}

        # T-test on compliant participants
        t_stat, p_value = stats.ttest_ind(treatment_compliant, control_compliant)

        # Effect size
        pooled_std = np.sqrt(((len(treatment_compliant)-1)*treatment_compliant.var() +
                             (len(control_compliant)-1)*control_compliant.var()) /
                            (len(treatment_compliant) + len(control_compliant) - 2))

        cohens_d = ((treatment_compliant.mean() - control_compliant.mean()) / pooled_std
                   if pooled_std > 0 else 0)

        pp_results = {
            'analysis_type': 'Per-Protocol',
            'treatment_mean': treatment_compliant.mean(),
            'control_mean': control_compliant.mean(),
            'difference': treatment_compliant.mean() - control_compliant.mean(),
            'effect_size_cohens_d': cohens_d,
            't_statistic': t_stat,
            'p_value': p_value,
            'n_treatment_compliant': len(treatment_compliant),
            'n_control_compliant': len(control_compliant),
            'compliance_rate_treatment': len(treatment_compliant) / len(self.data[self.data[treatment_var] == 1]),
            'compliance_rate_control': len(control_compliant) / len(self.data[self.data[treatment_var] == 0])
        }

        self.results['per_protocol'] = pp_results

        print(f"\nPer-Protocol Analysis:")
        print(f"  Treatment mean (compliant): {pp_results['treatment_mean']:.4f}")
        print(f"  Control mean (compliant): {pp_results['control_mean']:.4f}")
        print(f"  Difference: {pp_results['difference']:.4f}")
        print(f"  p-value: {pp_results['p_value']:.4f}")
        print(f"  Compliance rate (treatment): {pp_results['compliance_rate_treatment']:.2%}")
        print(f"  Compliance rate (control): {pp_results['compliance_rate_control']:.2%}")

        return pp_results

    def complier_average_causal_effect(self, outcome_var, treatment_var, instrument_var):
        """
        Calculate Complier Average Causal Effect (CACE)

        Estimates treatment effect for compliers using instrumental variables
        CACE = ITT_outcome / ITT_treatment

        Parameters:
        -----------
        outcome_var : str
            Outcome variable
        treatment_var : str
            Treatment variable (actual treatment received)
        instrument_var : str
            Instrument (randomization assignment)

        Returns:
        --------
        dict : CACE results
        """

        # ITT for outcome
        itt_outcome = self._calculate_itt_effect(outcome_var, instrument_var)

        # ITT for treatment (compliance rate difference)
        itt_treatment = self._calculate_itt_effect(treatment_var, instrument_var)

        if abs(itt_treatment) < 0.001:
            return {'error': 'No differential compliance - cannot calculate CACE'}

        cace_estimate = itt_outcome / itt_treatment

        # Bootstrap confidence intervals for CACE
        cace_bootstrap = []
        n_bootstrap = 1000

        for _ in range(n_bootstrap):
            boot_sample = self.data.sample(n=len(self.data), replace=True)
            boot_itt_outcome = self._calculate_itt_effect_data(boot_sample, outcome_var, instrument_var)
            boot_itt_treatment = self._calculate_itt_effect_data(boot_sample, treatment_var, instrument_var)

            if abs(boot_itt_treatment) >= 0.001:
                cace_bootstrap.append(boot_itt_outcome / boot_itt_treatment)

        cace_ci = np.percentile(cace_bootstrap, [2.5, 97.5]) if cace_bootstrap else [np.nan, np.nan]

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

        print(f"\nCACE Analysis:")
        print(f"  CACE Estimate: {cace_estimate:.4f}")
        print(f"  95% CI: [{cace_ci[0]:.4f}, {cace_ci[1]:.4f}]")
        print(f"  ITT (outcome): {itt_outcome:.4f}")
        print(f"  ITT (treatment uptake): {itt_treatment:.4f}")

        return cace_results

    def dose_response_analysis(self, outcome_var, dose_var, covariates=None):
        """
        Analyze dose-response relationship

        Tests linear and quadratic relationships between dose and outcome

        Parameters:
        -----------
        outcome_var : str
            Outcome variable
        dose_var : str
            Continuous dose/treatment intensity variable
        covariates : list, optional
            Covariates to adjust for

        Returns:
        --------
        dict : Dose-response analysis results
        """

        # Linear dose-response
        if covariates:
            formula = f"{outcome_var} ~ {dose_var} + " + ' + '.join(covariates)
        else:
            formula = f"{outcome_var} ~ {dose_var}"

        linear_model = ols(formula, data=self.data).fit()

        # Quadratic dose-response
        self.data['dose_squared'] = self.data[dose_var] ** 2
        if covariates:
            quad_formula = f"{outcome_var} ~ {dose_var} + dose_squared + " + ' + '.join(covariates)
        else:
            quad_formula = f"{outcome_var} ~ {dose_var} + dose_squared"

        quadratic_model = ols(quad_formula, data=self.data).fit()

        # Model comparison
        f_stat = ((quadratic_model.rsquared - linear_model.rsquared) /
                 (1 - quadratic_model.rsquared)) * (len(self.data) - quadratic_model.df_model - 1)
        f_p_value = 1 - stats.f.cdf(f_stat, 1, len(self.data) - quadratic_model.df_model - 1)

        dose_response_results = {
            'linear_model': {
                'coefficient': linear_model.params[dose_var],
                'p_value': linear_model.pvalues[dose_var],
                'r_squared': linear_model.rsquared,
                'interpretation': 'Unit increase in dose associated with {:.4f} change in outcome'.format(
                    linear_model.params[dose_var])
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

        print(f"\nDose-Response Analysis:")
        print(f"  Linear coefficient: {dose_response_results['linear_model']['coefficient']:.4f}")
        print(f"  Linear p-value: {dose_response_results['linear_model']['p_value']:.4f}")
        print(f"  Quadratic preferred: {dose_response_results['model_comparison']['prefer_quadratic']}")

        return dose_response_results

    def subgroup_analysis(self, outcome_var, treatment_var, subgroup_vars):
        """
        Analyze treatment effects in subgroups

        Tests for heterogeneous treatment effects across subgroups

        Parameters:
        -----------
        outcome_var : str
            Outcome variable
        treatment_var : str
            Treatment variable
        subgroup_vars : list
            Variables defining subgroups

        Returns:
        --------
        dict : Subgroup analysis results
        """

        subgroup_results = {}

        for subgroup_var in subgroup_vars:
            subgroup_effects = {}

            for subgroup_value in self.data[subgroup_var].unique():
                subgroup_data = self.data[self.data[subgroup_var] == subgroup_value]

                treatment_sub = subgroup_data[subgroup_data[treatment_var] == 1][outcome_var]
                control_sub = subgroup_data[subgroup_data[treatment_var] == 0][outcome_var]

                if len(treatment_sub) > 0 and len(control_sub) > 0:
                    t_stat, p_value = stats.ttest_ind(treatment_sub, control_sub)
                    effect = treatment_sub.mean() - control_sub.mean()

                    # Calculate standard error for confidence interval
                    pooled_std = np.sqrt(((len(treatment_sub)-1)*treatment_sub.var() +
                                         (len(control_sub)-1)*control_sub.var()) /
                                        (len(treatment_sub) + len(control_sub) - 2))
                    se = pooled_std * np.sqrt(1/len(treatment_sub) + 1/len(control_sub))

                    subgroup_effects[str(subgroup_value)] = {
                        'treatment_mean': treatment_sub.mean(),
                        'control_mean': control_sub.mean(),
                        'effect': effect,
                        'se': se,
                        'ci_95_lower': effect - 1.96 * se,
                        'ci_95_upper': effect + 1.96 * se,
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
                'significant_interaction': interaction_p < 0.05,
                'interpretation': ('Treatment effect varies by {}').format(subgroup_var) if interaction_p < 0.05
                                 else ('Treatment effect does not vary by {}').format(subgroup_var)
            }

        self.results['subgroup_analysis'] = subgroup_results

        self._print_subgroup_summary(subgroup_results)

        return subgroup_results

    def anova_analysis(self, outcome_var, factor_vars, interaction_terms=True):
        """
        ANOVA analysis for factorial designs

        Parameters:
        -----------
        outcome_var : str
            Outcome variable
        factor_vars : list
            List of factor variables
        interaction_terms : bool
            Whether to include interaction terms

        Returns:
        --------
        dict : ANOVA results
        """

        # Build formula
        if interaction_terms and len(factor_vars) > 1:
            formula = f"{outcome_var} ~ {' * '.join(factor_vars)}"
        else:
            formula = f"{outcome_var} ~ {' + '.join(factor_vars)}"

        # Fit model
        model = ols(formula, data=self.data).fit()

        # ANOVA table
        anova_table = anova_lm(model)

        # Identify significant effects
        significant_effects = []
        for effect in anova_table.index:
            if effect != 'Residual' and anova_table.loc[effect, 'PR(>F)'] < 0.05:
                significant_effects.append(effect)

        anova_results = {
            'model': model,
            'anova_table': anova_table,
            'r_squared': model.rsquared,
            'adj_r_squared': model.rsquared_adj,
            'significant_effects': significant_effects,
            'model_summary': model.summary()
        }

        self.results['anova'] = anova_results

        print(f"\nANOVA Analysis:")
        print(anova_table)
        print(f"\nSignificant effects (α = 0.05): {', '.join(significant_effects) if significant_effects else 'None'}")
        print(f"R-squared: {model.rsquared:.4f}")

        return anova_results

    def _regression_adjusted_itt(self, outcome_var, treatment_var, covariates):
        """Regression-adjusted ITT analysis"""

        formula = f"{outcome_var} ~ {treatment_var} + " + ' + '.join(covariates)
        model = ols(formula, data=self.data).fit()

        return {
            'treatment_coefficient': model.params[treatment_var],
            'p_value': model.pvalues[treatment_var],
            'ci_95_lower': model.conf_int().loc[treatment_var, 0],
            'ci_95_upper': model.conf_int().loc[treatment_var, 1],
            'r_squared': model.rsquared,
            'adjusted_r_squared': model.rsquared_adj,
            'covariates_controlled': covariates
        }

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

        formula = f"{outcome_var} ~ {treatment_var} * C({subgroup_var})"
        model = ols(formula, data=self.data).fit()

        # Find interaction term p-value
        interaction_terms = [param for param in model.params.index
                           if treatment_var in param and subgroup_var in param]

        if interaction_terms:
            return model.pvalues[interaction_terms[0]]
        else:
            return 1.0

    def _print_itt_summary(self, results):
        """Print ITT analysis summary"""

        print("\n" + "="*60)
        print("INTENTION-TO-TREAT ANALYSIS")
        print("="*60)
        print(f"\nTreatment Group Mean: {results['treatment_mean']:.4f} (N={results['n_treatment']})")
        print(f"Control Group Mean: {results['control_mean']:.4f} (N={results['n_control']})")
        print(f"\nTreatment Effect: {results['difference']:.4f}")
        print(f"95% CI: [{results['ci_95_lower']:.4f}, {results['ci_95_upper']:.4f}]")
        print(f"Cohen's d: {results['effect_size_cohens_d']:.4f}")
        print(f"p-value: {results['p_value']:.4f}")
        print(f"Statistically significant: {'Yes' if results['statistically_significant'] else 'No'}")

    def _print_subgroup_summary(self, results):
        """Print subgroup analysis summary"""

        print("\n" + "="*60)
        print("SUBGROUP ANALYSIS")
        print("="*60)

        for subgroup_var, subgroup_data in results.items():
            print(f"\nSubgroup: {subgroup_var}")
            print(f"Interaction p-value: {subgroup_data['interaction_p_value']:.4f}")
            print(f"{subgroup_data['interpretation']}\n")

            for level, effect_data in subgroup_data['subgroup_effects'].items():
                print(f"  {subgroup_var} = {level}:")
                print(f"    Effect: {effect_data['effect']:.4f} "
                      f"[{effect_data['ci_95_lower']:.4f}, {effect_data['ci_95_upper']:.4f}]")
                print(f"    p-value: {effect_data['p_value']:.4f}")

# Initialize analyzer with experimental data
analyzer = TreatmentEffectAnalyzer(experiment_data)

# Perform ITT analysis (primary analysis)
itt_results = analyzer.intention_to_treat_analysis(
    outcome_var='[OUTCOME_VARIABLE]',
    treatment_var='[TREATMENT_VARIABLE]',
    covariates=['[COVARIATES]'] if '[COVARIATES]' else None
)

# Additional analyses as needed
if '[COMPLIANCE_VARIABLE]' in experiment_data.columns:
    pp_results = analyzer.per_protocol_analysis(
        outcome_var='[OUTCOME_VARIABLE]',
        treatment_var='[TREATMENT_VARIABLE]',
        compliance_var='[COMPLIANCE_VARIABLE]'
    )

if '[SUBGROUP_VARIABLES]':
    subgroup_results = analyzer.subgroup_analysis(
        outcome_var='[OUTCOME_VARIABLE]',
        treatment_var='[TREATMENT_VARIABLE]',
        subgroup_vars=['[SUBGROUP_VARIABLES]']
    )

if '[DOSE_VARIABLE]':
    dose_results = analyzer.dose_response_analysis(
        outcome_var='[OUTCOME_VARIABLE]',
        dose_var='[DOSE_VARIABLE]',
        covariates=['[COVARIATES]'] if '[COVARIATES]' else None
    )
```

OUTPUT REQUIREMENTS:

1. **Primary Analysis Results**
   - ITT effect estimate and confidence interval
   - Statistical significance (p-value)
   - Effect size with interpretation
   - Sample sizes in each group

2. **Secondary Analyses**
   - Per-protocol results (if applicable)
   - Subgroup analyses with interaction tests
   - Dose-response relationships
   - Sensitivity analyses

3. **Model Diagnostics**
   - Residual plots
   - Assumption checking
   - Influential observations
   - Model fit statistics

4. **Statistical Tables**
   - ANOVA table (for factorial designs)
   - Regression coefficients table
   - Effect estimates by subgroup
   - Multiple testing corrections
```

## Variables

### Analysis Configuration
- [RESEARCH_OBJECTIVE] - Research objective
- [ANALYSIS_METHOD] - Primary analysis method (itt, per_protocol, anova, regression)
- [OUTCOME_VARIABLE] - Primary outcome variable name
- [TREATMENT_VARIABLE] - Treatment variable name
- [ANALYSIS_POPULATION] - Population for analysis (itt, per_protocol, as_treated)

### Study Variables
- [COVARIATES] - List of covariate names for adjustment
- [COMPLIANCE_VARIABLE] - Variable indicating protocol compliance
- [DOSE_VARIABLE] - Continuous dose/intensity variable
- [SUBGROUP_VARIABLES] - List of subgroup variables
- [PRIMARY_HYPOTHESIS] - Primary hypothesis statement

## Best Practices

1. **Pre-specify analyses** - Define primary and secondary analyses before seeing data
2. **ITT is primary** - Always report ITT as main analysis
3. **Adjust for baseline** - Include baseline covariates to increase precision
4. **Correct for multiple testing** - Use Bonferroni or FDR for multiple outcomes
5. **Check assumptions** - Verify normality, homoscedasticity, independence
6. **Report all results** - Don't cherry-pick significant findings
7. **Use robust methods** - Consider robust standard errors if assumptions violated

## Usage Examples

### Example 1: Basic RCT Analysis
```
ANALYSIS_METHOD: "itt"
OUTCOME_VARIABLE: "pain_score_change"
TREATMENT_VARIABLE: "treatment_group"
COVARIATES: "['baseline_pain', 'age', 'sex']"
```

### Example 2: Factorial Design Analysis
```
ANALYSIS_METHOD: "anova"
OUTCOME_VARIABLE: "yield"
FACTOR_VARS: "['temperature', 'pressure', 'catalyst']"
INTERACTION_TERMS: True
```

### Example 3: Subgroup Analysis
```
ANALYSIS_METHOD: "itt"
OUTCOME_VARIABLE: "response_rate"
TREATMENT_VARIABLE: "drug_assignment"
SUBGROUP_VARIABLES: "['disease_severity', 'prior_treatment']"
```
