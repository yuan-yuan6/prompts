---
title: Query Optimization - Indexing Strategies
category: data-analytics/Analytics Engineering
tags: [data-analytics, indexing, performance, database-design, optimization]
use_cases:
  - Designing comprehensive indexing strategies for optimal query performance
  - Analyzing index effectiveness and identifying optimization opportunities
  - Implementing automated index maintenance procedures
related_templates:
  - data-analytics/Analytics Engineering/query-optimization-baseline-analysis.md
  - data-analytics/Analytics Engineering/query-optimization-query-rewriting.md
  - data-analytics/Analytics Engineering/query-optimization-overview.md
last_updated: 2025-11-10
---

# Query Optimization - Indexing Strategies

## Purpose
Design and implement comprehensive indexing strategies including effectiveness analysis, advanced index types (B-tree, columnstore, filtered), and automated maintenance procedures to optimize query performance and minimize storage overhead.

## Quick Start

### For Index Optimization
Optimize your indexing strategy in 3 steps:

1. **Analyze Current Indexes**
   - Run index effectiveness analysis (lines 311-421) to identify unused, duplicate, or inefficient indexes
   - Review read/write ratios to determine index value vs. maintenance cost
   - Flag indexes for removal if: total_reads = 0, user_updates > 10x reads, or duplicates exist

2. **Identify Missing Indexes**
   - Execute missing index queries (lines 230-248 from baseline) with priority scoring
   - Focus on indexes with avg_user_impact > 80% and user_seeks > 1000
   - Create implementation plan ordered by index_priority_score

3. **Implement and Maintain** (Ongoing)
   - Create indexes using advanced design patterns (lines 425-474) with proper INCLUDE columns
   - Set up automated maintenance procedures (lines 478-587) for reorganize/rebuild
   - Schedule weekly fragmentation checks and monthly index usage reviews

**Key Outputs**: Index effectiveness report, missing index recommendations, maintenance schedule

**Key Variables**: `DATABASE_PLATFORM`, `FRAGMENTATION_THRESHOLD`, `REBUILD_THRESHOLD`, `MAINTENANCE_MAXDOP`

## Template

```
You are a database indexing optimization expert specializing in [DATABASE_PLATFORM]. Design a comprehensive indexing strategy for [ORGANIZATION_NAME] to optimize [WORKLOAD_TYPE] workload performance using [INDEXING_METHODOLOGY] approach.

INDEXING STRATEGY CONTEXT:
Project Context:
- Organization: [ORGANIZATION_NAME]
- Database platform: [DATABASE_PLATFORM]
- Workload type: [WORKLOAD_TYPE] (OLTP/OLAP/Hybrid)
- Data volume: [CURRENT_DATA_VOLUME]
- Query patterns: [QUERY_PATTERNS]
- Performance requirements: [PERFORMANCE_REQUIREMENTS]

### System Configuration
- Database version: [DATABASE_VERSION]
- Storage system: [STORAGE_SYSTEM]
- Memory allocation: [MEMORY_ALLOCATION]
- Maintenance windows: [MAINTENANCE_WINDOWS]

### INDEXING STRATEGY OPTIMIZATION

### Comprehensive Index Analysis
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

### Advanced Index Design
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

### Index Maintenance Strategy
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

OUTPUT: Deliver comprehensive indexing strategy including:
1. Index effectiveness analysis with usage statistics and performance metrics
2. Recommendations for unused, duplicate, or inefficient indexes
3. Missing index recommendations with priority scoring
4. Advanced index designs (composite, filtered, columnstore, partitioned)
5. Automated maintenance procedures for fragmentation management
6. Index consolidation opportunities to reduce overhead
7. Performance impact assessment for proposed changes
8. Implementation roadmap with phased approach
```

