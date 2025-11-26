---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- ai-ml
- design
- research
- security
- strategy
- testing
title: Data Quality Template
use_cases:
- Creating implement comprehensive data quality frameworks including validation, cleansing,
  monitoring, profiling, and governance to ensure high-quality, reliable, and trustworthy
  data across enterprise systems.
- Project planning and execution
- Strategy development
industries:
- finance
- government
- manufacturing
- technology
type: template
difficulty: intermediate
slug: engineering-data-quality
---

# Data Quality Template

## Purpose
Implement comprehensive data quality frameworks including validation, cleansing, monitoring, profiling, and governance to ensure high-quality, reliable, and trustworthy data across enterprise systems.

## Quick Data Quality Prompt
Implement data quality for [dataset/pipeline]. Dimensions: completeness, accuracy, consistency, timeliness, uniqueness. Rules: [null checks], [value ranges], [referential integrity], [business logic]. Tools: [Great Expectations/dbt tests/Soda]. Profiling: statistical summaries, distribution analysis. Alerting: threshold breaches → PagerDuty/Slack. Dashboard: quality scores by table, trend analysis. SLA: [X%] quality score, [Y-hour] freshness.

---

## Quick Start

**Data Quality Framework (1-2 Days):**
1. **Profile critical datasets** - Run data profiling on 3-5 key tables (customer, transaction, product), identify null rates, duplicates, outliers
2. **Define validation rules** - Create 10-15 rules per dataset (e.g., email format valid, revenue >= 0, customer_id not null, date ranges valid)
3. **Implement automated checks** - Add validation to ETL pipeline, quarantine failed records, alert on >5% failure rate
4. **Set up monitoring dashboard** - Track completeness rate (% non-null), accuracy rate (% passing validation), timeliness (data age)
5. **Establish remediation process** - Define SLAs (P1: fix in 4 hours, P2: 1 day), create runbooks for common issues

**Key Decision:** Focus on business-critical fields first (revenue, customer ID). Don't block pipelines for cosmetic issues (formatting).

---

## Template Structure

### Data Quality Overview
- **Data Domain**: [DATA_DOMAIN]
- **Quality Scope**: [QUALITY_SCOPE]
- **Business Context**: [BUSINESS_CONTEXT]
- **Stakeholders**: [STAKEHOLDERS]
- **Quality Objectives**: [QUALITY_OBJECTIVES]
- **Success Metrics**: [SUCCESS_METRICS]
- **Quality Standards**: [QUALITY_STANDARDS]
- **Compliance Requirements**: [COMPLIANCE_REQUIREMENTS]
- **Budget**: [QUALITY_BUDGET]
- **Timeline**: [QUALITY_TIMELINE]

### Data Quality Dimensions
- **Accuracy**: [ACCURACY]
- **Completeness**: [COMPLETENESS]
- **Consistency**: [CONSISTENCY]
- **Validity**: [VALIDITY]
- **Uniqueness**: [UNIQUENESS]
- **Timeliness**: [TIMELINESS]
- **Integrity**: [INTEGRITY]
- **Conformity**: [CONFORMITY]
- **Precision**: [PRECISION]
- **Reliability**: [RELIABILITY]

### Data Profiling
- **Profiling Strategy**: [PROFILING_STRATEGY]
- **Profiling Tools**: [PROFILING_TOOLS]
- **Profiling Scope**: [PROFILING_SCOPE]
- **Statistical Analysis**: [STATISTICAL_ANALYSIS]
- **Pattern Analysis**: [PATTERN_ANALYSIS]
- **Distribution Analysis**: [DISTRIBUTION_ANALYSIS]
- **Relationship Analysis**: [RELATIONSHIP_ANALYSIS]
- **Anomaly Detection**: [ANOMALY_DETECTION]
- **Metadata Discovery**: [METADATA_DISCOVERY]
- **Profiling Schedule**: [PROFILING_SCHEDULE]

### Data Validation
- **Validation Rules**: [VALIDATION_RULES]
- **Business Rules**: [BUSINESS_RULES]
- **Data Types**: [DATA_TYPE_VALIDATION]
- **Format Validation**: [FORMAT_VALIDATION]
- **Range Validation**: [RANGE_VALIDATION]
- **List Validation**: [LIST_VALIDATION]
- **Cross-Field Validation**: [CROSS_FIELD_VALIDATION]
- **Referential Integrity**: [REFERENTIAL_INTEGRITY]
- **Custom Validations**: [CUSTOM_VALIDATIONS]
- **Validation Framework**: [VALIDATION_FRAMEWORK]

### Data Cleansing
- **Cleansing Strategy**: [CLEANSING_STRATEGY]
- **Standardization**: [STANDARDIZATION]
- **Normalization**: [NORMALIZATION]
- **Deduplication**: [DEDUPLICATION]
- **Missing Value Treatment**: [MISSING_VALUE_TREATMENT]
- **Outlier Treatment**: [OUTLIER_TREATMENT]
- **Format Correction**: [FORMAT_CORRECTION]
- **Data Enrichment**: [DATA_ENRICHMENT]
- **Error Correction**: [ERROR_CORRECTION]
- **Transformation Rules**: [TRANSFORMATION_RULES]

