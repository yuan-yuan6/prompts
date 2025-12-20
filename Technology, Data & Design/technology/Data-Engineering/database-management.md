---
category: technology
related_templates:
- technology/Data-Engineering/data-infrastructure-as-code.md
- technology/DevOps-Cloud/cloud-architecture.md
- data-analytics/Analytics-Engineering/query-optimization.md
tags:
- database-management
- schema-design
- query-optimization
- backup-recovery
title: Database Management
use_cases:
- Designing production database schemas with proper normalization, indexing strategies, and performance optimization achieving <100ms query latency at scale
- Implementing high availability with replication, automatic failover, and disaster recovery achieving 99.99% uptime with <15 minute RTO
- Managing database operations including backup/recovery, security hardening, maintenance automation, and capacity planning for enterprise workloads
industries:
- technology
- financial-services
- healthcare
- retail
type: framework
difficulty: intermediate
slug: database-management
---

# Database Management

## Purpose
Comprehensive database management covering schema design, query optimization, high availability, backup/recovery, security, and operational excellence achieving production-grade reliability for enterprise database systems.

## Template

Design database management for {DATABASE_TYPE} supporting {APPLICATION_TYPE} with {SCALE_REQUIREMENTS} achieving {PERFORMANCE_TARGET} latency and {AVAILABILITY_TARGET}% availability.

**SCHEMA DESIGN**

Design schema balancing normalization with query performance. Third normal form (3NF): eliminate redundancy for transactional systems, maintain data integrity, easier updates. Denormalization: strategic redundancy for read-heavy workloads, pre-computed aggregates, materialized views for analytics. Document model: embed related data for single-query access patterns (MongoDB), balance document size vs update frequency. Hybrid approach: normalized core entities, denormalized read models, event sourcing for audit trails.

Define data types optimizing storage and query performance. Numeric types: INT for counts/IDs (4 bytes), BIGINT for large sequences, DECIMAL for financial precision (avoid float). String types: VARCHAR for variable-length (set reasonable max), TEXT for unbounded, avoid CHAR padding. Date/time: TIMESTAMP WITH TIMEZONE for events, DATE for calendar dates, avoid timezone-naive timestamps. JSON/JSONB: flexible attributes, schema-on-read, but index carefully (GIN indexes expensive to maintain).

Design keys and constraints for data integrity. Primary keys: UUID for distributed systems (no coordination needed), BIGSERIAL for single-node (compact, fast). Foreign keys: enforce referential integrity, choose ON DELETE behavior (CASCADE, RESTRICT, SET NULL). Unique constraints: enforce business rules, consider partial unique indexes for conditional uniqueness. Check constraints: validate data at database level, complement application validation.

**INDEXING STRATEGIES**

Create indexes based on query patterns. B-tree indexes: equality and range queries, most common type, ordered access. Hash indexes: equality-only queries (PostgreSQL), faster than B-tree for exact matches. GIN indexes: full-text search, JSONB containment, array operations (expensive to maintain). GiST indexes: geometric data, range types, full-text with weights.

Design composite indexes for multi-column queries. Column order matters: most selective column first for equality, range column last. Covering indexes: include all SELECT columns, enable index-only scans, avoid heap access. Partial indexes: index subset of rows (WHERE active = true), smaller and faster. Expression indexes: index computed values (LOWER(email)), enable optimized lookups.

Maintain indexes for optimal performance. Monitor index usage: pg_stat_user_indexes, remove unused indexes (write overhead without benefit). Detect bloat: pg_stat_user_tables dead tuples, REINDEX during maintenance windows. Statistics updates: ANALYZE regularly (auto-analyze handles most cases), manual for large batch loads. Index-only scan ratio: monitor in pg_stat_user_indexes, high ratio indicates good covering indexes.

**QUERY OPTIMIZATION**

Analyze query plans for performance issues. EXPLAIN ANALYZE: actual execution times, row estimates vs actuals, identify misestimates. Sequential scans: acceptable for small tables (<10K rows), investigate for large tables. Nested loops: efficient for small outer tables, problematic at scale. Hash joins: good for large tables without indexes, memory-intensive. Sort operations: expensive for large datasets, consider indexes for ORDER BY.

Optimize common query patterns. Pagination: keyset pagination (WHERE id > last_id) over OFFSET (OFFSET scans all rows). Aggregations: pre-compute in materialized views, incremental updates where possible. JOINs: ensure join columns indexed, consider denormalization for hot paths. Subqueries: rewrite as JOINs when possible, CTEs for readability (not always faster).

Configure query-level settings. Statement timeout: prevent runaway queries (SET statement_timeout = '30s'). Work memory: increase for complex sorts/hashes (work_mem per operation, not per query). Parallel query: enable for analytical queries (max_parallel_workers_per_gather). Prepared statements: reduce parsing overhead, enable plan caching.

**HIGH AVAILABILITY**

