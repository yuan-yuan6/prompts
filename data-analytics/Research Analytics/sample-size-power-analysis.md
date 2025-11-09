---
title: Power Analysis & Sample Size Determination
category: data-analytics/Research Analytics
tags: [automation, data-analytics, data-science, design, research, statistics, template]
use_cases:
  - Calculating required sample sizes to achieve desired statistical power
  - Determining minimum detectable effects for given sample sizes
  - Performing power analysis for different statistical tests
  - Conducting sensitivity analyses for power calculations
related_templates:
  - experimental-design-overview.md
  - experiment-design-principles.md
  - doe-analysis-methods.md
last_updated: 2025-11-09
---

# Power Analysis & Sample Size Determination

## Purpose
Calculate appropriate sample sizes and assess statistical power to ensure experiments can detect meaningful effects with desired confidence, avoiding both underpowered studies and unnecessary over-recruitment.

## Template

```
You are a power analysis expert. Calculate sample size requirements for [TEST_TYPE] to detect [EFFECT_SIZE] effect with [STATISTICAL_POWER] power at [ALPHA_LEVEL] significance level, considering [STUDY_CONSTRAINTS].

POWER ANALYSIS FRAMEWORK:

Study Parameters:
- Statistical test: [TEST_TYPE]
- Expected effect size: [EFFECT_SIZE]
- Desired power: [STATISTICAL_POWER]
- Significance level (α): [ALPHA_LEVEL]
- Alternative hypothesis: [ALTERNATIVE]
- Study constraints: [STUDY_CONSTRAINTS]

### Power Analysis Fundamentals

Key Relationships:
1. **Power (1-β)**: Probability of detecting effect when it exists
2. **Effect Size**: Magnitude of difference to detect
3. **Sample Size**: Number of observations needed
4. **Alpha (α)**: Type I error rate (false positive)

These four parameters are interdependent - fixing three determines the fourth.

IMPLEMENTATION:
```python
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.power import TTestPower, FTestAnovaPower, TTestIndPower
from statsmodels.stats.proportion import proportion_effectsize, proportions_ztest
import matplotlib.pyplot as plt
import seaborn as sns

