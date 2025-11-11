---
title: Data Quality & Validation Template
category: data-analytics/Analytics Engineering
tags: [automation, data-analytics, design, machine-learning, management, security, strategy, template]
use_cases:
  - Creating design comprehensive data quality validation frameworks including data profiling methodologies, validation rule engines, data cleansing processes, quality monitoring systems, and automated data quality management for enterprise data platforms.

  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---

# Data Quality & Validation Template

## Purpose
Design comprehensive data quality validation frameworks including data profiling methodologies, validation rule engines, data cleansing processes, quality monitoring systems, and automated data quality management for enterprise data platforms.

## Quick Start

### For Data Engineers
Implement data quality checks in 3 steps:

1. **Profile Your Data**
   - Run comprehensive profiling: Analyze completeness, validity, uniqueness, consistency across datasets
   - Use `DataProfiler` class (lines 78-337) to generate column-level statistics and quality metrics
   - Identify data quality issues: Missing values, duplicates, format inconsistencies, outliers
   - Example: `profiling_scope='FULL'` for complete analysis or `'STANDARD'` for faster results

2. **Define Validation Rules**
   - **Schema Validation**: Required columns, data types, nullability constraints
   - **Business Rules**: Value ranges, format patterns, referential integrity, statistical thresholds
   - **Custom Rules**: Domain-specific validation logic using validation engine (lines 342-634)
   - Set thresholds: `COMPLETENESS_THRESHOLD: "95%"`, `VALIDITY_THRESHOLD: "98%"`

3. **Automate Quality Monitoring**
   - Set up continuous monitoring with `DataQualityMonitor` (lines 1114-1320)
   - Configure alerts for quality threshold breaches (completeness <95%, accuracy <98%)
   - Implement automated remediation: ML-based imputation, duplicate removal, outlier handling
   - Create quality dashboards with dimension breakdowns and trend analysis

**Key Template Sections**: Profiling framework (69-337), Validation engine (339-748), Cleansing (750-1108), Monitoring (1111-1532)

## Template

```
You are a data quality engineering expert specializing in [DATA_QUALITY_METHODOLOGY]. Design a comprehensive data quality validation and management framework for [ORGANIZATION_NAME] to ensure [QUALITY_OBJECTIVES] using [VALIDATION_APPROACH] and [QUALITY_TOOLS].

DATA QUALITY FRAMEWORK OVERVIEW:
Project Context:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Data domain: [DATA_DOMAIN]
- Quality objectives: [QUALITY_OBJECTIVES]
- Compliance requirements: [COMPLIANCE_REQUIREMENTS]
- Data volume: [DATA_VOLUME_SCALE]
- Quality SLA targets: [QUALITY_SLA_TARGETS]
- Business impact: [QUALITY_BUSINESS_IMPACT]
- Stakeholder requirements: [STAKEHOLDER_QUALITY_REQUIREMENTS]

### Quality Strategy
- Validation methodology: [DATA_QUALITY_METHODOLOGY]
- Validation approach: [VALIDATION_APPROACH] (Preventive/Detective/Corrective/Comprehensive)
- Quality dimensions: [QUALITY_DIMENSIONS] (Accuracy/Completeness/Consistency/Timeliness/Validity/Uniqueness)
- Quality tools: [QUALITY_TOOLS]
- Monitoring strategy: [QUALITY_MONITORING_STRATEGY]
- Remediation approach: [QUALITY_REMEDIATION_APPROACH]
- Governance model: [QUALITY_GOVERNANCE_MODEL]
- Automation level: [QUALITY_AUTOMATION_LEVEL]

### Technical Architecture
- Data platforms: [DATA_PLATFORMS]
- Quality tools: [QUALITY_VALIDATION_TOOLS]
- Processing framework: [DATA_PROCESSING_FRAMEWORK]
- Monitoring platform: [QUALITY_MONITORING_PLATFORM]
- Alerting system: [QUALITY_ALERTING_SYSTEM]
- Metadata repository: [METADATA_REPOSITORY]
- Lineage tracking: [LINEAGE_TRACKING_SYSTEM]
- Dashboard platform: [QUALITY_DASHBOARD_PLATFORM]

### Quality Requirements
- Accuracy threshold: [ACCURACY_THRESHOLD_PERCENTAGE]
- Completeness threshold: [COMPLETENESS_THRESHOLD_PERCENTAGE]
- Consistency threshold: [CONSISTENCY_THRESHOLD_PERCENTAGE]
- Timeliness threshold: [TIMELINESS_THRESHOLD_HOURS]
- Uniqueness threshold: [UNIQUENESS_THRESHOLD_PERCENTAGE]
- Validity threshold: [VALIDITY_THRESHOLD_PERCENTAGE]
- Overall quality score target: [OVERALL_QUALITY_TARGET]
- Critical data elements: [CRITICAL_DATA_ELEMENTS]

### DATA PROFILING FRAMEWORK
### Comprehensive Data Discovery
```python
# Advanced data profiling framework
import [DATA_PROCESSING_LIBRARY] as [PROCESSING_ALIAS]
import [QUALITY_LIBRARY] as [QUALITY_ALIAS]
from [STATISTICAL_LIBRARY] import [STATISTICAL_FUNCTIONS]
from [VISUALIZATION_LIBRARY] import [PLOTTING_FUNCTIONS]

