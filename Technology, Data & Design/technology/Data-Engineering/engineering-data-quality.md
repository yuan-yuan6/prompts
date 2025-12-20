---
category: technology
related_templates:
- technology/Data-Engineering/data-pipeline-design.md
- data-analytics/Analytics-Engineering/analytics-data-quality.md
- data-analytics/data-governance-framework.md
tags:
- data-engineering
- data-quality
- data-validation
- data-governance
title: Data Quality Engineering
use_cases:
- Implementing automated data quality frameworks with validation rules, profiling, and monitoring achieving 99%+ accuracy and completeness across pipelines
- Building data quality gates in CI/CD pipelines using Great Expectations, dbt tests, or Soda to prevent bad data from reaching production
- Establishing quality SLAs with alerting, incident management, and remediation workflows for enterprise data platforms
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: engineering-data-quality
---

# Data Quality Engineering

## Purpose
Implement comprehensive data quality frameworks covering validation rules, profiling, monitoring, and remediation achieving measurable quality SLAs with automated detection and alerting for production data systems.

## Template

Implement data quality framework for {DATA_DOMAIN} achieving {QUALITY_TARGETS} with {MONITORING_APPROACH} monitoring and {SLA_REQUIREMENTS} SLAs.

**DATA QUALITY DIMENSIONS**

Define and measure quality across six core dimensions. Completeness: percentage of non-null values for required fields, measure at column and row level, target 95%+ for optional fields, 100% for required. Accuracy: percentage of values passing validation rules, compare against authoritative sources, measure format correctness and business rule compliance. Consistency: values match across systems and within dataset, referential integrity maintained, temporal consistency (no future dates for past events).

Timeliness: data freshness meets business requirements, measure max(event_time) vs current_time, partition arrival time vs SLA. Uniqueness: no unintended duplicates on natural keys, deduplication rate tracking, duplicate detection before and after processing. Validity: values conform to expected domains, formats, and ranges, enum values match allowed lists, patterns match expected formats.

Weight dimensions based on business impact. Critical fields (customer_id, transaction_amount): high weight, strict thresholds, immediate alerts. Important fields (email, phone): medium weight, warning thresholds, daily review. Nice-to-have fields (preferences, optional metadata): low weight, trend monitoring only.

**DATA PROFILING**

Implement automated profiling for baseline understanding. Statistical profiling: min, max, mean, median, standard deviation for numeric columns. Cardinality analysis: distinct values, uniqueness percentage, frequency distribution. Pattern detection: common formats, regex patterns, value length distribution. Null analysis: null percentage by column, null patterns across rows (all nulls, partial nulls).

Schedule profiling for continuous monitoring. Initial profiling: comprehensive analysis on first load, establish baselines. Incremental profiling: profile new data on each load, detect drift from baseline. Periodic deep profiling: weekly/monthly full dataset analysis, identify gradual changes. On-demand profiling: triggered on schema changes, new sources, quality incidents.

Tools for profiling at scale. Great Expectations profiling: auto-generate expectations from data, create data docs. pandas-profiling/ydata-profiling: detailed HTML reports for exploratory analysis. AWS Deequ: Spark-based profiling for large datasets, constraint suggestions. Apache Griffin: open-source quality solution with profiling, batch and streaming.

**VALIDATION RULES**

Design validation rules matching business requirements. Schema validation: column names, data types, nullability constraints match expected schema. Format validation: email regex, phone E.164 format, date ISO 8601, postal codes by country. Range validation: numeric bounds (amount > 0, age between 0-120), date ranges (not future, within retention). Referential integrity: foreign keys exist in reference tables, orphan detection.

Implement business rule validation. Cross-field rules: end_date > start_date, shipping_address required for physical products. Aggregation rules: daily sum matches source system, row counts within expected range (±10%). Temporal rules: monotonically increasing sequences, no gaps in time series. Domain-specific rules: Luhn check for credit cards, IBAN validation, SSN format.

Configure rule severity and handling. Critical rules (fail pipeline): null primary keys, invalid foreign keys, schema mismatch. Major rules (quarantine records): failed business validation, format errors on required fields. Minor rules (flag and continue): formatting issues on optional fields, soft validation failures. Warning rules (log only): approaching thresholds, unusual but valid values.

**VALIDATION FRAMEWORKS**

