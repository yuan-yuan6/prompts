---
title: Data Quality Template
category: technology/Data Engineering
tags: [data-science, design, research, security, strategy, technology, template, testing]
use_cases:
  - Creating implement comprehensive data quality frameworks including validation, cleansing, monitoring, profiling, and governance to ensure high-quality, reliable, and trustworthy data across enterprise systems.

  - Project planning and execution
  - Strategy development
related_templates:
  - cloud-architecture-framework.md
  - site-reliability-engineering.md
  - cloud-migration-strategy.md
last_updated: 2025-11-09
---

# Data Quality Template

## Purpose
Implement comprehensive data quality frameworks including validation, cleansing, monitoring, profiling, and governance to ensure high-quality, reliable, and trustworthy data across enterprise systems.

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
| `[DATA_DOMAIN]` | Specify the data domain | "[specify value]" |
| `[QUALITY_SCOPE]` | Specify the quality scope | "[specify value]" |
| `[BUSINESS_CONTEXT]` | Specify the business context | "[specify value]" |
| `[STAKEHOLDERS]` | Specify the stakeholders | "[specify value]" |
| `[QUALITY_OBJECTIVES]` | Specify the quality objectives | "Increase efficiency by 30%" |
| `[SUCCESS_METRICS]` | Specify the success metrics | "[specify value]" |
| `[QUALITY_STANDARDS]` | Specify the quality standards | "[specify value]" |
| `[COMPLIANCE_REQUIREMENTS]` | Specify the compliance requirements | "[specify value]" |
| `[QUALITY_BUDGET]` | Specify the quality budget | "$500,000" |
| `[QUALITY_TIMELINE]` | Specify the quality timeline | "6 months" |
| `[ACCURACY]` | Specify the accuracy | "[specify value]" |
| `[COMPLETENESS]` | Specify the completeness | "[specify value]" |
| `[CONSISTENCY]` | Specify the consistency | "[specify value]" |
| `[VALIDITY]` | Specify the validity | "[specify value]" |
| `[UNIQUENESS]` | Specify the uniqueness | "[specify value]" |
| `[TIMELINESS]` | Specify the timeliness | "6 months" |
| `[INTEGRITY]` | Specify the integrity | "[specify value]" |
| `[CONFORMITY]` | Specify the conformity | "[specify value]" |
| `[PRECISION]` | Specify the precision | "[specify value]" |
| `[RELIABILITY]` | Specify the reliability | "[specify value]" |
| `[PROFILING_STRATEGY]` | Specify the profiling strategy | "[specify value]" |
| `[PROFILING_TOOLS]` | Specify the profiling tools | "[specify value]" |
| `[PROFILING_SCOPE]` | Specify the profiling scope | "[specify value]" |
| `[STATISTICAL_ANALYSIS]` | Specify the statistical analysis | "[specify value]" |
| `[PATTERN_ANALYSIS]` | Specify the pattern analysis | "[specify value]" |
| `[DISTRIBUTION_ANALYSIS]` | Specify the distribution analysis | "[specify value]" |
| `[RELATIONSHIP_ANALYSIS]` | Specify the relationship analysis | "[specify value]" |
| `[ANOMALY_DETECTION]` | Specify the anomaly detection | "[specify value]" |
| `[METADATA_DISCOVERY]` | Specify the metadata discovery | "[specify value]" |
| `[PROFILING_SCHEDULE]` | Specify the profiling schedule | "[specify value]" |
| `[VALIDATION_RULES]` | Specify the validation rules | "[specify value]" |
| `[BUSINESS_RULES]` | Specify the business rules | "[specify value]" |
| `[DATA_TYPE_VALIDATION]` | Specify the data type validation | "Standard" |
| `[FORMAT_VALIDATION]` | Specify the format validation | "[specify value]" |
| `[RANGE_VALIDATION]` | Specify the range validation | "[specify value]" |
| `[LIST_VALIDATION]` | Specify the list validation | "[specify value]" |
| `[CROSS_FIELD_VALIDATION]` | Specify the cross field validation | "[specify value]" |
| `[REFERENTIAL_INTEGRITY]` | Specify the referential integrity | "[specify value]" |
| `[CUSTOM_VALIDATIONS]` | Specify the custom validations | "[specify value]" |
| `[VALIDATION_FRAMEWORK]` | Specify the validation framework | "[specify value]" |
| `[CLEANSING_STRATEGY]` | Specify the cleansing strategy | "[specify value]" |
| `[STANDARDIZATION]` | Specify the standardization | "[specify value]" |
| `[NORMALIZATION]` | Specify the normalization | "[specify value]" |
| `[DEDUPLICATION]` | Specify the deduplication | "[specify value]" |
| `[MISSING_VALUE_TREATMENT]` | Specify the missing value treatment | "[specify value]" |
| `[OUTLIER_TREATMENT]` | Specify the outlier treatment | "[specify value]" |
| `[FORMAT_CORRECTION]` | Specify the format correction | "[specify value]" |
| `[DATA_ENRICHMENT]` | Specify the data enrichment | "[specify value]" |
| `[ERROR_CORRECTION]` | Specify the error correction | "[specify value]" |
| `[TRANSFORMATION_RULES]` | Specify the transformation rules | "[specify value]" |
| `[MONITORING_FRAMEWORK]` | Specify the monitoring framework | "[specify value]" |
| `[QUALITY_METRICS]` | Specify the quality metrics | "[specify value]" |
| `[KPI_DEFINITIONS]` | Specify the kpi definitions | "[specify value]" |
| `[THRESHOLD_SETTINGS]` | Specify the threshold settings | "[specify value]" |
| `[ALERT_CONFIGURATION]` | Specify the alert configuration | "[specify value]" |
| `[DASHBOARD_DESIGN]` | Specify the dashboard design | "[specify value]" |
| `[REPORTING_SCHEDULE]` | Specify the reporting schedule | "[specify value]" |
| `[TREND_ANALYSIS]` | Specify the trend analysis | "[specify value]" |
| `[ROOT_CAUSE_ANALYSIS]` | Specify the root cause analysis | "[specify value]" |
| `[CONTINUOUS_MONITORING]` | Specify the continuous monitoring | "[specify value]" |
| `[ASSESSMENT_METHODOLOGY]` | Specify the assessment methodology | "[specify value]" |
| `[SCORING_MODELS]` | Specify the scoring models | "[specify value]" |
| `[BENCHMARKING]` | Specify the benchmarking | "[specify value]" |
| `[QUALITY_SCORECARDS]` | Specify the quality scorecards | "[specify value]" |
| `[MATURITY_ASSESSMENT]` | Specify the maturity assessment | "[specify value]" |
| `[GAP_ANALYSIS]` | Specify the gap analysis | "[specify value]" |
| `[RISK_ASSESSMENT]` | Specify the risk assessment | "[specify value]" |
| `[IMPACT_ANALYSIS]` | Specify the impact analysis | "[specify value]" |
| `[IMPROVEMENT_ROADMAP]` | Specify the improvement roadmap | "[specify value]" |
| `[PRIORITY_MATRIX]` | Specify the priority matrix | "High" |
| `[ISSUE_CLASSIFICATION]` | Specify the issue classification | "[specify value]" |
| `[ISSUE_TRACKING]` | Specify the issue tracking | "[specify value]" |
| `[ESCALATION_PROCESS]` | Specify the escalation process | "[specify value]" |
| `[RESOLUTION_WORKFLOW]` | Specify the resolution workflow | "[specify value]" |
| `[PRIORITY_ASSIGNMENT]` | Specify the priority assignment | "High" |
| `[SLA_MANAGEMENT]` | Specify the sla management | "[specify value]" |
| `[COMMUNICATION_PLAN]` | Specify the communication plan | "[specify value]" |
| `[STATUS_REPORTING]` | Specify the status reporting | "In Progress" |
| `[CLOSURE_CRITERIA]` | Specify the closure criteria | "[specify value]" |
| `[LESSONS_LEARNED]` | Specify the lessons learned | "[specify value]" |
| `[GOVERNANCE_FRAMEWORK]` | Specify the governance framework | "[specify value]" |
| `[DATA_OWNERSHIP]` | Specify the data ownership | "[specify value]" |
| `[DATA_STEWARDSHIP]` | Specify the data stewardship | "[specify value]" |
| `[QUALITY_POLICIES]` | Specify the quality policies | "[specify value]" |
| `[STANDARDS_DEFINITION]` | Specify the standards definition | "[specify value]" |
| `[ROLES_RESPONSIBILITIES]` | Specify the roles responsibilities | "[specify value]" |
| `[DECISION_FRAMEWORK]` | Specify the decision framework | "[specify value]" |
| `[CHANGE_MANAGEMENT]` | Specify the change management | "[specify value]" |
| `[COMPLIANCE_MONITORING]` | Specify the compliance monitoring | "[specify value]" |
| `[AUDIT_PROCEDURES]` | Specify the audit procedures | "[specify value]" |
| `[PREVENTIVE_CONTROLS]` | Specify the preventive controls | "[specify value]" |
| `[DETECTIVE_CONTROLS]` | Specify the detective controls | "[specify value]" |
| `[CORRECTIVE_CONTROLS]` | Specify the corrective controls | "[specify value]" |
| `[AUTOMATED_CONTROLS]` | Specify the automated controls | "[specify value]" |
| `[MANUAL_CONTROLS]` | Specify the manual controls | "[specify value]" |
| `[CONTROL_TESTING]` | Specify the control testing | "[specify value]" |
| `[CONTROL_MONITORING]` | Specify the control monitoring | "[specify value]" |
| `[CONTROL_DOCUMENTATION]` | Specify the control documentation | "[specify value]" |
| `[CONTROL_EFFECTIVENESS]` | Specify the control effectiveness | "[specify value]" |
| `[CONTROL_UPDATES]` | Specify the control updates | "2025-01-15" |
| `[LINEAGE_TRACKING]` | Specify the lineage tracking | "[specify value]" |
| `[SOURCE_IDENTIFICATION]` | Specify the source identification | "[specify value]" |
| `[TRANSFORMATION_TRACKING]` | Specify the transformation tracking | "[specify value]" |
| `[LINEAGE_IMPACT_ANALYSIS]` | Specify the lineage impact analysis | "[specify value]" |
| `[DEPENDENCY_MAPPING]` | Specify the dependency mapping | "[specify value]" |
| `[CHANGE_IMPACT]` | Specify the change impact | "[specify value]" |
| `[DATA_FLOW_DOCUMENTATION]` | Specify the data flow documentation | "[specify value]" |
| `[LINEAGE_VISUALIZATION]` | Specify the lineage visualization | "[specify value]" |
| `[METADATA_MANAGEMENT]` | Specify the metadata management | "[specify value]" |
| `[LINEAGE_AUTOMATION]` | Specify the lineage automation | "[specify value]" |
| `[TEST_STRATEGY]` | Specify the test strategy | "[specify value]" |
| `[TEST_CASES]` | Specify the test cases | "[specify value]" |
| `[TEST_DATA]` | Specify the test data | "[specify value]" |
| `[TEST_AUTOMATION]` | Specify the test automation | "[specify value]" |
| `[REGRESSION_TESTING]` | Specify the regression testing | "[specify value]" |
| `[QUALITY_PERFORMANCE_TESTING]` | Specify the quality performance testing | "[specify value]" |
| `[VOLUME_TESTING]` | Specify the volume testing | "[specify value]" |
| `[BOUNDARY_TESTING]` | Specify the boundary testing | "[specify value]" |
| `[QUALITY_INTEGRATION_TESTING]` | Specify the quality integration testing | "[specify value]" |
| `[USER_ACCEPTANCE_TESTING]` | Specify the user acceptance testing | "[specify value]" |
| `[REMEDIATION_STRATEGY]` | Specify the remediation strategy | "[specify value]" |
| `[ACTION_PLANS]` | Specify the action plans | "[specify value]" |
| `[FIX_PROCEDURES]` | Specify the fix procedures | "[specify value]" |
| `[DATA_RECOVERY]` | Specify the data recovery | "[specify value]" |
| `[REPROCESSING]` | Specify the reprocessing | "[specify value]" |
| `[MANUAL_CORRECTIONS]` | Specify the manual corrections | "[specify value]" |
| `[AUTOMATED_FIXES]` | Specify the automated fixes | "[specify value]" |
| `[VALIDATION_POST_FIX]` | Specify the validation post fix | "[specify value]" |
| `[REMEDIATION_IMPACT_ASSESSMENT]` | Specify the remediation impact assessment | "[specify value]" |
| `[REMEDIATION_COMMUNICATION]` | Specify the remediation communication | "[specify value]" |
| `[QUALITY_TOOLS]` | Specify the quality tools | "[specify value]" |
| `[PROFILING_TOOLS_TECH]` | Specify the profiling tools tech | "[specify value]" |
| `[VALIDATION_TOOLS]` | Specify the validation tools | "[specify value]" |
| `[CLEANSING_TOOLS]` | Specify the cleansing tools | "[specify value]" |
| `[MONITORING_TOOLS]` | Specify the monitoring tools | "[specify value]" |
| `[REPORTING_TOOLS]` | Specify the reporting tools | "[specify value]" |
| `[WORKFLOW_TOOLS]` | Specify the workflow tools | "[specify value]" |
| `[INTEGRATION_TOOLS]` | Specify the integration tools | "[specify value]" |
| `[METADATA_TOOLS]` | Specify the metadata tools | "[specify value]" |
| `[AUTOMATION_TOOLS]` | Specify the automation tools | "[specify value]" |
| `[QUALITY_METRICS_DETAIL]` | Specify the quality metrics detail | "[specify value]" |
| `[BUSINESS_KPIS]` | Specify the business kpis | "[specify value]" |
| `[TECHNICAL_KPIS]` | Specify the technical kpis | "[specify value]" |
| `[PROCESS_KPIS]` | Specify the process kpis | "[specify value]" |
| `[COST_METRICS]` | Specify the cost metrics | "[specify value]" |
| `[EFFICIENCY_METRICS]` | Specify the efficiency metrics | "[specify value]" |
| `[USER_SATISFACTION]` | Specify the user satisfaction | "[specify value]" |
| `[COMPLIANCE_METRICS]` | Specify the compliance metrics | "[specify value]" |
| `[TREND_METRICS]` | Specify the trend metrics | "[specify value]" |
| `[COMPARATIVE_METRICS]` | Specify the comparative metrics | "[specify value]" |
| `[TRAINING_STRATEGY]` | Specify the training strategy | "[specify value]" |
| `[ROLE_BASED_TRAINING]` | Specify the role based training | "[specify value]" |
| `[TOOL_TRAINING]` | Specify the tool training | "[specify value]" |
| `[PROCESS_TRAINING]` | Specify the process training | "[specify value]" |
| `[AWARENESS_PROGRAMS]` | Specify the awareness programs | "[specify value]" |
| `[CERTIFICATION_PROGRAMS]` | Specify the certification programs | "[specify value]" |
| `[KNOWLEDGE_MANAGEMENT]` | Specify the knowledge management | "[specify value]" |
| `[BEST_PRACTICES_SHARING]` | Specify the best practices sharing | "[specify value]" |
| `[ADOPTION_CHANGE_MANAGEMENT]` | Specify the adoption change management | "[specify value]" |
| `[USER_SUPPORT]` | Specify the user support | "[specify value]" |
| `[COST_CATEGORIES]` | Specify the cost categories | "[specify value]" |
| `[IMPLEMENTATION_COSTS]` | Specify the implementation costs | "[specify value]" |
| `[OPERATIONAL_COSTS]` | Specify the operational costs | "[specify value]" |
| `[RESOURCE_COSTS]` | Specify the resource costs | "[specify value]" |
| `[TECHNOLOGY_COSTS]` | Specify the technology costs | "[specify value]" |
| `[BENEFIT_CATEGORIES]` | Specify the benefit categories | "[specify value]" |
| `[REVENUE_BENEFITS]` | Specify the revenue benefits | "[specify value]" |
| `[COST_SAVINGS]` | Specify the cost savings | "[specify value]" |
| `[RISK_REDUCTION]` | Specify the risk reduction | "[specify value]" |
| `[ROI_CALCULATION]` | Specify the roi calculation | "[specify value]" |



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