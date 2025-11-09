---
title: Factorial & Fractional Factorial Designs
category: data-analytics/Research Analytics
tags: [automation, data-analytics, data-science, design, research, template]
use_cases:
  - Designing and analyzing factorial experiments to test multiple factors simultaneously
  - Understanding and estimating interaction effects between factors
  - Implementing full and fractional factorial designs for efficient experimentation
related_templates:
  - experimental-design-overview.md
  - experiment-design-principles.md
  - doe-analysis-methods.md
last_updated: 2025-11-09
---

# Factorial & Fractional Factorial Designs

## Purpose
Design and analyze factorial experiments to efficiently test multiple factors and their interactions simultaneously, enabling comprehensive understanding of how factors combine to affect outcomes.

## Template

```
You are a factorial design expert. Create a factorial experimental design for [RESEARCH_OBJECTIVE] testing [N_FACTORS] factors: [FACTOR_LIST] with [FACTOR_LEVELS] levels each to measure [PRIMARY_OUTCOME] and identify interaction effects.

FACTORIAL DESIGN FRAMEWORK:

Research Context:
- Objective: [RESEARCH_OBJECTIVE]
- Factors to test: [FACTOR_LIST]
- Factor levels: [FACTOR_LEVELS]
- Primary outcome: [PRIMARY_OUTCOME]
- Participants per cell: [N_PER_CELL]

### Factorial Design Types

1. **Full Factorial**: Test all combinations of all factors
   - 2^k design for k factors at 2 levels
   - 3^k design for k factors at 3 levels
   - Mixed factorial for different levels per factor

2. **Fractional Factorial**: Test subset of combinations
   - 2^(k-p) design tests 1/(2^p) of full factorial
   - Efficient for screening many factors
   - Some interactions confounded

3. **Mixed-Level Factorial**: Different factors have different numbers of levels
   - Common in practice
   - Flexible design structure

IMPLEMENTATION:
```python
import numpy as np
import pandas as pd
from itertools import product, combinations
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

