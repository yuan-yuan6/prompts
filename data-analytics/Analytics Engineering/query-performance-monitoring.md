---
title: Query Performance Monitoring Template
category: data-analytics/Analytics Engineering
tags: ['database', 'monitoring', 'performance', 'maintenance']
use_cases:
  - Implement query performance monitoring, automated statistics updates, and continuous optimization for database systems.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Query Performance Monitoring Template

## Purpose
Implement query performance monitoring, automated statistics updates, and continuous optimization for database systems.

## Quick Start

### For Data Engineers

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific implement needs
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine as needed

**Common Use Cases:**
- Implement query performance monitoring, automated statistics updates, and continuous optimization for database systems.
- Project-specific implementations
- Research and analysis workflows



## Template

---
title: Query Optimization & Performance Template
category: data-analytics/Analytics Engineering
tags: [data-analytics, data-science, design, optimization, research, strategy, template]
use_cases:
  - Creating design comprehensive sql query optimization strategies including performance tuning methodologies, indexing strategies, query efficiency analysis, and database performance optimization for analytical workloads.

  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---


# Query Optimization & Performance Template


## Purpose
Design comprehensive SQL query optimization strategies including performance tuning methodologies, indexing strategies, query efficiency analysis, and database performance optimization for analytical workloads.


### For Data Engineers
Optimize query performance in 3 steps:

1. **Baseline Performance Assessment**
   - Identify slow queries: Use query performance views to find queries >1s execution time
   - Analyze execution plans: Review table scans, missing indexes, expensive joins
   - Measure resource consumption: Track CPU time, logical/physical reads, memory usage
   - Run baseline queries (lines 63-100) to generate performance reports

2. **Apply Optimization Techniques**
   - **Indexing**: Create appropriate B-tree, columnstore, or covering indexes based on query patterns
   - **Query Rewriting**: Eliminate subqueries, optimize JOIN order, use CTEs effectively
   - **Statistics**: Update table statistics and enable auto-update for query optimizer
   - Use provided SQL patterns for index creation, partition pruning, and query hints

3. **Monitor and Tune**
   - Set up query performance monitoring with execution time tracking
   - Implement automated statistics updates and index maintenance
   - Configure alerts for query timeouts or resource spikes
   - Review execution plans regularly for regression detection

**Key Variables**: `DATABASE_PLATFORM` (SQL Server, PostgreSQL, Snowflake), `WORKLOAD_TYPE` (OLAP/OLTP), `QUERY_RESPONSE_TIME_SLA`


You are a database performance optimization expert specializing in [DATABASE_PLATFORM]. Design a comprehensive query optimization and performance tuning strategy for [ORGANIZATION_NAME] to improve [PERFORMANCE_OBJECTIVES] using [OPTIMIZATION_METHODOLOGY] approach.

PERFORMANCE OPTIMIZATION OVERVIEW:

- Performance objectives: [PERFORMANCE_OBJECTIVES]

- Current challenges: [CURRENT_PERFORMANCE_CHALLENGES]

- SLA requirements: [PERFORMANCE_SLA_REQUIREMENTS]

### Performance Requirements

### Performance Baseline Assessment

