---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- database-management
- schema-design
- query-optimization
- backup-recovery
title: Database Management Template
use_cases:
- Creating comprehensive database management including schema design, query optimization,
  performance tuning, backup/recovery, security, maintenance, and monitoring for enterprise
  database systems.
- Project planning and execution
- Strategy development
industries:
- finance
- government
- retail
- technology
type: template
difficulty: intermediate
slug: database-management
---

# Database Management Template

## Purpose
Comprehensive database management including schema design, query optimization, performance tuning, backup/recovery, security, maintenance, and monitoring for enterprise database systems.

## Quick Database Prompt
Design database for [application] with [X users], [Y transactions/sec]. Type: [PostgreSQL/MySQL/MongoDB/Redis]. Requirements: [consistency/availability priority], [read/write ratio]. Schema: [entities and relationships]. Optimization: indexing strategy, partitioning, connection pooling. Operations: backup schedule, replication ([sync/async]), monitoring (query performance, connections, storage), disaster recovery with [RPO/RTO targets].

## Quick Start

**Need to set up database management quickly?** Use this minimal example:

### Minimal Example
```
Design database management for ProductionDB PostgreSQL v14 with 1000+ concurrent users, 500GB data. Requirements: normalized schema for orders/customers/inventory, <100ms query performance, automated daily backups to S3, master-replica replication for 99.9% availability, connection pooling via pgBouncer, monitoring with Prometheus/Grafana.
```

### When to Use This
- Setting up new production database infrastructure
- Implementing high availability and disaster recovery
- Optimizing database performance and query efficiency
- Establishing backup/recovery and security protocols

### Basic 3-Step Workflow
1. **Design and provision** - Schema design, instance sizing, storage configuration
2. **Implement operations** - Backups, replication, monitoring, security controls
3. **Optimize and maintain** - Query tuning, index optimization, capacity planning

**Time to complete**: 1-2 weeks for initial setup, ongoing optimization

---

## Template Structure

### Database Overview
- **Database Name**: [DATABASE_NAME]
- **Database Type**: [DATABASE_TYPE]
- **Database Version**: [DATABASE_VERSION]
- **Environment**: [ENVIRONMENT]
- **Business Purpose**: [BUSINESS_PURPOSE]
- **Data Volume**: [DATA_VOLUME]
- **User Base**: [USER_BASE]
- **Performance Requirements**: [PERFORMANCE_REQUIREMENTS]
- **Availability Requirements**: [AVAILABILITY_REQUIREMENTS]
- **Compliance Requirements**: [COMPLIANCE_REQUIREMENTS]

### Schema Design
- **Database Schema**: [DATABASE_SCHEMA]
- **Table Design**: [TABLE_DESIGN]
- **Column Specifications**: [COLUMN_SPECIFICATIONS]
- **Data Types**: [DATA_TYPES]
- **Primary Keys**: [PRIMARY_KEYS]
- **Foreign Keys**: [FOREIGN_KEYS]
- **Constraints**: [CONSTRAINTS]
- **Indexes**: [INDEXES]
- **Views**: [VIEWS]
- **Stored Procedures**: [STORED_PROCEDURES]

### Query Optimization
- **Query Performance**: [QUERY_PERFORMANCE]
- **Execution Plans**: [EXECUTION_PLANS]
- **Index Strategy**: [INDEX_STRATEGY]
- **Query Rewriting**: [QUERY_REWRITING]
- **Join Optimization**: [JOIN_OPTIMIZATION]
- **Subquery Optimization**: [SUBQUERY_OPTIMIZATION]
- **Aggregate Optimization**: [AGGREGATE_OPTIMIZATION]
- **Query Caching**: [QUERY_CACHING]
- **Statistics Maintenance**: [STATISTICS_MAINTENANCE]
- **Query Monitoring**: [QUERY_MONITORING]

### Performance Tuning
- **Performance Metrics**: [PERFORMANCE_METRICS]
- **Bottleneck Analysis**: [BOTTLENECK_ANALYSIS]
- **Resource Utilization**: [RESOURCE_UTILIZATION]
- **Memory Management**: [MEMORY_MANAGEMENT]
- **CPU Optimization**: [CPU_OPTIMIZATION]
- **I/O Optimization**: [IO_OPTIMIZATION]
- **Storage Optimization**: [STORAGE_OPTIMIZATION]
- **Connection Management**: [CONNECTION_MANAGEMENT]
- **Lock Management**: [LOCK_MANAGEMENT]
- **Transaction Optimization**: [TRANSACTION_OPTIMIZATION]

### Backup and Recovery
- **Backup Strategy**: [BACKUP_STRATEGY]
- **Backup Types**: [BACKUP_TYPES]
- **Backup Schedule**: [BACKUP_SCHEDULE]
- **Backup Storage**: [BACKUP_STORAGE]
- **Backup Verification**: [BACKUP_VERIFICATION]
- **Recovery Procedures**: [RECOVERY_PROCEDURES]
- **Recovery Testing**: [RECOVERY_TESTING]
- **Point-in-Time Recovery**: [POINT_IN_TIME_RECOVERY]
- **Disaster Recovery**: [DISASTER_RECOVERY]
- **Business Continuity**: [BUSINESS_CONTINUITY]

