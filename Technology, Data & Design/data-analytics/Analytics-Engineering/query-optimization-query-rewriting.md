---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Analytics-Engineering/query-optimization-baseline-analysis.md
- data-analytics/Analytics-Engineering/query-optimization-indexing-strategies.md
- data-analytics/Analytics-Engineering/query-optimization-overview.md
tags:
- data-analytics
title: Query Optimization - Query Rewriting & SQL Optimization
use_cases:
- Rewriting inefficient SQL queries for improved performance
- Optimizing execution plans through query restructuring
- Implementing query hints and advanced SQL patterns for performance
industries:
- technology
type: template
difficulty: intermediate
slug: query-optimization-query-rewriting
---

# Query Optimization - Query Rewriting & SQL Optimization

## Purpose
Optimize SQL query performance through strategic rewriting, execution plan improvements, and advanced query patterns including subquery elimination, JOIN optimization, window functions, and query hints.

## Quick Start

### For Query Optimization
Optimize SQL queries in 3 steps:

1. **Identify Optimization Opportunities**
   - Review baseline analysis for queries with table scans, subqueries, or expensive sorts
   - Look for: IN clauses with subqueries, UNION without ALL, correlated subqueries, SELECT *
   - Prioritize queries with execution time > SLA or high execution frequency

2. **Apply Rewriting Patterns**
   - Convert IN subqueries to JOINs or EXISTS (lines 595-632)
   - Replace correlated subqueries with window functions (lines 646-663)
   - Use UNION ALL instead of UNION when duplicates are not an issue (lines 635-643)
   - Implement CTEs for complex analytical queries (lines 685-736)
   - Add explicit column lists and eliminate SELECT * (lines 667-679)

3. **Test and Validate**
   - Compare execution plans before and after optimization
   - Verify query results match original output
   - Measure performance improvement (execution time, I/O, CPU)
   - Apply query hints (lines 772-806) only if needed after testing

**Key Outputs**: Optimized queries, execution plan comparisons, performance metrics

**Key Variables**: `DATABASE_PLATFORM`, `OPTIMIZATION_APPROACH`, `QUERY_COMPLEXITY_LEVEL`

## Template

```
You are a SQL query optimization specialist for [DATABASE_PLATFORM]. Optimize SQL queries for [ORGANIZATION_NAME] to improve [PERFORMANCE_OBJECTIVES] using [OPTIMIZATION_APPROACH] methodology.

QUERY OPTIMIZATION CONTEXT:
Project Context:
- Organization: [ORGANIZATION_NAME]
- Database platform: [DATABASE_PLATFORM]
- Workload type: [WORKLOAD_TYPE]
- Query complexity: [QUERY_COMPLEXITY_LEVEL]
- Performance targets: [PERFORMANCE_TARGETS]
- Current challenges: [QUERY_PERFORMANCE_CHALLENGES]

### System Configuration
- Database version: [DATABASE_VERSION]
- Query timeout settings: [QUERY_TIMEOUT_SETTINGS]
- Parallelism configuration: [PARALLELISM_CONFIG]

### QUERY REWRITING AND OPTIMIZATION

### SQL Query Optimization Techniques
```sql
-- Query rewriting examples for performance optimization

-- 1. SUBQUERY TO JOIN CONVERSION
-- Original inefficient subquery
SELECT [COLUMN_LIST]
FROM [TABLE_A] a
WHERE a.[KEY_COLUMN] IN (
    SELECT b.[KEY_COLUMN]
    FROM [TABLE_B] b
    WHERE b.[FILTER_CONDITION] = '[FILTER_VALUE]'
);

-- Optimized JOIN version
SELECT [COLUMN_LIST]
FROM [TABLE_A] a
INNER JOIN (
    SELECT DISTINCT [KEY_COLUMN]
    FROM [TABLE_B]
    WHERE [FILTER_CONDITION] = '[FILTER_VALUE]'
) b ON a.[KEY_COLUMN] = b.[KEY_COLUMN];

-- 2. EXISTS vs IN optimization
-- Less efficient IN clause
SELECT [COLUMN_LIST]
FROM [TABLE_A] a
WHERE a.[ID] IN (
    SELECT [FOREIGN_KEY]
    FROM [TABLE_B]
    WHERE [STATUS] = '[ACTIVE_STATUS]'
);

-- More efficient EXISTS clause
SELECT [COLUMN_LIST]
FROM [TABLE_A] a
WHERE EXISTS (
    SELECT 1
    FROM [TABLE_B] b
    WHERE b.[FOREIGN_KEY] = a.[ID]
        AND b.[STATUS] = '[ACTIVE_STATUS]'
);