### Current Performance Metrics
```sql
-- Performance baseline assessment queries
-- Query execution time analysis
SELECT
    [QUERY_ID_COLUMN],
    [QUERY_TEXT_COLUMN],
    [EXECUTION_COUNT],
    [TOTAL_EXECUTION_TIME_MS],
    [AVERAGE_EXECUTION_TIME_MS],
    [MAX_EXECUTION_TIME_MS],
    [MIN_EXECUTION_TIME_MS],
    [TOTAL_CPU_TIME_MS],
    [TOTAL_LOGICAL_READS],
    [TOTAL_PHYSICAL_READS],
    [TOTAL_LOGICAL_WRITES],
    [COMPILATION_TIME_MS],
    [LAST_EXECUTION_TIME]
FROM [QUERY_PERFORMANCE_VIEW]
WHERE [LAST_EXECUTION_TIME] >= DATEADD(day, -[ANALYSIS_PERIOD_DAYS], GETDATE())
ORDER BY [TOTAL_EXECUTION_TIME_MS] DESC;

-- Top resource-consuming queries
WITH QueryStats AS (
    SELECT
        [QUERY_HASH],
        COUNT(*) as execution_count,
        AVG([DURATION_MS]) as avg_duration,
        MAX([DURATION_MS]) as max_duration,
        AVG([CPU_TIME_MS]) as avg_cpu,
        AVG([LOGICAL_READS]) as avg_reads,
        AVG([PHYSICAL_READS]) as avg_physical_reads,
        SUM([DURATION_MS]) as total_duration,
        SUM([CPU_TIME_MS]) as total_cpu
    FROM [QUERY_EXECUTION_LOG]
    WHERE [EXECUTION_DATE] >= DATEADD(day, -[ANALYSIS_DAYS], GETDATE())
    GROUP BY [QUERY_HASH]
)
SELECT
    TOP [TOP_N_QUERIES]
    [QUERY_HASH],
    execution_count,
    avg_duration,
    max_duration,
    avg_cpu,
    avg_reads,
    total_duration,
    total_cpu,
    -- Performance score calculation
    (total_duration * [DURATION_WEIGHT] + total_cpu * [CPU_WEIGHT] +
     avg_reads * [IO_WEIGHT]) as performance_impact_score
FROM QueryStats
ORDER BY performance_impact_score DESC;

-- Wait statistics analysis
SELECT
    [WAIT_TYPE],
    [WAITING_TASKS_COUNT],
    [WAIT_TIME_MS],
    [MAX_WAIT_TIME_MS],
    [SIGNAL_WAIT_TIME_MS],
    ([WAIT_TIME_MS] - [SIGNAL_WAIT_TIME_MS]) AS [RESOURCE_WAIT_TIME_MS],
    CASE
        WHEN [WAIT_TIME_MS] > 0
        THEN ([SIGNAL_WAIT_TIME_MS] * 100.0) / [WAIT_TIME_MS]
        ELSE 0
    END AS [SIGNAL_WAIT_PERCENTAGE],
    ROW_NUMBER() OVER(ORDER BY [WAIT_TIME_MS] DESC) AS [WAIT_RANK]
FROM [WAIT_STATS_VIEW]
WHERE [WAIT_TYPE] NOT LIKE '%SLEEP%'
    AND [WAIT_TYPE] NOT LIKE '%IDLE%'
    AND [WAIT_TYPE] NOT LIKE '%QUEUE%'
ORDER BY [WAIT_TIME_MS] DESC;

-- Index usage statistics
SELECT
    OBJECT_SCHEMA_NAME([OBJECT_ID]) AS [schema_name],
    OBJECT_NAME([OBJECT_ID]) AS [table_name],
    [INDEX_NAME],
    [USER_SEEKS],
    [USER_SCANS],
    [USER_LOOKUPS],
    [USER_UPDATES],
    ([USER_SEEKS] + [USER_SCANS] + [USER_LOOKUPS]) AS [total_reads],
    [LAST_USER_SEEK],
    [LAST_USER_SCAN],
    [LAST_USER_LOOKUP],
    [LAST_USER_UPDATE]
FROM [INDEX_USAGE_STATS_VIEW]
WHERE [DATABASE_ID] = DB_ID('[DATABASE_NAME]')
ORDER BY [total_reads] DESC;

Query Execution Plan Analysis:
```sql
-- Execution plan analysis framework
WITH ExecutionPlanAnalysis AS (
    SELECT
        [PLAN_HASH],
        [QUERY_HASH],
        [CACHED_TIME],
        [LAST_EXECUTION_TIME],
        [EXECUTION_COUNT],
        [TOTAL_WORKER_TIME] / 1000 as total_cpu_ms,
        [TOTAL_ELAPSED_TIME] / 1000 as total_elapsed_ms,
        [TOTAL_LOGICAL_READS],
        [TOTAL_PHYSICAL_READS],
        [TOTAL_LOGICAL_WRITES],
        [QUERY_PLAN],
        -- Plan efficiency metrics
        CASE
            WHEN [TOTAL_LOGICAL_READS] > [HIGH_IO_THRESHOLD] THEN 'HIGH_IO'
            WHEN [TOTAL_WORKER_TIME] > [HIGH_CPU_THRESHOLD] THEN 'HIGH_CPU'
            WHEN [TOTAL_ELAPSED_TIME] > [HIGH_DURATION_THRESHOLD] THEN 'HIGH_DURATION'
            ELSE 'NORMAL'
        END as performance_category
    FROM [PLAN_CACHE_VIEW]
    WHERE [LAST_EXECUTION_TIME] >= DATEADD(hour, -[ANALYSIS_HOURS], GETDATE())
)
SELECT
    [PLAN_HASH],
    [EXECUTION_COUNT],
    [total_cpu_ms],
    [total_elapsed_ms],
    [TOTAL_LOGICAL_READS],
    [TOTAL_PHYSICAL_READS],
    [performance_category],
    -- Extract key plan elements
    [QUERY_PLAN].value('(/ShowPlanXML/BatchSequence/Batch/Statements/StmtSimple/@StatementText)[1]', 'NVARCHAR(MAX)') as query_text,
    [QUERY_PLAN].value('(/ShowPlanXML/BatchSequence/Batch/Statements/StmtSimple/@StatementSubTreeCost)[1]', 'FLOAT') as estimated_cost,
    -- Identify problematic operators
    CASE
        WHEN [QUERY_PLAN].exist('/ShowPlanXML//RelOp[@PhysicalOp="Table Scan"]') = 1 THEN 'TABLE_SCAN'
        WHEN [QUERY_PLAN].exist('/ShowPlanXML//RelOp[@PhysicalOp="Clustered Index Scan"]') = 1 THEN 'CLUSTERED_SCAN'
        WHEN [QUERY_PLAN].exist('/ShowPlanXML//RelOp[@PhysicalOp="Sort"]') = 1 THEN 'EXPENSIVE_SORT'
        WHEN [QUERY_PLAN].exist('/ShowPlanXML//RelOp[@PhysicalOp="Hash Match"]') = 1 THEN 'HASH_JOIN'
        ELSE 'OPTIMIZED'
    END as plan_characteristics
