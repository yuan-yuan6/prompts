---
category: data-analytics/Business-Intelligence
last_updated: 2025-11-09
related_templates:
- data-analytics/Business-Intelligence/dashboard-strategy-requirements.md
- data-analytics/Business-Intelligence/dashboard-technical-implementation.md
- data-analytics/Business-Intelligence/dashboard-design-overview.md
tags:
- data-analytics
title: Dashboard Data Architecture & Integration
use_cases:
- Design data pipeline for dashboard with multiple source systems
- Build ETL workflow for nightly dashboard refresh from operational databases
- Create data model that supports both summary and drill-down reporting needs
industries:
- finance
- healthcare
- manufacturing
- technology
---

# Dashboard Data Architecture & Integration

## Overview
Design robust data architecture and integration pipelines to power dashboard analytics. This prompt guides data source integration, ETL/ELT design, and data modeling for optimal performance and reliability.

---

## Purpose
Use this prompt to:
- Design data integration architecture
- Develop ETL/ELT pipelines
- Model data warehouses for analytics
- Ensure data quality and governance

---

## Quick Start

**Data Pipeline Setup (1 Day):**
1. **Map source systems to KPIs** - List data sources (Salesforce, NetSuite, databases), identify tables/fields needed for each KPI
2. **Choose extraction method** - Use incremental loads for large tables (WHERE modified_date > last_run), full refresh for small reference data
3. **Design star schema** - Create fact table (transactions grain), dimension tables (customer, product, date), implement Type 2 SCD for history
4. **Build initial ETL pipeline** - Extract from sources, transform (clean, validate, aggregate), load to data warehouse on schedule
5. **Implement data quality checks** - Validate completeness (no nulls in key fields), accuracy (totals match sources), timeliness (data <2 hours old)

**Key Decision:** For data freshness needs: Real-time (<5 min) → CDC/streaming, Hourly → incremental batch, Daily → overnight batch processing.

---

## Prompt

I need to design a comprehensive data architecture for a dashboard solution with the following requirements:

### Data Source Landscape
**Primary Data Sources:**
- ERP system: [ERP_SYSTEM] (SAP/Oracle/NetSuite/Other/None)
- CRM system: [CRM_SYSTEM] (Salesforce/HubSpot/Dynamics/Other/None)
- Database systems: [DATABASES] (SQL Server/PostgreSQL/MySQL/Oracle/Other)
- Cloud platforms: [CLOUD_PLATFORMS] (AWS/Azure/GCP/Multi-cloud/None)
- File sources: [FILE_SOURCES] (CSV/Excel/JSON/XML/Other)
- APIs: [API_SOURCES]
- Other systems: [OTHER_SOURCES]

**Data Volume & Velocity:**
- Total data volume: [DATA_VOLUME] (GB/TB/PB)
- Daily data growth: [DAILY_GROWTH]
- Update frequency: [UPDATE_FREQUENCY] (Real-time/Hourly/Daily/Weekly)
- Historical data retention: [RETENTION_PERIOD]
- Peak load characteristics: [PEAK_LOAD]

### Integration Requirements
**Data Extraction:**
- Extraction method: [EXTRACTION_METHOD] (Full/Incremental/CDC/Streaming)
- Source system constraints: [SOURCE_CONSTRAINTS]
- Extraction schedule: [EXTRACTION_SCHEDULE]
- Data latency tolerance: [LATENCY_TOLERANCE]

**Data Transformation:**
- Cleansing requirements: [CLEANSING_NEEDS]
- Validation rules: [VALIDATION_RULES]
- Business logic: [BUSINESS_LOGIC]
- Enrichment needs: [ENRICHMENT_NEEDS]
- Aggregation requirements: [AGGREGATION_NEEDS]

**Data Loading:**
- Loading strategy: [LOADING_STRATEGY] (Batch/Real-time/Micro-batch/Hybrid)
- Target platform: [TARGET_PLATFORM] (Data warehouse/Data lake/Both)
- Loading schedule: [LOADING_SCHEDULE]
- Error handling approach: [ERROR_HANDLING]

