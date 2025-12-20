---
category: data-analytics
description: Design comprehensive indexing strategies including effectiveness analysis, advanced index types, and automated maintenance procedures for optimal query performance
title: Query Optimization - Indexing Strategies
tags:
- query-optimization
- database-indexes
- index-maintenance
- database-performance
use_cases:
- Designing comprehensive indexing strategies for optimal query performance
- Analyzing index effectiveness and identifying optimization opportunities
- Implementing automated index maintenance procedures
related_templates:
- data-analytics/Analytics-Engineering/query-optimization-baseline-analysis.md
- data-analytics/Analytics-Engineering/query-optimization-query-rewriting.md
- data-analytics/Analytics-Engineering/query-optimization-overview.md
industries:
- finance
- healthcare
- retail
- technology
- manufacturing
type: framework
difficulty: intermediate
slug: query-optimization-indexing-strategies
---

# Query Optimization - Indexing Strategies

## Purpose
Design and implement comprehensive indexing strategies that balance query performance with maintenance overhead. This framework covers index effectiveness analysis, advanced index type selection (B-tree, columnstore, filtered, covering), and automated maintenance procedures to optimize database workloads.

## Template

Design an indexing strategy for {DATABASE_CONTEXT}, supporting {WORKLOAD_CHARACTERISTICS} to achieve {PERFORMANCE_OBJECTIVES}.

**1. Index Inventory Assessment**

Begin by cataloging all existing indexes with their usage statistics and physical characteristics. For each index, capture read operations (seeks, scans, lookups) and write operations (updates from INSERT, UPDATE, DELETE) to calculate the read-write ratio indicating index value versus maintenance cost. Measure physical metrics including page count, fragmentation percentage, and size in megabytes. Classify indexes by effectiveness: high-value indexes have high read counts relative to writes, unused indexes have zero reads but accumulate write overhead, scan-heavy indexes serve mostly scans rather than seeks suggesting missing selectivity, and fragmented indexes exceed acceptable fragmentation thresholds degrading performance. Identify duplicate indexes where multiple indexes have the same leading key columns—these waste storage and slow writes without providing additional query benefit. Document clustered index choices validating that the clustering key supports the primary access pattern and is narrow, unique, and ever-increasing when possible.

**2. Index Usage Pattern Analysis**

Analyze how queries actually use indexes to identify optimization opportunities. Examine seek patterns to understand which column combinations queries filter on most frequently—these reveal candidates for composite index key columns. Review scan patterns identifying queries that read entire indexes when seeks would be more efficient, often indicating missing indexes or non-sargable predicates. Analyze lookup patterns where queries seek an index then look up additional columns from the clustered index—frequent lookups suggest adding INCLUDE columns to create covering indexes. Correlate index usage with query workload identifying which indexes support critical queries, which support only occasional queries, and which support no queries at all. Track usage over time since index value may vary by business cycle—month-end reporting, seasonal patterns, or batch processing windows may justify indexes that appear underused in daily metrics.

**3. Missing Index Identification**

Evaluate missing index recommendations while applying critical judgment to optimizer suggestions. Review missing index DMV recommendations capturing equality columns (used in equals predicates), inequality columns (used in range predicates), and included columns (selected but not filtered). Calculate impact scores combining average user impact percentage with seek and scan counts to prioritize high-value opportunities. Validate recommendations against actual query plans confirming the optimizer would use proposed indexes—some recommendations reflect queries that ran once or unusual parameter values. Consolidate overlapping recommendations where multiple suggestions could be satisfied by a single well-designed index covering several query patterns. Consider the write cost of each new index—tables with heavy insert, update, or delete activity pay higher maintenance costs for each additional index. Limit total indexes per table balancing query performance against write overhead—typically five to ten non-clustered indexes maximum for OLTP tables.

**4. Advanced Index Type Selection**

Select appropriate index types based on workload characteristics and query patterns. Use B-tree indexes (clustered and non-clustered) for OLTP workloads with point lookups and small range scans—these remain the default choice for most transactional queries. Design covering indexes that include all columns needed by critical queries, eliminating key lookups and enabling index-only access patterns. Create filtered indexes with WHERE clauses for queries that consistently filter to subsets of data—these reduce index size and maintenance for sparse conditions like active records or recent dates. Implement columnstore indexes for analytical workloads scanning large portions of tables with aggregations—columnstore provides dramatic compression and batch-mode execution for analytics. Consider hash indexes for memory-optimized tables with equality-only lookups requiring extreme low latency. Evaluate full-text indexes for text search scenarios rather than LIKE patterns with leading wildcards.

