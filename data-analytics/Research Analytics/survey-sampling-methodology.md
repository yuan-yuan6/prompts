---
title: Survey Sampling Methodology Template
category: data-analytics/Research Analytics
tags: [data-analytics, data-science, research, strategy, template, testing]
use_cases:
  - Design and implement survey sampling strategies with proper sample size calculations, stratification methods, and recruitment approaches to ensure representative and statistically valid samples.
  - Project planning and execution
  - Strategy development
related_templates:
  - survey-analysis-overview.md
  - survey-design-questionnaire.md
  - survey-data-collection.md
last_updated: 2025-11-09
---

# Survey Sampling Methodology Template

## Purpose
Design and implement survey sampling strategies with proper sample size calculations, stratification methods, and recruitment approaches to ensure representative and statistically valid samples.

## Template

```
You are a survey sampling expert. Design a comprehensive sampling strategy for [RESEARCH_PURPOSE] targeting [TARGET_POPULATION] with [SAMPLING_METHOD] methodology.

TARGET POPULATION:
- Population definition: [POPULATION_DEFINITION]
- Geographic scope: [GEOGRAPHIC_SCOPE]
- Demographic characteristics: [TARGET_DEMOGRAPHICS]
- Inclusion criteria: [INCLUSION_CRITERIA]
- Exclusion criteria: [EXCLUSION_CRITERIA]
- Population size: [POPULATION_SIZE]
- Accessibility: [POPULATION_ACCESSIBILITY]

SAMPLING DESIGN:

Sampling Strategy:
- Sampling method: [SAMPLING_METHOD] (Simple Random/Stratified/Cluster/Systematic/Convenience)
- Sampling frame: [SAMPLING_FRAME]
- Sampling units: [SAMPLING_UNITS]
- Stratification variables: [STRATIFICATION_VARS]
- Cluster variables: [CLUSTER_VARS]
- Multi-stage design: [MULTISTAGE_DESIGN]

```python
import numpy as np
import pandas as pd
from scipy import stats
import math

# Sample size calculation
def calculate_sample_size(population_size, margin_error, confidence_level, response_distribution=0.5):
    """Calculate required sample size for survey"""

    # Z-score for confidence level
    z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
    z_score = z_scores[confidence_level]

    # Sample size formula for proportions
    n = (z_score**2 * response_distribution * (1 - response_distribution)) / (margin_error**2)

    # Finite population correction
    if population_size is not None:
        n_adjusted = n / (1 + (n - 1) / population_size)
    else:
        n_adjusted = n

    return {
        'required_sample_size': math.ceil(n_adjusted),
        'unadjusted_sample_size': math.ceil(n),
        'population_size': population_size,
        'margin_of_error': margin_error,
        'confidence_level': confidence_level,
        'response_distribution': response_distribution
    }

# Stratified sampling design
def stratified_sample_design(strata_info, total_sample_size, allocation='proportional'):
    """Design stratified sampling plan"""

    strata_df = pd.DataFrame(strata_info)
    total_pop = strata_df['population_size'].sum()

    if allocation == 'proportional':
        # Proportional allocation
        strata_df['sample_size'] = (strata_df['population_size'] / total_pop * total_sample_size).round().astype(int)

    elif allocation == 'optimal':
        # Optimal allocation (Neyman allocation)
        # Requires variance estimates for each stratum
        numerator = strata_df['population_size'] * strata_df['std_dev']
        denominator = numerator.sum()
        strata_df['sample_size'] = (numerator / denominator * total_sample_size).round().astype(int)

    elif allocation == 'equal':
        # Equal allocation
        strata_df['sample_size'] = (total_sample_size / len(strata_df)).round().astype(int)

    # Calculate sampling fractions
    strata_df['sampling_fraction'] = strata_df['sample_size'] / strata_df['population_size']

    return strata_df

# Cluster sampling design
def cluster_sample_design(num_clusters_population, num_clusters_sample, avg_cluster_size):
    """Design cluster sampling plan"""

    # Calculate design effect
    # Assuming some intracluster correlation (ICC)
    icc = 0.05  # Default ICC
    design_effect = 1 + (avg_cluster_size - 1) * icc

    # Effective sample size
    total_sample_size = num_clusters_sample * avg_cluster_size
    effective_sample_size = total_sample_size / design_effect

    return {
        'num_clusters_population': num_clusters_population,
        'num_clusters_sample': num_clusters_sample,
        'avg_cluster_size': avg_cluster_size,
        'total_sample_size': total_sample_size,
        'design_effect': design_effect,
        'effective_sample_size': effective_sample_size,
        'cluster_sampling_fraction': num_clusters_sample / num_clusters_population
    }

# Sample size calculations
sample_size_results = calculate_sample_size(
    population_size=[POPULATION_SIZE],
    margin_error=[MARGIN_OF_ERROR],
    confidence_level=[CONFIDENCE_LEVEL],
    response_distribution=[EXPECTED_PROPORTION]
)

