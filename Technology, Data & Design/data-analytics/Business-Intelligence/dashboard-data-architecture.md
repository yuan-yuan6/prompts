---
category: data-analytics
last_updated: 2025-11-22
related_templates:
- data-analytics/Business-Intelligence/dashboard-strategy-requirements.md
- data-analytics/Business-Intelligence/dashboard-technical-implementation.md
- data-analytics/Business-Intelligence/dashboard-design-overview.md
tags:
- business-intelligence
- dashboards
- data-architecture
- etl
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
type: template
difficulty: intermediate
slug: dashboard-data-architecture
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

## Usage Examples

### Example 1: Retail Omnichannel Analytics

**Context:** Retail chain needs unified data architecture for online + in-store sales analytics

**Copy-paste this prompt:**

```
I need to design a comprehensive data architecture for a dashboard solution with the following requirements:

### Data Source Landscape
**Primary Data Sources:**
- ERP system: SAP S/4HANA (inventory, finance, purchasing)
- CRM system: None - using loyalty program database directly
- Database systems: Oracle (POS transactions), PostgreSQL (e-commerce orders)
- Cloud platforms: AWS (primary), Azure (legacy e-commerce)
- File sources: Daily CSV inventory feeds from 500 stores, Excel promotions calendar
- APIs: Shopify (online orders), Google Analytics 4 (web traffic), Meta Ads API
- Other systems: Manhattan WMS (warehouse), Salesforce Marketing Cloud (campaigns)

**Data Volume & Velocity:**
- Total data volume: 2 TB (3 years history)
- Daily data growth: 15 GB on regular days, 100 GB on Black Friday/Cyber Monday
- Update frequency: POS every 15 minutes, e-commerce real-time, inventory hourly
- Historical data retention: 3 years online (hot), 7 years archive (cold)
- Peak load characteristics: Holiday season 10x normal, flash sales spike 20x

### Integration Requirements
**Data Extraction:**
- Extraction method: CDC for Oracle POS (GoldenGate), API polling for e-commerce, batch for SAP
- Source system constraints: SAP extract window 12AM-4AM only, Oracle CDC has 5-minute lag
- Extraction schedule: POS CDC continuous, e-commerce real-time, SAP nightly at 2AM
- Data latency tolerance: Sales data 15 minutes, inventory 1 hour, finance next-day

**Data Transformation:**
- Cleansing requirements: Standardize product SKUs across systems, dedupe customer records
- Validation rules: Sales amount > 0, valid store ID, product exists in master
- Business logic: Calculate basket size, customer lifetime value, promotion attribution
- Enrichment needs: Add geographic data from store master, product hierarchy from PIM
- Aggregation requirements: Hourly/daily/weekly sales, store-level and region-level rollups

**Data Loading:**
- Loading strategy: Micro-batch for POS (15 min), streaming for e-commerce, batch for SAP
- Target platform: Snowflake data warehouse + S3 data lake
- Loading schedule: Continuous for transactions, nightly for dimensions
- Error handling approach: Quarantine invalid records, alert on >1% rejection rate

### Data Warehouse Design
**Modeling Approach:**
- Data model type: Star schema with conformed dimensions
- Grain definition: Individual transaction line item
- Fact tables: Sales, Inventory, Web Sessions, Marketing Touchpoints
- Dimension tables: Product, Store, Customer, Date, Promotion, Channel
- Slowly changing dimensions: Type 2 for Product (track price changes), Type 1 for Store

**Storage & Performance:**
- Storage platform: Snowflake (hot), S3 Glacier (archive)
- Partitioning strategy: Partition by month on transaction_date
- Indexing approach: Cluster on store_id, product_id, date
- Compression: Snowflake automatic + Parquet for lake
- Expected query performance: Dashboard loads <5 seconds, ad-hoc queries <30 seconds

### Data Quality & Governance
**Quality Framework:**
- Completeness checks: All transactions have store_id, product_id, customer_id (when known)
- Accuracy validation: Daily sales totals match POS system reports
- Consistency rules: Product exists in dimension before loading transactions
- Timeliness monitoring: Alert if POS data >20 minutes old, inventory >2 hours old
- Quality thresholds: 99.9% completeness, 99.8% accuracy, 100% referential integrity

**Governance Requirements:**
- Data ownership: Merchandising owns product data, IT owns POS integration
- Metadata management: Full data dictionary, business glossary for metrics
- Data lineage tracking: Track from source system to dashboard metric
- Catalog: Alation catalog with automated profiling
- Compliance requirements: GDPR (EU stores), CCPA (California customers), PCI-DSS (payment data)

### Pipeline Architecture
**Orchestration:**
- Orchestration tool: Apache Airflow on AWS MWAA
- Scheduling requirements: 15-min micro-batches for sales, hourly for inventory, nightly for dimensions
- Dependency management: Dimensions load before facts, aggregations after base tables
- Retry logic: 3 retries with exponential backoff, dead letter queue for failures
- Alerting requirements: PagerDuty for pipeline failures, Slack for data quality issues

**Scalability & Reliability:**
- Concurrent pipeline runs: Up to 50 (one per store group + shared jobs)
- Failover requirements: Multi-AZ deployment, auto-failover for critical pipelines
- Disaster recovery: RPO 1 hour, RTO 4 hours
- Monitoring approach: CloudWatch metrics, custom Airflow dashboard, Great Expectations for DQ

Please provide:
1. Complete data architecture diagram (sources → lake → warehouse → BI)
2. ETL pipeline design for each source system
3. Star schema data model with 4 fact tables and 6 dimensions
4. Data quality framework with specific rules per source
5. Holiday scaling strategy (10x capacity)
```

