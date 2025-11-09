# Query Optimization & Performance Template

## Purpose
Design comprehensive SQL query optimization strategies including performance tuning methodologies, indexing strategies, query efficiency analysis, and database performance optimization for analytical workloads.

## Template

```
You are a database performance optimization expert specializing in [DATABASE_PLATFORM]. Design a comprehensive query optimization and performance tuning strategy for [ORGANIZATION_NAME] to improve [PERFORMANCE_OBJECTIVES] using [OPTIMIZATION_METHODOLOGY] approach.

PERFORMANCE OPTIMIZATION OVERVIEW:
Project Context:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Database platform: [DATABASE_PLATFORM]
- Workload type: [WORKLOAD_TYPE] (OLTP/OLAP/Hybrid/Analytics)
- Performance objectives: [PERFORMANCE_OBJECTIVES]
- Current challenges: [CURRENT_PERFORMANCE_CHALLENGES]
- SLA requirements: [PERFORMANCE_SLA_REQUIREMENTS]
- Budget constraints: [OPTIMIZATION_BUDGET_CONSTRAINTS]
- Timeline: [OPTIMIZATION_TIMELINE]

System Architecture:
- Database version: [DATABASE_VERSION]
- Hardware specifications: [HARDWARE_SPECIFICATIONS]
- Server configuration: [SERVER_CONFIGURATION]
- Storage system: [STORAGE_SYSTEM]
- Memory allocation: [MEMORY_ALLOCATION]
- CPU configuration: [CPU_CONFIGURATION]
- Network infrastructure: [NETWORK_INFRASTRUCTURE]
- Cluster setup: [CLUSTER_CONFIGURATION]
- Cloud provider: [CLOUD_PROVIDER] (if applicable)

Performance Requirements:
- Query response time SLA: [QUERY_RESPONSE_TIME_SLA]
- Throughput requirements: [THROUGHPUT_REQUIREMENTS]
- Concurrent user capacity: [CONCURRENT_USER_CAPACITY]
- Data volume current: [CURRENT_DATA_VOLUME]
- Data volume projected: [PROJECTED_DATA_VOLUME]
- Peak load characteristics: [PEAK_LOAD_CHARACTERISTICS]
- Availability requirements: [AVAILABILITY_REQUIREMENTS]
- Recovery time objectives: [RTO_REQUIREMENTS]

QUERY ANALYSIS AND PROFILING:
Performance Baseline Assessment:
Current Performance Metrics:
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
```

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
```

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
```

INDEXING STRATEGY OPTIMIZATION:
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
```

Advanced Index Design:
```sql
-- Composite index optimization
CREATE INDEX [IX_[TABLE_NAME]_[COMPOSITE_DESCRIPTION]]
ON [SCHEMA].[TABLE_NAME] (
    [KEY_COLUMN_1] ASC,     -- Most selective column first
    [KEY_COLUMN_2] ASC,     -- Second most selective
    [KEY_COLUMN_3] DESC     -- Order by column if applicable
)
INCLUDE (
    [INCLUDED_COLUMN_1],    -- Frequently selected columns
    [INCLUDED_COLUMN_2],    -- Avoid key lookups
    [INCLUDED_COLUMN_3]
)
WITH (
    FILLFACTOR = [FILL_FACTOR_PERCENTAGE],      -- Leave space for inserts
    PAD_INDEX = [PAD_INDEX_SETTING],            -- Apply fill factor to intermediate levels
    IGNORE_DUP_KEY = [IGNORE_DUPLICATE_SETTING], -- Handle duplicate key errors
    ALLOW_ROW_LOCKS = [ROW_LOCK_SETTING],       -- Row-level locking
    ALLOW_PAGE_LOCKS = [PAGE_LOCK_SETTING],     -- Page-level locking
    MAXDOP = [MAX_DEGREE_PARALLELISM],          -- Parallel index creation
    ONLINE = [ONLINE_INDEX_CREATION]            -- Online index operations
);

-- Filtered index for selective data
CREATE NONCLUSTERED INDEX [IX_[TABLE_NAME]_[FILTERED_DESCRIPTION]]
ON [SCHEMA].[TABLE_NAME] (
    [FILTER_COLUMN_1],
    [FILTER_COLUMN_2]
)
INCLUDE ([INCLUDED_COLUMNS])
WHERE [FILTER_CONDITION]  -- e.g., [STATUS] = 'ACTIVE' AND [DATE_COLUMN] >= '2024-01-01'
WITH (FILLFACTOR = [FILTERED_FILL_FACTOR]);

-- Columnstore index for analytics
CREATE CLUSTERED COLUMNSTORE INDEX [CCI_[TABLE_NAME]_[ANALYTICS_DESCRIPTION]]
ON [SCHEMA].[TABLE_NAME]
WITH (
    MAXDOP = [COLUMNSTORE_MAXDOP],
    COMPRESSION_DELAY = [COMPRESSION_DELAY_MINUTES] MINUTES,
    DATA_COMPRESSION = [COLUMNSTORE_COMPRESSION] -- COLUMNSTORE/COLUMNSTORE_ARCHIVE
);

-- Partitioned index design
CREATE NONCLUSTERED INDEX [IX_[TABLE_NAME]_[PARTITIONED_DESCRIPTION]]
ON [SCHEMA].[TABLE_NAME] (
    [PARTITION_KEY],        -- Align with table partitioning
    [INDEX_KEY_COLUMNS]
)
ON [PARTITION_SCHEME] ([PARTITION_KEY]);
```

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
```

