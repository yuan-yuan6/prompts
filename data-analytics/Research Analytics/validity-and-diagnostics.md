---
title: Experimental Validity and Diagnostics
category: data-analytics/Research Analytics
tags: [data-analytics, quality-assurance, research, validation, template]
use_cases:
  - Assess experimental validity through randomization checks, covariate balance, attrition analysis, compliance evaluation, contamination detection, and statistical assumption verification to ensure reliable causal inference
related_templates:
  - experimental-design-setup.md
  - randomization-and-power-analysis.md
  - treatment-effect-analysis.md
last_updated: 2025-11-10
---

# Experimental Validity and Diagnostics

## Purpose
Perform comprehensive validity assessment and diagnostic checks for experimental studies. This prompt helps you verify randomization success, assess covariate balance, analyze attrition and compliance patterns, detect contamination, check temporal effects, evaluate external validity, and verify statistical assumptions to ensure reliable and valid causal inference.

## Quick Start

**Example: Comprehensive Validity Assessment for Educational Intervention Study**

```
You are an experimental validity expert. Assess the validity of an educational intervention study testing a new teaching method across 20 schools.

STUDY DESIGN:
- Design: Cluster randomized trial
- Units: 20 schools (clusters), ~60 students per school
- Total participants: 1,200 students
- Randomization: 10 schools to new method, 10 to standard
- Duration: Full academic year (9 months)
- Primary outcome: End-of-year math test scores

DATA AVAILABLE:
- Baseline characteristics: prior test scores, SES, school size, teacher experience
- Treatment assignment and actual treatment received
- Outcome data: End-of-year test scores (available for 1,080 students)
- Attrition: 120 students (10% overall) - 8% in treatment, 12% in control
- Implementation fidelity: 85% in treatment schools
- Timeline: Staggered implementation over first 2 months

VALIDITY ASSESSMENT REQUIREMENTS:
1. Randomization check - verify baseline balance across 10 key characteristics
2. Covariate balance - calculate standardized differences for all baseline variables
3. Attrition analysis - test for differential attrition between groups
4. Implementation fidelity - assess compliance and contamination
5. Temporal effects - check for time trends in enrollment and outcomes
6. Statistical assumptions - verify normality, homogeneity of variance, independence
7. External validity - assess generalizability to broader population
8. Comprehensive validity report with recommendations

DELIVERABLES:
- Randomization success verification with balance tests
- Balance table with standardized differences
- Attrition analysis with differential dropout tests
- Implementation fidelity assessment
- Temporal trends analysis
- Statistical assumption checks
- Overall validity assessment with threat evaluation
- Recommendations for analysis approach based on validity findings
```

## Template

