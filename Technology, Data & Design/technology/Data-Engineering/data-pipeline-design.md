---
category: technology
related_templates:
- technology/Data-Engineering/data-infrastructure-as-code.md
- data-analytics/Analytics-Engineering/pipeline-development.md
- data-analytics/Analytics-Engineering/pipeline-orchestration.md
tags:
- data-engineering
- data-pipelines
- etl
- batch-streaming
title: Data Pipeline Design
use_cases:
- Designing batch, streaming, and hybrid data pipelines processing TB-scale data with latency SLAs from real-time to daily batch windows
- Implementing medallion architecture (bronze/silver/gold) with data quality gates, schema evolution handling, and backfill capabilities
- Building fault-tolerant pipelines with idempotent processing, dead letter queues, and automated recovery for production data systems
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: data-pipeline-design
---

# Data Pipeline Design

## Purpose
Design comprehensive data pipelines covering ingestion patterns, transformation logic, quality frameworks, and operational concerns achieving reliable data flow from sources to analytics with defined latency SLAs and quality guarantees.

## 🚀 Quick Pipeline Design Prompt

> Design **[BATCH/STREAMING/HYBRID]** pipeline for **[USE_CASE]**. Sources: **[DATABASES/APIS/EVENTS]** at **[VOLUME]** daily. Latency: **[REAL_TIME/HOURLY/DAILY]**. Architecture: ingest → **[BRONZE/SILVER/GOLD]**. Stack: **[AIRFLOW/DAGSTER]** orchestrator, **[SPARK/DBT/FLINK]** processing, **[WAREHOUSE/LAKE]** storage. Include: schema evolution, idempotency, backfill support, **[QUALITY_CHECKS]**, monitoring (freshness, row counts, anomalies). SLA: **[REQUIREMENTS]**.

---

## Template

Design data pipeline for {USE_CASE} processing {DATA_VOLUME} from {SOURCE_SYSTEMS} with {LATENCY_SLA} latency achieving {QUALITY_TARGET}% data quality.

**PIPELINE ARCHITECTURE PATTERNS**

Choose processing pattern matching latency requirements and data characteristics. Batch processing: daily/hourly schedules, suitable for analytics workloads where freshness SLA allows hours, most cost-effective, simpler operations. Streaming processing: real-time or near-real-time (<1 minute), required for operational use cases (fraud detection, recommendations), higher complexity and cost. Hybrid (Lambda): batch for historical accuracy, streaming for real-time updates, eventual consistency between layers. Hybrid (Kappa): streaming-first with replay capability, single processing path, simpler architecture but requires robust stream storage.

Design medallion architecture for progressive data refinement. Bronze layer (raw): exact copy of source data, append-only, partitioned by ingestion timestamp, retain 30-90 days for reprocessing. Silver layer (cleaned): schema validated, deduplicated, standardized formats, enriched with reference data, partitioned by event date. Gold layer (business): aggregated metrics, denormalized for consumption, optimized for query patterns, business logic applied. Layer transitions: bronze→silver handles data quality, silver→gold handles business logic, clear ownership per layer.

Select technology stack matching scale and team expertise. Batch orchestration: Airflow (mature, large community), Dagster (modern, asset-centric), Prefect (Pythonic, cloud-native). Stream processing: Kafka Streams (JVM, stateful), Flink (exactly-once, complex event processing), Spark Structured Streaming (unified batch/stream). Transformation: Spark (large-scale, complex), dbt (SQL-first, incremental), Pandas (small-scale, prototyping). Storage: Delta Lake (ACID, time travel), Iceberg (open format, catalog), Parquet files (simple, universal).

**DATA INGESTION STRATEGIES**

Implement batch ingestion for periodic data loads. Full load: simplest, entire dataset each run, suitable for small tables (<1M rows) or dimension tables changing frequently. Incremental load: only new/changed records since last run, requires watermark column (updated_at, created_at), significantly faster. Snapshot with delta: periodic full snapshots plus incremental deltas between snapshots, balance freshness and cost. Schedule optimization: align with source system maintenance windows, avoid business hours for heavy loads, stagger multiple sources.

Configure CDC for low-latency database replication. Log-based CDC: read database transaction logs (Debezium, AWS DMS), minimal source impact, capture all changes including deletes. Query-based CDC: poll source for changes (high-watermark queries), simpler setup but may miss deletes and intermediate states. Hybrid approach: CDC for real-time, periodic full reconciliation for accuracy. Schema evolution: schema registry for version management, compatibility checks (backward, forward), migration strategies for breaking changes.

Handle streaming ingestion for event data. Kafka ingestion: topics per domain, partition by entity key for ordering, retention 7-30 days for replay. Event format: Avro/Protobuf with schema registry, JSON for flexibility with explicit schema validation. Exactly-once semantics: idempotent producers, consumer offset management, transactional writes to sinks. Backpressure handling: consumer lag monitoring, auto-scaling consumers, circuit breakers for downstream failures.

**TRANSFORMATION PATTERNS**