QUERY REWRITING AND OPTIMIZATION:
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
```

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
```

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
```

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
QueryTextExtraction AS (
    SELECT 
        cam.*,
        -- Extract query text
        SUBSTRING(
            qt.text,
            (cam.statement_start_offset / 2) + 1,
            ((CASE WHEN cam.statement_end_offset = -1
                   THEN DATALENGTH(qt.text)
                   ELSE cam.statement_end_offset
              END - cam.statement_start_offset) / 2) + 1
        ) AS query_text,
        qt.text as full_batch_text
    FROM CurrentActivityMetrics cam
    CROSS APPLY sys.dm_exec_sql_text(cam.sql_handle) qt
)
SELECT 
    session_id,
    request_id,
    start_time,
    status,
    command,
    DB_NAME(database_id) as database_name,
    login_name,
    host_name,
    program_name,
    blocking_session_id,
    wait_type,
    wait_time,
    wait_resource,
    percent_complete,
    estimated_completion_time,
    cpu_time,
    total_elapsed_time,
    reads,
    writes,
    logical_reads,
    open_transaction_count,
    query_text,
    -- Performance calculations
    CASE 
        WHEN total_elapsed_time > 0 
        THEN (cpu_time * 100.0) / total_elapsed_time 
        ELSE 0 
    END as cpu_percentage,
    CASE 
        WHEN total_elapsed_time > [LONG_RUNNING_THRESHOLD_MS] THEN 'LONG_RUNNING'
        WHEN cpu_time > [HIGH_CPU_THRESHOLD_MS] THEN 'HIGH_CPU'
        WHEN logical_reads > [HIGH_IO_THRESHOLD] THEN 'HIGH_IO'
        WHEN blocking_session_id IS NOT NULL THEN 'BLOCKED'
        ELSE 'NORMAL'
    END as performance_category
FROM QueryTextExtraction
WHERE status NOT IN ('background', 'sleeping')
    OR blocking_session_id IS NOT NULL;

-- Automated performance alert system
CREATE PROCEDURE [dbo].[sp_PerformanceAlertMonitor]
    @AlertThresholds NVARCHAR(MAX) = NULL, -- JSON configuration
    @NotificationMethod NVARCHAR(50) = 'EMAIL',
    @ExecutionMode NVARCHAR(20) = 'MONITOR' -- MONITOR/TEST
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Default thresholds if not provided
    IF @AlertThresholds IS NULL
    SET @AlertThresholds = N'{
        "long_running_query_minutes": [LONG_RUNNING_ALERT_MINUTES],
        "high_cpu_percentage": [HIGH_CPU_ALERT_PERCENTAGE],
        "blocked_query_minutes": [BLOCKED_QUERY_ALERT_MINUTES],
        "high_io_reads": [HIGH_IO_ALERT_THRESHOLD],
        "deadlock_count_threshold": [DEADLOCK_ALERT_COUNT],
        "wait_time_minutes": [WAIT_TIME_ALERT_MINUTES]
    }';
    
    DECLARE @Alerts TABLE (
        AlertType NVARCHAR(50),
        Severity NVARCHAR(20),
        Description NVARCHAR(500),
        SessionId INT,
        QueryText NVARCHAR(MAX),
        Recommendation NVARCHAR(500)
    );
    
    -- Check for long-running queries
    INSERT INTO @Alerts
    SELECT 
        'LONG_RUNNING_QUERY' as AlertType,
        'HIGH' as Severity,
        'Query has been running for ' + 
        CAST((total_elapsed_time / 1000 / 60) AS NVARCHAR(10)) + ' minutes' as Description,
        session_id as SessionId,
        query_text as QueryText,
        'Review query execution plan and consider optimization' as Recommendation
    FROM [dbo].[vw_RealTimePerformanceMetrics]
    WHERE total_elapsed_time > (JSON_VALUE(@AlertThresholds, '$.long_running_query_minutes') * 60 * 1000)
        AND status = 'running';
    
    -- Check for blocked queries
    INSERT INTO @Alerts
    SELECT 
        'BLOCKED_QUERY' as AlertType,
        'MEDIUM' as Severity,
        'Query blocked by session ' + CAST(blocking_session_id AS NVARCHAR(10)) as Description,
        session_id as SessionId,
        query_text as QueryText,
        'Investigate blocking session and consider query optimization' as Recommendation
    FROM [dbo].[vw_RealTimePerformanceMetrics]
    WHERE blocking_session_id IS NOT NULL
        AND wait_time > (JSON_VALUE(@AlertThresholds, '$.blocked_query_minutes') * 60 * 1000);
    
    -- Check for high CPU queries
    INSERT INTO @Alerts
    SELECT 
        'HIGH_CPU_QUERY' as AlertType,
        'MEDIUM' as Severity,
        'Query consuming ' + CAST(cpu_percentage AS NVARCHAR(10)) + '% CPU' as Description,
        session_id as SessionId,
        query_text as QueryText,
        'Analyze query plan for CPU-intensive operations' as Recommendation
    FROM [dbo].[vw_RealTimePerformanceMetrics]
    WHERE cpu_percentage > JSON_VALUE(@AlertThresholds, '$.high_cpu_percentage');
    
    -- Send alerts
    IF EXISTS (SELECT 1 FROM @Alerts) AND @ExecutionMode = 'MONITOR'
    BEGIN
        DECLARE @AlertMessage NVARCHAR(MAX);
        SELECT @AlertMessage = STRING_AGG(
            AlertType + ': ' + Description + 
            ' (Session: ' + CAST(SessionId AS NVARCHAR(10)) + ')', 
            CHAR(13) + CHAR(10)
        )
        FROM @Alerts;
        
        -- Send notification (implementation depends on notification system)
        EXEC [dbo].[sp_SendAlert] 
            @AlertType = 'DATABASE_PERFORMANCE',
            @Severity = 'HIGH',
            @Message = @AlertMessage,
            @Method = @NotificationMethod;
    END
    
    -- Return alert details for review
    SELECT * FROM @Alerts ORDER BY Severity, AlertType;
END;
```