class FactorialDesigner:
    def __init__(self):
        self.designs = {}
        self.analysis_results = {}

    def create_full_factorial(self, factors, factor_levels, n_per_cell=1, randomize=True):
        """
        Create full factorial design

        Parameters:
        -----------
        factors : list
            Names of factors (e.g., ['temperature', 'pressure', 'catalyst'])
        factor_levels : dict
            Number of levels per factor (e.g., {'temperature': 2, 'pressure': 3, 'catalyst': 2})
        n_per_cell : int
            Number of replicates per combination
        randomize : bool
            Whether to randomize run order

        Returns:
        --------
        dict : Design specification and run table
        """

        # Generate all factor combinations
        factor_combinations = list(product(*[range(levels) for levels in factor_levels.values()]))
        n_conditions = len(factor_combinations)
        total_runs = n_conditions * n_per_cell

        design = {
            'type': f'{len(factors)}-way Full Factorial',
            'factors': factors,
            'factor_levels': factor_levels,
            'n_conditions': n_conditions,
            'replicates_per_condition': n_per_cell,
            'total_runs': total_runs,
            'design_resolution': 'Full',
            'estimable_effects': self._get_estimable_effects(factors)
        }

        # Create design matrix
        design_matrix = self._create_design_matrix(factors, factor_levels, n_per_cell)

        # Randomize run order if requested
        if randomize:
            design_matrix = design_matrix.sample(frac=1).reset_index(drop=True)
            design_matrix['run_order'] = range(1, len(design_matrix) + 1)

        design['design_matrix'] = design_matrix

        print(f"\nFull Factorial Design Created:")
        print(f"  Factors: {len(factors)}")
        print(f"  Conditions: {n_conditions}")
        print(f"  Replicates: {n_per_cell}")
        print(f"  Total Runs: {total_runs}")
        print(f"\nFactor Configuration:")
        for factor, levels in factor_levels.items():
            print(f"  {factor}: {levels} levels")

        return design

    def create_fractional_factorial(self, factors, resolution='IV', replicate=1):
        """
        Create fractional factorial design

        Parameters:
        -----------
        factors : int
            Number of factors (assumes 2-level factors)
        resolution : str
            Design resolution ('III', 'IV', 'V')
            - III: Main effects confounded with 2-way interactions
            - IV: Main effects clear, some 2-way confounded
            - V: Main effects and 2-way interactions clear
        replicate : int
            Number of replicates

        Returns:
        --------
        dict : Fractional factorial design
        """

        # Determine fraction based on resolution
        if resolution == 'III':
            fraction_exp = max(1, factors - 3)
        elif resolution == 'IV':
            fraction_exp = max(1, factors - 4)
        elif resolution == 'V':
            fraction_exp = max(1, factors - 5)
        else:
            fraction_exp = 1

        n_runs = 2**(factors - fraction_exp) * replicate

        design = {
            'type': f'2^({factors}-{fraction_exp}) Fractional Factorial',
            'n_factors': factors,
            'resolution': resolution,
            'fraction': f'1/{2**fraction_exp}',
            'runs_per_replicate': 2**(factors - fraction_exp),
            'total_runs': n_runs,
            'replicates': replicate
        }

        # Create design matrix using standard fractional factorial generators
        base_design = self._generate_fractional_design(factors, fraction_exp)

        # Replicate if needed
        if replicate > 1:
            design_matrix = pd.concat([base_design.copy() for _ in range(replicate)], ignore_index=True)
        else:
            design_matrix = base_design

        design['design_matrix'] = design_matrix
        design['confounding_pattern'] = self._get_confounding_pattern(factors, fraction_exp, resolution)

        print(f"\nFractional Factorial Design Created:")
        print(f"  Design: 2^{factors}-{fraction_exp}")
        print(f"  Resolution: {resolution}")
        print(f"  Runs: {n_runs}")
        print(f"  Fraction: {design['fraction']}")

        return design

    def _create_design_matrix(self, factors, factor_levels, n_per_cell):
        """Create design matrix for factorial design"""

        design_matrix = []
        condition_id = 1

        # Generate all combinations
        for combination in product(*[range(levels) for levels in factor_levels.values()]):
            # Replicate each combination
            for rep in range(n_per_cell):
                row = {
                    'condition_id': condition_id,
                    'run_id': len(design_matrix) + 1,
                    'replicate': rep + 1
                }

                # Add factor levels
                for i, factor in enumerate(factors):
                    row[factor] = combination[i]

                design_matrix.append(row)

            condition_id += 1

        return pd.DataFrame(design_matrix)

    def _generate_fractional_design(self, n_factors, fraction_exp):
        """Generate fractional factorial design matrix"""

        # Number of base factors (not generated)
        n_base = n_factors - fraction_exp
        n_runs = 2**n_base

        # Create base design (full factorial for base factors)
        base_matrix = np.zeros((n_runs, n_factors), dtype=int)

        # Generate base factors
        for i in range(n_base):
            pattern = np.tile([0]*2**(n_base-i-1) + [1]*2**(n_base-i-1), 2**i)
            base_matrix[:, i] = pattern

        # Generate additional factors using generators
        # Standard generators for common designs
        if n_factors - n_base >= 1:
            # Simple generators: ABC, ABCD, etc.
            for i in range(n_base, n_factors):
                # Use XOR of previous columns as generator
                gen_cols = list(range(min(i, n_base)))
                base_matrix[:, i] = np.bitwise_xor.reduce(base_matrix[:, gen_cols], axis=1)

        # Convert to DataFrame with factor names
        factor_names = [f'Factor_{chr(65+i)}' for i in range(n_factors)]
        design_df = pd.DataFrame(base_matrix, columns=factor_names)

        return design_df

    def _get_estimable_effects(self, factors):
        """Generate list of all estimable effects"""

        effects = []

        # Main effects
        effects.extend(factors)

        # Two-way interactions
        for combo in combinations(factors, 2):
            effects.append(' × '.join(combo))

        # Three-way and higher interactions
        if len(factors) >= 3:
            for r in range(3, len(factors) + 1):
                for combo in combinations(factors, r):
                    effects.append(' × '.join(combo))

        return effects

    def _get_confounding_pattern(self, n_factors, fraction_exp, resolution):
        """Describe confounding pattern for fractional factorial"""

        patterns = []

        if resolution == 'III':
            patterns.append("Main effects confounded with two-way interactions")
            patterns.append("Some two-way interactions confounded with each other")

        elif resolution == 'IV':
            patterns.append("Main effects clear (not confounded)")
            patterns.append("Two-way interactions confounded with other two-way interactions")
            patterns.append("Main effects confounded with three-way+ interactions")

        elif resolution == 'V':
            patterns.append("Main effects clear")
            patterns.append("Two-way interactions clear")
            patterns.append("Two-way interactions confounded with three-way+ interactions")

        return patterns

    def add_center_points(self, design_matrix, n_center=3):
        """
        Add center points to factorial design

        Center points help detect curvature and assess pure error
        """

        # Calculate center values (midpoint for each factor)
        center_row = {}
        for col in design_matrix.columns:
            if col not in ['condition_id', 'run_id', 'replicate', 'run_order']:
                center_row[col] = design_matrix[col].max() / 2

        # Create center point runs
        center_points = []
        for i in range(n_center):
            center_run = center_row.copy()
            center_run['condition_id'] = 0  # Special ID for center points
            center_run['run_id'] = len(design_matrix) + i + 1
            center_run['replicate'] = i + 1
            center_points.append(center_run)

        # Append to design
        center_df = pd.DataFrame(center_points)
        augmented_design = pd.concat([design_matrix, center_df], ignore_index=True)

        print(f"\nAdded {n_center} center point runs")

        return augmented_design

    def analyze_factorial_effects(self, data, factors, outcome, include_interactions=True):
        """
        Analyze factorial design data

        Parameters:
        -----------
        data : DataFrame
            Experimental data with factors and outcome
        factors : list
            List of factor column names
        outcome : str
            Outcome variable name
        include_interactions : bool
            Whether to include interaction terms

        Returns:
        --------
        dict : Analysis results
        """

        # Build formula
        if include_interactions:
            # Full model with all interactions
            formula = f"{outcome} ~ {' * '.join(factors)}"
        else:
            # Main effects only
            formula = f"{outcome} ~ {' + '.join(factors)}"

        # Fit model
        model = ols(formula, data=data).fit()

        # ANOVA table
        anova_table = anova_lm(model)

        # Effect sizes
        effect_sizes = {}
        for factor in factors:
            if factor in model.params:
                effect_sizes[factor] = model.params[factor]

        # Interaction effects
        interaction_effects = {}
        if include_interactions:
            for param in model.params.index:
                if ':' in param:  # Interaction term
                    interaction_effects[param] = model.params[param]

        results = {
            'model': model,
            'anova_table': anova_table,
            'r_squared': model.rsquared,
            'adj_r_squared': model.rsquared_adj,
            'main_effects': effect_sizes,
            'interaction_effects': interaction_effects,
            'significant_effects': self._identify_significant_effects(anova_table)
        }

        self._print_analysis_summary(results)

        return results

    def _identify_significant_effects(self, anova_table, alpha=0.05):
        """Identify statistically significant effects"""

        significant = []
        for effect in anova_table.index:
            if effect != 'Residual' and anova_table.loc[effect, 'PR(>F)'] < alpha:
                significant.append({
                    'effect': effect,
                    'p_value': anova_table.loc[effect, 'PR(>F)'],
                    'f_value': anova_table.loc[effect, 'F']
                })

        return significant

    def _print_analysis_summary(self, results):
        """Print analysis summary"""

        print("\n" + "="*60)
        print("FACTORIAL DESIGN ANALYSIS RESULTS")
        print("="*60)

        print(f"\nModel Fit:")
        print(f"  R-squared: {results['r_squared']:.4f}")
        print(f"  Adjusted R-squared: {results['adj_r_squared']:.4f}")

        print(f"\nSignificant Effects (α = 0.05):")
        for effect in results['significant_effects']:
            print(f"  {effect['effect']}: F = {effect['f_value']:.2f}, p = {effect['p_value']:.4f}")

        if not results['significant_effects']:
            print("  No significant effects detected")

    def create_interaction_plot(self, data, factor1, factor2, outcome, ax=None):
        """
        Create interaction plot for two factors

        Parameters:
        -----------
        data : DataFrame
            Experimental data
        factor1 : str
            First factor (x-axis)
        factor2 : str
            Second factor (lines)
        outcome : str
            Outcome variable (y-axis)
        """

        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))

        # Calculate means for each combination
        means = data.groupby([factor1, factor2])[outcome].mean().reset_index()

        # Create plot
        for level2 in means[factor2].unique():
            subset = means[means[factor2] == level2]
            ax.plot(subset[factor1], subset[outcome], marker='o', label=f'{factor2}={level2}')

        ax.set_xlabel(factor1)
        ax.set_ylabel(outcome)
        ax.set_title(f'Interaction Plot: {factor1} × {factor2}')
        ax.legend()
        ax.grid(True, alpha=0.3)

        return ax

    def create_main_effects_plot(self, data, factors, outcome):
        """
        Create main effects plot for all factors

        Shows average outcome at each level of each factor
        """

        n_factors = len(factors)
        fig, axes = plt.subplots(1, n_factors, figsize=(5*n_factors, 4))

        if n_factors == 1:
            axes = [axes]

        for i, factor in enumerate(factors):
            means = data.groupby(factor)[outcome].agg(['mean', 'std']).reset_index()

            axes[i].errorbar(means[factor], means['mean'], yerr=means['std'],
                           marker='o', capsize=5, capthick=2)
            axes[i].set_xlabel(f'{factor} Level')
            axes[i].set_ylabel(outcome)
            axes[i].set_title(f'Main Effect: {factor}')
            axes[i].grid(True, alpha=0.3)

        plt.tight_layout()
        return fig