print(f"Required sample size: {sample_size_results['required_sample_size']}")
print(f"With finite population correction: {sample_size_results['unadjusted_sample_size']}")

# Example: Stratified sampling design
strata_information = [
    {'stratum': 'Age 18-35', 'population_size': 5000, 'std_dev': 1.2},
    {'stratum': 'Age 36-55', 'population_size': 7000, 'std_dev': 1.5},
    {'stratum': 'Age 56+', 'population_size': 3000, 'std_dev': 1.0}
]

stratified_plan = stratified_sample_design(
    strata_info=strata_information,
    total_sample_size=[TARGET_SAMPLE_SIZE],
    allocation='proportional'
)

print("\nStratified Sampling Plan:")
print(stratified_plan)

# Example: Cluster sampling design
cluster_plan = cluster_sample_design(
    num_clusters_population=200,
    num_clusters_sample=50,
    avg_cluster_size=20
)

print(f"\nCluster Sampling Design Effect: {cluster_plan['design_effect']:.2f}")
print(f"Effective Sample Size: {cluster_plan['effective_sample_size']:.0f}")
```

Sample Size Parameters:
- Target sample size: [TARGET_SAMPLE_SIZE]
- Margin of error: [MARGIN_OF_ERROR]
- Confidence level: [CONFIDENCE_LEVEL]
- Expected response rate: [EXPECTED_RESPONSE_RATE]
- Design effect: [DESIGN_EFFECT]
- Oversampling factor: [OVERSAMPLING_FACTOR]
- Final sample size needed: [FINAL_SAMPLE_SIZE]

RECRUITMENT STRATEGY:
```python
# Sample recruitment framework
class RecruitmentStrategy:
    def __init__(self, target_sample_size, expected_response_rate):
        self.target_sample_size = target_sample_size
        self.expected_response_rate = expected_response_rate
        self.invitations_needed = self.calculate_invitations()

    def calculate_invitations(self):
        """Calculate number of invitations needed"""
        return math.ceil(self.target_sample_size / self.expected_response_rate)

    def create_recruitment_plan(self):
        """Create comprehensive recruitment plan"""

        plan = {
            'initial_contact': {
                'method': 'Email/phone/mail invitation',
                'timing': 'Week 1',
                'sample_size': self.invitations_needed,
                'message': 'Initial invitation with survey details and incentive'
            },

            'reminder_sequence': [
                {
                    'reminder': 1,
                    'timing': 'Day 3',
                    'target': 'Non-respondents',
                    'method': 'Email reminder',
                    'message': 'Gentle reminder about importance'
                },
                {
                    'reminder': 2,
                    'timing': 'Day 7',
                    'target': 'Non-respondents',
                    'method': 'Email with different appeal',
                    'message': 'Emphasize contribution and value'
                },
                {
                    'reminder': 3,
                    'timing': 'Day 14',
                    'target': 'Non-respondents',
                    'method': 'Phone call or alternative mode',
                    'message': 'Final opportunity with urgency'
                }
            ],

            'incentive_structure': {
                'type': '[INCENTIVE_TYPE]',
                'amount': '[INCENTIVE_AMOUNT]',
                'distribution': 'Conditional/Unconditional',
                'alternatives': 'Lottery/Charitable donation'
            },

            'response_monitoring': {
                'daily_tracking': 'Monitor response rates daily',
                'demographic_balance': 'Check representativeness',
                'quality_checks': 'Review data quality metrics',
                'adjustment_triggers': 'When to modify recruitment'
            }
        }

        return plan

# Response rate estimation
def estimate_response_rate(mode, population_type, incentive=False):
    """Estimate expected response rates by mode"""

    baseline_rates = {
        'online': {
            'general_public': 0.10,
            'customers': 0.15,
            'employees': 0.40,
            'members': 0.25
        },
        'telephone': {
            'general_public': 0.09,
            'customers': 0.20,
            'employees': 0.50,
            'members': 0.30
        },
        'face_to_face': {
            'general_public': 0.50,
            'customers': 0.60,
            'employees': 0.70,
            'members': 0.65
        },
        'mail': {
            'general_public': 0.08,
            'customers': 0.12,
            'employees': 0.35,
            'members': 0.20
        }
    }

    base_rate = baseline_rates.get(mode, {}).get(population_type, 0.15)

    # Adjust for incentive
    if incentive:
        base_rate *= 1.5  # Typical incentive boost

    return base_rate
```

OUTPUT REQUIREMENTS:
Deliver comprehensive sampling methodology including:

1. **Sampling Design Documentation**
   - Sampling method justification
   - Sampling frame description
   - Sample size calculations
   - Power analysis results
   - Design effect estimation

2. **Stratification Plan** (if applicable)
   - Stratification variables
   - Stratum definitions
   - Allocation methods
   - Sample size per stratum
   - Sampling fractions

3. **Recruitment Strategy**
   - Contact methods and timing
   - Reminder schedule
   - Incentive structure
   - Response monitoring plan
   - Contingency procedures

4. **Quality Control**
   - Representativeness checks
   - Response rate targets
   - Bias assessment plan
   - Weighting strategy
   - Documentation procedures
```

