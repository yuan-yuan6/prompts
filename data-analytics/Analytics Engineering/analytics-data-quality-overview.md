---
title: Analytics Data Quality Overview
category: data-analytics/Analytics Engineering
tags: [data-analytics, data-quality, overview, strategy, template]
use_cases:
  - Overview and guidance for implementing comprehensive data quality management including assessment, profiling, cleansing, monitoring, and governance across the data quality lifecycle.
  - Quality strategy
  - Quality management
related_templates:
  - data-quality-assessment.md
  - data-profiling-validation.md
  - data-cleansing.md
  - quality-metrics-monitoring.md
  - data-governance-standards.md
last_updated: 2025-11-09
---

# Analytics Data Quality Overview

## Purpose
Comprehensive overview and guidance for implementing data quality management. This template helps you plan and execute quality initiatives across assessment, profiling, cleansing, monitoring, and governance.

## Available Data Quality Templates

### 1. Data Quality Assessment
**File:** `data-quality-assessment.md`
**Use for:** Initial quality evaluation, profiling, scoring, issue identification

### 2. Data Profiling and Validation
**File:** `data-profiling-validation.md`
**Use for:** Automated profiling, validation rules, constraint checking

### 3. Data Cleansing and Remediation
**File:** `data-cleansing.md`
**Use for:** Data cleansing, standardization, deduplication, correction

### 4. Quality Metrics and Monitoring
**File:** `quality-metrics-monitoring.md`
**Use for:** KPI tracking, dashboards, alerting, trend analysis

### 5. Data Governance Standards
**File:** `data-governance-standards.md`
**Use for:** Governance policies, standards, compliance, stewardship

## Data Quality Lifecycle

```
1. ASSESS → 2. PROFILE → 3. CLEANSE → 4. MONITOR → 5. GOVERN
     ↑                                                    ↓
     └────────────────── CONTINUOUS IMPROVEMENT ─────────┘
```

## Six Dimensions of Data Quality

1. **Accuracy** - Correctness of values
2. **Completeness** - Presence of required data
3. **Consistency** - Uniformity across systems
4. **Timeliness** - Currency and availability
5. **Validity** - Format and constraint compliance
6. **Uniqueness** - No unwanted duplicates

## Quick Start Guide

### Phase 1: Assess Current State (Week 1-2)
Use: `data-quality-assessment.md`
- Profile critical datasets
- Score quality dimensions
- Identify top issues
- Establish baseline

### Phase 2: Implement Validation (Week 3-4)
Use: `data-profiling-validation.md`
- Define validation rules
- Implement rule engine
- Automate profiling
- Test validation

### Phase 3: Cleanse Data (Week 5-6)
Use: `data-cleansing.md`
- Design cleansing processes
- Implement remediation
- Validate results
- Document changes

### Phase 4: Monitor Quality (Week 7-8)
Use: `quality-metrics-monitoring.md`
- Define KPIs
- Build dashboards
- Set up alerts
- Track trends

### Phase 5: Establish Governance (Week 9-10)
Use: `data-governance-standards.md`
- Define standards
- Assign stewards
- Document policies
- Ensure compliance

## Best Practices

1. **Start with critical data** - Focus on high-impact datasets
2. **Automate quality checks** - Build into data pipelines
3. **Monitor continuously** - Don't just assess once
4. **Involve stakeholders** - Business and technical
5. **Document everything** - Rules, processes, decisions
6. **Measure and improve** - Track progress over time
7. **Prevent issues** - Build quality in, not inspect it in
8. **Establish ownership** - Clear accountability

## Common Use Cases

| Scenario | Primary Templates | Key Actions |
|----------|------------------|-------------|
| New data source | Assessment, Profiling | Profile, validate, baseline |
| Quality issues | Assessment, Cleansing | Identify, remediate, prevent |
| Ongoing monitoring | Monitoring, Governance | Track KPIs, alert, improve |
| Compliance audit | Governance, Assessment | Document, evidence, attest |
| System migration | All templates | Assess, validate, cleanse, monitor |
