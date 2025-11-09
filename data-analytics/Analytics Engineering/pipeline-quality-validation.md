---
title: Pipeline Data Quality & Validation
category: data-analytics/Analytics Engineering
tags: [data-analytics, quality, validation, testing, monitoring]
use_cases:
  - Implementing comprehensive data quality checks, validation rules, data profiling, and quality monitoring for data pipelines to ensure data accuracy and reliability.
  - Building validation frameworks across bronze, silver, and gold layers
related_templates:
  - pipeline-development-overview.md
  - data-ingestion-extraction.md
  - data-transformation-processing.md
  - pipeline-monitoring-maintenance.md
last_updated: 2025-11-09
---

# Pipeline Data Quality & Validation

## Purpose
Implement comprehensive data quality frameworks including validation rules, profiling, anomaly detection, and quality monitoring to ensure data accuracy, completeness, and reliability across pipeline layers.

## Template

```
You are a data quality specialist. Design a comprehensive data quality framework for [ORGANIZATION_NAME] to validate data at [VALIDATION_LAYER] layer using [QUALITY_FRAMEWORK].

QUALITY REQUIREMENTS:
- Validation layer: [VALIDATION_LAYER] (Bronze/Silver/Gold/All)
- Quality dimensions: [QUALITY_DIMENSIONS] (Completeness/Accuracy/Consistency/Timeliness)
- Validation approach: [VALIDATION_APPROACH] (Rule-based/Statistical/ML-based)
- Quality framework: [QUALITY_FRAMEWORK]
- Failure handling: [FAILURE_HANDLING_STRATEGY]
- Quality SLAs: [QUALITY_SLAS]

Provide complete implementation for:
1. Data quality rule definitions
2. Validation execution logic
3. Quality scoring and metrics
4. Anomaly detection mechanisms
5. Quality reporting and alerting
6. Data profiling and discovery
```

## Data Quality Dimensions

### 1. Completeness Validation
```python
# Completeness checks for data quality
from [QUALITY_FRAMEWORK] import QualityValidator

class CompletenessValidator:
    """Validate data completeness"""

    @staticmethod
    def check_null_values(df, required_columns: list) -> dict:
        """
        Check for null values in required columns

        Args:
            df: DataFrame to validate
            required_columns: Columns that cannot be null

        Returns:
            Validation results dictionary
        """
        results = {}

        for col in required_columns:
            null_count = df[col].isna().sum()
            total_count = len(df)
            null_percentage = (null_count / total_count) * 100 if total_count > 0 else 0

            results[f'{col}_null_check'] = {
                'passed': null_count == 0,
                'null_count': null_count,
                'null_percentage': null_percentage,
                'severity': 'CRITICAL' if null_percentage > [NULL_THRESHOLD] else 'WARNING'
            }

        return results

    @staticmethod
    def check_record_count(df, expected_min: int, expected_max: int = None) -> dict:
        """
        Validate record count is within expected range

        Args:
            df: DataFrame to validate
            expected_min: Minimum expected record count
            expected_max: Maximum expected record count (optional)

        Returns:
            Validation results
        """
        actual_count = len(df)

        if expected_max:
            passed = expected_min <= actual_count <= expected_max
            message = f"Record count {actual_count} within range [{expected_min}, {expected_max}]"
        else:
            passed = actual_count >= expected_min
            message = f"Record count {actual_count} meets minimum {expected_min}"

        return {
            'passed': passed,
            'actual_count': actual_count,
            'expected_min': expected_min,
            'expected_max': expected_max,
            'message': message,
            'severity': 'HIGH' if not passed else 'INFO'
        }

    @staticmethod
    def check_expected_columns(df, expected_columns: list) -> dict:
        """
        Verify all expected columns are present

        Args:
            df: DataFrame to validate
            expected_columns: List of expected column names

        Returns:
            Validation results
        """
        actual_columns = set(df.columns)
        expected_columns_set = set(expected_columns)

        missing_columns = expected_columns_set - actual_columns
        extra_columns = actual_columns - expected_columns_set

        return {
            'passed': len(missing_columns) == 0,
            'missing_columns': list(missing_columns),
            'extra_columns': list(extra_columns),
            'severity': 'CRITICAL' if missing_columns else 'INFO'
        }
```