FROM ExecutionPlanAnalysis
WHERE performance_category != 'NORMAL'
ORDER BY [total_elapsed_ms] DESC;

-- Missing index analysis
SELECT
    [DATABASE_NAME],
    [SCHEMA_NAME],
    [TABLE_NAME],
    [COLUMN_NAME],
    [COLUMN_USAGE],
    [USER_SEEKS],
    [USER_SCANS],
    [LAST_USER_SEEK],
    [AVG_TOTAL_USER_COST],
    [AVG_USER_IMPACT],
    [SYSTEM_SEEKS],
    [SYSTEM_SCANS],
    -- Calculate index priority score
    ([USER_SEEKS] + [USER_SCANS]) * [AVG_TOTAL_USER_COST] * ([AVG_USER_IMPACT] / 100.0) as index_priority_score
FROM [MISSING_INDEX_DETAILS_VIEW] mid
INNER JOIN [MISSING_INDEX_GROUPS_VIEW] mig ON mid.[INDEX_GROUP_HANDLE] = mig.[INDEX_GROUP_HANDLE]
INNER JOIN [MISSING_INDEX_GROUP_STATS_VIEW] migs ON mig.[INDEX_GROUP_HANDLE] = migs.[GROUP_HANDLE]
WHERE [DATABASE_NAME] = '[TARGET_DATABASE]'
ORDER BY index_priority_score DESC;

Workload Pattern Analysis:
```sql
-- Temporal query patterns
WITH HourlyQueryPattern AS (
    SELECT
        DATEPART(hour, [EXECUTION_TIME]) as execution_hour,
        DATEPART(dow, [EXECUTION_TIME]) as day_of_week,
        COUNT(*) as query_count,
        AVG([DURATION_MS]) as avg_duration,
        MAX([DURATION_MS]) as max_duration,
        SUM([CPU_TIME_MS]) as total_cpu,
        SUM([LOGICAL_READS]) as total_reads
    FROM [QUERY_EXECUTION_LOG]
    WHERE [EXECUTION_TIME] >= DATEADD(day, -[PATTERN_ANALYSIS_DAYS], GETDATE())
    GROUP BY DATEPART(hour, [EXECUTION_TIME]), DATEPART(dow, [EXECUTION_TIME])
),
QueryComplexityAnalysis AS (
    SELECT
        [QUERY_HASH],
        [QUERY_TEXT],
        -- Complexity metrics
        LEN([QUERY_TEXT]) as query_length,
        (LEN([QUERY_TEXT]) - LEN(REPLACE(UPPER([QUERY_TEXT]), 'JOIN', ''))) / 4 as join_count,
        (LEN([QUERY_TEXT]) - LEN(REPLACE(UPPER([QUERY_TEXT]), 'WHERE', ''))) / 5 as where_clause_count,
        (LEN([QUERY_TEXT]) - LEN(REPLACE(UPPER([QUERY_TEXT]), 'GROUP BY', ''))) / 8 as group_by_count,
        (LEN([QUERY_TEXT]) - LEN(REPLACE(UPPER([QUERY_TEXT]), 'ORDER BY', ''))) / 8 as order_by_count,
        (LEN([QUERY_TEXT]) - LEN(REPLACE(UPPER([QUERY_TEXT]), 'UNION', ''))) / 5 as union_count,
        -- Performance metrics
        AVG([DURATION_MS]) as avg_duration,
        COUNT(*) as execution_frequency
    FROM [QUERY_EXECUTION_LOG]
    WHERE [EXECUTION_TIME] >= DATEADD(day, -[COMPLEXITY_ANALYSIS_DAYS], GETDATE())
    GROUP BY [QUERY_HASH], [QUERY_TEXT]
)
SELECT
    [QUERY_HASH],
    query_length,
    join_count,
    where_clause_count,
    group_by_count,
    order_by_count,
    union_count,
    avg_duration,
    execution_frequency,
    -- Complexity score calculation
    (query_length * [LENGTH_WEIGHT] +
     join_count * [JOIN_WEIGHT] +
     where_clause_count * [WHERE_WEIGHT] +
     group_by_count * [GROUP_WEIGHT] +
     order_by_count * [ORDER_WEIGHT] +
     union_count * [UNION_WEIGHT]) as complexity_score
FROM QueryComplexityAnalysis
ORDER BY complexity_score DESC;

Comprehensive Index Analysis:
```sql
-- Index effectiveness analysis
WITH IndexEffectivenessMetrics AS (
    SELECT
        i.[OBJECT_ID],
        i.[INDEX_ID],
        OBJECT_SCHEMA_NAME(i.[OBJECT_ID]) as schema_name,
        OBJECT_NAME(i.[OBJECT_ID]) as table_name,
        i.[NAME] as index_name,
        i.[TYPE_DESC] as index_type,
        i.[IS_UNIQUE],
        i.[IS_PRIMARY_KEY],
        i.[FILL_FACTOR],
        -- Usage statistics
        ISNULL(ius.[USER_SEEKS], 0) as user_seeks,
        ISNULL(ius.[USER_SCANS], 0) as user_scans,
        ISNULL(ius.[USER_LOOKUPS], 0) as user_lookups,
        ISNULL(ius.[USER_UPDATES], 0) as user_updates,
        ISNULL(ius.[USER_SEEKS] + ius.[USER_SCANS] + ius.[USER_LOOKUPS], 0) as total_reads,
        -- Physical statistics
        ips.[PAGE_COUNT],
        ips.[RECORD_COUNT],
        ips.[AVG_FRAGMENTATION_IN_PERCENT],
        ips.[FRAGMENT_COUNT],
        ips.[AVG_FRAGMENT_SIZE_IN_PAGES],
        -- Size metrics
        (ips.[PAGE_COUNT] * 8.0 / 1024) as size_mb
    FROM sys.indexes i
    LEFT JOIN sys.dm_db_index_usage_stats ius
        ON i.[OBJECT_ID] = ius.[OBJECT_ID] AND i.[INDEX_ID] = ius.[INDEX_ID]
        AND ius.[DATABASE_ID] = DB_ID()
    LEFT JOIN sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'LIMITED') ips
        ON i.[OBJECT_ID] = ips.[OBJECT_ID] AND i.[INDEX_ID] = ips.[INDEX_ID]
    WHERE i.[TYPE] IN (1, 2) -- Clustered and non-clustered indexes
        AND OBJECT_SCHEMA_NAME(i.[OBJECT_ID]) != 'sys'
)
SELECT
    schema_name,
    table_name,
    index_name,
    index_type,
    user_seeks,
    user_scans,
    user_lookups,
    user_updates,
    total_reads,
    [PAGE_COUNT],
    [AVG_FRAGMENTATION_IN_PERCENT],
    size_mb,
    -- Index efficiency metrics
    CASE
        WHEN total_reads = 0 AND user_updates > [UNUSED_UPDATE_THRESHOLD] THEN 'UNUSED_HIGH_MAINTENANCE'
        WHEN total_reads = 0 THEN 'UNUSED'
        WHEN user_scans > user_seeks AND user_scans > [SCAN_THRESHOLD] THEN 'SCAN_HEAVY'
        WHEN [AVG_FRAGMENTATION_IN_PERCENT] > [FRAGMENTATION_THRESHOLD] THEN 'FRAGMENTED'
        WHEN total_reads > [HIGH_USAGE_THRESHOLD] THEN 'HIGH_VALUE'
        ELSE 'NORMAL'
    END as index_status,
    -- Read/Write ratio
    CASE
        WHEN user_updates > 0
        THEN CAST(total_reads AS FLOAT) / user_updates
        ELSE total_reads
    END as read_write_ratio