```
You are an experimental validity expert. Assess the experimental validity for [RESEARCH_OBJECTIVE] from [STUDY_DESIGN] with [PARTICIPANTS/UNITS].

STUDY PARAMETERS:
Design Information:
- Study design: [STUDY_DESIGN]
- Sample size: [N_PARTICIPANTS]
- Treatment groups: [TREATMENT_GROUPS]
- Randomization level: [RANDOMIZATION_LEVEL]
- Study duration: [STUDY_DURATION]

Data Structure:
- Treatment variable: [TREATMENT_VARIABLE]
- Outcome variable: [OUTCOME_VARIABLE]
- Baseline variables: [BASELINE_VARIABLES]
- Attrition indicator: [ATTRITION_INDICATOR]
- Compliance indicator: [COMPLIANCE_VARIABLE]
- Cluster variable: [CLUSTER_VARIABLE]
- Timestamp variable: [TIMESTAMP_VARIABLE]

VALIDITY ASSESSMENT COMPONENTS:
1. Randomization Success:
   - Balance tests on: [BALANCE_TEST_VARS]
   - Acceptable imbalance threshold: [IMBALANCE_THRESHOLD]
   - Statistical tests: [BALANCE_TEST_METHODS]

2. Covariate Balance:
   - Standardized difference threshold: [STD_DIFF_THRESHOLD]
   - Variables to assess: [COVARIATE_BALANCE_VARS]
   - Balance quality criteria: [BALANCE_CRITERIA]

3. Attrition Analysis:
   - Overall attrition rate: [ATTRITION_RATE]
   - Differential attrition test: [ATTRITION_TEST]
   - Attrition predictors: [ATTRITION_PREDICTORS]

4. Compliance Analysis:
   - Compliance definition: [COMPLIANCE_DEFINITION]
   - Expected compliance rate: [EXPECTED_COMPLIANCE]
   - Non-compliance patterns: [NONCOMPLIANCE_PATTERNS]

5. Contamination Assessment:
   - Contamination indicators: [CONTAMINATION_INDICATORS]
   - Spillover potential: [SPILLOVER_RISK]
   - Isolation verification: [ISOLATION_CHECK]

6. Temporal Effects:
   - Time trends to check: [TEMPORAL_TRENDS]
   - Seasonal effects: [SEASONAL_EFFECTS]
   - Implementation timeline: [IMPLEMENTATION_TIMELINE]

7. Statistical Assumptions:
   - Normality requirements: [NORMALITY_REQUIRED]
   - Variance homogeneity: [HOMOSCEDASTICITY_CHECK]
   - Independence verification: [INDEPENDENCE_CHECK]

8. External Validity:
   - Target population: [TARGET_POPULATION]
   - Sample representativeness: [REPRESENTATIVENESS]
   - Generalizability scope: [GENERALIZABILITY_SCOPE]

EXPECTED DELIVERABLES:
- Comprehensive validity assessment report
- Balance verification tables and plots
- Attrition analysis results
- Compliance and contamination evaluation
- Temporal trends analysis
- Statistical assumption verification
- Threat-to-validity evaluation
- Recommendations for addressing validity concerns
```

## Validity Assessment Framework

### Comprehensive Validity Checker

