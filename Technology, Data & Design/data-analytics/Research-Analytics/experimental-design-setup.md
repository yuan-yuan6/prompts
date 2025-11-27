---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Research-Analytics/randomization-and-power-analysis.md
- data-analytics/Research-Analytics/treatment-effect-analysis.md
- data-analytics/Research-Analytics/validity-and-diagnostics.md
- data-analytics/Research-Analytics/variables-and-implementation.md
tags:
- research-analytics
- experimental-design
- rct
- ab-testing
title: Experimental Design Setup
use_cases:
- Select and configure appropriate experimental designs including RCTs, A/B tests,
  factorial designs, crossover designs, cluster trials, stepped wedge, quasi-experimental,
  and regression discontinuity designs
industries:
- education
- technology
type: template
difficulty: intermediate
slug: experimental-design-setup
---

# Experimental Design Setup

## Purpose
Select and configure the appropriate experimental design structure for your research objectives. This prompt helps you choose from 8 different design types and set up the framework for randomized controlled trials, A/B tests, factorial designs, crossover designs, cluster randomized trials, stepped wedge designs, quasi-experimental designs, and regression discontinuity designs.

## Quick Design Setup Prompt
Set up experiment for [research question] with [sample size] participants. Choose design type (RCT/A/B test/factorial/cluster), define treatment and control conditions, specify randomization method, identify primary and secondary outcomes, list key covariates to control, and create the allocation scheme. Output a design specification table and implementation checklist.

## Quick Start

**Example: Setting Up a Cluster Randomized Trial for Educational Intervention**

```
You are an experimental design expert. Set up a cluster randomized trial to test a new math curriculum across schools.

RESEARCH OBJECTIVE:
Test the effectiveness of an interactive digital math curriculum on 5th-grade student performance across 20 schools

DESIGN PARAMETERS:
- Design type: Cluster Randomized Trial
- Number of clusters: 20 schools
- Average cluster size: 60 students per school
- Total participants: 1,200 students
- Intracluster correlation: 0.08 (expected based on school-level similarity)
- Treatment: Interactive digital math curriculum
- Control: Standard math curriculum
- Primary outcome: End-of-year math test scores
- Duration: Full academic year

REQUIREMENTS:
1. Calculate design effect and effective sample size accounting for clustering
2. Randomize schools to treatment/control (1:1 allocation)
3. Account for baseline school characteristics (prior test scores, school size, SES)
4. Design data collection strategy for both school-level and student-level variables
5. Specify statistical model accounting for clustering
6. Create allocation table showing which schools receive treatment

Generate complete design setup with randomization scheme and implementation plan.
```

## Template

```
You are an experimental design expert. Set up a [DESIGN_TYPE] experimental design for [RESEARCH_OBJECTIVE] to test [HYPOTHESIS] with [PARTICIPANTS/UNITS].

RESEARCH CONTEXT:
- Research objective: [RESEARCH_OBJECTIVE]
- Primary hypothesis: [PRIMARY_HYPOTHESIS]
- Secondary hypotheses: [SECONDARY_HYPOTHESES]
- Target population: [TARGET_POPULATION]
- Study duration: [STUDY_DURATION]
- Budget constraints: [BUDGET_LIMITATIONS]

DESIGN CONFIGURATION:
- Design type: [DESIGN_TYPE]
- Number of participants/units: [N_PARTICIPANTS]
- Treatment conditions: [TREATMENT_LEVELS]
- Control condition: [CONTROL_CONDITION]
- Randomization level: [RANDOMIZATION_LEVEL]
- Allocation ratio: [ALLOCATION_RATIO]

DESIGN-SPECIFIC PARAMETERS:
For RCT:
- Stratification variables: [STRATIFICATION_VARS]
- Blinding type: [BLINDING_TYPE]
- Allocation concealment: [ALLOCATION_CONCEALMENT]

For A/B Test:
- Variants: [VARIANTS]
- Traffic allocation: [TRAFFIC_ALLOCATION]
- Randomization unit: [RANDOMIZATION_UNIT]

For Factorial Design:
- Factors: [FACTORS]
- Factor levels: [FACTOR_LEVELS]
- Participants per cell: [N_PER_CELL]

For Crossover Design:
- Number of periods: [N_PERIODS]
- Treatments: [TREATMENTS]
- Washout period: [WASHOUT_PERIOD]

For Cluster Trial:
- Number of clusters: [N_CLUSTERS]
- Cluster sizes: [CLUSTER_SIZES]
- Intracluster correlation: [ICC]

For Stepped Wedge:
- Number of time periods: [N_TIME_PERIODS]
- Randomization scheme: [WEDGE_RANDOMIZATION_SCHEME]

For Quasi-Experimental:
- Assignment rule: [ASSIGNMENT_RULE]
- Identification strategy: [IDENTIFICATION_STRATEGY]

For Regression Discontinuity:
- Cutoff value: [CUTOFF_VALUE]
- Assignment variable: [ASSIGNMENT_VARIABLE]
- Bandwidth: [BANDWIDTH]

EXPECTED DELIVERABLES:
- Complete design specification document
- Participant/unit allocation scheme
- Design matrix or allocation table
- Implementation timeline
- Data collection plan
```