class PowerAnalyzer:
    """
    Comprehensive power analysis for experimental designs
    """

    def __init__(self):
        self.power_calculators = {
            'ttest': TTestPower(),
            'anova': FTestAnovaPower(),
            'proportion': self.proportion_power_analysis,
            'correlation': self.correlation_power_analysis,
            'regression': self.regression_power_analysis
        }
        self.results_cache = {}

    def comprehensive_power_analysis(self, test_type, effect_size, alpha=0.05,
                                    power=0.8, **kwargs):
        """
        Perform comprehensive power analysis for different test types

        Parameters:
        -----------
        test_type : str
            Type of test ('ttest', 'anova', 'proportion', 'correlation', 'regression')
        effect_size : float
            Expected effect size
        alpha : float
            Significance level (default: 0.05)
        power : float
            Desired statistical power (default: 0.8)
        **kwargs : additional parameters specific to test type

        Returns:
        --------
        dict : Power analysis results
        """

        if test_type == 'ttest':
            return self.ttest_power_analysis(effect_size, alpha, power, **kwargs)
        elif test_type == 'anova':
            return self.anova_power_analysis(effect_size, alpha, power, **kwargs)
        elif test_type == 'proportion':
            return self.proportion_power_analysis(effect_size, alpha, power, **kwargs)
        elif test_type == 'correlation':
            return self.correlation_power_analysis(effect_size, alpha, power, **kwargs)
        elif test_type == 'regression':
            return self.regression_power_analysis(effect_size, alpha, power, **kwargs)
        else:
            raise ValueError(f"Unknown test type: {test_type}")

    def ttest_power_analysis(self, effect_size, alpha=0.05, power=0.8,
                           test_type='two-sample', alternative='two-sided', ratio=1):
        """
        T-test power analysis

        Parameters:
        -----------
        effect_size : float
            Cohen's d (standardized mean difference)
        alpha : float
            Significance level
        power : float
            Desired power
        test_type : str
            'one-sample', 'two-sample', or 'paired'
        alternative : str
            'two-sided', 'larger', or 'smaller'
        ratio : float
            Ratio of sample sizes (n2/n1) for two-sample test

        Returns:
        --------
        dict : Power analysis results including sample size and power curves
        """

        power_calc = TTestPower()

        # Calculate required sample size
        sample_size = power_calc.solve_power(
            effect_size=effect_size,
            power=power,
            alpha=alpha,
            ratio=ratio,
            alternative=alternative
        )

        # Generate power curve data
        sample_sizes = np.arange(5, int(sample_size * 2.5), 5)
        power_values = power_calc.solve_power(
            effect_size=effect_size,
            nobs1=sample_sizes,
            alpha=alpha,
            alternative=alternative,
            ratio=ratio
        )

        # Generate effect size curve data
        effect_sizes = np.arange(0.1, 2.0, 0.05)
        power_by_effect = power_calc.solve_power(
            effect_size=effect_sizes,
            nobs1=sample_size,
            alpha=alpha,
            alternative=alternative,
            ratio=ratio
        )

        results = {
            'test_type': 'T-test',
            'test_variant': test_type,
            'required_sample_size_per_group': int(np.ceil(sample_size)),
            'total_sample_size': int(np.ceil(sample_size * (1 + ratio))),
            'effect_size_cohens_d': effect_size,
            'power': power,
            'alpha': alpha,
            'alternative': alternative,
            'sample_size_ratio': ratio,
            'power_curve': {
                'sample_sizes': sample_sizes,
                'power_values': power_values
            },
            'effect_size_curve': {
                'effect_sizes': effect_sizes,
                'power_values': power_by_effect
            },
            'interpretation': self._interpret_effect_size_cohens_d(effect_size)
        }

        self._print_power_summary(results)

        return results

    def anova_power_analysis(self, effect_size, alpha=0.05, power=0.8, k_groups=3):
        """
        One-way ANOVA power analysis

        Parameters:
        -----------
        effect_size : float
            Effect size f (Cohen's f)
        alpha : float
            Significance level
        power : float
            Desired power
        k_groups : int
            Number of groups

        Returns:
        --------
        dict : Power analysis results
        """

        power_calc = FTestAnovaPower()

        # Calculate required sample size per group
        sample_size = power_calc.solve_power(
            effect_size=effect_size,
            alpha=alpha,
            power=power,
            k_groups=k_groups
        )

        # Convert Cohen's f to eta-squared
        eta_squared = effect_size**2 / (1 + effect_size**2)

        # Generate power curve
        sample_sizes = np.arange(5, int(sample_size * 2), 2)
        power_values = []
        for n in sample_sizes:
            p = power_calc.solve_power(
                effect_size=effect_size,
                nobs=n,
                alpha=alpha,
                k_groups=k_groups
            )
            power_values.append(p)

        results = {
            'test_type': 'One-way ANOVA',
            'required_sample_size_per_group': int(np.ceil(sample_size)),
            'total_sample_size': int(np.ceil(sample_size * k_groups)),
            'effect_size_f': effect_size,
            'effect_size_eta_squared': eta_squared,
            'k_groups': k_groups,
            'power': power,
            'alpha': alpha,
            'power_curve': {
                'sample_sizes': sample_sizes,
                'power_values': power_values
            },
            'interpretation': self._interpret_effect_size_f(effect_size)
        }

        self._print_power_summary(results)

        return results

    def proportion_power_analysis(self, effect_size, alpha=0.05, power=0.8,
                                 baseline_rate=None, treatment_rate=None, **kwargs):
        """
        Proportion test power analysis

        Parameters:
        -----------
        effect_size : float
            Either absolute difference in proportions or Cohen's h
        alpha : float
            Significance level
        power : float
            Desired power
        baseline_rate : float, optional
            Baseline proportion (if not using Cohen's h)
        treatment_rate : float, optional
            Treatment proportion (if not using Cohen's h)

        Returns:
        --------
        dict : Power analysis results
        """

        # Convert to proportions if needed
        if baseline_rate is not None and treatment_rate is not None:
            p1 = baseline_rate
            p2 = treatment_rate
            h = proportion_effectsize(p1, p2)
        else:
            # Assume effect_size is absolute difference
            p1 = baseline_rate if baseline_rate else 0.1
            p2 = p1 + effect_size
            p2 = max(0, min(1, p2))
            h = proportion_effectsize(p1, p2)

        # Calculate sample size using normal approximation
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(power)

        # Pooled proportion
        p_pooled = (p1 + p2) / 2

        # Sample size calculation
        if abs(p1 - p2) > 0:
            n = ((z_alpha * np.sqrt(2 * p_pooled * (1 - p_pooled)) +
                  z_beta * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / (p1 - p2) ** 2
        else:
            n = np.inf

        # Generate power curve
        sample_sizes = np.arange(50, int(min(n * 2, 10000)), 50)
        power_values = []
        for size in sample_sizes:
            se_pooled = np.sqrt(2 * p_pooled * (1 - p_pooled) / size)
            se_unpooled = np.sqrt(p1 * (1 - p1) / size + p2 * (1 - p2) / size)
            z = (p2 - p1) / se_unpooled
            p_val = 1 - stats.norm.cdf(z - z_alpha)
            power_values.append(p_val)

        results = {
            'test_type': 'Proportion test',
            'required_sample_size_per_group': int(np.ceil(n)),
            'total_sample_size': int(np.ceil(n * 2)),
            'baseline_proportion': p1,
            'treatment_proportion': p2,
            'absolute_difference': p2 - p1,
            'relative_lift': ((p2 - p1) / p1 * 100) if p1 > 0 else np.inf,
            'effect_size_h': h,
            'power': power,
            'alpha': alpha,
            'power_curve': {
                'sample_sizes': sample_sizes,
                'power_values': power_values
            }
        }

        self._print_power_summary(results)

        return results

    def correlation_power_analysis(self, effect_size, alpha=0.05, power=0.8, **kwargs):
        """
        Correlation power analysis

        Parameters:
        -----------
        effect_size : float
            Expected correlation coefficient (r)
        alpha : float
            Significance level
        power : float
            Desired power

        Returns:
        --------
        dict : Power analysis results
        """

        # Sample size for correlation
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(power)

        # Fisher's z transformation
        if abs(effect_size) < 1:
            z_r = 0.5 * np.log((1 + effect_size) / (1 - effect_size))
        else:
            z_r = np.inf

        # Sample size
        if z_r != 0:
            n = ((z_alpha + z_beta) / z_r) ** 2 + 3
        else:
            n = np.inf

        # Generate power curve
        sample_sizes = np.arange(10, int(min(n * 2, 1000)), 10)
        power_values = []
        for size in sample_sizes:
            se = 1 / np.sqrt(size - 3)
            z_stat = z_r / se
            p_val = 1 - stats.norm.cdf(z_stat - z_alpha)
            power_values.append(p_val)

        results = {
            'test_type': 'Correlation',
            'required_sample_size': int(np.ceil(n)),
            'correlation_coefficient': effect_size,
            'power': power,
            'alpha': alpha,
            'fishers_z': z_r,
            'power_curve': {
                'sample_sizes': sample_sizes,
                'power_values': power_values
            },
            'interpretation': self._interpret_correlation(effect_size)
        }

        self._print_power_summary(results)

        return results

    def regression_power_analysis(self, effect_size, alpha=0.05, power=0.8,
                                 n_predictors=1, **kwargs):
        """
        Multiple regression power analysis

        Parameters:
        -----------
        effect_size : float
            Effect size f² (Cohen's f-squared)
        alpha : float
            Significance level
        power : float
            Desired power
        n_predictors : int
            Number of predictors in model

        Returns:
        --------
        dict : Power analysis results
        """

        # Effect size f² to R²
        r_squared = effect_size / (1 + effect_size)

        # Degrees of freedom
        df1 = n_predictors

        # Critical F value (approximation)
        f_alpha = stats.f.ppf(1 - alpha, df1, 1000)

        # Non-centrality parameter for target power
        from scipy.stats import ncf
        lambda_power = ncf.ppf(power, df1, 1000, f_alpha)

        # Sample size
        if effect_size > 0:
            n = lambda_power / effect_size + n_predictors + 1
        else:
            n = np.inf

        results = {
            'test_type': 'Multiple Regression',
            'required_sample_size': int(np.ceil(n)),
            'effect_size_f2': effect_size,
            'r_squared': r_squared,
            'n_predictors': n_predictors,
            'power': power,
            'alpha': alpha,
            'interpretation': self._interpret_effect_size_f2(effect_size)
        }

        self._print_power_summary(results)

        return results

    def minimum_detectable_effect(self, test_type, sample_size, alpha=0.05, power=0.8, **kwargs):
        """
        Calculate minimum detectable effect for given sample size

        Parameters:
        -----------
        test_type : str
            Type of statistical test
        sample_size : int
            Available sample size
        alpha : float
            Significance level
        power : float
            Desired power
        **kwargs : additional test-specific parameters

        Returns:
        --------
        float : Minimum detectable effect size
        """

        if test_type == 'ttest':
            power_calc = TTestPower()
            mde = power_calc.solve_power(
                power=power,
                nobs1=sample_size,
                alpha=alpha,
                alternative=kwargs.get('alternative', 'two-sided')
            )

        elif test_type == 'proportion':
            # Simplified calculation for proportion test MDE
            z_alpha = stats.norm.ppf(1 - alpha/2)
            z_beta = stats.norm.ppf(power)
            baseline_rate = kwargs.get('baseline_rate', 0.1)

            mde = (z_alpha + z_beta) * np.sqrt(2 * baseline_rate * (1 - baseline_rate)) / np.sqrt(sample_size)

        elif test_type == 'correlation':
            # For correlation
            z_alpha = stats.norm.ppf(1 - alpha/2)
            z_beta = stats.norm.ppf(power)
            z_r = (z_alpha + z_beta) / np.sqrt(sample_size - 3)

            # Inverse Fisher transformation
            mde = (np.exp(2 * z_r) - 1) / (np.exp(2 * z_r) + 1)

        else:
            raise ValueError(f"MDE calculation not implemented for {test_type}")

        print(f"\nMinimum Detectable Effect:")
        print(f"  Test: {test_type}")
        print(f"  Sample size: {sample_size}")
        print(f"  MDE: {mde:.4f}")
        print(f"  Power: {power}")
        print(f"  Alpha: {alpha}")

        return mde

    def sensitivity_analysis(self, test_type, base_params, vary_param, param_range):
        """
        Perform sensitivity analysis on power calculations

        Parameters:
        -----------
        test_type : str
            Type of test
        base_params : dict
            Base parameters for power analysis
        vary_param : str
            Parameter to vary ('effect_size', 'sample_size', 'alpha', 'power')
        param_range : array-like
            Range of values for varied parameter

        Returns:
        --------
        DataFrame : Sensitivity analysis results
        """

        results = []

        for value in param_range:
            params = base_params.copy()
            params[vary_param] = value

            if vary_param == 'sample_size':
                # Calculate power for given sample size
                if test_type == 'ttest':
                    power_calc = TTestPower()
                    power = power_calc.solve_power(
                        nobs1=value,
                        effect_size=params['effect_size'],
                        alpha=params['alpha']
                    )
                    results.append({'sample_size': value, 'power': power})
            elif vary_param == 'effect_size':
                # Calculate sample size for given effect size
                analysis = self.comprehensive_power_analysis(test_type, **params)
                results.append({
                    'effect_size': value,
                    'sample_size': analysis.get('required_sample_size_per_group',
                                               analysis.get('required_sample_size', 0))
                })

        results_df = pd.DataFrame(results)

        print(f"\nSensitivity Analysis: Varying {vary_param}")
        print(results_df)

        return results_df

    def create_power_visualizations(self, power_results):
        """
        Create comprehensive power analysis visualizations

        Parameters:
        -----------
        power_results : dict
            Results from power analysis

        Returns:
        --------
        matplotlib.figure.Figure : Figure with power plots
        """

        fig, axes = plt.subplots(1, 2, figsize=(15, 5))

        # Power vs Sample Size
        if 'power_curve' in power_results:
            power_curve = power_results['power_curve']
            axes[0].plot(power_curve['sample_sizes'], power_curve['power_values'],
                        linewidth=2, color='#2E86AB')
            axes[0].axhline(y=0.8, color='red', linestyle='--', linewidth=1.5,
                          label='Target Power = 0.8')

            sample_size_key = ('required_sample_size_per_group' if 'required_sample_size_per_group' in power_results
                              else 'required_sample_size')

            axes[0].axvline(x=power_results[sample_size_key], color='green',
                          linestyle='--', linewidth=1.5,
                          label=f'Required N = {power_results[sample_size_key]}')
            axes[0].set_xlabel('Sample Size per Group', fontsize=12)
            axes[0].set_ylabel('Statistical Power', fontsize=12)
            axes[0].set_title('Power vs Sample Size', fontsize=14, fontweight='bold')
            axes[0].legend(fontsize=10)
            axes[0].grid(True, alpha=0.3)
            axes[0].set_ylim([0, 1])

        # Power vs Effect Size (if available)
        if 'effect_size_curve' in power_results:
            effect_curve = power_results['effect_size_curve']
            axes[1].plot(effect_curve['effect_sizes'], effect_curve['power_values'],
                        linewidth=2, color='#A23B72')
            axes[1].axhline(y=0.8, color='red', linestyle='--', linewidth=1.5,
                          label='Target Power = 0.8')

            effect_size_key = next((k for k in power_results.keys() if 'effect_size' in k.lower()), None)
            if effect_size_key:
                axes[1].axvline(x=power_results[effect_size_key], color='green',
                              linestyle='--', linewidth=1.5,
                              label=f'Target Effect Size = {power_results[effect_size_key]:.3f}')

            axes[1].set_xlabel('Effect Size', fontsize=12)
            axes[1].set_ylabel('Statistical Power', fontsize=12)
            axes[1].set_title('Power vs Effect Size', fontsize=14, fontweight='bold')
            axes[1].legend(fontsize=10)
            axes[1].grid(True, alpha=0.3)
            axes[1].set_ylim([0, 1])

        plt.tight_layout()
        return fig

    def _interpret_effect_size_cohens_d(self, d):
        """Interpret Cohen's d effect size"""
        if abs(d) < 0.2:
            return "Negligible effect"
        elif abs(d) < 0.5:
            return "Small effect"
        elif abs(d) < 0.8:
            return "Medium effect"
        else:
            return "Large effect"

    def _interpret_effect_size_f(self, f):
        """Interpret Cohen's f effect size"""
        if f < 0.1:
            return "Negligible effect"
        elif f < 0.25:
            return "Small effect"
        elif f < 0.4:
            return "Medium effect"
        else:
            return "Large effect"

    def _interpret_effect_size_f2(self, f2):
        """Interpret Cohen's f² effect size"""
        if f2 < 0.02:
            return "Negligible effect"
        elif f2 < 0.15:
            return "Small effect"
        elif f2 < 0.35:
            return "Medium effect"
        else:
            return "Large effect"

    def _interpret_correlation(self, r):
        """Interpret correlation coefficient"""
        r_abs = abs(r)
        if r_abs < 0.1:
            return "Negligible correlation"
        elif r_abs < 0.3:
            return "Small correlation"
        elif r_abs < 0.5:
            return "Medium correlation"
        else:
            return "Large correlation"

    def _print_power_summary(self, results):
        """Print formatted power analysis summary"""

        print("\n" + "="*60)
        print("POWER ANALYSIS RESULTS")
        print("="*60)
        print(f"\nTest Type: {results['test_type']}")

        if 'required_sample_size_per_group' in results:
            print(f"Required Sample Size per Group: {results['required_sample_size_per_group']}")
            if 'total_sample_size' in results:
                print(f"Total Sample Size: {results['total_sample_size']}")
        elif 'required_sample_size' in results:
            print(f"Required Sample Size: {results['required_sample_size']}")

        # Print effect size info
        for key in results:
            if 'effect_size' in key.lower() and not isinstance(results[key], dict):
                print(f"{key.replace('_', ' ').title()}: {results[key]:.4f}")

        if 'interpretation' in results:
            print(f"Interpretation: {results['interpretation']}")

        print(f"\nPower: {results['power']}")
        print(f"Alpha: {results['alpha']}")
        print("="*60)

# Perform power analysis
power_analyzer = PowerAnalyzer()

# Main power analysis
power_results = power_analyzer.comprehensive_power_analysis(
    test_type='[TEST_TYPE]',
    effect_size=[EFFECT_SIZE],
    alpha=[ALPHA_LEVEL],
    power=[STATISTICAL_POWER],
    # Additional test-specific parameters
    k_groups=[K_GROUPS] if '[TEST_TYPE]' == 'anova' else None,
    n_predictors=[N_PREDICTORS] if '[TEST_TYPE]' == 'regression' else None,
    baseline_rate=[BASELINE_RATE] if '[TEST_TYPE]' == 'proportion' else None
)

# Calculate MDE if sample size is fixed
if '[FIXED_SAMPLE_SIZE]':
    mde = power_analyzer.minimum_detectable_effect(
        test_type='[TEST_TYPE]',
        sample_size=[FIXED_SAMPLE_SIZE],
        alpha=[ALPHA_LEVEL],
        power=[STATISTICAL_POWER]
    )

# Create visualizations
fig = power_analyzer.create_power_visualizations(power_results)
plt.savefig('[OUTPUT_PATH]/power_analysis.png', dpi=300, bbox_inches='tight')
```

OUTPUT REQUIREMENTS:

1. **Sample Size Recommendation**
   - Required sample size with justification
   - Total participants needed
   - Expected recruitment timeline
   - Dropout/attrition buffer

2. **Power Analysis Documentation**
   - Statistical test specified
   - Effect size assumptions
   - Power curves
   - Sensitivity analyses

3. **Effect Size Justification**
   - Source of effect size estimate (pilot, literature, MCID)
   - Practical vs. statistical significance
   - Range of plausible effects

4. **Assumptions and Limitations**
   - Distributional assumptions
   - Multiple testing considerations
   - Interim analysis impact
   - Subgroup analysis plans
```

## Variables

### Test Configuration
- [TEST_TYPE] - Statistical test ('ttest', 'anova', 'proportion', 'correlation', 'regression')
- [EFFECT_SIZE] - Expected effect size
- [STATISTICAL_POWER] - Desired power (typically 0.8 or 0.9)
- [ALPHA_LEVEL] - Significance level (typically 0.05)
- [ALTERNATIVE] - Hypothesis type ('two-sided', 'larger', 'smaller')

### Study Parameters
- [K_GROUPS] - Number of groups (for ANOVA)
- [N_PREDICTORS] - Number of predictors (for regression)
- [BASELINE_RATE] - Baseline proportion (for proportion tests)
- [TREATMENT_RATE] - Treatment proportion (for proportion tests)
- [STUDY_CONSTRAINTS] - Budget, timeline, or other constraints

### Fixed Parameters
- [FIXED_SAMPLE_SIZE] - Fixed sample size (for MDE calculation)
- [OUTPUT_PATH] - Path for saving visualizations

## Best Practices

1. **Power of 0.8 is standard** - Higher power (0.9) may be needed for critical decisions
2. **Plan for attrition** - Inflate sample size by expected dropout rate
3. **Use conservative estimates** - Better to over than under-power
4. **Document assumptions** - Effect size estimates and their sources
5. **Consider practical significance** - Smallest effect that matters
6. **Account for multiple testing** - Adjust alpha or power for multiple outcomes
7. **Pilot when possible** - Refine effect size estimates with pilot data

## Usage Examples

### Example 1: Clinical Trial (Two-Sample T-test)
```
TEST_TYPE: "ttest"
EFFECT_SIZE: 0.5
STATISTICAL_POWER: 0.8
ALPHA_LEVEL: 0.05
ALTERNATIVE: "two-sided"
```

### Example 2: A/B Test (Proportion Test)
```
TEST_TYPE: "proportion"
BASELINE_RATE: 0.10
TREATMENT_RATE: 0.12
STATISTICAL_POWER: 0.8
ALPHA_LEVEL: 0.05
```

### Example 3: Multi-group Comparison (ANOVA)
```
TEST_TYPE: "anova"
EFFECT_SIZE: 0.25
K_GROUPS: 4
STATISTICAL_POWER: 0.8
ALPHA_LEVEL: 0.05
```
