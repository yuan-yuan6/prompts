---
title: Policy Impact Assessment
category: government/Policy Development
tags: [impact-assessment, evaluation, economic-impact, social-impact, environmental]
use_cases:
  - Evaluating economic, social, and environmental impacts of policy options
  - Conducting multi-criteria impact analysis
  - Assessing stakeholder effects and distribution
related_templates:
  - government/Policy Development/policy-research-analysis.md
  - government/Policy Development/policy-options-development.md
  - government/Policy Development/policy-implementation-planning.md
  - government/Policy Development/policy-research-overview.md
last_updated: 2025-11-09
---

# Policy Impact Assessment

## Purpose
Conduct comprehensive impact assessments of policy proposals across economic, social, and environmental dimensions, evaluate distributional effects, and analyze stakeholder impacts to inform evidence-based policy decisions.

## Quick Start

**Immediate Use:** For assessing a carbon pricing policy, specify:
- POLICY_PROPOSAL: "Carbon tax at $50 per tonne with revenue recycling"
- POLICY_AREA: "Climate policy and emissions reduction"
- GOVERNMENT_LEVEL: "Federal/National"
- IMPACT_DIMENSIONS: "Economic (GDP, employment, industry), social (equity, household costs), environmental (emissions, air quality)"

**Key Variables to Customize:**
- Cost analysis categories (implementation, operations, compliance costs over time)
- Distributional effects by income groups (identify who benefits and who bears costs)
- Environmental impact metrics (emissions reduction, resource use, sustainability)
- Sensitivity analysis variables (test different assumptions about behavioral responses)

**Expected Output:** Comprehensive impact assessment with quantified costs and benefits across economic, social, and environmental dimensions, distributional equity evaluation showing effects on different population groups, stakeholder impact mapping, sensitivity analysis testing robustness of findings, and evidence-based recommendations for decision-makers.

## Template