## Experimental Design Framework

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
                    [f'{var}_low', f'{var}_high'],
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
elif '[DESIGN_TYPE]' == 'crossover':
    experiment_design = designer.setup_crossover_design(
        n_participants=[N_PARTICIPANTS],
        n_periods=[N_PERIODS],
        treatments=[TREATMENTS],
        washout_period=[WASHOUT_PERIOD]
    )
elif '[DESIGN_TYPE]' == 'cluster':
    experiment_design = designer.setup_cluster_trial(
        n_clusters=[N_CLUSTERS],
        cluster_sizes=[CLUSTER_SIZES],
        intracluster_correlation=[ICC]
    )
elif '[DESIGN_TYPE]' == 'stepped_wedge':
    experiment_design = designer.setup_stepped_wedge(
        n_clusters=[N_CLUSTERS],
        n_time_periods=[N_TIME_PERIODS],
        randomization_scheme=[WEDGE_RANDOMIZATION_SCHEME]
    )
elif '[DESIGN_TYPE]' == 'quasi':
    experiment_design = designer.setup_quasi_experimental(
        treatment_assignment_rule=[ASSIGNMENT_RULE]
    )
elif '[DESIGN_TYPE]' == 'rdd':
    experiment_design = designer.setup_regression_discontinuity(
        cutoff_value=[CUTOFF_VALUE],
        assignment_variable=[ASSIGNMENT_VARIABLE],
        bandwidth=[BANDWIDTH]
    )
```

## Design-Specific Variables

### Common Design Variables
- [DESIGN_TYPE] - Type of experimental design (rct, ab_test, factorial, crossover, cluster, stepped_wedge, quasi, rdd)
- [RESEARCH_OBJECTIVE] - Primary research objective
- [PRIMARY_HYPOTHESIS] - Main hypothesis being tested
- [TARGET_POPULATION] - Population of interest
- [STUDY_DURATION] - Duration of the study

### RCT Variables
- [N_PARTICIPANTS] - Number of participants
- [TREATMENT_RATIO] - Treatment allocation ratio (e.g., 0.5 for 1:1)
- [STRATIFICATION_VARS] - List of variables for stratification
- [BLINDING_TYPE] - Type of blinding (single, double, triple, none)
- [ALLOCATION_CONCEALMENT] - Whether allocation is concealed

### A/B Test Variables
- [N_USERS] - Number of users
- [VARIANTS] - List of test variants
- [TRAFFIC_ALLOCATION] - Traffic allocation percentages
- [RANDOMIZATION_UNIT] - Unit of randomization (user, session, page_view)
- [MDE] - Minimum detectable effect
- [CORRECTION_METHOD] - Multiple testing correction method

### Factorial Design Variables
- [FACTORS] - List of factors
- [FACTOR_LEVELS] - Dictionary of levels for each factor
- [N_PER_CELL] - Participants per condition cell

### Crossover Design Variables
- [N_PERIODS] - Number of treatment periods
- [TREATMENTS] - List of treatments
- [WASHOUT_PERIOD] - Whether washout period is included
- [CARRYOVER_CONTROL] - Method for controlling carryover effects
- [PERIOD_CONTROL] - Method for controlling period effects

### Cluster Trial Variables
- [N_CLUSTERS] - Number of clusters
- [CLUSTER_SIZES] - List of cluster sizes or single integer
- [ICC] - Intracluster correlation coefficient

### Stepped Wedge Variables
- [N_TIME_PERIODS] - Number of time periods
- [WEDGE_RANDOMIZATION_SCHEME] - Randomization scheme (random, uniform)

### Quasi-Experimental Variables
- [ASSIGNMENT_RULE] - Rule for treatment assignment
- [ASSIGNMENT_MECHANISM] - Mechanism of assignment
- [IDENTIFICATION_STRATEGY] - Strategy for causal identification

### Regression Discontinuity Variables
- [CUTOFF_VALUE] - Cutoff value for treatment assignment
- [ASSIGNMENT_VARIABLE] - Variable used for assignment
- [BANDWIDTH] - Bandwidth for local estimation
- [BANDWIDTH_METHOD] - Method for bandwidth selection
- [KERNEL_TYPE] - Type of kernel (rectangular, triangular, epanechnikov)

## Usage Examples

### Example 1: RCT for Clinical Trial
```python
designer = ExperimentalDesigner()

