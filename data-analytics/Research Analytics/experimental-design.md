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

# Experimental Design and Testing Template

## Purpose
Design, implement, and analyze controlled experiments including A/B testing, randomized controlled trials, and causal inference studies to establish causal relationships and measure treatment effects with statistical rigor.

## Quick Start

**Example: Mobile App Pricing Experiment Design**

```
You are an experimental design expert. Design a randomized controlled experiment to test the impact of three different pricing strategies on mobile app subscription conversions and revenue.

BUSINESS OBJECTIVE:
Determine optimal pricing strategy for a SaaS mobile app by testing:
- Option A (Control): $9.99/month (current price)
- Option B (Treatment 1): $7.99/month with annual upsell emphasis
- Option C (Treatment 2): Freemium with $14.99/month premium features

EXPERIMENTAL PARAMETERS:
- Target sample size: 15,000 users (5,000 per group)
- Primary metric: 30-day conversion rate
- Secondary metrics: Revenue per user (RPU), 90-day retention rate, feature adoption rate
- Expected baseline conversion: 3.5% (from historical data)
- Minimum detectable effect: 0.7% absolute difference in conversion rate
- Statistical power: 80%
- Significance level: α = 0.05 (two-tailed)
- Duration: 30 days (minimum)
- Allocation: Equal randomization (1:1:1)

DESIGN REQUIREMENTS:
1. Power analysis: Calculate required sample size per group to detect 0.7% difference with 80% power
2. Randomization: Design stratified randomization by user segment (new users vs. trial users)
3. Control variables: Account for device type, geographic region, acquisition channel
4. Success criteria: Define primary decision rule (e.g., conversion rate increase ≥ 0.5% with p < 0.05)
5. Data collection: Specify tracking events, conversion funnel metrics, revenue tracking
6. Analysis plan: Pre-specify statistical tests (chi-square for conversion, t-test for RPU)
7. Interim analysis: Plan for one interim look at 50% sample with Bonferroni correction
8. Early stopping: Define rules for stopping for futility or overwhelming success

EXPECTED DELIVERABLES:
- Complete experimental protocol document
- Power analysis calculations with sample size justification
- Randomization algorithm and stratification scheme
- Statistical analysis plan (SAP) with hypothesis tests
- Data collection specification and tracking implementation plan
- Timeline with milestones (setup, launch, interim analysis, completion)
- Risk mitigation plan for potential confounders
- Ethical considerations and user experience impact assessment
```

## Template

```
You are an experimental design expert. Design and analyze a controlled experiment for [RESEARCH_OBJECTIVE] using [EXPERIMENTAL_METHOD] to test [HYPOTHESIS] with [PARTICIPANTS/UNITS] and measure [PRIMARY_OUTCOME].

EXPERIMENTAL DESIGN FRAMEWORK:
Research Context:
- Research objective: [RESEARCH_OBJECTIVE]
- Primary hypothesis: [PRIMARY_HYPOTHESIS]
- Secondary hypotheses: [SECONDARY_HYPOTHESES]
- Research question: [RESEARCH_QUESTION]
- Causal question: [CAUSAL_QUESTION]
- Population of interest: [TARGET_POPULATION]
- Context/Setting: [EXPERIMENTAL_CONTEXT]
- Time frame: [STUDY_DURATION]
- Budget constraints: [BUDGET_LIMITATIONS]

### Treatment Design
- Treatment variable: [TREATMENT_VARIABLE]
- Treatment levels: [TREATMENT_LEVELS] (Control/Treatment/Multiple treatments)
- Control condition: [CONTROL_CONDITION]
- Treatment description: [TREATMENT_DESCRIPTION]
- Dosage/Intensity: [TREATMENT_INTENSITY]
- Duration: [TREATMENT_DURATION]
- Delivery method: [DELIVERY_METHOD]
- Compliance monitoring: [COMPLIANCE_TRACKING]

### EXPERIMENTAL DESIGN TYPES
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

# Initialize experimental designer
designer = ExperimentalDesigner()

# Set up experiment based on design type
if '[DESIGN_TYPE]' == 'rct':
    experiment_design = designer.setup_rct(
        n_participants=[N_PARTICIPANTS],
        treatment_ratio=[TREATMENT_RATIO],
        stratification_vars=[STRATIFICATION_VARS]
    )
elif '[DESIGN_TYPE]' == 'ab_test':
    experiment_design = designer.setup_ab_test(
        n_users=[N_USERS],
        variants=[VARIANTS],
        traffic_allocation=[TRAFFIC_ALLOCATION]
    )
elif '[DESIGN_TYPE]' == 'factorial':
    experiment_design = designer.setup_factorial_design(
        factors=[FACTORS],
        factor_levels=[FACTOR_LEVELS],
        n_per_cell=[N_PER_CELL]
    )
```