FROM IndexEffectivenessMetrics
ORDER BY total_reads DESC, size_mb DESC;

-- Index recommendation engine
WITH TableAnalysis AS (
    SELECT
        OBJECT_SCHEMA_NAME([OBJECT_ID]) as schema_name,
        OBJECT_NAME([OBJECT_ID]) as table_name,
        [OBJECT_ID],
        SUM([USER_SEEKS]) as total_seeks,
        SUM([USER_SCANS]) as total_scans,
        SUM([USER_LOOKUPS]) as total_lookups,
        SUM([USER_UPDATES]) as total_updates,
        COUNT(*) as index_count
    FROM sys.dm_db_index_usage_stats
    WHERE [DATABASE_ID] = DB_ID()
    GROUP BY [OBJECT_ID]
),
ColumnUsageAnalysis AS (
    SELECT
        ic.[OBJECT_ID],
        c.[NAME] as column_name,
        ic.[INDEX_ID],
        ic.[KEY_ORDINAL],
        ic.[IS_DESCENDING_KEY],
        ic.[IS_INCLUDED_COLUMN],
        COUNT(*) OVER (PARTITION BY ic.[OBJECT_ID], c.[NAME]) as column_index_count
    FROM sys.index_columns ic
    INNER JOIN sys.columns c ON ic.[OBJECT_ID] = c.[OBJECT_ID] AND ic.[COLUMN_ID] = c.[COLUMN_ID]
    WHERE ic.[KEY_ORDINAL] > 0 OR ic.[IS_INCLUDED_COLUMN] = 1
)
SELECT
    ta.schema_name,
    ta.table_name,
    ta.total_seeks,
    ta.total_scans,
    ta.index_count,
    -- Index recommendations
    CASE
        WHEN ta.total_scans > ta.total_seeks * [SCAN_SEEK_RATIO_THRESHOLD]
        THEN 'CONSIDER_COVERING_INDEXES'
        WHEN ta.index_count < [MIN_RECOMMENDED_INDEXES] AND ta.total_seeks > [HIGH_SEEK_THRESHOLD]
        THEN 'ADD_SELECTIVE_INDEXES'
        WHEN ta.index_count > [MAX_RECOMMENDED_INDEXES]
        THEN 'CONSOLIDATE_INDEXES'
        ELSE 'INDEXES_ADEQUATE'
    END as recommendation