```
You are a policy impact assessment specialist. Evaluate the impacts of [POLICY_PROPOSAL] on [POLICY_AREA] for [GOVERNMENT_LEVEL] across [IMPACT_DIMENSIONS] affecting [STAKEHOLDER_GROUPS] over [TIMEFRAME].

### POLICY PROPOSAL CONTEXT

Policy Description:
- Policy name: [POLICY_NAME]
- Policy objective: [POLICY_OBJECTIVE]
- Target population: [TARGET_POPULATION]
- Geographic scope: [GEOGRAPHIC_SCOPE]
- Implementation timeframe: [IMPLEMENTATION_TIMEFRAME]
- Expected duration: [DURATION]

Baseline Conditions:
- Current situation: [CURRENT_SITUATION]
- Problem magnitude: [PROBLEM_MAGNITUDE]
- Affected population: [AFFECTED_POPULATION]
- Baseline metrics: [BASELINE_METRICS]

### ECONOMIC IMPACT ANALYSIS

Economic Impact Assessment:
Sector           | Direct Impact   | Indirect Impact | Timeline       | Magnitude
-----------------|-----------------|-----------------|----------------|----------
Government Budget| [GOV_DIRECT]    | [GOV_INDIRECT]  | [GOV_TIME]     | [GOV_MAG]
Private Sector   | [PRIV_DIRECT]   | [PRIV_INDIRECT] | [PRIV_TIME]    | [PRIV_MAG]
Households       | [HOUSE_DIRECT]  | [HOUSE_INDIRECT]| [HOUSE_TIME]   | [HOUSE_MAG]
Labor Market     | [LABOR_DIRECT]  | [LABOR_INDIRECT]| [LABOR_TIME]   | [LABOR_MAG]
GDP/Growth       | [GDP_DIRECT]    | [GDP_INDIRECT]  | [GDP_TIME]     | [GDP_MAG]

Cost Analysis:
Cost Category    | One-time Costs  | Annual Costs    | Duration       | Total NPV
-----------------|-----------------|-----------------|----------------|----------
Implementation   | [IMP_ONETIME]   | [IMP_ANNUAL]    | [IMP_DUR]      | [IMP_NPV]
Operations       | [OPS_ONETIME]   | [OPS_ANNUAL]    | [OPS_DUR]      | [OPS_NPV]
Compliance       | [COMP_ONETIME]  | [COMP_ANNUAL]   | [COMP_DUR]     | [COMP_NPV]
Administration   | [ADM_ONETIME]   | [ADM_ANNUAL]    | [ADM_DUR]      | [ADM_NPV]

Benefit Analysis:
Benefit Category | Quantifiable    | Non-Quantifiable| Timeline       | Value
-----------------|-----------------|-----------------|----------------|-------
Direct Benefits  | [DIR_QUANT]     | [DIR_QUAL]      | [DIR_TIME]     | [DIR_VALUE]
Indirect Benefits| [IND_QUANT]     | [IND_QUAL]      | [IND_TIME]     | [IND_VALUE]
Multiplier Effects| [MULT_QUANT]   | [MULT_QUAL]     | [MULT_TIME]    | [MULT_VALUE]
Long-term Benefits| [LONG_QUANT]   | [LONG_QUAL]     | [LONG_TIME]    | [LONG_VALUE]

### SOCIAL IMPACT ANALYSIS

Social Impact Assessment:
Dimension        | Affected Groups | Impact Type     | Severity       | Duration
-----------------|-----------------|-----------------|----------------|----------
Equity           | [EQ_GROUPS]     | [EQ_TYPE]       | [EQ_SEVERITY]  | [EQ_DURATION]
Access           | [ACC_GROUPS]    | [ACC_TYPE]      | [ACC_SEVERITY] | [ACC_DURATION]
Quality of Life  | [QOL_GROUPS]    | [QOL_TYPE]      | [QOL_SEVERITY] | [QOL_DURATION]
Health           | [HEALTH_GROUPS] | [HEALTH_TYPE]   | [HEALTH_SEV]   | [HEALTH_DUR]
Education        | [EDU_GROUPS]    | [EDU_TYPE]      | [EDU_SEVERITY] | [EDU_DURATION]

Distributional Effects:
Population Group | Current Status  | Impact          | Net Effect     | Equity Score
-----------------|-----------------|-----------------|----------------|-------------
Low Income       | [LOW_CURR]      | [LOW_IMPACT]    | [LOW_NET]      | [LOW_EQUITY]
Middle Income    | [MID_CURR]      | [MID_IMPACT]    | [MID_NET]      | [MID_EQUITY]
High Income      | [HIGH_CURR]     | [HIGH_IMPACT]   | [HIGH_NET]     | [HIGH_EQUITY]
Vulnerable Groups| [VUL_CURR]      | [VUL_IMPACT]    | [VUL_NET]      | [VUL_EQUITY]
Special Needs    | [SPEC_CURR]     | [SPEC_IMPACT]   | [SPEC_NET]     | [SPEC_EQUITY]

Social Outcomes:
- Employment effects: [EMPLOYMENT_EFFECTS]
- Income distribution: [INCOME_DISTRIBUTION]
- Social cohesion: [SOCIAL_COHESION]
- Community wellbeing: [COMMUNITY_WELLBEING]
- Cultural impacts: [CULTURAL_IMPACTS]

### ENVIRONMENTAL IMPACT ANALYSIS

Environmental Assessment:
Factor           | Current State   | Projected Change| Mitigation     | Monitoring
-----------------|-----------------|-----------------|----------------|------------
Emissions        | [EMIS_CURRENT]  | [EMIS_CHANGE]   | [EMIS_MITIG]   | [EMIS_MON]
Resources        | [RES_CURRENT]   | [RES_CHANGE]    | [RES_MITIG]    | [RES_MON]
Biodiversity     | [BIO_CURRENT]   | [BIO_CHANGE]    | [BIO_MITIG]    | [BIO_MON]
Land Use         | [LAND_CURRENT]  | [LAND_CHANGE]   | [LAND_MITIG]   | [LAND_MON]
Sustainability   | [SUST_CURRENT]  | [SUST_CHANGE]   | [SUST_MITIG]   | [SUST_MON]

Climate Impact:
- GHG emissions: [GHG_EMISSIONS]
- Carbon footprint: [CARBON_FOOTPRINT]
- Climate resilience: [CLIMATE_RESILIENCE]
- Adaptation support: [ADAPTATION_SUPPORT]
- Mitigation contribution: [MITIGATION_CONTRIBUTION]

Resource Efficiency:
- Energy use: [ENERGY_USE]
- Water consumption: [WATER_CONSUMPTION]
- Material efficiency: [MATERIAL_EFFICIENCY]
- Waste generation: [WASTE_GENERATION]
- Circular economy: [CIRCULAR_ECONOMY]

### STAKEHOLDER IMPACT ANALYSIS

Stakeholder Impact Matrix:
Stakeholder Group| Current Position| Expected Impact | Magnitude     | Response
-----------------|-----------------|-----------------|---------------|----------
[STAKEHOLDER_1]  | [POS_1]         | [IMPACT_1]      | [MAG_1]       | [RESP_1]
[STAKEHOLDER_2]  | [POS_2]         | [IMPACT_2]      | [MAG_2]       | [RESP_2]
[STAKEHOLDER_3]  | [POS_3]         | [IMPACT_3]      | [MAG_3]       | [RESP_3]
[STAKEHOLDER_4]  | [POS_4]         | [IMPACT_4]      | [MAG_4]       | [RESP_4]
[STAKEHOLDER_5]  | [POS_5]         | [IMPACT_5]      | [MAG_5]       | [RESP_5]

Regional/Geographic Impact:
Region           | Economic Impact | Social Impact   | Environmental | Overall
-----------------|-----------------|-----------------|---------------|--------
[REGION_1]       | [ECON_1]        | [SOC_1]         | [ENV_1]       | [OVER_1]
[REGION_2]       | [ECON_2]        | [SOC_2]         | [ENV_2]       | [OVER_2]
[REGION_3]       | [ECON_3]        | [SOC_3]         | [ENV_3]       | [OVER_3]
[REGION_4]       | [ECON_4]        | [SOC_4]         | [ENV_4]       | [OVER_4]

### MULTI-CRITERIA ANALYSIS

Integrated Impact Assessment:
Criteria         | Weight          | Score           | Weighted Score| Rationale
-----------------|-----------------|-----------------|---------------|----------
Economic Efficiency| [ECON_WEIGHT] | [ECON_SCORE]    | [ECON_WTSC]   | [ECON_RAT]
Social Equity    | [SOC_WEIGHT]    | [SOC_SCORE]     | [SOC_WTSC]    | [SOC_RAT]
Environmental    | [ENV_WEIGHT]    | [ENV_SCORE]     | [ENV_WTSC]    | [ENV_RAT]
Political Feasibility| [POL_WEIGHT]| [POL_SCORE]     | [POL_WTSC]    | [POL_RAT]
Implementation   | [IMP_WEIGHT]    | [IMP_SCORE]     | [IMP_WTSC]    | [IMP_RAT]
Total Score      | 100%            | -               | [TOTAL_SCORE] | -

Sensitivity Analysis:
Variable         | Base Case       | Best Case       | Worst Case    | Range
-----------------|-----------------|-----------------|---------------|-------
[VAR_1]          | [BASE_1]        | [BEST_1]        | [WORST_1]     | [RANGE_1]
[VAR_2]          | [BASE_2]        | [BEST_2]        | [WORST_2]     | [RANGE_2]
[VAR_3]          | [BASE_3]        | [BEST_3]        | [WORST_3]     | [RANGE_3]

### IMPACT ASSESSMENT OUTPUT

Policy: [POLICY_NAME]
Overall Impact Rating: [IMPACT_RATING]
Primary Benefits: [PRIMARY_BENEFITS]
Primary Concerns: [PRIMARY_CONCERNS]
Net Assessment: [NET_ASSESSMENT]

[COMPLETE_IMPACT_ASSESSMENT]

Impact Summary:
- Economic impact: [ECONOMIC_SUMMARY]
- Social impact: [SOCIAL_SUMMARY]
- Environmental impact: [ENVIRONMENTAL_SUMMARY]
- Distributional effects: [DISTRIBUTION_SUMMARY]
- Overall assessment: [OVERALL_ASSESSMENT]

OUTPUT: Deliver comprehensive impact assessment with:
1. Multi-dimensional impact analysis
2. Quantified costs and benefits
3. Distributional equity evaluation
4. Stakeholder impact mapping
5. Environmental sustainability review
6. Sensitivity analysis
7. Evidence-based recommendations
```

