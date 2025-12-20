---
category: data-analytics
description: Design comprehensive data quality frameworks including profiling, validation rules, cleansing processes, monitoring systems, and automated remediation for enterprise data platforms
title: Data Quality and Validation
tags:
- data-quality
- data-validation
- data-profiling
- analytics-engineering
use_cases:
- Profiling datasets to discover quality issues and data characteristics
- Designing validation rule engines for schema and business rule enforcement
- Implementing automated data cleansing and standardization pipelines
- Building real-time quality monitoring with alerting and dashboards
related_templates:
- data-analytics/Analytics-Engineering/analytics-data-modeling.md
- data-analytics/Analytics-Engineering/analytics-pipeline-design.md
- data-analytics/data-governance-framework.md
industries:
- finance
- healthcare
- retail
- technology
- government
type: framework
difficulty: intermediate
slug: analytics-data-quality
---

# Data Quality and Validation

## Purpose
Design comprehensive data quality frameworks covering data profiling, validation rule engines, cleansing processes, quality monitoring, and automated remediation. This framework ensures data accuracy, completeness, consistency, timeliness, validity, and uniqueness across enterprise data platforms.

## Template

Design a comprehensive data quality framework for {DATA_CONTEXT}, validating against {QUALITY_REQUIREMENTS} to support {BUSINESS_OBJECTIVES}.

**1. Data Profiling and Discovery**

Begin with comprehensive data profiling to understand your data's current state and identify quality issues. Profile each dataset at the table level—record count, column count, storage size, freshness, and schema structure. Profile at the column level—data type, null count, distinct count, min/max/mean for numerics, length statistics for strings, and value distribution patterns. Calculate completeness (percentage of non-null values), cardinality (distinct value ratio), and detect potential primary keys. For numeric columns, compute descriptive statistics including percentiles, standard deviation, skewness, and kurtosis to understand distribution shape. For string columns, analyze length distribution, character patterns (alphabetic, numeric, mixed), and format consistency (emails, phones, dates). For datetime columns, identify range, gaps, temporal patterns, and timezone consistency. Detect anomalies including outliers (values beyond 3 standard deviations or IQR bounds), unexpected nulls in required fields, and format violations. Document data patterns discovered and their business implications.

**2. Quality Dimension Assessment**

Assess data quality across six core dimensions with quantified scores. Completeness measures presence of required data—calculate percentage of non-null values for each column, weight by business criticality, and aggregate to dataset score. Accuracy measures correctness of values—validate against authoritative sources, check referential integrity, and verify business rule compliance. Consistency measures uniformity across systems—compare values across tables and sources, verify format standardization, and check temporal consistency. Timeliness measures data freshness—calculate lag from source event to availability, track refresh frequency adherence, and measure query-time recency. Validity measures conformance to formats and constraints—check data type compliance, range validity, pattern matching (regex for emails, phones), and domain value membership. Uniqueness measures absence of duplicates—identify exact duplicates, fuzzy duplicates (similar records that should be merged), and inappropriate cardinality. Weight each dimension by business importance and calculate overall quality score using the formula: weighted sum of dimension scores divided by total weights.

**3. Validation Rule Engine Design**

Design a comprehensive validation rule engine with multiple rule categories. Schema validation rules enforce structural constraints—required column presence, data type compliance, nullability constraints, and column naming conventions. Business rule validation enforces domain logic—value range constraints (price > 0, age 0-150), cross-field dependencies (end_date >= start_date), conditional requirements (if status='shipped' then ship_date required), and calculation verification (line_item_total = quantity × unit_price). Referential integrity rules verify relationships—foreign key existence in parent tables, orphan record detection, and cardinality validation (one-to-many, many-to-many). Format validation rules check patterns—email format with regex, phone number formats by region, date format consistency, and code format compliance (SKU, account numbers). Statistical validation rules detect anomalies—z-score thresholds for outliers, trend deviation alerts, and distribution shift detection. For each rule, specify severity (critical/warning/info), failure threshold (percentage tolerable), and remediation action (reject/flag/auto-correct).

**4. Data Cleansing Procedures**

