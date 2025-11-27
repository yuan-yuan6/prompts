---
title: Pipeline Development Overview & Navigation
category: data-analytics
tags:
- data-analytics
- data-pipelines
- etl
- data-engineering
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
- data-analytics/data-governance-framework.md
last_updated: 2025-11-22
industries:
- healthcare
- manufacturing
- technology
type: template
difficulty: intermediate
slug: pipeline-development-overview
---

# Pipeline Development Overview & Navigation

## Purpose
This overview provides comprehensive guidance for data pipeline development, helping you navigate the complete pipeline development lifecycle from data ingestion through infrastructure deployment. Use this as a starting point to understand the pipeline architecture and navigate to specialized sub-prompts for detailed implementation guidance.

## Quick Navigation Prompt
I need to build a [PIPELINE_TYPE] data pipeline for [USE_CASE]. The data sources are [SOURCE_TYPES] and destination is [TARGET_PLATFORM]. Help me identify which sub-prompt to use: ingestion patterns (batch/streaming/CDC), transformation logic (medallion architecture), orchestration (DAG design), observability (monitoring/alerting), or infrastructure (IaC/Kubernetes).

## Quick Start

**Want to build a data pipeline?** Here's how to navigate this framework:

### When to Use This Overview
- Building a new data pipeline from scratch
- Modernizing existing ETL processes to ELT or streaming
- Implementing medallion architecture (Bronze/Silver/Gold layers)
- Need guidance on which pipeline component to focus on
- Planning end-to-end data pipeline architecture

### Quick Module Selection
```
Your Pipeline Task → Recommended Module:

1. Extract data from databases, APIs, files, or streams
   → pipeline-ingestion.md (Batch, streaming, CDC patterns, 2-4 hours)

2. Clean, transform, and apply business logic to data
   → pipeline-transformation.md (Bronze→Silver→Gold, 3-5 hours)

3. Schedule, coordinate, and manage pipeline workflows
   → pipeline-orchestration.md (Airflow, Prefect, dbt workflows, 2-3 hours)

4. Monitor, alert, and troubleshoot pipeline issues
   → pipeline-observability.md (Logging, metrics, alerts, 2-3 hours)

5. Deploy and manage pipeline infrastructure
   → pipeline-infrastructure.md (IaC, CI/CD, scalability, 3-5 hours)
```

### Basic 3-Step Workflow
1. **Start with ingestion** - Use pipeline-ingestion.md to extract data from sources
2. **Add transformation** - Use pipeline-transformation.md to implement Bronze→Silver→Gold layers
3. **Enable orchestration** - Use pipeline-orchestration.md to schedule and coordinate jobs

**Time to complete**: 1-2 days for basic pipeline, 1-2 weeks for production-ready with all components

**Pro tip**: Build incrementally - start with simple batch ingestion and basic transformations, validate data quality, then add streaming, complex business logic, and advanced monitoring.

---

## Pipeline Development Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                   PIPELINE DEVELOPMENT LIFECYCLE                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  1. INGESTION → 2. TRANSFORMATION → 3. ORCHESTRATION →          │
│     4. OBSERVABILITY → 5. INFRASTRUCTURE                         │
│                                                                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │  BRONZE      │ →  │   SILVER     │ →  │    GOLD      │      │
│  │  Raw Data    │    │  Cleansed    │    │  Business    │      │
│  │              │    │  Validated   │    │  Ready       │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Sub-Prompt Navigation

### 1. Pipeline Ingestion (pipeline-ingestion.md)
**Focus**: Data extraction layer - getting data into your pipeline

**When to use**:
- Setting up batch data extraction from databases, APIs, or files
- Implementing real-time streaming ingestion from Kafka, Kinesis, or event sources
- Configuring Change Data Capture (CDC) for database synchronization
- Building resilient extraction with error handling and retries

**Key capabilities**:
- Batch ingestion with scheduling and incremental loads
- Streaming ingestion with Kafka/event streams
- CDC pipelines for real-time database sync
- Data validation at ingestion point
- Dead letter queue for failed records
- Extraction metadata tracking

**Line count**: ~550-600 lines

---

### 2. Pipeline Transformation (pipeline-transformation.md)
**Focus**: Medallion architecture (Bronze → Silver → Gold) and data quality

**When to use**:
- Implementing medallion/lakehouse architecture
- Building data cleansing and standardization logic
- Creating slowly changing dimensions (SCD Type 2)
- Applying complex business logic and aggregations
- Enriching data from external sources or ML models