### Security Management
- **Authentication**: [AUTHENTICATION]
- **Authorization**: [AUTHORIZATION]
- **Role-Based Access**: [ROLE_BASED_ACCESS]
- **Data Encryption**: [DATA_ENCRYPTION]
- **Network Security**: [NETWORK_SECURITY]
- **Audit Logging**: [AUDIT_LOGGING]
- **Security Policies**: [SECURITY_POLICIES]
- **Vulnerability Management**: [VULNERABILITY_MANAGEMENT]
- **Compliance Monitoring**: [COMPLIANCE_MONITORING]
- **Access Controls**: [ACCESS_CONTROLS]

### Maintenance Operations
- **Routine Maintenance**: [ROUTINE_MAINTENANCE]
- **Index Maintenance**: [INDEX_MAINTENANCE]
- **Statistics Updates**: [STATISTICS_UPDATES]
- **Data Archival**: [DATA_ARCHIVAL]
- **Data Purging**: [DATA_PURGING]
- **Space Management**: [SPACE_MANAGEMENT]
- **Log Management**: [LOG_MANAGEMENT]
- **Integrity Checks**: [INTEGRITY_CHECKS]
- **Health Checks**: [HEALTH_CHECKS]
- **Preventive Maintenance**: [PREVENTIVE_MAINTENANCE]

### Monitoring and Alerting
- **Monitoring Strategy**: [MONITORING_STRATEGY]
- **Key Metrics**: [KEY_METRICS]
- **Performance Monitoring**: [PERFORMANCE_MONITORING]
- **Availability Monitoring**: [AVAILABILITY_MONITORING]
- **Capacity Monitoring**: [CAPACITY_MONITORING]
- **Security Monitoring**: [SECURITY_MONITORING]
- **Alerting Rules**: [ALERTING_RULES]
- **Dashboard Design**: [DASHBOARD_DESIGN]
- **Reporting**: [MONITORING_REPORTING]
- **Trend Analysis**: [TREND_ANALYSIS]

### High Availability
- **HA Architecture**: [HA_ARCHITECTURE]
- **Replication Strategy**: [REPLICATION_STRATEGY]
- **Clustering**: [CLUSTERING]
- **Load Balancing**: [LOAD_BALANCING]
- **Failover Procedures**: [FAILOVER_PROCEDURES]
- **Split-Brain Prevention**: [SPLIT_BRAIN_PREVENTION]
- **Data Synchronization**: [DATA_SYNCHRONIZATION]
- **Consistency Management**: [CONSISTENCY_MANAGEMENT]
- **Service Discovery**: [SERVICE_DISCOVERY]
- **Health Monitoring**: [HEALTH_MONITORING]

### Scalability
- **Scaling Strategy**: [SCALING_STRATEGY]
- **Horizontal Scaling**: [HORIZONTAL_SCALING]
- **Vertical Scaling**: [VERTICAL_SCALING]
- **Partitioning**: [PARTITIONING]
- **Sharding**: [SHARDING]
- **Read Replicas**: [READ_REPLICAS]
- **Caching Layers**: [CACHING_LAYERS]
- **Connection Pooling**: [CONNECTION_POOLING]
- **Load Distribution**: [LOAD_DISTRIBUTION]
- **Capacity Planning**: [CAPACITY_PLANNING]

### Data Migration
- **Migration Strategy**: [MIGRATION_STRATEGY]
- **Source Assessment**: [SOURCE_ASSESSMENT]
- **Target Preparation**: [TARGET_PREPARATION]
- **Data Mapping**: [DATA_MAPPING]
- **ETL Processes**: [ETL_PROCESSES]
- **Validation Procedures**: [VALIDATION_PROCEDURES]
- **Cutover Planning**: [CUTOVER_PLANNING]
- **Rollback Procedures**: [ROLLBACK_PROCEDURES]
- **Testing Strategy**: [MIGRATION_TESTING]
- **Go-Live Support**: [GO_LIVE_SUPPORT]

### Database Operations
- **Operational Procedures**: [OPERATIONAL_PROCEDURES]
- **Change Management**: [CHANGE_MANAGEMENT]
- **Deployment Procedures**: [DEPLOYMENT_PROCEDURES]
- **Configuration Management**: [CONFIGURATION_MANAGEMENT]
- **Version Control**: [VERSION_CONTROL]
- **Environment Management**: [ENVIRONMENT_MANAGEMENT]
- **Release Management**: [RELEASE_MANAGEMENT]
- **Documentation**: [OPERATIONAL_DOCUMENTATION]
- **Training**: [OPERATIONAL_TRAINING]
- **Support Procedures**: [SUPPORT_PROCEDURES]