Automated Performance Tuning:
```sql
-- Self-tuning database maintenance
CREATE PROCEDURE [dbo].[sp_AutoPerformanceTuning]
    @DatabaseName NVARCHAR(128) = NULL,
    @TuningScope NVARCHAR(50) = 'COMPREHENSIVE', -- INDEXES/STATISTICS/COMPREHENSIVE
    @ExecutionMode NVARCHAR(20) = 'EXECUTE',     -- REPORT/EXECUTE
    @MaxExecutionMinutes INT = [DEFAULT_TUNING_MINUTES],
    @PerformanceThresholds NVARCHAR(MAX) = NULL
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @StartTime DATETIME2 = GETDATE();
    DECLARE @TuningActions TABLE (
        ActionType NVARCHAR(50),
        Priority INT,
        TableName NVARCHAR(128),
        ActionDescription NVARCHAR(500),
        EstimatedImpact NVARCHAR(20),
        ExecutionSQL NVARCHAR(MAX),
        ExecutionStatus NVARCHAR(20) DEFAULT 'PENDING',
        ExecutionTime DATETIME2
    );
    
    -- 1. Identify missing indexes with high impact
    IF @TuningScope IN ('INDEXES', 'COMPREHENSIVE')
    BEGIN
        INSERT INTO @TuningActions
        SELECT 
            'CREATE_INDEX' as ActionType,
            1 as Priority,
            OBJECT_NAME(mid.object_id) as TableName,
            'Create index on ' + ISNULL(mid.equality_columns, '') + 
            CASE WHEN mid.inequality_columns IS NOT NULL 
                 THEN ' (inequality: ' + mid.inequality_columns + ')'
                 ELSE '' END as ActionDescription,
            CASE 
                WHEN migs.avg_user_impact > 80 THEN 'HIGH'
                WHEN migs.avg_user_impact > 50 THEN 'MEDIUM'
                ELSE 'LOW'
            END as EstimatedImpact,
            'CREATE NONCLUSTERED INDEX [IX_' + OBJECT_NAME(mid.object_id) + '_' + 
            FORMAT(GETDATE(), 'yyyyMMdd_HHmm') + '_AUTO] ON [' + 
            OBJECT_SCHEMA_NAME(mid.object_id) + '].[' + OBJECT_NAME(mid.object_id) + '] (' +
            ISNULL(mid.equality_columns, '') +
            CASE WHEN mid.inequality_columns IS NOT NULL 
                 THEN CASE WHEN mid.equality_columns IS NOT NULL THEN ', ' ELSE '' END + 
                      mid.inequality_columns 
                 ELSE '' END +
            ')' +
            CASE WHEN mid.included_columns IS NOT NULL 
                 THEN ' INCLUDE (' + mid.included_columns + ')' 
                 ELSE '' END +
            ' WITH (FILLFACTOR = 90, ONLINE = ON);' as ExecutionSQL,
            'PENDING' as ExecutionStatus,
            NULL as ExecutionTime
        FROM sys.dm_db_missing_index_details mid
        INNER JOIN sys.dm_db_missing_index_groups mig 
            ON mid.index_group_handle = mig.index_group_handle
        INNER JOIN sys.dm_db_missing_index_group_stats migs 
            ON mig.index_group_handle = migs.group_handle
        WHERE migs.avg_user_impact > [MIN_INDEX_IMPACT_THRESHOLD]
            AND migs.user_seeks + migs.user_scans > [MIN_INDEX_USAGE_THRESHOLD]
            AND mid.database_id = DB_ID(@DatabaseName);
    END
    
    -- 2. Update outdated statistics
    IF @TuningScope IN ('STATISTICS', 'COMPREHENSIVE')
    BEGIN
        INSERT INTO @TuningActions
        SELECT 
            'UPDATE_STATISTICS' as ActionType,
            2 as Priority,
            OBJECT_NAME(s.object_id) as TableName,
            'Update statistics for ' + s.name as ActionDescription,
            CASE 
                WHEN DATEDIFF(day, sp.last_updated, GETDATE()) > 7 THEN 'HIGH'
                WHEN DATEDIFF(day, sp.last_updated, GETDATE()) > 3 THEN 'MEDIUM'
                ELSE 'LOW'
            END as EstimatedImpact,
            'UPDATE STATISTICS [' + OBJECT_SCHEMA_NAME(s.object_id) + '].[' + 
            OBJECT_NAME(s.object_id) + '] [' + s.name + '] WITH FULLSCAN;' as ExecutionSQL,
            'PENDING' as ExecutionStatus,
            NULL as ExecutionTime
        FROM sys.stats s
        CROSS APPLY sys.dm_db_stats_properties(s.object_id, s.stats_id) sp
        WHERE DATEDIFF(day, sp.last_updated, GETDATE()) > [STATS_UPDATE_THRESHOLD_DAYS]
            AND OBJECT_SCHEMA_NAME(s.object_id) != 'sys'
            AND (@DatabaseName IS NULL OR DB_NAME() = @DatabaseName);
    END
    
    -- 3. Reorganize fragmented indexes
    IF @TuningScope IN ('INDEXES', 'COMPREHENSIVE')
    BEGIN
        INSERT INTO @TuningActions
        SELECT 
            'REORGANIZE_INDEX' as ActionType,
            3 as Priority,
            OBJECT_NAME(ips.object_id) as TableName,
            'Reorganize fragmented index ' + i.name + 
            ' (fragmentation: ' + CAST(ROUND(ips.avg_fragmentation_in_percent, 1) AS NVARCHAR(10)) + '%)' as ActionDescription,
            CASE 
                WHEN ips.avg_fragmentation_in_percent > 50 THEN 'HIGH'
                WHEN ips.avg_fragmentation_in_percent > 30 THEN 'MEDIUM'
                ELSE 'LOW'
            END as EstimatedImpact,
            'ALTER INDEX [' + i.name + '] ON [' + OBJECT_SCHEMA_NAME(ips.object_id) + '].[' + 
            OBJECT_NAME(ips.object_id) + '] REORGANIZE;' as ExecutionSQL,
            'PENDING' as ExecutionStatus,
            NULL as ExecutionTime
        FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'LIMITED') ips
        INNER JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
        WHERE ips.avg_fragmentation_in_percent > [REORGANIZE_FRAGMENTATION_THRESHOLD]
            AND ips.page_count > [MIN_PAGES_FOR_MAINTENANCE]
            AND i.type_desc IN ('CLUSTERED', 'NONCLUSTERED');
    END
    
    -- Execute tuning actions
    IF @ExecutionMode = 'EXECUTE'
    BEGIN
        DECLARE @ActionSQL NVARCHAR(MAX);
        DECLARE @ActionType NVARCHAR(50);
        DECLARE @TableName NVARCHAR(128);
        
        DECLARE tuning_cursor CURSOR FOR
        SELECT ExecutionSQL, ActionType, TableName
        FROM @TuningActions
        WHERE EstimatedImpact IN ('HIGH', 'MEDIUM')
        ORDER BY Priority, EstimatedImpact DESC;
        
        OPEN tuning_cursor;
        FETCH NEXT FROM tuning_cursor INTO @ActionSQL, @ActionType, @TableName;
        
        WHILE @@FETCH_STATUS = 0 AND DATEDIFF(minute, @StartTime, GETDATE()) < @MaxExecutionMinutes
        BEGIN
            BEGIN TRY
                EXEC sp_executesql @ActionSQL;
                
                UPDATE @TuningActions
                SET ExecutionStatus = 'SUCCESS',
                    ExecutionTime = GETDATE()
                WHERE ExecutionSQL = @ActionSQL;
                
                PRINT 'SUCCESS: ' + @ActionType + ' on ' + @TableName;
                
            END TRY
            BEGIN CATCH
                UPDATE @TuningActions
                SET ExecutionStatus = 'FAILED',
                    ExecutionTime = GETDATE()
                WHERE ExecutionSQL = @ActionSQL;
                
                PRINT 'FAILED: ' + @ActionType + ' on ' + @TableName + ' - ' + ERROR_MESSAGE();
            END CATCH
            
            FETCH NEXT FROM tuning_cursor INTO @ActionSQL, @ActionType, @TableName;
        END
        
        CLOSE tuning_cursor;
        DEALLOCATE tuning_cursor;
    END
    
    -- Return tuning results
    SELECT 
        ActionType,
        Priority,
        TableName,
        ActionDescription,
        EstimatedImpact,
        ExecutionStatus,
        ExecutionTime,
        CASE WHEN @ExecutionMode = 'REPORT' THEN ExecutionSQL ELSE NULL END as ProposedSQL
    FROM @TuningActions
    ORDER BY Priority, EstimatedImpact DESC, ExecutionStatus;
    
END;
```

