---
title: Data Analysis Methods Generator
category: education/Academic Research
tags: [data-science, design, education, research]
use_cases:
  - Creating comprehensive data analysis plans covering statistical analysis, qualitative analysis, and mixed methods approaches for academic research projects.
  - Project planning and execution
  - Strategy development
related_templates:
  - education/curriculum-development.md
  - education/curriculum-development-framework.md
last_updated: 2025-11-09
---

# Data Analysis Methods Generator

## Purpose
Create comprehensive data analysis plans covering statistical analysis, qualitative analysis, and mixed methods approaches for academic research projects.

## Quick Start

### For Researchers & Data Analysts

**Step 1: Define Your Analysis Context**
- Specify your research questions and hypotheses
- Identify study design type (experimental, observational, longitudinal, etc.)
- List all variables: dependent, independent, moderating, mediating, and control variables
- Determine measurement scales and data types collected

**Step 2: Select Analysis Software and Approach**
- Choose primary analysis software (SPSS, R, Python, NVivo, ATLAS.ti, etc.)
- Define analytical paradigm (positivist, interpretivist, pragmatic)
- Specify analysis approach (confirmatory, exploratory, or mixed)
- Set statistical power requirements and effect sizes of interest

**Step 3: Generate Your Analysis Plan**
- Input your specifications into the template variables
- Generate comprehensive analysis framework including:
  - Data preparation and cleaning procedures
  - Descriptive and inferential statistical tests
  - Qualitative coding and theme development protocols
  - Mixed methods integration strategies
  - Quality assurance and reproducibility measures

**Step 4: Implement and Document (Ongoing)**
- Follow generated data preparation procedures
- Execute primary and secondary analyses systematically
- Document decisions and maintain analysis audit trail
- Generate results following reporting standards framework

**Common Use Cases:**
- Pre-registration analysis plans
- Dissertation data analysis chapters
- Statistical analysis protocols for publications
- IRB data management plans
- Reproducible research documentation

## Template