**Key capabilities**:
- Bronze → Silver: Cleansing, standardization, validation
- Silver → Gold: Business logic, aggregations, dimensional modeling
- Data quality checks between layers
- SCD Type 2 implementation
- Window functions and advanced analytics
- Data deduplication strategies
- Data lineage tracking

**Line count**: ~500-550 lines

---

### 3. Pipeline Orchestration (pipeline-orchestration.md)
**Focus**: Workflow definition, task dependencies, and scheduling

**When to use**:
- Designing Apache Airflow DAGs or similar workflows
- Managing complex task dependencies and parallel execution
- Implementing dynamic task generation
- Setting up conditional workflows and branching
- Configuring retry logic and failure handling

**Key capabilities**:
- DAG design patterns and best practices
- Task dependency management
- Dynamic task generation for multiple sources
- Conditional branching based on data/quality
- Resource pool management
- SLA monitoring and alerting
- XCom for inter-task communication

**Line count**: ~450-500 lines

---

### 4. Pipeline Observability (pipeline-observability.md)
**Focus**: Monitoring, alerting, error handling, and recovery

**When to use**:
- Setting up pipeline monitoring and alerting
- Implementing comprehensive error handling
- Building operational dashboards
- Creating incident response procedures
- Implementing circuit breakers for resilience

**Key capabilities**:
- Pipeline execution metrics collection
- SLA compliance monitoring
- Data quality threshold alerting
- Real-time streaming pipeline monitors
- Error classification and recovery strategies
- Circuit breaker pattern for unreliable dependencies
- Dead letter queue management
- Automated incident response

**Line count**: ~650-700 lines

---

### 5. Pipeline Infrastructure (pipeline-infrastructure.md)
**Focus**: Infrastructure provisioning, deployment, and performance optimization

**When to use**:
- Provisioning infrastructure with Terraform/IaC
- Deploying containerized pipelines with Kubernetes
- Optimizing pipeline performance and resource usage
- Implementing auto-scaling strategies
- Setting up high availability and disaster recovery

**Key capabilities**:
- Performance bottleneck identification and optimization
- Terraform infrastructure as code templates
- Kubernetes deployment manifests
- Auto-scaling configuration (HPA)
- Resource allocation and limits
- Cost optimization strategies
- High availability setup
- CI/CD pipeline integration

**Line count**: ~600-650 lines

---

## Decision Tree: Which Sub-Prompt Should I Use?

```
START: What is your current focus?

├─ "I need to extract data from sources"
│  └─ → Use pipeline-ingestion.md
│     ├─ Batch extraction? → See "Batch Ingestion" section
│     ├─ Real-time streaming? → See "Streaming Ingestion" section
│     └─ Database CDC? → See "Change Data Capture" section
│
├─ "I need to transform and clean data"
│  └─ → Use pipeline-transformation.md
│     ├─ Raw to cleansed? → See "Bronze to Silver" section
│     ├─ Cleansed to business-ready? → See "Silver to Gold" section
│     ├─ Historical tracking? → See "SCD Type 2" section
│     └─ Advanced analytics? → See "Window Functions" section
│
├─ "I need to orchestrate workflow execution"
│  └─ → Use pipeline-orchestration.md
│     ├─ Basic DAG? → See "Workflow Definition" section
│     ├─ Multiple sources? → See "Dynamic Task Generation" section
│     └─ Conditional logic? → See "Advanced Patterns" section
│
├─ "I need monitoring and error handling"
│  └─ → Use pipeline-observability.md
│     ├─ Batch monitoring? → See "Pipeline Monitoring Framework" section
│     ├─ Streaming monitoring? → See "Streaming Monitor" section
│     ├─ Error handling? → See "Error Handling Framework" section
│     └─ Resilience patterns? → See "Circuit Breaker" section
│
└─ "I need infrastructure and deployment"
   └─ → Use pipeline-infrastructure.md
      ├─ Performance issues? → See "Performance Optimization" section
      ├─ IaC setup? → See "Infrastructure as Code" section
      └─ Container deployment? → See "Kubernetes" section
```

## Integration Patterns

### Pattern 1: Simple Batch ETL Pipeline
**Use case**: Daily batch processing from database to warehouse

**Components**:
1. **Ingestion** (pipeline-ingestion.md): Batch extraction from PostgreSQL
2. **Transformation** (pipeline-transformation.md): Bronze → Silver → Gold
3. **Orchestration** (pipeline-orchestration.md): Airflow DAG scheduled daily
4. **Observability** (pipeline-observability.md): Monitor execution time and data quality
5. **Infrastructure** (pipeline-infrastructure.md): Terraform for RDS and EMR cluster