### Data Warehouse Design
**Modeling Approach:**
- Data model type: [MODEL_TYPE] (Star schema/Snowflake/Data vault/OBT)
- Grain definition: [GRAIN_LEVEL]
- Fact tables: [FACT_TABLES]
- Dimension tables: [DIMENSION_TABLES]
- Slowly changing dimensions: [SCD_STRATEGY] (Type 1/Type 2/Type 3/Hybrid)

**Storage & Performance:**
- Storage platform: [STORAGE_PLATFORM] (Snowflake/Redshift/BigQuery/Synapse/Other)
- Partitioning strategy: [PARTITIONING_STRATEGY]
- Indexing approach: [INDEXING_STRATEGY]
- Compression: [COMPRESSION_METHOD]
- Expected query performance: [PERFORMANCE_TARGET]

### Data Quality & Governance
**Quality Framework:**
- Completeness checks: [COMPLETENESS_CHECKS]
- Accuracy validation: [ACCURACY_VALIDATION]
- Consistency rules: [CONSISTENCY_RULES]
- Timeliness monitoring: [TIMELINESS_MONITORING]
- Quality thresholds: [QUALITY_THRESHOLDS]

**Governance Requirements:**
- Data ownership: [DATA_OWNERSHIP]
- Metadata management: [METADATA_REQUIREMENTS]
- Data lineage tracking: [LINEAGE_TRACKING]
- Data catalog: [CATALOG_NEEDS]
- Compliance requirements: [COMPLIANCE_REQUIREMENTS] (GDPR/HIPAA/SOX/Other)

### Pipeline Architecture
**Orchestration:**
- Orchestration tool: [ORCHESTRATION_TOOL] (Airflow/Azure Data Factory/AWS Glue/Other)
- Scheduling requirements: [SCHEDULING_NEEDS]
- Dependency management: [DEPENDENCY_MANAGEMENT]
- Retry logic: [RETRY_LOGIC]
- Alerting requirements: [ALERTING_NEEDS]

**Scalability & Reliability:**
- Concurrent pipeline runs: [CONCURRENT_RUNS]
- Failover requirements: [FAILOVER_NEEDS]
- Disaster recovery: [DR_REQUIREMENTS]
- Monitoring approach: [MONITORING_APPROACH]

---

## Deliverables

Please provide:

1. **Data Architecture Design**
   - High-level architecture diagram
   - Data flow diagrams (source to dashboard)
   - Integration patterns and approaches
   - Technology stack recommendations

2. **ETL/ELT Pipeline Specifications**
   - Detailed pipeline design for each data source
   - Extraction logic and schedules
   - Transformation rules and business logic
   - Loading strategies and error handling
   - Performance optimization techniques

3. **Data Model Design**
   - Logical data model (ERD)
   - Physical data model with tables and columns
   - Fact and dimension table definitions
   - Slowly changing dimension strategy
   - Indexing and partitioning recommendations

4. **Data Quality Framework**
   - Data quality rules and validations
   - Quality monitoring dashboard design
   - Exception handling procedures
   - Data reconciliation approach
   - Quality metrics and SLAs

5. **Implementation Roadmap**
   - Phased implementation plan
   - Source system prioritization
   - Testing strategy
   - Migration approach (if applicable)
   - Risk mitigation plan

---

## Example Usage

### Example: Multi-Source Sales Analytics

