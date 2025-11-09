---
title: Data Quality Assessment Template
category: data-analytics/Analytics Engineering
tags: [automation, data-analytics, data-quality, profiling, template, validation]
use_cases:
  - Conducting comprehensive data quality assessments including initial quality evaluation, data profiling, anomaly detection, and quality scoring for data platforms and analytics systems.
  - Data quality evaluation
  - Quality assessment
related_templates:
  - analytics-data-quality-overview.md
  - data-profiling-validation.md
  - quality-metrics-monitoring.md
last_updated: 2025-11-09
---

# Data Quality Assessment Template

## Purpose
Conduct comprehensive data quality assessments including initial quality evaluation, data profiling, anomaly detection, quality scoring, and identification of quality issues for data platforms.

## Template

```
You are a data quality assessment specialist. Conduct a data quality assessment for [DATASET_NAME] containing [DATA_VOLUME] to evaluate [QUALITY_DIMENSIONS] using [ASSESSMENT_METHODS] and produce [DELIVERABLES].

ASSESSMENT FRAMEWORK:
Dataset Context:
- Dataset name: [DATASET_NAME]
- Data source: [DATA_SOURCE]
- Data volume: [DATA_VOLUME]
- Quality dimensions: [QUALITY_DIMENSIONS]
- Assessment methods: [ASSESSMENT_METHODS]
- Business context: [BUSINESS_CONTEXT]
- Critical data elements: [CRITICAL_DATA_ELEMENTS]
- Quality objectives: [QUALITY_OBJECTIVES]

### DATA QUALITY DIMENSIONS

### Six Dimensions of Data Quality
```
1. ACCURACY
   - Definition: Degree to which data correctly represents real-world entity
   - Measurement: % of values matching authoritative source
   - Target: [ACCURACY_TARGET]%
   - Assessment methods:
     * Source comparison
     * Statistical validation
     * Business rule verification
     * Domain expert review

2. COMPLETENESS
   - Definition: Extent to which all required data is present
   - Measurement: % of populated required fields
   - Target: [COMPLETENESS_TARGET]%
   - Assessment methods:
     * Null value analysis
     * Required field validation
     * Record completeness scoring
     * Coverage analysis

3. CONSISTENCY
   - Definition: Data uniformity across systems and over time
   - Measurement: % of records matching across sources
   - Target: [CONSISTENCY_TARGET]%
   - Assessment methods:
     * Cross-system comparison
     * Format standardization check
     * Temporal consistency validation
     * Referential integrity verification

4. TIMELINESS
   - Definition: Currency and availability of data when needed
   - Measurement: Average age of data vs. requirement
   - Target: Data < [TIMELINESS_TARGET] hours old
   - Assessment methods:
     * Timestamp analysis
     * Update frequency validation
     * Latency measurement
     * Staleness detection

5. VALIDITY
   - Definition: Conformance to defined formats, types, and ranges
   - Measurement: % of values passing validation rules
   - Target: [VALIDITY_TARGET]%
   - Assessment methods:
     * Format validation
     * Range checking
     * Type verification
     * Business rule validation

6. UNIQUENESS
   - Definition: No duplicate records for same entity
   - Measurement: % of unique records vs. expected
   - Target: [UNIQUENESS_TARGET]%
   - Assessment methods:
     * Duplicate detection
     * Primary key validation
     * Fuzzy matching
     * Entity resolution
```

### ASSESSMENT METHODOLOGY

### Initial Data Profiling
```python
import pandas as pd
import numpy as np
from datetime import datetime

class DataQualityAssessor:
    def __init__(self, dataset_name, data):
        self.dataset_name = dataset_name
        self.data = data
        self.assessment_results = {}
    
    def assess_completeness(self, required_columns):
        """Assess data completeness"""
        completeness_scores = {}
        
        for col in required_columns:
            if col in self.data.columns:
                non_null_count = self.data[col].notna().sum()
                total_count = len(self.data)
                completeness_pct = (non_null_count / total_count) * 100
                
                completeness_scores[col] = {
                    'completeness_percentage': completeness_pct,
                    'missing_count': total_count - non_null_count,
                    'status': 'PASS' if completeness_pct >= [COMPLETENESS_THRESHOLD] else 'FAIL'
                }
        
        overall_completeness = np.mean([s['completeness_percentage'] for s in completeness_scores.values()])
        
        return {
            'column_scores': completeness_scores,
            'overall_completeness': overall_completeness,
            'assessment_timestamp': datetime.now()
        }
    
    def assess_validity(self, validation_rules):
        """Assess data validity against rules"""
        validity_results = {}
        
        for rule_name, rule_config in validation_rules.items():
            column = rule_config['column']
            rule_type = rule_config['type']
            
            if rule_type == 'range':
                min_val = rule_config['min']
                max_val = rule_config['max']
                valid_mask = (self.data[column] >= min_val) & (self.data[column] <= max_val)
                
            elif rule_type == 'format':
                pattern = rule_config['pattern']
                valid_mask = self.data[column].astype(str).str.match(pattern)
                
            elif rule_type == 'values':
                allowed_values = rule_config['allowed_values']
                valid_mask = self.data[column].isin(allowed_values)
            
            valid_count = valid_mask.sum()
            total_count = len(self.data)
            validity_pct = (valid_count / total_count) * 100
            
            validity_results[rule_name] = {
                'validity_percentage': validity_pct,
                'invalid_count': total_count - valid_count,
                'status': 'PASS' if validity_pct >= [VALIDITY_THRESHOLD] else 'FAIL'
            }
        
        return validity_results
    
    def detect_duplicates(self, key_columns):
        """Detect duplicate records"""
        duplicates = self.data[self.data.duplicated(subset=key_columns, keep=False)]
        duplicate_count = len(duplicates)
        total_count = len(self.data)
        uniqueness_pct = ((total_count - duplicate_count) / total_count) * 100
        
        return {
            'duplicate_count': duplicate_count,
            'uniqueness_percentage': uniqueness_pct,
            'duplicate_records': duplicates,
            'status': 'PASS' if uniqueness_pct >= [UNIQUENESS_THRESHOLD] else 'FAIL'
        }