## Variables

### Core Variables
- [POLICY_PROPOSAL] - Specific policy being assessed
- [POLICY_AREA] - Domain of policy
- [GOVERNMENT_LEVEL] - Jurisdiction
- [IMPACT_DIMENSIONS] - Scope of assessment
- [STAKEHOLDER_GROUPS] - Affected parties

### Economic Variables
- [GOV_DIRECT/INDIRECT] - Government fiscal impacts
- [PRIV_DIRECT/INDIRECT] - Private sector effects
- [HOUSE_DIRECT/INDIRECT] - Household impacts
- [LABOR_DIRECT/INDIRECT] - Employment effects
- [GDP_DIRECT/INDIRECT] - Growth impacts

### Social Variables
- [EQ_GROUPS/TYPE/SEVERITY] - Equity impacts
- [ACC_GROUPS/TYPE/SEVERITY] - Access effects
- [QOL_GROUPS/TYPE/SEVERITY] - Quality of life
- [HEALTH_GROUPS/TYPE/SEV] - Health outcomes
- [EDU_GROUPS/TYPE/SEVERITY] - Education impacts

### Environmental Variables
- [EMIS_CURRENT/CHANGE/MITIG] - Emissions
- [RES_CURRENT/CHANGE/MITIG] - Resources
- [BIO_CURRENT/CHANGE/MITIG] - Biodiversity
- [LAND_CURRENT/CHANGE/MITIG] - Land use
- [SUST_CURRENT/CHANGE/MITIG] - Sustainability