### Quality Monitoring
- **Monitoring Framework**: [MONITORING_FRAMEWORK]
- **Quality Metrics**: [QUALITY_METRICS]
- **KPI Definitions**: [KPI_DEFINITIONS]
- **Threshold Settings**: [THRESHOLD_SETTINGS]
- **Alert Configuration**: [ALERT_CONFIGURATION]
- **Dashboard Design**: [DASHBOARD_DESIGN]
- **Reporting Schedule**: [REPORTING_SCHEDULE]
- **Trend Analysis**: [TREND_ANALYSIS]
- **Root Cause Analysis**: [ROOT_CAUSE_ANALYSIS]
- **Continuous Monitoring**: [CONTINUOUS_MONITORING]

### Quality Assessment
- **Assessment Methodology**: [ASSESSMENT_METHODOLOGY]
- **Scoring Models**: [SCORING_MODELS]
- **Benchmarking**: [BENCHMARKING]
- **Quality Scorecards**: [QUALITY_SCORECARDS]
- **Maturity Assessment**: [MATURITY_ASSESSMENT]
- **Gap Analysis**: [GAP_ANALYSIS]
- **Risk Assessment**: [RISK_ASSESSMENT]
- **Impact Analysis**: [IMPACT_ANALYSIS]
- **Improvement Roadmap**: [IMPROVEMENT_ROADMAP]
- **Priority Matrix**: [PRIORITY_MATRIX]

### Issue Management
- **Issue Classification**: [ISSUE_CLASSIFICATION]
- **Issue Tracking**: [ISSUE_TRACKING]
- **Escalation Process**: [ESCALATION_PROCESS]
- **Resolution Workflow**: [RESOLUTION_WORKFLOW]
- **Priority Assignment**: [PRIORITY_ASSIGNMENT]
- **SLA Management**: [SLA_MANAGEMENT]
- **Communication Plan**: [COMMUNICATION_PLAN]
- **Status Reporting**: [STATUS_REPORTING]
- **Closure Criteria**: [CLOSURE_CRITERIA]
- **Lessons Learned**: [LESSONS_LEARNED]

### Data Governance
- **Governance Framework**: [GOVERNANCE_FRAMEWORK]
- **Data Ownership**: [DATA_OWNERSHIP]
- **Data Stewardship**: [DATA_STEWARDSHIP]
- **Quality Policies**: [QUALITY_POLICIES]
- **Standards Definition**: [STANDARDS_DEFINITION]
- **Roles and Responsibilities**: [ROLES_RESPONSIBILITIES]
- **Decision Framework**: [DECISION_FRAMEWORK]
- **Change Management**: [CHANGE_MANAGEMENT]
- **Compliance Monitoring**: [COMPLIANCE_MONITORING]
- **Audit Procedures**: [AUDIT_PROCEDURES]

### Quality Controls
- **Preventive Controls**: [PREVENTIVE_CONTROLS]
- **Detective Controls**: [DETECTIVE_CONTROLS]
- **Corrective Controls**: [CORRECTIVE_CONTROLS]
- **Automated Controls**: [AUTOMATED_CONTROLS]
- **Manual Controls**: [MANUAL_CONTROLS]
- **Control Testing**: [CONTROL_TESTING]
- **Control Monitoring**: [CONTROL_MONITORING]
- **Control Documentation**: [CONTROL_DOCUMENTATION]
- **Control Effectiveness**: [CONTROL_EFFECTIVENESS]
- **Control Updates**: [CONTROL_UPDATES]

### Data Lineage
- **Lineage Tracking**: [LINEAGE_TRACKING]
- **Source Identification**: [SOURCE_IDENTIFICATION]
- **Transformation Tracking**: [TRANSFORMATION_TRACKING]
- **Impact Analysis**: [LINEAGE_IMPACT_ANALYSIS]
- **Dependency Mapping**: [DEPENDENCY_MAPPING]
- **Change Impact**: [CHANGE_IMPACT]
- **Data Flow Documentation**: [DATA_FLOW_DOCUMENTATION]
- **Lineage Visualization**: [LINEAGE_VISUALIZATION]
- **Metadata Management**: [METADATA_MANAGEMENT]
- **Lineage Automation**: [LINEAGE_AUTOMATION]

### Quality Testing
- **Test Strategy**: [TEST_STRATEGY]
- **Test Cases**: [TEST_CASES]
- **Test Data**: [TEST_DATA]
- **Test Automation**: [TEST_AUTOMATION]
- **Regression Testing**: [REGRESSION_TESTING]
- **Performance Testing**: [QUALITY_PERFORMANCE_TESTING]
- **Volume Testing**: [VOLUME_TESTING]
- **Boundary Testing**: [BOUNDARY_TESTING]
- **Integration Testing**: [QUALITY_INTEGRATION_TESTING]
- **User Acceptance Testing**: [USER_ACCEPTANCE_TESTING]

### Remediation Framework
- **Remediation Strategy**: [REMEDIATION_STRATEGY]
- **Action Plans**: [ACTION_PLANS]
- **Fix Procedures**: [FIX_PROCEDURES]
- **Data Recovery**: [DATA_RECOVERY]
- **Reprocessing**: [REPROCESSING]
- **Manual Corrections**: [MANUAL_CORRECTIONS]
- **Automated Fixes**: [AUTOMATED_FIXES]
- **Validation Post-Fix**: [VALIDATION_POST_FIX]
- **Impact Assessment**: [REMEDIATION_IMPACT_ASSESSMENT]
- **Communication**: [REMEDIATION_COMMUNICATION]