**Expected Output:**
- Lambda architecture: Real-time layer (e-commerce) + batch layer (SAP, historical)
- Conformed dimension strategy across online and in-store
- Store clustering for parallel processing
- Black Friday/Cyber Monday capacity planning

---

### Example 2: Healthcare Claims Analytics

**Context:** Health insurer needs claims data warehouse for cost analysis and fraud detection

**Copy-paste this prompt:**

```
I need to design a comprehensive data architecture for a dashboard solution with the following requirements:

### Data Source Landscape
**Primary Data Sources:**
- ERP system: Oracle EBS (finance, GL)
- CRM system: Salesforce Health Cloud (member interactions)
- Database systems: SQL Server (claims processing - FACETS), Oracle (provider network)
- Cloud platforms: Azure (primary cloud environment)
- File sources: 837/835 EDI files (claims, remittances), Excel provider contracts
- APIs: CMS data hub (Medicare data), pharmacy benefit manager (CVS/Caremark API)
- Other systems: UM platform (utilization management), Care management system

**Data Volume & Velocity:**
- Total data volume: 5 TB (10 years claims history required by regulation)
- Daily data growth: 8 GB (claims adjudication)
- Update frequency: Claims batch nightly, eligibility real-time, provider quarterly
- Historical data retention: 10 years online (regulatory requirement), unlimited archive
- Peak load characteristics: Annual enrollment period 5x normal, end-of-month processing

### Integration Requirements
**Data Extraction:**
- Extraction method: Batch for claims (nightly adjudication complete), CDC for eligibility
- Source system constraints: FACETS batch window 11PM-3AM, read replica available
- Extraction schedule: Claims nightly at 3AM, eligibility CDC, providers monthly full refresh
- Data latency tolerance: Claims next-day, eligibility real-time, cost metrics weekly

**Data Transformation:**
- Cleansing requirements: Standardize diagnosis codes (ICD-10), procedure codes (CPT), NPI validation
- Validation rules: Member eligible on date of service, provider in network, valid codes
- Business logic: Calculate allowed amount, member responsibility, risk scores (HCC)
- Enrichment needs: Add provider specialty from NPPES, drug classification from NDC
- Aggregation requirements: PMPM costs, utilization rates, medical loss ratio

**Data Loading:**
- Loading strategy: Batch for claims and finance, micro-batch for eligibility
- Target platform: Azure Synapse Analytics
- Loading schedule: Claims at 5AM daily, eligibility continuous, finance weekly
- Error handling approach: Reject invalid claims to review queue, alert on pattern anomalies

### Data Warehouse Design
**Modeling Approach:**
- Data model type: Star schema with claim-centric and member-centric views
- Grain definition: Individual claim line (most granular), rollup to claim header and episode
- Fact tables: Claims, Eligibility Months, Authorizations, Pharmacy, Lab Results
- Dimension tables: Member, Provider, Diagnosis, Procedure, Drug, Date, Plan, Employer Group
- Slowly changing dimensions: Type 2 for Member (track plan changes), Type 2 for Provider (network status)

**Storage & Performance:**
- Storage platform: Azure Synapse dedicated pool (hot), ADLS Gen2 (cold/archive)
- Partitioning strategy: Partition by paid_date (month), distribute by member_id
- Indexing approach: Columnstore + hash distribution on member_id
- Compression: Columnstore compression (10:1 typical for claims)
- Expected query performance: Member 360 view <3 seconds, aggregate queries <10 seconds

### Data Quality & Governance
**Quality Framework:**
- Completeness checks: All claims have member_id, provider_npi, diagnosis, procedure
- Accuracy validation: Total paid matches GL, claim counts match source system
- Consistency rules: Member eligible on service date, provider active on service date
- Timeliness monitoring: Alert if claims data >6 hours late
- Quality thresholds: 99.99% completeness (claims are financial), 100% GL reconciliation

**Governance Requirements:**
- Data ownership: Claims ops owns claims data, Actuarial owns cost metrics
- Metadata management: Business glossary with actuarial definitions
- Data lineage tracking: Full lineage for regulatory audits
- Catalog: Azure Purview with sensitivity classification
- Compliance requirements: HIPAA (all data is PHI), SOX (financial controls), state regulations

### Pipeline Architecture
**Orchestration:**
- Orchestration tool: Azure Data Factory + Databricks
- Scheduling requirements: Nightly claims load, weekly finance reconciliation, monthly provider refresh
- Dependency management: Eligibility before claims, claims before aggregations
- Retry logic: 5 retries for batch jobs, escalate to on-call after 2 hours
- Alerting requirements: PagerDuty for failures, email for reconciliation variances

**Scalability & Reliability:**
- Concurrent pipeline runs: Up to 20 (by line of business)
- Failover requirements: Geo-redundant storage, failover to secondary region
- Disaster recovery: RPO 1 hour, RTO 2 hours (regulatory requirement)
- Monitoring approach: Azure Monitor, custom Power BI ops dashboard

Please provide:
1. HIPAA-compliant data architecture with encryption and access controls
2. Claims ETL with EDI 837/835 parsing and validation
3. Member-centric and claim-centric star schema design
4. Data quality framework for financial accuracy (must reconcile to GL)
5. Fraud detection data pipeline integration points
```