FROM TableAnalysis ta
ORDER BY (ta.total_seeks + ta.total_scans) DESC;

Index Maintenance Strategy:
```sql
-- Automated index maintenance procedures
CREATE PROCEDURE [dbo].[sp_OptimizeIndexMaintenance]
    @DatabaseName NVARCHAR(128) = NULL,
    @SchemaName NVARCHAR(128) = NULL,
    @TableName NVARCHAR(128) = NULL,
    @FragmentationThreshold FLOAT = [DEFAULT_FRAGMENTATION_THRESHOLD],
    @RebuildThreshold FLOAT = [REBUILD_THRESHOLD],
    @ReorganizeThreshold FLOAT = [REORGANIZE_THRESHOLD],
    @UpdateStatisticsThreshold INT = [STATS_UPDATE_THRESHOLD],
    @MaxDOP INT = [MAINTENANCE_MAXDOP],
    @ExecutionMode NVARCHAR(20) = 'EXECUTE' -- 'EXECUTE' or 'REPORT'
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @SQL NVARCHAR(MAX);
    DECLARE @MaintenanceActions TABLE (
        SchemaName NVARCHAR(128),
        TableName NVARCHAR(128),
        IndexName NVARCHAR(128),
        FragmentationPercent FLOAT,
        PageCount BIGINT,
        RecommendedAction NVARCHAR(50),
        MaintenanceSQL NVARCHAR(MAX),
        Priority INT
    );

    -- Analyze index fragmentation
    INSERT INTO @MaintenanceActions
    SELECT
        OBJECT_SCHEMA_NAME(ips.object_id) as SchemaName,
        OBJECT_NAME(ips.object_id) as TableName,
        i.name as IndexName,
        ips.avg_fragmentation_in_percent as FragmentationPercent,
        ips.page_count as PageCount,
        CASE
            WHEN ips.avg_fragmentation_in_percent >= @RebuildThreshold
                AND ips.page_count > [MIN_PAGES_FOR_REBUILD]
            THEN 'REBUILD'
            WHEN ips.avg_fragmentation_in_percent >= @ReorganizeThreshold
                AND ips.page_count > [MIN_PAGES_FOR_REORGANIZE]
            THEN 'REORGANIZE'
            ELSE 'NO_ACTION'
        END as RecommendedAction,
        CASE
            WHEN ips.avg_fragmentation_in_percent >= @RebuildThreshold
                AND ips.page_count > [MIN_PAGES_FOR_REBUILD]
            THEN 'ALTER INDEX [' + i.name + '] ON [' +
                 OBJECT_SCHEMA_NAME(ips.object_id) + '].[' +
                 OBJECT_NAME(ips.object_id) + '] REBUILD WITH (MAXDOP = ' +
                 CAST(@MaxDOP AS NVARCHAR(10)) + ', ONLINE = ON);'
            WHEN ips.avg_fragmentation_in_percent >= @ReorganizeThreshold
                AND ips.page_count > [MIN_PAGES_FOR_REORGANIZE]
            THEN 'ALTER INDEX [' + i.name + '] ON [' +
                 OBJECT_SCHEMA_NAME(ips.object_id) + '].[' +
                 OBJECT_NAME(ips.object_id) + '] REORGANIZE;'
            ELSE NULL
        END as MaintenanceSQL,
        CASE
            WHEN ips.avg_fragmentation_in_percent >= @RebuildThreshold THEN 1
            WHEN ips.avg_fragmentation_in_percent >= @ReorganizeThreshold THEN 2
            ELSE 3
        END as Priority
    FROM sys.dm_db_index_physical_stats(
        DB_ID(@DatabaseName),
        OBJECT_ID(@SchemaName + '.' + @TableName),
        NULL, NULL, 'LIMITED'
    ) ips
    INNER JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
    WHERE ips.avg_fragmentation_in_percent >= @FragmentationThreshold
        AND i.type_desc IN ('CLUSTERED', 'NONCLUSTERED')
        AND (@SchemaName IS NULL OR OBJECT_SCHEMA_NAME(ips.object_id) = @SchemaName)
        AND (@TableName IS NULL OR OBJECT_NAME(ips.object_id) = @TableName);

    -- Execute maintenance actions
    IF @ExecutionMode = 'EXECUTE'
    BEGIN
        DECLARE maintenance_cursor CURSOR FOR
        SELECT MaintenanceSQL
        FROM @MaintenanceActions
        WHERE RecommendedAction != 'NO_ACTION'
        ORDER BY Priority, FragmentationPercent DESC;

        OPEN maintenance_cursor;
        FETCH NEXT FROM maintenance_cursor INTO @SQL;

        WHILE @@FETCH_STATUS = 0
        BEGIN
            BEGIN TRY
                EXEC sp_executesql @SQL;
                PRINT 'Executed: ' + @SQL;
            END TRY
            BEGIN CATCH
                PRINT 'Error executing: ' + @SQL;
                PRINT 'Error: ' + ERROR_MESSAGE();
            END CATCH

            FETCH NEXT FROM maintenance_cursor INTO @SQL;
        END

        CLOSE maintenance_cursor;
        DEALLOCATE maintenance_cursor;
    END
    ELSE
    BEGIN
        -- Report mode - show recommended actions
        SELECT * FROM @MaintenanceActions
        ORDER BY Priority, FragmentationPercent DESC;
    END
END;

SQL Query Optimization Techniques:
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

Advanced Query Patterns:
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

Query Hint Optimization:
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

PERFORMANCE MONITORING AND TUNING:

Real-time Performance Monitoring:
```sql
-- Comprehensive performance monitoring framework
CREATE VIEW [dbo].[vw_RealTimePerformanceMetrics]
AS
WITH CurrentActivityMetrics AS (
    SELECT
        r.session_id,
        r.request_id,
        r.start_time,
        r.status,
        r.command,
        r.sql_handle,
        r.statement_start_offset,
        r.statement_end_offset,
        r.plan_handle,
        r.database_id,
        r.user_id,
        r.connection_id,
        r.blocking_session_id,
        r.wait_type,
        r.wait_time,
        r.last_wait_type,
        r.wait_resource,
        r.open_transaction_count,
        r.open_resultset_count,
        r.transaction_id,
        r.context_info,
        r.percent_complete,
        r.estimated_completion_time,
        r.cpu_time,
        r.total_elapsed_time,
        r.reads,
        r.writes,
        r.logical_reads,
        r.text_size,
        r.language,
        r.date_format,
        r.date_first,
        r.quoted_identifier,
        r.arithabort,
        r.ansi_null_dflt_on,
        r.ansi_defaults,
        r.ansi_warnings,
        r.ansi_padding,
        r.ansi_nulls,
        r.concat_null_yields_null,
        r.transaction_isolation_level,
        r.lock_timeout,
        r.deadlock_priority,
        r.row_count,
        r.prev_error,
        r.original_security_id,
        r.original_login_name,
        r.last_request_start_time,
        r.last_request_end_time,
        r.is_user_process,
        r.text_size as request_text_size,
        -- Session information
        s.host_name,
        s.program_name,
        s.host_process_id,
        s.client_version,
        s.client_interface_name,
        s.security_id,
        s.login_name,
        s.nt_domain,
        s.nt_user_name,
        s.original_login_name as session_original_login_name,
        s.last_request_start_time as session_last_request_start_time,
        s.last_request_end_time as session_last_request_end_time,
        s.login_time,
        s.is_user_process as session_is_user_process
    FROM sys.dm_exec_requests r
    LEFT JOIN sys.dm_exec_sessions s ON r.session_id = s.session_id
),