RANDOMIZATION AND ALLOCATION:
Advanced Randomization Methods:
```python
class RandomizationManager:
    def __init__(self, seed=None):
        self.seed = seed
        if seed:
            np.random.seed(seed)
            random.seed(seed)

    def simple_randomization(self, n_participants, allocation_ratio=0.5):
        """Simple randomization with specified allocation ratio"""

        assignments = np.random.choice(
            ['control', 'treatment'],
            size=n_participants,
            p=[1-allocation_ratio, allocation_ratio]
        )

        allocation_result = {
            'method': 'Simple Randomization',
            'assignments': assignments,
            'control_count': np.sum(assignments == 'control'),
            'treatment_count': np.sum(assignments == 'treatment'),
            'actual_ratio': np.mean(assignments == 'treatment'),
            'target_ratio': allocation_ratio
        }

        return allocation_result

    def block_randomization(self, n_participants, block_size=4, allocation_ratio=0.5):
        """Block randomization to ensure balance in allocation"""

        n_treatment_per_block = int(block_size * allocation_ratio)
        n_control_per_block = block_size - n_treatment_per_block

        # Create block template
        block_template = ['treatment'] * n_treatment_per_block + ['control'] * n_control_per_block

        assignments = []
        n_complete_blocks = n_participants // block_size

        # Assign complete blocks
        for _ in range(n_complete_blocks):
            block = block_template.copy()
            np.random.shuffle(block)
            assignments.extend(block)

        # Handle remaining participants
        remaining = n_participants % block_size
        if remaining > 0:
            final_block = block_template[:remaining].copy()
            np.random.shuffle(final_block)
            assignments.extend(final_block)

        allocation_result = {
            'method': 'Block Randomization',
            'block_size': block_size,
            'n_blocks': n_complete_blocks + (1 if remaining > 0 else 0),
            'assignments': assignments,
            'control_count': assignments.count('control'),
            'treatment_count': assignments.count('treatment'),
            'balance_achieved': True
        }

        return allocation_result

    def stratified_randomization(self, participants_df, strata_vars, allocation_ratio=0.5):
        """Stratified randomization maintaining balance within strata"""

        assignments = []
        strata_info = []

        # Group by strata
        for strata_values, group in participants_df.groupby(strata_vars):
            n_in_stratum = len(group)
            n_treatment = int(n_in_stratum * allocation_ratio)
            n_control = n_in_stratum - n_treatment

            # Randomize within stratum
            stratum_assignments = ['treatment'] * n_treatment + ['control'] * n_control
            np.random.shuffle(stratum_assignments)

            assignments.extend(stratum_assignments)

            strata_info.append({
                'strata': strata_values,
                'n_participants': n_in_stratum,
                'n_treatment': n_treatment,
                'n_control': n_control,
                'treatment_ratio': n_treatment / n_in_stratum
            })

        allocation_result = {
            'method': 'Stratified Randomization',
            'strata_variables': strata_vars,
            'assignments': assignments,
            'strata_details': strata_info,
            'overall_balance': assignments.count('treatment') / len(assignments)
        }

        return allocation_result

    def cluster_randomization(self, clusters_df, cluster_id_col, allocation_ratio=0.5):
        """Cluster-level randomization"""

        unique_clusters = clusters_df[cluster_id_col].unique()
        n_clusters = len(unique_clusters)
        n_treatment_clusters = int(n_clusters * allocation_ratio)

        # Randomize clusters
        treatment_clusters = np.random.choice(
            unique_clusters,
            size=n_treatment_clusters,
            replace=False
        )

        # Assign all participants in cluster
        assignments = []
        for _, row in clusters_df.iterrows():
            if row[cluster_id_col] in treatment_clusters:
                assignments.append('treatment')
            else:
                assignments.append('control')

        allocation_result = {
            'method': 'Cluster Randomization',
            'n_clusters': n_clusters,
            'treatment_clusters': treatment_clusters,
            'control_clusters': [c for c in unique_clusters if c not in treatment_clusters],
            'assignments': assignments,
            'cluster_level_balance': len(treatment_clusters) / n_clusters
        }

        return allocation_result

    def adaptive_randomization(self, current_assignments, next_participant_strata,
                              target_ratio=0.5, imbalance_tolerance=0.1):
        """Adaptive randomization based on current imbalance"""

        current_treatment_ratio = np.mean([a == 'treatment' for a in current_assignments])
        imbalance = abs(current_treatment_ratio - target_ratio)

        if imbalance > imbalance_tolerance:
            # Bias toward underrepresented group
            if current_treatment_ratio < target_ratio:
                treatment_probability = 0.7
            else:
                treatment_probability = 0.3
        else:
            treatment_probability = target_ratio

        assignment = np.random.choice(
            ['control', 'treatment'],
            p=[1-treatment_probability, treatment_probability]
        )

        return {
            'assignment': assignment,
            'current_imbalance': imbalance,
            'treatment_probability_used': treatment_probability,
            'adaptive_adjustment': imbalance > imbalance_tolerance
        }

    def minimization_algorithm(self, participant_characteristics, existing_assignments,
                              factor_weights=None):
        """Minimization algorithm for treatment allocation"""

        if factor_weights is None:
            factor_weights = {factor: 1.0 for factor in participant_characteristics.keys()}

        # Calculate imbalance for each treatment assignment
        imbalance_scores = {}

        for treatment in ['control', 'treatment']:
            score = 0
            test_assignment = existing_assignments + [treatment]

            for factor, value in participant_characteristics.items():
                # Calculate imbalance for this factor
                factor_assignments = [assign for assign, char in
                                    zip(test_assignment,
                                        [existing_assignments[i][factor] for i in range(len(existing_assignments))] +
                                        [participant_characteristics])]

                treatment_count = sum(1 for assign in factor_assignments if assign == 'treatment')
                control_count = len(factor_assignments) - treatment_count

                imbalance = abs(treatment_count - control_count)
                score += imbalance * factor_weights[factor]

            imbalance_scores[treatment] = score

        # Choose assignment that minimizes imbalance
        best_assignment = min(imbalance_scores, key=imbalance_scores.get)

        return {
            'assignment': best_assignment,
            'imbalance_scores': imbalance_scores,
            'method': 'minimization'
        }

# Initialize randomization manager
randomizer = RandomizationManager(seed=[RANDOM_SEED])

# Perform randomization based on method
randomization_result = randomizer.[RANDOMIZATION_METHOD](
    n_participants=[N_PARTICIPANTS],
    allocation_ratio=[ALLOCATION_RATIO]
)
```