### Cost Optimization
- **Cost Analysis**: [COST_ANALYSIS]
- **Resource Optimization**: [RESOURCE_OPTIMIZATION]
- **Storage Optimization**: [STORAGE_COST_OPTIMIZATION]
- **Compute Optimization**: [COMPUTE_OPTIMIZATION]
- **Licensing Optimization**: [LICENSING_OPTIMIZATION]
- **Usage Monitoring**: [USAGE_MONITORING]
- **Cost Allocation**: [COST_ALLOCATION]
- **Budget Management**: [BUDGET_MANAGEMENT]
- **ROI Analysis**: [ROI_ANALYSIS]
- **Cost Reporting**: [COST_REPORTING]

### Compliance and Governance
- **Regulatory Compliance**: [REGULATORY_COMPLIANCE]
- **Data Governance**: [DATA_GOVERNANCE]
- **Data Classification**: [DATA_CLASSIFICATION]
- **Retention Policies**: [RETENTION_POLICIES]
- **Privacy Controls**: [PRIVACY_CONTROLS]
- **Audit Requirements**: [AUDIT_REQUIREMENTS]
- **Policy Enforcement**: [POLICY_ENFORCEMENT]
- **Compliance Reporting**: [COMPLIANCE_REPORTING]
- **Risk Management**: [RISK_MANAGEMENT]
- **Control Framework**: [CONTROL_FRAMEWORK]

### Troubleshooting
- **Common Issues**: [COMMON_ISSUES]
- **Diagnostic Procedures**: [DIAGNOSTIC_PROCEDURES]
- **Performance Issues**: [PERFORMANCE_ISSUES]
- **Connectivity Issues**: [CONNECTIVITY_ISSUES]
- **Replication Issues**: [REPLICATION_ISSUES]
- **Backup Issues**: [BACKUP_ISSUES]
- **Security Issues**: [SECURITY_ISSUES]
- **Corruption Issues**: [CORRUPTION_ISSUES]
- **Space Issues**: [SPACE_ISSUES]
- **Lock Issues**: [LOCK_ISSUES]

## Prompt Template

Design comprehensive database management for [DATABASE_NAME] [DATABASE_TYPE] v[DATABASE_VERSION] serving [USER_BASE] users with [DATA_VOLUME] data volume. Meet [PERFORMANCE_REQUIREMENTS] performance and [AVAILABILITY_REQUIREMENTS] availability requirements while ensuring [COMPLIANCE_REQUIREMENTS] compliance.

**Schema Design:**
- Design [DATABASE_SCHEMA] with [TABLE_DESIGN] architecture
- Define [COLUMN_SPECIFICATIONS] using [DATA_TYPES]
- Implement [PRIMARY_KEYS], [FOREIGN_KEYS], and [CONSTRAINTS]
- Create [INDEXES] strategy and [VIEWS] for data access
- Develop [STORED_PROCEDURES] for business logic

**Performance Optimization:**
- Achieve [QUERY_PERFORMANCE] with optimized [EXECUTION_PLANS]
- Implement [INDEX_STRATEGY] and [QUERY_CACHING]
- Optimize [JOIN_OPTIMIZATION] and [AGGREGATE_OPTIMIZATION]
- Monitor [PERFORMANCE_METRICS] and conduct [BOTTLENECK_ANALYSIS]
- Manage [MEMORY_MANAGEMENT] and [CONNECTION_MANAGEMENT]

**Backup and Recovery:**
- Implement [BACKUP_STRATEGY] with [BACKUP_TYPES]
- Schedule [BACKUP_SCHEDULE] to [BACKUP_STORAGE]
- Design [RECOVERY_PROCEDURES] with [POINT_IN_TIME_RECOVERY]
- Plan [DISASTER_RECOVERY] and [BUSINESS_CONTINUITY]
- Test [RECOVERY_TESTING] and [BACKUP_VERIFICATION]

**Security Management:**
- Configure [AUTHENTICATION] and [AUTHORIZATION]
- Implement [ROLE_BASED_ACCESS] and [ACCESS_CONTROLS]
- Enable [DATA_ENCRYPTION] and [NETWORK_SECURITY]
- Set up [AUDIT_LOGGING] and [COMPLIANCE_MONITORING]
- Manage [VULNERABILITY_MANAGEMENT] and [SECURITY_POLICIES]

**High Availability:**
- Design [HA_ARCHITECTURE] with [REPLICATION_STRATEGY]
- Implement [CLUSTERING] and [LOAD_BALANCING]
- Plan [FAILOVER_PROCEDURES] and [SPLIT_BRAIN_PREVENTION]
- Ensure [DATA_SYNCHRONIZATION] and [CONSISTENCY_MANAGEMENT]
- Monitor [HEALTH_MONITORING] and [SERVICE_DISCOVERY]