```python
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency, shapiro, levene, normaltest
import matplotlib.pyplot as plt
import seaborn as sns

class ExperimentalValidityChecker:
    def __init__(self, data, treatment_var, outcome_var):
        self.data = data
        self.treatment_var = treatment_var
        self.outcome_var = outcome_var
        self.validity_results = {}

    def comprehensive_validity_assessment(self, baseline_vars=None, post_treatment_vars=None):
        """Perform comprehensive experimental validity checks"""

        validity_checks = {
            'randomization_check': self.check_randomization_success(baseline_vars),
            'balance_check': self.check_covariate_balance(baseline_vars),
            'attrition_analysis': self.analyze_attrition(),
            'compliance_analysis': self.analyze_compliance() if '[COMPLIANCE_VARIABLE]' in self.data.columns else None,
            'contamination_check': self.check_contamination(),
            'temporal_effects': self.check_temporal_effects() if '[TIMESTAMP_VARIABLE]' in self.data.columns else None,
            'external_validity': self.assess_external_validity(),
            'statistical_assumptions': self.check_statistical_assumptions()
        }

        self.validity_results = validity_checks
        return validity_checks

    def check_randomization_success(self, baseline_vars):
        """Check if randomization was successful"""

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
                t_stat, p_value = ttest_ind(treatment_group, control_group)
                effect_size = (treatment_group.mean() - control_group.mean()) / np.sqrt((treatment_group.var() + control_group.var()) / 2)

                balance_tests[var] = {
                    'test_type': 't-test',
                    'treatment_mean': treatment_group.mean(),
                    'control_mean': control_group.mean(),
                    'difference': treatment_group.mean() - control_group.mean(),
                    'standardized_difference': effect_size,
                    't_statistic': t_stat,
                    'p_value': p_value,
                    'balanced': p_value > 0.05 and abs(effect_size) < 0.25
                }
            else:
                # Categorical variable - chi-square test
                crosstab = pd.crosstab(self.data[var], self.data[self.treatment_var])
                chi2, p_value, dof, expected = chi2_contingency(crosstab)

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
        """Check covariate balance using standardized differences"""

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

            else:
                # Categorical variables
                treatment_props = treatment_group.value_counts(normalize=True)
                control_props = control_group.value_counts(normalize=True)

                # Calculate standardized difference for each category
                for category in self.data[var].unique():
                    p_treat = treatment_props.get(category, 0)
                    p_control = control_props.get(category, 0)

                    pooled_p = (len(treatment_group) * p_treat + len(control_group) * p_control) / (len(treatment_group) + len(control_group))

                    if pooled_p > 0 and pooled_p < 1:
                        std_diff = (p_treat - p_control) / np.sqrt(pooled_p * (1 - pooled_p))
                    else:
                        std_diff = 0

                    balance_table.append({
                        'variable': f'{var}_{category}',
                        'treatment_proportion': p_treat,
                        'control_proportion': p_control,
                        'standardized_difference': std_diff,
                        'well_balanced': abs(std_diff) < 0.1,
                        'acceptable_balance': abs(std_diff) < 0.25
                    })

        balance_df = pd.DataFrame(balance_table)

        return {
            'balance_table': balance_df,
            'n_well_balanced': balance_df['well_balanced'].sum() if len(balance_df) > 0 else 0,
            'n_acceptable_balance': balance_df['acceptable_balance'].sum() if len(balance_df) > 0 else 0,
            'overall_balance_quality': balance_df['well_balanced'].mean() if len(balance_df) > 0 else 0
        }

    def analyze_attrition(self):
        """Analyze differential attrition between groups"""

        if '[ATTRITION_INDICATOR]' not in self.data.columns:
            return {'error': 'No attrition indicator variable found'}

        attrition_crosstab = pd.crosstab(self.data[self.treatment_var], self.data['[ATTRITION_INDICATOR]'])

        # Chi-square test for differential attrition
        chi2, p_value, dof, expected = chi2_contingency(attrition_crosstab)

        # Attrition rates by group
        attrition_rates = self.data.groupby(self.treatment_var)['[ATTRITION_INDICATOR]'].mean()

        return {
            'attrition_rates': attrition_rates.to_dict(),
            'differential_attrition_test': {
                'chi2_statistic': chi2,
                'p_value': p_value,
                'significant_differential_attrition': p_value < 0.05
            },
            'overall_attrition_rate': self.data['[ATTRITION_INDICATOR]'].mean(),
            'attrition_difference': attrition_rates.iloc[1] - attrition_rates.iloc[0] if len(attrition_rates) >= 2 else None
        }

    def analyze_compliance(self):
        """Analyze treatment compliance"""

        compliance_var = '[COMPLIANCE_VARIABLE]'

        if compliance_var not in self.data.columns:
            return {'error': 'No compliance variable found'}

        # Compliance rates by assigned treatment
        compliance_by_treatment = self.data.groupby(self.treatment_var)[compliance_var].agg([
            'count', 'mean', 'std'
        ])

        # Cross-tabulation of assignment vs. actual treatment
        compliance_crosstab = pd.crosstab(
            self.data[self.treatment_var],
            self.data[compliance_var],
            margins=True
        )

        # Calculate compliance types
        always_takers = len(self.data[(self.data[self.treatment_var] == 0) & (self.data[compliance_var] == 1)])
        never_takers = len(self.data[(self.data[self.treatment_var] == 1) & (self.data[compliance_var] == 0)])
        compliers = len(self.data[(self.data[self.treatment_var] == 1) & (self.data[compliance_var] == 1)]) + \
                   len(self.data[(self.data[self.treatment_var] == 0) & (self.data[compliance_var] == 0)])

        total_n = len(self.data)

        return {
            'compliance_rates': compliance_by_treatment,
            'compliance_crosstab': compliance_crosstab,
            'compliance_types': {
                'always_takers': always_takers,
                'never_takers': never_takers,
                'compliers': compliers,
                'always_taker_rate': always_takers / total_n,
                'never_taker_rate': never_takers / total_n,
                'complier_rate': compliers / total_n
            }
        }

    def check_contamination(self):
        """Check for treatment contamination"""

        contamination_indicators = []

        # Check for spillover effects if cluster or network data available
        if '[CLUSTER_VARIABLE]' in self.data.columns:
            cluster_treatment_rates = self.data.groupby('[CLUSTER_VARIABLE]')[self.treatment_var].mean()
            partial_treatment_clusters = ((cluster_treatment_rates > 0) & (cluster_treatment_rates < 1)).sum()

            contamination_indicators.append({
                'indicator': 'Partial treatment clusters',
                'value': partial_treatment_clusters,
                'interpretation': 'Higher values suggest possible contamination'
            })

        # Check for unusual outcome patterns in control group
        if self.outcome_var in self.data.columns:
            control_outcomes = self.data[self.data[self.treatment_var] == 0][self.outcome_var]

            # Check for bimodality in control group (potential contamination sign)
            _, normality_p = normaltest(control_outcomes.dropna())

            contamination_indicators.append({
                'indicator': 'Control group normality',
                'p_value': normality_p,
                'interpretation': 'Very low p-values might suggest contamination'
            })

        return {
            'contamination_indicators': contamination_indicators,
            'contamination_likely': any(ind.get('p_value', 1) < 0.01 for ind in contamination_indicators)
        }

    def check_temporal_effects(self):
        """Check for time-related effects"""

        timestamp_var = '[TIMESTAMP_VARIABLE]'

        if timestamp_var not in self.data.columns:
            return {'error': 'No timestamp variable found'}

        # Convert to datetime if not already
        self.data[timestamp_var] = pd.to_datetime(self.data[timestamp_var])

        # Check for temporal trends in treatment assignment
        temporal_treatment = self.data.groupby(self.data[timestamp_var].dt.date)[self.treatment_var].mean()

        # Test for trend in treatment assignment over time
        time_numeric = np.arange(len(temporal_treatment))
        treatment_trend_corr = np.corrcoef(time_numeric, temporal_treatment.values)[0, 1]

        # Check for temporal trends in outcome
        if self.outcome_var in self.data.columns:
            temporal_outcome = self.data.groupby(self.data[timestamp_var].dt.date)[self.outcome_var].mean()
            outcome_trend_corr = np.corrcoef(time_numeric[:len(temporal_outcome)], temporal_outcome.values)[0, 1]
        else:
            outcome_trend_corr = None

        return {
            'treatment_assignment_trend': {
                'correlation_with_time': treatment_trend_corr,
                'significant_trend': abs(treatment_trend_corr) > 0.3
            },
            'outcome_temporal_trend': {
                'correlation_with_time': outcome_trend_corr,
                'significant_trend': abs(outcome_trend_corr) > 0.3 if outcome_trend_corr else None
            }
        }

    def assess_external_validity(self):
        """Assess external validity of the experiment"""

        # This is largely conceptual and would need domain-specific implementation
        external_validity_checklist = {
            'population_representativeness': '[POPULATION_REPRESENTATIVENESS]',
            'setting_generalizability': '[SETTING_GENERALIZABILITY]',
            'treatment_fidelity': '[TREATMENT_FIDELITY]',
            'outcome_relevance': '[OUTCOME_RELEVANCE]',
            'time_period_relevance': '[TIME_PERIOD_RELEVANCE]'
        }

        return external_validity_checklist

    def check_statistical_assumptions(self):
        """Check statistical assumptions for the analysis"""

        if self.outcome_var not in self.data.columns:
            return {'error': 'Outcome variable not found for assumption checking'}

        assumptions = {}

        # Normality of outcome by group
        treatment_outcomes = self.data[self.data[self.treatment_var] == 1][self.outcome_var].dropna()
        control_outcomes = self.data[self.data[self.treatment_var] == 0][self.outcome_var].dropna()

        # Normality tests
        if len(treatment_outcomes) >= 3:
            _, treat_normal_p = shapiro(treatment_outcomes)
            assumptions['treatment_group_normality'] = {
                'p_value': treat_normal_p,
                'normal': treat_normal_p > 0.05
            }

        if len(control_outcomes) >= 3:
            _, control_normal_p = shapiro(control_outcomes)
            assumptions['control_group_normality'] = {
                'p_value': control_normal_p,
                'normal': control_normal_p > 0.05
            }

        # Homogeneity of variance
        if len(treatment_outcomes) >= 2 and len(control_outcomes) >= 2:
            _, levene_p = levene(treatment_outcomes, control_outcomes)
            assumptions['homogeneity_of_variance'] = {
                'levene_p_value': levene_p,
                'equal_variances': levene_p > 0.05
            }

        # Independence (conceptual check)
        assumptions['independence'] = {
            'clustering_present': '[CLUSTER_VARIABLE]' in self.data.columns,
            'temporal_structure': '[TIMESTAMP_VARIABLE]' in self.data.columns,
            'potential_dependence': '[CLUSTER_VARIABLE]' in self.data.columns or '[TIMESTAMP_VARIABLE]' in self.data.columns
        }

        return assumptions

    def generate_validity_report(self):
        """Generate comprehensive validity assessment report"""

        if not self.validity_results:
            self.comprehensive_validity_assessment()

        report_sections = []

        report_sections.append("EXPERIMENTAL VALIDITY ASSESSMENT REPORT")
        report_sections.append("=" * 50)

        # Randomization success
        if 'randomization_check' in self.validity_results:
            rand_check = self.validity_results['randomization_check']
            report_sections.append(f"\n1. RANDOMIZATION SUCCESS")
            report_sections.append(f"   Overall balance rate: {rand_check['overall_balance_rate']:.2%}")
            report_sections.append(f"   Randomization successful: {rand_check['randomization_successful']}")
            report_sections.append(f"   Variables balanced: {rand_check['n_balanced']}/{rand_check['n_variables_tested']}")

        # Attrition analysis
        if 'attrition_analysis' in self.validity_results and 'error' not in self.validity_results['attrition_analysis']:
            attrition = self.validity_results['attrition_analysis']
            report_sections.append(f"\n2. ATTRITION ANALYSIS")
            report_sections.append(f"   Overall attrition rate: {attrition['overall_attrition_rate']:.2%}")
            report_sections.append(f"   Differential attrition: {attrition['differential_attrition_test']['significant_differential_attrition']}")

        # Statistical assumptions
        if 'statistical_assumptions' in self.validity_results:
            assumptions = self.validity_results['statistical_assumptions']
            report_sections.append(f"\n3. STATISTICAL ASSUMPTIONS")

            if 'treatment_group_normality' in assumptions:
                report_sections.append(f"   Treatment group normality: {assumptions['treatment_group_normality']['normal']}")

            if 'control_group_normality' in assumptions:
                report_sections.append(f"   Control group normality: {assumptions['control_group_normality']['normal']}")

            if 'homogeneity_of_variance' in assumptions:
                report_sections.append(f"   Equal variances: {assumptions['homogeneity_of_variance']['equal_variances']}")

        return "\n".join(report_sections)

# Perform validity assessment
validity_checker = ExperimentalValidityChecker(
    data=experiment_data,
    treatment_var='[TREATMENT_VARIABLE]',
    outcome_var='[OUTCOME_VARIABLE]'
)

validity_assessment = validity_checker.comprehensive_validity_assessment(
    baseline_vars=['[BASELINE_VARIABLES]'] if '[BASELINE_VARIABLES]' else None
)

validity_report = validity_checker.generate_validity_report()
```