POWER ANALYSIS AND SAMPLE SIZE:
Comprehensive Power and Sample Size Calculations:
```python
from statsmodels.stats.power import TTestPower, FTestAnovaPower
from statsmodels.stats.proportion import proportion_effectsize, proportions_ztest
from statsmodels.stats.contingency_tables import mcnemar
import scipy.stats as stats

class PowerAnalyzer:
    def __init__(self):
        self.power_calculators = {
            'ttest': TTestPower(),
            'anova': FTestAnovaPower(),
            'proportion': self.proportion_power_analysis,
            'correlation': self.correlation_power_analysis,
            'regression': self.regression_power_analysis
        }

    def comprehensive_power_analysis(self, test_type, effect_size, alpha=0.05, power=0.8, **kwargs):
        """Perform comprehensive power analysis for different test types"""

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
            raise ValueError(f"Unknown test type: [TEST_TYPE]")

    def ttest_power_analysis(self, effect_size, alpha=0.05, power=0.8,
                           test_type='two-sample', alternative='two-sided'):
        """T-test power analysis"""

        power_calc = TTestPower()

        # Calculate required sample size
        sample_size = power_calc.solve_power(
            effect_size=effect_size,
            power=power,
            alpha=alpha,
            ratio=1,  # Equal group sizes
            alternative=alternative
        )

        # Power curve data
        sample_sizes = np.arange(5, int(sample_size * 2), 5)
        power_values = power_calc.solve_power(
            effect_size=effect_size,
            nobs=sample_sizes,
            alpha=alpha,
            alternative=alternative
        )

        # Effect size curve data
        effect_sizes = np.arange(0.1, 2.0, 0.1)
        power_by_effect = power_calc.solve_power(
            effect_size=effect_sizes,
            nobs=sample_size,
            alpha=alpha,
            alternative=alternative
        )

        results = {
            'test_type': 'T-test',
            'required_sample_size_per_group': int(np.ceil(sample_size)),
            'total_sample_size': int(np.ceil(sample_size * 2)),
            'effect_size': effect_size,
            'power': power,
            'alpha': alpha,
            'alternative': alternative,
            'power_curve': {
                'sample_sizes': sample_sizes,
                'power_values': power_values
            },
            'effect_size_curve': {
                'effect_sizes': effect_sizes,
                'power_values': power_by_effect
            }
        }

        return results

    def anova_power_analysis(self, effect_size, alpha=0.05, power=0.8, k_groups=3):
        """ANOVA power analysis"""

        power_calc = FTestAnovaPower()

        # Calculate required sample size
        sample_size = power_calc.solve_power(
            effect_size=effect_size,
            alpha=alpha,
            power=power,
            k_groups=k_groups
        )

        results = {
            'test_type': 'One-way ANOVA',
            'required_sample_size_per_group': int(np.ceil(sample_size)),
            'total_sample_size': int(np.ceil(sample_size * k_groups)),
            'effect_size_f': effect_size,
            'k_groups': k_groups,
            'power': power,
            'alpha': alpha
        }

        return results

    def proportion_power_analysis(self, effect_size, alpha=0.05, power=0.8,
                                 baseline_rate=0.1, **kwargs):
        """Proportion test power analysis"""

        # Convert effect size to actual proportions
        p1 = baseline_rate
        p2 = baseline_rate + effect_size

        # Ensure valid probabilities
        p2 = max(0, min(1, p2))

        # Calculate effect size (Cohen's h)
        h = proportion_effectsize(p1, p2)

        # Calculate sample size using normal approximation
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(power)

        # Pooled proportion
        p_pooled = (p1 + p2) / 2

        # Sample size calculation
        n = ((z_alpha * np.sqrt(2 * p_pooled * (1 - p_pooled)) +
              z_beta * np.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / (p1 - p2) ** 2

        results = {
            'test_type': 'Proportion test',
            'required_sample_size_per_group': int(np.ceil(n)),
            'total_sample_size': int(np.ceil(n * 2)),
            'baseline_proportion': p1,
            'treatment_proportion': p2,
            'effect_size_difference': effect_size,
            'effect_size_h': h,
            'power': power,
            'alpha': alpha
        }

        return results

    def correlation_power_analysis(self, effect_size, alpha=0.05, power=0.8, **kwargs):
        """Correlation power analysis"""

        # Sample size for correlation
        z_alpha = stats.norm.ppf(1 - alpha/2)
        z_beta = stats.norm.ppf(power)

        # Fisher's z transformation
        z_r = 0.5 * np.log((1 + effect_size) / (1 - effect_size))

        # Sample size
        n = ((z_alpha + z_beta) / z_r) ** 2 + 3

        results = {
            'test_type': 'Correlation',
            'required_sample_size': int(np.ceil(n)),
            'correlation_coefficient': effect_size,
            'power': power,
            'alpha': alpha,
            'fishers_z': z_r
        }

        return results

    def regression_power_analysis(self, effect_size, alpha=0.05, power=0.8,
                                 n_predictors=1, **kwargs):
        """Multiple regression power analysis"""

        # Effect size f² to R²
        r_squared = effect_size / (1 + effect_size)

        # Degrees of freedom
        df1 = n_predictors

        # Critical F value
        f_alpha = stats.f.ppf(1 - alpha, df1, 1000)  # Large df2 approximation

        # Non-centrality parameter
        lambda_power = stats.ncf.ppf(power, df1, 1000, f_alpha)

        # Sample size
        n = lambda_power / effect_size + n_predictors + 1

        results = {
            'test_type': 'Multiple Regression',
            'required_sample_size': int(np.ceil(n)),
            'effect_size_f2': effect_size,
            'r_squared': r_squared,
            'n_predictors': n_predictors,
            'power': power,
            'alpha': alpha
        }

        return results

    def minimum_detectable_effect(self, test_type, sample_size, alpha=0.05, power=0.8, **kwargs):
        """Calculate minimum detectable effect for given sample size"""

        if test_type == 'ttest':
            power_calc = TTestPower()
            mde = power_calc.solve_power(
                power=power,
                nobs=sample_size,
                alpha=alpha,
                alternative='two-sided'
            )
        elif test_type == 'proportion':
            # Simplified calculation for proportion test MDE
            z_alpha = stats.norm.ppf(1 - alpha/2)
            z_beta = stats.norm.ppf(power)
            baseline_rate = kwargs.get('baseline_rate', 0.1)

            mde = (z_alpha + z_beta) * np.sqrt(2 * baseline_rate * (1 - baseline_rate)) / np.sqrt(sample_size)

        return mde

    def power_sensitivity_analysis(self, test_type, base_params, param_ranges):
        """Perform sensitivity analysis on power calculations"""

        sensitivity_results = {}

        for param, param_range in param_ranges.items():
            results = []
            for value in param_range:
                params = base_params.copy()
                params[param] = value

                if test_type == 'ttest':
                    power_calc = TTestPower()
                    if param == 'sample_size':
                        power = power_calc.solve_power(nobs=value, **{k:v for k,v in params.items() if k != 'sample_size'})
                        results.append({'value': value, 'power': power})
                    elif param == 'effect_size':
                        power = power_calc.solve_power(effect_size=value, **{k:v for k,v in params.items() if k != 'effect_size'})
                        results.append({'value': value, 'power': power})

            sensitivity_results[param] = results

        return sensitivity_results

    def create_power_visualizations(self, power_results):
        """Create power analysis visualizations"""

        fig, axes = plt.subplots(2, 2, figsize=(15, 12))

        # Power vs Sample Size
        if 'power_curve' in power_results:
            power_curve = power_results['power_curve']
            axes[0, 0].plot(power_curve['sample_sizes'], power_curve['power_values'])
            axes[0, 0].axhline(y=0.8, color='r', linestyle='--', label='Power = 0.8')
            axes[0, 0].axvline(x=power_results['required_sample_size_per_group'], color='r', linestyle='--', label=f'Required N = {power_results["required_sample_size_per_group"]}')
            axes[0, 0].set_xlabel('Sample Size per Group')
            axes[0, 0].set_ylabel('Statistical Power')
            axes[0, 0].set_title('Power vs Sample Size')
            axes[0, 0].legend()
            axes[0, 0].grid(True)

        # Power vs Effect Size
        if 'effect_size_curve' in power_results:
            effect_curve = power_results['effect_size_curve']
            axes[0, 1].plot(effect_curve['effect_sizes'], effect_curve['power_values'])
            axes[0, 1].axhline(y=0.8, color='r', linestyle='--', label='Power = 0.8')
            axes[0, 1].axvline(x=power_results['effect_size'], color='r', linestyle='--', label=f'Target Effect Size = {power_results["effect_size"]}')
            axes[0, 1].set_xlabel('Effect Size')
            axes[0, 1].set_ylabel('Statistical Power')
            axes[0, 1].set_title('Power vs Effect Size')
            axes[0, 1].legend()
            axes[0, 1].grid(True)

        plt.tight_layout()
        return fig

# Perform power analysis
power_analyzer = PowerAnalyzer()
power_results = power_analyzer.comprehensive_power_analysis(
    test_type='[TEST_TYPE]',
    effect_size=[EFFECT_SIZE],
    alpha=[ALPHA_LEVEL],
    power=[STATISTICAL_POWER]
)

mde_analysis = power_analyzer.minimum_detectable_effect(
    test_type='[TEST_TYPE]',
    sample_size=[SAMPLE_SIZE],
    alpha=[ALPHA_LEVEL],
    power=[STATISTICAL_POWER]
)
```