**Monitoring and Maintenance:**
- Track [KEY_METRICS] and [PERFORMANCE_MONITORING]
- Set up [ALERTING_RULES] and [DASHBOARD_DESIGN]
- Schedule [ROUTINE_MAINTENANCE] and [INDEX_MAINTENANCE]
- Perform [STATISTICS_UPDATES] and [INTEGRITY_CHECKS]
- Manage [DATA_ARCHIVAL] and [SPACE_MANAGEMENT]

**Scalability Planning:**
- Plan [SCALING_STRATEGY] with [HORIZONTAL_SCALING]
- Implement [PARTITIONING] and [SHARDING]
- Deploy [READ_REPLICAS] and [CACHING_LAYERS]
- Optimize [CONNECTION_POOLING] and [LOAD_DISTRIBUTION]
- Conduct [CAPACITY_PLANNING] analysis

Please provide detailed implementation plans, configuration examples, monitoring setup, operational procedures, and troubleshooting guides with specific recommendations for the target database platform.

## Usage Examples

### PostgreSQL Production Database
```
Design comprehensive database management for CustomerDB PostgreSQL v14 serving 10,000+ users with 5TB data volume. Meet <100ms query performance and 99.9% availability requirements while ensuring GDPR, SOX compliance.

Schema Design:
- Design normalized database schema with microservices-aligned table design architecture
- Define user, product, order column specifications using JSONB, UUID, timestamp data types
- Implement composite primary keys, cascading foreign keys, and check constraints
- Create B-tree, GIN indexes strategy and materialized views for analytics data access
- Develop PL/pgSQL stored procedures for complex business logic

Performance Optimization:
- Achieve sub-100ms query performance with parallel execution plans
- Implement covering index strategy and shared_buffers query caching
- Optimize hash join optimization and parallel aggregate optimization
- Monitor connection count, cache hit ratio performance metrics and conduct I/O bottleneck analysis
- Manage 16GB shared_buffers memory management and pgbouncer connection management

### High Availability
- Design master-replica ha architecture with streaming replication strategy
- Implement Patroni clustering and HAProxy load balancing
- Plan automatic failover procedures and etcd split brain prevention
- Ensure WAL shipping data synchronization and read-after-write consistency management
- Monitor Consul health monitoring and DNS service discovery
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[DATABASE_NAME]` | Name of the database instance | "CustomerDB", "OrdersDB", "InventoryDB", "AnalyticsDB", "UserAuthDB" |
| `[DATABASE_TYPE]` | Database technology | "PostgreSQL", "MySQL", "MongoDB", "SQL Server", "Oracle", "Redis", "DynamoDB" |
| `[DATABASE_VERSION]` | Database version number | "PostgreSQL 15", "MySQL 8.0", "MongoDB 7.0", "SQL Server 2022", "Oracle 19c" |
| `[ENVIRONMENT]` | Deployment environment | "production", "staging", "development", "test", "disaster-recovery" |
| `[BUSINESS_PURPOSE]` | Business function of database | "e-commerce transactions", "customer data platform", "real-time analytics", "user authentication" |
| `[DATA_VOLUME]` | Expected data size | "500GB", "5TB", "50TB", "100GB with 10% monthly growth" |
| `[USER_BASE]` | Number of concurrent users | "1,000+ concurrent users", "10,000 daily active users", "50,000 peak connections" |
| `[PERFORMANCE_REQUIREMENTS]` | Performance targets | "<100ms query response", "<50ms p99 latency", "10,000 TPS", "sub-second aggregations" |
| `[AVAILABILITY_REQUIREMENTS]` | Uptime requirements | "99.9% uptime", "99.99% availability", "zero planned downtime" |
| `[COMPLIANCE_REQUIREMENTS]` | Regulatory standards | "GDPR", "SOX", "PCI-DSS", "HIPAA", "SOC2" |
| `[DATABASE_SCHEMA]` | Schema design approach | "normalized 3NF", "star schema", "document-oriented", "key-value", "graph model" |
| `[TABLE_DESIGN]` | Table architecture pattern | "microservices-aligned", "domain-driven", "event-sourced", "CQRS pattern" |
| `[COLUMN_SPECIFICATIONS]` | Column definitions | "user, product, order entities", "JSONB for flexible attributes", "UUID primary keys" |
| `[DATA_TYPES]` | Data type selections | "JSONB, UUID, TIMESTAMP WITH TIMEZONE", "VARCHAR, DECIMAL, DATETIME", "BSON documents" |
| `[PRIMARY_KEYS]` | Primary key strategy | "UUID primary keys", "auto-increment BIGINT", "composite keys", "natural keys" |
| `[FOREIGN_KEYS]` | Foreign key configuration | "cascading deletes", "restrict on delete", "deferred constraints", "no FK (NoSQL)" |
| `[CONSTRAINTS]` | Data constraints | "NOT NULL, CHECK, UNIQUE", "custom domain constraints", "exclusion constraints" |
| `[INDEXES]` | Index types | "B-tree indexes", "GIN indexes for JSONB", "composite indexes", "partial indexes" |
| `[VIEWS]` | View definitions | "materialized views for analytics", "security views", "API views" |
| `[STORED_PROCEDURES]` | Stored procedure usage | "PL/pgSQL functions", "T-SQL procedures", "MongoDB aggregation pipelines" |
| `[QUERY_PERFORMANCE]` | Query performance targets | "sub-100ms for OLTP", "sub-second for analytics", "<10ms cache hits" |
| `[EXECUTION_PLANS]` | Query plan optimization | "parallel execution", "index-only scans", "hash joins", "merge joins" |
| `[INDEX_STRATEGY]` | Indexing approach | "covering indexes", "partial indexes", "expression indexes", "composite indexes" |
| `[QUERY_REWRITING]` | Query optimization techniques | "subquery flattening", "predicate pushdown", "join reordering" |
| `[JOIN_OPTIMIZATION]` | Join performance tuning | "hash joins for large tables", "nested loop for small sets", "merge joins for sorted data" |
| `[SUBQUERY_OPTIMIZATION]` | Subquery handling | "CTEs for readability", "lateral joins", "correlated subquery elimination" |
| `[AGGREGATE_OPTIMIZATION]` | Aggregation performance | "parallel aggregation", "pre-computed aggregates", "incremental aggregation" |
| `[QUERY_CACHING]` | Query cache configuration | "Redis query cache", "application-level caching", "prepared statement caching" |
| `[STATISTICS_MAINTENANCE]` | Statistics update schedule | "auto-analyze", "weekly ANALYZE", "histogram updates" |
| `[QUERY_MONITORING]` | Query monitoring tools | "pg_stat_statements", "Performance Schema", "Query Store", "slow query log" |
| `[PERFORMANCE_METRICS]` | Key performance indicators | "QPS, latency percentiles, cache hit ratio", "connections, locks, I/O wait" |
| `[BOTTLENECK_ANALYSIS]` | Performance analysis approach | "I/O bottleneck analysis", "lock contention analysis", "CPU profiling" |
| `[RESOURCE_UTILIZATION]` | Resource monitoring | "CPU, memory, disk I/O, network", "connection pool utilization" |
| `[MEMORY_MANAGEMENT]` | Memory configuration | "shared_buffers 25% RAM", "work_mem tuning", "buffer pool sizing" |
| `[CPU_OPTIMIZATION]` | CPU optimization | "parallel query workers", "query parallelization", "CPU affinity" |
| `[IO_OPTIMIZATION]` | I/O performance tuning | "SSD storage", "RAID configuration", "tablespace separation", "WAL placement" |
| `[STORAGE_OPTIMIZATION]` | Storage efficiency | "compression", "partitioning old data", "TOAST configuration" |
| `[CONNECTION_MANAGEMENT]` | Connection handling | "PgBouncer pooling", "ProxySQL", "HikariCP", "connection limits" |
| `[LOCK_MANAGEMENT]` | Lock handling strategy | "advisory locks", "row-level locking", "lock timeout configuration" |
| `[TRANSACTION_OPTIMIZATION]` | Transaction tuning | "batch commits", "transaction isolation levels", "savepoints" |
| `[BACKUP_STRATEGY]` | Backup approach | "continuous WAL archiving", "full + incremental", "snapshot-based" |
| `[BACKUP_TYPES]` | Backup methods | "full backup", "incremental backup", "differential backup", "logical backup" |
| `[BACKUP_SCHEDULE]` | Backup frequency | "daily full + hourly incremental", "continuous archiving", "weekly full" |
| `[BACKUP_STORAGE]` | Backup destination | "S3 bucket", "Azure Blob", "GCS", "on-premises NAS", "cross-region replication" |
| `[BACKUP_VERIFICATION]` | Backup validation | "automated restore tests", "checksum verification", "monthly restore drills" |
| `[RECOVERY_PROCEDURES]` | Recovery playbooks | "point-in-time recovery", "full restore procedure", "table-level recovery" |
| `[RECOVERY_TESTING]` | Recovery validation | "quarterly DR drills", "restore time testing", "data integrity verification" |
| `[POINT_IN_TIME_RECOVERY]` | PITR configuration | "WAL-based PITR", "5-minute recovery point", "transaction log shipping" |
| `[DISASTER_RECOVERY]` | DR strategy | "cross-region standby", "pilot light DR", "warm standby" |
| `[BUSINESS_CONTINUITY]` | BC planning | "RTO: 4 hours, RPO: 1 hour", "multi-region active-active", "geographic redundancy" |
| `[AUTHENTICATION]` | Authentication method | "LDAP integration", "SCRAM-SHA-256", "certificate authentication", "IAM authentication" |
| `[AUTHORIZATION]` | Authorization model | "role-based permissions", "row-level security", "schema-level access" |
| `[ROLE_BASED_ACCESS]` | RBAC configuration | "application roles", "read-only roles", "admin roles", "service accounts" |
| `[DATA_ENCRYPTION]` | Encryption implementation | "TDE at rest", "TLS 1.3 in transit", "column-level encryption" |
| `[NETWORK_SECURITY]` | Network protection | "VPC isolation", "security groups", "private endpoints", "SSL/TLS" |
| `[AUDIT_LOGGING]` | Audit trail configuration | "pgAudit", "SQL Server Audit", "MongoDB audit log", "CloudTrail" |
| `[SECURITY_POLICIES]` | Security policy enforcement | "password policies", "session timeout", "failed login lockout" |
| `[VULNERABILITY_MANAGEMENT]` | Vulnerability handling | "regular patching", "CVE monitoring", "security scanning" |
| `[COMPLIANCE_MONITORING]` | Compliance tracking | "AWS Config rules", "Azure Policy", "custom compliance checks" |
| `[ACCESS_CONTROLS]` | Access control mechanisms | "IP whitelisting", "VPN-only access", "bastion host", "just-in-time access" |
| `[ROUTINE_MAINTENANCE]` | Regular maintenance tasks | "VACUUM/ANALYZE", "index rebuilds", "statistics updates", "log rotation" |
| `[INDEX_MAINTENANCE]` | Index upkeep | "REINDEX scheduled", "index bloat monitoring", "unused index removal" |
| `[STATISTICS_UPDATES]` | Statistics refresh schedule | "daily ANALYZE", "auto_vacuum_analyze_threshold", "manual for large tables" |
| `[DATA_ARCHIVAL]` | Archival strategy | "partition-based archiving", "cold storage tier", "S3 Glacier archival" |
| `[DATA_PURGING]` | Data retention/purge | "90-day retention policy", "GDPR right-to-erasure", "scheduled purge jobs" |
| `[SPACE_MANAGEMENT]` | Storage management | "autovacuum tuning", "tablespace monitoring", "storage alerts at 80%" |
| `[LOG_MANAGEMENT]` | Log handling | "log rotation", "centralized logging", "log retention 30 days" |
| `[INTEGRITY_CHECKS]` | Data integrity validation | "CHECKDB weekly", "pg_amcheck", "foreign key validation" |
| `[HEALTH_CHECKS]` | Health monitoring | "connection health", "replication lag", "disk space", "query queue depth" |
| `[PREVENTIVE_MAINTENANCE]` | Proactive maintenance | "quarterly performance review", "capacity forecasting", "hardware refresh cycle" |
| `[MONITORING_STRATEGY]` | Monitoring approach | "Prometheus + Grafana", "Datadog", "CloudWatch", "custom dashboards" |
| `[KEY_METRICS]` | Critical metrics | "QPS, latency, connections, replication lag, disk I/O, cache hit ratio" |
| `[PERFORMANCE_MONITORING]` | Performance tracking | "query latency percentiles", "slow query analysis", "resource utilization" |
| `[AVAILABILITY_MONITORING]` | Uptime monitoring | "health check endpoints", "synthetic monitoring", "failover detection" |
| `[CAPACITY_MONITORING]` | Capacity tracking | "disk growth trends", "connection pool usage", "memory pressure" |
| `[SECURITY_MONITORING]` | Security alerting | "failed login alerts", "privilege escalation detection", "unusual query patterns" |
| `[ALERTING_RULES]` | Alert configuration | "PagerDuty for P1", "Slack for warnings", "email for informational" |
| `[DASHBOARD_DESIGN]` | Dashboard layout | "Grafana dashboards", "executive summary view", "operational detail view" |
| `[MONITORING_REPORTING]` | Reporting schedule | "daily health reports", "weekly performance summary", "monthly capacity review" |
| `[TREND_ANALYSIS]` | Trend tracking | "query pattern analysis", "growth forecasting", "seasonal pattern detection" |
| `[HA_ARCHITECTURE]` | High availability design | "primary-replica", "multi-AZ deployment", "active-active cluster" |
| `[REPLICATION_STRATEGY]` | Replication approach | "streaming replication", "logical replication", "synchronous replication" |
| `[CLUSTERING]` | Cluster configuration | "Patroni cluster", "MySQL Group Replication", "MongoDB replica set" |
| `[LOAD_BALANCING]` | Load distribution | "HAProxy", "PgBouncer", "ProxySQL", "read/write splitting" |
| `[FAILOVER_PROCEDURES]` | Failover handling | "automatic failover", "manual promotion", "DNS-based failover" |
| `[SPLIT_BRAIN_PREVENTION]` | Split-brain mitigation | "etcd consensus", "fencing", "quorum-based decisions" |
| `[DATA_SYNCHRONIZATION]` | Sync mechanism | "WAL shipping", "binlog replication", "change streams" |
| `[CONSISTENCY_MANAGEMENT]` | Consistency level | "read-after-write consistency", "eventual consistency", "strong consistency" |
| `[SERVICE_DISCOVERY]` | Discovery mechanism | "Consul", "etcd", "DNS-based discovery", "Kubernetes services" |
| `[HEALTH_MONITORING]` | Health check system | "pg_isready", "mysqladmin ping", "custom health endpoints" |
| `[SCALING_STRATEGY]` | Scaling approach | "read replicas for read scaling", "sharding for write scaling", "vertical scaling" |
| `[HORIZONTAL_SCALING]` | Horizontal scale-out | "read replica addition", "sharding", "connection pooling scale-out" |
| `[VERTICAL_SCALING]` | Vertical scale-up | "instance size upgrade", "storage expansion", "memory increase" |
| `[PARTITIONING]` | Partitioning strategy | "range partitioning by date", "list partitioning", "hash partitioning" |
| `[SHARDING]` | Sharding implementation | "Citus sharding", "Vitess", "application-level sharding", "consistent hashing" |
| `[READ_REPLICAS]` | Read replica setup | "3 read replicas", "cross-region replicas", "analytics replica" |
| `[CACHING_LAYERS]` | Cache implementation | "Redis cache", "Memcached", "application query cache" |
| `[CONNECTION_POOLING]` | Connection pool setup | "PgBouncer transaction mode", "ProxySQL", "HikariCP" |
| `[LOAD_DISTRIBUTION]` | Load balancing strategy | "round-robin", "least connections", "weighted distribution" |
| `[CAPACITY_PLANNING]` | Capacity forecasting | "6-month growth projection", "seasonal capacity planning" |
| `[MIGRATION_STRATEGY]` | Migration approach | "blue-green migration", "rolling migration", "big-bang cutover" |
| `[SOURCE_ASSESSMENT]` | Source system analysis | "schema analysis", "data profiling", "dependency mapping" |
| `[TARGET_PREPARATION]` | Target setup | "schema creation", "index setup", "user provisioning" |
| `[DATA_MAPPING]` | Data transformation mapping | "column mapping", "data type conversion", "default value handling" |
| `[ETL_PROCESSES]` | ETL implementation | "AWS DMS", "Debezium CDC", "custom ETL scripts", "Airbyte" |
| `[VALIDATION_PROCEDURES]` | Data validation | "row count validation", "checksum comparison", "sample data verification" |
| `[CUTOVER_PLANNING]` | Cutover strategy | "maintenance window cutover", "zero-downtime migration", "parallel run" |
| `[ROLLBACK_PROCEDURES]` | Rollback plan | "snapshot restore", "reverse replication", "application rollback" |
| `[MIGRATION_TESTING]` | Migration validation | "performance testing", "application compatibility testing", "UAT" |
| `[GO_LIVE_SUPPORT]` | Go-live support | "24/7 war room", "escalation procedures", "rollback criteria" |
| `[OPERATIONAL_PROCEDURES]` | Operations runbooks | "daily health checks", "incident response", "maintenance procedures" |
| `[CHANGE_MANAGEMENT]` | Change control | "CAB approval", "change windows", "rollback plans" |
| `[DEPLOYMENT_PROCEDURES]` | Deployment process | "Flyway migrations", "Liquibase", "blue-green deployments" |
| `[CONFIGURATION_MANAGEMENT]` | Config management | "Ansible playbooks", "Terraform", "parameter groups" |
| `[VERSION_CONTROL]` | Schema version control | "Git-based migrations", "Flyway versioning", "schema registry" |
| `[ENVIRONMENT_MANAGEMENT]` | Environment handling | "dev/staging/prod parity", "data masking for lower envs" |
| `[RELEASE_MANAGEMENT]` | Release process | "schema migration pipeline", "backward-compatible changes", "feature flags" |
| `[OPERATIONAL_DOCUMENTATION]` | Ops documentation | "runbooks", "architecture diagrams", "troubleshooting guides" |
| `[OPERATIONAL_TRAINING]` | Staff training | "DBA training program", "on-call onboarding", "incident response training" |
| `[SUPPORT_PROCEDURES]` | Support process | "L1/L2/L3 escalation", "vendor support", "24/7 on-call rotation" |
| `[COST_ANALYSIS]` | Cost assessment | "TCO analysis", "cost per query", "storage cost breakdown" |
| `[RESOURCE_OPTIMIZATION]` | Resource efficiency | "right-sizing instances", "reserved capacity", "spot instances for dev" |
| `[STORAGE_COST_OPTIMIZATION]` | Storage cost reduction | "compression", "tiered storage", "archival policies" |
| `[COMPUTE_OPTIMIZATION]` | Compute cost reduction | "auto-scaling", "scheduled scaling", "instance right-sizing" |
| `[LICENSING_OPTIMIZATION]` | License cost management | "open-source alternatives", "license pooling", "BYOL options" |
| `[USAGE_MONITORING]` | Usage tracking | "query patterns", "user activity", "resource consumption" |
| `[COST_ALLOCATION]` | Specify the cost allocation | "North America" |
| `[BUDGET_MANAGEMENT]` | Specify the budget management | "$500,000" |
| `[ROI_ANALYSIS]` | Return on investment analysis | "cost savings vs. on-prem", "performance improvement ROI", "availability value" |
| `[COST_REPORTING]` | Cost reporting setup | "monthly cost reports", "chargeback by application", "cost anomaly alerts" |
| `[REGULATORY_COMPLIANCE]` | Regulatory requirements | "GDPR data residency", "SOX audit controls", "HIPAA safeguards", "PCI-DSS requirements" |
| `[DATA_GOVERNANCE]` | Governance framework | "data stewardship", "data catalog", "lineage tracking", "quality rules" |
| `[DATA_CLASSIFICATION]` | Data classification scheme | "PII, sensitive, public", "confidentiality levels", "data sensitivity tags" |
| `[RETENTION_POLICIES]` | Data retention rules | "7-year financial data", "90-day logs", "GDPR erasure compliance" |
| `[PRIVACY_CONTROLS]` | Privacy implementation | "data masking", "anonymization", "pseudonymization", "consent management" |
| `[AUDIT_REQUIREMENTS]` | Audit compliance | "quarterly audits", "access reviews", "change tracking", "SOC2 evidence" |
| `[POLICY_ENFORCEMENT]` | Policy implementation | "automated policy checks", "approval workflows", "exception handling" |
| `[COMPLIANCE_REPORTING]` | Compliance documentation | "audit reports", "compliance dashboards", "evidence collection" |
| `[RISK_MANAGEMENT]` | Risk handling | "risk assessment", "mitigation plans", "risk register", "BIA" |
| `[CONTROL_FRAMEWORK]` | Control standards | "COBIT", "ISO 27001 controls", "NIST framework", "CIS benchmarks" |
| `[COMMON_ISSUES]` | Frequent problems | "connection timeouts", "slow queries", "replication lag", "deadlocks" |
| `[DIAGNOSTIC_PROCEDURES]` | Troubleshooting steps | "log analysis", "query plan review", "wait event analysis" |
| `[PERFORMANCE_ISSUES]` | Performance problems | "slow query identification", "index recommendations", "resource bottlenecks" |
| `[CONNECTIVITY_ISSUES]` | Connection problems | "connection pool exhaustion", "network timeouts", "DNS resolution" |
| `[REPLICATION_ISSUES]` | Replication problems | "replication lag", "replication conflicts", "slot overflow" |
| `[BACKUP_ISSUES]` | Backup problems | "backup failures", "restore failures", "backup performance" |
| `[SECURITY_ISSUES]` | Security incidents | "unauthorized access", "SQL injection attempts", "privilege escalation" |
| `[CORRUPTION_ISSUES]` | Data corruption handling | "checksum failures", "page corruption", "index corruption" |
| `[SPACE_ISSUES]` | Storage problems | "disk full", "tablespace growth", "bloat accumulation" |
| `[LOCK_ISSUES]` | Locking problems | "deadlocks", "lock waits", "blocking queries", "lock escalation" |