### 2. Accuracy Validation
```python
class AccuracyValidator:
    """Validate data accuracy"""

    @staticmethod
    def check_data_types(df, expected_types: dict) -> dict:
        """
        Validate data types match expectations

        Args:
            df: DataFrame to validate
            expected_types: Dictionary of column: expected_type

        Returns:
            Validation results
        """
        results = {}

        for col, expected_type in expected_types.items():
            if col not in df.columns:
                results[f'{col}_type_check'] = {
                    'passed': False,
                    'message': f'Column {col} not found',
                    'severity': 'HIGH'
                }
                continue

            actual_type = str(df[col].dtype)
            type_match = actual_type == expected_type

            results[f'{col}_type_check'] = {
                'passed': type_match,
                'expected_type': expected_type,
                'actual_type': actual_type,
                'severity': 'MEDIUM' if not type_match else 'INFO'
            }

        return results

    @staticmethod
    def check_value_ranges(df, range_rules: dict) -> dict:
        """
        Validate numeric values are within expected ranges

        Args:
            df: DataFrame to validate
            range_rules: Dictionary of column: (min, max) tuples

        Returns:
            Validation results
        """
        results = {}

        for col, (min_val, max_val) in range_rules.items():
            out_of_range = df[
                (df[col] < min_val) | (df[col] > max_val)
            ]
            out_of_range_count = len(out_of_range)
            out_of_range_pct = (out_of_range_count / len(df)) * 100

            results[f'{col}_range_check'] = {
                'passed': out_of_range_count == 0,
                'out_of_range_count': out_of_range_count,
                'out_of_range_percentage': out_of_range_pct,
                'min_value': min_val,
                'max_value': max_val,
                'severity': 'HIGH' if out_of_range_pct > [RANGE_THRESHOLD] else 'LOW'
            }

        return results

    @staticmethod
    def check_format_patterns(df, pattern_rules: dict) -> dict:
        """
        Validate string formats match expected patterns

        Args:
            df: DataFrame to validate
            pattern_rules: Dictionary of column: regex_pattern

        Returns:
            Validation results
        """
        import re
        results = {}

        for col, pattern in pattern_rules.items():
            regex = re.compile(pattern)
            invalid_formats = ~df[col].astype(str).str.match(regex)
            invalid_count = invalid_formats.sum()
            invalid_pct = (invalid_count / len(df)) * 100

            results[f'{col}_format_check'] = {
                'passed': invalid_count == 0,
                'invalid_count': invalid_count,
                'invalid_percentage': invalid_pct,
                'pattern': pattern,
                'severity': 'MEDIUM' if invalid_pct > [FORMAT_THRESHOLD] else 'LOW'
            }

        return results
```

### 3. Consistency Validation
```python
class ConsistencyValidator:
    """Validate data consistency"""

    @staticmethod
    def check_referential_integrity(
        df,
        reference_df,
        foreign_key: str,
        primary_key: str
    ) -> dict:
        """
        Validate foreign key relationships

        Args:
            df: DataFrame with foreign key
            reference_df: Reference DataFrame with primary key
            foreign_key: Column name in df
            primary_key: Column name in reference_df

        Returns:
            Validation results
        """
        # Find orphaned records
        orphaned = df[~df[foreign_key].isin(reference_df[primary_key])]
        orphaned_count = len(orphaned)
        orphaned_pct = (orphaned_count / len(df)) * 100

        return {
            'passed': orphaned_count == 0,
            'orphaned_count': orphaned_count,
            'orphaned_percentage': orphaned_pct,
            'foreign_key': foreign_key,
            'primary_key': primary_key,
            'severity': 'CRITICAL' if orphaned_pct > [REFERENTIAL_THRESHOLD] else 'WARNING'
        }

    @staticmethod
    def check_duplicate_keys(df, key_columns: list) -> dict:
        """
        Check for duplicate records based on key columns

        Args:
            df: DataFrame to validate
            key_columns: List of columns that form unique key

        Returns:
            Validation results
        """
        duplicates = df[df.duplicated(subset=key_columns, keep=False)]
        duplicate_count = len(duplicates)
        duplicate_pct = (duplicate_count / len(df)) * 100

        return {
            'passed': duplicate_count == 0,
            'duplicate_count': duplicate_count,
            'duplicate_percentage': duplicate_pct,
            'key_columns': key_columns,
            'severity': 'HIGH' if duplicate_count > 0 else 'INFO'
        }

    @staticmethod
    def check_cross_field_consistency(df, consistency_rules: list) -> dict:
        """
        Validate consistency between related fields

        Args:
            df: DataFrame to validate
            consistency_rules: List of consistency rule expressions

        Returns:
            Validation results
        """
        results = {}

        for i, rule in enumerate(consistency_rules):
            rule_name = rule.get('name', f'consistency_rule_{i}')
            expression = rule['expression']

            # Evaluate consistency rule
            violations = df[~df.eval(expression)]
            violation_count = len(violations)
            violation_pct = (violation_count / len(df)) * 100

            results[rule_name] = {
                'passed': violation_count == 0,
                'violation_count': violation_count,
                'violation_percentage': violation_pct,
                'rule_expression': expression,
                'severity': rule.get('severity', 'MEDIUM')
            }

        return results
```