### Tools and Technologies
- **Quality Tools**: [QUALITY_TOOLS]
- **Profiling Tools**: [PROFILING_TOOLS_TECH]
- **Validation Tools**: [VALIDATION_TOOLS]
- **Cleansing Tools**: [CLEANSING_TOOLS]
- **Monitoring Tools**: [MONITORING_TOOLS]
- **Reporting Tools**: [REPORTING_TOOLS]
- **Workflow Tools**: [WORKFLOW_TOOLS]
- **Integration Tools**: [INTEGRATION_TOOLS]
- **Metadata Tools**: [METADATA_TOOLS]
- **Automation Tools**: [AUTOMATION_TOOLS]

### Metrics and KPIs
- **Quality Metrics**: [QUALITY_METRICS_DETAIL]
- **Business KPIs**: [BUSINESS_KPIS]
- **Technical KPIs**: [TECHNICAL_KPIS]
- **Process KPIs**: [PROCESS_KPIS]
- **Cost Metrics**: [COST_METRICS]
- **Efficiency Metrics**: [EFFICIENCY_METRICS]
- **User Satisfaction**: [USER_SATISFACTION]
- **Compliance Metrics**: [COMPLIANCE_METRICS]
- **Trend Metrics**: [TREND_METRICS]
- **Comparative Metrics**: [COMPARATIVE_METRICS]

### Training and Adoption
- **Training Strategy**: [TRAINING_STRATEGY]
- **Role-Based Training**: [ROLE_BASED_TRAINING]
- **Tool Training**: [TOOL_TRAINING]
- **Process Training**: [PROCESS_TRAINING]
- **Awareness Programs**: [AWARENESS_PROGRAMS]
- **Certification Programs**: [CERTIFICATION_PROGRAMS]
- **Knowledge Management**: [KNOWLEDGE_MANAGEMENT]
- **Best Practices Sharing**: [BEST_PRACTICES_SHARING]
- **Change Management**: [ADOPTION_CHANGE_MANAGEMENT]
- **User Support**: [USER_SUPPORT]

### Cost-Benefit Analysis
- **Cost Categories**: [COST_CATEGORIES]
- **Implementation Costs**: [IMPLEMENTATION_COSTS]
- **Operational Costs**: [OPERATIONAL_COSTS]
- **Resource Costs**: [RESOURCE_COSTS]
- **Technology Costs**: [TECHNOLOGY_COSTS]
- **Benefit Categories**: [BENEFIT_CATEGORIES]
- **Revenue Benefits**: [REVENUE_BENEFITS]
- **Cost Savings**: [COST_SAVINGS]
- **Risk Reduction**: [RISK_REDUCTION]
- **ROI Calculation**: [ROI_CALCULATION]

## Prompt Template

Implement comprehensive data quality framework for [DATA_DOMAIN] covering [QUALITY_SCOPE] to achieve [QUALITY_OBJECTIVES] for [STAKEHOLDERS]. Meet [QUALITY_STANDARDS] and ensure [COMPLIANCE_REQUIREMENTS] compliance within [QUALITY_BUDGET] budget and [QUALITY_TIMELINE] timeline.

**Quality Dimensions:**
- Ensure [ACCURACY]% accuracy and [COMPLETENESS]% completeness
- Maintain [CONSISTENCY] across systems and [VALIDITY] per business rules
- Achieve [UNIQUENESS] without duplicates and [TIMELINESS] for real-time needs
- Verify [INTEGRITY], [CONFORMITY], [PRECISION], and [RELIABILITY]

**Data Profiling:**
- Use [PROFILING_TOOLS] for [PROFILING_SCOPE] analysis
- Perform [STATISTICAL_ANALYSIS] and [PATTERN_ANALYSIS]
- Conduct [DISTRIBUTION_ANALYSIS] and [RELATIONSHIP_ANALYSIS]
- Implement [ANOMALY_DETECTION] and [METADATA_DISCOVERY]
- Schedule [PROFILING_SCHEDULE] automated profiling

**Validation Framework:**
- Define [VALIDATION_RULES] and [BUSINESS_RULES]
- Implement [DATA_TYPE_VALIDATION] and [FORMAT_VALIDATION]
- Set up [RANGE_VALIDATION] and [LIST_VALIDATION]
- Configure [CROSS_FIELD_VALIDATION] and [REFERENTIAL_INTEGRITY]
- Deploy [VALIDATION_FRAMEWORK] with [CUSTOM_VALIDATIONS]

**Cleansing Strategy:**
- Apply [STANDARDIZATION] and [NORMALIZATION] rules
- Implement [DEDUPLICATION] and [MISSING_VALUE_TREATMENT]
- Handle [OUTLIER_TREATMENT] and [FORMAT_CORRECTION]
- Perform [DATA_ENRICHMENT] and [ERROR_CORRECTION]
- Execute [TRANSFORMATION_RULES] automatically

**Monitoring and Alerting:**
- Track [QUALITY_METRICS] and [KPI_DEFINITIONS]
- Set [THRESHOLD_SETTINGS] with [ALERT_CONFIGURATION]
- Create [DASHBOARD_DESIGN] for [REPORTING_SCHEDULE]
- Perform [TREND_ANALYSIS] and [ROOT_CAUSE_ANALYSIS]
- Enable [CONTINUOUS_MONITORING] capabilities

**Governance Framework:**
- Establish [DATA_OWNERSHIP] and [DATA_STEWARDSHIP]
- Define [QUALITY_POLICIES] and [STANDARDS_DEFINITION]
- Assign [ROLES_RESPONSIBILITIES] and [DECISION_FRAMEWORK]
- Implement [CHANGE_MANAGEMENT] and [COMPLIANCE_MONITORING]
- Set up [AUDIT_PROCEDURES] for oversight