MEMORY AND STORAGE OPTIMIZATION:
Buffer Pool and Memory Management:
```sql
-- Buffer pool analysis and optimization
CREATE VIEW [dbo].[vw_BufferPoolAnalysis]
AS
WITH BufferPoolStats AS (
    SELECT 
        DB_NAME(bd.database_id) as database_name,
        OBJECT_SCHEMA_NAME(p.object_id, bd.database_id) as schema_name,
        OBJECT_NAME(p.object_id, bd.database_id) as table_name,
        i.name as index_name,
        i.type_desc as index_type,
        COUNT(*) as buffer_page_count,
        COUNT(*) * 8 / 1024 as buffer_size_mb,
        SUM(CASE WHEN bd.is_modified = 1 THEN 1 ELSE 0 END) as dirty_page_count,
        AVG(bd.read_microsec) as avg_read_microsec,
        MAX(bd.read_microsec) as max_read_microsec
    FROM sys.dm_os_buffer_descriptors bd
    INNER JOIN sys.allocation_units au ON bd.allocation_unit_id = au.allocation_unit_id
    INNER JOIN sys.partitions p ON au.container_id = p.partition_id
    INNER JOIN sys.indexes i ON p.object_id = i.object_id AND p.index_id = i.index_id
    WHERE bd.database_id = DB_ID()
        AND p.object_id > 100  -- Exclude system objects
    GROUP BY 
        bd.database_id,
        p.object_id,
        i.index_id,
        i.name,
        i.type_desc
),
TableSizeStats AS (
    SELECT 
        OBJECT_SCHEMA_NAME(p.object_id) as schema_name,
        OBJECT_NAME(p.object_id) as table_name,
        SUM(a.total_pages) * 8 / 1024 as total_size_mb,
        SUM(a.used_pages) * 8 / 1024 as used_size_mb,
        SUM(a.data_pages) * 8 / 1024 as data_size_mb
    FROM sys.partitions p
    INNER JOIN sys.allocation_units a ON p.partition_id = a.container_id
    WHERE p.object_id > 100
    GROUP BY p.object_id
)
SELECT 
    bps.database_name,
    bps.schema_name,
    bps.table_name,
    bps.index_name,
    bps.index_type,
    bps.buffer_page_count,
    bps.buffer_size_mb,
    tss.total_size_mb as table_total_size_mb,
    CASE 
        WHEN tss.total_size_mb > 0 
        THEN (bps.buffer_size_mb * 100.0) / tss.total_size_mb 
        ELSE 0 
    END as buffer_cache_hit_ratio,
    bps.dirty_page_count,
    bps.avg_read_microsec,
    bps.max_read_microsec,
    -- Buffer efficiency classification
    CASE 
        WHEN (bps.buffer_size_mb * 100.0) / NULLIF(tss.total_size_mb, 0) > 80 THEN 'HOT_DATA'
        WHEN (bps.buffer_size_mb * 100.0) / NULLIF(tss.total_size_mb, 0) > 50 THEN 'WARM_DATA'
        WHEN (bps.buffer_size_mb * 100.0) / NULLIF(tss.total_size_mb, 0) > 20 THEN 'COOL_DATA'
        ELSE 'COLD_DATA'
    END as data_temperature,
    -- Optimization recommendations
    CASE 
        WHEN bps.buffer_size_mb > [LARGE_BUFFER_THRESHOLD] AND bps.avg_read_microsec > [HIGH_READ_LATENCY_THRESHOLD]
        THEN 'CONSIDER_INDEX_OPTIMIZATION'
        WHEN (bps.buffer_size_mb * 100.0) / NULLIF(tss.total_size_mb, 0) < 10 AND tss.total_size_mb > [LARGE_TABLE_THRESHOLD]
        THEN 'CONSIDER_PARTITIONING'
        WHEN bps.dirty_page_count > bps.buffer_page_count * 0.5
        THEN 'HIGH_WRITE_ACTIVITY'
        ELSE 'OPTIMAL'
    END as optimization_recommendation
FROM BufferPoolStats bps
INNER JOIN TableSizeStats tss ON bps.schema_name = tss.schema_name AND bps.table_name = tss.table_name;

-- Memory pressure analysis
SELECT 
    -- Memory clerks analysis
    mc.type as memory_clerk_type,
    SUM(mc.pages_kb) / 1024 as memory_used_mb,
    COUNT(*) as clerk_count,
    AVG(mc.pages_kb) / 1024 as avg_memory_per_clerk_mb
FROM sys.dm_os_memory_clerks mc
GROUP BY mc.type
HAVING SUM(mc.pages_kb) > [MEMORY_THRESHOLD_KB]
ORDER BY memory_used_mb DESC;

-- Wait statistics for memory pressure
SELECT 
    wait_type,
    waiting_tasks_count,
    wait_time_ms / 1000.0 as wait_time_seconds,
    max_wait_time_ms / 1000.0 as max_wait_time_seconds,
    signal_wait_time_ms / 1000.0 as signal_wait_time_seconds
FROM sys.dm_os_wait_stats
WHERE wait_type IN (
    'RESOURCE_SEMAPHORE',
    'RESOURCE_SEMAPHORE_QUERY_COMPILE', 
    'RESOURCE_SEMAPHORE_MUTEX',
    'RESOURCE_SEMAPHORE_RESERVE',
    'RESOURCE_SEMAPHORE_SMALL_QUERY'
)
    AND waiting_tasks_count > 0
ORDER BY wait_time_ms DESC;
```