class DataProfiler:
    def __init__(self, config: dict):
        self.config = config
        self.profiling_engine = [QUALITY_ALIAS].ProfilingEngine([PROFILING_CONFIG])
        self.statistical_analyzer = [STATISTICAL_ANALYZER]([STATS_CONFIG])
        self.pattern_analyzer = [PATTERN_ANALYZER]([PATTERN_CONFIG])

    def comprehensive_profile_analysis(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        table_name: str,
        profiling_scope: str = 'FULL'
    ) -> dict:
        """
        Perform comprehensive data profiling analysis

### Args
            dataset: Dataset to profile
            table_name: Name of the table/dataset
            profiling_scope: Scope of profiling (BASIC/STANDARD/FULL/DEEP)

### Returns
            Complete profiling results dictionary
        """

        profiling_results = {
            'table_metadata': self.analyze_table_metadata(dataset, table_name),
            'column_profiles': self.analyze_column_profiles(dataset, profiling_scope),
            'data_patterns': self.analyze_data_patterns(dataset),
            'statistical_summary': self.generate_statistical_summary(dataset),
            'quality_assessment': self.assess_data_quality(dataset),
            'relationship_analysis': self.analyze_relationships(dataset),
            'anomaly_detection': self.detect_anomalies(dataset),
            'business_rules_validation': self.validate_business_rules(dataset)
        }

        return profiling_results

    def analyze_table_metadata(self, dataset: [PROCESSING_ALIAS].DataFrame, table_name: str) -> dict:
        """
        Analyze table-level metadata and characteristics
        """
        return {
            'table_name': table_name,
            'record_count': len(dataset),
            'column_count': len(dataset.columns),
            'data_types': dict(dataset.dtypes),
            'memory_usage_mb': dataset.memory_usage(deep=True).sum() / (1024 * 1024),
            'table_size_estimate': [TABLE_SIZE_CALCULATION],
            'creation_timestamp': [CURRENT_TIMESTAMP],
            'profiling_scope': [PROFILING_SCOPE_LEVEL],
            'sample_records': dataset.head([SAMPLE_SIZE]).to_dict('records'),
            'schema_hash': [SCHEMA_HASH_CALCULATION]
        }

    def analyze_column_profiles(self, dataset: [PROCESSING_ALIAS].DataFrame, scope: str) -> dict:
        """
        Analyze individual column profiles and characteristics
        """
        column_profiles = {}

        for column in dataset.columns:
            column_data = dataset[column]

            # Basic statistics
            basic_stats = {
                'column_name': column,
                'data_type': str(column_data.dtype),
                'non_null_count': column_data.count(),
                'null_count': column_data.isnull().sum(),
                'null_percentage': (column_data.isnull().sum() / len(dataset)) * 100,
                'unique_count': column_data.nunique(),
                'unique_percentage': (column_data.nunique() / len(dataset)) * 100,
                'memory_usage': column_data.memory_usage(deep=True)
            }

            # Data type specific analysis
            if [PROCESSING_ALIAS].api.types.is_numeric_dtype(column_data):
                numeric_stats = self.analyze_numeric_column(column_data)
                basic_stats.update(numeric_stats)

            elif [PROCESSING_ALIAS].api.types.is_string_dtype(column_data):
                string_stats = self.analyze_string_column(column_data)
                basic_stats.update(string_stats)

            elif [PROCESSING_ALIAS].api.types.is_datetime64_any_dtype(column_data):
                datetime_stats = self.analyze_datetime_column(column_data)
                basic_stats.update(datetime_stats)

            # Advanced profiling based on scope
            if scope in ['FULL', 'DEEP']:
                advanced_stats = self.advanced_column_analysis(column_data, scope)
                basic_stats.update(advanced_stats)

            column_profiles[column] = basic_stats

        return column_profiles

    def analyze_numeric_column(self, column_data: [PROCESSING_ALIAS].Series) -> dict:
        """
        Analyze numeric column characteristics
        """
        numeric_data = column_data.dropna()

        if len(numeric_data) == 0:
            return {'analysis_type': 'numeric', 'data_available': False}

        return {
            'analysis_type': 'numeric',
            'data_available': True,
            'min_value': float(numeric_data.min()),
            'max_value': float(numeric_data.max()),
            'mean_value': float(numeric_data.mean()),
            'median_value': float(numeric_data.median()),
            'mode_value': float(numeric_data.mode().iloc[0]) if not numeric_data.mode().empty else None,
            'standard_deviation': float(numeric_data.std()),
            'variance': float(numeric_data.var()),
            'skewness': float(numeric_data.skew()),
            'kurtosis': float(numeric_data.kurtosis()),
            'quartile_25': float(numeric_data.quantile(0.25)),
            'quartile_75': float(numeric_data.quantile(0.75)),
            'percentile_95': float(numeric_data.quantile(0.95)),
            'percentile_99': float(numeric_data.quantile(0.99)),
            'zero_count': (numeric_data == 0).sum(),
            'negative_count': (numeric_data < 0).sum(),
            'positive_count': (numeric_data > 0).sum(),
            'outlier_count_iqr': self.detect_outliers_iqr(numeric_data),
            'outlier_count_zscore': self.detect_outliers_zscore(numeric_data),
            'distribution_type': self.identify_distribution_type(numeric_data),
            'normality_test_pvalue': self.test_normality(numeric_data)
        }

    def analyze_string_column(self, column_data: [PROCESSING_ALIAS].Series) -> dict:
        """
        Analyze string column characteristics
        """
        string_data = column_data.dropna().astype(str)

        if len(string_data) == 0:
            return {'analysis_type': 'string', 'data_available': False}

        # Length statistics
        lengths = string_data.str.len()

        # Pattern analysis
        pattern_stats = self.analyze_string_patterns(string_data)

        return {
            'analysis_type': 'string',
            'data_available': True,
            'min_length': int(lengths.min()),
            'max_length': int(lengths.max()),
            'avg_length': float(lengths.mean()),
            'median_length': float(lengths.median()),
            'std_length': float(lengths.std()),
            'empty_string_count': (string_data == '').sum(),
            'whitespace_only_count': string_data.str.strip().eq('').sum(),
            'leading_whitespace_count': (string_data != string_data.str.lstrip()).sum(),
            'trailing_whitespace_count': (string_data != string_data.str.rstrip()).sum(),
            'numeric_string_count': string_data.str.isnumeric().sum(),
            'alpha_string_count': string_data.str.isalpha().sum(),
            'alphanumeric_string_count': string_data.str.isalnum().sum(),
            'contains_special_chars_count': string_data.str.contains(r'[^a-zA-Z0-9\s]', na=False).sum(),
            'common_patterns': pattern_stats['common_patterns'],
            'format_consistency': pattern_stats['format_consistency'],
            'encoding_issues': self.detect_encoding_issues(string_data),
            'most_common_values': string_data.value_counts().head([TOP_VALUES_COUNT]).to_dict(),
            'least_common_values': string_data.value_counts().tail([BOTTOM_VALUES_COUNT]).to_dict()
        }

    def analyze_datetime_column(self, column_data: [PROCESSING_ALIAS].Series) -> dict:
        """
        Analyze datetime column characteristics
        """
        datetime_data = [PROCESSING_ALIAS].to_datetime(column_data, errors='coerce').dropna()

        if len(datetime_data) == 0:
            return {'analysis_type': 'datetime', 'data_available': False}

        # Time range analysis
        time_range = datetime_data.max() - datetime_data.min()

        # Temporal patterns
        temporal_patterns = self.analyze_temporal_patterns(datetime_data)

        return {
            'analysis_type': 'datetime',
            'data_available': True,
            'min_datetime': datetime_data.min().isoformat(),
            'max_datetime': datetime_data.max().isoformat(),
            'date_range_days': time_range.days,
            'date_range_hours': time_range.total_seconds() / 3600,
            'most_common_year': datetime_data.dt.year.value_counts().index[0],
            'most_common_month': datetime_data.dt.month.value_counts().index[0],
            'most_common_day': datetime_data.dt.day.value_counts().index[0],
            'most_common_weekday': datetime_data.dt.dayofweek.value_counts().index[0],
            'most_common_hour': datetime_data.dt.hour.value_counts().index[0],
            'weekend_count': datetime_data.dt.dayofweek.isin([5, 6]).sum(),
            'weekday_count': (~datetime_data.dt.dayofweek.isin([5, 6])).sum(),
            'business_hours_count': datetime_data.dt.hour.between([BUSINESS_START_HOUR], [BUSINESS_END_HOUR]).sum(),
            'timezone_info': str(datetime_data.dt.tz) if datetime_data.dt.tz is not None else 'No timezone',
            'temporal_gaps': self.detect_temporal_gaps(datetime_data),
            'seasonal_patterns': temporal_patterns['seasonal_patterns'],
            'trend_analysis': temporal_patterns['trend_analysis']
        }

    def analyze_data_patterns(self, dataset: [PROCESSING_ALIAS].DataFrame) -> dict:
        """
        Analyze cross-column data patterns and relationships
        """
        pattern_analysis = {
            'correlation_matrix': self.calculate_correlation_matrix(dataset),
            'dependency_patterns': self.identify_functional_dependencies(dataset),
            'cardinality_patterns': self.analyze_cardinality_patterns(dataset),
            'co_occurrence_patterns': self.analyze_co_occurrence_patterns(dataset),
            'sequence_patterns': self.analyze_sequence_patterns(dataset),
            'hierarchical_patterns': self.identify_hierarchical_patterns(dataset),
            'referential_integrity': self.validate_referential_integrity(dataset)
        }

        return pattern_analysis

    def assess_data_quality(self, dataset: [PROCESSING_ALIAS].DataFrame) -> dict:
        """
        Assess overall data quality across multiple dimensions
        """
        quality_dimensions = {
            'completeness': self.assess_completeness(dataset),
            'accuracy': self.assess_accuracy(dataset),
            'consistency': self.assess_consistency(dataset),
            'validity': self.assess_validity(dataset),
            'uniqueness': self.assess_uniqueness(dataset),
            'timeliness': self.assess_timeliness(dataset),
            'integrity': self.assess_integrity(dataset)
        }

        # Calculate overall quality score
        dimension_weights = {
            'completeness': [COMPLETENESS_WEIGHT],
            'accuracy': [ACCURACY_WEIGHT],
            'consistency': [CONSISTENCY_WEIGHT],
            'validity': [VALIDITY_WEIGHT],
            'uniqueness': [UNIQUENESS_WEIGHT],
            'timeliness': [TIMELINESS_WEIGHT],
            'integrity': [INTEGRITY_WEIGHT]
        }

        weighted_score = sum(
            quality_dimensions[dim]['score'] * dimension_weights[dim]
            for dim in quality_dimensions.keys()
        ) / sum(dimension_weights.values())

        return {
            'dimension_scores': quality_dimensions,
            'overall_quality_score': weighted_score,
            'quality_grade': self.calculate_quality_grade(weighted_score),
            'critical_issues': self.identify_critical_quality_issues(quality_dimensions),
            'improvement_recommendations': self.generate_quality_recommendations(quality_dimensions)
        }
