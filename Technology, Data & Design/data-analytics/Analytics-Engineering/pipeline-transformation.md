---
category: data-analytics
title: Data Transformation Pipeline Design
tags:
- data-transformation
- medallion-architecture
- etl-design
- data-quality
use_cases:
- Designing medallion architecture transformations (Bronze → Silver → Gold)
- Planning data cleansing, standardization, and enrichment strategies
- Implementing slowly changing dimensions and dimensional models
- Architecting scalable transformation pipelines
related_templates:
- data-analytics/Analytics-Engineering/pipeline-ingestion.md
- data-analytics/Analytics-Engineering/pipeline-orchestration.md
- data-analytics/Analytics-Engineering/pipeline-observability.md
- data-analytics/Analytics-Engineering/data-modeling.md
industries:
- technology
- finance
- retail
- healthcare
- manufacturing
type: framework
difficulty: intermediate
slug: pipeline-transformation
---

# Data Transformation Pipeline Design

## Purpose
Design comprehensive data transformation pipelines following medallion architecture patterns. This framework guides transformation strategy across Bronze, Silver, and Gold layers including data cleansing, standardization, enrichment, business logic application, and advanced patterns like slowly changing dimensions.

## 🚀 Quick Transformation Prompt

> Design a **[MEDALLION_LAYER]** transformation pipeline for **[DATA_DOMAIN]** using **[PROCESSING_FRAMEWORK]**. Evaluate across: (1) **Cleansing strategy**—how should nulls, duplicates, invalid formats, and outliers be handled? What are the business rules for data validity? (2) **Standardization approach**—what reference data lookups, code mappings, and format normalizations are required? (3) **Enrichment requirements**—what calculated fields, external data joins, or derived attributes are needed? (4) **Quality gates**—what validation rules must pass before data advances to the next layer? (5) **Performance design**—what partitioning, caching, and optimization strategies apply? Provide transformation specifications, data quality rules, and implementation guidance.

---

## Template

Design data transformation pipeline for {DATA_DOMAIN} implementing {TRANSFORMATION_ARCHITECTURE} architecture using {PROCESSING_FRAMEWORK} with business objectives of {BUSINESS_REQUIREMENTS}.

**BRONZE LAYER TRANSFORMATION**

Define bronze layer specifications establishing the raw data landing zone with minimal transformation. Specify source system extraction patterns determining how data arrives from operational systems, files, APIs, or streaming sources. Configure schema inference or explicit schema definitions balancing flexibility against data contract enforcement. Implement metadata capture recording source system, extraction timestamp, batch identifier, and file provenance for lineage tracking. Design partition strategy for bronze layer optimizing for write performance and raw data queryability, typically partitioning by ingestion date. Establish retention policies determining how long raw data remains available for reprocessing scenarios.

**SILVER LAYER TRANSFORMATION**

Design bronze-to-silver cleansing transformations addressing data quality issues systematically. Define null handling strategies specifying default values, forward-fill logic, or exclusion rules for each column based on business semantics. Implement deduplication logic identifying the business key for uniqueness and ranking criteria when duplicates exist such as keeping the most recent record by timestamp or highest quality score. Specify data type conversions casting string representations to proper types including dates, numerics, and booleans with explicit format patterns and error handling. Design format standardization for common fields including phone number normalization, email lowercase conversion, address parsing, and name capitalization rules.

Configure standardization transformations applying reference data and business rules. Define reference data joins specifying lookup tables for code translations, hierarchies, and enrichment such as mapping country codes to country names or product SKUs to category hierarchies. Implement business rule calculations adding derived fields computed from source columns including age from birthdate, tenure from hire date, or margin from revenue and cost. Design outlier handling determining detection methods such as standard deviation bounds, interquartile range, or domain-specific limits and treatment options including cap, flag, exclude, or quarantine.

Establish silver layer validation gates defining quality rules that must pass before data advances. Specify completeness rules requiring non-null values for critical fields. Define validity rules constraining values to acceptable ranges or reference lists. Implement consistency rules ensuring related fields align logically such as end dates after start dates or child records having valid parent references. Configure uniqueness rules preventing duplicate business keys from reaching silver layer. Design timeliness rules flagging stale data based on expected refresh frequencies.

**GOLD LAYER TRANSFORMATION**

Design silver-to-gold aggregation and business logic transformations creating analytics-ready datasets. Define dimensional model structure specifying fact tables containing measurable events and dimension tables containing descriptive attributes. Implement grain definitions establishing the most atomic level of detail for each fact table such as one row per transaction, per customer per day, or per product per location per week.