TREATMENT EFFECT ANALYSIS:
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

EXPERIMENTAL VALIDITY AND DIAGNOSTICS:
Comprehensive Validity Assessment:
```python
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
                        'variable': f'[VAR]_[CATEGORY]',
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
            from scipy.stats import normaltest
            _, normality_p = normaltest(control_outcomes.dropna())

            contamination_indicators.append({
                'indicator': 'Control group normality',
                'p_value': normality_p,
                'interpretation': 'Very low p-values might suggest contamination'
            })

        return {
            'contamination_indicators': contamination_indicators,
            'contamination_likely': any(ind['p_value'] < 0.01 for ind in contamination_indicators if 'p_value' in ind)
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

        from scipy.stats import shapiro, levene

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

OUTPUT REQUIREMENTS:
Deliver comprehensive experimental analysis including:

1. **Experimental Design Documentation**
   - Research objectives and hypotheses
   - Treatment and control descriptions
   - Randomization procedures and allocation
   - Sample size justification and power analysis
   - Timeline and implementation details

2. **Randomization and Balance Assessment**
   - Randomization method verification
   - Covariate balance checks
   - Baseline characteristics comparison
   - Randomization success evaluation
   - Allocation concealment verification

3. **Treatment Effect Analysis**
   - Intention-to-treat analysis
   - Per-protocol analysis (if applicable)
   - Complier average causal effect
   - Dose-response relationships
   - Subgroup analyses

4. **Statistical Analysis Results**
   - Primary outcome analysis
   - Secondary outcome analyses
   - Effect sizes and confidence intervals
   - Multiple testing corrections
   - Sensitivity analyses

5. **Validity Assessment**
   - Internal validity threats
   - External validity evaluation
   - Statistical assumption checking
   - Attrition and compliance analysis
   - Contamination assessment

6. **Causal Inference**
   - Causal identification strategy
   - Instrumental variable analysis (if applicable)
   - Mediation analysis
   - Moderation analysis
   - Counterfactual reasoning

7. **Visualization Suite**
   - Treatment effect plots
   - Balance assessment charts
   - Power analysis curves
   - Subgroup effect visualizations
   - Diagnostic plots

8. **Robustness Checks**
   - Alternative analysis methods
   - Outlier sensitivity analysis
   - Missing data handling
   - Model specification tests
   - Bootstrap confidence intervals

9. **Implementation Assessment**
   - Protocol adherence evaluation
   - Treatment fidelity assessment
   - Data quality evaluation
   - Timeline adherence analysis
   - Resource utilization review

10. **Strategic Recommendations**
    - Policy/business implications
    - Implementation recommendations
    - Future research directions
    - Scalability considerations
    - Cost-benefit analysis
```