Storage Optimization:
```sql
-- Storage I/O analysis and optimization
CREATE FUNCTION [dbo].[fn_GetStoragePerformanceMetrics]()
RETURNS TABLE
AS
RETURN
WITH DriveStats AS (
    SELECT 
        vfs.database_id,
        DB_NAME(vfs.database_id) as database_name,
        vfs.file_id,
        mf.name as logical_file_name,
        mf.physical_name,
        mf.type_desc as file_type,
        vfs.num_of_reads,
        vfs.num_of_bytes_read,
        vfs.io_stall_read_ms,
        vfs.num_of_writes,
        vfs.num_of_bytes_written,
        vfs.io_stall_write_ms,
        vfs.io_stall as total_io_stall_ms,
        vfs.size_on_disk_bytes / 1024 / 1024 as file_size_mb,
        -- Calculate I/O performance metrics
        CASE 
            WHEN vfs.num_of_reads > 0 
            THEN vfs.io_stall_read_ms / vfs.num_of_reads 
            ELSE 0 
        END as avg_read_latency_ms,
        CASE 
            WHEN vfs.num_of_writes > 0 
            THEN vfs.io_stall_write_ms / vfs.num_of_writes 
            ELSE 0 
        END as avg_write_latency_ms,
        CASE 
            WHEN vfs.num_of_reads > 0 
            THEN (vfs.num_of_bytes_read / vfs.num_of_reads) / 1024 
            ELSE 0 
        END as avg_read_size_kb,
        CASE 
            WHEN vfs.num_of_writes > 0 
            THEN (vfs.num_of_bytes_written / vfs.num_of_writes) / 1024 
            ELSE 0 
        END as avg_write_size_kb
    FROM sys.dm_io_virtual_file_stats(NULL, NULL) vfs
    INNER JOIN sys.master_files mf ON vfs.database_id = mf.database_id AND vfs.file_id = mf.file_id
    WHERE mf.state = 0  -- Online files only
)
SELECT 
    *,
    -- Performance classification
    CASE 
        WHEN avg_read_latency_ms > [HIGH_READ_LATENCY_THRESHOLD] THEN 'HIGH_READ_LATENCY'
        WHEN avg_write_latency_ms > [HIGH_WRITE_LATENCY_THRESHOLD] THEN 'HIGH_WRITE_LATENCY'
        WHEN total_io_stall_ms > [HIGH_TOTAL_STALL_THRESHOLD] THEN 'HIGH_IO_PRESSURE'
        ELSE 'NORMAL'
    END as performance_status,
    -- Optimization recommendations
    CASE 
        WHEN avg_read_latency_ms > [HIGH_READ_LATENCY_THRESHOLD] AND file_type = 'ROWS'
        THEN 'CONSIDER_FASTER_STORAGE_FOR_DATA'
        WHEN avg_write_latency_ms > [HIGH_WRITE_LATENCY_THRESHOLD] AND file_type = 'LOG'
        THEN 'CONSIDER_FASTER_STORAGE_FOR_LOG'
        WHEN file_size_mb > [LARGE_FILE_THRESHOLD]
        THEN 'CONSIDER_FILE_PARTITIONING'
        ELSE 'OPTIMAL'
    END as optimization_recommendation
FROM DriveStats;

-- Automated storage optimization
CREATE PROCEDURE [dbo].[sp_OptimizeStorageConfiguration]
    @DatabaseName NVARCHAR(128) = NULL,
    @OptimizationType NVARCHAR(50) = 'COMPREHENSIVE', -- FILEGROUPS/PARTITIONING/COMPREHENSIVE
    @ExecutionMode NVARCHAR(20) = 'REPORT' -- REPORT/EXECUTE
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @OptimizationActions TABLE (
        ActionType NVARCHAR(50),
        Priority INT,
        Description NVARCHAR(500),
        ExecutionSQL NVARCHAR(MAX),
        EstimatedBenefit NVARCHAR(100)
    );
    
    -- Analyze current storage configuration
    DECLARE @CurrentConfig TABLE (
        database_name NVARCHAR(128),
        file_name NVARCHAR(128),
        file_type NVARCHAR(20),
        file_size_mb INT,
        growth_setting NVARCHAR(50),
        max_size_mb INT,
        is_percent_growth BIT,
        growth_increment INT
    );
    
    INSERT INTO @CurrentConfig
    SELECT 
        DB_NAME(database_id) as database_name,
        name as file_name,
        type_desc as file_type,
        size * 8 / 1024 as file_size_mb,
        CASE 
            WHEN is_percent_growth = 1 
            THEN CAST(growth AS NVARCHAR(20)) + '%'
            ELSE CAST(growth * 8 / 1024 AS NVARCHAR(20)) + 'MB'
        END as growth_setting,
        CASE 
            WHEN max_size = -1 THEN -1
            ELSE max_size * 8 / 1024
        END as max_size_mb,
        is_percent_growth,
        growth
    FROM sys.master_files
    WHERE database_id = DB_ID(@DatabaseName) OR @DatabaseName IS NULL;
    
    -- Recommend filegroup optimizations
    IF @OptimizationType IN ('FILEGROUPS', 'COMPREHENSIVE')
    BEGIN
        -- Check for single filegroup usage
        INSERT INTO @OptimizationActions
        SELECT 
            'CREATE_ADDITIONAL_FILEGROUPS' as ActionType,
            1 as Priority,
            'Create separate filegroups for indexes and data for improved I/O distribution' as Description,
            'ALTER DATABASE [' + @DatabaseName + '] ADD FILEGROUP [INDEXES]; ' +
            'ALTER DATABASE [' + @DatabaseName + '] ADD FILE (NAME = ''' + @DatabaseName + '_Indexes'', ' +
            'FILENAME = ''[DATA_PATH]\' + @DatabaseName + '_Indexes.ndf'', ' +
            'SIZE = [INITIAL_FILEGROUP_SIZE], FILEGROWTH = [FILEGROUP_GROWTH]) TO FILEGROUP [INDEXES];' as ExecutionSQL,
            'Improved I/O parallelism and maintenance flexibility' as EstimatedBenefit
        FROM @CurrentConfig
        GROUP BY database_name
        HAVING COUNT(DISTINCT file_type) = 1 AND database_name = @DatabaseName;
    END
    
    -- Recommend growth settings optimization
    INSERT INTO @OptimizationActions
    SELECT 
        'OPTIMIZE_GROWTH_SETTINGS' as ActionType,
        2 as Priority,
        'Change percentage-based growth to fixed size for file: ' + file_name as Description,
        'ALTER DATABASE [' + database_name + '] MODIFY FILE (NAME = ''' + file_name + ''', ' +
        'FILEGROWTH = [OPTIMAL_GROWTH_SIZE_MB]MB);' as ExecutionSQL,
        'Reduced fragmentation and more predictable growth' as EstimatedBenefit
    FROM @CurrentConfig
    WHERE is_percent_growth = 1 
        AND file_size_mb > [MIN_SIZE_FOR_FIXED_GROWTH_MB]
        AND (database_name = @DatabaseName OR @DatabaseName IS NULL);
    
    -- Execute optimization actions
    IF @ExecutionMode = 'EXECUTE'
    BEGIN
        DECLARE @SQL NVARCHAR(MAX);
        DECLARE optimization_cursor CURSOR FOR
        SELECT ExecutionSQL
        FROM @OptimizationActions
        ORDER BY Priority;
        
        OPEN optimization_cursor;
        FETCH NEXT FROM optimization_cursor INTO @SQL;
        
        WHILE @@FETCH_STATUS = 0
        BEGIN
            BEGIN TRY
                EXEC sp_executesql @SQL;
                PRINT 'Executed: ' + LEFT(@SQL, 100) + '...';
            END TRY
            BEGIN CATCH
                PRINT 'Error executing: ' + ERROR_MESSAGE();
            END CATCH
            
            FETCH NEXT FROM optimization_cursor INTO @SQL;
        END
        
        CLOSE optimization_cursor;
        DEALLOCATE optimization_cursor;
    END
    
    -- Return optimization recommendations
    SELECT 
        ActionType,
        Priority,
        Description,
        EstimatedBenefit,
        CASE WHEN @ExecutionMode = 'REPORT' THEN ExecutionSQL ELSE NULL END as ProposedSQL
    FROM @OptimizationActions
    ORDER BY Priority;
END;
```

