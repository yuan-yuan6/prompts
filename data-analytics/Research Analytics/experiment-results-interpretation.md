---
title: Experiment Results Interpretation & Reporting
category: data-analytics/Research Analytics
tags: [automation, data-analytics, data-science, research, reporting, template]
use_cases:
  - Interpreting experimental results including effect sizes and statistical significance
  - Assessing internal and external validity of experimental findings
  - Reporting experimental results following standard guidelines (CONSORT, etc.)
  - Drawing practical implications from statistical findings
related_templates:
  - experimental-design-overview.md
  - doe-analysis-methods.md
  - sample-size-power-analysis.md
last_updated: 2025-11-09
---

# Experiment Results Interpretation & Reporting

## Purpose
Interpret experimental results correctly, assess validity of findings, distinguish between statistical and practical significance, and report results following established standards for transparent and reproducible research.

## Template

```
You are an experimental results interpretation expert. Interpret findings from [EXPERIMENT_TYPE] showing [EFFECT_ESTIMATE] effect (p=[P_VALUE]) on [OUTCOME], assess [VALIDITY_CONCERNS], and provide recommendations for [STAKEHOLDERS].

INTERPRETATION FRAMEWORK:

Study Results:
- Effect estimate: [EFFECT_ESTIMATE]
- Confidence interval: [CONFIDENCE_INTERVAL]
- P-value: [P_VALUE]
- Effect size: [EFFECT_SIZE]
- Sample size: [SAMPLE_SIZE]
- Outcome: [OUTCOME]

### Interpretation Dimensions

1. **Statistical Significance**: Is the effect statistically different from zero?
2. **Practical Significance**: Is the effect large enough to matter?
3. **Internal Validity**: Can we trust the causal inference?
4. **External Validity**: Does it generalize beyond this study?
5. **Clinical/Business Relevance**: What are the real-world implications?

IMPLEMENTATION:
```python
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