## Usage Examples

### Example 1: Carbon Tax Impact
```
POLICY_PROPOSAL: "National carbon tax at $50/tonne CO2"
IMPACT_DIMENSIONS: "Economic, social, environmental"
GOV_DIRECT: "Revenue of $15B annually"
HOUSE_DIRECT: "Average cost increase $300/year"
EMIS_CHANGE: "Projected 12% emissions reduction by 2030"
EQ_GROUPS: "Low-income households disproportionately affected"
```

### Example 2: Universal Childcare Impact
```
POLICY_PROPOSAL: "Universal subsidized childcare program"
STAKEHOLDER_GROUPS: "Parents, children, childcare providers, employers"
LABOR_DIRECT: "Increased workforce participation by 8%"
SOC_IMPACT: "Improved early childhood development outcomes"
IMP_ONETIME: "$2.5B infrastructure investment"
OPS_ANNUAL: "$8B annual operating costs"
```

### Example 3: Transit Expansion Impact
```
POLICY_PROPOSAL: "Regional rapid transit expansion"
ECON_IMPACT: "Construction jobs, reduced congestion costs"
ENV_CHANGE: "Reduced emissions, improved air quality"
REGION_1: "Urban core - high benefit, moderate disruption"
STAKEHOLDER_1: "Commuters - reduced travel time, improved reliability"
```

## Best Practices

1. **Use consistent methodology** - Apply standardized assessment frameworks
2. **Quantify where possible** - Provide measurable impact estimates
3. **Acknowledge uncertainties** - Document assumptions and confidence levels
4. **Consider timeframes** - Distinguish short, medium, and long-term impacts
5. **Assess distribution** - Identify who wins and who loses
6. **Include externalities** - Capture indirect and spillover effects
7. **Conduct sensitivity analysis** - Test robustness of conclusions
8. **Engage stakeholders** - Validate impact assumptions with affected parties
9. **Use comparable metrics** - Enable comparison across policy options
10. **Document thoroughly** - Provide transparent methodology and data sources

## Tips for Success

- Begin with clear impact assessment criteria and metrics
- Use both quantitative data and qualitative insights
- Consider cumulative and interactive effects across dimensions
- Account for behavioral responses and adaptation
- Validate models and assumptions with subject matter experts
- Present results in decision-maker friendly formats
- Include visual representations of key impacts
- Conduct peer review of methodology and findings
- Update assessments as new data becomes available
- Communicate uncertainties clearly and honestly