```
You are an expert data analyst and methodologist with extensive experience in quantitative statistics, qualitative analysis, and mixed methods integration. Create a comprehensive data analysis plan based on:

Research Context:
- Research Questions: [RESEARCH_QUESTIONS]
- Study Design: [STUDY_DESIGN_TYPE]
- Data Types: [DATA_TYPES_COLLECTED]
- Sample Size: [SAMPLE_SIZE]
- Variables: [VARIABLE_LIST]
- Analysis Software: [ANALYSIS_SOFTWARE]

### Data Characteristics
- Dependent Variables: [DEPENDENT_VARIABLES]
- Independent Variables: [INDEPENDENT_VARIABLES]
- Moderating Variables: [MODERATING_VARIABLES]
- Mediating Variables: [MEDIATING_VARIABLES]
- Control Variables: [CONTROL_VARIABLES]
- Measurement Scales: [MEASUREMENT_SCALES]

### Analysis Objectives
- Primary Hypotheses: [PRIMARY_HYPOTHESES]
- Secondary Hypotheses: [SECONDARY_HYPOTHESES]
- Exploratory Questions: [EXPLORATORY_QUESTIONS]
- Effect Sizes of Interest: [EFFECT_SIZES]
- Statistical Power: [POWER_REQUIREMENTS]

### Generate a comprehensive data analysis plan

1. DATA ANALYSIS OVERVIEW

### Analysis Philosophy
   • [ANALYTICAL_PARADIGM]: [Positivist/Interpretivist/Pragmatic]
   • [ANALYSIS_APPROACH]: [Confirmatory/Exploratory/Mixed]
   • [STATISTICAL_PHILOSOPHY]: [Frequentist/Bayesian]

### Analysis Software and Tools
   Primary Software: [PRIMARY_SOFTWARE]
   • Version: [SOFTWARE_VERSION]
   • Key packages/modules: [SOFTWARE_PACKAGES]
   • Specialized functions: [SPECIALIZED_FUNCTIONS]

   Secondary Software: [SECONDARY_SOFTWARE]
   • Purpose: [SECONDARY_PURPOSE]
   • Integration approach: [INTEGRATION_METHOD]

### Analysis Team
   • Lead Analyst: [LEAD_ANALYST_ROLE]
   • Statistical Consultant: [STATISTICAL_CONSULTANT]
   • Qualitative Analyst: [QUALITATIVE_ANALYST]
   • Data Management: [DATA_MANAGER]

### Quality Assurance
   • [ANALYSIS_VERIFICATION_PROCEDURES]
   • [INDEPENDENT_ANALYSIS_CHECKS]
   • [CODE_REVIEW_PROCESS]
   • [REPRODUCIBILITY_MEASURES]

2. DATA PREPARATION & MANAGEMENT

### Data Import and Setup
   • [DATA_IMPORT_PROCEDURES]
   • [DATA_FORMAT_CONVERSIONS]
   • [VARIABLE_NAMING_CONVENTIONS]
   • [DATA_STRUCTURE_ORGANIZATION]

### Data Cleaning Procedures

### Outlier Detection
   • [OUTLIER_DETECTION_METHODS]
   • [OUTLIER_CRITERIA]: [Statistical thresholds]
   • [OUTLIER_TREATMENT_STRATEGY]
   • [OUTLIER_SENSITIVITY_ANALYSIS]

### Missing Data Assessment
### Missing Data Patterns
   • [MISSING_DATA_MECHANISM]: [MCAR/MAR/MNAR]
   • [MISSING_DATA_TESTS]: [Little's MCAR test, etc.]
   • [MISSING_DATA_VISUALIZATION]
   • [MISSING_DATA_PATTERNS_ANALYSIS]

### Missing Data Treatment
   • [LISTWISE_DELETION_CONDITIONS]
   • [IMPUTATION_METHODS]: [Mean/Median/Mode/Multiple/Model-based]
   • [IMPUTATION_SOFTWARE]: [Specific packages/procedures]
   • [IMPUTATION_DIAGNOSTICS]
   • [SENSITIVITY_ANALYSIS_MISSING]

### Data Transformation
### Variable Transformations
   • [TRANSFORMATION_1]: [Log/Square root/Reciprocal] for [VARIABLE_1]
   • [TRANSFORMATION_2]: [Normalization/Standardization] for [VARIABLE_2]
   • [TRANSFORMATION_3]: [Categorical recoding] for [VARIABLE_3]

### Composite Variable Creation
   • [COMPOSITE_VARIABLE_1]: [Calculation method]
   • [COMPOSITE_VARIABLE_2]: [Aggregation approach]
   • [SCALE_RELIABILITY_ASSESSMENT]

### Data Quality Checks
   • [RANGE_CHECKS]: [Acceptable value ranges]
   • [CONSISTENCY_CHECKS]: [Cross-variable validation]
   • [LOGIC_CHECKS]: [Logical relationship verification]
   • [DUPLICATE_DETECTION]: [Identification procedures]

3. DESCRIPTIVE ANALYSIS PLAN

### Sample Description

### Demographic Analysis
   • [DEMOGRAPHIC_VARIABLE_1]: [Frequency/Percentage/Mean ± SD]
   • [DEMOGRAPHIC_VARIABLE_2]: [Median/IQR/Range]
   • [DEMOGRAPHIC_VARIABLE_3]: [Mode/Distribution shape]

### Sample Characteristics
   • [SAMPLE_SIZE_BREAKDOWN]: By [GROUPING_VARIABLE]
   • [ATTRITION_ANALYSIS]: [Dropout patterns and reasons]
   • [REPRESENTATIVENESS_ASSESSMENT]: [Comparison to population]

### Variable Distributions

### Continuous Variables
   For each [CONTINUOUS_VARIABLE]:
   • Measures of central tendency: [Mean/Median/Mode]
   • Measures of dispersion: [SD/Variance/Range/IQR]
   • Distribution shape: [Skewness/Kurtosis/Visual inspection]
   • Normality assessment: [Shapiro-Wilk/Kolmogorov-Smirnov]

### Categorical Variables
   For each [CATEGORICAL_VARIABLE]:
   • Frequency distributions: [Counts and percentages]
   • Cross-tabulations: [With key grouping variables]
   • Missing data summary: [Patterns and percentages]

### Correlation Analysis

### Bivariate Correlations
   • [CORRELATION_METHOD]: [Pearson/Spearman/Kendall's tau]
   • [CORRELATION_MATRIX]: All continuous variables
   • [CORRELATION_SIGNIFICANCE]: [Bonferroni/FDR correction]

### Association Measures
   • [CATEGORICAL_ASSOCIATIONS]: [Chi-square/Cramér's V/Phi]
   • [MIXED_ASSOCIATIONS]: [Point-biserial/Eta-squared]

### Data Visualization
   • [HISTOGRAM_DISTRIBUTIONS]: For all continuous variables
   • [BOXPLOT_COMPARISONS]: By grouping variables
   • [SCATTERPLOT_RELATIONSHIPS]: For key variable pairs
   • [BAR_CHARTS]: For categorical variables

4. STATISTICAL ASSUMPTIONS TESTING

### Parametric Assumptions

### Normality Testing
   • [NORMALITY_TESTS]: [Shapiro-Wilk/Anderson-Darling/Jarque-Bera]
   • [NORMALITY_CRITERIA]: [p-value thresholds]
   • [NORMALITY_VISUALIZATION]: [Q-Q plots/Histograms]
   • [NORMALITY_TRANSFORMATION]: If violated

### Homogeneity of Variance
   • [HOMOGENEITY_TESTS]: [Levene's/Bartlett's/Brown-Forsythe]
   • [HOMOGENEITY_CRITERIA]: [Test statistics and p-values]
   • [HOMOGENEITY_REMEDIATION]: [Welch's correction/Transformations]

### Independence of Observations
   • [INDEPENDENCE_ASSESSMENT]: [Durbin-Watson/Visual inspection]
   • [CLUSTERING_EFFECTS]: [ICC/Design effect calculations]
   • [INDEPENDENCE_VIOLATIONS]: [Mixed models consideration]

### Linearity Assessment
   • [LINEARITY_TESTS]: [Rainbow test/Harvey-Collier test]
   • [LINEARITY_VISUALIZATION]: [Residual plots/Scatterplots]
   • [NONLINEARITY_MODELING]: [Polynomial/Spline terms]

### Multicollinearity Detection
   • [MULTICOLLINEARITY_MEASURES]: [VIF/Tolerance/Condition index]
   • [MULTICOLLINEARITY_THRESHOLDS]: [VIF > 10, Tolerance < 0.1]
   • [MULTICOLLINEARITY_REMEDIATION]: [Variable selection/Ridge regression]

5. PRIMARY STATISTICAL ANALYSIS

### Hypothesis Testing Framework
   • [SIGNIFICANCE_LEVEL]: α = [ALPHA_LEVEL]
   • [MULTIPLE_COMPARISONS]: [Bonferroni/Holm/FDR adjustment]
   • [EFFECT_SIZE_MEASURES]: [Cohen's d/Eta-squared/R-squared]
   • [CONFIDENCE_INTERVALS]: [CONFIDENCE_LEVEL]% CIs

   Primary Analysis for [PRIMARY_HYPOTHESIS_1]:

   Statistical Test: [PRIMARY_TEST_1]
   • Test rationale: [TEST_JUSTIFICATION_1]
   • Assumptions checked: [ASSUMPTION_LIST_1]
   • Effect size: [EFFECT_SIZE_MEASURE_1]
   • Power analysis: [POST_HOC_POWER_1]

### Analysis Procedure
   1. [ANALYSIS_STEP_1_1]
   2. [ANALYSIS_STEP_1_2]
   3. [ANALYSIS_STEP_1_3]
   4. [ANALYSIS_STEP_1_4]

### Interpretation Framework
   • [STATISTICAL_SIGNIFICANCE_INTERPRETATION]
   • [PRACTICAL_SIGNIFICANCE_INTERPRETATION]
   • [CONFIDENCE_INTERVAL_INTERPRETATION]

   Primary Analysis for [PRIMARY_HYPOTHESIS_2]:

   Statistical Test: [PRIMARY_TEST_2]
   • Test rationale: [TEST_JUSTIFICATION_2]
   • Assumptions checked: [ASSUMPTION_LIST_2]
   • Effect size: [EFFECT_SIZE_MEASURE_2]
   • Power analysis: [POST_HOC_POWER_2]

### Model Specification
   • [MODEL_EQUATION]: Mathematical representation
   • [MODEL_PARAMETERS]: [Parameter interpretation]
   • [MODEL_ASSUMPTIONS]: [Specific to this analysis]

### Advanced Statistical Techniques

### Regression Analysis
   Model Type: [LINEAR/LOGISTIC/POISSON/NEGATIVE_BINOMIAL]

### Model Building Strategy
   • [VARIABLE_SELECTION_METHOD]: [Forward/Backward/Stepwise/Theory-driven]
   • [MODEL_COMPARISON_CRITERIA]: [AIC/BIC/Cross-validation]
   • [INTERACTION_TESTING]: [Planned interactions]
   • [MODEL_VALIDATION]: [Cross-validation/Bootstrap]

### Multivariate Analysis
   • [MULTIVARIATE_METHOD]: [MANOVA/Discriminant/Factor/Cluster]
   • [MULTIVARIATE_ASSUMPTIONS]: [Specific checks]
   • [DIMENSION_REDUCTION]: [PCA/Factor analysis]

   Time Series Analysis (if applicable):
   • [TIME_SERIES_METHOD]: [ARIMA/VAR/State-space]
   • [STATIONARITY_TESTING]: [ADF/KPSS tests]
   • [SEASONALITY_ASSESSMENT]: [Seasonal decomposition]
   • [FORECASTING_APPROACH]: [Method and validation]

6. SECONDARY & EXPLORATORY ANALYSIS

### Secondary Hypotheses Testing

   Analysis for [SECONDARY_HYPOTHESIS_1]:
   • [SECONDARY_TEST_1]: [Test description]
   • [SECONDARY_RATIONALE_1]: [Why this test]
   • [SECONDARY_INTERPRETATION_1]: [How to interpret]

   Analysis for [SECONDARY_HYPOTHESIS_2]:
   • [SECONDARY_TEST_2]: [Test description]
   • [SECONDARY_RATIONALE_2]: [Why this test]
   • [SECONDARY_INTERPRETATION_2]: [How to interpret]

### Exploratory Data Analysis

### Data Mining Approaches
   • [CLUSTERING_ANALYSIS]: [K-means/Hierarchical/DBSCAN]
   • [CLASSIFICATION_TREES]: [Decision trees/Random forest]
   • [PATTERN_RECOGNITION]: [Association rules/Sequence analysis]

### Subgroup Analysis
### Planned Subgroups
   • [SUBGROUP_1]: [Definition and analysis approach]
   • [SUBGROUP_2]: [Definition and analysis approach]
   • [SUBGROUP_INTERACTION_TESTS]

   Post-hoc Analysis:
   • [POST_HOC_COMPARISONS]: [Tukey/Scheffe/Bonferroni]
   • [POST_HOC_CONTRASTS]: [Planned/Unplanned comparisons]
   • [POST_HOC_POWER]: [Observed power calculations]

### Sensitivity Analysis
   • [SENSITIVITY_SCENARIO_1]: [Alternative analysis approach]
   • [SENSITIVITY_SCENARIO_2]: [Robustness check]
   • [SENSITIVITY_INTERPRETATION]: [How to interpret differences]

7. QUALITATIVE ANALYSIS PLAN

### Qualitative Data Types
   • [QUALITATIVE_DATA_TYPE_1]: [Interviews/Focus groups/Observations]
   • [QUALITATIVE_DATA_TYPE_2]: [Documents/Artifacts/Media]
   • [QUALITATIVE_DATA_VOLUME]: [Hours/Pages/Files]

### Analysis Methodology

   Primary Approach: [THEMATIC/CONTENT/NARRATIVE/GROUNDED_THEORY/PHENOMENOLOGICAL]

### Philosophical Foundation
   • [ONTOLOGICAL_POSITION]: [Realist/Relativist/Critical realist]
   • [EPISTEMOLOGICAL_STANCE]: [Objectivist/Constructivist/Subjectivist]
   • [THEORETICAL_FRAMEWORK]: [Inductive/Deductive/Abductive]

### Data Preparation

### Transcription Procedures
   • [TRANSCRIPTION_STYLE]: [Verbatim/Intelligent/Detailed]
   • [TRANSCRIPTION_NOTATION]: [Jefferson/Simplified/Custom]
   • [TRANSCRIPTION_QUALITY]: [Accuracy checks/Verification]
   • [TRANSCRIPTION_SOFTWARE]: [Software used]

### Data Organization
   • [DATA_MANAGEMENT_SYSTEM]: [File organization structure]
   • [CODING_SOFTWARE]: [NVivo/Atlas.ti/MAXQDA/Dedoose]
   • [BACKUP_PROCEDURES]: [Data security measures]
   • [VERSION_CONTROL]: [File version management]

### Coding Procedures

   Phase 1: Initial Coding
   Coding Approach: [OPEN/AXIAL/SELECTIVE/IN_VIVO]
   • [CODING_UNIT]: [Word/Phrase/Sentence/Paragraph]
   • [CODING_STRATEGY]: [Line-by-line/Incident-by-incident]
   • [INITIAL_CODE_DEVELOPMENT]: [Process description]

   Phase 2: Focused Coding
   • [FOCUSED_CODING_CRITERIA]: [Selection criteria]
   • [CODE_REFINEMENT_PROCESS]: [How codes are refined]
   • [CATEGORY_DEVELOPMENT]: [Grouping procedures]

   Phase 3: Theoretical Coding
   • [THEORETICAL_INTEGRATION]: [Theory building approach]
   • [RELATIONSHIP_IDENTIFICATION]: [Between categories]
   • [CORE_CATEGORY_SELECTION]: [Central organizing concept]

   Inter-coder Reliability:
   • [RELIABILITY_APPROACH]: [Percent agreement/Cohen's kappa/Krippendorff's alpha]
   • [RELIABILITY_THRESHOLD]: [Acceptable agreement level]
   • [DISAGREEMENT_RESOLUTION]: [Consensus procedures]
   • [RELIABILITY_REPORTING]: [How reported in results]

### Theme Development

### Theme Identification
   • [THEME_DEFINITION_CRITERIA]: [What constitutes a theme]
   • [THEME_PREVALENCE]: [Frequency vs. importance]
   • [THEME_COHERENCE]: [Internal consistency]
   • [THEME_DISTINCTIVENESS]: [Clear boundaries]

### Theme Refinement
   • [THEME_REVIEW_PROCESS]: [Multiple review stages]
   • [THEME_VALIDATION]: [Data fit assessment]
   • [THEME_NAMING]: [Clear and concise labels]
   • [THEME_HIERARCHY]: [Main themes and subthemes]

### Analysis Quality Assurance

### Trustworthiness Criteria
### Credibility
   • [PROLONGED_ENGAGEMENT]: [Time in field/with data]
   • [TRIANGULATION]: [Data/Method/Investigator/Theory]
   • [MEMBER_CHECKING]: [Participant validation]
   • [PEER_DEBRIEFING]: [External perspective]

### Transferability
   • [THICK_DESCRIPTION]: [Rich contextual details]
   • [PURPOSIVE_SAMPLING]: [Maximum variation]
   • [CONTEXTUAL_INFORMATION]: [Setting description]

### Dependability
   • [AUDIT_TRAIL]: [Decision documentation]
   • [METHODOLOGICAL_CONSISTENCY]: [Process stability]
   • [EXTERNAL_AUDITING]: [Independent review]

### Confirmability
   • [REFLEXIVITY]: [Researcher self-awareness]
   • [BIAS_ACKNOWLEDGMENT]: [Assumption examination]
   • [DATA_GROUNDING]: [Evidence-based conclusions]

8. MIXED METHODS INTEGRATION

### Integration Strategy

   Design Type: [CONVERGENT/SEQUENTIAL_EXPLANATORY/SEQUENTIAL_EXPLORATORY/EMBEDDED]

### Integration Approach
   • [INTEGRATION_TIMING]: [Concurrent/Sequential]
   • [INTEGRATION_EMPHASIS]: [Equal/Quantitative priority/Qualitative priority]
   • [INTEGRATION_PROCEDURES]: [Specific methods]

### Data Transformation

### Quantification of Qualitative Data
   • [QUANTIFICATION_METHOD]: [Counting/Scaling/Typology creation]
   • [QUANTIFICATION_PURPOSE]: [Statistical analysis/Comparison]
   • [QUANTIFICATION_VALIDATION]: [Quality checks]

### Qualification of Quantitative Data
   • [QUALIFICATION_APPROACH]: [Narrative/Case selection]
   • [QUALIFICATION_PURPOSE]: [Explanation/Exploration]
   • [QUALIFICATION_CRITERIA]: [Selection procedures]

### Comparative Analysis

### Convergence Assessment
   • [CONVERGENCE_CRITERIA]: [Agreement standards]
   • [CONVERGENCE_ANALYSIS]: [Side-by-side comparison]
   • [CONVERGENCE_INTERPRETATION]: [Meaning of agreement]

### Divergence Exploration
   • [DIVERGENCE_IDENTIFICATION]: [Discrepancy detection]
   • [DIVERGENCE_EXPLANATION]: [Reason exploration]
   • [DIVERGENCE_RESOLUTION]: [Integration approach]

### Joint Displays
   • [JOINT_DISPLAY_TYPE]: [Comparison/Expansion/Integration]
   • [JOINT_DISPLAY_CONTENT]: [What is displayed]
   • [JOINT_DISPLAY_PURPOSE]: [Integration goal]

   Meta-inferences:
   • [META_INFERENCE_DEVELOPMENT]: [Higher-order interpretation]
   • [META_INFERENCE_VALIDATION]: [Quality assessment]
   • [META_INFERENCE_IMPLICATIONS]: [Broader meaning]

9. ADVANCED ANALYTICAL TECHNIQUES

### Machine Learning Approaches

### Supervised Learning
   • [SUPERVISED_METHOD_1]: [Random Forest/SVM/Neural Networks]
   • [SUPERVISED_PURPOSE_1]: [Prediction/Classification goal]
   • [SUPERVISED_VALIDATION_1]: [Cross-validation approach]

### Unsupervised Learning
   • [UNSUPERVISED_METHOD_1]: [Clustering/Dimensionality reduction]
   • [UNSUPERVISED_PURPOSE_1]: [Pattern discovery goal]
   • [UNSUPERVISED_EVALUATION_1]: [Quality metrics]

### Longitudinal Analysis

### Growth Curve Modeling
   • [GROWTH_MODEL_TYPE]: [Linear/Quadratic/Piecewise]
   • [GROWTH_PARAMETERS]: [Intercept/Slope/Acceleration]
   • [GROWTH_PREDICTORS]: [Time-invariant/Time-varying]

### Survival Analysis
   • [SURVIVAL_METHOD]: [Kaplan-Meier/Cox regression/Parametric]
   • [SURVIVAL_ASSUMPTIONS]: [Proportional hazards/Competing risks]
   • [SURVIVAL_INTERPRETATION]: [Hazard ratios/Survival curves]

### Structural Equation Modeling
   • [SEM_MODEL_TYPE]: [Confirmatory/Exploratory/Path analysis]
   • [SEM_ESTIMATION]: [Maximum likelihood/Robust methods]
   • [SEM_FIT_INDICES]: [CFI/RMSEA/SRMR/Chi-square]

### Multilevel Analysis
   • [MULTILEVEL_STRUCTURE]: [Level definitions]
   • [MULTILEVEL_EFFECTS]: [Fixed/Random effects]
   • [MULTILEVEL_ASSUMPTIONS]: [Residual structure]

10. REPORTING & INTERPRETATION FRAMEWORK

### Statistical Reporting Standards

### Descriptive Statistics
    • [DESCRIPTIVE_REPORTING]: [M ± SD, Median (IQR), n (%)]
    • [MISSING_DATA_REPORTING]: [Patterns and handling]
    • [SAMPLE_CHARACTERISTICS]: [Demographic tables]

### Inferential Statistics
    • [TEST_STATISTIC_REPORTING]: [Statistic, df, p-value]
    • [EFFECT_SIZE_REPORTING]: [Point estimate and CI]
    • [ASSUMPTION_REPORTING]: [Violations and handling]

### Model Results
    • [MODEL_FIT_REPORTING]: [Goodness-of-fit measures]
    • [PARAMETER_REPORTING]: [Estimates, SE, p-values]
    • [MODEL_COMPARISON]: [Information criteria]

### Qualitative Reporting

### Theme Presentation
    • [THEME_ORGANIZATION]: [Hierarchical/Narrative structure]
    • [QUOTE_SELECTION]: [Representative examples]
    • [PARTICIPANT_ATTRIBUTION]: [Anonymous identification]

### Process Description
    • [ANALYSIS_TRANSPARENCY]: [Decision documentation]
    • [REFLEXIVITY_REPORTING]: [Researcher influence]
    • [QUALITY_EVIDENCE]: [Trustworthiness demonstration]

### Interpretation Guidelines

### Statistical Interpretation
    • [STATISTICAL_VS_PRACTICAL]: [Significance vs. importance]
    • [CONFIDENCE_INTERVAL_USE]: [Precision estimation]
    • [P_VALUE_INTERPRETATION]: [Null hypothesis testing]

### Qualitative Interpretation
    • [MEANING_MAKING]: [Theoretical integration]
    • [CONTEXT_CONSIDERATION]: [Situational factors]
    • [PARTICIPANT_VOICE]: [Authentic representation]

### Mixed Methods Integration
    • [INTEGRATION_REPORTING]: [Joint findings presentation]
    • [CONVERGENCE_DIVERGENCE]: [Agreement/Disagreement discussion]
    • [META_INFERENCE_PRESENTATION]: [Higher-order conclusions]

11. QUALITY CONTROL & VALIDATION

### Analytical Quality Assurance

### Code Verification
    • [CODE_REVIEW_PROCESS]: [Peer review procedures]
    • [CODE_DOCUMENTATION]: [Comment standards]
    • [CODE_TESTING]: [Output verification]

### Result Validation
    • [INDEPENDENT_ANALYSIS]: [Parallel analysis procedures]
    • [RESULT_COMPARISON]: [Cross-validation methods]
    • [SENSITIVITY_TESTING]: [Robustness checks]

### Reproducibility Measures
    • [ANALYSIS_DOCUMENTATION]: [Step-by-step procedures]
    • [DATA_AVAILABILITY]: [Sharing protocols]
    • [CODE_SHARING]: [Analysis script availability]

### Error Detection
    • [ERROR_CHECKING_PROCEDURES]: [Systematic review]
    • [OUTLIER_INVESTIGATION]: [Extreme value examination]
    • [LOGIC_VALIDATION]: [Results reasonableness]

12. ANALYSIS TIMELINE & MILESTONES

### Analysis Phases

    Phase 1: Data Preparation ([PREP_TIMELINE])
    • [PREP_MILESTONE_1]: [Data cleaning completion]
    • [PREP_MILESTONE_2]: [Assumption testing completion]
    • [PREP_DELIVERABLE]: [Clean dataset and documentation]

    Phase 2: Primary Analysis ([PRIMARY_TIMELINE])
    • [PRIMARY_MILESTONE_1]: [Hypothesis testing completion]
    • [PRIMARY_MILESTONE_2]: [Primary results interpretation]
    • [PRIMARY_DELIVERABLE]: [Primary analysis report]

    Phase 3: Secondary Analysis ([SECONDARY_TIMELINE])
    • [SECONDARY_MILESTONE_1]: [Exploratory analysis completion]
    • [SECONDARY_MILESTONE_2]: [Additional findings documentation]
    • [SECONDARY_DELIVERABLE]: [Comprehensive results]

    Phase 4: Integration & Reporting ([INTEGRATION_TIMELINE])
    • [INTEGRATION_MILESTONE_1]: [Mixed methods integration]
    • [INTEGRATION_MILESTONE_2]: [Final report preparation]
    • [INTEGRATION_DELIVERABLE]: [Complete analysis report]

### Ensure the analysis plan is
- Methodologically rigorous and appropriate
- Aligned with research questions and hypotheses
- Transparent and reproducible
- Comprehensive in scope
- Feasible within resource constraints
- Compliant with disciplinary standards
```