class ExperimentalValidityChecker:
    """
    Comprehensive validity assessment and results interpretation
    """

    def __init__(self, data, treatment_var, outcome_var):
        """
        Initialize validity checker

        Parameters:
        -----------
        data : DataFrame
            Experimental data
        treatment_var : str
            Treatment variable name
        outcome_var : str
            Outcome variable name
        """
        self.data = data
        self.treatment_var = treatment_var
        self.outcome_var = outcome_var
        self.validity_results = {}

    def comprehensive_validity_assessment(self, baseline_vars=None):
        """
        Perform comprehensive experimental validity checks

        Returns:
        --------
        dict : Validity assessment results
        """

        validity_checks = {
            'randomization_check': self.check_randomization_success(baseline_vars),
            'balance_check': self.check_covariate_balance(baseline_vars),
            'attrition_analysis': self.analyze_attrition(),
            'statistical_assumptions': self.check_statistical_assumptions(),
            'sample_size_adequacy': self.assess_sample_size_adequacy(),
            'effect_heterogeneity': self.assess_effect_heterogeneity()
        }

        self.validity_results = validity_checks
        return validity_checks

    def check_randomization_success(self, baseline_vars):
        """
        Check if randomization achieved baseline balance

        Parameters:
        -----------
        baseline_vars : list
            Baseline variables to check

        Returns:
        --------
        dict : Randomization check results
        """

        if baseline_vars is None:
            return {'error': 'No baseline variables provided for randomization check'}

        balance_tests = {}
        overall_balance_score = 0

        for var in baseline_vars:
            if var not in self.data.columns:
                continue

            treatment_group = self.data[self.data[self.treatment_var] == 1][var]
            control_group = self.data[self.data[self.treatment_var] == 0][var]

            # Test depends on variable type
            if self.data[var].dtype in ['int64', 'float64']:
                # Continuous variable - t-test
                t_stat, p_value = stats.ttest_ind(treatment_group, control_group)

                # Standardized difference
                pooled_std = np.sqrt((treatment_group.var() + control_group.var()) / 2)
                std_diff = (treatment_group.mean() - control_group.mean()) / pooled_std if pooled_std > 0 else 0

                balance_tests[var] = {
                    'test_type': 't-test',
                    'treatment_mean': treatment_group.mean(),
                    'control_mean': control_group.mean(),
                    'difference': treatment_group.mean() - control_group.mean(),
                    'standardized_difference': std_diff,
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'balanced': p_value > 0.05 and abs(std_diff) < 0.25
                }
            else:
                # Categorical variable - chi-square test
                crosstab = pd.crosstab(self.data[var], self.data[self.treatment_var])
                chi2, p_value, dof, expected = stats.chi2_contingency(crosstab)

                balance_tests[var] = {
                    'test_type': 'chi-square',
                    'chi2_statistic': chi2,
                    'p_value': p_value,
                    'degrees_of_freedom': dof,
                    'balanced': p_value > 0.05
                }

            # Update overall balance score
            if balance_tests[var]['balanced']:
                overall_balance_score += 1

        overall_balance_rate = overall_balance_score / len(baseline_vars) if baseline_vars else 0

        return {
            'individual_tests': balance_tests,
            'overall_balance_rate': overall_balance_rate,
            'randomization_successful': overall_balance_rate >= 0.8,
            'n_variables_tested': len(baseline_vars),
            'n_balanced': overall_balance_score
        }

    def check_covariate_balance(self, baseline_vars):
        """
        Check covariate balance using standardized differences

        Standardized difference < 0.1 = well balanced
        Standardized difference < 0.25 = acceptable

        Parameters:
        -----------
        baseline_vars : list
            Variables to check balance on

        Returns:
        --------
        dict : Balance check results
        """

        if baseline_vars is None:
            return {'error': 'No baseline variables provided for balance check'}

        balance_table = []

        for var in baseline_vars:
            if var not in self.data.columns:
                continue

            treatment_group = self.data[self.data[self.treatment_var] == 1][var]
            control_group = self.data[self.data[self.treatment_var] == 0][var]

            if self.data[var].dtype in ['int64', 'float64']:
                # Continuous variables
                treatment_mean = treatment_group.mean()
                control_mean = control_group.mean()
                treatment_std = treatment_group.std()
                control_std = control_group.std()

                pooled_std = np.sqrt((treatment_std**2 + control_std**2) / 2)
                standardized_diff = (treatment_mean - control_mean) / pooled_std if pooled_std > 0 else 0

                balance_table.append({
                    'variable': var,
                    'treatment_mean': treatment_mean,
                    'control_mean': control_mean,
                    'standardized_difference': standardized_diff,
                    'well_balanced': abs(standardized_diff) < 0.1,
                    'acceptable_balance': abs(standardized_diff) < 0.25
                })

        balance_df = pd.DataFrame(balance_table)

        return {
            'balance_table': balance_df,
            'n_well_balanced': balance_df['well_balanced'].sum() if len(balance_df) > 0 else 0,
            'n_acceptable_balance': balance_df['acceptable_balance'].sum() if len(balance_df) > 0 else 0,
            'overall_balance_quality': balance_df['well_balanced'].mean() if len(balance_df) > 0 else 0
        }

    def analyze_attrition(self):
        """
        Analyze differential attrition between groups

        Returns:
        --------
        dict : Attrition analysis results
        """

        if 'attrition' not in self.data.columns:
            return {'note': 'No attrition indicator variable found'}

        attrition_crosstab = pd.crosstab(self.data[self.treatment_var], self.data['attrition'])

        # Chi-square test for differential attrition
        chi2, p_value, dof, expected = stats.chi2_contingency(attrition_crosstab)

        # Attrition rates by group
        attrition_rates = self.data.groupby(self.treatment_var)['attrition'].mean()

        return {
            'attrition_rates': attrition_rates.to_dict(),
            'differential_attrition_test': {
                'chi2_statistic': chi2,
                'p_value': p_value,
                'significant_differential_attrition': p_value < 0.05
            },
            'overall_attrition_rate': self.data['attrition'].mean(),
            'attrition_difference': abs(attrition_rates.iloc[1] - attrition_rates.iloc[0]) if len(attrition_rates) >= 2 else None,
            'concern_level': 'High' if p_value < 0.05 else 'Low'
        }

    def check_statistical_assumptions(self):
        """
        Check statistical assumptions for the analysis

        Returns:
        --------
        dict : Assumption check results
        """

        if self.outcome_var not in self.data.columns:
            return {'error': 'Outcome variable not found for assumption checking'}

        assumptions = {}

        # Normality of outcome by group
        treatment_outcomes = self.data[self.data[self.treatment_var] == 1][self.outcome_var].dropna()
        control_outcomes = self.data[self.data[self.treatment_var] == 0][self.outcome_var].dropna()

        # Normality tests
        if len(treatment_outcomes) >= 3:
            _, treat_normal_p = stats.shapiro(treatment_outcomes[:5000])  # Shapiro max 5000
            assumptions['treatment_group_normality'] = {
                'p_value': treat_normal_p,
                'normal': treat_normal_p > 0.05,
                'note': 'Based on Shapiro-Wilk test'
            }

        if len(control_outcomes) >= 3:
            _, control_normal_p = stats.shapiro(control_outcomes[:5000])
            assumptions['control_group_normality'] = {
                'p_value': control_normal_p,
                'normal': control_normal_p > 0.05,
                'note': 'Based on Shapiro-Wilk test'
            }

        # Homogeneity of variance
        if len(treatment_outcomes) >= 2 and len(control_outcomes) >= 2:
            _, levene_p = stats.levene(treatment_outcomes, control_outcomes)
            assumptions['homogeneity_of_variance'] = {
                'levene_p_value': levene_p,
                'equal_variances': levene_p > 0.05,
                'note': 'Based on Levene test'
            }

        return assumptions

    def assess_sample_size_adequacy(self):
        """
        Assess if sample size was adequate for detecting effects

        Returns:
        --------
        dict : Sample size adequacy assessment
        """

        n_treatment = len(self.data[self.data[self.treatment_var] == 1])
        n_control = len(self.data[self.data[self.treatment_var] == 0])
        total_n = len(self.data)

        # Basic adequacy checks
        adequacy = {
            'total_sample_size': total_n,
            'treatment_n': n_treatment,
            'control_n': n_control,
            'balance_ratio': n_treatment / n_control if n_control > 0 else np.inf,
            'minimum_n_met': min(n_treatment, n_control) >= 30,
            'balanced_allocation': 0.8 <= (n_treatment / n_control) <= 1.25 if n_control > 0 else False
        }

        # Overall assessment
        if adequacy['minimum_n_met'] and adequacy['balanced_allocation']:
            adequacy['overall_assessment'] = 'Adequate'
        elif adequacy['minimum_n_met']:
            adequacy['overall_assessment'] = 'Adequate but imbalanced'
        else:
            adequacy['overall_assessment'] = 'Inadequate - underpowered'

        return adequacy

    def assess_effect_heterogeneity(self):
        """
        Assess whether treatment effects are consistent

        Returns:
        --------
        dict : Effect heterogeneity assessment
        """

        # Check variance of outcomes within treatment groups
        treatment_outcomes = self.data[self.data[self.treatment_var] == 1][self.outcome_var]
        control_outcomes = self.data[self.data[self.treatment_var] == 0][self.outcome_var]

        heterogeneity = {
            'treatment_variance': treatment_outcomes.var(),
            'control_variance': control_outcomes.var(),
            'variance_ratio': treatment_outcomes.var() / control_outcomes.var() if control_outcomes.var() > 0 else np.inf,
            'treatment_cv': treatment_outcomes.std() / treatment_outcomes.mean() if treatment_outcomes.mean() != 0 else np.inf,
            'control_cv': control_outcomes.std() / control_outcomes.mean() if control_outcomes.mean() != 0 else np.inf
        }

        # Assess heterogeneity level
        if heterogeneity['variance_ratio'] > 2 or heterogeneity['variance_ratio'] < 0.5:
            heterogeneity['heterogeneity_level'] = 'High'
        else:
            heterogeneity['heterogeneity_level'] = 'Low to Moderate'

        return heterogeneity

    def interpret_effect_size(self, effect_estimate, effect_type='cohens_d'):
        """
        Interpret effect size magnitude

        Parameters:
        -----------
        effect_estimate : float
            Effect size estimate
        effect_type : str
            Type of effect size (cohens_d, correlation, odds_ratio, etc.)

        Returns:
        --------
        dict : Effect size interpretation
        """

        interpretation = {
            'effect_estimate': effect_estimate,
            'effect_type': effect_type
        }

        if effect_type == 'cohens_d':
            abs_effect = abs(effect_estimate)
            if abs_effect < 0.2:
                interpretation['magnitude'] = 'Negligible'
                interpretation['interpretation'] = 'Very small effect, may not be practically meaningful'
            elif abs_effect < 0.5:
                interpretation['magnitude'] = 'Small'
                interpretation['interpretation'] = 'Small effect, may be of limited practical importance'
            elif abs_effect < 0.8:
                interpretation['magnitude'] = 'Medium'
                interpretation['interpretation'] = 'Moderate effect, likely practically important'
            else:
                interpretation['magnitude'] = 'Large'
                interpretation['interpretation'] = 'Large effect, very likely practically important'

        elif effect_type == 'correlation':
            abs_effect = abs(effect_estimate)
            if abs_effect < 0.1:
                interpretation['magnitude'] = 'Negligible'
            elif abs_effect < 0.3:
                interpretation['magnitude'] = 'Small'
            elif abs_effect < 0.5:
                interpretation['magnitude'] = 'Medium'
            else:
                interpretation['magnitude'] = 'Large'

        return interpretation

    def assess_practical_significance(self, effect_estimate, mcid=None, cost_benefit_ratio=None):
        """
        Assess practical/clinical significance beyond statistical significance

        Parameters:
        -----------
        effect_estimate : float
            Observed effect size
        mcid : float, optional
            Minimal Clinically Important Difference
        cost_benefit_ratio : float, optional
            Cost per unit of benefit

        Returns:
        --------
        dict : Practical significance assessment
        """

        assessment = {
            'effect_estimate': effect_estimate,
            'statistical_significance_alone': 'Not sufficient for decision-making'
        }

        if mcid is not None:
            assessment['mcid'] = mcid
            assessment['exceeds_mcid'] = abs(effect_estimate) >= mcid
            assessment['practical_importance'] = 'Yes' if assessment['exceeds_mcid'] else 'Questionable'

        if cost_benefit_ratio is not None:
            assessment['cost_benefit_ratio'] = cost_benefit_ratio
            assessment['cost_effective'] = effect_estimate > 0 and cost_benefit_ratio < 50000  # Example threshold

        return assessment

    def generate_validity_report(self):
        """
        Generate comprehensive validity assessment report

        Returns:
        --------
        str : Formatted validity report
        """

        if not self.validity_results:
            self.comprehensive_validity_assessment()

        report_sections = []

        report_sections.append("="*70)
        report_sections.append("EXPERIMENTAL VALIDITY ASSESSMENT REPORT")
        report_sections.append("="*70)

        # Randomization success
        if 'randomization_check' in self.validity_results:
            rand_check = self.validity_results['randomization_check']
            if 'error' not in rand_check:
                report_sections.append(f"\n1. RANDOMIZATION SUCCESS")
                report_sections.append(f"   Overall balance rate: {rand_check['overall_balance_rate']:.2%}")
                report_sections.append(f"   Randomization successful: {'Yes' if rand_check['randomization_successful'] else 'No'}")
                report_sections.append(f"   Variables balanced: {rand_check['n_balanced']}/{rand_check['n_variables_tested']}")

        # Sample size adequacy
        if 'sample_size_adequacy' in self.validity_results:
            sample_check = self.validity_results['sample_size_adequacy']
            report_sections.append(f"\n2. SAMPLE SIZE ADEQUACY")
            report_sections.append(f"   Total sample: {sample_check['total_sample_size']}")
            report_sections.append(f"   Treatment: {sample_check['treatment_n']}, Control: {sample_check['control_n']}")
            report_sections.append(f"   Assessment: {sample_check['overall_assessment']}")

        # Statistical assumptions
        if 'statistical_assumptions' in self.validity_results:
            assumptions = self.validity_results['statistical_assumptions']
            report_sections.append(f"\n3. STATISTICAL ASSUMPTIONS")

            if 'treatment_group_normality' in assumptions:
                report_sections.append(f"   Treatment group normality: {'Met' if assumptions['treatment_group_normality']['normal'] else 'Violated'}")

            if 'control_group_normality' in assumptions:
                report_sections.append(f"   Control group normality: {'Met' if assumptions['control_group_normality']['normal'] else 'Violated'}")

            if 'homogeneity_of_variance' in assumptions:
                report_sections.append(f"   Equal variances: {'Yes' if assumptions['homogeneity_of_variance']['equal_variances'] else 'No'}")

        # Attrition
        if 'attrition_analysis' in self.validity_results:
            attrition = self.validity_results['attrition_analysis']
            if 'overall_attrition_rate' in attrition:
                report_sections.append(f"\n4. ATTRITION ANALYSIS")
                report_sections.append(f"   Overall attrition: {attrition['overall_attrition_rate']:.2%}")
                report_sections.append(f"   Differential attrition concern: {attrition['concern_level']}")

        report_sections.append("\n" + "="*70)

        return "\n".join(report_sections)