```

Data Quality Validation Rules Engine:
```python
# Comprehensive validation rules framework
class DataValidationEngine:
    def __init__(self, config: dict):
        self.config = config
        self.rule_engine = [RULES_ENGINE]([RULES_CONFIG])
        self.validation_results = []

    def create_validation_suite(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        validation_config: dict
    ) -> dict:
        """
        Create comprehensive data validation suite

### Args
            dataset: Dataset to validate
            validation_config: Validation configuration

### Returns
            Validation suite results
        """

        validation_suite = {
            'schema_validation': self.validate_schema(dataset, validation_config.get('schema_rules', {})),
            'business_rules_validation': self.validate_business_rules(dataset, validation_config.get('business_rules', [])),
            'referential_integrity_validation': self.validate_referential_integrity(dataset, validation_config.get('referential_rules', [])),
            'data_range_validation': self.validate_data_ranges(dataset, validation_config.get('range_rules', [])),
            'format_validation': self.validate_formats(dataset, validation_config.get('format_rules', [])),
            'custom_validation': self.validate_custom_rules(dataset, validation_config.get('custom_rules', [])),
            'cross_field_validation': self.validate_cross_field_rules(dataset, validation_config.get('cross_field_rules', [])),
            'temporal_validation': self.validate_temporal_rules(dataset, validation_config.get('temporal_rules', []))
        }

        return validation_suite

    def validate_schema(self, dataset: [PROCESSING_ALIAS].DataFrame, schema_rules: dict) -> dict:
        """
        Validate dataset schema against defined rules
        """
        schema_results = {
            'validation_type': 'schema',
            'tests_passed': 0,
            'tests_failed': 0,
            'validation_details': [],
            'critical_failures': []
        }

        # Column existence validation
        expected_columns = schema_rules.get('required_columns', [])
        actual_columns = set(dataset.columns)

        for column in expected_columns:
            if column['name'] in actual_columns:
                # Validate data type
                expected_type = column.get('data_type')
                actual_type = str(dataset[column['name']].dtype)

                if self.is_compatible_data_type(actual_type, expected_type):
                    schema_results['tests_passed'] += 1
                    schema_results['validation_details'].append({
                        'rule_type': 'COLUMN_DATA_TYPE',
                        'column': column['name'],
                        'expected': expected_type,
                        'actual': actual_type,
                        'status': 'PASS'
                    })
                else:
                    schema_results['tests_failed'] += 1
                    failure_detail = {
                        'rule_type': 'COLUMN_DATA_TYPE',
                        'column': column['name'],
                        'expected': expected_type,
                        'actual': actual_type,
                        'status': 'FAIL',
                        'severity': column.get('criticality', 'MEDIUM')
                    }
                    schema_results['validation_details'].append(failure_detail)

                    if column.get('criticality') == 'CRITICAL':
                        schema_results['critical_failures'].append(failure_detail)

                # Validate nullability
                if not column.get('nullable', True):
                    null_count = dataset[column['name']].isnull().sum()
                    if null_count == 0:
                        schema_results['tests_passed'] += 1
                        schema_results['validation_details'].append({
                            'rule_type': 'COLUMN_NULLABILITY',
                            'column': column['name'],
                            'null_count': null_count,
                            'status': 'PASS'
                        })
                    else:
                        schema_results['tests_failed'] += 1
                        schema_results['validation_details'].append({
                            'rule_type': 'COLUMN_NULLABILITY',
                            'column': column['name'],
                            'null_count': null_count,
                            'status': 'FAIL',
                            'severity': 'HIGH'
                        })
            else:
                schema_results['tests_failed'] += 1
                missing_column_detail = {
                    'rule_type': 'COLUMN_EXISTENCE',
                    'column': column['name'],
                    'status': 'FAIL',
                    'message': f"Required column '{column['name']}' not found",
                    'severity': column.get('criticality', 'HIGH')
                }
                schema_results['validation_details'].append(missing_column_detail)

                if column.get('criticality') == 'CRITICAL':
                    schema_results['critical_failures'].append(missing_column_detail)

        return schema_results

    def validate_business_rules(self, dataset: [PROCESSING_ALIAS].DataFrame, business_rules: list) -> dict:
        """
        Validate business-specific rules and constraints
        """
        business_results = {
            'validation_type': 'business_rules',
            'tests_passed': 0,
            'tests_failed': 0,
            'validation_details': [],
            'rule_violations': []
        }

        for rule in business_rules:
            try:
                rule_type = rule['type']
                rule_name = rule['name']
                rule_condition = rule['condition']

                # Evaluate rule condition
                if rule_type == 'CONSTRAINT':
                    violations = dataset.query(f"not ([RULE_CONDITION])")
                    violation_count = len(violations)

                    if violation_count == 0:
                        business_results['tests_passed'] += 1
                        business_results['validation_details'].append({
                            'rule_name': rule_name,
                            'rule_type': rule_type,
                            'condition': rule_condition,
                            'violation_count': violation_count,
                            'status': 'PASS'
                        })
                    else:
                        business_results['tests_failed'] += 1
                        violation_detail = {
                            'rule_name': rule_name,
                            'rule_type': rule_type,
                            'condition': rule_condition,
                            'violation_count': violation_count,
                            'violation_percentage': (violation_count / len(dataset)) * 100,
                            'status': 'FAIL',
                            'severity': rule.get('severity', 'MEDIUM'),
                            'sample_violations': violations.head([SAMPLE_VIOLATION_COUNT]).to_dict('records')
                        }
                        business_results['validation_details'].append(violation_detail)
                        business_results['rule_violations'].append(violation_detail)

                elif rule_type == 'AGGREGATION':
                    # Validate aggregation-based rules
                    aggregate_condition = rule['aggregate_condition']
                    agg_result = eval(f"dataset.[AGGREGATE_CONDITION]")

                    if agg_result:
                        business_results['tests_passed'] += 1
                    else:
                        business_results['tests_failed'] += 1
                        business_results['validation_details'].append({
                            'rule_name': rule_name,
                            'rule_type': rule_type,
                            'aggregate_condition': aggregate_condition,
                            'status': 'FAIL',
                            'severity': rule.get('severity', 'MEDIUM')
                        })

                elif rule_type == 'STATISTICAL':
                    # Validate statistical constraints
                    statistical_result = self.validate_statistical_rule(dataset, rule)
                    business_results['validation_details'].append(statistical_result)

                    if statistical_result['status'] == 'PASS':
                        business_results['tests_passed'] += 1
                    else:
                        business_results['tests_failed'] += 1

            except Exception as e:
                business_results['tests_failed'] += 1
                business_results['validation_details'].append({
                    'rule_name': rule_name,
                    'rule_type': rule_type,
                    'status': 'ERROR',
                    'error_message': str(e),
                    'severity': 'HIGH'
                })

        return business_results

    def validate_referential_integrity(self, dataset: [PROCESSING_ALIAS].DataFrame, referential_rules: list) -> dict:
        """
        Validate referential integrity constraints
        """
        referential_results = {
            'validation_type': 'referential_integrity',
            'tests_passed': 0,
            'tests_failed': 0,
            'validation_details': [],
            'orphan_records': []
        }

        for rule in referential_rules:
            parent_dataset = self.load_reference_dataset(rule['parent_table'])
            child_column = rule['child_column']
            parent_column = rule['parent_column']

            # Find orphan records
            child_values = dataset[child_column].dropna().unique()
            parent_values = parent_dataset[parent_column].unique()
            orphan_values = set(child_values) - set(parent_values)

            if len(orphan_values) == 0:
                referential_results['tests_passed'] += 1
                referential_results['validation_details'].append({
                    'rule_type': 'FOREIGN_KEY',
                    'child_column': child_column,
                    'parent_table': rule['parent_table'],
                    'parent_column': parent_column,
                    'orphan_count': 0,
                    'status': 'PASS'
                })
            else:
                referential_results['tests_failed'] += 1
                orphan_records = dataset[dataset[child_column].isin(orphan_values)]

                orphan_detail = {
                    'rule_type': 'FOREIGN_KEY',
                    'child_column': child_column,
                    'parent_table': rule['parent_table'],
                    'parent_column': parent_column,
                    'orphan_count': len(orphan_records),
                    'orphan_percentage': (len(orphan_records) / len(dataset)) * 100,
                    'status': 'FAIL',
                    'severity': rule.get('severity', 'HIGH'),
                    'sample_orphans': orphan_records.head([SAMPLE_ORPHAN_COUNT]).to_dict('records')
                }
                referential_results['validation_details'].append(orphan_detail)
                referential_results['orphan_records'].append(orphan_detail)

        return referential_results

    def validate_custom_rules(self, dataset: [PROCESSING_ALIAS].DataFrame, custom_rules: list) -> dict:
        """
        Execute custom validation rules with flexible logic
        """
        custom_results = {
            'validation_type': 'custom_rules',
            'tests_passed': 0,
            'tests_failed': 0,
            'validation_details': []
        }

        for rule in custom_rules:
            try:
                rule_name = rule['name']
                rule_function = rule['function']
                rule_parameters = rule.get('parameters', {})

                # Execute custom validation function
                validation_result = eval(f"[RULE_FUNCTION](dataset, **[RULE_PARAMETERS])")

                if validation_result['status'] == 'PASS':
                    custom_results['tests_passed'] += 1
                else:
                    custom_results['tests_failed'] += 1

                validation_result['rule_name'] = rule_name
                custom_results['validation_details'].append(validation_result)

            except Exception as e:
                custom_results['tests_failed'] += 1
                custom_results['validation_details'].append({
                    'rule_name': rule_name,
                    'status': 'ERROR',
                    'error_message': str(e),
                    'severity': 'HIGH'
                })

        return custom_results