```
ERP system: NetSuite
CRM system: Salesforce
Database systems: PostgreSQL (product catalog), MySQL (customer data)
Cloud platforms: AWS
File sources: Monthly Excel reports from finance
APIs: Stripe (payments), Google Analytics (web traffic)
Other systems: Zendesk (support tickets)

Total data volume: 500 GB
Daily data growth: 2 GB
Update frequency: Sales data hourly, other data daily
Historical data retention: 5 years online, 7 years archive
Peak load characteristics: End of month/quarter processing

Extraction method: Incremental for transactional data, full for reference data
Source system constraints: Salesforce API rate limits, NetSuite batch windows
Extraction schedule: Salesforce every hour, NetSuite nightly at 2 AM
Data latency tolerance: Sales data 1 hour, finance data next-day

Cleansing requirements: Standardize customer names, deduplicate records
Validation rules: Revenue must be non-negative, dates within valid ranges
Business logic: Calculate deal stage duration, categorize products
Enrichment needs: Add geographic data from zip codes, industry classifications
Aggregation requirements: Daily/monthly/quarterly sales summaries

Loading strategy: Micro-batch for sales, batch for reference data
Target platform: Snowflake data warehouse
Loading schedule: Continuous for sales, nightly for others
Error handling approach: Quarantine bad records, alert on quality issues

Data model type: Star schema
Grain level: Individual sales transaction
Fact tables: Sales, Support tickets, Web sessions
Dimension tables: Customer, Product, Time, Geography, Sales rep
SCD strategy: Type 2 for customer and product dimensions

Storage platform: Snowflake
Partitioning strategy: Partition by month on transaction date
Indexing strategy: Cluster on customer_id and date
Compression: Snowflake automatic compression
Expected query performance: Dashboard loads in <3 seconds

Completeness checks: All required fields present, no null values in key fields
Accuracy validation: Cross-reference totals with source systems
Consistency rules: Customer exists in dimension before fact load
Timeliness monitoring: Alert if data is >2 hours old
Quality thresholds: 99.9% completeness, 99.5% accuracy

Data ownership: Finance owns revenue data, Sales owns CRM data
Metadata requirements: Track source system, load timestamp, transformation applied
Lineage tracking: Full lineage from source to dashboard
Data catalog: Automated catalog with business glossary
Compliance requirements: GDPR for EU customers, SOX for financial data

Orchestration tool: Apache Airflow
Scheduling needs: Hourly, daily, and monthly pipelines
Dependency management: Finance loads after sales, aggregations after base tables
Retry logic: 3 retries with exponential backoff
Alerting requirements: Slack alerts for failures, email for quality issues

Concurrent pipeline runs: Up to 10
Failover requirements: Multi-AZ deployment
Disaster recovery: 4-hour RPO, 8-hour RTO
Monitoring approach: CloudWatch metrics, custom quality dashboard
```