## Variables
[DATABASE_PLATFORM], [ORGANIZATION_NAME], [WORKLOAD_TYPE], [INDEXING_METHODOLOGY], [CURRENT_DATA_VOLUME], [QUERY_PATTERNS], [PERFORMANCE_REQUIREMENTS], [DATABASE_VERSION], [STORAGE_SYSTEM], [MEMORY_ALLOCATION], [MAINTENANCE_WINDOWS], [OBJECT_ID], [INDEX_ID], [INDEX_NAME], [USER_SEEKS], [USER_SCANS], [USER_LOOKUPS], [USER_UPDATES], [PAGE_COUNT], [AVG_FRAGMENTATION_IN_PERCENT], [UNUSED_UPDATE_THRESHOLD], [SCAN_THRESHOLD], [FRAGMENTATION_THRESHOLD], [HIGH_USAGE_THRESHOLD], [SCAN_SEEK_RATIO_THRESHOLD], [MIN_RECOMMENDED_INDEXES], [HIGH_SEEK_THRESHOLD], [MAX_RECOMMENDED_INDEXES], [TABLE_NAME], [COMPOSITE_DESCRIPTION], [SCHEMA], [KEY_COLUMN_1], [KEY_COLUMN_2], [KEY_COLUMN_3], [INCLUDED_COLUMN_1], [INCLUDED_COLUMN_2], [INCLUDED_COLUMN_3], [FILL_FACTOR_PERCENTAGE], [PAD_INDEX_SETTING], [IGNORE_DUPLICATE_SETTING], [ROW_LOCK_SETTING], [PAGE_LOCK_SETTING], [MAX_DEGREE_PARALLELISM], [ONLINE_INDEX_CREATION], [FILTERED_DESCRIPTION], [FILTER_COLUMN_1], [FILTER_COLUMN_2], [INCLUDED_COLUMNS], [FILTER_CONDITION], [FILTERED_FILL_FACTOR], [ANALYTICS_DESCRIPTION], [COLUMNSTORE_MAXDOP], [COMPRESSION_DELAY_MINUTES], [COLUMNSTORE_COMPRESSION], [PARTITIONED_DESCRIPTION], [PARTITION_KEY], [INDEX_KEY_COLUMNS], [PARTITION_SCHEME], [DEFAULT_FRAGMENTATION_THRESHOLD], [REBUILD_THRESHOLD], [REORGANIZE_THRESHOLD], [STATS_UPDATE_THRESHOLD], [MAINTENANCE_MAXDOP], [MIN_PAGES_FOR_REBUILD], [MIN_PAGES_FOR_REORGANIZE]

## Usage Examples

### Example 1: OLTP Indexing Strategy
```
DATABASE_PLATFORM: "SQL Server 2022"
ORGANIZATION_NAME: "E-commerce Platform"
WORKLOAD_TYPE: "OLTP"
FRAGMENTATION_THRESHOLD: "10"
REBUILD_THRESHOLD: "30"
REORGANIZE_THRESHOLD: "10"
FILL_FACTOR_PERCENTAGE: "90"
MAINTENANCE_MAXDOP: "4"
ONLINE_INDEX_CREATION: "ON"
```

### Example 2: OLAP Columnstore Strategy
```
DATABASE_PLATFORM: "SQL Server 2022"
ORGANIZATION_NAME: "Analytics Data Warehouse"
WORKLOAD_TYPE: "OLAP"
COLUMNSTORE_MAXDOP: "8"
COMPRESSION_DELAY_MINUTES: "30"
COLUMNSTORE_COMPRESSION: "COLUMNSTORE_ARCHIVE"
MIN_RECOMMENDED_INDEXES: "2"
MAX_RECOMMENDED_INDEXES: "8"
```

### Example 3: Hybrid Workload Indexing
```
DATABASE_PLATFORM: "PostgreSQL 15"
ORGANIZATION_NAME: "SaaS Application"
WORKLOAD_TYPE: "Hybrid"
UNUSED_UPDATE_THRESHOLD: "1000"
SCAN_THRESHOLD: "10000"
HIGH_USAGE_THRESHOLD: "100000"
SCAN_SEEK_RATIO_THRESHOLD: "3"
```

## Best Practices

1. **Column order matters** - Place most selective columns first in composite indexes
2. **Use INCLUDE wisely** - Add frequently queried columns to avoid key lookups
3. **Monitor read/write ratios** - Remove indexes with low reads and high writes
4. **Leverage filtered indexes** - Use WHERE clauses for selective queries on large tables
5. **Consider columnstore for OLAP** - Implement for large fact tables with analytical queries
6. **Set appropriate fill factors** - Use 90-95% for mostly-read tables, 70-80% for heavy writes
7. **Maintain indexes regularly** - Schedule weekly reorganize and monthly rebuild operations
8. **Avoid over-indexing** - More indexes slow down writes and increase storage
9. **Align partitioned indexes** - Match index partitioning with table partitioning scheme
10. **Test before production** - Validate index changes in staging environment first

## Tips for Success

- Start with missing index DMVs but validate recommendations with actual query plans
- Create covering indexes for your most frequent and expensive queries
- Use online index operations (ONLINE = ON) to minimize production impact
- Monitor index fragmentation weekly and rebuild indexes >30% fragmented
- Remove duplicate indexes (same key columns in same order)
- Set up alerts for low index usage (reads < 100 over 30 days)
- Document index purpose and creation rationale in extended properties
- Review index strategy quarterly as workload evolves
- Use filtered indexes for common query predicates (e.g., Status = 'Active')
- Consider compression for large indexes to save storage (PAGE or ROW compression)