## Variables

### Research Context
- `[RESEARCH_QUESTIONS]`: Primary and secondary research questions
- `[STUDY_DESIGN_TYPE]`: Type of research design employed
- `[DATA_TYPES_COLLECTED]`: Types of data collected in the study
- `[SAMPLE_SIZE]`: Total sample size for analysis
- `[VARIABLE_LIST]`: Comprehensive list of all variables
- `[ANALYSIS_SOFTWARE]`: Primary software for data analysis
- `[DEPENDENT_VARIABLES]`: Outcome variables in the study
- `[INDEPENDENT_VARIABLES]`: Predictor variables
- `[MODERATING_VARIABLES]`: Variables that modify relationships
- `[MEDIATING_VARIABLES]`: Variables that explain relationships
- `[CONTROL_VARIABLES]`: Variables held constant
- `[MEASUREMENT_SCALES]`: Scale types for each variable
- `[PRIMARY_HYPOTHESES]`: Main hypotheses to be tested
- `[SECONDARY_HYPOTHESES]`: Secondary hypotheses
- `[EXPLORATORY_QUESTIONS]`: Questions for exploratory analysis
- `[EFFECT_SIZES]`: Expected or important effect sizes
- `[POWER_REQUIREMENTS]`: Statistical power requirements

### Analysis Framework
- `[ANALYTICAL_PARADIGM]`: Overall analytical philosophy
- `[ANALYSIS_APPROACH]`: Confirmatory or exploratory approach
- `[STATISTICAL_PHILOSOPHY]`: Frequentist or Bayesian framework
- `[PRIMARY_SOFTWARE]`: Main statistical software package
- `[SOFTWARE_VERSION]`: Version of primary software
- `[SOFTWARE_PACKAGES]`: Specific packages or modules used
- `[SPECIALIZED_FUNCTIONS]`: Special functions or procedures
- `[SECONDARY_SOFTWARE]`: Additional software tools
- `[SECONDARY_PURPOSE]`: Purpose of secondary software
- `[INTEGRATION_METHOD]`: Method for integrating software tools
- `[LEAD_ANALYST_ROLE]`: Role of lead data analyst
- `[STATISTICAL_CONSULTANT]`: Statistical consultant involvement
- `[QUALITATIVE_ANALYST]`: Qualitative analysis expertise
- `[DATA_MANAGER]`: Data management responsibilities

