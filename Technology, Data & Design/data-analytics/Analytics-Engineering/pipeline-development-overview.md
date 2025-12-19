---
category: data-analytics
description: Navigate the complete data pipeline development lifecycle from ingestion through infrastructure, selecting appropriate patterns and modules for end-to-end pipeline architecture
title: Pipeline Development Overview & Navigation
tags:
- data-pipelines
- etl-elt
- data-engineering
- analytics-engineering
use_cases:
- Understanding the complete data pipeline development lifecycle
- Navigating to focused sub-prompts for specific pipeline components
- Designing end-to-end data pipeline architectures
- Selecting appropriate patterns and technologies for pipeline projects
related_templates:
- data-analytics/Analytics-Engineering/pipeline-ingestion.md
- data-analytics/Analytics-Engineering/pipeline-transformation.md
- data-analytics/Analytics-Engineering/pipeline-orchestration.md
- data-analytics/Analytics-Engineering/pipeline-observability.md
- data-analytics/Analytics-Engineering/pipeline-infrastructure.md
industries:
- finance
- healthcare
- retail
- technology
- manufacturing
type: framework
difficulty: intermediate
slug: pipeline-development-overview
---

# Pipeline Development Overview & Navigation

## Purpose
Navigate the complete data pipeline development lifecycle from data ingestion through infrastructure deployment. This overview helps you understand pipeline architecture patterns and select the appropriate specialized module for detailed implementation guidance across ingestion, transformation, orchestration, observability, and infrastructure.

## 🚀 Quick Start Prompt

> Design a **data pipeline architecture** for **[USE CASE]** with sources from **[SOURCE TYPES]** to **[TARGET PLATFORM]**. Evaluate: (1) **Pipeline pattern**—batch, streaming, CDC, or hybrid based on latency requirements; (2) **Architecture layers**—medallion (bronze-silver-gold), lambda, or kappa; (3) **Component selection**—ingestion method, transformation approach, orchestration platform, observability stack; (4) **Technology choices**—processing framework, storage format, cloud services. Deliver architecture diagram, component selection rationale, module navigation guide, and implementation phasing.

---

## Template

Design a pipeline architecture for {PIPELINE_CONTEXT}, implementing {ARCHITECTURE_REQUIREMENTS} to achieve {DELIVERY_OBJECTIVES}.

**1. Pipeline Pattern Selection**

Begin by selecting the fundamental pipeline pattern based on latency, volume, and complexity requirements. Batch processing suits workloads with daily or hourly freshness requirements, large data volumes processed efficiently in bulk, and well-defined processing windows—most analytics and reporting pipelines start here. Streaming processing fits real-time use cases requiring sub-second to minute latency, continuous event processing, and immediate reaction to data changes—user behavior analytics, fraud detection, and operational monitoring benefit from streaming. Change Data Capture (CDC) provides efficient incremental processing capturing only database changes rather than full extracts—ideal for keeping data warehouses synchronized with operational systems without heavy source system load. Hybrid architectures combine patterns for different data types or use cases—batch for historical analysis with streaming for real-time dashboards, or CDC for transactional data with batch for reference data.

**2. Architecture Layer Design**

Structure your pipeline using proven architectural patterns that separate concerns and enable incremental processing. Medallion architecture (bronze-silver-gold) organizes data by quality level: bronze receives raw data with minimal transformation preserving source fidelity, silver contains cleaned and validated data conforming to enterprise standards, and gold provides business-ready aggregates optimized for specific consumption patterns. Lambda architecture separates batch and streaming paths that merge at the serving layer—batch provides accurate historical views while streaming enables real-time updates, though it requires maintaining two codebases. Kappa architecture treats all data as streams, using replay for reprocessing—simpler to maintain but requires streaming infrastructure capable of handling historical volumes. Choose medallion for most modern data platforms, lambda when you have distinct batch and streaming requirements with different processing logic, and kappa when streaming-first simplicity outweighs reprocessing complexity.

**3. Ingestion Module Selection**

Navigate to the appropriate ingestion approach based on source characteristics and freshness requirements. For database sources, choose between full extracts (simple but inefficient for large tables), incremental extracts using timestamps or sequence numbers (efficient for append-heavy tables), or CDC using database logs (most efficient, captures all changes including deletes). For API sources, implement pagination handling, rate limiting, authentication management, and cursor-based incremental extraction. For file sources, design landing zones with file arrival detection, format handling (CSV, JSON, Parquet, Avro), and archive management. For streaming sources, configure consumer groups, partition assignment, offset management, and exactly-once semantics. The pipeline-ingestion module provides detailed patterns for each source type including error handling, retry logic, and metadata tracking.

**4. Transformation Module Selection**