**Workflow**:
```
Daily Schedule (2 AM)
  ↓
Extract from PostgreSQL (Batch Ingestion)
  ↓
Load to Bronze Layer (Raw)
  ↓
Transform to Silver Layer (Cleansed)
  ↓
Transform to Gold Layer (Business Ready)
  ↓
Data Quality Checks
  ↓
Update Dashboards / Send Notifications
```

---

### Pattern 2: Real-time Streaming Pipeline
**Use case**: Real-time event processing and analytics

**Components**:
1. **Ingestion** (pipeline-ingestion.md): Kafka streaming ingestion
2. **Transformation** (pipeline-transformation.md): Streaming transformations with micro-batches
3. **Orchestration** (pipeline-orchestration.md): Airflow for monitoring, not scheduling
4. **Observability** (pipeline-observability.md): Real-time latency and throughput monitoring
5. **Infrastructure** (pipeline-infrastructure.md): Kubernetes with auto-scaling

**Workflow**:
```
Continuous Stream
  ↓
Kafka Consumer (Streaming Ingestion)
  ↓
Real-time Validation & Enrichment
  ↓
Micro-batch Aggregation
  ↓
Write to Silver/Gold Layers
  ↓
Real-time Dashboards & Alerts
```

---

### Pattern 3: Hybrid Batch + CDC Pipeline
**Use case**: Combine historical batch loads with incremental CDC

**Components**:
1. **Ingestion** (pipeline-ingestion.md): Initial batch + ongoing CDC
2. **Transformation** (pipeline-transformation.md): SCD Type 2 for dimension tracking
3. **Orchestration** (pipeline-orchestration.md): Separate DAGs for batch and CDC
4. **Observability** (pipeline-observability.md): Monitor both batch and CDC metrics
5. **Infrastructure** (pipeline-infrastructure.md): Separate compute for batch vs streaming

**Workflow**:
```
Initial Load:               Incremental Updates:
  Batch Extract               CDC Events
      ↓                           ↓
  Bronze Layer ← ─ ─ ─ ─ ─ ─ Bronze Layer
      ↓                           ↓
  SCD Type 2 Merge ← ─ ─ ─ SCD Type 2 Merge
      ↓                           ↓
  Gold Dimensions    →    Gold Dimensions
```

---

### Pattern 4: Multi-Source Data Integration
**Use case**: Combine data from multiple heterogeneous sources

**Components**:
1. **Ingestion** (pipeline-ingestion.md): Dynamic ingestion for N sources
2. **Transformation** (pipeline-transformation.md): Standardization and joining
3. **Orchestration** (pipeline-orchestration.md): Dynamic task generation
4. **Observability** (pipeline-observability.md): Per-source monitoring
5. **Infrastructure** (pipeline-infrastructure.md): Resource pools per source type

**Workflow**:
```
Dynamic Task Generation:
  For each source in [CRM, ERP, Web, Mobile]:
    ↓
  Extract in parallel
    ↓
  Validate independently
    ↓
  Load to Bronze (separate tables)
    ↓
  Join on common keys (Silver)
    ↓
  Create unified view (Gold)
```

---

## Technology Selection Guide

### Orchestration Platform
| **Platform** | **Best For** | **See Section** |
|--------------|-------------|----------------|
| **Apache Airflow** | Python-centric workflows, complex dependencies | pipeline-orchestration.md |
| **Prefect** | Modern Python workflows, dynamic pipelines | pipeline-orchestration.md |
| **Dagster** | Software-defined assets, data-aware orchestration | pipeline-orchestration.md |
| **Azure Data Factory** | Azure-native, low-code GUI workflows | pipeline-orchestration.md |
| **AWS Step Functions** | AWS serverless, event-driven workflows | pipeline-orchestration.md |

### Processing Framework
| **Framework** | **Best For** | **See Section** |
|--------------|-------------|----------------|
| **Apache Spark** | Large-scale distributed processing (> 1TB) | pipeline-transformation.md, pipeline-infrastructure.md |
| **Pandas/Dask** | Medium-scale Python processing (< 100GB) | pipeline-transformation.md |
| **DBT** | SQL-based transformations in warehouse | pipeline-transformation.md |
| **Apache Flink** | Real-time streaming with stateful processing | pipeline-ingestion.md |
| **Kafka Streams** | Lightweight streaming transformations | pipeline-ingestion.md |