### Quality Assurance
- `[ANALYSIS_VERIFICATION_PROCEDURES]`: Procedures for verifying analysis
- `[INDEPENDENT_ANALYSIS_CHECKS]`: Independent verification methods
- `[CODE_REVIEW_PROCESS]`: Process for reviewing analysis code
- `[REPRODUCIBILITY_MEASURES]`: Measures to ensure reproducibility

### Data Preparation
- `[DATA_IMPORT_PROCEDURES]`: Procedures for importing data
- `[DATA_FORMAT_CONVERSIONS]`: Format conversion requirements
- `[VARIABLE_NAMING_CONVENTIONS]`: Conventions for variable names
- `[DATA_STRUCTURE_ORGANIZATION]`: Organization of data structure
- `[OUTLIER_DETECTION_METHODS]`: Methods for detecting outliers
- `[OUTLIER_CRITERIA]`: Criteria for defining outliers
- `[OUTLIER_TREATMENT_STRATEGY]`: Strategy for handling outliers
- `[OUTLIER_SENSITIVITY_ANALYSIS]`: Sensitivity analysis for outliers
- `[MISSING_DATA_MECHANISM]`: Mechanism of missing data
- `[MISSING_DATA_TESTS]`: Tests for missing data patterns
- `[MISSING_DATA_VISUALIZATION]`: Visualization of missing data
- `[MISSING_DATA_PATTERNS_ANALYSIS]`: Analysis of missing patterns
- `[LISTWISE_DELETION_CONDITIONS]`: Conditions for listwise deletion
- `[IMPUTATION_METHODS]`: Methods for data imputation
- `[IMPUTATION_SOFTWARE]`: Software for imputation
- `[IMPUTATION_DIAGNOSTICS]`: Diagnostic procedures for imputation
- `[SENSITIVITY_ANALYSIS_MISSING]`: Sensitivity analysis for missing data

