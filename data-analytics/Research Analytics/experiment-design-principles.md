---
title: Experimental Design Principles & Frameworks
category: data-analytics/Research Analytics
tags: [automation, data-analytics, data-science, design, research, template]
use_cases:
  - Understanding core experimental design principles including control, randomization, and replication
  - Selecting appropriate experimental vs. observational designs
  - Implementing randomized controlled trials, A/B tests, crossover, and quasi-experimental designs
related_templates:
  - experimental-design-overview.md
  - factorial-designs.md
  - randomization-blocking.md
  - sample-size-power-analysis.md
last_updated: 2025-11-09
---

# Experimental Design Principles & Frameworks

## Purpose
Understand and apply fundamental experimental design principles to establish causal relationships through controlled experiments, including RCTs, A/B tests, crossover designs, and quasi-experimental approaches.

## Template

```
You are an experimental design expert. Design a controlled experiment for [RESEARCH_OBJECTIVE] using [DESIGN_TYPE] to test [HYPOTHESIS] with [PARTICIPANTS/UNITS] and measure [PRIMARY_OUTCOME].

EXPERIMENTAL DESIGN FRAMEWORK:
Research Context:
- Research objective: [RESEARCH_OBJECTIVE]
- Primary hypothesis: [PRIMARY_HYPOTHESIS]
- Research question: [RESEARCH_QUESTION]
- Causal question: [CAUSAL_QUESTION]
- Population of interest: [TARGET_POPULATION]
- Context/Setting: [EXPERIMENTAL_CONTEXT]
- Time frame: [STUDY_DURATION]

### Core Design Principles

1. **Randomization**: [RANDOMIZATION_STRATEGY]
   - Ensures groups are comparable at baseline
   - Eliminates selection bias
   - Balances known and unknown confounders

2. **Control**: [CONTROL_CONDITION]
   - Provides comparison baseline
   - Isolates treatment effect
   - Accounts for natural variation

3. **Replication**: [REPLICATION_APPROACH]
   - Multiple units per condition
   - Enables statistical inference
   - Quantifies variability

4. **Blinding**: [BLINDING_TYPE]
   - Single-blind: Participants unaware
   - Double-blind: Participants and researchers unaware
   - Triple-blind: Including data analysts

### Treatment Configuration
- Treatment variable: [TREATMENT_VARIABLE]
- Treatment levels: [TREATMENT_LEVELS]
- Control condition: [CONTROL_CONDITION]
- Treatment description: [TREATMENT_DESCRIPTION]
- Dosage/Intensity: [TREATMENT_INTENSITY]
- Duration: [TREATMENT_DURATION]
- Delivery method: [DELIVERY_METHOD]

DESIGN IMPLEMENTATION:
```python
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from itertools import product
import random