Design replication topology for availability requirements. Streaming replication (PostgreSQL): primary → replicas via WAL, synchronous for zero data loss, async for performance. Group replication (MySQL): multi-primary with conflict resolution, automatic failover. Replica sets (MongoDB): primary election via consensus, automatic failover, read preference configuration. Read replicas: offload read traffic, analytics queries, geographic distribution.

Configure automatic failover for minimal downtime. Patroni (PostgreSQL): etcd-based consensus, automatic leader election, <30 second failover. Orchestrator (MySQL): topology management, automated failover, web UI for operations. Connection routing: HAProxy/PgBouncer for connection routing, DNS-based failover for applications. Split-brain prevention: fencing (STONITH), quorum requirements, witness nodes.

Plan disaster recovery for regional failures. Cross-region replication: async replication to DR region (accept some data loss for latency). Pilot light DR: minimal infrastructure in DR region, scale up on activation. Warm standby: replicated infrastructure, faster activation, higher cost. RTO/RPO targets: document and test regularly, align with business requirements.

**BACKUP AND RECOVERY**

Implement backup strategy matching recovery requirements. Full backups: weekly for large databases, daily for critical systems, pg_basebackup/xtrabackup. Incremental backups: WAL archiving (PostgreSQL), binlog shipping (MySQL), reduce storage and time. Logical backups: pg_dump for portability, slower restore, schema migration flexibility. Snapshots: cloud provider snapshots, fast but vendor-locked, combine with WAL for point-in-time.

Configure point-in-time recovery capability. WAL archiving: continuous archiving to S3/GCS, enable PITR to any point. Retention: 7 days for operational recovery, 30 days for compliance, archive to cold storage. Recovery testing: monthly restore tests, measure actual RTO, validate data integrity. Backup verification: automated checksum validation, sample query verification.

Automate backup operations. Scheduling: cron or orchestrator-based (Kubernetes CronJob), multiple backup windows. Monitoring: backup success/failure alerts, backup size trends, storage utilization. Retention management: automated deletion of expired backups, compliance-aware retention. Documentation: runbook for restore procedures, tested and updated regularly.

**SECURITY HARDENING**

Implement authentication and access control. Authentication: SCRAM-SHA-256 (PostgreSQL), caching_sha2_password (MySQL), certificate-based for services. Role-based access: least privilege principle, separate roles for app/analytics/admin. Row-level security: tenant isolation, data classification enforcement. Audit logging: log all DDL, log DML for sensitive tables, pgAudit/MySQL Audit Plugin.

Configure network security. Private networking: no public IP, VPC-only access, private endpoints. Encryption in transit: TLS 1.2+ required, verify server certificates. Connection limits: max connections per user/database, rate limiting at proxy. IP allowlisting: restrict to known application IPs, bastion for admin access.

Protect data at rest. Encryption at rest: TDE (Transparent Data Encryption), cloud provider KMS integration. Column-level encryption: application-level for highly sensitive data (SSN, card numbers). Key management: regular rotation, separate keys per environment, HSM for compliance. Data masking: mask PII in non-production environments, dynamic masking for analytics.

**MAINTENANCE OPERATIONS**

Automate routine maintenance tasks. VACUUM (PostgreSQL): autovacuum handles most cases, tune for high-write tables. ANALYZE: update statistics after large data changes, enable auto-analyze. Index maintenance: REINDEX for bloated indexes, rebuild during low-traffic windows. Integrity checks: pg_amcheck for corruption detection, schedule weekly.

Manage storage growth and archival. Partitioning: range partition by date, detach and archive old partitions. Data lifecycle: identify cold data, move to cheaper storage tiers. Purging: implement retention policies, soft-delete with scheduled hard-delete. Storage alerts: 80% threshold warning, 90% critical, automatic scaling where possible.

Plan maintenance windows. Change windows: defined low-traffic periods, communicated to stakeholders. Rolling upgrades: replica-first, promote, repeat (minimize downtime). Schema migrations: backward-compatible changes, blue-green for breaking changes. Rollback planning: tested rollback procedures for all changes.

**MONITORING AND OBSERVABILITY**

Track database health metrics. Connection metrics: active/idle connections, connection pool utilization, waiting connections. Query metrics: queries per second, average latency, p95/p99 latency, slow query count. Resource metrics: CPU, memory, disk I/O, storage usage, replication lag. Lock metrics: lock waits, deadlocks, blocking queries.

Configure alerting for proactive issue detection. Availability: connection failures, replication failures, failover events. Performance: query latency exceeding threshold, connection pool exhaustion. Capacity: disk usage >80%, connection count >80% of max. Security: authentication failures, privilege escalation, unusual query patterns.

Build operational dashboards. Overview dashboard: cluster health, key metrics, recent events. Query performance: slow queries, query patterns, index usage. Replication: lag trends, sync status, failover history. Capacity: storage trends, growth projections, cost allocation.

Deliver database management as:

1. **SCHEMA DESIGN** - Entity definitions, relationships, constraints, indexing strategy

2. **PERFORMANCE CONFIGURATION** - Query optimization, connection pooling, caching, resource tuning