# Quality assessment functions
def assess_completeness(dataset: [PROCESSING_ALIAS].DataFrame) -> dict:
    """
    Assess data completeness across all columns
    """
    total_cells = dataset.shape[0] * dataset.shape[1]
    missing_cells = dataset.isnull().sum().sum()
    completeness_percentage = ((total_cells - missing_cells) / total_cells) * 100

    column_completeness = {}
    for column in dataset.columns:
        non_null_count = dataset[column].count()
        total_count = len(dataset)
        column_completeness[column] = {
            'completeness_percentage': (non_null_count / total_count) * 100,
            'missing_count': total_count - non_null_count,
            'non_null_count': non_null_count
        }

    return {
        'score': completeness_percentage,
        'overall_completeness': completeness_percentage,
        'total_cells': total_cells,
        'missing_cells': missing_cells,
        'column_completeness': column_completeness,
        'columns_below_threshold': [
            col for col, stats in column_completeness.items()
            if stats['completeness_percentage'] < [COMPLETENESS_THRESHOLD]
        ]
    }

def assess_validity(dataset: [PROCESSING_ALIAS].DataFrame) -> dict:
    """
    Assess data validity based on format and constraint rules
    """
    validity_results = {
        'score': 0,
        'column_validity': {},
        'format_violations': [],
        'constraint_violations': []
    }

    # Define validity rules per column type
    validity_rules = [VALIDITY_RULES_CONFIG]

    total_valid_values = 0
    total_values = 0

    for column in dataset.columns:
        column_data = dataset[column].dropna()
        if len(column_data) == 0:
            continue

        column_validity = {
            'total_values': len(column_data),
            'valid_values': 0,
            'invalid_values': 0,
            'validity_percentage': 0,
            'validation_errors': []
        }

        # Apply format validation based on column type
        if column in validity_rules:
            rules = validity_rules[column]

            for rule in rules:
                if rule['type'] == 'REGEX':
                    valid_mask = column_data.astype(str).str.match(rule['pattern'])
                    valid_count = valid_mask.sum()
                    invalid_count = len(column_data) - valid_count

                    if invalid_count > 0:
                        column_validity['validation_errors'].append({
                            'rule_type': 'REGEX',
                            'pattern': rule['pattern'],
                            'invalid_count': invalid_count,
                            'invalid_percentage': (invalid_count / len(column_data)) * 100
                        })

                elif rule['type'] == 'RANGE':
                    if [PROCESSING_ALIAS].api.types.is_numeric_dtype(column_data):
                        valid_mask = column_data.between(rule['min_value'], rule['max_value'])
                        valid_count = valid_mask.sum()
                        invalid_count = len(column_data) - valid_count

                        if invalid_count > 0:
                            column_validity['validation_errors'].append({
                                'rule_type': 'RANGE',
                                'min_value': rule['min_value'],
                                'max_value': rule['max_value'],
                                'invalid_count': invalid_count,
                                'out_of_range_values': column_data[~valid_mask].tolist()[:10]
                            })

        # Calculate column validity percentage
        if column_validity['validation_errors']:
            total_invalid = sum(error['invalid_count'] for error in column_validity['validation_errors'])
            column_validity['invalid_values'] = total_invalid
            column_validity['valid_values'] = len(column_data) - total_invalid
        else:
            column_validity['valid_values'] = len(column_data)

        column_validity['validity_percentage'] = (column_validity['valid_values'] / len(column_data)) * 100

        validity_results['column_validity'][column] = column_validity
        total_valid_values += column_validity['valid_values']
        total_values += len(column_data)

    # Calculate overall validity score
    validity_results['score'] = (total_valid_values / total_values * 100) if total_values > 0 else 0

    return validity_results