# Initialize validity checker
validity_checker = ExperimentalValidityChecker(
    data=experiment_data,
    treatment_var='[TREATMENT_VARIABLE]',
    outcome_var='[OUTCOME_VARIABLE]'
)

# Perform comprehensive validity assessment
validity_assessment = validity_checker.comprehensive_validity_assessment(
    baseline_vars=['[BASELINE_VARIABLES]'] if '[BASELINE_VARIABLES]' else None
)

# Generate report
validity_report = validity_checker.generate_validity_report()
print(validity_report)

# Interpret effect size
effect_interpretation = validity_checker.interpret_effect_size(
    effect_estimate=[EFFECT_SIZE_ESTIMATE],
    effect_type='[EFFECT_TYPE]'
)

# Assess practical significance
practical_assessment = validity_checker.assess_practical_significance(
    effect_estimate=[EFFECT_SIZE_ESTIMATE],
    mcid=[MCID] if '[MCID]' else None
)
```

OUTPUT REQUIREMENTS:

1. **Results Summary**
   - Effect estimate with confidence interval
   - Statistical significance (p-value)
   - Effect size with interpretation
   - Number analyzed vs. randomized

2. **Validity Assessment**
   - Internal validity threats identified
   - External validity considerations
   - Statistical assumption violations
   - Quality indicators (CONSORT checklist)

3. **Interpretation**
   - Statistical vs. practical significance
   - Clinical/business relevance
   - Strength of evidence
   - Limitations and caveats

4. **Recommendations**
   - Implementation recommendations
   - Conditions for generalization
   - Need for replication
   - Future research directions

5. **Reporting Standards**
   - CONSORT diagram (for RCTs)
   - Baseline characteristics table
   - Primary outcome results table
   - Adverse events summary
```