Configure slowly changing dimension logic determining how dimension changes are tracked. For Type 1 dimensions, specify overwrite behavior for attributes where history is not needed. For Type 2 dimensions, define effective dating strategy including surrogate key generation, effective and expiration dates, and current record flagging for attributes requiring full history. For Type 3 dimensions, specify previous value columns for attributes needing limited history such as previous address alongside current address.

Design aggregation transformations defining summary tables optimized for common query patterns. Specify aggregation grains such as daily, weekly, monthly, or by customer segment, product category, or geographic region. Implement KPI calculations defining business metric formulas including revenue recognition rules, customer lifetime value algorithms, conversion rate calculations, and retention metrics. Configure window function analytics for running totals, moving averages, period-over-period comparisons, and ranking calculations.

Establish gold layer quality validation ensuring business rule compliance. Define cross-table consistency rules verifying fact-dimension relationships and aggregate-to-detail reconciliation. Implement business threshold validations flagging unexpected values such as negative inventory, future dates in historical fields, or metrics outside normal ranges.

**PERFORMANCE OPTIMIZATION**

Design transformation performance strategy addressing large-scale data processing. Specify partitioning scheme for each layer optimizing for both write patterns during transformation and read patterns during consumption. Implement incremental processing logic identifying change detection mechanisms such as timestamps, change data capture flags, or hash comparisons to process only new and modified records. Configure caching strategy for reference data and intermediate results reducing redundant computation in complex multi-step transformations.

Define parallelization approach determining partition counts, worker allocation, and memory configuration for distributed processing frameworks. Specify optimization hints including broadcast joins for small reference tables, predicate pushdown to minimize data movement, and column pruning to reduce I/O. Implement storage optimization using columnar formats with appropriate compression and file sizing for downstream query performance.

Deliver transformation design as:

1. **LAYER SPECIFICATIONS** - Detailed transformation logic for each medallion layer with data flow diagrams

2. **DATA QUALITY RULES** - Complete rule catalog with thresholds, actions, and monitoring requirements

3. **SCHEMA DEFINITIONS** - Target schemas for each layer including data types, constraints, and documentation

4. **TRANSFORMATION LOGIC** - Business rule specifications, calculation formulas, and mapping documentation

5. **PERFORMANCE CONFIGURATION** - Partitioning, caching, and optimization settings with sizing guidance

6. **LINEAGE DOCUMENTATION** - Source-to-target mappings and transformation dependency graphs

---

## Usage Examples

### Example 1: E-commerce Customer 360
**Prompt:** Design data transformation pipeline for customer analytics implementing medallion architecture using Spark with business objectives of creating unified customer view joining transactions, interactions, and preferences for personalization and lifetime value analysis.

**Expected Output:** Bronze layer ingesting raw clickstream, transaction, and CRM exports with schema inference. Silver layer deduplicating customers by email with recency ranking, standardizing addresses via geocoding API, and validating email formats. Gold layer implementing Type 2 SCD for customer attributes, calculating RFM scores and predicted lifetime value, and building customer segment assignments with daily refresh.

### Example 2: Financial Reporting Pipeline
**Prompt:** Design data transformation pipeline for regulatory reporting implementing star schema dimensional model using dbt with business objectives of producing accurate daily position reporting and monthly regulatory submissions with full audit trail.

**Expected Output:** Bronze layer capturing trading system extracts and market data feeds with immutable storage. Silver layer applying trade date adjustments, currency conversions via daily rate lookups, and counterparty enrichment from reference master. Gold layer building fact_positions at instrument-day grain, dim_accounts with Type 2 history, and pre-aggregated regulatory report tables with reconciliation validations against source systems.

### Example 3: IoT Sensor Analytics
**Prompt:** Design data transformation pipeline for manufacturing quality monitoring implementing streaming medallion architecture using Kafka and Spark Structured Streaming with business objectives of real-time anomaly detection and hourly quality dashboards.

**Expected Output:** Bronze layer capturing raw sensor JSON with five-minute micro-batches preserving full message payload. Silver layer parsing measurements, filtering invalid readings outside physical bounds, and deduplicating by sensor-timestamp with latest-value semantics. Gold layer computing five-minute rolling averages, detecting anomalies via three-sigma deviation, aggregating to hourly quality metrics by production line, and triggering alerts on threshold breaches.

---

## Cross-References

- [Pipeline Ingestion](pipeline-ingestion.md) - Source system extraction and landing zone design
- [Pipeline Orchestration](pipeline-orchestration.md) - Workflow scheduling and dependency management
- [Pipeline Observability](pipeline-observability.md) - Monitoring, alerting, and debugging
- [Data Modeling](data-modeling.md) - Dimensional modeling and schema design patterns
- [Analytics Data Quality](analytics-data-quality.md) - Data quality frameworks and validation rules