[Content truncated for length - see original for full details]


## Variables

[DATABASE_PLATFORM], [ORGANIZATION_NAME], [PERFORMANCE_OBJECTIVES], [OPTIMIZATION_METHODOLOGY], [INDUSTRY_SECTOR], [WORKLOAD_TYPE], [CURRENT_PERFORMANCE_CHALLENGES], [PERFORMANCE_SLA_REQUIREMENTS], [OPTIMIZATION_BUDGET_CONSTRAINTS], [OPTIMIZATION_TIMELINE], [DATABASE_VERSION], [HARDWARE_SPECIFICATIONS], [SERVER_CONFIGURATION], [STORAGE_SYSTEM], [MEMORY_ALLOCATION], [CPU_CONFIGURATION], [NETWORK_INFRASTRUCTURE], [CLUSTER_CONFIGURATION], [CLOUD_PROVIDER], [QUERY_RESPONSE_TIME_SLA], [THROUGHPUT_REQUIREMENTS], [CONCURRENT_USER_CAPACITY], [CURRENT_DATA_VOLUME], [PROJECTED_DATA_VOLUME], [PEAK_LOAD_CHARACTERISTICS], [AVAILABILITY_REQUIREMENTS], [RTO_REQUIREMENTS], [QUERY_ID_COLUMN], [QUERY_TEXT_COLUMN], [EXECUTION_COUNT], [TOTAL_EXECUTION_TIME_MS], [AVERAGE_EXECUTION_TIME_MS], [MAX_EXECUTION_TIME_MS], [MIN_EXECUTION_TIME_MS], [TOTAL_CPU_TIME_MS], [TOTAL_LOGICAL_READS], [TOTAL_PHYSICAL_READS], [TOTAL_LOGICAL_WRITES], [COMPILATION_TIME_MS], [LAST_EXECUTION_TIME], [QUERY_PERFORMANCE_VIEW], [ANALYSIS_PERIOD_DAYS], [QUERY_HASH], [DURATION_MS], [CPU_TIME_MS], [LOGICAL_READS], [PHYSICAL_READS], [QUERY_EXECUTION_LOG], [EXECUTION_DATE], [ANALYSIS_DAYS], [TOP_N_QUERIES], [DURATION_WEIGHT], [CPU_WEIGHT], [IO_WEIGHT], [WAIT_TYPE], [WAITING_TASKS_COUNT], [WAIT_TIME_MS], [MAX_WAIT_TIME_MS], [SIGNAL_WAIT_TIME_MS], [RESOURCE_WAIT_TIME_MS], [SIGNAL_WAIT_PERCENTAGE], [WAIT_RANK], [WAIT_STATS_VIEW], [OBJECT_ID], [INDEX_NAME], [USER_SEEKS], [USER_SCANS], [USER_LOOKUPS], [USER_UPDATES], [LAST_USER_SEEK], [LAST_USER_SCAN], [LAST_USER_LOOKUP], [LAST_USER_UPDATE], [INDEX_USAGE_STATS_VIEW], [DATABASE_NAME], [PLAN_HASH], [CACHED_TIME], [TOTAL_WORKER_TIME], [TOTAL_ELAPSED_TIME], [QUERY_PLAN], [HIGH_IO_THRESHOLD], [HIGH_CPU_THRESHOLD], [HIGH_DURATION_THRESHOLD], [PLAN_CACHE_VIEW], [ANALYSIS_HOURS], [SCHEMA_NAME], [TABLE_NAME], [COLUMN_NAME], [COLUMN_USAGE], [AVG_TOTAL_USER_COST], [AVG_USER_IMPACT], [SYSTEM_SEEKS], [SYSTEM_SCANS], [MISSING_INDEX_DETAILS_VIEW], [INDEX_GROUP_HANDLE], [MISSING_INDEX_GROUPS_VIEW], [GROUP_HANDLE], [MISSING_INDEX_GROUP_STATS_VIEW], [TARGET_DATABASE], [PATTERN_ANALYSIS_DAYS], [COMPLEXITY_ANALYSIS_DAYS], [LENGTH_WEIGHT], [JOIN_WEIGHT], [WHERE_WEIGHT], [GROUP_WEIGHT], [ORDER_WEIGHT], [UNION_WEIGHT], [FILL_FACTOR_PERCENTAGE], [PAD_INDEX_SETTING], [IGNORE_DUPLICATE_SETTING], [ROW_LOCK_SETTING], [PAGE_LOCK_SETTING], [MAX_DEGREE_PARALLELISM], [ONLINE_INDEX_CREATION], [FILTERED_FILL_FACTOR], [COLUMNSTORE_MAXDOP], [COMPRESSION_DELAY_MINUTES], [COLUMNSTORE_COMPRESSION], [PARTITION_SCHEME], [PARTITION_KEY], [INDEX_KEY_COLUMNS], [DEFAULT_FRAGMENTATION_THRESHOLD], [REBUILD_THRESHOLD], [REORGANIZE_THRESHOLD], [STATS_UPDATE_THRESHOLD], [MAINTENANCE_MAXDOP], [MIN_PAGES_FOR_REBUILD], [MIN_PAGES_FOR_REORGANIZE], [LOG_PATH], [TABLE_A], [TABLE_B], [FILTER_CONDITION], [FILTER_VALUE], [COLUMN_LIST], [KEY_COLUMN], [FOREIGN_KEY], [ACTIVE_STATUS], [CONDITION_A], [CONDITION_B], [PARTITION_COLUMN], [DATE_COLUMN], [LARGE_TABLE], [REFERENCE_TABLE], [SORT_COLUMN_1], [SORT_COLUMN_2], [REQUIRED_COLUMN_1], [REQUIRED_COLUMN_2], [LOOKUP_VALUE], [SOURCE_COLUMN], [MAPPED_COLUMN], [CALCULATED_COLUMN_1], [CALCULATION_LOGIC_1], [CALCULATED_COLUMN_2], [CALCULATION_LOGIC_2], [CTE_NAME_1], [DIMENSION_COLUMNS], [MEASURE_COLUMNS], [FACT_TABLE], [START_DATE], [END_DATE], [STATUS_FILTER], [CTE_NAME_2], [GROUPING_COLUMNS], [MEASURE_1], [MEASURE_2], [CTE_NAME_3], [PARTITION_COLUMNS], [DATE_GROUPING], [FINAL_COLUMN_LIST], [TOP_N_LIMIT], [SORT_COLUMNS], [THRESHOLD_VALUE], [HIGH_CATEGORY], [MEDIUM_THRESHOLD], [MEDIUM_CATEGORY], [LOW_CATEGORY], [ROW_IDENTIFIER], [PIVOT_VALUE_1], [PIVOT_VALUE_2], [PIVOT_VALUE_3], [PIVOT_VALUE_4], [PIVOT_COLUMN], [VALUE_COLUMN], [SOURCE_TABLE], [FILTER_CONDITIONS], [ROWS_TO_SKIP], [PAGE_SIZE], [SPECIFIC_INDEX_NAME], [SPECIFIC_MAXDOP], [HINT_NAME], [COVERING_INDEX_NAME], [INDEXED_COLUMN], [KEY], [KEY2], [LONG_RUNNING_THRESHOLD_MS], [HIGH_CPU_THRESHOLD_MS], [HIGH_IO_THRESHOLD], [LONG_RUNNING_ALERT_MINUTES], [HIGH_CPU_ALERT_PERCENTAGE], [BLOCKED_QUERY_ALERT_MINUTES], [HIGH_IO_ALERT_THRESHOLD], [DEADLOCK_ALERT_COUNT], [WAIT_TIME_ALERT_MINUTES], [DEFAULT_TUNING_MINUTES], [MIN_INDEX_IMPACT_THRESHOLD], [MIN_INDEX_USAGE_THRESHOLD], [STATS_UPDATE_THRESHOLD_DAYS], [REORGANIZE_FRAGMENTATION_THRESHOLD], [MIN_PAGES_FOR_MAINTENANCE], [LARGE_BUFFER_THRESHOLD], [HIGH_READ_LATENCY_THRESHOLD], [LARGE_TABLE_THRESHOLD], [MEMORY_THRESHOLD_KB], [HIGH_READ_LATENCY_THRESHOLD], [HIGH_WRITE_LATENCY_THRESHOLD], [HIGH_TOTAL_STALL_THRESHOLD], [LARGE_FILE_THRESHOLD], [DATA_PATH], [INITIAL_FILEGROUP_SIZE], [FILEGROUP_GROWTH], [OPTIMAL_GROWTH_SIZE_MB], [MIN_SIZE_FOR_FIXED_GROWTH_MB], [UNUSED_UPDATE_THRESHOLD], [SCAN_THRESHOLD], [FRAGMENTATION_THRESHOLD], [HIGH_USAGE_THRESHOLD], [SCAN_SEEK_RATIO_THRESHOLD], [MIN_RECOMMENDED_INDEXES], [HIGH_SEEK_THRESHOLD], [MAX_RECOMMENDED_INDEXES], [COMPOSITE_DESCRIPTION], [KEY_COLUMN_1], [KEY_COLUMN_2], [KEY_COLUMN_3], [INCLUDED_COLUMN_1], [INCLUDED_COLUMN_2], [INCLUDED_COLUMN_3], [FILTERED_DESCRIPTION], [FILTER_COLUMN_1], [FILTER_COLUMN_2], [INCLUDED_COLUMNS], [ANALYTICS_DESCRIPTION], [PARTITIONED_DESCRIPTION], [LONG_WAIT_THRESHOLD_MS], [LONG_TRANSACTION_THRESHOLD_MS], [CONCURRENCY_WAIT_THRESHOLD_MS]

