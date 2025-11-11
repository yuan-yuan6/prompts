---
title: Quasi-Experimental Design Template
category: data-analytics/Research Analytics
tags: ['research', 'quasi-experimental', 'causal-inference', 'statistics']
use_cases:
  - Design quasi-experimental studies including difference-in-differences, regression discontinuity, and propensity score matching.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Quasi-Experimental Design Template

## Purpose
Design quasi-experimental studies including difference-in-differences, regression discontinuity, and propensity score matching.

## Quick Start

### For Researchers

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific design needs
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
- Design quasi-experimental studies including difference-in-differences, regression discontinuity, and propensity score matching.
- Project-specific implementations
- Research and analysis workflows



## Template

### Design Selection and Setup
```python
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split
from statsmodels.stats.power import TTestPower, ttest_power
from statsmodels.stats.proportion import proportions_ztest, proportion_effectsize
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations, product
import random

class ExperimentalDesigner:
    def __init__(self):
        self.design_types = {
            'randomized_controlled_trial': self.setup_rct,
            'ab_test': self.setup_ab_test,
            'factorial_design': self.setup_factorial_design,
            'crossover_design': self.setup_crossover_design,
            'cluster_randomized_trial': self.setup_cluster_trial,
            'stepped_wedge': self.setup_stepped_wedge,
            'quasi_experimental': self.setup_quasi_experimental,
            'regression_discontinuity': self.setup_regression_discontinuity
        }
        self.randomization_methods = {
            'simple': self.simple_randomization,
            'block': self.block_randomization,
            'stratified': self.stratified_randomization,
            'cluster': self.cluster_randomization,
            'adaptive': self.adaptive_randomization
        }

    def setup_rct(self, n_participants, treatment_ratio=0.5, stratification_vars=None):
        """Set up Randomized Controlled Trial"""

        design = {
            'type': 'Randomized Controlled Trial',
            'total_participants': n_participants,
            'treatment_allocation_ratio': treatment_ratio,
            'control_size': int(n_participants * (1 - treatment_ratio)),
            'treatment_size': int(n_participants * treatment_ratio),
            'stratification_variables': stratification_vars,
            'randomization_level': 'individual',
            'blinding': '[BLINDING_TYPE]',  # single, double, triple, none
            'allocation_concealment': True
        }

        # Create participant allocation
        participants = pd.DataFrame({
            'participant_id': range(1, n_participants + 1),
            'treatment_group': np.random.choice(
                ['control', 'treatment'],
                size=n_participants,
                p=[1-treatment_ratio, treatment_ratio]
            )
        })

        # Add stratification if specified
        if stratification_vars:
            for var in stratification_vars:
                participants[var] = np.random.choice(
                    [f'[VAR]_low', f'[VAR]_high'],
                    size=n_participants
                )

        design['allocation_table'] = participants
        return design

    def setup_ab_test(self, n_users, variants=['A', 'B'], traffic_allocation=None):
        """Set up A/B Test design"""

        if traffic_allocation is None:
            traffic_allocation = [1/len(variants)] * len(variants)

        design = {
            'type': 'A/B Test',
            'variants': variants,
            'traffic_allocation': traffic_allocation,
            'total_users': n_users,
            'randomization_unit': '[RANDOMIZATION_UNIT]',  # user, session, page_view
            'minimum_detectable_effect': '[MDE]',
            'statistical_power': 0.8,
            'significance_level': 0.05,
            'multiple_testing_correction': '[CORRECTION_METHOD]'
        }

        # Allocate users to variants
        user_allocation = pd.DataFrame({
            'user_id': range(1, n_users + 1),
            'variant': np.random.choice(
                variants,
                size=n_users,
                p=traffic_allocation
            )
        })

        design['user_allocation'] = user_allocation
        design['variant_sizes'] = user_allocation['variant'].value_counts().to_dict()

        return design

    def setup_factorial_design(self, factors, factor_levels, n_per_cell=20):
        """Set up Factorial Design"""

        # Generate all factor combinations
        factor_combinations = list(product(*[range(levels) for levels in factor_levels.values()]))
        n_conditions = len(factor_combinations)
        total_n = n_conditions * n_per_cell

        design = {
            'type': f'{len(factors)}-way Factorial Design',
            'factors': factors,
            'factor_levels': factor_levels,
            'conditions': n_conditions,
            'participants_per_condition': n_per_cell,
            'total_participants': total_n,
            'design_matrix': self._create_design_matrix(factors, factor_levels, n_per_cell),
            'main_effects': factors,
            'interactions': self._generate_interactions(factors)
        }

        return design

    def setup_crossover_design(self, n_participants, n_periods, treatments, washout_period=True):
        """Set up Crossover Design"""

        # Generate treatment sequences
        sequences = self._generate_crossover_sequences(treatments, n_periods)

        design = {
            'type': 'Crossover Design',
            'n_participants': n_participants,
            'n_periods': n_periods,
            'treatments': treatments,
            'washout_period': washout_period,
            'sequences': sequences,
            'participants_per_sequence': n_participants // len(sequences),
            'carryover_effects': '[CARRYOVER_CONTROL]',
            'period_effects': '[PERIOD_CONTROL]'
        }

        # Assign participants to sequences
        sequence_assignment = []
        for i, seq in enumerate(sequences):
            n_in_seq = n_participants // len(sequences)
            if i < n_participants % len(sequences):
                n_in_seq += 1

            for j in range(n_in_seq):
                participant_id = len(sequence_assignment) + 1
                sequence_assignment.append({
                    'participant_id': participant_id,
                    'sequence': seq,
                    'sequence_id': i + 1
                })

        design['participant_assignment'] = pd.DataFrame(sequence_assignment)
        return design

    def setup_cluster_trial(self, n_clusters, cluster_sizes, intracluster_correlation=0.05):
        """Set up Cluster Randomized Trial"""

        if isinstance(cluster_sizes, int):
            cluster_sizes = [cluster_sizes] * n_clusters

        total_participants = sum(cluster_sizes)

        design = {
            'type': 'Cluster Randomized Trial',
            'n_clusters': n_clusters,
            'cluster_sizes': cluster_sizes,
            'total_participants': total_participants,
            'intracluster_correlation': intracluster_correlation,
            'randomization_level': 'cluster',
            'design_effect': 1 + (np.mean(cluster_sizes) - 1) * intracluster_correlation
        }

        # Randomize clusters to treatment
        cluster_allocation = pd.DataFrame({
            'cluster_id': range(1, n_clusters + 1),
            'cluster_size': cluster_sizes,
            'treatment_group': np.random.choice(
                ['control', 'treatment'],
                size=n_clusters
            )
        })

        design['cluster_allocation'] = cluster_allocation
        design['effective_sample_size'] = total_participants / design['design_effect']

        return design

    def setup_stepped_wedge(self, n_clusters, n_time_periods, randomization_scheme='random'):
        """Set up Stepped Wedge Design"""

        design = {
            'type': 'Stepped Wedge Design',
            'n_clusters': n_clusters,
            'n_time_periods': n_time_periods,
            'randomization_scheme': randomization_scheme,
            'intervention_rollout': 'sequential'
        }

        # Create stepped wedge matrix
        wedge_matrix = np.zeros((n_clusters, n_time_periods))

        if randomization_scheme == 'random':
            # Randomize when each cluster switches
            switch_times = np.random.permutation(range(1, n_time_periods))[:n_clusters]
        else:
            # Uniform distribution of switch times
            switch_times = np.linspace(1, n_time_periods-1, n_clusters, dtype=int)

        for i, switch_time in enumerate(switch_times):
            wedge_matrix[i, switch_time:] = 1

        design['wedge_matrix'] = wedge_matrix
        design['switch_times'] = switch_times

        return design

    def setup_quasi_experimental(self, treatment_assignment_rule, cutoff_variable=None):
        """Set up Quasi-experimental Design"""

        design = {
            'type': 'Quasi-experimental Design',
            'assignment_rule': treatment_assignment_rule,
            'assignment_mechanism': '[ASSIGNMENT_MECHANISM]',
            'threats_to_validity': [
                'selection_bias',
                'confounding',
                'temporal_effects',
                'regression_to_mean'
            ],
            'identification_strategy': '[IDENTIFICATION_STRATEGY]'
        }

        if cutoff_variable:
            design['cutoff_variable'] = cutoff_variable
            design['subtype'] = 'Regression Discontinuity'

        return design

    def setup_regression_discontinuity(self, cutoff_value, assignment_variable, bandwidth=None):
        """Set up Regression Discontinuity Design"""

        design = {
            'type': 'Regression Discontinuity Design',
            'cutoff_value': cutoff_value,
            'assignment_variable': assignment_variable,
            'bandwidth': bandwidth,
            'bandwidth_selection': '[BANDWIDTH_METHOD]',  # IK, CV, MSE-optimal
            'kernel': '[KERNEL_TYPE]',  # rectangular, triangular, epanechnikov
            'continuity_tests': True,
            'density_tests': True,
            'covariate_balance_tests': True
        }

        return design

    def _create_design_matrix(self, factors, factor_levels, n_per_cell):
        """Create design matrix for factorial design"""

        design_matrix = []
        condition_id = 1

        for combination in product(*[range(levels) for levels in factor_levels.values()]):
            for rep in range(n_per_cell):
                row = {'condition_id': condition_id, 'participant_id': len(design_matrix) + 1}

                for i, factor in enumerate(factors):
                    row[factor] = combination[i]

                design_matrix.append(row)

            condition_id += 1

        return pd.DataFrame(design_matrix)

    def _generate_interactions(self, factors):
        """Generate all possible interactions for factorial design"""

        interactions = []
        for r in range(2, len(factors) + 1):
            for combo in combinations(factors, r):
                interactions.append(' × '.join(combo))

        return interactions

    def _generate_crossover_sequences(self, treatments, n_periods):
        """Generate balanced crossover sequences"""

        from itertools import permutations

        # Generate all possible sequences
        all_sequences = list(permutations(treatments, n_periods))

        # For balanced design, select subset that balances carryover effects
        if len(all_sequences) <= 12:  # Use all sequences for small designs
            return all_sequences
        else:
            # Use Latin square approach for larger designs
            return self._latin_square_sequences(treatments, n_periods)

    def _latin_square_sequences(self, treatments, n_periods):
        """Generate Latin square sequences for crossover design"""

        n_treatments = len(treatments)
        sequences = []

        # Simple Latin square generation (can be enhanced)
        for i in range(min(n_treatments, n_periods)):
            sequence = []
            for j in range(n_periods):
                treatment_idx = (i + j) % n_treatments
                sequence.append(treatments[treatment_idx])
            sequences.append(tuple(sequence))

        return sequences


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