Select transformation approaches based on processing complexity and target structure. Bronze-to-silver transformations focus on data quality: deduplication, null handling, data type standardization, timestamp normalization, and referential integrity validation. Silver-to-gold transformations implement business logic: calculations, aggregations, dimensional modeling, slowly changing dimension (SCD) handling, and metric derivation. Choose SQL-based transformation (dbt, Spark SQL) for declarative logic that analysts can understand and maintain. Use DataFrame APIs (PySpark, Pandas) for complex procedural logic, ML feature engineering, or integration with Python libraries. Implement data quality gates between layers validating row counts, aggregate consistency, business rule compliance, and freshness requirements. The pipeline-transformation module details medallion layer patterns, SCD implementations, and quality check frameworks.

**5. Orchestration Module Selection**

Design workflow coordination based on dependency complexity and operational requirements. Simple linear pipelines with few dependencies may use basic scheduling (cron, cloud scheduler) without dedicated orchestration platforms. Complex pipelines with branching logic, cross-pipeline dependencies, and dynamic task generation benefit from dedicated orchestrators like Airflow, Prefect, or Dagster. Consider orchestrator capabilities: dependency management (how complex can dependency graphs be), dynamic workflows (can tasks be generated at runtime), backfill support (how easily can you reprocess historical data), and operational features (alerting, retries, SLAs). Design DAGs with clear task boundaries, appropriate parallelism, sensible timeout and retry configurations, and observable task states. The pipeline-orchestration module provides DAG design patterns, dependency management strategies, and platform-specific guidance.

**6. Observability Module Selection**

Implement monitoring covering pipeline health, data quality, and operational metrics. Pipeline execution monitoring tracks job status, duration, resource consumption, and failure rates—essential for operational awareness and SLA management. Data quality monitoring validates row counts, null rates, value distributions, and business rule compliance at each pipeline stage—catching data issues before they reach consumers. Alerting rules notify appropriate teams of failures, SLA breaches, data quality violations, and anomalies requiring investigation. Dashboards provide operational visibility into pipeline fleet health, individual pipeline status, and data freshness across domains. Error handling frameworks classify failures, implement appropriate retry strategies, route unprocessable records to dead letter queues, and enable manual intervention workflows. The pipeline-observability module details metric collection, alerting strategies, and incident response patterns.

**7. Infrastructure Module Selection**

Plan infrastructure supporting pipeline compute, storage, and deployment requirements. Compute infrastructure ranges from serverless functions for simple transformations, to container-based workers for medium complexity, to dedicated clusters for large-scale processing—choose based on volume, complexity, and cost optimization needs. Storage architecture includes landing zones for incoming data, bronze/silver/gold layers for processed data, and archive tiers for historical retention—configure lifecycle policies and access patterns appropriately. Deployment automation using infrastructure as code (Terraform, CloudFormation) ensures reproducible environments across development, staging, and production. Auto-scaling configurations enable pipelines to handle variable loads efficiently—scale based on queue depth, processing lag, or scheduled capacity increases. The pipeline-infrastructure module covers IaC patterns, Kubernetes deployments, and performance optimization.

**8. Implementation Phasing**

Plan implementation in phases that deliver incremental value while managing complexity. Phase one establishes foundation: implement core ingestion for highest-priority sources, basic bronze layer storage, and simple orchestration proving the architecture works end-to-end. Phase two adds transformation depth: build silver layer quality rules, implement business logic for gold layer, and add data quality monitoring validating transformation correctness. Phase three enhances operations: implement comprehensive observability, optimize performance for production volumes, and harden error handling for production reliability. Phase four expands scope: add remaining data sources, implement advanced patterns (streaming, CDC), and optimize infrastructure costs. Each phase should deliver usable capability—avoid big-bang implementations that delay all value until everything is complete.

Deliver your pipeline architecture as:

1. **Pattern selection** justifying batch, streaming, CDC, or hybrid based on requirements
2. **Layer architecture** specifying medallion, lambda, or kappa with layer responsibilities
3. **Ingestion approach** for each source type with module navigation
4. **Transformation strategy** with quality gates and module navigation
5. **Orchestration design** specifying platform and DAG patterns
6. **Observability plan** covering monitoring, alerting, and error handling
7. **Infrastructure requirements** with compute, storage, and deployment approach
8. **Implementation roadmap** with phased delivery and success criteria

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{PIPELINE_CONTEXT}` | Use case, sources, and targets | "e-commerce analytics pipeline from PostgreSQL, Stripe API, and Segment to Snowflake" |
| `{ARCHITECTURE_REQUIREMENTS}` | Patterns and constraints | "medallion architecture, daily batch with real-time inventory, SOC 2 compliance" |
| `{DELIVERY_OBJECTIVES}` | Timeline and success criteria | "MVP in 4 weeks with core sales data, full scope in 12 weeks, data ready by 6am daily" |

---

## Usage Examples

### Example 1: E-Commerce Analytics Pipeline
**Prompt:** "Design a pipeline architecture for {PIPELINE_CONTEXT: e-commerce analytics consolidating PostgreSQL orders, Stripe payments, Shopify products, and Google Analytics events into Snowflake}, implementing {ARCHITECTURE_REQUIREMENTS: medallion architecture with daily batch processing, incremental loads where possible, and dbt for transformations}, to achieve {DELIVERY_OBJECTIVES: marketing and finance dashboards operational in 6 weeks with data freshness by 6am daily}."

**Expected Output:** Pattern selection choosing batch with incremental extraction for database sources and API pagination for Stripe/Shopify. Medallion architecture with bronze preserving source schemas, silver standardizing to common models (orders, payments, products, sessions), and gold providing marketing attribution and financial reporting aggregates. Ingestion approach using Fivetran or Airbyte for managed connectors with pipeline-ingestion patterns for custom sources. Transformation with dbt models implementing silver cleaning and gold business logic per pipeline-transformation. Orchestration with Airflow running at 2am with source extraction parallel, then sequential layer processing. Observability with row count monitoring, freshness alerts at 5:30am, and Slack notifications. Infrastructure on Snowflake with appropriately sized warehouses per workload. Four-week MVP covering orders and payments, full scope at week six.

### Example 2: Real-Time Fraud Detection Pipeline
**Prompt:** "Design a pipeline architecture for {PIPELINE_CONTEXT: payment fraud detection processing 10,000 transactions per second from Kafka with enrichment from customer profiles and transaction history}, implementing {ARCHITECTURE_REQUIREMENTS: streaming architecture with sub-second latency for scoring, batch for model training features, and real-time dashboards}, to achieve {DELIVERY_OBJECTIVES: production fraud scoring in 8 weeks with 99.9% availability and P99 latency under 200ms}."

**Expected Output:** Pattern selection choosing streaming for transaction scoring with batch for historical feature generation—hybrid architecture. Kappa-style streaming with Kafka Streams or Flink for real-time processing, separate batch pipeline for ML feature store updates. Ingestion from Kafka with exactly-once semantics, consumer group management per pipeline-ingestion streaming patterns. Transformation using Flink for real-time feature computation and scoring, Spark for batch feature engineering per pipeline-transformation. Orchestration minimal for streaming (self-running), Airflow for batch feature jobs per pipeline-orchestration. Observability with consumer lag monitoring, latency percentile tracking, and PagerDuty integration per pipeline-observability. Infrastructure on Kubernetes with auto-scaling based on Kafka lag per pipeline-infrastructure. Phased delivery: basic scoring week four, full enrichment week six, production hardening week eight.

### Example 3: Healthcare Data Integration Pipeline
**Prompt:** "Design a pipeline architecture for {PIPELINE_CONTEXT: clinical data warehouse integrating Epic EHR via HL7 FHIR, claims from multiple payers, and lab results from reference labs into Databricks}, implementing {ARCHITECTURE_REQUIREMENTS: medallion lakehouse with HIPAA compliance, full data lineage, and support for both operational reporting and research analytics}, to achieve {DELIVERY_OBJECTIVES: quality measure reporting in 12 weeks, research data mart in 20 weeks, with complete audit trail}."

**Expected Output:** Pattern selection choosing batch for claims with CDC for EHR changes and near-real-time for lab results. Medallion lakehouse with bronze on Delta Lake preserving PHI with encryption, silver implementing FHIR-to-common-model transformation with de-identification capability, and gold providing quality measure calculations and de-identified research views. Ingestion using FHIR bulk export for Epic, SFTP for claims files, API polling for labs per pipeline-ingestion. Transformation with patient matching in silver, quality measure logic in gold, Unity Catalog for data lineage per pipeline-transformation. Orchestration with Databricks Workflows and approval gates for research data access per pipeline-orchestration. Observability with PHI access logging, data quality dashboards, and compliance reporting per pipeline-observability. Infrastructure with workspace isolation, VPC peering, and customer-managed keys per pipeline-infrastructure. Phased: EHR integration weeks 1-6, claims weeks 7-12, research mart weeks 13-20.

---

## Cross-References

- [pipeline-ingestion.md](pipeline-ingestion.md) - Batch, streaming, and CDC extraction patterns
- [pipeline-transformation.md](pipeline-transformation.md) - Medallion layers and data quality
- [pipeline-orchestration.md](pipeline-orchestration.md) - DAG design and workflow coordination
- [pipeline-observability.md](pipeline-observability.md) - Monitoring, alerting, and error handling
- [pipeline-infrastructure.md](pipeline-infrastructure.md) - IaC, deployment, and scaling
