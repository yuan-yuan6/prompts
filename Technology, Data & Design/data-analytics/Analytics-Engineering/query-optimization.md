---
category: data-analytics
title: Query Performance Assessment Framework
tags:
- query-optimization
- performance-tuning
- database-assessment
- sql-optimization
use_cases:
- Assessing database query performance health across multiple dimensions
- Identifying optimization priorities and investment areas
- Benchmarking query performance maturity against best practices
- Creating performance improvement roadmaps
related_templates:
- data-analytics/Analytics-Engineering/query-optimization-baseline-analysis.md
- data-analytics/Analytics-Engineering/query-optimization-indexing-strategies.md
- data-analytics/Analytics-Engineering/query-optimization-query-rewriting.md
- data-analytics/Analytics-Engineering/query-optimization-monitoring-tuning.md
- data-analytics/Analytics-Engineering/query-optimization-resource-concurrency.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: query-optimization
---

# Query Performance Assessment Framework

## Purpose
Comprehensively assess database query performance health across five dimensions: Query Efficiency, Indexing Strategy, Resource Utilization, Concurrency Management, and Monitoring Maturity. This framework identifies bottlenecks, prioritizes optimizations, and creates a performance improvement roadmap.

## Template

Conduct a comprehensive query performance assessment for {DATABASE_CONTEXT} database serving {APPLICATION_WORKLOAD} with performance targets of {PERFORMANCE_REQUIREMENTS}.

Assess performance across five dimensions, scoring each 1-5:

**1. QUERY EFFICIENCY**

Evaluate query execution quality starting with response time distribution across average, median, 95th percentile, and 99th percentile compared against SLA targets. Analyze execution plan quality measuring the ratio of index seeks versus table scans and identifying queries with suboptimal access paths. Review problematic query patterns including SELECT star operations, correlated subqueries, inefficient UNION versus UNION ALL usage, and excessive sorting or hashing. Assess parameter sniffing impact and plan cache efficiency looking for plan recompilation rates and cache hit ratios. Consider query complexity and maintainability evaluating whether queries are readable, properly commented, and following established patterns.

**2. INDEXING STRATEGY**

Assess indexing effectiveness beginning with coverage analysis for critical query patterns ensuring high-frequency and high-impact queries have supporting indexes. Measure index utilization rates distinguishing between productive seeks, wasteful scans, and completely unused indexes consuming space and slowing writes. Evaluate fragmentation levels across key tables and assess maintenance frequency for rebuilds and reorganizations. Review missing index recommendations from the database engine weighing impact scores against implementation costs. Analyze index overhead on write-heavy operations calculating the balance between read performance gains and write performance costs.

**3. RESOURCE UTILIZATION**

Profile resource consumption patterns starting with CPU utilization including average, peak, and distribution identifying compute-bound operations. Assess memory pressure through buffer cache hit ratios, page life expectancy, and memory grants looking for queries consuming excessive memory. Analyze storage I/O including read and write latency, throughput, and queue depths across database files. Review wait statistics identifying top wait types whether they indicate CPU, I/O, memory, lock, or network bottlenecks. Evaluate tempdb health for sort and hash spill activity and transaction log throughput for write-intensive workloads.

**4. CONCURRENCY MANAGEMENT**

Evaluate multi-user performance beginning with blocking analysis measuring frequency, duration, and impact of blocked sessions during peak usage. Review deadlock history identifying patterns, affected queries, and root causes whether index-related, application design, or transaction ordering. Assess lock escalation patterns determining whether row-level locks are appropriately escalating and whether isolation levels match workload requirements. Analyze transaction isolation level appropriateness balancing consistency requirements against concurrency. Evaluate connection pool efficiency including pool sizing, connection wait times, and connection lifetime management.

**5. MONITORING MATURITY**

Assess operational capabilities starting with performance baseline existence determining whether current-state benchmarks exist for comparison and trend analysis. Evaluate alerting coverage and threshold appropriateness ensuring critical metrics have alerts that trigger at actionable levels. Review automated maintenance procedures including statistics updates, index maintenance, and cleanup jobs. Assess query performance tracking capabilities for historical trending, regression detection, and capacity planning. Evaluate incident response and root cause analysis capability including documentation, escalation paths, and post-incident reviews.

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall score, maturity level, top 3 priorities, estimated optimization effort