### Data Transformation
- `[TRANSFORMATION_1]`: First variable transformation
- `[TRANSFORMATION_2]`: Second variable transformation
- `[TRANSFORMATION_3]`: Third variable transformation
- `[VARIABLE_1]`: First variable to be transformed
- `[VARIABLE_2]`: Second variable to be transformed
- `[VARIABLE_3]`: Third variable to be transformed
- `[COMPOSITE_VARIABLE_1]`: First composite variable
- `[COMPOSITE_VARIABLE_2]`: Second composite variable
- `[SCALE_RELIABILITY_ASSESSMENT]`: Assessment of scale reliability
- `[RANGE_CHECKS]`: Procedures for checking value ranges
- `[CONSISTENCY_CHECKS]`: Cross-variable consistency checks
- `[LOGIC_CHECKS]`: Logical relationship verification
- `[DUPLICATE_DETECTION]`: Procedures for detecting duplicates

### Descriptive Analysis
- `[DEMOGRAPHIC_VARIABLE_1]`: First demographic variable
- `[DEMOGRAPHIC_VARIABLE_2]`: Second demographic variable
- `[DEMOGRAPHIC_VARIABLE_3]`: Third demographic variable
- `[SAMPLE_SIZE_BREAKDOWN]`: Breakdown of sample size by groups
- `[GROUPING_VARIABLE]`: Variable used for grouping
- `[ATTRITION_ANALYSIS]`: Analysis of participant attrition
- `[REPRESENTATIVENESS_ASSESSMENT]`: Assessment of sample representativeness
- `[CONTINUOUS_VARIABLE]`: Continuous variables for analysis
- `[CATEGORICAL_VARIABLE]`: Categorical variables for analysis
- `[CORRELATION_METHOD]`: Method for correlation analysis
- `[CORRELATION_MATRIX]`: Correlation matrix specifications
- `[CORRELATION_SIGNIFICANCE]`: Significance testing for correlations
- `[CATEGORICAL_ASSOCIATIONS]`: Association measures for categories
- `[MIXED_ASSOCIATIONS]`: Association measures for mixed variables
- `[HISTOGRAM_DISTRIBUTIONS]`: Histogram specifications
- `[BOXPLOT_COMPARISONS]`: Boxplot comparison specifications
- `[SCATTERPLOT_RELATIONSHIPS]`: Scatterplot specifications
- `[BAR_CHARTS]`: Bar chart specifications