```

DATA CLEANSING AND STANDARDIZATION:
Automated Data Cleansing Framework:
```python
# Comprehensive data cleansing framework
class DataCleansingEngine:
    def __init__(self, config: dict):
        self.config = config
        self.cleansing_rules = [CLEANSING_RULES_CONFIG]
        self.standardization_rules = [STANDARDIZATION_RULES_CONFIG]
        self.transformation_log = []

    def comprehensive_data_cleansing(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        cleansing_profile: str = 'STANDARD'
    ) -> dict:
        """
        Perform comprehensive data cleansing

### Args
            dataset: Dataset to cleanse
            cleansing_profile: Cleansing intensity (BASIC/STANDARD/AGGRESSIVE)

### Returns
            Cleansing results and transformed dataset
        """

        original_dataset = dataset.copy()
        cleansed_dataset = dataset.copy()

        cleansing_results = {
            'original_record_count': len(dataset),
            'original_column_count': len(dataset.columns),
            'cleansing_operations': [],
            'data_transformations': [],
            'quality_improvements': {},
            'cleansing_summary': {}
        }

        # Step 1: Handle missing values
        cleansed_dataset, missing_value_results = self.handle_missing_values(
            cleansed_dataset, cleansing_profile
        )
        cleansing_results['cleansing_operations'].append(missing_value_results)

        # Step 2: Remove duplicates
        cleansed_dataset, duplicate_results = self.remove_duplicates(
            cleansed_dataset, cleansing_profile
        )
        cleansing_results['cleansing_operations'].append(duplicate_results)

        # Step 3: Standardize formats
        cleansed_dataset, standardization_results = self.standardize_formats(
            cleansed_dataset, cleansing_profile
        )
        cleansing_results['cleansing_operations'].append(standardization_results)

        # Step 4: Handle outliers
        cleansed_dataset, outlier_results = self.handle_outliers(
            cleansed_dataset, cleansing_profile
        )
        cleansing_results['cleansing_operations'].append(outlier_results)

        # Step 5: Validate and correct data types
        cleansed_dataset, datatype_results = self.correct_data_types(
            cleansed_dataset, cleansing_profile
        )
        cleansing_results['cleansing_operations'].append(datatype_results)

        # Step 6: Apply business rule corrections
        cleansed_dataset, business_rule_results = self.apply_business_rule_corrections(
            cleansed_dataset, cleansing_profile
        )
        cleansing_results['cleansing_operations'].append(business_rule_results)

        # Calculate quality improvements
        cleansing_results['quality_improvements'] = self.calculate_quality_improvements(
            original_dataset, cleansed_dataset
        )

        # Final summary
        cleansing_results['final_record_count'] = len(cleansed_dataset)
        cleansing_results['final_column_count'] = len(cleansed_dataset.columns)
        cleansing_results['records_removed'] = len(dataset) - len(cleansed_dataset)
        cleansing_results['cleansed_dataset'] = cleansed_dataset

        return cleansing_results

    def handle_missing_values(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        profile: str
    ) -> tuple:
        """
        Handle missing values based on profile and column characteristics
        """
        missing_value_results = {
            'operation_type': 'MISSING_VALUE_HANDLING',
            'strategies_applied': {},
            'values_imputed': 0,
            'records_removed': 0
        }

        for column in dataset.columns:
            missing_count = dataset[column].isnull().sum()
            if missing_count == 0:
                continue

            missing_percentage = (missing_count / len(dataset)) * 100

            # Determine handling strategy based on missing percentage and profile
            if missing_percentage > [HIGH_MISSING_THRESHOLD]:
                if profile == 'AGGRESSIVE':
                    # Remove column if too many missing values
                    dataset = dataset.drop(columns=[column])
                    missing_value_results['strategies_applied'][column] = {
                        'strategy': 'COLUMN_REMOVAL',
                        'missing_percentage': missing_percentage,
                        'reason': 'Excessive missing values'
                    }
                else:
                    # Keep column but flag for review
                    missing_value_results['strategies_applied'][column] = {
                        'strategy': 'FLAGGED_FOR_REVIEW',
                        'missing_percentage': missing_percentage,
                        'reason': 'High missing percentage requires review'
                    }

            elif missing_percentage > [MEDIUM_MISSING_THRESHOLD]:
                # Apply sophisticated imputation
                imputation_strategy = self.determine_imputation_strategy(dataset[column])
                dataset[column] = self.apply_imputation(dataset[column], imputation_strategy)

                missing_value_results['strategies_applied'][column] = {
                    'strategy': 'IMPUTATION',
                    'imputation_method': imputation_strategy['method'],
                    'missing_percentage': missing_percentage,
                    'values_imputed': missing_count
                }
                missing_value_results['values_imputed'] += missing_count

            else:
                # Simple imputation for low missing percentages
                if [PROCESSING_ALIAS].api.types.is_numeric_dtype(dataset[column]):
                    fill_value = dataset[column].median()
                    imputation_method = 'MEDIAN'
                else:
                    fill_value = dataset[column].mode().iloc[0] if not dataset[column].mode().empty else '[DEFAULT_STRING_VALUE]'
                    imputation_method = 'MODE'

                dataset[column] = dataset[column].fillna(fill_value)

                missing_value_results['strategies_applied'][column] = {
                    'strategy': 'SIMPLE_IMPUTATION',
                    'imputation_method': imputation_method,
                    'fill_value': str(fill_value),
                    'values_imputed': missing_count
                }
                missing_value_results['values_imputed'] += missing_count

        return dataset, missing_value_results

    def remove_duplicates(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        profile: str
    ) -> tuple:
        """
        Remove duplicate records based on profile settings
        """
        original_count = len(dataset)

        duplicate_results = {
            'operation_type': 'DUPLICATE_REMOVAL',
            'original_count': original_count,
            'duplicate_strategy': None,
            'duplicates_removed': 0,
            'final_count': None
        }

        # Identify duplicate handling strategy
        if profile == 'BASIC':
            # Remove exact duplicates only
            dataset = dataset.drop_duplicates()
            duplicate_results['duplicate_strategy'] = 'EXACT_DUPLICATES_ONLY'

        elif profile == 'STANDARD':
            # Remove duplicates based on key columns if defined
            key_columns = self.config.get('key_columns', None)
            if key_columns:
                dataset = dataset.drop_duplicates(subset=key_columns, keep='last')
                duplicate_results['duplicate_strategy'] = f'KEY_COLUMNS: [KEY_COLUMNS]'
            else:
                dataset = dataset.drop_duplicates()
                duplicate_results['duplicate_strategy'] = 'EXACT_DUPLICATES_ONLY'

        elif profile == 'AGGRESSIVE':
            # Apply fuzzy duplicate detection
            dataset, fuzzy_results = self.remove_fuzzy_duplicates(dataset)
            duplicate_results['duplicate_strategy'] = 'FUZZY_MATCHING'
            duplicate_results['fuzzy_matching_results'] = fuzzy_results

        duplicate_results['final_count'] = len(dataset)
        duplicate_results['duplicates_removed'] = original_count - len(dataset)

        return dataset, duplicate_results

    def standardize_formats(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        profile: str
    ) -> tuple:
        """
        Standardize data formats across columns
        """
        standardization_results = {
            'operation_type': 'FORMAT_STANDARDIZATION',
            'columns_standardized': {},
            'total_values_standardized': 0
        }

        for column in dataset.columns:
            column_type = str(dataset[column].dtype)
            standardization_applied = False
            values_standardized = 0

            # String column standardization
            if 'object' in column_type or 'string' in column_type:
                original_values = dataset[column].copy()

                # Apply string standardizations
                if profile in ['STANDARD', 'AGGRESSIVE']:
                    # Trim whitespace
                    dataset[column] = dataset[column].astype(str).str.strip()

                    # Convert to consistent case if specified
                    case_conversion = self.config.get('case_conversion', {}).get(column)
                    if case_conversion == 'UPPER':
                        dataset[column] = dataset[column].str.upper()
                    elif case_conversion == 'LOWER':
                        dataset[column] = dataset[column].str.lower()
                    elif case_conversion == 'TITLE':
                        dataset[column] = dataset[column].str.title()

                    # Remove extra spaces
                    dataset[column] = dataset[column].str.replace(r'\s+', ' ', regex=True)

                    standardization_applied = True

                # Apply format-specific standardizations
                format_type = self.detect_format_type(dataset[column])
                if format_type in ['PHONE', 'EMAIL', 'ZIP_CODE', 'SSN']:
                    dataset[column] = self.apply_format_standardization(dataset[column], format_type)
                    standardization_applied = True

                # Count standardized values
                if standardization_applied:
                    values_standardized = (original_values != dataset[column]).sum()

            # Numeric column standardization
            elif [PROCESSING_ALIAS].api.types.is_numeric_dtype(dataset[column]):
                if profile == 'AGGRESSIVE':
                    # Round to specified decimal places if configured
                    decimal_places = self.config.get('decimal_places', {}).get(column)
                    if decimal_places is not None:
                        original_values = dataset[column].copy()
                        dataset[column] = dataset[column].round(decimal_places)
                        values_standardized = (original_values != dataset[column]).sum()
                        standardization_applied = True

            # Date column standardization
            elif 'datetime' in column_type:
                if profile in ['STANDARD', 'AGGRESSIVE']:
                    # Standardize datetime format
                    date_format = self.config.get('date_formats', {}).get(column, '%Y-%m-%d')
                    original_values = dataset[column].copy()
                    dataset[column] = [PROCESSING_ALIAS].to_datetime(dataset[column]).dt.strftime(date_format)
                    values_standardized = len(dataset[column])
                    standardization_applied = True

            if standardization_applied:
                standardization_results['columns_standardized'][column] = {
                    'format_type': format_type if 'format_type' in locals() else column_type,
                    'values_standardized': values_standardized,
                    'standardization_percentage': (values_standardized / len(dataset)) * 100 if len(dataset) > 0 else 0
                }
                standardization_results['total_values_standardized'] += values_standardized

        return dataset, standardization_results

    def handle_outliers(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        profile: str
    ) -> tuple:
        """
        Detect and handle outliers in numeric columns
        """
        outlier_results = {
            'operation_type': 'OUTLIER_HANDLING',
            'columns_processed': {},
            'total_outliers_handled': 0
        }

        numeric_columns = dataset.select_dtypes(include=[[NUMERIC_TYPES]]).columns

        for column in numeric_columns:
            column_data = dataset[column].dropna()
            if len(column_data) < [MIN_SAMPLE_SIZE_FOR_OUTLIERS]:
                continue

            # Detect outliers using multiple methods
            outliers_iqr = self.detect_outliers_iqr(column_data)
            outliers_zscore = self.detect_outliers_zscore(column_data)
            outliers_isolation_forest = self.detect_outliers_isolation_forest(column_data)

            # Combine outlier detection results
            combined_outliers = set(outliers_iqr) | set(outliers_zscore) | set(outliers_isolation_forest)

            if len(combined_outliers) == 0:
                continue

            outlier_handling_strategy = self.determine_outlier_strategy(column, profile, len(combined_outliers))

            if outlier_handling_strategy == 'REMOVE':
                dataset = dataset[~dataset.index.isin(combined_outliers)]
                outliers_handled = len(combined_outliers)

            elif outlier_handling_strategy == 'CAP':
                # Cap outliers at percentile values
                lower_bound = column_data.quantile([OUTLIER_LOWER_PERCENTILE])
                upper_bound = column_data.quantile([OUTLIER_UPPER_PERCENTILE])

                dataset.loc[dataset[column] < lower_bound, column] = lower_bound
                dataset.loc[dataset[column] > upper_bound, column] = upper_bound
                outliers_handled = len(combined_outliers)

            elif outlier_handling_strategy == 'TRANSFORM':
                # Apply transformation (e.g., log transformation)
                if (column_data > 0).all():
                    dataset[column] = [NUMPY_ALIAS].log1p(dataset[column])
                outliers_handled = len(combined_outliers)

            else:  # KEEP
                outliers_handled = 0

            outlier_results['columns_processed'][column] = {
                'outliers_detected_iqr': len(outliers_iqr),
                'outliers_detected_zscore': len(outliers_zscore),
                'outliers_detected_isolation_forest': len(outliers_isolation_forest),
                'total_outliers_detected': len(combined_outliers),
                'outlier_percentage': (len(combined_outliers) / len(column_data)) * 100,
                'handling_strategy': outlier_handling_strategy,
                'outliers_handled': outliers_handled
            }

            outlier_results['total_outliers_handled'] += outliers_handled

        return dataset, outlier_results