## Variables

### Results Variables
- [EXPERIMENT_TYPE] - Type of experiment conducted
- [EFFECT_ESTIMATE] - Primary effect estimate
- [CONFIDENCE_INTERVAL] - 95% confidence interval
- [P_VALUE] - Statistical p-value
- [EFFECT_SIZE] - Standardized effect size (Cohen's d, etc.)
- [SAMPLE_SIZE] - Total sample size
- [OUTCOME] - Primary outcome measure

### Interpretation Variables
- [VALIDITY_CONCERNS] - Known validity threats
- [STAKEHOLDERS] - Target audience for recommendations
- [MCID] - Minimal Clinically Important Difference
- [BASELINE_VARIABLES] - Variables to check balance on
- [EFFECT_TYPE] - Type of effect size (cohens_d, correlation, odds_ratio)

### Analysis Variables
- [TREATMENT_VARIABLE] - Treatment variable name in data
- [OUTCOME_VARIABLE] - Outcome variable name in data
- [EFFECT_SIZE_ESTIMATE] - Calculated effect size value

## Best Practices

1. **Distinguish statistical from practical significance** - p < 0.05 doesn't mean important
2. **Always report confidence intervals** - More informative than p-values alone
3. **Assess and report validity threats** - Be transparent about limitations
4. **Use standard reporting guidelines** - CONSORT for RCTs, TREND for quasi-experimental
5. **Report all pre-specified outcomes** - Including non-significant results
6. **Provide context for effect sizes** - Compare to MCID or prior studies
7. **Consider alternative explanations** - Don't over-interpret findings

## Interpretation Guidelines

### Statistical Significance
- **p < 0.05**: Conventionally "statistically significant"
- **p < 0.01**: "Highly significant"
- **p > 0.05**: "Not statistically significant" (NOT "no effect")

### Effect Size (Cohen's d)
- **d < 0.2**: Negligible
- **0.2 ≤ d < 0.5**: Small
- **0.5 ≤ d < 0.8**: Medium
- **d ≥ 0.8**: Large

### Confidence Intervals
- **Narrow CI**: Precise estimate
- **Wide CI**: Imprecise estimate (need larger sample)
- **CI excludes 0**: Statistically significant
- **CI includes MCID**: Potentially clinically meaningful

## Usage Examples

### Example 1: RCT Results Interpretation
```
EFFECT_ESTIMATE: 5.2
CONFIDENCE_INTERVAL: "[2.1, 8.3]"
P_VALUE: 0.001
EFFECT_SIZE: 0.65
MCID: 3.0
INTERPRETATION: "Medium to large effect, exceeds MCID, high confidence"
```

### Example 2: Non-Significant Finding
```
EFFECT_ESTIMATE: 1.2
CONFIDENCE_INTERVAL: "[-0.5, 2.9]"
P_VALUE: 0.18
EFFECT_SIZE: 0.15
INTERPRETATION: "Small, non-significant effect. CI compatible with small benefit or small harm."
```

### Example 3: Statistical but Not Practical Significance
```
EFFECT_ESTIMATE: 0.8
CONFIDENCE_INTERVAL: "[0.2, 1.4]"
P_VALUE: 0.01
EFFECT_SIZE: 0.12
MCID: 3.0
INTERPRETATION: "Statistically significant but below MCID threshold. Limited practical importance."
```