## Variables

[The template includes 400+ comprehensive variables covering all aspects of experimental design and analysis...]

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

### Treatment Variables
- [TREATMENT_VARIABLE] - Name of treatment variable
- [TREATMENT_LEVELS] - Levels of treatment
- [CONTROL_CONDITION] - Description of control condition
- [TREATMENT_DESCRIPTION] - Detailed treatment description
- [TREATMENT_INTENSITY] - Intensity/dosage of treatment
- [TREATMENT_DURATION] - Duration of treatment exposure
- [DELIVERY_METHOD] - Method of treatment delivery
- [COMPLIANCE_TRACKING] - Compliance monitoring approach

### Design Configuration Variables
- [DESIGN_TYPE] - Type of experimental design
- [N_PARTICIPANTS] - Number of participants
- [TREATMENT_RATIO] - Treatment allocation ratio
- [STRATIFICATION_VARS] - Variables for stratification
- [N_USERS] - Number of users (for digital experiments)
- [VARIANTS] - Different variants in experiment
- [TRAFFIC_ALLOCATION] - Traffic allocation percentages
- [FACTORS] - Factors in factorial design
- [FACTOR_LEVELS] - Levels for each factor
- [N_PER_CELL] - Participants per condition

### Randomization Variables
- [RANDOMIZATION_METHOD] - Randomization method used
- [RANDOM_SEED] - Seed for reproducible randomization
- [ALLOCATION_RATIO] - Treatment allocation ratio
- [BLOCK_SIZE] - Block size for block randomization
- [RANDOMIZATION_UNIT] - Unit of randomization
- [STRATIFICATION_VARIABLES] - Variables for stratified randomization
- [CLUSTER_VARIABLE] - Variable defining clusters
- [MINIMIZATION_FACTORS] - Factors for minimization algorithm