-- 3. UNION to UNION ALL optimization
-- Original UNION (with implicit DISTINCT)
SELECT [COLUMN_1], [COLUMN_2] FROM [TABLE_A] WHERE [CONDITION_A]
UNION
SELECT [COLUMN_1], [COLUMN_2] FROM [TABLE_B] WHERE [CONDITION_B];

-- Optimized UNION ALL (when duplicates are not an issue)
SELECT [COLUMN_1], [COLUMN_2] FROM [TABLE_A] WHERE [CONDITION_A]
UNION ALL
SELECT [COLUMN_1], [COLUMN_2] FROM [TABLE_B] WHERE [CONDITION_B];

-- 4. Window function optimization
-- Original correlated subquery
SELECT
    [COLUMN_LIST],
    (SELECT COUNT(*)
     FROM [TABLE_A] a2
     WHERE a2.[PARTITION_COLUMN] = a1.[PARTITION_COLUMN]
       AND a2.[DATE_COLUMN] <= a1.[DATE_COLUMN]) as running_count
FROM [TABLE_A] a1;

-- Optimized window function
SELECT
    [COLUMN_LIST],
    COUNT(*) OVER (
        PARTITION BY [PARTITION_COLUMN]
        ORDER BY [DATE_COLUMN]
        ROWS UNBOUNDED PRECEDING
    ) as running_count
FROM [TABLE_A];

-- 5. Selective projection optimization
-- Avoid SELECT *
SELECT *
FROM [LARGE_TABLE] l
JOIN [REFERENCE_TABLE] r ON l.[KEY] = r.[KEY]
WHERE [FILTER_CONDITION];

-- Use explicit column lists
SELECT
    l.[REQUIRED_COLUMN_1],
    l.[REQUIRED_COLUMN_2],
    r.[LOOKUP_VALUE]
FROM [LARGE_TABLE] l
JOIN [REFERENCE_TABLE] r ON l.[KEY] = r.[KEY]
WHERE [FILTER_CONDITION];
```

### Advanced Query Patterns
```sql
-- Complex analytical query optimization
WITH [CTE_NAME_1] AS (
    -- Base data with filters applied early
    SELECT
        [DIMENSION_COLUMNS],
        [MEASURE_COLUMNS],
        [DATE_COLUMN]
    FROM [FACT_TABLE]
    WHERE [DATE_COLUMN] >= '[START_DATE]'
        AND [DATE_COLUMN] < '[END_DATE]'
        AND [STATUS_FILTER] = '[ACTIVE_STATUS]'
),
[CTE_NAME_2] AS (
    -- Pre-aggregated metrics
    SELECT
        [GROUPING_COLUMNS],
        SUM([MEASURE_1]) as total_measure_1,
        AVG([MEASURE_2]) as avg_measure_2,
        COUNT(*) as record_count,
        MIN([DATE_COLUMN]) as min_date,
        MAX([DATE_COLUMN]) as max_date
    FROM [CTE_NAME_1]
    GROUP BY [GROUPING_COLUMNS]
),
[CTE_NAME_3] AS (
    -- Window functions for rankings and running totals
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY [PARTITION_COLUMNS]
            ORDER BY total_measure_1 DESC
        ) as ranking,
        SUM(total_measure_1) OVER (
            PARTITION BY [PARTITION_COLUMNS]
            ORDER BY [DATE_GROUPING]
            ROWS UNBOUNDED PRECEDING
        ) as running_total
    FROM [CTE_NAME_2]
)
-- Final result set with performance optimizations
SELECT
    [FINAL_COLUMN_LIST],
    ranking,
    running_total,
    -- Calculated fields
    CASE
        WHEN total_measure_1 > [THRESHOLD_VALUE] THEN '[HIGH_CATEGORY]'
        WHEN total_measure_1 > [MEDIUM_THRESHOLD] THEN '[MEDIUM_CATEGORY]'
        ELSE '[LOW_CATEGORY]'
    END as performance_category
FROM [CTE_NAME_3]
WHERE ranking <= [TOP_N_LIMIT]
ORDER BY [SORT_COLUMNS];

-- Optimized pivot query for reporting
SELECT
    [ROW_IDENTIFIER],
    [PIVOT_VALUE_1],
    [PIVOT_VALUE_2],
    [PIVOT_VALUE_3],
    [PIVOT_VALUE_4],
    ([PIVOT_VALUE_1] + [PIVOT_VALUE_2] + [PIVOT_VALUE_3] + [PIVOT_VALUE_4]) as total_value