CONCURRENCY AND LOCKING OPTIMIZATION:
Lock Analysis and Optimization:
```sql
-- Comprehensive lock analysis framework
CREATE VIEW [dbo].[vw_LockingAnalysis]
AS
WITH LockHierarchy AS (
    SELECT 
        tl.request_session_id,
        tl.request_mode,
        tl.request_type,
        tl.request_status,
        tl.resource_type,
        tl.resource_database_id,
        tl.resource_associated_entity_id,
        tl.resource_lock_partition,
        tl.resource_description,
        DB_NAME(tl.resource_database_id) as database_name,
        CASE tl.resource_type
            WHEN 'OBJECT' THEN OBJECT_NAME(tl.resource_associated_entity_id, tl.resource_database_id)
            WHEN 'PAGE' THEN OBJECT_NAME(
                (SELECT p.object_id FROM sys.partitions p 
                 WHERE p.hobt_id = tl.resource_associated_entity_id), 
                tl.resource_database_id)
            WHEN 'KEY' THEN OBJECT_NAME(
                (SELECT p.object_id FROM sys.partitions p 
                 WHERE p.hobt_id = tl.resource_associated_entity_id), 
                tl.resource_database_id)
            ELSE 'N/A'
        END as object_name,
        -- Session information
        es.login_name,
        es.host_name,
        es.program_name,
        es.status as session_status,
        er.command,
        er.blocking_session_id,
        er.wait_type,
        er.wait_time,
        er.wait_resource,
        er.cpu_time,
        er.total_elapsed_time,
        er.logical_reads,
        er.writes,
        -- Query text
        SUBSTRING(
            qt.text,
            (er.statement_start_offset / 2) + 1,
            ((CASE WHEN er.statement_end_offset = -1
                   THEN DATALENGTH(qt.text)
                   ELSE er.statement_end_offset
              END - er.statement_start_offset) / 2) + 1
        ) as current_query_text
    FROM sys.dm_tran_locks tl
    LEFT JOIN sys.dm_exec_sessions es ON tl.request_session_id = es.session_id
    LEFT JOIN sys.dm_exec_requests er ON es.session_id = er.session_id
    OUTER APPLY sys.dm_exec_sql_text(er.sql_handle) qt
    WHERE tl.request_session_id > 50  -- Exclude system sessions
),
BlockingChains AS (
    -- Identify blocking chains
    SELECT 
        session_id,
        blocking_session_id,
        0 as blocking_level,
        CAST(session_id AS NVARCHAR(MAX)) as blocking_chain
    FROM sys.dm_exec_sessions
    WHERE blocking_session_id = 0
        AND session_id IN (SELECT DISTINCT blocking_session_id FROM sys.dm_exec_sessions WHERE blocking_session_id != 0)
    
    UNION ALL
    
    SELECT 
        s.session_id,
        s.blocking_session_id,
        bc.blocking_level + 1,
        CAST(bc.blocking_chain + ' -> ' + CAST(s.session_id AS NVARCHAR(10)) AS NVARCHAR(MAX))
    FROM sys.dm_exec_sessions s
    INNER JOIN BlockingChains bc ON s.blocking_session_id = bc.session_id
    WHERE s.blocking_session_id != 0
        AND bc.blocking_level < 10  -- Prevent infinite recursion
)
SELECT 
    lh.request_session_id,
    lh.request_mode,
    lh.request_type,
    lh.request_status,
    lh.resource_type,
    lh.database_name,
    lh.object_name,
    lh.resource_description,
    lh.login_name,
    lh.host_name,
    lh.program_name,
    lh.blocking_session_id,
    bc.blocking_chain,
    bc.blocking_level,
    lh.wait_type,
    lh.wait_time,
    lh.wait_resource,
    lh.total_elapsed_time,
    lh.current_query_text,
    -- Lock contention analysis
    CASE 
        WHEN lh.request_status = 'WAIT' THEN 'BLOCKED'
        WHEN lh.request_session_id IN (SELECT DISTINCT blocking_session_id FROM sys.dm_exec_sessions WHERE blocking_session_id != 0) THEN 'BLOCKING'
        ELSE 'NORMAL'
    END as lock_status,
    -- Optimization recommendations
    CASE 
        WHEN lh.wait_time > [LONG_WAIT_THRESHOLD_MS] AND lh.resource_type IN ('PAGE', 'KEY')
        THEN 'CONSIDER_INDEX_OPTIMIZATION'
        WHEN lh.request_mode IN ('X', 'IX') AND lh.total_elapsed_time > [LONG_TRANSACTION_THRESHOLD_MS]
        THEN 'LONG_TRANSACTION_REVIEW'
        WHEN lh.resource_type = 'OBJECT' AND lh.request_mode = 'X'
        THEN 'TABLE_LEVEL_LOCK_CONCERN'
        ELSE 'MONITOR'
    END as optimization_recommendation
FROM LockHierarchy lh
LEFT JOIN BlockingChains bc ON lh.request_session_id = bc.session_id;

-- Deadlock analysis and prevention
CREATE PROCEDURE [dbo].[sp_AnalyzeDeadlocks]
    @AnalysisPeriodDays INT = 7,
    @DeadlockThreshold INT = 5
AS
BEGIN
    SET NOCOUNT ON;
    
    -- Enable deadlock monitoring if not already enabled
    IF NOT EXISTS (SELECT 1 FROM sys.traces WHERE id = 1)
    BEGIN
        -- Create extended event session for deadlock monitoring
        IF NOT EXISTS (SELECT 1 FROM sys.dm_xe_sessions WHERE name = 'DeadlockMonitoring')
        BEGIN
            CREATE EVENT SESSION [DeadlockMonitoring] ON SERVER
            ADD EVENT sqlserver.xml_deadlock_report
            ADD TARGET package0.event_file(
                SET filename = N'[LOG_PATH]\DeadlockMonitoring',
                max_file_size = 10,
                max_rollover_files = 5
            )
            WITH (
                MAX_MEMORY = 4096 KB,
                EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
                MAX_DISPATCH_LATENCY = 30 SECONDS,
                MAX_EVENT_SIZE = 0 KB,
                MEMORY_PARTITION_MODE = NONE,
                TRACK_CAUSALITY = OFF,
                STARTUP_STATE = ON
            );
            
            ALTER EVENT SESSION [DeadlockMonitoring] ON SERVER STATE = START;
        END
    END
    
    -- Analyze deadlock patterns from system health
    WITH DeadlockEvents AS (
        SELECT 
            CAST(event_data AS XML) as event_xml,
            DATEADD(hour, DATEDIFF(hour, GETUTCDATE(), GETDATE()), 
                    CAST(event_data.value('(event/@timestamp)[1]', 'DATETIME2')) as event_time
        FROM sys.fn_xe_file_target_read_file(
            '[LOG_PATH]\system_health*.xel', 
            NULL, NULL, NULL
        )
        WHERE object_name = 'xml_deadlock_report'
            AND CAST(event_data.value('(event/@timestamp)[1]', 'DATETIME2') as DATETIME) >= DATEADD(day, -@AnalysisPeriodDays, GETDATE())
    ),
    DeadlockAnalysis AS (
        SELECT 
            event_time,
            -- Extract deadlock victim information
            event_xml.value('(/event/data/value/deadlock/victim-list/victimProcess/@id)[1]', 'NVARCHAR(50)') as victim_session_id,
            event_xml.value('(/event/data/value/deadlock/victim-list/victimProcess/@hostname)[1]', 'NVARCHAR(128)') as victim_hostname,
            event_xml.value('(/event/data/value/deadlock/victim-list/victimProcess/@loginname)[1]', 'NVARCHAR(128)') as victim_login,
            event_xml.value('(/event/data/value/deadlock/victim-list/victimProcess/@clientapp)[1]', 'NVARCHAR(256)') as victim_application,
            -- Extract deadlock process information
            event_xml.query('/event/data/value/deadlock/process-list') as process_list_xml,
            event_xml.query('/event/data/value/deadlock/resource-list') as resource_list_xml,
            -- Extract involved objects
            event_xml.value('(/event/data/value/deadlock/resource-list/objectlock/@objectname)[1]', 'NVARCHAR(256)') as deadlock_object
        FROM DeadlockEvents
    ),
    DeadlockSummary AS (
        SELECT 
            COUNT(*) as deadlock_count,
            COUNT(DISTINCT victim_login) as affected_logins,
            COUNT(DISTINCT victim_hostname) as affected_hosts,
            COUNT(DISTINCT victim_application) as affected_applications,
            COUNT(DISTINCT deadlock_object) as affected_objects,
            MIN(event_time) as first_deadlock,
            MAX(event_time) as last_deadlock
        FROM DeadlockAnalysis
    )
    SELECT 
        'DEADLOCK_SUMMARY' as analysis_type,
        deadlock_count,
        affected_logins,
        affected_hosts,
        affected_applications,
        affected_objects,
        first_deadlock,
        last_deadlock,
        CASE 
            WHEN deadlock_count > @DeadlockThreshold 
            THEN 'HIGH_DEADLOCK_ACTIVITY'
            ELSE 'NORMAL'
        END as severity_level,
        CASE 
            WHEN deadlock_count > @DeadlockThreshold 
            THEN 'Review deadlock patterns and implement prevention strategies'
            ELSE 'Continue monitoring'
        END as recommendation
    FROM DeadlockSummary
    
    UNION ALL
    
    -- Detailed deadlock breakdown
    SELECT 
        'DEADLOCK_DETAIL' as analysis_type,
        NULL as deadlock_count,
        NULL as affected_logins,
        NULL as affected_hosts,
        NULL as affected_applications,
        NULL as affected_objects,
        event_time as first_deadlock,
        NULL as last_deadlock,
        victim_login + ' on ' + victim_hostname as severity_level,
        'Object: ' + ISNULL(deadlock_object, 'Multiple') as recommendation
    FROM DeadlockAnalysis
    ORDER BY event_time DESC;
    
END;
```