### Storage Architecture
| **Pattern** | **Best For** | **See Section** |
|------------|-------------|----------------|
| **Delta Lake** | ACID transactions, time travel, schema evolution | pipeline-transformation.md |
| **Apache Iceberg** | Large-scale analytics, partition evolution | pipeline-transformation.md |
| **Parquet** | Columnar storage, read-heavy analytics | pipeline-infrastructure.md |
| **Avro** | Schema evolution, streaming serialization | pipeline-ingestion.md |

### Cloud Provider
| **Provider** | **Strengths** | **See Section** |
|--------------|--------------|----------------|
| **AWS** | Mature data services (S3, EMR, Glue, Redshift) | pipeline-infrastructure.md |
| **Azure** | Enterprise integration (Synapse, Data Factory) | pipeline-infrastructure.md |
| **GCP** | BigQuery, Dataflow, real-time analytics | pipeline-infrastructure.md |
| **Multi-cloud** | Avoid vendor lock-in, use best-of-breed | All sections |

---

## Common Pipeline Patterns

### 1. Medallion Architecture (Bronze → Silver → Gold)
- **Bronze**: Raw ingested data, minimal transformation
- **Silver**: Cleansed, validated, standardized data
- **Gold**: Business-ready, aggregated, optimized for consumption
- **See**: pipeline-transformation.md

### 2. Lambda Architecture
- **Batch Layer**: Historical data processing
- **Speed Layer**: Real-time stream processing
- **Serving Layer**: Merged view of batch + streaming
- **See**: pipeline-ingestion.md, pipeline-transformation.md

### 3. Kappa Architecture
- **Single streaming pipeline**: All data treated as unbounded stream
- **Reprocessing**: Replay stream from start for recalculation
- **See**: pipeline-ingestion.md (Streaming section)

### 4. Data Vault
- **Hubs**: Business entities (Customer, Product)
- **Links**: Relationships between entities
- **Satellites**: Temporal and descriptive attributes
- **See**: pipeline-transformation.md (SCD section)

---

## Getting Started Checklist

### Phase 1: Planning (Week 1)
- [ ] Define business requirements and SLAs
- [ ] Identify all data sources and targets
- [ ] Select orchestration platform and processing framework
- [ ] Design pipeline architecture (batch/streaming/hybrid)
- [ ] Define data quality requirements
- [ ] Choose cloud provider and infrastructure approach

### Phase 2: Ingestion (Week 2-3)
- [ ] Implement source connectors (pipeline-ingestion.md)
- [ ] Set up extraction scheduling
- [ ] Configure error handling and retries
- [ ] Implement data validation at ingestion
- [ ] Set up extraction metadata tracking
- [ ] Test with sample data from each source

### Phase 3: Transformation (Week 4-5)
- [ ] Design medallion architecture (Bronze/Silver/Gold)
- [ ] Implement cleansing and standardization logic (pipeline-transformation.md)
- [ ] Build business logic transformations
- [ ] Add data quality checks between layers
- [ ] Implement SCD Type 2 if needed
- [ ] Set up data lineage tracking

### Phase 4: Orchestration (Week 6)
- [ ] Create DAG with task dependencies (pipeline-orchestration.md)
- [ ] Configure retry logic and timeouts
- [ ] Set up resource pools
- [ ] Implement dynamic task generation if needed
- [ ] Configure SLA monitoring
- [ ] Test backfill scenarios

### Phase 5: Observability (Week 7)
- [ ] Set up metrics collection (pipeline-observability.md)
- [ ] Create operational dashboards
- [ ] Configure alerting rules
- [ ] Implement error handling framework
- [ ] Set up dead letter queues
- [ ] Create runbooks for common issues

### Phase 6: Infrastructure (Week 8)
- [ ] Write Terraform/IaC configurations (pipeline-infrastructure.md)
- [ ] Set up auto-scaling policies
- [ ] Configure high availability
- [ ] Implement backup and disaster recovery
- [ ] Optimize resource allocation
- [ ] Set up cost monitoring

### Phase 7: Testing & Deployment (Week 9-10)
- [ ] Unit test individual transformations
- [ ] Integration test end-to-end pipeline
- [ ] Performance test with production-scale data
- [ ] Security and compliance review
- [ ] Documentation and knowledge transfer
- [ ] Production deployment and monitoring

---

## Best Practices Summary