**Expected Output:**
- PHI encryption at rest and in transit, tokenization for analytics
- EDI parsing pipeline with X12 standard compliance
- HCC risk adjustment calculation pipeline
- GL reconciliation process with variance alerting

---

### Example 3: Manufacturing IoT Analytics

**Context:** Manufacturer needs data platform for production analytics and predictive maintenance

**Copy-paste this prompt:**

```
I need to design a comprehensive data architecture for a dashboard solution with the following requirements:

### Data Source Landscape
**Primary Data Sources:**
- ERP system: SAP S/4HANA (production orders, inventory, costs)
- CRM system: None (B2B with EDI integration)
- Database systems: SQL Server (MES - Rockwell FactoryTalk), Historian (OSIsoft PI)
- Cloud platforms: AWS (analytics), on-premise (operational systems)
- File sources: Excel quality inspection sheets, CSV sensor exports (backup)
- APIs: Equipment OPC-UA endpoints (300 machines), weather API (external factors)
- Other systems: CMMS (Maximo for maintenance), PLM (product specs), SCADA

**Data Volume & Velocity:**
- Total data volume: 10 TB (2 years sensor history at 1-second resolution)
- Daily data growth: 50 GB (sensor data), 500 MB (transactional)
- Update frequency: Sensor data every second, MES every minute, SAP hourly
- Historical data retention: 2 years at full resolution, 5 years aggregated, 10 years daily
- Peak load characteristics: 3-shift operation, consistent load 24/7

### Integration Requirements
**Data Extraction:**
- Extraction method: Streaming for sensor data (Kafka), CDC for MES, batch for SAP
- Source system constraints: OPC-UA bandwidth limits, Historian query performance
- Extraction schedule: Sensors continuous, MES every minute, SAP every 2 hours
- Data latency tolerance: Sensors 5 seconds (for real-time monitoring), MES 1 minute, SAP 2 hours

**Data Transformation:**
- Cleansing requirements: Filter sensor noise, interpolate missing values, validate ranges
- Validation rules: Sensor values within physical limits, timestamps sequential
- Business logic: Calculate OEE, cycle time, yield, MTBF, MTTR
- Enrichment needs: Add product specs from PLM, maintenance history from CMMS
- Aggregation requirements: Second → Minute → Hour → Shift → Day → Week rollups

**Data Loading:**
- Loading strategy: Streaming for sensors (Kafka → Spark → S3), micro-batch for MES
- Target platform: S3 data lake (raw), Redshift (aggregated analytics)
- Loading schedule: Continuous for sensors, minute-level for MES, hourly for SAP
- Error handling approach: Buffer sensor data during outages, replay from Historian

### Data Warehouse Design
**Modeling Approach:**
- Data model type: Time-series optimized (Timescale pattern) + star schema for reporting
- Grain definition: 1-second sensor readings (raw), 1-minute aggregates (analytics)
- Fact tables: Sensor Readings, Production Events, Quality Measurements, Maintenance Tickets
- Dimension tables: Machine, Product, Shift, Date/Time, Operator, Location, Sensor Type
- Slowly changing dimensions: Type 2 for Machine (track configuration changes)

**Storage & Performance:**
- Storage platform: S3 (raw), Timestream (time-series), Redshift (aggregates)
- Partitioning strategy: Partition by day + machine_id for sensor data
- Indexing approach: Time-based partitioning, machine_id secondary
- Compression: Parquet with snappy, time-series delta encoding
- Expected query performance: Real-time dashboard <1 second, historical query <5 seconds

### Data Quality & Governance
**Quality Framework:**
- Completeness checks: Continuous sensor data (detect gaps), all production events captured
- Accuracy validation: Sensor readings within physical limits, OEE calculation audit
- Consistency rules: Machine exists, product valid for machine, operator on shift
- Timeliness monitoring: Alert if sensor data >10 seconds delayed, MES >2 minutes
- Quality thresholds: 99.9% sensor uptime, 100% production event capture

**Governance Requirements:**
- Data ownership: Engineering owns sensor data, Operations owns production metrics
- Metadata management: Sensor catalog with units, ranges, calibration data
- Data lineage tracking: Trace from raw sensor to OEE metric
- Catalog: AWS Glue catalog with machine/sensor metadata
- Compliance requirements: ISO 9001 (quality data retention), customer audit requirements

### Pipeline Architecture
**Orchestration:**
- Orchestration tool: Apache Airflow for batch, Kafka Streams for real-time
- Scheduling requirements: Continuous streaming, hourly aggregations, daily ML model refresh
- Dependency management: Raw before aggregates, aggregates before ML features
- Retry logic: Sensor replay from Historian, 3 retries for batch jobs
- Alerting requirements: Real-time alerts for sensor anomalies, Slack for pipeline issues

**Scalability & Reliability:**
- Concurrent pipeline runs: Parallel per plant (4 plants), per machine group
- Failover requirements: Kafka HA cluster, buffer to Historian during outages
- Disaster recovery: RPO 1 minute for sensor data, RTO 15 minutes
- Monitoring approach: Prometheus for Kafka, CloudWatch for AWS, Grafana dashboards

Please provide:
1. Streaming architecture for 1M+ sensor readings per minute
2. Time-series data model optimized for OEE queries
3. Edge-to-cloud data flow for low-latency analytics
4. Aggregation strategy (second → minute → hour → shift)
5. Predictive maintenance feature engineering pipeline
```

**Expected Output:**
- Kafka + Spark Streaming architecture
- Timestream for real-time, S3+Parquet for historical
- OEE calculation pipeline (Availability × Performance × Quality)
- ML feature store for predictive maintenance

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