Configure Great Expectations for comprehensive testing. Expectation suites: group expectations by table/domain, version with data. Checkpoints: run expectations at pipeline stages, integrate with orchestrator. Data docs: auto-generated documentation, validation results history. Custom expectations: extend for domain-specific validation (e.g., geospatial checks).

Implement dbt tests for transformation validation. Built-in tests: unique, not_null, accepted_values, relationships (foreign keys). Custom tests: SQL-based tests for complex business logic. Test macros: reusable test patterns across models. Test severity: warn vs error, configure per test.

Use Soda for multi-platform validation. Soda Core: open-source, YAML-based checks, CLI and programmatic use. Soda Cloud: managed platform, anomaly detection, incident management. Cross-platform: same checks for warehouse, lake, source databases. Freshness checks: built-in freshness monitoring, SLA tracking.

**QUALITY MONITORING**

Track quality metrics continuously. Quality score: weighted average across dimensions, track by table/domain/pipeline. Trend analysis: week-over-week quality changes, detect gradual degradation. Anomaly detection: ML-based detection of unusual patterns, alert on statistical anomalies. SLA compliance: percentage of datasets meeting quality SLAs, SLA breach tracking.

Configure alerting for proactive detection. Threshold alerts: quality score below threshold (critical <90%, warning <95%). Freshness alerts: data older than SLA, pipeline delayed, source lag. Volume alerts: row count anomalies (±50% from expected), unexpected empty tables. Trend alerts: quality degrading over time, pattern changes detected.

Build quality dashboards for visibility. Executive dashboard: overall quality score, SLA compliance, trend summary. Domain dashboard: per-domain quality metrics, top issues, remediation status. Pipeline dashboard: quality by pipeline stage, failure rates, processing times. Incident dashboard: open quality issues, age, owner, resolution progress.

**DATA PROFILING AND OBSERVABILITY**

Implement data observability platforms. Monte Carlo: ML-powered anomaly detection, automatic lineage, incident management. Datafold: data diff for change detection, CI integration, column-level lineage. Bigeye: automated monitoring, anomaly detection, integrates with modern data stack. Elementary: dbt-native observability, open-source, self-hosted option.

Integrate observability with data pipelines. Pipeline integration: observability checks as pipeline stages, fail on critical issues. CI/CD integration: quality checks on PR, prevent regression deployment. Metadata collection: automatic schema tracking, lineage capture, usage statistics. Incident correlation: link quality issues to upstream changes, root cause identification.

**REMEDIATION WORKFLOWS**

Design issue classification and triage. Severity levels: P1 (critical, immediate action), P2 (major, same day), P3 (minor, within sprint), P4 (cosmetic, backlog). Impact assessment: downstream systems affected, business processes impacted, user count. Root cause categories: source system issues, transformation bugs, schema changes, infrastructure failures.

Implement remediation procedures. Automated remediation: auto-fix known patterns (trim whitespace, standardize case, apply defaults). Quarantine workflow: isolate bad records, continue processing good data, queue for review. Reprocessing: replay from source after fix, incremental vs full reprocess decision. Manual correction: workflow for human review and fix, approval process, audit trail.

Track remediation effectiveness. Resolution time: time from detection to fix, track by severity and category. Recurrence rate: same issue recurring, indicates incomplete fix. Fix effectiveness: quality improvement after remediation. Backlog management: age of open issues, prioritization, capacity planning.

**DATA GOVERNANCE INTEGRATION**

Connect quality to data governance. Data ownership: quality responsibilities by domain owner, escalation paths. Data stewardship: stewards responsible for quality rules, issue triage. Quality policies: documented standards, thresholds, handling procedures. Compliance requirements: regulatory quality requirements (BCBS 239, GDPR), audit evidence.

Implement quality in data contracts. Contract definition: expected schema, quality thresholds, SLAs between producer and consumer. Contract testing: automated validation of contract compliance on each delivery. Breaking change detection: alert on schema changes violating contracts. SLA enforcement: automatic escalation on SLA breach, chargeback for quality failures.

Deliver data quality framework as:

1. **QUALITY DIMENSIONS** - Definitions, measurement methods, weights, thresholds per dimension

2. **VALIDATION RULES** - Rule catalog by table/domain, severity levels, expected vs actual logic

3. **PROFILING CONFIGURATION** - Profiling schedule, baseline definitions, drift detection thresholds

4. **MONITORING SETUP** - Metrics collection, dashboards, alerting rules, escalation paths