**5. Composite Index Design**

Design composite (multi-column) indexes following principles that maximize effectiveness. Order key columns by selectivity placing the most selective column first—this enables the index to narrow results quickly before evaluating subsequent columns. Include equality predicate columns before inequality columns since equality predicates can use all matching rows while range predicates terminate the seek. Add ORDER BY columns after filter columns when queries sort results to enable index-ordered retrieval without explicit sorting. Use INCLUDE for columns that are selected but not filtered or sorted—included columns appear only in leaf pages reducing index size while still enabling covering index benefits. Set appropriate fill factors leaving space for row insertions—use ninety to ninety-five percent for read-heavy indexes, seventy to eighty percent for write-heavy indexes with random inserts. Consider index key size limits (typically 900-1700 bytes depending on platform) when designing composite keys.

**6. Index Consolidation and Cleanup**

Identify opportunities to reduce index overhead through consolidation and removal. Remove truly unused indexes that have zero reads over an extended observation period (typically thirty or more days covering full business cycles)—these consume storage and slow every write operation. Consolidate similar indexes where one broader index can serve multiple query patterns—an index on columns A, B, C can serve queries filtering on A alone, A and B, or all three. Merge overlapping indexes that differ only in INCLUDE columns by creating a single index with the superset of included columns. Evaluate indexes supporting only low-value queries—if the query itself should be optimized or eliminated, the supporting index may no longer be needed. Document removal decisions and maintain rollback scripts enabling quick recreation if unexpected query regressions occur. Schedule consolidation changes during maintenance windows with performance monitoring to validate impact.

**7. Maintenance Procedure Design**

Design automated maintenance procedures that keep indexes performing optimally. Define fragmentation thresholds triggering maintenance—typically reorganize indexes with ten to thirty percent fragmentation (online, minimal blocking) and rebuild indexes exceeding thirty percent (more thorough but more resource-intensive). Configure rebuild options including online operations for production availability, maximum degree of parallelism for resource control, and sort in tempdb to avoid data file growth. Schedule maintenance windows balancing frequency against business impact—weekly for volatile tables, monthly for stable tables, with priority given to high-value and heavily fragmented indexes. Update statistics after index rebuilds or on a complementary schedule since index maintenance may not update all statistics. Set execution time limits preventing maintenance from running into business hours. Implement logging and alerting for maintenance job failures, long-running operations, and persistent fragmentation indicating design issues.

**8. Monitoring and Continuous Optimization**

Establish ongoing monitoring to maintain index effectiveness over time. Track index usage trends identifying indexes becoming more or less valuable as workload evolves. Monitor missing index recommendations for new patterns emerging from application changes or query modifications. Measure maintenance effectiveness validating that fragmentation stays within targets and rebuild operations complete within windows. Alert on anomalies including sudden index usage spikes, new unused indexes, or fragmentation exceeding thresholds shortly after maintenance. Create index effectiveness dashboards showing read/write ratios, fragmentation trends, and maintenance history for each significant index. Review indexing strategy quarterly adjusting for workload changes, data growth, and new query patterns. Document index purposes linking each index to the queries and business processes it supports, enabling informed decisions about modifications.

Deliver your indexing strategy as:

1. **Index inventory** cataloging current indexes with usage, fragmentation, and effectiveness classification
2. **Usage analysis** identifying seek patterns, scan issues, lookup overhead, and query correlations
3. **Missing index recommendations** validated and prioritized with impact scores and write cost consideration
4. **Index type selections** specifying B-tree, covering, filtered, or columnstore based on workload
5. **Composite designs** with column ordering, fill factors, and INCLUDE specifications
6. **Consolidation plan** identifying removals, merges, and cleanup with rollback procedures
7. **Maintenance automation** with thresholds, schedules, options, and logging
8. **Monitoring framework** tracking usage trends, fragmentation, and effectiveness over time

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DATABASE_CONTEXT}` | Platform, version, and scale | "SQL Server 2022 with 2TB database, 500 tables, mixed OLTP/reporting workload" |
| `{WORKLOAD_CHARACTERISTICS}` | Query patterns and volumes | "80% point lookups, 15% small range scans, 5% analytical aggregations, 50,000 queries/hour peak" |
| `{PERFORMANCE_OBJECTIVES}` | Target improvements | "reduce average query time by 50%, eliminate table scans on top 20 tables, complete nightly maintenance in 4-hour window" |

---

## Usage Examples

### Example 1: High-Volume E-Commerce OLTP
**Prompt:** "Design an indexing strategy for {DATABASE_CONTEXT: PostgreSQL 15 with 800GB order management database supporting e-commerce platform}, supporting {WORKLOAD_CHARACTERISTICS: 100,000 order lookups per hour by order_id and customer_id, inventory checks by product_id and warehouse_id, heavy insert activity during sales events}, to achieve {PERFORMANCE_OBJECTIVES: order lookup under 10ms P99, inventory check under 5ms, index maintenance completing in 2-hour nightly window}."

**Expected Output:** Index inventory showing current indexes on orders and inventory tables with usage statistics and bloat percentages. Usage analysis identifying customer order history queries causing sequential scans suggesting composite index on (customer_id, order_date). Missing index for inventory (warehouse_id, product_id) with include (quantity_available) enabling covering index access. B-tree indexes for all OLTP patterns with partial indexes for active orders only. Composite design placing customer_id before order_date for equality-then-range pattern. Consolidation removing duplicate indexes on orders table. Maintenance using pg_repack for online rebuilds with bloat threshold at 20%. Monitoring via pg_stat_user_indexes tracking index usage and bloat trends.

### Example 2: Financial Analytics Data Warehouse
**Prompt:** "Design an indexing strategy for {DATABASE_CONTEXT: SQL Server 2022 Enterprise data warehouse with 5TB fact tables and 100GB dimension tables}, supporting {WORKLOAD_CHARACTERISTICS: daily batch loads of 50M rows, complex analytical queries joining facts to dimensions with date range filters, ad-hoc reporting by business analysts}, to achieve {PERFORMANCE_OBJECTIVES: analytical queries under 30 seconds, batch load window under 6 hours, storage efficiency with compression}."

**Expected Output:** Index inventory distinguishing fact table columnstore indexes from dimension B-tree indexes. Usage analysis showing dimension lookups during fact table queries and date range filtering patterns. Columnstore recommendation for all fact tables with clustered columnstore replacing heap or B-tree clustered. B-tree indexes on dimension surrogate keys for join performance. Filtered indexes on fact tables for current-year queries reducing scan volume. No composite indexes on columnstore—rely on segment elimination instead. Maintenance using columnstore reorganize to compress open delta stores after batch loads. Monitoring tracking columnstore segment quality, delta store sizes, and query batch mode usage.

### Example 3: Multi-Tenant SaaS Application
**Prompt:** "Design an indexing strategy for {DATABASE_CONTEXT: Azure SQL Database elastic pool supporting 500 tenant databases with identical schema}, supporting {WORKLOAD_CHARACTERISTICS: tenant isolation via tenant_id column in all queries, mixed workload varying by tenant size, unpredictable query patterns from customizable reporting}, to achieve {PERFORMANCE_OBJECTIVES: consistent performance across tenant sizes, automated maintenance without per-tenant tuning, efficient use of elastic pool resources}."

**Expected Output:** Index inventory template applicable across all tenant databases. Usage analysis aggregating patterns across tenants identifying common and tenant-specific index needs. Standard index set with tenant_id as leading column on all multi-tenant tables. Filtered indexes per tenant rejected due to maintenance complexity at scale—rely on tenant_id leading column instead. Composite designs with tenant_id, then entity-specific columns matching common query patterns. Automated maintenance using elastic job agent applying consistent maintenance across all databases. Monitoring aggregating index metrics across pool identifying outlier databases needing attention and validating standard index set effectiveness across varying workloads.

---

## Cross-References

- [query-optimization-baseline-analysis.md](query-optimization-baseline-analysis.md) - Query analysis informing index design
- [query-optimization-query-rewriting.md](query-optimization-query-rewriting.md) - Query changes enabling better index usage
- [query-optimization-overview.md](query-optimization-overview.md) - Query optimization module navigation