Design automated cleansing procedures to remediate quality issues. For missing values, apply context-appropriate strategies—delete records with excessive nulls (>50% columns), impute with statistical methods (mean/median for numeric, mode for categorical), use ML-based imputation for correlated features, or flag for manual review. For duplicates, implement exact matching on business keys, fuzzy matching using similarity algorithms (Levenshtein, Jaro-Winkler) for near-duplicates, and survivorship rules determining which record values to retain during merge. For format standardization, apply transformations—case normalization, whitespace trimming, date format unification, phone number formatting, and address standardization. For outliers, implement bounded replacement (cap at percentile thresholds), transformation (log, winsorization), or flagging for investigation. For referential integrity violations, either reject records, assign to default/unknown category, or cascade corrections. Log all cleansing operations with before/after values, transformation applied, and timestamp for auditability. Calculate quality improvement metrics comparing pre- and post-cleansing scores.

**5. Quality Monitoring Architecture**

Design real-time quality monitoring with continuous validation. Implement quality checks at pipeline checkpoints—ingestion validation (reject malformed at entry), transformation validation (verify logic correctness), and load validation (reconcile counts and sums). Define monitoring frequency by data criticality—real-time for financial transactions, hourly for operational data, daily for analytical datasets. Calculate quality metrics at each checkpoint and store in quality metrics repository with timestamps for trend analysis. Implement anomaly detection using statistical process control—track quality scores over time, set control limits (mean ± 2-3 standard deviations), and alert on out-of-control conditions. Design quality dashboards showing current scores by dimension and dataset, trend charts over time, drill-down to specific issues, and comparison to SLA thresholds. Create alert escalation tiers—automated remediation for minor issues, analyst notification for moderate issues, and incident escalation for critical failures affecting downstream systems.

**6. Quality Alerting and Escalation**

Configure intelligent alerting to catch issues without alert fatigue. Define alert thresholds by dimension and criticality—critical data elements require higher thresholds (99%+ completeness), less critical can tolerate lower (95%). Implement alert suppression for known patterns—scheduled maintenance windows, expected seasonality, and already-acknowledged issues. Design alert routing—data engineers for technical failures, data stewards for business rule violations, business owners for critical data quality degradation. Include in alerts: affected dataset, quality dimension, current score, threshold violated, sample records, and suggested remediation. Implement alert aggregation to group related issues rather than flooding with individual alerts. Track alert response times and resolution effectiveness. Create runbooks for common quality issues with step-by-step remediation procedures.

**7. Quality Governance and Ownership**

Establish governance structure for sustained data quality. Define data ownership—data owners (business accountability), data stewards (operational quality management), and data engineers (technical implementation). Create quality SLAs with measurable targets by dataset and dimension—document acceptable thresholds, measurement frequency, reporting cadence, and escalation procedures. Implement quality certification process—datasets must meet quality thresholds before promotion to production, with automated gates in deployment pipelines. Design quality metadata catalog documenting quality rules, historical scores, ownership, and lineage for each dataset. Schedule regular quality reviews—weekly operational reviews of quality trends, monthly steward reviews of rule effectiveness, and quarterly governance reviews of SLA achievement. Track quality costs including remediation effort, downstream impact of quality failures, and investment in quality tools.

**8. Automated Remediation and ML Enhancement**

Implement automated remediation for scalable quality management. Design remediation workflows triggered by validation failures—automatic retry for transient errors, default value assignment for missing non-critical fields, record quarantine for critical failures pending review. Implement ML-enhanced quality features—train models to predict likely correct values for imputation, detect anomalies using unsupervised learning (isolation forest, DBSCAN), and classify records by quality risk score. Use pattern learning to discover validation rules automatically—analyze historical data to infer expected ranges, formats, and relationships. Implement feedback loops where manual corrections inform automated remediation rules. Track remediation effectiveness—success rate of auto-corrections, false positive rate requiring manual override, and time saved versus manual processing. Continuously improve remediation models with new data and feedback.

Deliver your data quality framework as:

1. **Profiling report** with column-level statistics, quality scores by dimension, and issue inventory
2. **Quality scorecard** showing current state across six dimensions with trends and SLA status
3. **Validation rule catalog** documenting all rules with severity, thresholds, and remediation actions
4. **Cleansing procedures** specifying transformations for each issue type with logging requirements
5. **Monitoring architecture** with checkpoint design, metric collection, and dashboard specifications
6. **Alert configuration** with thresholds, routing, and escalation procedures
7. **Governance model** defining ownership, SLAs, certification process, and review cadence
8. **Remediation playbook** with automated workflows and ML enhancement opportunities

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DATA_CONTEXT}` | Data domain, systems, and scale | "customer data platform with 50M records across CRM, marketing, and support systems" |
| `{QUALITY_REQUIREMENTS}` | Quality thresholds and compliance needs | "99% completeness for PII fields, 100% referential integrity, GDPR compliance for data accuracy" |
| `{BUSINESS_OBJECTIVES}` | How quality supports business goals | "enabling personalized marketing with <1% bounce rate and regulatory audit readiness" |

---

## Usage Examples

### Example 1: Financial Services Data Quality
**Prompt:** "Design a comprehensive data quality framework for {DATA_CONTEXT: transaction processing system handling 10M daily transactions across payment, settlement, and reconciliation datasets}, validating against {QUALITY_REQUIREMENTS: 99.99% accuracy for transaction amounts, 100% referential integrity, zero duplicate transactions, SOX and Basel III compliance}, to support {BUSINESS_OBJECTIVES: regulatory reporting accuracy and real-time fraud detection with <100ms latency impact}."

**Expected Output:** Profiling report identifying critical fields (transaction_id, amount, timestamp, account_ids) with current quality scores. Quality scorecard: accuracy 99.97% (below 99.99% threshold—flagged), completeness 99.99%, uniqueness 100%, timeliness 99.8%. Validation rules: exact duplicate detection on transaction_id, amount range validation ($0.01-$10M), foreign key validation for account references, temporal sequence validation (settlement_date >= transaction_date). Real-time monitoring at ingestion with reject-on-failure for critical rules. Alert configuration: immediate pager for accuracy drops below 99.99%, Slack for daily quality summaries. Governance: transaction data steward reviews daily exceptions, quarterly SOX audit preparation with quality certification.

### Example 2: Healthcare Data Quality
**Prompt:** "Design a comprehensive data quality framework for {DATA_CONTEXT: electronic health records system with 5M patient records, clinical encounters, medications, and lab results across 20 hospitals}, validating against {QUALITY_REQUIREMENTS: 100% patient identifier accuracy, 98% clinical data completeness, HIPAA compliance for data integrity}, to support {BUSINESS_OBJECTIVES: clinical decision support accuracy and quality measure reporting for CMS reimbursement}."

**Expected Output:** Profiling revealing MRN completeness at 99.8%, diagnosis code validity at 96% (ICD-10 format violations), medication dosage outliers in 0.3% of records. Quality dimensions: completeness varies by data type (demographics 99%, clinical notes 87%), validity issues concentrated in free-text fields. Validation rules: MRN format and check-digit validation, ICD-10/CPT code lookup validation, medication dosage range checks by drug class, temporal consistency (discharge_date >= admission_date). Cleansing: standardize name formats, normalize medication names to RxNorm, flag outlier dosages for pharmacist review. HIPAA-compliant audit logging of all data access and modifications. Governance: clinical data stewards per hospital, monthly quality reviews aligned with CMS reporting deadlines.

### Example 3: E-commerce Data Quality
**Prompt:** "Design a comprehensive data quality framework for {DATA_CONTEXT: product catalog and order management system with 2M SKUs and 500K daily orders across web, mobile, and marketplace channels}, validating against {QUALITY_REQUIREMENTS: 99% product data completeness for customer-facing fields, zero pricing errors, inventory accuracy within 2%}, to support {BUSINESS_OBJECTIVES: reducing cart abandonment from bad product data and preventing revenue loss from pricing errors}."

**Expected Output:** Profiling: product descriptions 94% complete (below threshold), images present for 97% SKUs, pricing populated 100% but 0.2% have $0 or negative values. Quality dimensions: completeness gap in product attributes varies by category (electronics 98%, apparel 89%), consistency issues between marketplace and direct channels. Validation rules: required fields by category template, price range validation by category ($1-$10K electronics, $5-$500 apparel), inventory count non-negative, cross-channel price consistency (max 5% variance). Real-time validation on catalog updates with rejection of invalid prices. Automated enrichment: ML-based attribute extraction from descriptions, image quality scoring. Alert routing: merchandising team for completeness gaps, pricing team for immediate price anomalies, operations for inventory discrepancies.

---

## Cross-References

- [analytics-data-modeling.md](analytics-data-modeling.md) - Data modeling patterns that support quality
- [analytics-pipeline-design.md](analytics-pipeline-design.md) - Pipeline design with quality checkpoints
- [data-governance-framework.md](../data-governance-framework.md) - Governance structures for data quality