class ExperimentalDesigner:
    def __init__(self):
        self.design_types = {
            'randomized_controlled_trial': self.setup_rct,
            'ab_test': self.setup_ab_test,
            'crossover_design': self.setup_crossover_design,
            'cluster_randomized_trial': self.setup_cluster_trial,
            'stepped_wedge': self.setup_stepped_wedge,
            'quasi_experimental': self.setup_quasi_experimental,
            'regression_discontinuity': self.setup_regression_discontinuity
        }

    def setup_rct(self, n_participants, treatment_ratio=0.5, stratification_vars=None):
        """
        Set up Randomized Controlled Trial

        Key Features:
        - Individual-level randomization
        - Parallel group design
        - Control and treatment groups
        - Optional stratification
        """

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

        print(f"RCT Design Created:")
        print(f"  - Total N: {n_participants}")
        print(f"  - Control: {design['control_size']}")
        print(f"  - Treatment: {design['treatment_size']}")
        if stratification_vars:
            print(f"  - Stratified by: {', '.join(stratification_vars)}")

        return design

    def setup_ab_test(self, n_users, variants=['A', 'B'], traffic_allocation=None):
        """
        Set up A/B Test for digital experiments

        Key Features:
        - Multiple variant support
        - Traffic splitting
        - User-level or session-level randomization
        - Real-time allocation
        """

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

        print(f"A/B Test Design Created:")
        print(f"  - Total Users: {n_users}")
        print(f"  - Variants: {variants}")
        print(f"  - Allocation: {dict(zip(variants, traffic_allocation))}")

        return design

    def setup_crossover_design(self, n_participants, n_periods, treatments, washout_period=True):
        """
        Set up Crossover Design

        Key Features:
        - Within-subject comparisons
        - Each participant receives all treatments
        - Sequences balanced across participants
        - Controls for carryover effects
        """

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

        print(f"Crossover Design Created:")
        print(f"  - Participants: {n_participants}")
        print(f"  - Periods: {n_periods}")
        print(f"  - Treatments: {treatments}")
        print(f"  - Sequences: {len(sequences)}")

        return design

    def setup_cluster_trial(self, n_clusters, cluster_sizes, intracluster_correlation=0.05):
        """
        Set up Cluster Randomized Trial

        Key Features:
        - Cluster-level randomization
        - Accounts for intracluster correlation
        - Design effect calculation
        - Appropriate for group interventions
        """

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

        print(f"Cluster RCT Design Created:")
        print(f"  - Clusters: {n_clusters}")
        print(f"  - Total Participants: {total_participants}")
        print(f"  - ICC: {intracluster_correlation}")
        print(f"  - Design Effect: {design['design_effect']:.2f}")
        print(f"  - Effective N: {design['effective_sample_size']:.0f}")

        return design

    def setup_stepped_wedge(self, n_clusters, n_time_periods, randomization_scheme='random'):
        """
        Set up Stepped Wedge Design

        Key Features:
        - Sequential intervention rollout
        - All clusters eventually receive treatment
        - Before-after comparisons within clusters
        - Between-cluster comparisons over time
        """

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

        print(f"Stepped Wedge Design Created:")
        print(f"  - Clusters: {n_clusters}")
        print(f"  - Time Periods: {n_time_periods}")
        print("\nWedge Matrix (0=Control, 1=Treatment):")
        print(wedge_matrix)

        return design

    def setup_quasi_experimental(self, treatment_assignment_rule, cutoff_variable=None):
        """
        Set up Quasi-experimental Design

        Key Features:
        - Non-random treatment assignment
        - Natural or administrative assignment
        - Requires careful identification strategy
        - Multiple validity threats to address
        """

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
            'identification_strategy': '[IDENTIFICATION_STRATEGY]',
            'required_controls': [
                'baseline_equivalence_check',
                'covariate_adjustment',
                'sensitivity_analysis'
            ]
        }

        if cutoff_variable:
            design['cutoff_variable'] = cutoff_variable
            design['subtype'] = 'Regression Discontinuity'

        return design

    def setup_regression_discontinuity(self, cutoff_value, assignment_variable, bandwidth=None):
        """
        Set up Regression Discontinuity Design

        Key Features:
        - Assignment based on cutoff threshold
        - Local randomization near cutoff
        - Continuity assumptions
        - Bandwidth selection critical
        """

        design = {
            'type': 'Regression Discontinuity Design',
            'cutoff_value': cutoff_value,
            'assignment_variable': assignment_variable,
            'bandwidth': bandwidth,
            'bandwidth_selection': '[BANDWIDTH_METHOD]',  # IK, CV, MSE-optimal
            'kernel': '[KERNEL_TYPE]',  # rectangular, triangular, epanechnikov
            'continuity_tests': True,
            'density_tests': True,
            'covariate_balance_tests': True,
            'required_checks': [
                'no_manipulation_of_assignment_variable',
                'continuity_of_covariates',
                'no_density_discontinuity'
            ]
        }

        print(f"Regression Discontinuity Design Created:")
        print(f"  - Assignment Variable: {assignment_variable}")
        print(f"  - Cutoff Value: {cutoff_value}")
        print(f"  - Bandwidth: {bandwidth if bandwidth else 'To be determined'}")

        return design

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

        # Simple Latin square generation
        for i in range(min(n_treatments, n_periods)):
            sequence = []
            for j in range(n_periods):
                treatment_idx = (i + j) % n_treatments
                sequence.append(treatments[treatment_idx])
            sequences.append(tuple(sequence))

        return sequences

# Initialize experimental designer
designer = ExperimentalDesigner()

# Select and configure design based on research needs
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
elif '[DESIGN_TYPE]' == 'crossover':
    experiment_design = designer.setup_crossover_design(
        n_participants=[N_PARTICIPANTS],
        n_periods=[N_PERIODS],
        treatments=[TREATMENTS],
        washout_period=[WASHOUT_REQUIRED]
    )
elif '[DESIGN_TYPE]' == 'cluster':
    experiment_design = designer.setup_cluster_trial(
        n_clusters=[N_CLUSTERS],
        cluster_sizes=[CLUSTER_SIZES],
        intracluster_correlation=[ICC]
    )