FROM (
    SELECT
        [ROW_IDENTIFIER],
        [PIVOT_COLUMN],
        [VALUE_COLUMN]
    FROM [SOURCE_TABLE]
    WHERE [FILTER_CONDITIONS]
) source_data
PIVOT (
    SUM([VALUE_COLUMN])
    FOR [PIVOT_COLUMN] IN ([PIVOT_VALUE_1], [PIVOT_VALUE_2], [PIVOT_VALUE_3], [PIVOT_VALUE_4])
) pivoted_data
ORDER BY total_value DESC;

-- Efficient pagination with OFFSET/FETCH
SELECT
    [COLUMN_LIST]
FROM [TABLE_NAME]
WHERE [FILTER_CONDITIONS]
ORDER BY [SORT_COLUMNS]
OFFSET [ROWS_TO_SKIP] ROWS
FETCH NEXT [PAGE_SIZE] ROWS ONLY;
```

### Query Hint Optimization
```sql
-- Strategic use of query hints for performance
SELECT [COLUMN_LIST]
FROM [TABLE_A] a WITH (INDEX([SPECIFIC_INDEX_NAME]))
JOIN [TABLE_B] b WITH (FORCESEEK) ON a.[KEY] = b.[KEY]
WHERE [FILTER_CONDITIONS]
OPTION (
    MAXDOP [SPECIFIC_MAXDOP],           -- Control parallelism
    USE HINT('[HINT_NAME]'),            -- Specific optimizer hints
    RECOMPILE,                          -- Force plan recompilation
    OPTIMIZE FOR (@parameter = '[VALUE]') -- Parameter sniffing optimization
);

-- Index hints for specific scenarios
SELECT [COLUMN_LIST]
FROM [LARGE_TABLE] WITH (INDEX([COVERING_INDEX_NAME]), NOLOCK)
WHERE [INDEXED_COLUMN] = '[VALUE]'
    AND [DATE_COLUMN] BETWEEN '[START_DATE]' AND '[END_DATE]';

-- Join hints for complex queries
SELECT [COLUMN_LIST]
FROM [TABLE_A] a
INNER HASH JOIN [TABLE_B] b ON a.[KEY] = b.[KEY]    -- Force hash join
LEFT MERGE JOIN [TABLE_C] c ON a.[KEY2] = c.[KEY2]  -- Force merge join
WHERE [CONDITIONS];

-- Lock hints for concurrency control
SELECT [COLUMN_LIST]
FROM [TABLE_NAME] WITH (READPAST)      -- Skip locked rows
WHERE [CONDITIONS];

-- Statistics hints for cardinality estimation
SELECT [COLUMN_LIST]
FROM [TABLE_NAME]
WHERE [COLUMN] = '[VALUE]'
OPTION (USE HINT('FORCE_LEGACY_CARDINALITY_ESTIMATION'));
```

OUTPUT: Deliver optimized SQL queries including:
1. Rewritten queries with performance improvements
2. Before/after execution plan comparisons
3. Performance metrics (execution time, I/O, CPU reduction)
4. Query optimization rationale and trade-offs
5. Advanced patterns (CTEs, window functions, efficient joins)
6. Query hint recommendations with justification
7. Testing and validation results
8. Implementation guidelines and rollback plans
```

## Variables
[DATABASE_PLATFORM], [ORGANIZATION_NAME], [PERFORMANCE_OBJECTIVES], [OPTIMIZATION_APPROACH], [WORKLOAD_TYPE], [QUERY_COMPLEXITY_LEVEL], [PERFORMANCE_TARGETS], [QUERY_PERFORMANCE_CHALLENGES], [DATABASE_VERSION], [QUERY_TIMEOUT_SETTINGS], [PARALLELISM_CONFIG], [COLUMN_LIST], [TABLE_A], [TABLE_B], [KEY_COLUMN], [FILTER_CONDITION], [FILTER_VALUE], [ID], [FOREIGN_KEY], [STATUS], [ACTIVE_STATUS], [COLUMN_1], [COLUMN_2], [CONDITION_A], [CONDITION_B], [PARTITION_COLUMN], [DATE_COLUMN], [LARGE_TABLE], [REFERENCE_TABLE], [KEY], [REQUIRED_COLUMN_1], [REQUIRED_COLUMN_2], [LOOKUP_VALUE], [CTE_NAME_1], [DIMENSION_COLUMNS], [MEASURE_COLUMNS], [FACT_TABLE], [START_DATE], [END_DATE], [STATUS_FILTER], [CTE_NAME_2], [GROUPING_COLUMNS], [MEASURE_1], [MEASURE_2], [CTE_NAME_3], [PARTITION_COLUMNS], [DATE_GROUPING], [FINAL_COLUMN_LIST], [THRESHOLD_VALUE], [HIGH_CATEGORY], [MEDIUM_THRESHOLD], [MEDIUM_CATEGORY], [LOW_CATEGORY], [TOP_N_LIMIT], [SORT_COLUMNS], [ROW_IDENTIFIER], [PIVOT_VALUE_1], [PIVOT_VALUE_2], [PIVOT_VALUE_3], [PIVOT_VALUE_4], [PIVOT_COLUMN], [VALUE_COLUMN], [SOURCE_TABLE], [FILTER_CONDITIONS], [TABLE_NAME], [ROWS_TO_SKIP], [PAGE_SIZE], [SPECIFIC_INDEX_NAME], [KEY2], [SPECIFIC_MAXDOP], [HINT_NAME], [VALUE], [COVERING_INDEX_NAME], [INDEXED_COLUMN], [COLUMN], [CONDITIONS]