## Variables

### Core Validity Variables
- [TREATMENT_VARIABLE] - Treatment assignment variable
- [OUTCOME_VARIABLE] - Primary outcome variable
- [BASELINE_VARIABLES] - List of baseline covariates
- [ATTRITION_INDICATOR] - Variable indicating dropout/attrition
- [COMPLIANCE_VARIABLE] - Variable indicating treatment compliance
- [CLUSTER_VARIABLE] - Cluster identifier (if applicable)
- [TIMESTAMP_VARIABLE] - Timestamp for temporal analysis

### Assessment Configuration
- [BALANCE_TEST_VARS] - Variables for balance testing
- [IMBALANCE_THRESHOLD] - Acceptable imbalance threshold
- [STD_DIFF_THRESHOLD] - Standardized difference threshold (typically 0.1 or 0.25)
- [BALANCE_CRITERIA] - Criteria for acceptable balance
- [ATTRITION_TEST] - Statistical test for attrition
- [CONTAMINATION_INDICATORS] - Indicators of contamination
- [SPILLOVER_RISK] - Risk level of spillover effects

### External Validity Variables
- [TARGET_POPULATION] - Intended population for generalization
- [REPRESENTATIVENESS] - How representative sample is
- [GENERALIZABILITY_SCOPE] - Scope of generalizability
- [POPULATION_REPRESENTATIVENESS] - Population representation assessment
- [SETTING_GENERALIZABILITY] - Setting generalizability assessment
- [TREATMENT_FIDELITY] - Treatment implementation fidelity
- [OUTCOME_RELEVANCE] - Relevance of measured outcomes