### Design Principles
1. **Idempotency**: Ensure reruns produce same results
2. **Incremental processing**: Process only new/changed data
3. **Data quality gates**: Validate at each layer boundary
4. **Observability first**: Build monitoring from the start
5. **Fail fast**: Detect issues early in the pipeline
6. **Graceful degradation**: Continue with partial data when possible

### Operational Excellence
1. **Version control**: Track all code and infrastructure changes
2. **Automated testing**: Test transformations and infrastructure
3. **Clear ownership**: Assign teams to pipeline components
4. **Documentation**: Maintain architecture diagrams and runbooks
5. **Incident response**: Define procedures for common failure modes
6. **Continuous improvement**: Regular performance and cost reviews

### Security & Compliance
1. **Encryption**: At rest and in transit
2. **Least privilege**: Minimal permissions for each component
3. **Audit logging**: Track all data access and modifications
4. **Data masking**: Protect sensitive data (PII, PHI)
5. **Compliance**: GDPR, HIPAA, SOC 2 as required
6. **Secret management**: Use vault services, never hardcode

---

## Related Resources

### Internal Templates
- **data-governance-framework.md**: Data quality rules and governance
- **dashboard-design-patterns.md**: Consuming pipeline outputs in dashboards
- **predictive-modeling-framework.md**: ML pipelines and feature engineering

### External Documentation
- Apache Airflow: https://airflow.apache.org/docs/
- Terraform: https://developer.hashicorp.com/terraform/docs
- Kubernetes: https://kubernetes.io/docs/
- Delta Lake: https://docs.delta.io/
- Apache Spark: https://spark.apache.org/docs/

---

## Usage Examples

### Example 1: E-commerce Daily Sales Pipeline

**Context:** E-commerce company needs daily batch pipeline from PostgreSQL to Snowflake

**Copy-paste this prompt:**

```
I need to build an end-to-end data pipeline for e-commerce sales analytics.

PIPELINE CONTEXT:
- Source systems: PostgreSQL (orders, customers, products), Stripe API (payments), Google Analytics (web traffic)
- Target: Snowflake data warehouse for BI dashboards
- Pipeline type: Daily batch processing with incremental loads
- Data volume: 5M orders/month, 100GB total, 2GB daily incremental
- SLA: Data ready by 6 AM for business users

ARCHITECTURE REQUIREMENTS:
Medallion Architecture:
- Bronze: Raw extracts with source metadata (extracted_at, source_system)
- Silver: Cleaned, deduplicated, validated data with referential integrity
- Gold: Business metrics (daily sales, customer LTV, product performance)

SPECIFIC PIPELINE COMPONENTS:
1. Ingestion (pipeline-ingestion.md pattern):
   - PostgreSQL: Incremental by updated_at timestamp
   - Stripe: API pagination with cursor-based extraction
   - GA: BigQuery export to S3

2. Transformation (pipeline-transformation.md pattern):
   - Bronze to Silver: Remove duplicates, validate order amounts > 0, standardize timestamps to UTC
   - Silver to Gold: Calculate order_total, apply refund logic, join customer segments

3. Orchestration (pipeline-orchestration.md pattern):
   - Airflow DAG: extract (parallel) → load_bronze → transform_silver → transform_gold → notify
   - Schedule: Daily at 2 AM UTC
   - Dependencies: All extracts complete before bronze load

4. Observability (pipeline-observability.md pattern):
   - Monitor: Row counts, extract duration, transformation errors
   - Alert: Data freshness > 30 minutes late, row count variance > 10%
   - Dashboard: Pipeline health in Grafana

Please provide:
1. Complete Airflow DAG code with task dependencies
2. dbt models for Bronze → Silver → Gold transformations
3. Data quality checks between each layer
4. Monitoring queries for pipeline health
```

**Expected Output:**
- Airflow DAG with 8-10 tasks, parallel extraction, sequential transformation
- dbt models with incremental materialization strategy
- Great Expectations or dbt tests for data quality
- Alerting thresholds and notification channels

---

### Example 2: Real-time Clickstream Pipeline

**Context:** Media company needs real-time user behavior analytics for personalization

**Copy-paste this prompt:**