---



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Dashboard Strategy Requirements](dashboard-strategy-requirements.md)** - Strategic planning and execution frameworks
- **[Dashboard Technical Implementation](dashboard-technical-implementation.md)** - Complementary approaches and methodologies
- **[Dashboard Design Overview](dashboard-design-overview.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Dashboard Data Architecture & Integration)
2. Use [Dashboard Strategy Requirements](dashboard-strategy-requirements.md) for deeper analysis
3. Apply [Dashboard Technical Implementation](dashboard-technical-implementation.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Business Intelligence](../../data-analytics/Business Intelligence/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Design data pipeline for dashboard with multiple source systems**: Combine this template with related analytics and strategy frameworks
- **Build ETL workflow for nightly dashboard refresh from operational databases**: Combine this template with related analytics and strategy frameworks
- **Create data model that supports both summary and drill-down reporting needs**: Combine this template with related analytics and strategy frameworks

## Best Practices

**Top 5 Critical Practices:**
1. **Pre-aggregate for speed, not storage** - A 50MB aggregate table beats a 5GB raw query every time
2. **Build once, use everywhere** - One clean customer table beats 5 teams calculating "active customers" differently
3. **Schedule based on business needs, not technology** - "Ready by 9am" matters more than "runs at 2am"
4. **Alert on data quality, not just failures** - 90% drop in records is worse than a complete failure
5. **Document transformations in code, not wikis** - Comments in SQL > external docs that go stale

### Data Integration
1. **Start with high-value sources** - Prioritize data sources that deliver the most business value
2. **Implement incremental loading** - Avoid full refreshes where possible
3. **Design for idempotency** - Ensure pipelines can safely re-run
4. **Use CDC when available** - Change data capture is more efficient than batch
5. **Plan for API rate limits** - Implement throttling and queuing

### Data Modeling
6. **Choose appropriate grain** - Balance detail with performance
7. **Use star schema for simplicity** - Easier for BI tools and users to understand
8. **Implement Type 2 SCD for critical dimensions** - Preserve history where needed
9. **Denormalize for performance** - Pre-aggregate common queries
10. **Create date dimension** - Include fiscal periods, holidays, business days

### Data Quality
11. **Validate at ingestion** - Catch issues early
12. **Monitor data freshness** - Alert when data is stale
13. **Track lineage** - Understand data flow from source to report
14. **Reconcile with sources** - Regularly verify totals match
15. **Document quality issues** - Build knowledge base of known issues

### Performance Optimization
16. **Partition large tables** - By date for time-series data
17. **Use appropriate indexes** - Based on query patterns
18. **Implement caching** - For frequently accessed aggregations
19. **Optimize transformation logic** - Push down to database where possible
20. **Monitor query performance** - Identify and optimize slow queries

---

## Data Quality Framework

### Quality Dimensions

| Dimension | Check Type | Example Rule | Action on Failure |
|-----------|------------|--------------|-------------------|
| Completeness | Required fields | Order must have customer_id | Quarantine record |
| Accuracy | Range validation | Revenue between $0 and $1M | Flag for review |
| Consistency | Cross-reference | Customer exists in dimension | Reject transaction |
| Timeliness | Freshness check | Data < 2 hours old | Alert operations |
| Uniqueness | Duplicate detection | One record per order_id | Keep latest |
| Validity | Format validation | Email matches pattern | Cleanse or reject |

### Quality Metrics

- **Completeness Rate**: (Records with all required fields / Total records) × 100
- **Accuracy Rate**: (Records passing validation / Total records) × 100
- **Timeliness**: Time between source update and availability in dashboard
- **Consistency Rate**: (Reconciled records / Total records) × 100

---

## Common Pitfalls to Avoid

- Attempting full loads for large tables (use incremental)
- Ignoring source system capacity constraints
- Poor error handling (data loss or duplicate processing)
- Missing data quality validations
- Insufficient monitoring and alerting
- Lack of data lineage tracking
- Over-normalization (poor query performance)
- Under-partitioning large tables
- No disaster recovery plan
- Inadequate documentation

---

## Technology Selection Guide

### Data Warehouse Platforms

| Platform | Best For | Strengths | Considerations |
|----------|----------|-----------|----------------|
| Snowflake | Cloud-native, scalability | Separation of compute/storage, easy scaling | Cost can grow with usage |
| Redshift | AWS ecosystem | Tight AWS integration, mature | More hands-on management |
| BigQuery | Google Cloud, large scale | Serverless, pay-per-query | Query cost optimization needed |
| Synapse | Azure ecosystem | Unified analytics platform | Complexity for simple use cases |

### ETL/ELT Tools

| Tool | Best For | Strengths | Considerations |
|------|----------|-----------|----------------|
| Airflow | Complex workflows | Flexibility, Python-based | Requires coding skills |
| Azure Data Factory | Azure-centric | Visual interface, managed service | Limited to Azure ecosystem |
| AWS Glue | AWS-centric | Serverless, auto-scaling | Learning curve |
| dbt | SQL transformations | Version control, testing | Requires separate orchestration |

---

## Variables Quick Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `[ERP_SYSTEM]` | ERP platform | "NetSuite" |
| `[CRM_SYSTEM]` | CRM platform | "Salesforce" |
| `[DATA_VOLUME]` | Total data size | "500 GB" |
| `[UPDATE_FREQUENCY]` | Refresh cadence | "Hourly for sales, daily for others" |
| `[EXTRACTION_METHOD]` | Extract approach | "Incremental via CDC" |
| `[MODEL_TYPE]` | Data model | "Star schema" |
| `[STORAGE_PLATFORM]` | Warehouse | "Snowflake" |
| `[ORCHESTRATION_TOOL]` | Pipeline tool | "Apache Airflow" |
| `[QUALITY_THRESHOLDS]` | Acceptable quality | "99.5% completeness" |
| `[COMPLIANCE_REQUIREMENTS]` | Regulations | "GDPR, SOX" |