Implement data cleansing as first transformation step. Deduplication: identify natural keys, define dedup strategy (first, last, merge), handle late-arriving duplicates. Missing value handling: default values for dimensions, interpolation for time series, null propagation rules. Format standardization: date formats to ISO 8601, string normalization (trim, case), unit conversions. Type coercion: explicit casting with error handling, schema validation before processing.

Design enrichment and derivation logic. Dimensional enrichment: join with reference data (customer, product, geography), handle missing dimension keys (unknown dimension record). Derived columns: calculated fields, business rules, feature engineering. Window operations: running totals, moving averages, rank/row_number. Temporal handling: event time vs processing time, late arrival windows, watermarks for streaming.

Build aggregation layers for analytics. Pre-aggregated tables: common query patterns (daily/weekly/monthly rollups), reduce query cost and latency. Dimensional modeling: fact tables with foreign keys, conformed dimensions, star schema for BI tools. Incremental aggregation: update aggregates with new data only, merge logic for late arrivals. Materialized views: auto-refresh on source changes, query acceleration, managed by warehouse.

**DATA QUALITY FRAMEWORK**

Implement quality checks at pipeline boundaries. Input quality: schema validation, required fields present, value ranges, referential integrity. Processing quality: row count reconciliation (input vs output), no data loss during transformation. Output quality: business rules satisfied, aggregation correctness, temporal consistency. Quality dimensions: completeness (nulls), accuracy (valid values), consistency (across sources), timeliness (freshness).

Configure data quality tooling. Great Expectations: Python-based, rich expectation library, data docs for documentation. dbt tests: SQL-based, integrated with transformations, severity levels. Monte Carlo/Bigeye: ML-based anomaly detection, automated monitoring, incident management. Custom checks: business-specific validation, threshold alerting, trend analysis.

Handle quality failures appropriately. Fail-fast: stop pipeline on critical failures, prevent bad data propagation. Quarantine: isolate failing records, continue processing good data, manual review queue. Alert and continue: log warnings, send notifications, flag records for downstream awareness. Severity levels: critical (stop), major (quarantine), minor (flag), info (log only).

**ORCHESTRATION AND SCHEDULING**

Design DAG structure for maintainability. Task granularity: one task per logical operation, avoid monolithic tasks, enable partial reruns. Dependencies: explicit task dependencies, sensor for external dependencies, cross-DAG dependencies via datasets (Airflow 2.4+). Idempotency: tasks produce same result on rerun, partition-based processing, upsert logic for updates.

Configure scheduling and SLA management. Schedule alignment: coordinate with source availability, allow buffer for upstream delays. SLA monitoring: define expected completion times, alert on SLA breach, track historical trends. Catchup strategy: enable for backfill scenarios, disable for real-time, bounded catchup to prevent queue buildup.

Implement backfill and reprocessing capability. Partition-based reprocessing: rerun specific date partitions, clear and rebuild pattern. Full historical rebuild: process entire history, staged rollout (shadow tables first). Incremental rebuild: process only affected records, merge with existing data. Backfill prioritization: recent data first, older data in background, resource limits.

**ERROR HANDLING AND RECOVERY**

Design retry strategies for transient failures. Exponential backoff: 1min → 2min → 4min → 8min delays, max 3-5 retries. Retry scope: retry failed task only, not entire DAG, checkpointing for long tasks. Timeout handling: set appropriate timeouts per task, kill hung processes, cleanup partial outputs.

Implement dead letter queues for data errors. Record-level failures: capture failing records with error details, source metadata, timestamp. Reprocessing workflow: review queue, fix data or logic, replay to main pipeline. Retention policy: 30-day retention, archive for compliance, alerting on queue growth.

Build recovery procedures for major failures. Checkpoint and resume: save progress in streaming jobs, resume from last checkpoint. State reconstruction: rebuild state from source of truth, validate consistency. Incident runbooks: documented recovery procedures, tested regularly, ownership defined.

**MONITORING AND OBSERVABILITY**

Track pipeline health metrics. Operational metrics: task duration, success/failure rates, resource utilization, queue depths. Data metrics: row counts by partition, data volume (bytes), record freshness (max event time). Quality metrics: test pass rate, null percentage, anomaly score, SLI compliance.

Configure alerting for proactive issue detection. Freshness alerts: data older than threshold, pipeline delayed, source lag. Volume alerts: row count anomalies (±50% from baseline), unexpected empty tables. Quality alerts: test failures, validation errors, schema changes detected. Resource alerts: job memory/CPU spikes, storage growth, cost anomalies.

Build operational dashboards for visibility. Pipeline status: DAG status, recent failures, SLA tracking. Data quality: quality score trends, top failing tests, quarantine queue size. Lineage and catalog: source to target mapping, data dictionary, usage statistics.

Deliver data pipeline design as:

1. **ARCHITECTURE DIAGRAM** - End-to-end data flow showing sources, processing stages, storage layers, consumers

2. **INGESTION SPECIFICATION** - Per-source configuration (method, schedule, format, schema), CDC setup