### Statistical Assumptions
- `[NORMALITY_TESTS]`: Tests for normality assumption
- `[NORMALITY_CRITERIA]`: Criteria for assessing normality
- `[NORMALITY_VISUALIZATION]`: Visualization for normality check
- `[NORMALITY_TRANSFORMATION]`: Transformation for normality
- `[HOMOGENEITY_TESTS]`: Tests for homogeneity of variance
- `[HOMOGENEITY_CRITERIA]`: Criteria for homogeneity
- `[HOMOGENEITY_REMEDIATION]`: Remediation for heterogeneity
- `[INDEPENDENCE_ASSESSMENT]`: Assessment of independence
- `[CLUSTERING_EFFECTS]`: Assessment of clustering effects
- `[INDEPENDENCE_VIOLATIONS]`: Handling independence violations
- `[LINEARITY_TESTS]`: Tests for linearity assumption
- `[LINEARITY_VISUALIZATION]`: Visualization for linearity
- `[NONLINEARITY_MODELING]`: Modeling nonlinear relationships
- `[MULTICOLLINEARITY_MEASURES]`: Measures of multicollinearity
- `[MULTICOLLINEARITY_THRESHOLDS]`: Thresholds for multicollinearity
- `[MULTICOLLINEARITY_REMEDIATION]`: Remediation for multicollinearity

### Primary Statistical Analysis
- `[SIGNIFICANCE_LEVEL]`: Statistical significance level
- `[ALPHA_LEVEL]`: Alpha level for hypothesis testing
- `[MULTIPLE_COMPARISONS]`: Adjustment for multiple comparisons
- `[EFFECT_SIZE_MEASURES]`: Effect size measures used
- `[CONFIDENCE_INTERVALS]`: Confidence interval specifications
- `[CONFIDENCE_LEVEL]`: Confidence level for intervals
- `[PRIMARY_HYPOTHESIS_1]`: First primary hypothesis
- `[PRIMARY_TEST_1]`: Statistical test for first hypothesis
- `[TEST_JUSTIFICATION_1]`: Justification for first test
- `[ASSUMPTION_LIST_1]`: Assumptions for first test
- `[EFFECT_SIZE_MEASURE_1]`: Effect size measure for first test
- `[POST_HOC_POWER_1]`: Post-hoc power for first test
- `[ANALYSIS_STEP_1_1]`: First analysis step
- `[ANALYSIS_STEP_1_2]`: Second analysis step
- `[ANALYSIS_STEP_1_3]`: Third analysis step
- `[ANALYSIS_STEP_1_4]`: Fourth analysis step
- `[STATISTICAL_SIGNIFICANCE_INTERPRETATION]`: Interpretation of statistical significance
- `[PRACTICAL_SIGNIFICANCE_INTERPRETATION]`: Interpretation of practical significance
- `[CONFIDENCE_INTERVAL_INTERPRETATION]`: Interpretation of confidence intervals

### Secondary Analysis
- `[PRIMARY_HYPOTHESIS_2]`: Second primary hypothesis
- `[PRIMARY_TEST_2]`: Statistical test for second hypothesis
- `[TEST_JUSTIFICATION_2]`: Justification for second test
- `[ASSUMPTION_LIST_2]`: Assumptions for second test
- `[EFFECT_SIZE_MEASURE_2]`: Effect size measure for second test
- `[POST_HOC_POWER_2]`: Post-hoc power for second test
- `[MODEL_EQUATION]`: Mathematical model equation
- `[MODEL_PARAMETERS]`: Model parameter interpretation
- `[MODEL_ASSUMPTIONS]`: Model-specific assumptions
- `[LINEAR/LOGISTIC/POISSON/NEGATIVE_BINOMIAL]`: Regression model type
- `[VARIABLE_SELECTION_METHOD]`: Method for variable selection
- `[MODEL_COMPARISON_CRITERIA]`: Criteria for model comparison
- `[INTERACTION_TESTING]`: Testing of interaction effects
- `[MODEL_VALIDATION]`: Model validation procedures
- `[MULTIVARIATE_METHOD]`: Multivariate analysis method
- `[MULTIVARIATE_ASSUMPTIONS]`: Multivariate analysis assumptions
- `[DIMENSION_REDUCTION]`: Dimension reduction techniques

### Time Series Analysis
- `[TIME_SERIES_METHOD]`: Time series analysis method
- `[STATIONARITY_TESTING]`: Tests for stationarity
- `[SEASONALITY_ASSESSMENT]`: Assessment of seasonality
- `[FORECASTING_APPROACH]`: Forecasting methodology