Transaction Isolation Optimization:
```sql
-- Transaction isolation level analysis
CREATE FUNCTION [dbo].[fn_AnalyzeTransactionIsolation]()
RETURNS TABLE
AS
RETURN
WITH IsolationLevelStats AS (
    SELECT 
        es.session_id,
        es.login_name,
        es.program_name,
        es.host_name,
        er.database_id,
        DB_NAME(er.database_id) as database_name,
        CASE es.transaction_isolation_level
            WHEN 0 THEN 'Unspecified'
            WHEN 1 THEN 'ReadUncommitted'
            WHEN 2 THEN 'ReadCommitted'
            WHEN 3 THEN 'Repeatable'
            WHEN 4 THEN 'Serializable'
            WHEN 5 THEN 'Snapshot'
        END as isolation_level,
        er.open_transaction_count,
        er.cpu_time,
        er.total_elapsed_time,
        er.logical_reads,
        er.writes,
        er.wait_type,
        er.wait_time,
        er.blocking_session_id,
        -- Query text
        SUBSTRING(
            qt.text,
            (er.statement_start_offset / 2) + 1,
            ((CASE WHEN er.statement_end_offset = -1
                   THEN DATALENGTH(qt.text)
                   ELSE er.statement_end_offset
              END - er.statement_start_offset) / 2) + 1
        ) as query_text
    FROM sys.dm_exec_sessions es
    LEFT JOIN sys.dm_exec_requests er ON es.session_id = er.session_id
    OUTER APPLY sys.dm_exec_sql_text(er.sql_handle) qt
    WHERE es.session_id > 50  -- Exclude system sessions
        AND es.is_user_process = 1
),
ConcurrencyProblems AS (
    SELECT 
        session_id,
        isolation_level,
        database_name,
        wait_type,
        wait_time,
        blocking_session_id,
        query_text,
        -- Problem identification
        CASE 
            WHEN wait_type LIKE '%LOCK%' AND isolation_level = 'Serializable'
            THEN 'EXCESSIVE_LOCKING_SERIALIZABLE'
            WHEN wait_type LIKE '%LOCK%' AND isolation_level = 'Repeatable'
            THEN 'EXCESSIVE_LOCKING_REPEATABLE'
            WHEN blocking_session_id IS NOT NULL
            THEN 'BLOCKING_DETECTED'
            WHEN wait_type IN ('PAGEIOLATCH_SH', 'PAGEIOLATCH_EX') AND isolation_level != 'ReadUncommitted'
            THEN 'IO_CONTENTION'
            ELSE 'NORMAL'
        END as concurrency_issue,
        -- Optimization recommendations
        CASE 
            WHEN wait_type LIKE '%LOCK%' AND isolation_level IN ('Serializable', 'Repeatable')
            THEN 'Consider READ COMMITTED SNAPSHOT or lower isolation level'
            WHEN blocking_session_id IS NOT NULL AND isolation_level != 'ReadUncommitted'
            THEN 'Consider NOLOCK hints for read operations or READ UNCOMMITTED'
            WHEN wait_type IN ('PAGEIOLATCH_SH', 'PAGEIOLATCH_EX')
            THEN 'Consider query optimization or caching strategies'
            ELSE 'No immediate action required'
        END as recommendation
    FROM IsolationLevelStats
    WHERE wait_time > [CONCURRENCY_WAIT_THRESHOLD_MS] OR blocking_session_id IS NOT NULL
)
SELECT 
    session_id,
    isolation_level,
    database_name,
    concurrency_issue,
    wait_type,
    wait_time,
    blocking_session_id,
    recommendation,
    query_text
FROM ConcurrencyProblems;

-- Automated concurrency optimization
CREATE PROCEDURE [dbo].[sp_OptimizeConcurrency]
    @DatabaseName NVARCHAR(128),
    @OptimizationLevel NVARCHAR(20) = 'CONSERVATIVE', -- CONSERVATIVE/AGGRESSIVE
    @ExecutionMode NVARCHAR(20) = 'REPORT' -- REPORT/EXECUTE
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @OptimizationActions TABLE (
        ActionType NVARCHAR(50),
        Priority INT,
        Description NVARCHAR(500),
        ExecutionSQL NVARCHAR(MAX),
        Risk NVARCHAR(20),
        ExpectedBenefit NVARCHAR(100)
    );
    
    -- Check for Read Committed Snapshot eligibility
    IF NOT EXISTS (
        SELECT 1 FROM sys.databases 
        WHERE name = @DatabaseName 
            AND is_read_committed_snapshot_on = 1
    )
    BEGIN
        INSERT INTO @OptimizationActions
        VALUES (
            'ENABLE_READ_COMMITTED_SNAPSHOT',
            1,
            'Enable Read Committed Snapshot isolation to reduce lock contention',
            'ALTER DATABASE [' + @DatabaseName + '] SET READ_COMMITTED_SNAPSHOT ON WITH ROLLBACK IMMEDIATE;',
            'MEDIUM',
            'Significant reduction in reader-writer blocking'
        );
    END
    
    -- Check for snapshot isolation eligibility
    IF NOT EXISTS (
        SELECT 1 FROM sys.databases 
        WHERE name = @DatabaseName 
            AND snapshot_isolation_state = 1
    )
    AND @OptimizationLevel = 'AGGRESSIVE'
    BEGIN
        INSERT INTO @OptimizationActions
        VALUES (
            'ENABLE_SNAPSHOT_ISOLATION',
            2,
            'Enable Snapshot isolation for applications that can handle versioning overhead',
            'ALTER DATABASE [' + @DatabaseName + '] SET ALLOW_SNAPSHOT_ISOLATION ON;',
            'HIGH',
            'Complete elimination of reader-writer blocking with versioning overhead'
        );
    END
    
    -- Recommend query-level optimizations
    INSERT INTO @OptimizationActions
    SELECT 
        'QUERY_HINT_OPTIMIZATION' as ActionType,
        3 as Priority,
        'Add NOLOCK hints to read-only queries experiencing lock waits' as Description,
        '-- Add WITH (NOLOCK) hints to SELECT statements in: ' + ISNULL(program_name, 'Unknown Application') as ExecutionSQL,
        'LOW' as Risk,
        'Reduced lock waits for read operations' as ExpectedBenefit
    FROM [dbo].[fn_AnalyzeTransactionIsolation]()
    WHERE concurrency_issue LIKE '%LOCKING%'
        AND database_name = @DatabaseName
    GROUP BY program_name;
    
    -- Execute optimizations
    IF @ExecutionMode = 'EXECUTE'
    BEGIN
        DECLARE @SQL NVARCHAR(MAX);
        DECLARE optimization_cursor CURSOR FOR
        SELECT ExecutionSQL
        FROM @OptimizationActions
        WHERE ActionType != 'QUERY_HINT_OPTIMIZATION'  -- Skip manual query changes
        ORDER BY Priority;
        
        OPEN optimization_cursor;
        FETCH NEXT FROM optimization_cursor INTO @SQL;
        
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
            
            FETCH NEXT FROM optimization_cursor INTO @SQL;
        END
        
        CLOSE optimization_cursor;
        DEALLOCATE optimization_cursor;
    END
    
    -- Return optimization recommendations
    SELECT 
        ActionType,
        Priority,
        Description,
        Risk,
        ExpectedBenefit,
        CASE WHEN @ExecutionMode = 'REPORT' THEN ExecutionSQL ELSE NULL END as ProposedSQL
    FROM @OptimizationActions
    ORDER BY Priority;
    
END;
```