## Usage Examples

### Example 1: Basic Validity Assessment
```python
# Load data
data = pd.read_csv('experiment_data.csv')

# Initialize checker
checker = ExperimentalValidityChecker(
    data=data,
    treatment_var='treatment_assigned',
    outcome_var='outcome_score'
)

# Run comprehensive assessment
validity = checker.comprehensive_validity_assessment(
    baseline_vars=['age', 'gender', 'baseline_score', 'ses']
)

# Generate report
report = checker.generate_validity_report()
print(report)
```

### Example 2: Detailed Balance Check
```python
balance_results = checker.check_covariate_balance(
    baseline_vars=['age', 'gender', 'prior_score', 'ses', 'school_type']
)

balance_df = balance_results['balance_table']
print(f"Well-balanced variables: {balance_results['n_well_balanced']}")
print(f"Overall balance quality: {balance_results['overall_balance_quality']:.2%}")

# Display variables with poor balance
poor_balance = balance_df[~balance_df['acceptable_balance']]
if len(poor_balance) > 0:
    print("\nVariables with poor balance:")
    print(poor_balance[['variable', 'standardized_difference']])
```

### Example 3: Attrition Analysis
```python
attrition_results = checker.analyze_attrition()

print(f"Overall attrition: {attrition_results['overall_attrition_rate']:.1%}")
print(f"Treatment attrition: {attrition_results['attrition_rates'][1]:.1%}")
print(f"Control attrition: {attrition_results['attrition_rates'][0]:.1%}")
print(f"Differential attrition significant: {attrition_results['differential_attrition_test']['significant_differential_attrition']}")
```