**Issue Management:**
- Classify issues using [ISSUE_CLASSIFICATION]
- Track with [ISSUE_TRACKING] and [ESCALATION_PROCESS]
- Follow [RESOLUTION_WORKFLOW] with [PRIORITY_ASSIGNMENT]
- Monitor [SLA_MANAGEMENT] and execute [COMMUNICATION_PLAN]
- Document [LESSONS_LEARNED] and [CLOSURE_CRITERIA]

**Technology Stack:**
- Deploy [QUALITY_TOOLS] for overall management
- Use [VALIDATION_TOOLS] and [CLEANSING_TOOLS]
- Implement [MONITORING_TOOLS] and [REPORTING_TOOLS]
- Integrate [WORKFLOW_TOOLS] and [AUTOMATION_TOOLS]
- Manage [METADATA_TOOLS] for lineage tracking

Please provide implementation roadmap, tool configurations, process definitions, training materials, and success metrics with specific recommendations for achieving data quality objectives.

## Usage Examples

### Customer Data Quality
```
Implement comprehensive data quality framework for Customer Master Data covering CRM, Marketing, Sales systems to achieve 99% accuracy, 95% completeness objectives for Sales, Marketing, Customer Service stakeholders. Meet ISO 8000, GDPR quality standards and ensure GDPR, CCPA compliance within $500K budget and 6-month timeline.

Quality Dimensions:
- Ensure 99% accuracy and 95% completeness
- Maintain referential consistency across CRM, ERP systems and business rule validity per customer lifecycle rules
- Achieve 99.9% uniqueness without duplicates and real-time timeliness for customer interactions
- Verify foreign key integrity, format conformity, address precision, and source reliability

Data Profiling:
- Use Informatica Data Quality for customer, contact, address profiling scope analysis
- Perform statistical analysis on demographic fields and regex pattern analysis on identifiers
- Conduct frequency distribution analysis and customer-contact relationship analysis
- Implement ML-based anomaly detection and automated metadata discovery
- Schedule daily automated profiling with weekly reporting

### Validation Framework
- Define 50+ validation rules and customer lifecycle business rules
- Implement strong data type validation and email/phone format validation
- Set up age, income range validation and country code list validation
- Configure customer-contact cross field validation and CRM-ERP referential integrity
- Deploy Great Expectations validation framework with custom email/phone validations

### Monitoring and Alerting
- Track accuracy, completeness, timeliness quality metrics and customer satisfaction, data processing time kpi definitions
- Set 95% accuracy threshold settings with Slack, email alert configuration
- Create Tableau dashboard design for daily, weekly reporting schedule
- Perform monthly trend analysis and automated root cause analysis
- Enable 24/7 continuous monitoring capabilities
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[DATA_DOMAIN]` | Data area being governed | "Customer Master Data", "Financial Transactions", "Product Catalog", "Sales Data", "IoT Sensor Data" |
| `[QUALITY_SCOPE]` | Systems and data in scope | "CRM, ERP, Data Warehouse", "all customer touchpoints", "transactional systems", "analytics pipelines" |
| `[BUSINESS_CONTEXT]` | Business use case | "customer 360 initiative", "regulatory reporting", "real-time fraud detection", "ML model training" |
| `[STAKEHOLDERS]` | Teams and individuals involved | "Data Governance Council", "Business Analysts", "Data Engineers", "Compliance team" |
| `[QUALITY_OBJECTIVES]` | Specify the quality objectives | "Increase efficiency by 30%" |
| `[SUCCESS_METRICS]` | Success measurement criteria | "DQ score >95%", "zero critical defects", "SLA compliance >99%", "issue resolution <4 hours" |
| `[QUALITY_STANDARDS]` | Quality framework standards | "ISO 8000", "DAMA DMBOK", "DCAM", "internal DQ policy" |
| `[COMPLIANCE_REQUIREMENTS]` | Regulatory requirements | "GDPR", "CCPA", "SOX", "BCBS 239", "HIPAA", "MiFID II" |
| `[QUALITY_BUDGET]` | Specify the quality budget | "$500,000" |
| `[QUALITY_TIMELINE]` | Specify the quality timeline | "6 months" |
| `[ACCURACY]` | Accuracy target percentage | "99%", "99.9%", "99.99%", ">98% for critical fields" |
| `[COMPLETENESS]` | Completeness target percentage | "95%", "100% for required fields", ">90% for optional" |
| `[CONSISTENCY]` | Consistency requirements | "referential consistency across CRM/ERP", "format consistency", "cross-system alignment" |
| `[VALIDITY]` | Validity rules | "business rule compliance", "domain value validation", "format correctness" |
| `[UNIQUENESS]` | Uniqueness requirements | "99.9% no duplicates", "unique customer IDs", "deduplication within 24 hours" |
| `[TIMELINESS]` | Data freshness requirements | "real-time (<1 min)", "near-real-time (<15 min)", "daily refresh", "hourly updates" |
| `[INTEGRITY]` | Data integrity checks | "foreign key integrity", "referential integrity", "transaction integrity" |
| `[CONFORMITY]` | Format conformity standards | "ISO date formats", "phone number E.164", "address standardization" |
| `[PRECISION]` | Data precision requirements | "2 decimal places for currency", "6 decimal places for geo-coordinates" |
| `[RELIABILITY]` | Source reliability assessment | "primary source verified", "secondary source validated", "confidence scoring" |
| `[PROFILING_STRATEGY]` | Profiling approach | "automated continuous profiling", "batch profiling on load", "sampling-based" |
| `[PROFILING_TOOLS]` | Data profiling tools | "Great Expectations", "dbt tests", "Informatica Data Quality", "Talend DQ", "AWS Deequ" |
| `[PROFILING_SCOPE]` | Profiling coverage | "all critical tables", "new data sources", "customer and transaction data" |
| `[STATISTICAL_ANALYSIS]` | Statistical methods | "mean/median/mode", "standard deviation", "null rate analysis", "cardinality" |
| `[PATTERN_ANALYSIS]` | Pattern detection methods | "regex pattern matching", "format detection", "value distribution patterns" |
| `[DISTRIBUTION_ANALYSIS]` | Distribution analysis approach | "frequency distribution", "histogram analysis", "percentile analysis" |
| `[RELATIONSHIP_ANALYSIS]` | Relationship validation | "FK relationships", "business entity relationships", "cross-table dependencies" |
| `[ANOMALY_DETECTION]` | Anomaly detection methods | "ML-based outlier detection", "statistical z-score", "IQR method", "time-series anomalies" |
| `[METADATA_DISCOVERY]` | Metadata capture approach | "automated schema discovery", "data catalog integration", "lineage tracking" |
| `[PROFILING_SCHEDULE]` | Profiling frequency | "daily automated", "weekly deep profiling", "on-demand for new sources" |
| `[VALIDATION_RULES]` | Validation rule types | "50+ validation rules per dataset", "schema validation", "semantic validation" |
| `[BUSINESS_RULES]` | Business logic validation | "customer lifecycle rules", "transaction limits", "product constraints" |
| `[DATA_TYPE_VALIDATION]` | Type checking approach | "strict type enforcement", "schema validation", "JSON schema validation" |
| `[FORMAT_VALIDATION]` | Format checking rules | "email regex", "phone E.164", "date ISO 8601", "postal code formats" |
| `[RANGE_VALIDATION]` | Range and boundary checks | "age 0-120", "price >0", "date within valid range", "percentage 0-100" |
| `[LIST_VALIDATION]` | Enumeration validation | "country code ISO 3166", "currency ISO 4217", "status values", "category codes" |
| `[CROSS_FIELD_VALIDATION]` | Multi-field validation | "end_date > start_date", "shipping_address required if physical product" |
| `[REFERENTIAL_INTEGRITY]` | FK validation approach | "customer_id exists", "product_id valid", "cross-system reference checks" |
| `[CUSTOM_VALIDATIONS]` | Custom business logic | "Luhn check for credit cards", "IBAN validation", "custom regex patterns" |
| `[VALIDATION_FRAMEWORK]` | Validation tool/framework | "Great Expectations", "dbt tests", "Pandera", "Cerberus", "JSON Schema" |
| `[CLEANSING_STRATEGY]` | Data cleansing approach | "automated cleansing pipeline", "manual review for critical errors", "quarantine and fix" |
| `[STANDARDIZATION]` | Standardization rules | "address standardization USPS", "name casing", "phone normalization" |
| `[NORMALIZATION]` | Data normalization | "Unicode normalization", "whitespace trimming", "case standardization" |
| `[DEDUPLICATION]` | Deduplication approach | "fuzzy matching", "exact match + merge", "probabilistic matching", "golden record" |
| `[MISSING_VALUE_TREATMENT]` | Null handling strategy | "imputation", "default values", "flag and report", "reject record" |
| `[OUTLIER_TREATMENT]` | Outlier handling | "cap at percentiles", "flag for review", "statistical winsorization" |
| `[FORMAT_CORRECTION]` | Format standardization | "date format conversion", "phone number formatting", "address parsing" |
| `[DATA_ENRICHMENT]` | Enrichment sources | "third-party data append", "geocoding", "firmographic enrichment" |
| `[ERROR_CORRECTION]` | Error correction approach | "automated fixes for known patterns", "ML-based suggestions", "manual correction queue" |
| `[TRANSFORMATION_RULES]` | Transformation logic | "100+ transformation rules", "lookup-based transforms", "calculation rules" |
| `[MONITORING_FRAMEWORK]` | DQ monitoring platform | "Monte Carlo", "Datafold", "Great Expectations + Airflow", "custom dashboards" |
| `[QUALITY_METRICS]` | Quality KPIs tracked | "accuracy %, completeness %, freshness, rule pass rate" |
| `[KPI_DEFINITIONS]` | KPI specifications | "DQ score = weighted average of dimensions", "defect rate = errors/total records" |
| `[THRESHOLD_SETTINGS]` | Alert thresholds | "critical <95%", "warning <98%", "target >99%", "SLA breach notification" |
| `[ALERT_CONFIGURATION]` | Alert routing | "PagerDuty for critical", "Slack for warnings", "email digest for info" |
| `[DASHBOARD_DESIGN]` | Dashboard layout | "Tableau DQ dashboard", "Grafana metrics", "custom React dashboard" |
| `[REPORTING_SCHEDULE]` | Report frequency | "real-time dashboards", "daily summary", "weekly executive report" |
| `[TREND_ANALYSIS]` | Trend tracking | "week-over-week DQ score", "monthly trend reports", "anomaly trend detection" |
| `[ROOT_CAUSE_ANALYSIS]` | RCA approach | "automated lineage-based RCA", "5 Whys process", "fishbone diagrams" |
| `[CONTINUOUS_MONITORING]` | Continuous monitoring | "24/7 pipeline monitoring", "real-time anomaly detection", "SLA tracking" |
| `[ASSESSMENT_METHODOLOGY]` | Assessment approach | "DMBOK-based assessment", "maturity model evaluation", "capability assessment" |
| `[SCORING_MODELS]` | Quality scoring | "weighted dimension scoring", "rule-based scoring", "ML quality prediction" |
| `[BENCHMARKING]` | Benchmark comparisons | "industry benchmarks", "historical baseline", "peer comparison" |
| `[QUALITY_SCORECARDS]` | Scorecard design | "executive scorecard", "domain scorecards", "source system scorecards" |
| `[MATURITY_ASSESSMENT]` | Maturity evaluation | "CMMI-based levels", "DCAM assessment", "custom maturity model" |
| `[GAP_ANALYSIS]` | Gap identification | "current vs. target state analysis", "capability gaps", "tool gaps" |
| `[RISK_ASSESSMENT]` | Risk evaluation | "data risk scoring", "impact assessment", "likelihood analysis" |
| `[IMPACT_ANALYSIS]` | Impact evaluation | "business impact of DQ issues", "downstream system impact", "revenue impact" |
| `[IMPROVEMENT_ROADMAP]` | Improvement planning | "90-day quick wins", "6-month strategic initiatives", "annual roadmap" |
| `[PRIORITY_MATRIX]` | Specify the priority matrix | "High" |
| `[ISSUE_CLASSIFICATION]` | Issue categorization | "critical/major/minor", "by data domain", "by root cause type" |
| `[ISSUE_TRACKING]` | Issue tracking system | "Jira DQ project", "ServiceNow", "custom issue tracker" |
| `[ESCALATION_PROCESS]` | Escalation procedures | "P1: immediate escalation", "P2: 4-hour escalation", "tiered support" |
| `[RESOLUTION_WORKFLOW]` | Resolution process | "triage → assign → fix → verify → close", "automated resolution for known issues" |
| `[PRIORITY_ASSIGNMENT]` | Specify the priority assignment | "High" |
| `[SLA_MANAGEMENT]` | SLA tracking and enforcement | "P1: 4-hour resolution", "P2: 24-hour resolution", "99.9% SLA compliance" |
| `[COMMUNICATION_PLAN]` | Stakeholder communication | "daily standup for active issues", "weekly status report", "incident notifications" |
| `[STATUS_REPORTING]` | Specify the status reporting | "In Progress" |
| `[CLOSURE_CRITERIA]` | Issue closure requirements | "root cause identified", "fix verified in production", "no recurrence for 7 days" |
| `[LESSONS_LEARNED]` | Knowledge capture | "post-incident reviews", "knowledge base updates", "process improvements documented" |
| `[GOVERNANCE_FRAMEWORK]` | Governance structure | "DAMA DMBOK framework", "custom governance model", "federated governance" |
| `[DATA_OWNERSHIP]` | Ownership model | "business domain owners", "RACI matrix", "data trustees" |
| `[DATA_STEWARDSHIP]` | Stewardship program | "dedicated data stewards", "part-time stewards per domain", "steward council" |
| `[QUALITY_POLICIES]` | Quality policy documents | "enterprise DQ policy", "domain-specific standards", "acceptable quality levels" |
| `[STANDARDS_DEFINITION]` | Standard specifications | "naming conventions", "data definitions", "quality thresholds" |
| `[ROLES_RESPONSIBILITIES]` | Role definitions | "data owner, data steward, data custodian", "RACI matrix", "accountability chart" |
| `[DECISION_FRAMEWORK]` | Decision-making process | "data governance council", "steering committee", "escalation matrix" |
| `[CHANGE_MANAGEMENT]` | Change control process | "schema change review", "rule change approval", "impact assessment" |
| `[COMPLIANCE_MONITORING]` | Compliance tracking | "automated compliance checks", "audit trail", "policy adherence reports" |
| `[AUDIT_PROCEDURES]` | Audit processes | "quarterly internal audits", "annual external audits", "continuous audit" |
| `[PREVENTIVE_CONTROLS]` | Prevention measures | "schema validation on ingest", "data contracts", "input validation" |
| `[DETECTIVE_CONTROLS]` | Detection mechanisms | "anomaly detection", "rule-based alerts", "sampling and review" |
| `[CORRECTIVE_CONTROLS]` | Correction procedures | "automated remediation", "manual correction workflow", "root cause elimination" |
| `[AUTOMATED_CONTROLS]` | Automation implementation | "CI/CD quality gates", "automated testing", "pipeline validations" |
| `[MANUAL_CONTROLS]` | Manual processes | "data steward review", "exception handling", "approval workflows" |
| `[CONTROL_TESTING]` | Control validation | "quarterly control testing", "effectiveness assessment", "gap identification" |
| `[CONTROL_MONITORING]` | Control oversight | "continuous control monitoring", "control dashboards", "exception tracking" |
| `[CONTROL_DOCUMENTATION]` | Control documentation | "control catalog", "procedure documentation", "evidence repository" |
| `[CONTROL_EFFECTIVENESS]` | Effectiveness measurement | "control success rate", "defect escape rate", "time to detect" |
| `[CONTROL_UPDATES]` | Specify the control updates | "2025-01-15" |
| `[LINEAGE_TRACKING]` | Lineage capture method | "automated lineage from dbt", "OpenLineage integration", "manual documentation" |
| `[SOURCE_IDENTIFICATION]` | Source system tracking | "source system tagging", "origin metadata", "authoritative source registry" |
| `[TRANSFORMATION_TRACKING]` | Transformation documentation | "dbt model lineage", "ETL job tracking", "transformation audit trail" |
| `[LINEAGE_IMPACT_ANALYSIS]` | Impact assessment approach | "upstream/downstream analysis", "change impact simulation" |
| `[DEPENDENCY_MAPPING]` | Dependency documentation | "data dependency graphs", "pipeline DAGs", "cross-system dependencies" |
| `[CHANGE_IMPACT]` | Change impact evaluation | "schema change impact", "rule change propagation", "downstream effects" |
| `[DATA_FLOW_DOCUMENTATION]` | Flow documentation | "data flow diagrams", "pipeline documentation", "integration maps" |
| `[LINEAGE_VISUALIZATION]` | Lineage display tools | "Atlan lineage view", "DataHub graph", "dbt docs lineage" |
| `[METADATA_MANAGEMENT]` | Metadata handling | "data catalog integration", "business glossary", "technical metadata" |
| `[LINEAGE_AUTOMATION]` | Automated lineage capture | "OpenLineage events", "SQL parsing", "API-based collection" |
| `[TEST_STRATEGY]` | Testing approach | "test pyramid for data", "shift-left testing", "continuous testing" |
| `[TEST_CASES]` | Test case design | "positive/negative tests", "edge cases", "business scenario tests" |
| `[TEST_DATA]` | Test data management | "synthetic test data", "masked production data", "fixture datasets" |
| `[TEST_AUTOMATION]` | Automated testing | "dbt tests in CI", "Great Expectations suites", "pytest fixtures" |
| `[REGRESSION_TESTING]` | Regression test approach | "baseline comparison", "historical data validation", "model output comparison" |
| `[QUALITY_PERFORMANCE_TESTING]` | Performance validation | "large dataset validation", "query performance", "pipeline throughput" |
| `[VOLUME_TESTING]` | Volume/scale testing | "10x data volume tests", "peak load simulation", "stress testing" |
| `[BOUNDARY_TESTING]` | Edge case testing | "min/max values", "null handling", "special characters" |
| `[QUALITY_INTEGRATION_TESTING]` | Integration validation | "end-to-end pipeline tests", "cross-system validation", "API contract testing" |
| `[USER_ACCEPTANCE_TESTING]` | UAT process | "business user validation", "sample data review", "sign-off workflow" |
| `[REMEDIATION_STRATEGY]` | Remediation approach | "automated fix + manual review", "quarantine and correct", "source fix priority" |
| `[ACTION_PLANS]` | Action planning | "prioritized fix backlog", "sprint-based remediation", "quick wins identification" |
| `[FIX_PROCEDURES]` | Fix implementation | "standardized fix procedures", "code review for fixes", "fix verification" |
| `[DATA_RECOVERY]` | Data recovery process | "point-in-time recovery", "backup restoration", "source re-extraction" |
| `[REPROCESSING]` | Reprocessing approach | "full reprocessing", "incremental reprocessing", "targeted correction" |
| `[MANUAL_CORRECTIONS]` | Manual fix process | "correction request workflow", "approval process", "audit trail" |
| `[AUTOMATED_FIXES]` | Automated remediation | "auto-fix for known patterns", "ML-suggested corrections", "rule-based fixes" |
| `[VALIDATION_POST_FIX]` | Post-fix validation | "re-run quality checks", "regression testing", "stakeholder verification" |
| `[REMEDIATION_IMPACT_ASSESSMENT]` | Fix impact analysis | "downstream impact check", "timing considerations", "rollback planning" |
| `[REMEDIATION_COMMUNICATION]` | Fix communication | "stakeholder notifications", "fix release notes", "impact communication" |
| `[QUALITY_TOOLS]` | Quality management tools | "Collibra DQ", "Informatica DQ", "Talend Data Quality", "Ataccama" |
| `[PROFILING_TOOLS_TECH]` | Profiling technology | "Great Expectations", "AWS Deequ", "Apache Griffin", "Pandas Profiling" |
| `[VALIDATION_TOOLS]` | Validation frameworks | "dbt tests", "Great Expectations", "Pandera", "Soda Core" |
| `[CLEANSING_TOOLS]` | Cleansing solutions | "Trifacta", "Talend Data Prep", "OpenRefine", "custom Python scripts" |
| `[MONITORING_TOOLS]` | Monitoring platforms | "Monte Carlo", "Datafold", "Bigeye", "custom Grafana dashboards" |
| `[REPORTING_TOOLS]` | Reporting solutions | "Tableau", "Power BI", "Looker", "custom React dashboards" |
| `[WORKFLOW_TOOLS]` | Workflow management | "Jira", "ServiceNow", "Asana", "custom workflow engine" |
| `[INTEGRATION_TOOLS]` | Integration platforms | "Airbyte", "Fivetran", "Apache NiFi", "custom ETL" |
| `[METADATA_TOOLS]` | Metadata management | "DataHub", "Atlan", "Alation", "AWS Glue Data Catalog" |
| `[AUTOMATION_TOOLS]` | Automation platforms | "Airflow", "Prefect", "Dagster", "dbt Cloud" |
| `[QUALITY_METRICS_DETAIL]` | Detailed quality metrics | "accuracy by field", "completeness by source", "timeliness by pipeline" |
| `[BUSINESS_KPIS]` | Business KPIs impacted | "customer satisfaction", "revenue accuracy", "regulatory compliance rate" |
| `[TECHNICAL_KPIS]` | Technical KPIs | "rule pass rate", "pipeline success rate", "detection latency" |
| `[PROCESS_KPIS]` | Process KPIs | "issue resolution time", "fix cycle time", "backlog age" |
| `[COST_METRICS]` | Cost tracking | "cost of poor data quality", "remediation costs", "tool costs" |
| `[EFFICIENCY_METRICS]` | Efficiency tracking | "automation rate", "manual effort reduction", "time savings" |
| `[USER_SATISFACTION]` | User satisfaction measurement | "NPS for data quality", "user surveys", "support ticket analysis" |
| `[COMPLIANCE_METRICS]` | Compliance tracking | "audit findings", "policy adherence rate", "regulatory compliance score" |
| `[TREND_METRICS]` | Trend tracking | "DQ score over time", "defect rate trends", "improvement velocity" |
| `[COMPARATIVE_METRICS]` | Benchmarking metrics | "vs. industry standards", "vs. historical baseline", "cross-domain comparison" |
| `[TRAINING_STRATEGY]` | Training approach | "role-based curriculum", "self-paced learning", "hands-on workshops" |
| `[ROLE_BASED_TRAINING]` | Role-specific training | "steward training", "analyst training", "engineer training" |
| `[TOOL_TRAINING]` | Tool-specific training | "Great Expectations certification", "dbt training", "catalog tool training" |
| `[PROCESS_TRAINING]` | Process training | "DQ workflow training", "issue management training", "governance training" |
| `[AWARENESS_PROGRAMS]` | Awareness initiatives | "data quality week", "lunch and learns", "newsletter updates" |
| `[CERTIFICATION_PROGRAMS]` | Certification paths | "CDMP certification", "internal DQ certification", "tool certifications" |
| `[KNOWLEDGE_MANAGEMENT]` | Knowledge base | "Confluence knowledge base", "FAQ documentation", "video tutorials" |
| `[BEST_PRACTICES_SHARING]` | Best practice sharing | "community of practice", "case study sharing", "pattern library" |
| `[ADOPTION_CHANGE_MANAGEMENT]` | Change management | "stakeholder engagement", "pilot programs", "phased rollout" |
| `[USER_SUPPORT]` | Support model | "Slack support channel", "office hours", "ticketing system" |
| `[COST_CATEGORIES]` | Cost classification | "tooling costs", "personnel costs", "infrastructure costs", "training costs" |
| `[IMPLEMENTATION_COSTS]` | Implementation budget | "tool licensing", "consulting fees", "development effort" |
| `[OPERATIONAL_COSTS]` | Ongoing costs | "annual tool maintenance", "support costs", "cloud infrastructure" |
| `[RESOURCE_COSTS]` | Personnel costs | "FTE allocation", "contractor costs", "training investment" |
| `[TECHNOLOGY_COSTS]` | Technology expenses | "SaaS subscriptions", "infrastructure costs", "integration costs" |
| `[BENEFIT_CATEGORIES]` | Benefit types | "efficiency gains", "risk reduction", "revenue protection", "compliance" |
| `[REVENUE_BENEFITS]` | Revenue impact | "reduced customer churn", "improved conversion", "pricing accuracy" |
| `[COST_SAVINGS]` | Cost reduction | "reduced manual effort", "fewer errors", "regulatory fine avoidance" |
| `[RISK_REDUCTION]` | Risk mitigation | "regulatory risk reduction", "reputational risk mitigation", "operational risk" |
| `[ROI_CALCULATION]` | ROI methodology | "3-year NPV", "payback period", "cost-benefit ratio" |