### Power Analysis Variables
- [TEST_TYPE] - Type of statistical test for power analysis
- [EFFECT_SIZE] - Expected effect size
- [ALPHA_LEVEL] - Type I error rate
- [STATISTICAL_POWER] - Desired statistical power
- [SAMPLE_SIZE] - Sample size for power calculation
- [MDE] - Minimum detectable effect
- [CORRECTION_METHOD] - Multiple testing correction method
- [POWER_ANALYSIS_METHOD] - Method for power calculation

### Outcome Variables
- [PRIMARY_OUTCOME] - Primary outcome measure
- [SECONDARY_OUTCOMES] - Secondary outcome measures
- [OUTCOME_VARIABLE] - Main outcome variable name
- [OUTCOME_TYPE] - Type of outcome (continuous, binary, etc.)
- [OUTCOME_SCALE] - Scale of measurement
- [BASELINE_OUTCOME] - Baseline measurement of outcome
- [FOLLOW_UP_PERIODS] - Follow-up time points
- [COMPOSITE_OUTCOMES] - Composite outcome measures

### Validity Variables
- [BASELINE_VARIABLES] - Baseline covariates for balance checking
- [COMPLIANCE_VARIABLE] - Variable indicating compliance
- [ATTRITION_INDICATOR] - Variable indicating study dropout
- [TIMESTAMP_VARIABLE] - Variable with timestamp information
- [BLINDING_TYPE] - Type of blinding implemented
- [ALLOCATION_CONCEALMENT] - Allocation concealment method
- [PROTOCOL_DEVIATIONS] - Number/type of protocol deviations