5. **TOOL CONFIGURATION** - Great Expectations suites, dbt tests, Soda checks, observability platform

6. **REMEDIATION PROCEDURES** - Issue classification, triage workflow, fix procedures, SLA tracking

7. **GOVERNANCE INTEGRATION** - Data contracts, ownership matrix, compliance requirements

---

## Usage Examples

### Example 1: E-commerce Data Quality
**Prompt:** Implement data quality for EcommerceAnalytics covering orders, customers, and products achieving 99% accuracy, 95% completeness with 2-hour freshness SLA using Great Expectations and dbt tests.

**Expected Output:** Quality dimensions: completeness (required fields 100%, optional 90%), accuracy (99% validation pass rate), timeliness (max 2-hour lag from source). Validation rules: orders (order_id unique, customer_id exists, amount > 0, status in allowed values), customers (email format valid, created_date not future), products (sku unique, price > 0, category in catalog). Great Expectations: 3 suites (orders_suite, customers_suite, products_suite), checkpoint runs post-ETL, data docs published to S3. dbt tests: unique and not_null on PKs, relationships for FKs, custom test for order totals matching line items. Monitoring: quality score dashboard (Grafana), freshness monitoring (data loaded within SLA), volume tracking (±20% baseline). Alerting: Slack for warnings (quality <95%), PagerDuty for critical (quality <90% or freshness breach). Remediation: quarantine failed orders to dead letter table, auto-retry 3x, escalate to on-call after 4 hours. SLA: 99% quality score, 99.5% freshness SLA compliance, <4 hour P1 resolution.

### Example 2: Financial Data Quality
**Prompt:** Implement data quality for TradingData achieving 99.99% accuracy, 100% completeness for critical fields with real-time monitoring and SOX compliance using Soda and Monte Carlo.

**Expected Output:** Quality dimensions: accuracy (99.99% for trade data, 99.9% for market data), completeness (100% for regulatory fields, 99% for optional), timeliness (T+0 for intraday, T+1 for settlement). Validation rules: trades (trade_id unique, counterparty exists in reference, quantity > 0, price within market bounds), positions (position reconciles with trades, no negative holdings for long-only), market data (price within 10% of previous close, no stale quotes). Soda checks: freshness checks for each feed, schema validation on ingest, row count monitoring. Monte Carlo: ML anomaly detection on price/volume, automatic lineage to source systems, incident management with JIRA integration. Regulatory compliance: BCBS 239 data quality requirements, audit trail for all quality checks, evidence collection for SOX. Alerting: immediate escalation for trade data failures, 15-minute SLA for market data issues. Governance: data contracts with upstream systems, quality SLAs in vendor contracts, daily quality report to risk committee. Remediation: no auto-fix for financial data (manual review required), strict 4-eye principle for corrections, full audit trail.

### Example 3: Healthcare Data Quality
**Prompt:** Implement data quality for PatientRecords achieving HIPAA compliance with 99.9% accuracy on clinical data, PHI protection validation, and audit logging using Great Expectations and custom validators.

**Expected Output:** Quality dimensions: accuracy (99.9% for clinical data, 99% for administrative), completeness (100% for required clinical fields, MRN, DOB), validity (ICD-10 codes valid, drug codes in formulary). PHI validation: SSN format valid and not exposed in logs, date shifting applied for research datasets, minimum necessary principle for data access. Custom validators: ICD-10 code lookup validation, drug interaction checking, clinical range validation (vitals within physiological limits). Great Expectations: HIPAA-compliant configuration (no PHI in validation messages), encrypted data docs, access-controlled checkpoints. Audit logging: all data access logged, quality check results with user context, retention per HIPAA requirements. Access control: role-based access to quality dashboards, PHI fields masked in monitoring. Alerting: immediate alert for PHI exposure, escalation to privacy officer for data breaches. Governance: data stewards per clinical domain, quality review in data governance council, annual quality audit. Compliance: quality evidence for HIPAA audits, breach notification workflow integration.

---

## Cross-References

- [Data Pipeline Design](data-pipeline-design.md) - Quality gates within pipeline architecture
- [Analytics Data Quality](../../data-analytics/Analytics-Engineering/analytics-data-quality.md) - Quality for analytics workloads
- [Data Governance Framework](../../data-analytics/data-governance-framework.md) - Governance context for quality