### Secondary and Exploratory Analysis
- `[SECONDARY_HYPOTHESIS_1]`: First secondary hypothesis
- `[SECONDARY_TEST_1]`: Test for first secondary hypothesis
- `[SECONDARY_RATIONALE_1]`: Rationale for first secondary test
- `[SECONDARY_INTERPRETATION_1]`: Interpretation of first secondary test
- `[SECONDARY_HYPOTHESIS_2]`: Second secondary hypothesis
- `[SECONDARY_TEST_2]`: Test for second secondary hypothesis
- `[SECONDARY_RATIONALE_2]`: Rationale for second secondary test
- `[SECONDARY_INTERPRETATION_2]`: Interpretation of second secondary test
- `[CLUSTERING_ANALYSIS]`: Clustering analysis method
- `[CLASSIFICATION_TREES]`: Classification tree methods
- `[PATTERN_RECOGNITION]`: Pattern recognition techniques
- `[SUBGROUP_1]`: First subgroup definition
- `[SUBGROUP_2]`: Second subgroup definition
- `[SUBGROUP_INTERACTION_TESTS]`: Subgroup interaction testing
- `[POST_HOC_COMPARISONS]`: Post-hoc comparison methods
- `[POST_HOC_CONTRASTS]`: Post-hoc contrast testing
- `[POST_HOC_POWER]`: Post-hoc power calculations
- `[SENSITIVITY_SCENARIO_1]`: First sensitivity analysis scenario
- `[SENSITIVITY_SCENARIO_2]`: Second sensitivity analysis scenario
- `[SENSITIVITY_INTERPRETATION]`: Interpretation of sensitivity analysis

### Qualitative Analysis
- `[QUALITATIVE_DATA_TYPE_1]`: First type of qualitative data
- `[QUALITATIVE_DATA_TYPE_2]`: Second type of qualitative data
- `[QUALITATIVE_DATA_VOLUME]`: Volume of qualitative data
- `[THEMATIC/CONTENT/NARRATIVE/GROUNDED_THEORY/PHENOMENOLOGICAL]`: Qualitative analysis approach
- `[ONTOLOGICAL_POSITION]`: Ontological position taken
- `[EPISTEMOLOGICAL_STANCE]`: Epistemological stance adopted
- `[THEORETICAL_FRAMEWORK]`: Theoretical framework for analysis
- `[TRANSCRIPTION_STYLE]`: Style of transcription
- `[TRANSCRIPTION_NOTATION]`: Notation system for transcription
- `[TRANSCRIPTION_QUALITY]`: Quality control for transcription
- `[TRANSCRIPTION_SOFTWARE]`: Software for transcription
- `[DATA_MANAGEMENT_SYSTEM]`: System for managing qualitative data
- `[CODING_SOFTWARE]`: Software for qualitative coding
- `[BACKUP_PROCEDURES]`: Backup procedures for qualitative data
- `[VERSION_CONTROL]`: Version control for qualitative files

### Coding Procedures
- `[OPEN/AXIAL/SELECTIVE/IN_VIVO]`: Type of coding approach
- `[CODING_UNIT]`: Unit of analysis for coding
- `[CODING_STRATEGY]`: Strategy for coding data
- `[INITIAL_CODE_DEVELOPMENT]`: Process for developing initial codes
- `[FOCUSED_CODING_CRITERIA]`: Criteria for focused coding
- `[CODE_REFINEMENT_PROCESS]`: Process for refining codes
- `[CATEGORY_DEVELOPMENT]`: Process for developing categories
- `[THEORETICAL_INTEGRATION]`: Integration with theory
- `[RELATIONSHIP_IDENTIFICATION]`: Identification of relationships
- `[CORE_CATEGORY_SELECTION]`: Selection of core category
- `[RELIABILITY_APPROACH]`: Approach to inter-coder reliability
- `[RELIABILITY_THRESHOLD]`: Threshold for acceptable reliability
- `[DISAGREEMENT_RESOLUTION]`: Process for resolving disagreements
- `[RELIABILITY_REPORTING]`: Reporting of reliability measures

### Theme Development
- `[THEME_DEFINITION_CRITERIA]`: Criteria for defining themes
- `[THEME_PREVALENCE]`: Consideration of theme prevalence
- `[THEME_COHERENCE]`: Internal coherence of themes
- `[THEME_DISTINCTIVENESS]`: Distinctiveness between themes
- `[THEME_REVIEW_PROCESS]`: Process for reviewing themes
- `[THEME_VALIDATION]`: Validation of themes
- `[THEME_NAMING]`: Naming convention for themes
- `[THEME_HIERARCHY]`: Hierarchical organization of themes

### Trustworthiness
- `[PROLONGED_ENGAGEMENT]`: Duration of engagement with data
- `[TRIANGULATION]`: Types of triangulation employed
- `[MEMBER_CHECKING]`: Member checking procedures
- `[PEER_DEBRIEFING]`: Peer debriefing processes
- `[THICK_DESCRIPTION]`: Provision of thick description
- `[PURPOSIVE_SAMPLING]`: Use of purposive sampling
- `[CONTEXTUAL_INFORMATION]`: Contextual information provided
- `[AUDIT_TRAIL]`: Maintenance of audit trail
- `[METHODOLOGICAL_CONSISTENCY]`: Consistency in methodology
- `[EXTERNAL_AUDITING]`: External auditing procedures
- `[REFLEXIVITY]`: Reflexivity practices
- `[BIAS_ACKNOWLEDGMENT]`: Acknowledgment of bias
- `[DATA_GROUNDING]`: Grounding of conclusions in data

### Mixed Methods Integration
- `[CONVERGENT/SEQUENTIAL_EXPLANATORY/SEQUENTIAL_EXPLORATORY/EMBEDDED]`: Mixed methods design type
- `[INTEGRATION_TIMING]`: Timing of integration
- `[INTEGRATION_EMPHASIS]`: Emphasis given to each method
- `[INTEGRATION_PROCEDURES]`: Specific integration procedures
- `[QUANTIFICATION_METHOD]`: Method for quantifying qualitative data
- `[QUANTIFICATION_PURPOSE]`: Purpose of quantification
- `[QUANTIFICATION_VALIDATION]`: Validation of quantification
- `[QUALIFICATION_APPROACH]`: Approach to qualifying quantitative data
- `[QUALIFICATION_PURPOSE]`: Purpose of qualification
- `[QUALIFICATION_CRITERIA]`: Criteria for qualification
- `[CONVERGENCE_CRITERIA]`: Criteria for assessing convergence
- `[CONVERGENCE_ANALYSIS]`: Analysis of convergence
- `[CONVERGENCE_INTERPRETATION]`: Interpretation of convergence
- `[DIVERGENCE_IDENTIFICATION]`: Identification of divergence
- `[DIVERGENCE_EXPLANATION]`: Explanation of divergence
- `[DIVERGENCE_RESOLUTION]`: Resolution of divergence
- `[JOINT_DISPLAY_TYPE]`: Type of joint display
- `[JOINT_DISPLAY_CONTENT]`: Content of joint display
- `[JOINT_DISPLAY_PURPOSE]`: Purpose of joint display
- `[META_INFERENCE_DEVELOPMENT]`: Development of meta-inferences
- `[META_INFERENCE_VALIDATION]`: Validation of meta-inferences
- `[META_INFERENCE_IMPLICATIONS]`: Implications of meta-inferences