### Financial Data Quality
```
Implement comprehensive data quality framework for Trading Data covering market data, reference data, transaction data to achieve 99.99% accuracy, 100% completeness objectives for Risk, Trading, Compliance stakeholders. Meet Basel III, BCBS 239 quality standards and ensure SOX, MiFID II compliance within $1M budget and 12-month timeline.

Quality Dimensions:
- Ensure 99.99% accuracy and 100% completeness
- Maintain trade lifecycle consistency across front, middle, back office systems and regulatory validity per trade validation rules
- Achieve 100% uniqueness without trade duplicates and T+0 timeliness for real-time risk
- Verify settlement integrity, regulatory conformity, pricing precision, and market data reliability

Cleansing Strategy:
- Apply ISDA standardization and trade normalization rules
- Implement fuzzy matching deduplication and interpolation missing value treatment
- Handle statistical outlier treatment and ISO format correction
- Perform market data enrichment and automated error correction
- Execute 100+ transformation rules automatically

### Governance Framework
- Establish Business Owner data ownership and dedicated data stewardship
- Define SOX-compliant quality policies and Basel III standards definition
- Assign front office, risk, operations roles responsibilities and risk committee decision framework
- Implement SDLC change management and daily compliance monitoring
- Set up quarterly external audit procedures for regulatory oversight
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Data Quality Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Data Engineering](../../technology/Data Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating implement comprehensive data quality frameworks including validation, cleansing, monitoring, profiling, and governance to ensure high-quality, reliable, and trustworthy data across enterprise systems.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Start with business impact and user requirements**
2. **Define clear quality dimensions and measurable metrics**
3. **Implement automated validation and monitoring**
4. **Establish strong data governance and stewardship**
5. **Focus on root cause analysis, not just symptoms**
6. **Build quality into data pipelines from the beginning**
7. **Provide clear, actionable quality reports**
8. **Train users on quality standards and tools**
9. **Continuously improve based on metrics and feedback**
10. **Balance automation with human oversight and judgment**