# Initialize factorial designer
factorial = FactorialDesigner()

# Create design based on specifications
if '[DESIGN_TYPE]' == 'full_factorial':
    design = factorial.create_full_factorial(
        factors=[FACTORS],
        factor_levels=[FACTOR_LEVELS],
        n_per_cell=[N_PER_CELL],
        randomize=True
    )

elif '[DESIGN_TYPE]' == 'fractional_factorial':
    design = factorial.create_fractional_factorial(
        factors=[N_FACTORS],
        resolution='[RESOLUTION]',  # III, IV, or V
        replicate=[N_REPLICATES]
    )

# Optional: Add center points for response surface
if '[ADD_CENTER_POINTS]':
    design['design_matrix'] = factorial.add_center_points(
        design['design_matrix'],
        n_center=[N_CENTER_POINTS]
    )

# After data collection, analyze results
if '[DATA_COLLECTED]':
    results = factorial.analyze_factorial_effects(
        data=experiment_data,
        factors=[FACTORS],
        outcome='[OUTCOME_VARIABLE]',
        include_interactions=True
    )

    # Create visualizations
    factorial.create_main_effects_plot(
        data=experiment_data,
        factors=[FACTORS],
        outcome='[OUTCOME_VARIABLE]'
    )
```

OUTPUT REQUIREMENTS:

1. **Design Specification**
   - Complete factor list with levels
   - Design matrix with all runs
   - Randomized run order
   - Blocking scheme (if applicable)

2. **Effect Estimation**
   - Main effects for all factors
   - Two-way interaction effects
   - Higher-order interactions (if powered)
   - Effect size estimates with confidence intervals

3. **Statistical Analysis**
   - ANOVA table
   - Significance tests for all effects
   - Model diagnostics
   - R-squared and model fit statistics

4. **Visualizations**
   - Main effects plots
   - Interaction plots
   - Pareto chart of effects
   - Residual diagnostics plots

5. **Interpretation**
   - Which factors are significant
   - How factors interact
   - Optimal factor settings
   - Recommendations for follow-up experiments
```