### Analysis Variables
- [ANALYSIS_POPULATION] - Population for primary analysis
- [COVARIATES] - Covariates for adjustment
- [SUBGROUP_VARIABLES] - Variables defining subgroups
- [INTERACTION_TERMS] - Interaction terms to test
- [MISSING_DATA_METHOD] - Method for handling missing data
- [OUTLIER_HANDLING] - Method for handling outliers
- [TRANSFORMATION_METHOD] - Data transformation method

### Causal Inference Variables
- [IDENTIFICATION_STRATEGY] - Causal identification strategy
- [INSTRUMENTAL_VARIABLE] - Instrumental variable (if applicable)
- [MEDIATOR_VARIABLES] - Variables that mediate the effect
- [MODERATOR_VARIABLES] - Variables that moderate the effect
- [CONFOUNDING_VARIABLES] - Potential confounding variables
- [ASSIGNMENT_MECHANISM] - Treatment assignment mechanism
- [SELECTION_BIAS_CONTROLS] - Controls for selection bias

### Implementation Variables
- [RECRUITMENT_METHOD] - Method for participant recruitment
- [ELIGIBILITY_CRITERIA] - Inclusion/exclusion criteria
- [CONSENT_PROCESS] - Informed consent process
- [DATA_COLLECTION_METHOD] - Method for data collection
- [QUALITY_ASSURANCE] - Quality assurance procedures
- [ADVERSE_EVENT_MONITORING] - Adverse event monitoring
- [PROTOCOL_ADHERENCE] - Protocol adherence monitoring

### Temporal Variables
- [BASELINE_PERIOD] - Baseline measurement period
- [INTERVENTION_PERIOD] - Intervention/treatment period
- [WASHOUT_PERIOD] - Washout period (for crossover)
- [FOLLOW_UP_DURATION] - Duration of follow-up
- [MEASUREMENT_SCHEDULE] - Schedule of measurements
- [SEASONAL_EFFECTS] - Consideration of seasonal effects
- [TIME_VARYING_EFFECTS] - Time-varying treatment effects