### MySQL E-commerce Database
```
Design comprehensive database management for EcommerceDB MySQL v8.0 serving 50,000+ users with 10TB data volume. Meet <50ms query performance and 99.95% availability requirements while ensuring PCI DSS compliance.

Schema Design:
- Design denormalized database schema with product-catalog optimized table design architecture
- Define customer, product, order, payment column specifications using JSON, DECIMAL, DATETIME data types
- Implement auto-increment primary keys, indexed foreign keys, and unique constraints
- Create composite, partial indexes strategy and indexed views for reporting data access
- Develop MySQL stored procedures for payment processing business logic

Scalability Planning:
- Plan read-write splitting scaling strategy with read replica horizontal scaling
- Implement range partitioning and consistent hashing sharding
- Deploy 5 read replicas and Redis caching layers
- Optimize ProxySQL connection pooling and weighted round-robin load distribution
- Conduct monthly capacity planning analysis

### Security Management
- Configure PAM authentication and role-based authorization
- Implement table-level role based access and column-level access controls
- Enable TDE data encryption and SSL network security
- Set up binary logging audit logging and automated compliance monitoring
- Manage quarterly vulnerability management and PCI DSS security policies
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Database Management Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Data Engineering](../../technology/Data Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive database management including schema design, query optimization, performance tuning, backup/recovery, security, maintenance, and monitoring for enterprise database systems.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Design schema with normalization and performance balance**
2. **Implement comprehensive monitoring and alerting early**
3. **Plan for scalability and high availability from the start**
4. **Automate routine maintenance and backup procedures**
5. **Follow security best practices and compliance requirements**
6. **Test backup and recovery procedures regularly**
7. **Monitor and optimize query performance continuously**
8. **Document all procedures and maintain operational runbooks**
9. **Implement proper change management processes**
10. **Plan capacity and cost optimization strategies**