rct_design = designer.setup_rct(
    n_participants=400,
    treatment_ratio=0.5,
    stratification_vars=['age_group', 'disease_severity']
)

print(f"Design: {rct_design['type']}")
print(f"Treatment group size: {rct_design['treatment_size']}")
print(f"Control group size: {rct_design['control_size']}")
```

### Example 2: A/B Test for Website
```python
ab_design = designer.setup_ab_test(
    n_users=50000,
    variants=['control', 'variant_A', 'variant_B'],
    traffic_allocation=[0.4, 0.3, 0.3]
)

print(f"Total users: {ab_design['total_users']}")
print(f"Variant allocation: {ab_design['variant_sizes']}")
```

### Example 3: Factorial Design for Marketing
```python
factorial_design = designer.setup_factorial_design(
    factors=['message_type', 'timing', 'channel'],
    factor_levels={'message_type': 2, 'timing': 3, 'channel': 2},
    n_per_cell=30
)

print(f"Design: {factorial_design['type']}")
print(f"Total conditions: {factorial_design['conditions']}")
print(f"Total participants: {factorial_design['total_participants']}")
print(f"Interactions: {factorial_design['interactions']}")
```

### Example 4: Cluster Trial for Schools
```python
cluster_design = designer.setup_cluster_trial(
    n_clusters=20,
    cluster_sizes=60,
    intracluster_correlation=0.08
)

print(f"Design effect: {cluster_design['design_effect']:.2f}")
print(f"Effective sample size: {cluster_design['effective_sample_size']:.0f}")
print(f"Actual sample size: {cluster_design['total_participants']}")
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Randomization And Power Analysis](randomization-and-power-analysis.md)** - Complementary approaches and methodologies
- **[Treatment Effect Analysis](treatment-effect-analysis.md)** - Complementary approaches and methodologies
- **[Validity And Diagnostics](validity-and-diagnostics.md)** - Complementary approaches and methodologies
- **[Variables And Implementation](variables-and-implementation.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Experimental Design Setup)
2. Use [Randomization And Power Analysis](randomization-and-power-analysis.md) for deeper analysis
3. Apply [Treatment Effect Analysis](treatment-effect-analysis.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Research Analytics](../../data-analytics/Research Analytics/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Select and configure appropriate experimental designs including RCTs, A/B tests, factorial designs, crossover designs, cluster trials, stepped wedge, quasi-experimental, and regression discontinuity designs**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Choose the Right Design** - Match design type to research question and practical constraints
2. **Account for Clustering** - Use cluster designs when randomizing groups rather than individuals
3. **Plan for Sufficient Power** - Ensure sample size is adequate for detecting meaningful effects
4. **Consider Practical Constraints** - Balance statistical ideal with feasibility and cost
5. **Document Design Decisions** - Record rationale for all design choices
6. **Plan for Attrition** - Oversample to account for expected dropout
7. **Use Stratification Wisely** - Stratify on prognostic factors to improve balance
8. **Consider Crossover When Appropriate** - Use for stable conditions with reversible treatments
9. **Account for Multiple Testing** - Adjust for multiple comparisons in factorial designs
10. **Validate Design Assumptions** - Check that design assumptions hold in your context