```

### QUALITY SCORING

### Overall Quality Score Calculation
```python
def calculate_quality_score(assessment_results):
    """Calculate weighted overall quality score"""
    
    dimension_weights = {
        'accuracy': [ACCURACY_WEIGHT],
        'completeness': [COMPLETENESS_WEIGHT],
        'consistency': [CONSISTENCY_WEIGHT],
        'timeliness': [TIMELINESS_WEIGHT],
        'validity': [VALIDITY_WEIGHT],
        'uniqueness': [UNIQUENESS_WEIGHT]
    }
    
    weighted_scores = []
    for dimension, weight in dimension_weights.items():
        if dimension in assessment_results:
            score = assessment_results[dimension]['score']
            weighted_scores.append(score * weight)
    
    overall_score = sum(weighted_scores)
    
    # Quality rating
    if overall_score >= 95:
        rating = 'EXCELLENT'
    elif overall_score >= 85:
        rating = 'GOOD'
    elif overall_score >= 70:
        rating = 'FAIR'
    else:
        rating = 'POOR'
    
    return {
        'overall_score': overall_score,
        'rating': rating,
        'dimension_scores': assessment_results,
        'improvement_priority': identify_improvement_areas(assessment_results)
    }
```

OUTPUT REQUIREMENTS:
1. **Assessment Report** - Comprehensive quality evaluation
2. **Quality Scorecard** - Scores by dimension
3. **Issue Summary** - Identified quality problems
4. **Remediation Recommendations** - Improvement suggestions
5. **Data Profile** - Statistical summary of dataset
```

## Variables

- [DATASET_NAME] - Name of dataset to assess
- [DATA_SOURCE] - Source system or location
- [DATA_VOLUME] - Size of dataset
- [QUALITY_DIMENSIONS] - Dimensions to evaluate
- [ASSESSMENT_METHODS] - Methods for assessment
- [BUSINESS_CONTEXT] - Business context for data
- [CRITICAL_DATA_ELEMENTS] - Most important fields
- [QUALITY_OBJECTIVES] - Quality goals
- [ACCURACY_TARGET] - Target accuracy percentage
- [COMPLETENESS_TARGET] - Target completeness percentage
- [CONSISTENCY_TARGET] - Target consistency percentage
- [TIMELINESS_TARGET] - Target data age in hours
- [VALIDITY_TARGET] - Target validity percentage
- [UNIQUENESS_TARGET] - Target uniqueness percentage

## Usage Examples

### Example 1: Customer Data Assessment
```
DATASET_NAME: "Customer Master Data"
DATA_VOLUME: "5M records"
QUALITY_DIMENSIONS: "All six dimensions"
CRITICAL_DATA_ELEMENTS: "customer_id, email, address, phone"
ACCURACY_TARGET: "98"
COMPLETENESS_TARGET: "95"
UNIQUENESS_TARGET: "99.9"
```

### Example 2: Financial Transaction Assessment
```
DATASET_NAME: "Daily Transactions"
DATA_VOLUME: "10M records/day"
QUALITY_DIMENSIONS: "Accuracy, completeness, timeliness, validity"
TIMELINESS_TARGET: "4"
VALIDITY_TARGET: "99.5"
```

## Best Practices

1. **Start with critical data** - Prioritize most important elements
2. **Use representative samples** - For large datasets
3. **Establish baselines** - Measure current state before improvement
4. **Document assumptions** - Record assessment criteria
5. **Involve business stakeholders** - Validate quality requirements
6. **Automate where possible** - Create reusable assessment scripts
7. **Track trends over time** - Monitor quality improvements
8. **Provide actionable insights** - Focus on improvement opportunities