### Statistical Variables
- [STATISTICAL_MODEL] - Statistical model specification
- [ESTIMATOR_TYPE] - Type of estimator used
- [STANDARD_ERROR_METHOD] - Method for standard error calculation
- [CONFIDENCE_LEVEL] - Confidence level for intervals
- [HYPOTHESIS_TEST_TYPE] - Type of hypothesis test
- [TAIL_TYPE] - One-tailed or two-tailed test
- [ROBUST_METHODS] - Use of robust statistical methods
- [BAYESIAN_METHODS] - Use of Bayesian methods

### Quality Control Variables
- [DATA_MONITORING_COMMITTEE] - Data monitoring committee
- [INTERIM_ANALYSES] - Interim analysis schedule
- [STOPPING_RULES] - Rules for early stopping
- [SAFETY_MONITORING] - Safety monitoring procedures
- [DATA_QUALITY_CHECKS] - Data quality assurance checks
- [AUDIT_PROCEDURES] - Audit procedures implemented
- [REGULATORY_COMPLIANCE] - Regulatory compliance requirements

### Reporting Variables
- [PRIMARY_ANALYSIS_RESULTS] - Primary analysis results summary
- [EFFECT_SIZE_ESTIMATE] - Estimated effect size
- [CONFIDENCE_INTERVAL] - Confidence interval for effect
- [P_VALUE] - P-value from primary test
- [CLINICAL_SIGNIFICANCE] - Clinical significance assessment
- [PRACTICAL_SIGNIFICANCE] - Practical significance assessment
- [ADVERSE_EVENTS] - Summary of adverse events
- [PROTOCOL_VIOLATIONS] - Protocol violations summary

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: A/B Testing for Website Optimization
```
RESEARCH_OBJECTIVE: "Increase conversion rate through new checkout design"
DESIGN_TYPE: "ab_test"
VARIANTS: "['current_checkout', 'streamlined_checkout']"
N_USERS: "50000"
PRIMARY_OUTCOME: "conversion_rate"
MDE: "2% relative improvement"
STATISTICAL_POWER: "0.8"
```

### Example 2: Clinical Drug Trial
```
RESEARCH_OBJECTIVE: "Test efficacy of new diabetes medication"
DESIGN_TYPE: "rct"
TREATMENT_DESCRIPTION: "New medication vs. placebo"
N_PARTICIPANTS: "400"
PRIMARY_OUTCOME: "HbA1c_reduction"
BLINDING_TYPE: "double_blind"
FOLLOW_UP_DURATION: "12 months"
```

### Example 3: Educational Intervention Study
```
RESEARCH_OBJECTIVE: "Improve student math performance with new teaching method"
DESIGN_TYPE: "cluster_randomized_trial"
RANDOMIZATION_UNIT: "classroom"
TREATMENT_DESCRIPTION: "Interactive digital math curriculum"
PRIMARY_OUTCOME: "math_test_scores"
BASELINE_VARIABLES: "['prior_math_score', 'socioeconomic_status']"
```

### Example 4: Marketing Campaign Experiment
```
RESEARCH_OBJECTIVE: "Test effectiveness of personalized marketing messages"
DESIGN_TYPE: "factorial"
FACTORS: "['message_type', 'timing', 'channel']"
FACTOR_LEVELS: "{'message_type': 2, 'timing': 3, 'channel': 2}"
PRIMARY_OUTCOME: "customer_response_rate"
SECONDARY_OUTCOMES: "['click_through_rate', 'purchase_rate']"
```

### Example 5: Policy Intervention Study
```
RESEARCH_OBJECTIVE: "Evaluate impact of new social program"
DESIGN_TYPE: "stepped_wedge"
RANDOMIZATION_UNIT: "community"
TREATMENT_DESCRIPTION: "Enhanced social services program"
PRIMARY_OUTCOME: "employment_rate"
TEMPORAL_ANALYSIS: "Track outcomes over 2-year rollout"
```

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