### Advanced Techniques
- `[SUPERVISED_METHOD_1]`: First supervised learning method
- `[SUPERVISED_PURPOSE_1]`: Purpose of first supervised method
- `[SUPERVISED_VALIDATION_1]`: Validation of first supervised method
- `[UNSUPERVISED_METHOD_1]`: First unsupervised learning method
- `[UNSUPERVISED_PURPOSE_1]`: Purpose of first unsupervised method
- `[UNSUPERVISED_EVALUATION_1]`: Evaluation of first unsupervised method
- `[GROWTH_MODEL_TYPE]`: Type of growth curve model
- `[GROWTH_PARAMETERS]`: Parameters in growth model
- `[GROWTH_PREDICTORS]`: Predictors in growth model
- `[SURVIVAL_METHOD]`: Survival analysis method
- `[SURVIVAL_ASSUMPTIONS]`: Assumptions in survival analysis
- `[SURVIVAL_INTERPRETATION]`: Interpretation of survival results
- `[SEM_MODEL_TYPE]`: Type of structural equation model
- `[SEM_ESTIMATION]`: Estimation method for SEM
- `[SEM_FIT_INDICES]`: Fit indices for SEM
- `[MULTILEVEL_STRUCTURE]`: Structure of multilevel model
- `[MULTILEVEL_EFFECTS]`: Effects in multilevel model
- `[MULTILEVEL_ASSUMPTIONS]`: Assumptions in multilevel model

### Reporting Framework
- `[DESCRIPTIVE_REPORTING]`: Format for reporting descriptives
- `[MISSING_DATA_REPORTING]`: Reporting of missing data
- `[SAMPLE_CHARACTERISTICS]`: Reporting of sample characteristics
- `[TEST_STATISTIC_REPORTING]`: Format for test statistics
- `[EFFECT_SIZE_REPORTING]`: Format for effect sizes
- `[ASSUMPTION_REPORTING]`: Reporting of assumption testing
- `[MODEL_FIT_REPORTING]`: Reporting of model fit
- `[PARAMETER_REPORTING]`: Reporting of model parameters
- `[MODEL_COMPARISON]`: Comparison of models
- `[THEME_ORGANIZATION]`: Organization of themes
- `[QUOTE_SELECTION]`: Selection of quotes
- `[PARTICIPANT_ATTRIBUTION]`: Attribution of quotes to participants
- `[ANALYSIS_TRANSPARENCY]`: Transparency in analysis reporting
- `[REFLEXIVITY_REPORTING]`: Reporting of reflexivity
- `[QUALITY_EVIDENCE]`: Evidence of analysis quality

### Interpretation Guidelines
- `[STATISTICAL_VS_PRACTICAL]`: Statistical vs practical significance
- `[CONFIDENCE_INTERVAL_USE]`: Use of confidence intervals
- `[P_VALUE_INTERPRETATION]`: Interpretation of p-values
- `[MEANING_MAKING]`: Process of meaning-making
- `[CONTEXT_CONSIDERATION]`: Consideration of context
- `[PARTICIPANT_VOICE]`: Representation of participant voice
- `[INTEGRATION_REPORTING]`: Reporting of mixed methods integration
- `[CONVERGENCE_DIVERGENCE]`: Discussion of convergence and divergence
- `[META_INFERENCE_PRESENTATION]`: Presentation of meta-inferences

### Quality Control
- `[CODE_REVIEW_PROCESS]`: Process for reviewing code
- `[CODE_DOCUMENTATION]`: Documentation standards for code
- `[CODE_TESTING]`: Testing of analysis code
- `[INDEPENDENT_ANALYSIS]`: Independent analysis procedures
- `[RESULT_COMPARISON]`: Comparison of results
- `[SENSITIVITY_TESTING]`: Sensitivity testing procedures
- `[ANALYSIS_DOCUMENTATION]`: Documentation of analysis
- `[DATA_AVAILABILITY]`: Availability of data
- `[CODE_SHARING]`: Sharing of analysis code
- `[ERROR_CHECKING_PROCEDURES]`: Procedures for error checking
- `[OUTLIER_INVESTIGATION]`: Investigation of outliers
- `[LOGIC_VALIDATION]`: Validation of logical consistency

### Timeline and Milestones
- `[PREP_TIMELINE]`: Timeline for data preparation
- `[PREP_MILESTONE_1]`: First preparation milestone
- `[PREP_MILESTONE_2]`: Second preparation milestone
- `[PREP_DELIVERABLE]`: Deliverable from preparation phase
- `[PRIMARY_TIMELINE]`: Timeline for primary analysis
- `[PRIMARY_MILESTONE_1]`: First primary analysis milestone
- `[PRIMARY_MILESTONE_2]`: Second primary analysis milestone
- `[PRIMARY_DELIVERABLE]`: Deliverable from primary analysis
- `[SECONDARY_TIMELINE]`: Timeline for secondary analysis
- `[SECONDARY_MILESTONE_1]`: First secondary analysis milestone
- `[SECONDARY_MILESTONE_2]`: Second secondary analysis milestone
- `[SECONDARY_DELIVERABLE]`: Deliverable from secondary analysis
- `[INTEGRATION_TIMELINE]`: Timeline for integration phase
- `[INTEGRATION_MILESTONE_1]`: First integration milestone
- `[INTEGRATION_MILESTONE_2]`: Second integration milestone
- `[INTEGRATION_DELIVERABLE]`: Deliverable from integration phase

## Usage Example
Use for research proposals, data analysis plans, statistical analysis protocols, methodology sections, or analytical training and education.

## Customization Tips
- Adapt to specific statistical software capabilities
- Include discipline-specific analytical approaches
- Add regulatory or compliance requirements
- Consider cultural and contextual factors in interpretation
- Include reproducibility and open science practices
- Add data visualization and presentation guidelines
- Consider ethical implications of analytical choices
- Include guidance for negative or null results