### Example 4: Statistical Assumptions Check
```python
assumptions = checker.check_statistical_assumptions()

print("Normality:")
print(f"  Treatment group: {assumptions['treatment_group_normality']['normal']}")
print(f"  Control group: {assumptions['control_group_normality']['normal']}")

print("\nVariance homogeneity:")
print(f"  Equal variances: {assumptions['homogeneity_of_variance']['equal_variances']}")

print("\nIndependence:")
print(f"  Potential dependence: {assumptions['independence']['potential_dependence']}")
```

## Best Practices

1. **Pre-specify Checks** - Define validity checks in analysis plan before data collection
2. **Test Multiple Variables** - Check balance on many baseline covariates, not just a few
3. **Use Standardized Differences** - Prefer standardized differences over p-values for balance
4. **Document Violations** - Record all protocol violations and deviations
5. **Analyze Attrition Patterns** - Check if dropout is random or systematic
6. **Verify Assumptions** - Don't assume statistical assumptions hold without checking
7. **Check Temporal Patterns** - Look for time trends in enrollment and outcomes
8. **Assess Contamination** - Verify treatment isolation in control group
9. **Report Transparently** - Disclose all validity threats and how they were addressed
10. **Adjust Analysis Plan** - Modify analytical approach based on validity findings

## Common Validity Threats

### Internal Validity Threats
- Selection bias from non-random assignment
- Attrition bias from differential dropout
- Contamination from treatment spillover
- Testing effects from repeated measures
- Instrumentation changes over time
- Regression to the mean
- Maturation effects

### External Validity Threats
- Sample not representative of population
- Artificial experimental setting
- Treatment implementation differs from real-world
- Outcome measures not clinically relevant
- Short-term effects may not persist
- Context-specific effects

### Statistical Conclusion Validity Threats
- Insufficient statistical power
- Violated statistical assumptions
- Fishing and multiple comparisons
- Unreliable measures
- Random heterogeneity of participants
- Implementation variability