3. **HIGH AVAILABILITY** - Replication topology, failover configuration, split-brain prevention

4. **BACKUP/RECOVERY** - Backup schedule, retention policy, PITR configuration, restore procedures

5. **SECURITY CONTROLS** - Authentication, authorization, encryption, audit logging

6. **MAINTENANCE PROCEDURES** - Automated tasks, maintenance windows, upgrade procedures

7. **MONITORING SETUP** - Metrics collection, alerting rules, operational dashboards

---

## Usage Examples

### Example 1: PostgreSQL E-commerce Database
**Prompt:** Design database management for PostgreSQL supporting E-commercePlatform with 10K concurrent users, 5000 TPS achieving <50ms p99 latency and 99.99% availability.

**Expected Output:** Schema: normalized core (customers, orders, products) with denormalized order_summary for listing queries, JSONB for product attributes, UUID primary keys for future sharding. Indexes: composite indexes on (customer_id, created_at) for order history, partial index on orders WHERE status = 'pending' for fulfillment queries, GIN index on product attributes JSONB. Performance: PgBouncer transaction pooling (200 connections to 20 backend), shared_buffers 25% RAM (8GB), effective_cache_size 75% (24GB), parallel query for analytics. HA: Patroni cluster with 3 nodes (1 primary, 2 sync replicas), etcd for consensus, HAProxy for connection routing, <30s automatic failover. Backup: continuous WAL archiving to S3, daily pg_basebackup, 7-day PITR capability, monthly restore tests. Security: SCRAM-SHA-256 auth, row-level security for multi-tenant, TLS required, pgAudit for SOC2. Monitoring: Prometheus postgres_exporter, Grafana dashboards (connections, query latency, replication lag), PagerDuty for P1 alerts. Cost: db.r6g.2xlarge ($0.50/hr) × 3 = ~$1,100/month, S3 backup ~$50/month.

### Example 2: MySQL SaaS Multi-tenant Database
**Prompt:** Design database management for MySQL supporting SaaSPlatform with 500 tenants, 100M rows, achieving tenant isolation and <100ms queries with PCI DSS compliance.

**Expected Output:** Schema: tenant_id in all tables (enforced by application), composite primary keys (tenant_id, entity_id), foreign keys within tenant scope. Partitioning: RANGE partition by tenant_id for large tables, enables efficient tenant data management. Indexes: include tenant_id in all indexes (tenant_id, column), covering indexes for common queries. Tenant isolation: application-enforced (no DB-level RLS in MySQL), audit all cross-tenant queries. Performance: ProxySQL for connection pooling and read/write splitting, query rules for routing. HA: MySQL Group Replication (3 nodes), MySQL Router for connection routing, automatic failover. Backup: Percona XtraBackup daily full + hourly incremental, binlog shipping to S3, 30-day retention for compliance. Security: TLS required, audit plugin enabled, encryption at rest (AWS RDS), PCI DSS compliance controls. Multi-tenant operations: tenant provisioning automation, tenant data export/delete for GDPR. Monitoring: PMM (Percona Monitoring and Management), per-tenant query analysis, noisy tenant detection. Cost: db.r6g.xlarge × 3 = ~$550/month, storage $0.10/GB (100GB) = $10/month.

### Example 3: MongoDB Real-time Analytics Database
**Prompt:** Design database management for MongoDB supporting AnalyticsPlatform ingesting 1M events/minute with 90-day retention and <10ms read latency for dashboards.

**Expected Output:** Schema: time-series collections (events, metrics), document design optimized for time-range queries, TTL indexes for automatic expiration. Sharding: shard key (tenant_id, timestamp) for write distribution, zone sharding for data locality. Indexes: compound index (tenant_id, timestamp, event_type) for dashboard queries, sparse indexes for optional fields. Read preference: secondary reads for analytics (reduce primary load), primary for real-time dashboards. Aggregation pipeline: $match early, $project to reduce document size, $bucket for time-series aggregations. HA: 3-node replica set per shard, config server replica set, mongos for routing. Sharding: 3 shards initially, add shards as volume grows, balancer scheduled for off-peak. Backup: MongoDB Cloud Backup continuous, queryable snapshots, 30-day retention. Performance: WiredTiger cache 50% RAM, readahead for sequential scans, write concern majority. Monitoring: MongoDB Atlas monitoring or Ops Manager, slow query analysis, oplog window monitoring. Scaling: auto-shard balancing, add shards at 70% capacity, vertical scale mongos nodes. Cost: M50 cluster (3 shards × 3 nodes) ~$3,000/month on Atlas, self-managed on EC2 ~$1,500/month.

---

## Cross-References

- [Data Infrastructure as Code](data-infrastructure-as-code.md) - Terraform modules for database provisioning
- [Cloud Architecture](../DevOps-Cloud/cloud-architecture.md) - Cloud database service selection
- [Query Optimization](../../data-analytics/Analytics-Engineering/query-optimization.md) - Deep-dive on query performance