```

OUTPUT REQUIREMENTS:
Deliver comprehensive design documentation including:

1. **Design Justification**
   - Why this design is appropriate for research question
   - Advantages over alternative designs
   - Assumptions and limitations

2. **Implementation Plan**
   - Participant recruitment strategy
   - Randomization procedures
   - Timeline and milestones
   - Resource requirements

3. **Quality Assurance**
   - Blinding procedures
   - Allocation concealment
   - Protocol adherence monitoring
   - Data quality checks

4. **Validity Considerations**
   - Internal validity threats and controls
   - External validity assessment
   - Statistical conclusion validity
   - Construct validity

5. **Documentation**
   - Pre-registration details
   - Protocol documentation
   - Analysis plan
   - Reporting standards (CONSORT, etc.)
```

## Variables

### Research Design Variables
- [RESEARCH_OBJECTIVE] - Primary research objective
- [PRIMARY_HYPOTHESIS] - Main hypothesis being tested
- [RESEARCH_QUESTION] - Core research question
- [CAUSAL_QUESTION] - Specific causal question
- [TARGET_POPULATION] - Population of interest
- [EXPERIMENTAL_CONTEXT] - Context/setting of experiment
- [STUDY_DURATION] - Duration of the study

### Design Type Variables
- [DESIGN_TYPE] - Type of experimental design (rct, ab_test, crossover, cluster, quasi_experimental)
- [N_PARTICIPANTS] - Number of participants
- [N_USERS] - Number of users (for digital experiments)
- [N_CLUSTERS] - Number of clusters
- [N_PERIODS] - Number of time periods

### Treatment Variables
- [TREATMENT_VARIABLE] - Name of treatment variable
- [TREATMENT_LEVELS] - Levels of treatment
- [CONTROL_CONDITION] - Description of control condition
- [TREATMENT_DESCRIPTION] - Detailed treatment description
- [TREATMENT_INTENSITY] - Intensity/dosage of treatment
- [TREATMENT_DURATION] - Duration of treatment exposure
- [DELIVERY_METHOD] - Method of treatment delivery

### Design Configuration Variables
- [TREATMENT_RATIO] - Treatment allocation ratio (e.g., 0.5 for 1:1)
- [STRATIFICATION_VARS] - Variables for stratification
- [VARIANTS] - Different variants in A/B test (e.g., ['A', 'B'])
- [TRAFFIC_ALLOCATION] - Traffic allocation percentages
- [TREATMENTS] - List of treatments in crossover design
- [WASHOUT_REQUIRED] - Whether washout period needed (True/False)
- [CLUSTER_SIZES] - Size of each cluster or uniform size
- [ICC] - Intracluster correlation coefficient

### Validity Variables
- [BLINDING_TYPE] - Type of blinding (single, double, triple, none)
- [RANDOMIZATION_STRATEGY] - Randomization approach
- [CONTROL_CONDITION] - Control group specification
- [REPLICATION_APPROACH] - How replication is achieved
- [ALLOCATION_CONCEALMENT] - Method for allocation concealment

## Best Practices

1. **Choose simplest adequate design** - Don't overcomplicate
2. **Randomize whenever possible** - Strengthens causal inference
3. **Pre-specify everything** - Hypotheses, outcomes, analyses
4. **Plan for attrition** - Over-recruit if dropout expected
5. **Pilot test procedures** - Identify issues before full launch
6. **Document deviations** - Track any protocol changes
7. **Consider practical constraints** - Feasibility matters
8. **Engage stakeholders early** - Get buy-in for implementation

## Usage Examples

### Example 1: Clinical Drug Trial (RCT)
```
RESEARCH_OBJECTIVE: "Test efficacy of new diabetes medication"
DESIGN_TYPE: "rct"
N_PARTICIPANTS: 400
TREATMENT_RATIO: 0.5
PRIMARY_OUTCOME: "HbA1c_reduction"
BLINDING_TYPE: "double_blind"
STUDY_DURATION: "12 months"
```

### Example 2: Website Conversion (A/B Test)
```
RESEARCH_OBJECTIVE: "Increase checkout conversion rate"
DESIGN_TYPE: "ab_test"
N_USERS: 50000
VARIANTS: "['control', 'new_checkout']"
TRAFFIC_ALLOCATION: "[0.5, 0.5]"
PRIMARY_OUTCOME: "conversion_rate"
```

### Example 3: Educational Intervention (Cluster RCT)
```
RESEARCH_OBJECTIVE: "Improve student math scores"
DESIGN_TYPE: "cluster"
N_CLUSTERS: 40
CLUSTER_SIZES: 25
ICC: 0.05
PRIMARY_OUTCOME: "math_test_scores"
RANDOMIZATION_LEVEL: "classroom"
```
