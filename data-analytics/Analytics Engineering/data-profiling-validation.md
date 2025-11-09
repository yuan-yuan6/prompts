---
title: Data Profiling and Validation Template
category: data-analytics/Analytics Engineering
tags: [automation, data-analytics, data-quality, profiling, template, validation]
use_cases:
  - Implementing data profiling methodologies and validation rule engines including automated profiling, validation rules, constraint checking, and quality rule management.
  - Data profiling
  - Validation rules
related_templates:
  - analytics-data-quality-overview.md
  - data-quality-assessment.md
  - data-cleansing.md
last_updated: 2025-11-09
---

# Data Profiling and Validation Template

## Purpose
Implement comprehensive data profiling methodologies and validation rule engines including automated profiling, validation rules, constraint checking, and quality rule management for enterprise data.

## Template

```
You are a data profiling and validation expert. Implement profiling and validation for [DATA_DOMAIN] using [PROFILING_TOOLS] with [VALIDATION_APPROACH] to enforce [QUALITY_RULES].

### DATA PROFILING

```python
class DataProfiler:
    def profile_dataset(self, data):
        profile = {
            'row_count': len(data),
            'column_count': len(data.columns),
            'memory_usage': data.memory_usage(deep=True).sum(),
            'columns': {}
        }
        
        for col in data.columns:
            profile['columns'][col] = {
                'dtype': str(data[col].dtype),
                'null_count': data[col].isnull().sum(),
                'null_percentage': data[col].isnull().sum() / len(data) * 100,
                'unique_count': data[col].nunique(),
                'sample_values': data[col].dropna().head(5).tolist()
            }
            
            if data[col].dtype in ['int64', 'float64']:
                profile['columns'][col].update({
                    'min': data[col].min(),
                    'max': data[col].max(),
                    'mean': data[col].mean(),
                    'median': data[col].median(),
                    'std': data[col].std()
                })
        
        return profile
```

### VALIDATION RULES

```python
class ValidationEngine:
    def __init__(self):
        self.rules = []
    
    def add_rule(self, rule_name, column, rule_type, **kwargs):
        self.rules.append({
            'name': rule_name,
            'column': column,
            'type': rule_type,
            'params': kwargs
        })
    
    def validate(self, data):
        results = []
        for rule in self.rules:
            if rule['type'] == 'not_null':
                valid = data[rule['column']].notna()
            elif rule['type'] == 'range':
                valid = (data[rule['column']] >= rule['params']['min']) & \
                        (data[rule['column']] <= rule['params']['max'])
            elif rule['type'] == 'regex':
                valid = data[rule['column']].astype(str).str.match(rule['params']['pattern'])
            
            results.append({
                'rule': rule['name'],
                'passed': valid.sum(),
                'failed': (~valid).sum(),
                'pass_rate': valid.sum() / len(data) * 100
            })
        
        return results
```

OUTPUT: Profiling reports, validation results, rule compliance metrics
```

## Variables
- [DATA_DOMAIN] - Data domain to profile
- [PROFILING_TOOLS] - Tools for profiling
- [VALIDATION_APPROACH] - Validation strategy
- [QUALITY_RULES] - Quality rules to enforce

## Best Practices
1. **Profile regularly** - Scheduled profiling runs
2. **Version control rules** - Track rule changes
3. **Automate validation** - Continuous validation
4. **Document rules** - Clear rule definitions