### 4. Timeliness Validation
```python
class TimelinessValidator:
    """Validate data timeliness"""

    @staticmethod
    def check_data_freshness(df, timestamp_column: str, max_age_hours: int) -> dict:
        """
        Validate data is fresh enough

        Args:
            df: DataFrame to validate
            timestamp_column: Column with timestamps
            max_age_hours: Maximum acceptable age in hours

        Returns:
            Validation results
        """
        from datetime import datetime, timedelta

        current_time = datetime.now()
        max_timestamp = df[timestamp_column].max()
        data_age_hours = (current_time - max_timestamp).total_seconds() / 3600

        return {
            'passed': data_age_hours <= max_age_hours,
            'data_age_hours': data_age_hours,
            'max_allowed_age_hours': max_age_hours,
            'max_timestamp': max_timestamp,
            'current_time': current_time,
            'severity': 'HIGH' if data_age_hours > max_age_hours else 'INFO'
        }

    @staticmethod
    def check_processing_lag(
        extraction_time: datetime,
        processing_time: datetime,
        max_lag_minutes: int
    ) -> dict:
        """
        Validate processing lag is within acceptable limits

        Args:
            extraction_time: When data was extracted
            processing_time: When data is being processed
            max_lag_minutes: Maximum acceptable lag

        Returns:
            Validation results
        """
        lag_minutes = (processing_time - extraction_time).total_seconds() / 60

        return {
            'passed': lag_minutes <= max_lag_minutes,
            'lag_minutes': lag_minutes,
            'max_lag_minutes': max_lag_minutes,
            'extraction_time': extraction_time,
            'processing_time': processing_time,
            'severity': 'MEDIUM' if lag_minutes > max_lag_minutes else 'INFO'
        }
```

## Validation Orchestration

### Comprehensive Validation Framework
```python
@task
def validate_source_data(df: DataFrame, validation_config: dict) -> DataFrame:
    """
    Comprehensive validation of source data

    Args:
        df: Raw extracted DataFrame
        validation_config: Validation configuration

    Returns:
        Validated DataFrame with quality metrics
    """
    validation_results = {}

    # Completeness checks
    completeness_validator = CompletenessValidator()
    validation_results['null_checks'] = completeness_validator.check_null_values(
        df,
        validation_config['required_columns']
    )
    validation_results['record_count'] = completeness_validator.check_record_count(
        df,
        validation_config['min_records'],
        validation_config.get('max_records')
    )
    validation_results['column_check'] = completeness_validator.check_expected_columns(
        df,
        validation_config['expected_columns']
    )

    # Accuracy checks
    accuracy_validator = AccuracyValidator()
    validation_results['type_checks'] = accuracy_validator.check_data_types(
        df,
        validation_config['expected_types']
    )
    validation_results['range_checks'] = accuracy_validator.check_value_ranges(
        df,
        validation_config['range_rules']
    )
    validation_results['format_checks'] = accuracy_validator.check_format_patterns(
        df,
        validation_config.get('pattern_rules', {})
    )

    # Consistency checks
    consistency_validator = ConsistencyValidator()
    validation_results['duplicate_check'] = consistency_validator.check_duplicate_keys(
        df,
        validation_config['key_columns']
    )

    # Record validation results
    [VALIDATION_LOGGER].log_validation_results(
        source_system=validation_config['source_system'],
        validation_date=[PROCESSING_DATE],
        results=validation_results,
        record_count=len(df)
    )

    # Calculate overall quality score
    quality_score = calculate_quality_score(validation_results)
    df['data_quality_score'] = quality_score

    # Raise alert if quality below threshold
    if quality_score < validation_config['quality_threshold']:
        [ALERTING_SYSTEM].send_quality_alert(
            source_system=validation_config['source_system'],
            quality_score=quality_score,
            validation_results=validation_results
        )

    return df

def calculate_quality_score(validation_results: dict) -> float:
    """
    Calculate overall quality score from validation results

    Args:
        validation_results: Dictionary of validation results

    Returns:
        Quality score (0-100)
    """
    total_checks = 0
    passed_checks = 0

    for category, checks in validation_results.items():
        if isinstance(checks, dict):
            for check_name, result in checks.items():
                if isinstance(result, dict) and 'passed' in result:
                    total_checks += 1
                    if result['passed']:
                        passed_checks += 1

    quality_score = (passed_checks / total_checks * 100) if total_checks > 0 else 0
    return round(quality_score, 2)
```

## Anomaly Detection