```
I need to build a real-time streaming pipeline for clickstream analytics.

PIPELINE CONTEXT:
- Source: Segment.io events via Kafka (page views, clicks, video plays)
- Target: Pinot for real-time dashboards, S3 + Spark for batch analytics
- Pipeline type: Real-time streaming with 5-second latency SLA
- Data volume: 50,000 events/second peak, 2B events/day
- Use case: Real-time content recommendations, audience segmentation

ARCHITECTURE REQUIREMENTS:
Streaming Architecture:
- Ingestion: Kafka with 3-day retention, 48 partitions
- Processing: Kafka Streams for sessionization, Flink for complex aggregations
- Serving: Pinot for real-time queries, Delta Lake for historical analysis

SPECIFIC PIPELINE COMPONENTS:
1. Ingestion (pipeline-ingestion.md streaming pattern):
   - Kafka consumer with exactly-once semantics
   - Schema registry for event schema evolution (Avro)
   - Dead letter queue for malformed events

2. Transformation (pipeline-transformation.md streaming pattern):
   - Session windowing: 30-minute inactivity timeout
   - User stitching: Connect anonymous to authenticated events
   - Real-time aggregations: Page views per minute, trending content

3. Orchestration (pipeline-orchestration.md for monitoring):
   - No scheduling needed (continuous streaming)
   - Airflow for daily reconciliation jobs and backfill
   - Health check DAG every 15 minutes

4. Observability (pipeline-observability.md streaming pattern):
   - Monitor: Consumer lag, processing latency, throughput
   - Alert: Lag > 10,000 messages, latency > 5 seconds
   - Dashboard: Kafka lag, Flink checkpoints, Pinot query latency

Please provide:
1. Kafka topic design (partitioning strategy, retention, compaction)
2. Flink job for session windowing and user stitching
3. Schema evolution strategy for backward compatibility
4. Consumer lag monitoring and auto-scaling
```

**Expected Output:**
- Kafka partition key strategy (user_id for ordering)
- Flink session window implementation
- Avro schema with compatibility rules
- HPA configuration for consumer scaling

---

### Example 3: Multi-Source Financial Pipeline

**Context:** Finance team needs consolidated financial data from multiple ERPs post-merger

**Copy-paste this prompt:**

```
I need to build a data integration pipeline consolidating financial data from two ERP systems.

PIPELINE CONTEXT:
- Source systems: SAP S/4HANA (legacy company), Oracle EBS (acquired company)
- Target: Snowflake for unified financial reporting
- Pipeline type: Daily batch with monthly close support
- Data volume: 50M GL entries/year combined, 500GB total
- Compliance: SOX controls, full audit trail required

ARCHITECTURE REQUIREMENTS:
Integration Architecture:
- Common data model: Unified chart of accounts, standardized cost centers
- Data quality: Cross-system reconciliation, balance validation
- Audit: Full lineage from source to report, change tracking

SPECIFIC PIPELINE COMPONENTS:
1. Ingestion (pipeline-ingestion.md pattern):
   - SAP: CDS views extraction via OData, incremental by posting date
   - Oracle: Direct SQL extraction with read replica, incremental by last_update_date
   - Both: Full extract monthly for reconciliation

2. Transformation (pipeline-transformation.md pattern):
   - Bronze: Raw extracts with source system identifier
   - Silver:
     - Map SAP account codes to unified chart of accounts
     - Map Oracle account codes to same unified chart
     - Standardize dates to fiscal calendar
     - Convert currencies to USD using daily rates
   - Gold:
     - Consolidated trial balance
     - P&L by business unit (combined)
     - Balance sheet by entity

3. Orchestration (pipeline-orchestration.md pattern):
   - Airflow DAG: Parallel extract → transform in sequence → reconcile → approve
   - Schedule: Daily at midnight, monthly close job on day 3
   - Human-in-the-loop: Reconciliation variance > $1000 requires approval

4. Observability (pipeline-observability.md pattern):
   - Monitor: GL balance totals, cross-system variance
   - Alert: SAP vs Oracle debits don't match, TB out of balance
   - Audit: Log every record source, transformation, and load timestamp

Please provide:
1. Unified chart of accounts mapping strategy
2. Multi-source ETL with common data model
3. Cross-system reconciliation checks
4. Monthly close workflow with approval gates
5. SOX-compliant audit logging
```

**Expected Output:**
- Account mapping table design
- dbt models with source tagging for lineage
- Reconciliation queries with variance thresholds
- Airflow sensor for manual approval step

---

## Support & Contribution

For questions or improvements to these templates:
1. Review the specific sub-prompt for detailed implementation guidance
2. Check the Usage Examples section in each sub-prompt
3. Consult the Best Practices and Tips for Success sections
4. Refer to the technology-specific documentation links

**Remember**: Start with the simplest approach that meets your requirements. You can always add complexity later as needs evolve.
