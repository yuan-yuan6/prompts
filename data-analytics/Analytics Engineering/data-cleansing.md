---
title: Data Cleansing and Remediation Template
category: data-analytics/Analytics Engineering
tags: [automation, cleansing, data-analytics, data-quality, remediation, template]
use_cases:
  - Implementing data cleansing processes including standardization, normalization, deduplication, correction, and automated remediation workflows for data quality improvement.
  - Data cleansing
  - Data remediation
related_templates:
  - analytics-data-quality-overview.md
  - data-quality-assessment.md
  - data-profiling-validation.md
last_updated: 2025-11-09
---

# Data Cleansing and Remediation Template

## Purpose
Implement comprehensive data cleansing processes including standardization, normalization, deduplication, correction, and automated remediation workflows to improve data quality.

## Template

```
You are a data cleansing specialist. Design cleansing processes for [DATA_TYPE] using [CLEANSING_METHODS] with [AUTOMATION_LEVEL] to achieve [QUALITY_TARGETS].

### DATA CLEANSING FRAMEWORK

```python
class DataCleanser:
    def standardize_values(self, data, column, mappings):
        """Standardize values using mapping dictionary"""
        return data[column].map(mappings).fillna(data[column])
    
    def remove_duplicates(self, data, key_columns, keep='first'):
        """Remove duplicate records"""
        return data.drop_duplicates(subset=key_columns, keep=keep)
    
    def fill_missing_values(self, data, column, method='mean'):
        """Fill missing values"""
        if method == 'mean':
            fill_value = data[column].mean()
        elif method == 'median':
            fill_value = data[column].median()
        elif method == 'mode':
            fill_value = data[column].mode()[0]
        elif method == 'forward_fill':
            return data[column].fillna(method='ffill')
        
        return data[column].fillna(fill_value)
    
    def normalize_text(self, data, column):
        """Normalize text data"""
        return data[column].str.strip().str.lower().str.replace(r'\s+', ' ', regex=True)
    
    def validate_and_correct_email(self, email):
        """Validate and attempt to correct email addresses"""
        import re
        email = email.lower().strip()
        # Basic email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email, True
        return email, False
```

### AUTOMATED REMEDIATION

```python
class AutomatedRemediation:
    def __init__(self, remediation_rules):
        self.rules = remediation_rules
    
    def apply_remediation(self, data, quality_issues):
        """Apply automated remediation based on rules"""
        remediated_data = data.copy()
        remediation_log = []
        
        for issue in quality_issues:
            rule = self.rules.get(issue['type'])
            if rule and rule['automated']:
                result = rule['action'](remediated_data, issue)
                remediation_log.append({
                    'issue_type': issue['type'],
                    'records_affected': result['count'],
                    'action_taken': rule['description']
                })
        
        return remediated_data, remediation_log
```

OUTPUT: Cleansed data, remediation logs, quality improvement metrics
```

## Variables
- [DATA_TYPE] - Type of data to cleanse
- [CLEANSING_METHODS] - Methods for cleansing
- [AUTOMATION_LEVEL] - Level of automation
- [QUALITY_TARGETS] - Target quality metrics

## Best Practices
1. **Preserve original data** - Keep raw data unchanged
2. **Log all changes** - Track cleansing operations
3. **Validate results** - Verify cleansing effectiveness
4. **Automate repetitive tasks** - Use rules and scripts