## Variables

### Design Configuration
- [RESEARCH_OBJECTIVE] - Research objective
- [N_FACTORS] - Number of factors to test
- [FACTOR_LIST] - List of factor names (e.g., ['temperature', 'pressure', 'catalyst'])
- [FACTOR_LEVELS] - Levels per factor (e.g., {'temperature': 2, 'pressure': 3, 'catalyst': 2})
- [N_PER_CELL] - Replicates per condition
- [PRIMARY_OUTCOME] - Primary outcome measure

### Fractional Factorial
- [DESIGN_TYPE] - 'full_factorial' or 'fractional_factorial'
- [RESOLUTION] - Design resolution ('III', 'IV', 'V')
- [N_REPLICATES] - Number of complete replicates
- [ADD_CENTER_POINTS] - Whether to add center points (True/False)
- [N_CENTER_POINTS] - Number of center point runs

### Analysis
- [DATA_COLLECTED] - Whether data has been collected (True/False)
- [OUTCOME_VARIABLE] - Name of outcome variable in data
- [FACTORS] - List of factor column names in data

## Best Practices

1. **Start with screening designs** - Use fractional factorials to identify important factors
2. **Follow up with full factorials** - Investigate important factors in detail
3. **Replicate appropriately** - Multiple replicates enable error estimation
4. **Randomize run order** - Protects against time-related confounds
5. **Include center points** - Detect curvature and estimate pure error
6. **Check for interactions** - Don't assume factors act independently
7. **Validate assumptions** - Check residuals for normality and homoscedasticity

## Usage Examples

### Example 1: 2³ Full Factorial (Manufacturing)
```
RESEARCH_OBJECTIVE: "Optimize injection molding process"
DESIGN_TYPE: "full_factorial"
FACTORS: "['temperature', 'pressure', 'cooling_time']"
FACTOR_LEVELS: "{'temperature': 2, 'pressure': 2, 'cooling_time': 2}"
N_PER_CELL: 3
PRIMARY_OUTCOME: "part_strength"
```

### Example 2: 2⁷⁻³ Fractional Factorial (Product Testing)
```
RESEARCH_OBJECTIVE: "Screen 7 design factors for new product"
DESIGN_TYPE: "fractional_factorial"
N_FACTORS: 7
RESOLUTION: "IV"
N_REPLICATES: 2
PRIMARY_OUTCOME: "customer_satisfaction"
```

### Example 3: Mixed-Level Factorial (Marketing)
```
RESEARCH_OBJECTIVE: "Test ad creative elements"
DESIGN_TYPE: "full_factorial"
FACTORS: "['headline', 'image', 'cta_button']"
FACTOR_LEVELS: "{'headline': 3, 'image': 2, 'cta_button': 2}"
N_PER_CELL: 5000
PRIMARY_OUTCOME: "click_through_rate"
```