## Usage Examples

### Example 1: OLAP Data Warehouse Optimization
```
DATABASE_PLATFORM: "SQL Server 2022"
ORGANIZATION_NAME: "DataMart Solutions"
WORKLOAD_TYPE: "OLAP"
OPTIMIZATION_METHODOLOGY: "Comprehensive analysis with columnstore optimization"
PERFORMANCE_OBJECTIVES: "Reduce query response time by 60% and increase throughput"
QUERY_RESPONSE_TIME_SLA: "< 30 seconds for analytical queries"
CLOUD_PROVIDER: "Azure"
```


### Example 2: High-Volume OLTP System
```
DATABASE_PLATFORM: "PostgreSQL 15"
ORGANIZATION_NAME: "E-commerce Platform"
WORKLOAD_TYPE: "OLTP"
OPTIMIZATION_METHODOLOGY: "Concurrency and indexing optimization"
PERFORMANCE_OBJECTIVES: "Support 10,000 concurrent users with < 100ms response"
CONCURRENT_USER_CAPACITY: "10000"
THROUGHPUT_REQUIREMENTS: "50000 transactions/minute"
CURRENT_DATA_VOLUME: "5TB"
```


### Example 3: Mixed Analytical Workload
```
DATABASE_PLATFORM: "Snowflake"
ORGANIZATION_NAME: "Financial Analytics Corp"
WORKLOAD_TYPE: "Hybrid"
OPTIMIZATION_METHODOLOGY: "Query optimization with storage optimization"
PERFORMANCE_OBJECTIVES: "Optimize complex analytical queries and reduce compute costs"
QUERY_RESPONSE_TIME_SLA: "< 5 minutes for complex analytics"
PEAK_LOAD_CHARACTERISTICS: "Morning batch processing + real-time queries"
```


## Best Practices

1. **Focus**: Concentrate on the specific aspect covered by this template
2. **Integration**: Combine with related templates for comprehensive solutions
3. **Iteration**: Start simple and refine based on results
4. **Documentation**: Track your parameters and customizations

## Tips for Success

- Begin with the Quick Start section
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This focused template is part of a comprehensive collection designed for improved usability.