OUTPUT: Deliver comprehensive query optimization and performance tuning solution including:
1. Complete performance baseline analysis and metrics collection
2. Advanced indexing strategies and maintenance procedures
3. Query rewriting and optimization techniques
4. Execution plan analysis and optimization
5. Memory and buffer pool optimization strategies
6. Storage I/O optimization and configuration
7. Concurrency and locking optimization
8. Automated performance monitoring and alerting systems
9. Self-tuning maintenance procedures
10. Performance troubleshooting and resolution frameworks
```

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

## Customization Options

1. **Database Platforms**
   - SQL Server (2017, 2019, 2022)
   - PostgreSQL (12, 13, 14, 15)
   - Oracle Database (19c, 21c)
   - MySQL (8.0+)
   - Cloud platforms (Snowflake, Redshift, BigQuery)
   - NoSQL databases (MongoDB, Cassandra)

2. **Workload Types**
   - OLTP (Online Transaction Processing)
   - OLAP (Online Analytical Processing)
   - Hybrid transactional/analytical
   - Data warehouse workloads
   - Real-time analytics
   - Batch processing systems

3. **Optimization Focus Areas**
   - Query execution optimization
   - Index strategy optimization
   - Memory and buffer management
   - I/O and storage optimization
   - Concurrency and locking
   - Statistics and cardinality estimation

4. **Performance Objectives**
   - Response time optimization
   - Throughput maximization
   - Resource utilization optimization
   - Cost optimization (cloud environments)
   - Scalability improvements
   - Availability and reliability

5. **Industry Specializations**
   - Financial services (high-frequency trading systems)
   - Healthcare (large-scale analytical workloads)
   - E-commerce (high-concurrency OLTP)
   - Manufacturing (IoT data processing)
   - Government (compliance and security focus)
   - SaaS platforms (multi-tenant optimization)