```

QUALITY MONITORING AND ALERTING:
Real-time Quality Monitoring:
```python
# Real-time data quality monitoring system
class DataQualityMonitor:
    def __init__(self, config: dict):
        self.config = config
        self.monitoring_rules = [MONITORING_RULES_CONFIG]
        self.alert_manager = [ALERT_MANAGER]([ALERT_CONFIG])
        self.metrics_collector = [METRICS_COLLECTOR]([METRICS_CONFIG])

    def setup_continuous_monitoring(
        self,
        data_source: str,
        monitoring_frequency: str = 'HOURLY'
    ) -> dict:
        """
        Setup continuous data quality monitoring

### Args
            data_source: Data source identifier
            monitoring_frequency: Monitoring frequency (REAL_TIME/HOURLY/DAILY)

### Returns
            Monitoring setup configuration
        """

        monitoring_setup = {
            'data_source': data_source,
            'monitoring_frequency': monitoring_frequency,
            'quality_checks': self.define_quality_checks(data_source),
            'alert_rules': self.define_alert_rules(data_source),
            'monitoring_schedule': self.create_monitoring_schedule(monitoring_frequency),
            'dashboard_config': self.create_monitoring_dashboard(data_source)
        }

        return monitoring_setup

    def execute_quality_monitoring_cycle(
        self,
        data_source: str,
        dataset: [PROCESSING_ALIAS].DataFrame
    ) -> dict:
        """
        Execute a complete quality monitoring cycle
        """
        monitoring_results = {
            'data_source': data_source,
            'monitoring_timestamp': [CURRENT_TIMESTAMP],
            'dataset_summary': self.generate_dataset_summary(dataset),
            'quality_metrics': self.calculate_quality_metrics(dataset),
            'trend_analysis': self.analyze_quality_trends(data_source),
            'anomaly_detection': self.detect_quality_anomalies(dataset),
            'alert_triggers': [],
            'recommendations': []
        }

        # Check quality thresholds and generate alerts
        alert_triggers = self.check_quality_thresholds(monitoring_results['quality_metrics'])
        monitoring_results['alert_triggers'] = alert_triggers

        # Send alerts if necessary
        for alert in alert_triggers:
            self.send_quality_alert(alert, data_source)

        # Generate improvement recommendations
        monitoring_results['recommendations'] = self.generate_quality_recommendations(
            monitoring_results['quality_metrics'],
            monitoring_results['anomaly_detection']
        )

        # Store monitoring results for trend analysis
        self.store_monitoring_results(monitoring_results)

        return monitoring_results

    def calculate_quality_metrics(self, dataset: [PROCESSING_ALIAS].DataFrame) -> dict:
        """
        Calculate comprehensive quality metrics
        """
        quality_metrics = {
            'completeness_metrics': self.calculate_completeness_metrics(dataset),
            'accuracy_metrics': self.calculate_accuracy_metrics(dataset),
            'consistency_metrics': self.calculate_consistency_metrics(dataset),
            'validity_metrics': self.calculate_validity_metrics(dataset),
            'uniqueness_metrics': self.calculate_uniqueness_metrics(dataset),
            'timeliness_metrics': self.calculate_timeliness_metrics(dataset),
            'integrity_metrics': self.calculate_integrity_metrics(dataset),
            'overall_quality_score': 0
        }

        # Calculate weighted overall quality score
        dimension_weights = self.config.get('quality_dimension_weights', {
            'completeness': [COMPLETENESS_WEIGHT],
            'accuracy': [ACCURACY_WEIGHT],
            'consistency': [CONSISTENCY_WEIGHT],
            'validity': [VALIDITY_WEIGHT],
            'uniqueness': [UNIQUENESS_WEIGHT],
            'timeliness': [TIMELINESS_WEIGHT],
            'integrity': [INTEGRITY_WEIGHT]
        })

        weighted_score = 0
        total_weight = 0

        for dimension, weight in dimension_weights.items():
            if dimension in quality_metrics:
                dimension_score = quality_metrics[dimension]['overall_score']
                weighted_score += dimension_score * weight
                total_weight += weight

        quality_metrics['overall_quality_score'] = weighted_score / total_weight if total_weight > 0 else 0

        return quality_metrics

    def detect_quality_anomalies(self, dataset: [PROCESSING_ALIAS].DataFrame) -> dict:
        """
        Detect data quality anomalies using statistical methods
        """
        anomaly_detection = {
            'statistical_anomalies': self.detect_statistical_anomalies(dataset),
            'pattern_anomalies': self.detect_pattern_anomalies(dataset),
            'distribution_anomalies': self.detect_distribution_anomalies(dataset),
            'correlation_anomalies': self.detect_correlation_anomalies(dataset),
            'temporal_anomalies': self.detect_temporal_anomalies(dataset)
        }

        return anomaly_detection

    def create_quality_dashboard(self, data_source: str) -> dict:
        """
        Create interactive data quality dashboard configuration
        """
        dashboard_config = {
            'dashboard_name': f'Data Quality Dashboard - [DATA_SOURCE]',
            'data_source': data_source,
            'refresh_interval': [DASHBOARD_REFRESH_INTERVAL],
            'widgets': [
                {
                    'widget_type': 'QUALITY_SCORECARD',
                    'title': 'Overall Quality Score',
                    'metrics': ['overall_quality_score'],
                    'visualization': 'gauge',
                    'thresholds': {
                        'excellent': [EXCELLENT_QUALITY_THRESHOLD],
                        'good': [GOOD_QUALITY_THRESHOLD],
                        'poor': [POOR_QUALITY_THRESHOLD]
                    }
                },
                {
                    'widget_type': 'DIMENSION_BREAKDOWN',
                    'title': 'Quality Dimensions',
                    'metrics': [
                        'completeness_score',
                        'accuracy_score',
                        'consistency_score',
                        'validity_score',
                        'uniqueness_score',
                        'timeliness_score'
                    ],
                    'visualization': 'radar_chart'
                },
                {
                    'widget_type': 'TREND_ANALYSIS',
                    'title': 'Quality Trends',
                    'time_range': '[TREND_TIME_RANGE]',
                    'metrics': ['overall_quality_score'],
                    'visualization': 'line_chart'
                },
                {
                    'widget_type': 'TOP_ISSUES',
                    'title': 'Top Quality Issues',
                    'limit': [TOP_ISSUES_COUNT],
                    'metrics': ['quality_issues'],
                    'visualization': 'table'
                },
                {
                    'widget_type': 'COLUMN_QUALITY_HEATMAP',
                    'title': 'Column Quality Heatmap',
                    'metrics': ['column_quality_scores'],
                    'visualization': 'heatmap'
                },
                {
                    'widget_type': 'ALERT_SUMMARY',
                    'title': 'Recent Alerts',
                    'time_range': '[ALERT_TIME_RANGE]',
                    'metrics': ['active_alerts', 'resolved_alerts'],
                    'visualization': 'status_list'
                }
            ],
            'filters': [
                {
                    'filter_type': 'TIME_RANGE',
                    'default_value': '[DEFAULT_TIME_RANGE]',
                    'options': ['LAST_HOUR', 'LAST_DAY', 'LAST_WEEK', 'LAST_MONTH']
                },
                {
                    'filter_type': 'QUALITY_DIMENSION',
                    'default_value': 'ALL',
                    'options': ['ALL', 'COMPLETENESS', 'ACCURACY', 'CONSISTENCY', 'VALIDITY']
                },
                {
                    'filter_type': 'SEVERITY_LEVEL',
                    'default_value': 'ALL',
                    'options': ['ALL', 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW']
                }
            ]
        }

        return dashboard_config

# Automated quality remediation system
class QualityRemediationEngine:
    def __init__(self, config: dict):
        self.config = config
        self.remediation_rules = [REMEDIATION_RULES_CONFIG]
        self.ml_models = [ML_MODELS_CONFIG]

    def auto_remediate_quality_issues(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        quality_issues: list,
        remediation_level: str = 'CONSERVATIVE'
    ) -> dict:
        """
        Automatically remediate data quality issues

### Args
            dataset: Dataset with quality issues
            quality_issues: List of identified quality issues
            remediation_level: Level of remediation (CONSERVATIVE/STANDARD/AGGRESSIVE)

### Returns
            Remediation results and improved dataset
        """

        remediation_results = {
            'original_dataset_shape': dataset.shape,
            'issues_addressed': [],
            'issues_unresolved': [],
            'remediation_actions': [],
            'quality_improvement': {},
            'remediated_dataset': dataset.copy()
        }

        for issue in quality_issues:
            try:
                issue_type = issue['issue_type']
                severity = issue.get('severity', 'MEDIUM')

                # Determine if issue should be auto-remediated
                if self.should_auto_remediate(issue_type, severity, remediation_level):

                    # Apply appropriate remediation strategy
                    if issue_type == 'MISSING_VALUES':
                        remediation_result = self.remediate_missing_values(
                            remediation_results['remediated_dataset'],
                            issue
                        )

                    elif issue_type == 'DUPLICATE_RECORDS':
                        remediation_result = self.remediate_duplicates(
                            remediation_results['remediated_dataset'],
                            issue
                        )

                    elif issue_type == 'FORMAT_INCONSISTENCY':
                        remediation_result = self.remediate_format_issues(
                            remediation_results['remediated_dataset'],
                            issue
                        )

                    elif issue_type == 'OUTLIERS':
                        remediation_result = self.remediate_outliers(
                            remediation_results['remediated_dataset'],
                            issue
                        )

                    elif issue_type == 'REFERENTIAL_INTEGRITY':
                        remediation_result = self.remediate_referential_issues(
                            remediation_results['remediated_dataset'],
                            issue
                        )

                    elif issue_type == 'BUSINESS_RULE_VIOLATION':
                        remediation_result = self.remediate_business_rule_violations(
                            remediation_results['remediated_dataset'],
                            issue
                        )

                    else:
                        # Custom remediation for unknown issue types
                        remediation_result = self.apply_custom_remediation(
                            remediation_results['remediated_dataset'],
                            issue
                        )

                    # Update dataset if remediation was successful
                    if remediation_result['success']:
                        remediation_results['remediated_dataset'] = remediation_result['updated_dataset']
                        remediation_results['issues_addressed'].append(issue)
                        remediation_results['remediation_actions'].append(remediation_result)
                    else:
                        remediation_results['issues_unresolved'].append({
                            'issue': issue,
                            'reason': remediation_result.get('error_message', 'Unknown error')
                        })

                else:
                    remediation_results['issues_unresolved'].append({
                        'issue': issue,
                        'reason': f'Issue not eligible for auto-remediation at [REMEDIATION_LEVEL] level'
                    })

            except Exception as e:
                remediation_results['issues_unresolved'].append({
                    'issue': issue,
                    'reason': f'Remediation failed: {str(e)}'
                })

        # Calculate quality improvement
        remediation_results['quality_improvement'] = self.calculate_quality_improvement(
            dataset,
            remediation_results['remediated_dataset']
        )

        return remediation_results

    def remediate_missing_values(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        issue: dict
    ) -> dict:
        """
        Remediate missing value issues using advanced techniques
        """
        column = issue['column']
        missing_percentage = issue.get('missing_percentage', 0)

        try:
            if missing_percentage > [SEVERE_MISSING_THRESHOLD]:
                # Use ML-based imputation for severe missing values
                imputed_values = self.ml_based_imputation(dataset, column)
                dataset[column] = imputed_values
                remediation_method = 'ML_BASED_IMPUTATION'

            elif missing_percentage > [MODERATE_MISSING_THRESHOLD]:
                # Use advanced statistical imputation
                imputed_values = self.advanced_statistical_imputation(dataset, column)
                dataset[column] = imputed_values
                remediation_method = 'ADVANCED_STATISTICAL_IMPUTATION'

            else:
                # Use simple imputation for low missing percentages
                if [PROCESSING_ALIAS].api.types.is_numeric_dtype(dataset[column]):
                    fill_value = dataset[column].median()
                else:
                    fill_value = dataset[column].mode().iloc[0] if not dataset[column].mode().empty else '[DEFAULT_VALUE]'

                dataset[column] = dataset[column].fillna(fill_value)
                remediation_method = 'SIMPLE_IMPUTATION'

            return {
                'success': True,
                'updated_dataset': dataset,
                'remediation_method': remediation_method,
                'values_imputed': issue.get('missing_count', 0),
                'imputation_accuracy': self.estimate_imputation_accuracy(dataset, column)
            }

        except Exception as e:
            return {
                'success': False,
                'error_message': str(e),
                'updated_dataset': dataset
            }

    def ml_based_imputation(
        self,
        dataset: [PROCESSING_ALIAS].DataFrame,
        target_column: str
    ) -> [PROCESSING_ALIAS].Series:
        """
        Use machine learning models for advanced missing value imputation
        """
        from [ML_LIBRARY] import [ML_IMPUTATION_MODELS]

        # Prepare features for ML imputation
        feature_columns = [col for col in dataset.columns if col != target_column]
        feature_data = dataset[feature_columns].fillna(dataset[feature_columns].median())

        # Split data into training and prediction sets
        train_mask = dataset[target_column].notna()
        train_features = feature_data[train_mask]
        train_target = dataset.loc[train_mask, target_column]

        predict_features = feature_data[~train_mask]

        # Select appropriate ML model based on data type
        if [PROCESSING_ALIAS].api.types.is_numeric_dtype(dataset[target_column]):
            # Use regression for numeric data
            model = [ML_IMPUTATION_MODELS].RandomForestRegressor(
                n_estimators=[RF_N_ESTIMATORS],
                random_state=[RANDOM_STATE]
            )
        else:
            # Use classification for categorical data
            model = [ML_IMPUTATION_MODELS].RandomForestClassifier(
                n_estimators=[RF_N_ESTIMATORS],
                random_state=[RANDOM_STATE]
            )

        # Train model and make predictions
        model.fit(train_features, train_target)
        predicted_values = model.predict(predict_features)

        # Create complete series with original and predicted values
        complete_series = dataset[target_column].copy()
        complete_series.loc[~train_mask] = predicted_values

        return complete_series
```

OUTPUT: Deliver comprehensive data quality validation and management framework including:
1. Complete data profiling and discovery system
2. Advanced validation rules engine with business logic
3. Automated data cleansing and standardization procedures
4. Real-time quality monitoring and alerting system
5. Interactive quality dashboards and reporting
6. ML-powered quality issue detection and remediation
7. Data lineage and impact analysis for quality issues
8. Quality governance workflows and approval processes
9. Integration APIs for data pipeline quality checkpoints
10. Comprehensive quality metrics and KPI tracking systems
```

## Variables
[DATA_QUALITY_METHODOLOGY], [ORGANIZATION_NAME], [QUALITY_OBJECTIVES], [VALIDATION_APPROACH], [QUALITY_TOOLS], [INDUSTRY_SECTOR], [DATA_DOMAIN], [COMPLIANCE_REQUIREMENTS], [DATA_VOLUME_SCALE], [QUALITY_SLA_TARGETS], [QUALITY_BUSINESS_IMPACT], [STAKEHOLDER_QUALITY_REQUIREMENTS], [QUALITY_DIMENSIONS], [QUALITY_MONITORING_STRATEGY], [QUALITY_REMEDIATION_APPROACH], [QUALITY_GOVERNANCE_MODEL], [QUALITY_AUTOMATION_LEVEL], [DATA_PLATFORMS], [QUALITY_VALIDATION_TOOLS], [DATA_PROCESSING_FRAMEWORK], [QUALITY_MONITORING_PLATFORM], [QUALITY_ALERTING_SYSTEM], [METADATA_REPOSITORY], [LINEAGE_TRACKING_SYSTEM], [QUALITY_DASHBOARD_PLATFORM], [ACCURACY_THRESHOLD_PERCENTAGE], [COMPLETENESS_THRESHOLD_PERCENTAGE], [CONSISTENCY_THRESHOLD_PERCENTAGE], [TIMELINESS_THRESHOLD_HOURS], [UNIQUENESS_THRESHOLD_PERCENTAGE], [VALIDITY_THRESHOLD_PERCENTAGE], [OVERALL_QUALITY_TARGET], [CRITICAL_DATA_ELEMENTS], [DATA_PROCESSING_LIBRARY], [PROCESSING_ALIAS], [QUALITY_LIBRARY], [QUALITY_ALIAS], [STATISTICAL_LIBRARY], [STATISTICAL_FUNCTIONS], [VISUALIZATION_LIBRARY], [PLOTTING_FUNCTIONS], [PROFILING_CONFIG], [STATISTICAL_ANALYZER], [STATS_CONFIG], [PATTERN_ANALYZER], [PATTERN_CONFIG], [TABLE_SIZE_CALCULATION], [CURRENT_TIMESTAMP], [PROFILING_SCOPE_LEVEL], [SAMPLE_SIZE], [SCHEMA_HASH_CALCULATION], [HIGH_IO_THRESHOLD], [HIGH_READ_LATENCY_THRESHOLD], [HIGH_CPU_THRESHOLD], [TOP_VALUES_COUNT], [BOTTOM_VALUES_COUNT], [BUSINESS_START_HOUR], [BUSINESS_END_HOUR], [COMPLETENESS_WEIGHT], [ACCURACY_WEIGHT], [CONSISTENCY_WEIGHT], [VALIDITY_WEIGHT], [UNIQUENESS_WEIGHT], [TIMELINESS_WEIGHT], [INTEGRITY_WEIGHT], [COMPLETENESS_THRESHOLD], [RULES_ENGINE], [RULES_CONFIG], [SAMPLE_VIOLATION_COUNT], [SAMPLE_ORPHAN_COUNT], [VALIDITY_RULES_CONFIG], [CLEANSING_RULES_CONFIG], [STANDARDIZATION_RULES_CONFIG], [HIGH_MISSING_THRESHOLD], [MEDIUM_MISSING_THRESHOLD], [DEFAULT_STRING_VALUE], [NUMERIC_TYPES], [MIN_SAMPLE_SIZE_FOR_OUTLIERS], [OUTLIER_LOWER_PERCENTILE], [OUTLIER_UPPER_PERCENTILE], [NUMPY_ALIAS], [MONITORING_RULES_CONFIG], [ALERT_MANAGER], [ALERT_CONFIG], [METRICS_COLLECTOR], [METRICS_CONFIG], [DASHBOARD_REFRESH_INTERVAL], [EXCELLENT_QUALITY_THRESHOLD], [GOOD_QUALITY_THRESHOLD], [POOR_QUALITY_THRESHOLD], [TREND_TIME_RANGE], [TOP_ISSUES_COUNT], [ALERT_TIME_RANGE], [DEFAULT_TIME_RANGE], [REMEDIATION_RULES_CONFIG], [ML_MODELS_CONFIG], [SEVERE_MISSING_THRESHOLD], [MODERATE_MISSING_THRESHOLD], [DEFAULT_VALUE], [ML_LIBRARY], [ML_IMPUTATION_MODELS], [RF_N_ESTIMATORS], [RANDOM_STATE]

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
### Example 1: Financial Services Data Quality
```
DATA_QUALITY_METHODOLOGY: "Risk-based validation with regulatory compliance"
ORGANIZATION_NAME: "SecureBank Corp"
VALIDATION_APPROACH: "Comprehensive validation with real-time monitoring"
QUALITY_OBJECTIVES: "Ensure 99.9% accuracy for financial transactions and regulatory reporting"
COMPLIANCE_REQUIREMENTS: ["SOX", "Basel III", "GDPR", "PCI-DSS"]
ACCURACY_THRESHOLD_PERCENTAGE: "99.9"
TIMELINESS_THRESHOLD_HOURS: "1"
CRITICAL_DATA_ELEMENTS: ["transaction_amount", "customer_id", "account_balance"]
```

### Example 2: Healthcare Data Validation
```
DATA_QUALITY_METHODOLOGY: "Clinical data validation with HIPAA compliance"
ORGANIZATION_NAME: "HealthSystem Network"
VALIDATION_APPROACH: "Preventive validation with automated remediation"
QUALITY_OBJECTIVES: "Maintain patient data integrity and care quality standards"
COMPLIANCE_REQUIREMENTS: ["HIPAA", "FDA 21 CFR Part 11", "SOC 2"]
DATA_DOMAIN: "Electronic Health Records (EHR)"
COMPLETENESS_THRESHOLD_PERCENTAGE: "95"
VALIDITY_THRESHOLD_PERCENTAGE: "98"
```

### Example 3: E-commerce Platform Quality
```
DATA_QUALITY_METHODOLOGY: "Customer-centric quality validation"
ORGANIZATION_NAME: "GlobalRetail Inc"
VALIDATION_APPROACH: "Real-time validation with customer impact analysis"
QUALITY_OBJECTIVES: "Optimize customer experience through high-quality product and order data"
QUALITY_SLA_TARGETS: "< 2% invalid product information, < 0.1% order processing errors"
UNIQUENESS_THRESHOLD_PERCENTAGE: "99.5"
CONSISTENCY_THRESHOLD_PERCENTAGE: "97"
DATA_VOLUME_SCALE: "10TB+ daily transaction data"
```

## Customization Options

1. **Quality Methodologies**
   - Statistical process control
   - Risk-based validation
   - Regulatory compliance-driven
   - Business impact-focused
   - Machine learning-enhanced
   - Real-time continuous validation

2. **Validation Approaches**
   - Preventive (data entry validation)
   - Detective (post-ingestion validation)
   - Corrective (automated remediation)
   - Comprehensive (end-to-end validation)
   - Selective (critical data elements only)
   - Continuous (real-time monitoring)

3. **Quality Tools Integration**
   - Great Expectations
   - Apache Griffin
   - Talend Data Quality
   - Informatica Data Quality
   - AWS Deequ
   - Google Cloud Data Quality
   - Custom validation frameworks

4. **Industry Specializations**
   - Financial services (regulatory compliance)
   - Healthcare (clinical data integrity)
   - Retail/E-commerce (customer experience)
   - Manufacturing (IoT sensor data quality)
   - Government (data governance standards)
   - Insurance (actuarial data accuracy)

5. **Quality Dimensions Focus**
   - Accuracy (correctness of data values)
   - Completeness (presence of required data)
   - Consistency (uniformity across systems)
   - Timeliness (data freshness and availability)
   - Validity (format and constraint compliance)
   - Uniqueness (elimination of duplicates)
   - Integrity (referential and relational consistency)