## Usage Examples

### Example 1: OLTP Transaction Optimization
```
DATABASE_PLATFORM: "SQL Server 2022"
ORGANIZATION_NAME: "E-commerce Platform"
WORKLOAD_TYPE: "OLTP"
OPTIMIZATION_APPROACH: "Subquery elimination and index hints"
QUERY_COMPLEXITY_LEVEL: "Medium"
PERFORMANCE_TARGETS: "< 100ms response time"
SPECIFIC_MAXDOP: "1"
```

### Example 2: OLAP Analytical Query Optimization
```
DATABASE_PLATFORM: "PostgreSQL 15"
ORGANIZATION_NAME: "Analytics Data Warehouse"
WORKLOAD_TYPE: "OLAP"
OPTIMIZATION_APPROACH: "CTE and window function optimization"
QUERY_COMPLEXITY_LEVEL: "High"
PERFORMANCE_TARGETS: "< 30 seconds for complex analytics"
TOP_N_LIMIT: "100"
```

### Example 3: Hybrid Workload Query Tuning
```
DATABASE_PLATFORM: "Snowflake"
ORGANIZATION_NAME: "SaaS Application"
WORKLOAD_TYPE: "Hybrid"
OPTIMIZATION_APPROACH: "Comprehensive rewriting with partition pruning"
QUERY_COMPLEXITY_LEVEL: "Medium-High"
PARALLELISM_CONFIG: "Auto-scale with query complexity"
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Query Optimization Baseline Analysis](query-optimization-baseline-analysis.md)** - Complementary approaches and methodologies
- **[Query Optimization Indexing Strategies](query-optimization-indexing-strategies.md)** - Complementary approaches and methodologies
- **[Query Optimization Overview](query-optimization-overview.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Query Optimization - Query Rewriting & SQL Optimization)
2. Use [Query Optimization Baseline Analysis](query-optimization-baseline-analysis.md) for deeper analysis
3. Apply [Query Optimization Indexing Strategies](query-optimization-indexing-strategies.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Analytics Engineering](../../data-analytics/Analytics Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Rewriting inefficient SQL queries for improved performance**: Combine this template with related analytics and strategy frameworks
- **Optimizing execution plans through query restructuring**: Combine this template with related analytics and strategy frameworks
- **Implementing query hints and advanced SQL patterns for performance**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Always test in non-production first** - Validate query changes in staging environment
2. **Preserve query semantics** - Ensure optimized query returns identical results
3. **Measure before and after** - Capture execution time, I/O, and CPU metrics
4. **Use EXISTS over IN for correlated data** - Better performance for large datasets
5. **Apply filters early in CTEs** - Reduce data volume before complex operations
6. **Leverage window functions** - Replace correlated subqueries for better performance
7. **Avoid SELECT *** - Specify only required columns to reduce I/O
8. **Use UNION ALL when possible** - Skip DISTINCT operation if not needed
9. **Order JOIN tables by size** - Start with smallest table for better execution plans
10. **Apply query hints sparingly** - Use only when optimizer makes suboptimal choices

## Tips for Success

- Start with the most expensive queries (highest execution time × frequency)
- Review actual execution plans, not just estimated plans
- Convert scalar subqueries to JOINs or window functions
- Push WHERE clause predicates as close to data source as possible
- Use CTEs to improve query readability and optimizer efficiency
- Test with production-like data volumes to validate performance gains
- Document optimization rationale for future reference
- Consider query hint alternatives (better indexes, updated statistics) first
- Use NOLOCK hints carefully - understand dirty read implications
- Monitor query performance over time to detect regressions
- Break complex queries into smaller steps if needed for clarity
- Cache frequently used subquery results in temporary tables for reuse