### Statistical Anomaly Detection
```python
class AnomalyDetector:
    """Detect anomalies in data using statistical methods"""

    @staticmethod
    def detect_outliers_iqr(df, columns: list, iqr_multiplier: float = 1.5) -> dict:
        """
        Detect outliers using Interquartile Range (IQR) method

        Args:
            df: DataFrame to analyze
            columns: Numeric columns to check
            iqr_multiplier: IQR multiplier for outlier detection

        Returns:
            Dictionary of outlier detection results
        """
        results = {}

        for col in columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - (iqr_multiplier * IQR)
            upper_bound = Q3 + (iqr_multiplier * IQR)

            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            outlier_count = len(outliers)
            outlier_pct = (outlier_count / len(df)) * 100

            results[col] = {
                'outlier_count': outlier_count,
                'outlier_percentage': outlier_pct,
                'lower_bound': lower_bound,
                'upper_bound': upper_bound,
                'Q1': Q1,
                'Q3': Q3,
                'IQR': IQR
            }

        return results

    @staticmethod
    def detect_volume_anomalies(
        current_count: int,
        historical_counts: list,
        std_threshold: float = 3.0
    ) -> dict:
        """
        Detect volume anomalies using standard deviation

        Args:
            current_count: Current record count
            historical_counts: List of historical record counts
            std_threshold: Number of standard deviations for threshold

        Returns:
            Anomaly detection results
        """
        import numpy as np

        mean_count = np.mean(historical_counts)
        std_count = np.std(historical_counts)

        z_score = (current_count - mean_count) / std_count if std_count > 0 else 0
        is_anomaly = abs(z_score) > std_threshold

        return {
            'is_anomaly': is_anomaly,
            'current_count': current_count,
            'historical_mean': mean_count,
            'historical_std': std_count,
            'z_score': z_score,
            'threshold': std_threshold,
            'severity': 'HIGH' if is_anomaly else 'INFO'
        }
```

## Data Profiling

### Profiling Framework
```python
class DataProfiler:
    """Generate data profiling statistics"""

    @staticmethod
    def profile_dataset(df) -> dict:
        """
        Generate comprehensive data profile

        Args:
            df: DataFrame to profile

        Returns:
            Profiling results dictionary
        """
        profile = {
            'row_count': len(df),
            'column_count': len(df.columns),
            'memory_usage_mb': df.memory_usage(deep=True).sum() / 1024**2,
            'columns': {}
        }

        for col in df.columns:
            profile['columns'][col] = DataProfiler.profile_column(df[col])

        return profile

    @staticmethod
    def profile_column(series) -> dict:
        """
        Profile individual column

        Args:
            series: Pandas Series to profile

        Returns:
            Column profile dictionary
        """
        profile = {
            'dtype': str(series.dtype),
            'null_count': series.isna().sum(),
            'null_percentage': (series.isna().sum() / len(series)) * 100,
            'unique_count': series.nunique(),
            'unique_percentage': (series.nunique() / len(series)) * 100
        }

        # Numeric column stats
        if series.dtype in ['int64', 'float64']:
            profile.update({
                'min': series.min(),
                'max': series.max(),
                'mean': series.mean(),
                'median': series.median(),
                'std': series.std(),
                'q25': series.quantile(0.25),
                'q75': series.quantile(0.75)
            })

        # String column stats
        elif series.dtype == 'object':
            profile.update({
                'min_length': series.astype(str).str.len().min(),
                'max_length': series.astype(str).str.len().max(),
                'avg_length': series.astype(str).str.len().mean(),
                'most_common': series.value_counts().head(5).to_dict()
            })

        return profile
```

## Variables
[ORGANIZATION_NAME], [VALIDATION_LAYER], [QUALITY_DIMENSIONS], [VALIDATION_APPROACH], [QUALITY_FRAMEWORK], [FAILURE_HANDLING_STRATEGY], [QUALITY_SLAS], [NULL_THRESHOLD], [RANGE_THRESHOLD], [FORMAT_THRESHOLD], [REFERENTIAL_THRESHOLD], [VALIDATION_LOGGER], [PROCESSING_DATE], [ALERTING_SYSTEM]

## Best Practices

1. **Validate at every layer** - Bronze (schema), Silver (business rules), Gold (aggregations)
2. **Define quality thresholds** - Set acceptable error rates per use case
3. **Implement early validation** - Catch issues at ingestion
4. **Use statistical methods** - Detect anomalies automatically
5. **Profile data regularly** - Understand data distributions
6. **Track quality trends** - Monitor quality metrics over time
7. **Quarantine bad data** - Isolate failed records for analysis
8. **Alert on quality issues** - Notify teams of threshold breaches
9. **Document quality rules** - Maintain clear validation logic
10. **Test validation logic** - Ensure validators work correctly