2. **DIMENSION SCORECARD** - Table with score and key finding per dimension

3. **CRITICAL QUERY ANALYSIS** - For top 5 problematic queries showing current metrics, root cause, and expected improvement

4. **GAP ANALYSIS** - Top 5 gaps ranked by performance impact with specific remediation steps

5. **90-DAY ROADMAP** - Monthly actions across indexing, query rewriting, resource tuning, and monitoring

6. **SUCCESS METRICS** - Current baseline versus 30-day and 90-day targets for key indicators

Use this maturity scale: 1.0-1.9 Critical with severe issues and reactive firefighting, 2.0-2.9 Developing with known issues and ad-hoc optimization, 3.0-3.9 Defined with documented practices and proactive tuning, 4.0-4.9 Managed with automated optimization and predictive monitoring, 5.0 Optimized with industry-leading performance and self-tuning capabilities.

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DATABASE_CONTEXT}` | Database platform, version, and environment | "SQL Server 2019 Enterprise on AWS RDS" |
| `{APPLICATION_WORKLOAD}` | Application name and workload characteristics | "OrderManagement OLTP system with 500 concurrent users and 800GB data" |
| `{PERFORMANCE_REQUIREMENTS}` | SLA targets and known issues | "p95 < 200ms for transactions, < 5s for reports; checkout slowing during peak" |

---

## Usage Examples

### Example 1: E-commerce OLTP Database
**Prompt:** Conduct a comprehensive query performance assessment for SQL Server 2019 Enterprise on AWS RDS database serving OrderManagement OLTP system with 500 concurrent users processing 50M orders across 800GB with performance targets of p95 under 200ms for transactions and under 5 seconds for reports where checkout process slows during peak hours and inventory queries cause blocking.

**Expected Output:** Maturity scorecard showing 2.6/5 overall with indexing at 2.0 due to 15 missing indexes and 40% fragmentation, critical query analysis identifying checkout flow table scans and inventory blocking patterns, 90-day roadmap prioritizing covering indexes for checkout queries, query rewriting for correlated subqueries, and baseline establishment.

### Example 2: Data Warehouse Analytics
**Prompt:** Conduct a comprehensive query performance assessment for Snowflake Enterprise database serving CustomerAnalytics platform with 50 analysts and 200 dashboard viewers querying 5TB of transaction data with performance targets of dashboard queries under 10 seconds and ad-hoc queries under 60 seconds where morning dashboard refresh competes with ETL and some queries timeout.

**Expected Output:** Assessment identifying warehouse sizing issues with small warehouse handling concurrent dashboard and ETL loads, clustering key opportunities for time-series queries, query rewriting recommendations for inefficient CTEs, and multi-cluster warehouse configuration for workload isolation.

### Example 3: Healthcare Hybrid System
**Prompt:** Conduct a comprehensive query performance assessment for PostgreSQL 15 on AWS RDS database serving PatientRecords hybrid system supporting 300 clinical staff for real-time lookups and 20 analysts for reporting across 200GB of patient data with performance targets of patient lookup under 100ms and reports under 30 seconds where patient search is slow and report generation blocks clinical queries.

**Expected Output:** Analysis revealing missing GIN indexes for text search, connection pool exhaustion during report runs, inappropriate isolation levels causing lock contention, recommendations for read replica offloading reports, and pg_stat_statements baseline configuration.

---

## Cross-References

- [Query Optimization Baseline Analysis](query-optimization-baseline-analysis.md) - Establish performance baselines before optimizing
- [Query Optimization Indexing Strategies](query-optimization-indexing-strategies.md) - Detailed index design and maintenance
- [Query Optimization Query Rewriting](query-optimization-query-rewriting.md) - SQL pattern improvements and refactoring
- [Query Optimization Resource Concurrency](query-optimization-resource-concurrency.md) - Memory, I/O, and lock tuning
- [Query Optimization Monitoring Tuning](query-optimization-monitoring-tuning.md) - Ongoing performance management setup