3. **TRANSFORMATION LOGIC** - Stage-by-stage transformations (cleanse, enrich, aggregate), business rules

4. **DATA QUALITY RULES** - Quality checks per layer, severity levels, handling strategies

5. **ORCHESTRATION DESIGN** - DAG structure, scheduling, dependencies, backfill procedures

6. **ERROR HANDLING** - Retry policies, dead letter queues, recovery procedures

7. **MONITORING SETUP** - Metrics, alerts, dashboards, SLA tracking

---

## Usage Examples

### Example 1: E-commerce Analytics Pipeline
**Prompt:** Design hybrid pipeline for EcommerceAnalytics processing orders (10M/day), clickstream (500M events/day), and inventory updates from MySQL, Kafka, and ERP API with 2-hour latency SLA.

**Expected Output:** Architecture: Kafka for clickstream (real-time), Debezium CDC for MySQL orders (5-minute lag), daily batch from ERP API. Medallion layers: Bronze (S3 Parquet, raw events partitioned by hour), Silver (Delta Lake, deduplicated orders with customer enrichment, sessionized clicks), Gold (aggregated daily metrics, customer lifetime value, product performance). Processing: Spark Structured Streaming for click aggregation, Spark batch for order processing, dbt for Gold layer transformations. Orchestration: Dagster with asset-based DAG, hourly incremental for orders, daily full for ERP, continuous for streaming aggregates. Quality: Great Expectations on Silver (row counts ±10%, required fields 100%, amount > 0), dbt tests on Gold (metric reconciliation). Error handling: Kafka DLQ for malformed events, retry 3x with backoff for API failures, quarantine invalid orders for manual review. Monitoring: Grafana dashboards (pipeline status, data freshness, quality scores), PagerDuty alerts on SLA breach (>2 hour freshness). SLA: 95th percentile end-to-end latency <90 minutes.

### Example 2: Financial Reporting Pipeline
**Prompt:** Design batch pipeline for FinanceReporting processing general ledger, AP/AR, and bank transactions from Oracle, SAP, and bank files with daily 6 AM deadline and SOX compliance.

**Expected Output:** Architecture: daily batch, sequential source processing (GL first, then AP/AR joins, finally bank reconciliation). Medallion layers: Bronze (encrypted S3, full daily snapshots, 7-year retention), Silver (validated transactions, standardized chart of accounts, currency converted), Gold (trial balance, P&L, balance sheet, regulatory reports). Processing: Spark for large GL tables (50M rows), dbt for financial calculations and report generation. Ingestion: JDBC batch extract at 1 AM (GL), SFTP file ingestion at 2 AM (bank files), API pull at 2:30 AM (SAP). Quality: mandatory reconciliation (GL debits = credits, bank statement matches), threshold alerts (>1% variance), audit trail for all transformations. Orchestration: Airflow with strict SLA (6 AM completion), sensor for source availability, no automatic retry (manual approval required). Compliance: encryption at rest (KMS), access logging (CloudTrail), immutable Bronze layer, change data capture for audit. Error handling: fail entire DAG on reconciliation failure, notify finance team, checkpoint before each major stage. Monitoring: Tableau dashboard for finance team (report status, reconciliation results), email alerts to controller on completion/failure.

### Example 3: Real-time Fraud Detection Pipeline
**Prompt:** Design streaming pipeline for FraudDetection processing payment transactions (50K TPS peak) with <500ms latency for ML scoring and real-time decisioning.

**Expected Output:** Architecture: pure streaming (Kappa), Kafka → Flink → feature store + ML scoring → decision service. Ingestion: Kafka with 100 partitions (partition by customer_id for ordering), Avro with schema registry, exactly-once semantics. Processing: Flink stateful processing for feature computation (velocity features, aggregates), 1-minute tumbling windows for aggregations, customer state in RocksDB. Feature store: Redis for real-time features (<5ms lookup), periodic sync to offline store for model training. ML integration: model served via TensorFlow Serving, <50ms inference, A/B testing for model versions. Decisioning: rules engine for deterministic rules, ML score threshold for automation, manual review queue for edge cases. Quality: schema validation at ingestion, feature drift monitoring, model performance tracking (precision/recall). Error handling: DLQ for invalid transactions (continue processing valid), circuit breaker on ML service failure (fallback to rules), replay capability from Kafka. Monitoring: real-time dashboard (TPS, latency percentiles, fraud rate, false positive rate), alert on latency >500ms or fraud rate anomaly. Latency budget: ingestion 50ms, feature compute 200ms, ML scoring 100ms, decisioning 50ms, buffer 100ms.

---

## Cross-References

- [Data Infrastructure as Code](data-infrastructure-as-code.md) - Infrastructure provisioning for data pipelines
- [Pipeline Development](../../data-analytics/Analytics-Engineering/pipeline-development.md) - Detailed pipeline implementation patterns
- [Pipeline Orchestration](../../data-analytics/Analytics-Engineering/pipeline-orchestration.md) - Airflow/Dagster orchestration patterns