## Variables

### Target Population Variables
- [RESEARCH_PURPOSE] - Primary purpose of the survey research
- [TARGET_POPULATION] - Population of interest for the survey
- [POPULATION_DEFINITION] - Precise definition of target population
- [GEOGRAPHIC_SCOPE] - Geographic boundaries of the study
- [TARGET_DEMOGRAPHICS] - Demographic characteristics of interest
- [INCLUSION_CRITERIA] - Criteria for including participants
- [EXCLUSION_CRITERIA] - Criteria for excluding participants
- [POPULATION_SIZE] - Estimated size of target population
- [POPULATION_ACCESSIBILITY] - Level of access to target population

### Sampling Variables
- [SAMPLING_METHOD] - Primary sampling method used
- [SAMPLING_FRAME] - List or source for sampling
- [SAMPLING_UNITS] - Units being sampled (individuals, households, etc.)
- [STRATIFICATION_VARS] - Variables used for stratification
- [CLUSTER_VARS] - Variables defining clusters
- [MULTISTAGE_DESIGN] - Multi-stage sampling design details
- [TARGET_SAMPLE_SIZE] - Desired sample size
- [MARGIN_OF_ERROR] - Acceptable margin of error
- [CONFIDENCE_LEVEL] - Statistical confidence level
- [EXPECTED_PROPORTION] - Expected response proportion for calculations
- [EXPECTED_RESPONSE_RATE] - Anticipated response rate
- [DESIGN_EFFECT] - Design effect due to sampling method
- [OVERSAMPLING_FACTOR] - Factor for oversampling specific groups
- [FINAL_SAMPLE_SIZE] - Final required sample size accounting for all factors
- [SAMPLING_FRACTION] - Proportion of population sampled
- [REPLACEMENT_STRATEGY] - Strategy for replacement sampling

### Recruitment Variables
- [INCENTIVE_TYPE] - Type of incentive offered
- [INCENTIVE_AMOUNT] - Amount or value of incentive
- [CONTACT_STRATEGY] - Strategy for contacting respondents
- [REMINDER_SCHEDULE] - Schedule for follow-up reminders
- [FIELD_PERIOD] - Duration of data collection period

## Usage Examples

### Example 1: Simple Random Sampling
```
SAMPLING_METHOD: "Simple random sampling"
POPULATION_SIZE: "50,000 customers"
TARGET_SAMPLE_SIZE: "1,000"
MARGIN_OF_ERROR: "±3%"
CONFIDENCE_LEVEL: "95%"
EXPECTED_RESPONSE_RATE: "20%"
```

### Example 2: Stratified Random Sampling
```
SAMPLING_METHOD: "Stratified random sampling"
STRATIFICATION_VARS: "Age group, gender, region"
TARGET_SAMPLE_SIZE: "2,500"
ALLOCATION_METHOD: "Proportional allocation"
DESIGN_EFFECT: "1.2"
```

### Example 3: Cluster Sampling
```
SAMPLING_METHOD: "Two-stage cluster sampling"
CLUSTER_VARS: "Geographic regions, then households"
NUM_CLUSTERS: "50 regions"
AVG_CLUSTER_SIZE: "30 households"
DESIGN_EFFECT: "1.8"
```

### Example 4: Public Opinion Poll
```
RESEARCH_PURPOSE: "Assess public opinion on policy issues"
TARGET_POPULATION: "Adults 18+ in metropolitan area"
SAMPLING_METHOD: "Random digit dialing with cell phone supplement"
MARGIN_OF_ERROR: "±3% at 95% confidence level"
TARGET_SAMPLE_SIZE: "1,200 adults"
```

## Best Practices

1. **Define population precisely** - Clear inclusion and exclusion criteria
2. **Use probability sampling when possible** - Enables statistical inference
3. **Calculate appropriate sample size** - Balance precision and resources
4. **Account for non-response** - Oversample based on expected response rate
5. **Document sampling frame** - Describe source and quality of frame
6. **Consider design effects** - Account for clustering and stratification
7. **Plan for representativeness** - Monitor demographic balance during collection
8. **Use stratification strategically** - Improve precision for key subgroups
9. **Prepare for contingencies** - Have backup recruitment strategies
10. **Maintain detailed records** - Document all sampling procedures

## Tips for Success

- Start with clear research questions to guide sampling decisions
- Consult power analysis to determine minimum sample size
- Balance statistical requirements with budget constraints
- Use multiple contact methods to maximize response rates
- Monitor data collection in real-time for quality issues
- Consider weighting strategies during sampling design
- Test recruitment materials before full launch
- Build relationships with gatekeepers for hard-to-reach populations
- Plan adequate field period for achieving target sample size
- Document all deviations from original sampling plan
