---
title: Query Optimization - Resource & Concurrency Management
category: data-analytics/Analytics Engineering
tags: [data-analytics, memory-optimization, storage, concurrency, locking, resource-management]
use_cases:
  - Optimizing memory allocation and buffer pool management
  - Implementing storage I/O optimization strategies
  - Resolving concurrency issues and minimizing locking contention
  - Managing deadlocks and transaction isolation levels
related_templates:
  - query-optimization-baseline-analysis.md
  - query-optimization-indexing-strategies.md
  - query-optimization-overview.md
last_updated: 2025-11-10
---

# Query Optimization - Resource & Concurrency Management

## Purpose
Optimize database resource utilization including memory/buffer pool management, storage I/O configuration, and concurrency control through lock analysis, deadlock prevention, and transaction isolation optimization to maximize performance and minimize contention.

## Quick Start

### For Resource Optimization
Optimize resources and concurrency in 3 steps:

1. **Analyze Resource Utilization** (30-45 minutes)
   - Run buffer pool analysis (lines 1218-1291) to identify hot/cold data patterns
   - Review memory pressure indicators and wait statistics (lines 1294-1321)
   - Execute storage I/O analysis (lines 1327-1391) to identify latency issues
   - Flag issues: buffer hit ratio < 80%, read latency > 20ms, high memory waits

2. **Optimize Concurrency** (45-60 minutes)
   - Deploy lock analysis view (lines 1520-1635) to identify blocking chains
   - Run deadlock analysis procedure (lines 1638-1749) to review deadlock patterns
   - Analyze transaction isolation levels (lines 1755-1842) for concurrency problems
   - Document blocking: session IDs, wait times, resources, query patterns

3. **Implement Improvements** (Ongoing)
   - Enable Read Committed Snapshot isolation (lines 1869-1877) to reduce blocking
   - Optimize storage growth settings (lines 1462-1473) to use fixed increments
   - Configure automated concurrency optimization (lines 1845-1955) in REPORT mode first
   - Schedule monthly resource reviews and quarterly configuration tuning

**Key Outputs**: Resource utilization report, blocking analysis, concurrency recommendations

**Key Variables**: `MEMORY_ALLOCATION`, `STORAGE_SYSTEM`, `CONCURRENCY_OPTIMIZATION_LEVEL`

## Template

```
You are a database resource and concurrency optimization expert for [DATABASE_PLATFORM]. Optimize resource utilization and concurrency control for [ORGANIZATION_NAME] to support [WORKLOAD_TYPE] workload with [PERFORMANCE_REQUIREMENTS] using [OPTIMIZATION_APPROACH] methodology.

RESOURCE OPTIMIZATION CONTEXT:
Project Context:
- Organization: [ORGANIZATION_NAME]
- Database platform: [DATABASE_PLATFORM]
- Workload type: [WORKLOAD_TYPE]
- Concurrency requirements: [CONCURRENT_USER_CAPACITY]
- Resource constraints: [RESOURCE_CONSTRAINTS]
- Performance targets: [PERFORMANCE_TARGETS]

### System Configuration
- Database version: [DATABASE_VERSION]
- Memory allocation: [MEMORY_ALLOCATION]
- Storage system: [STORAGE_SYSTEM]
- CPU configuration: [CPU_CONFIGURATION]
- Cloud provider: [CLOUD_PROVIDER] (if applicable)

### MEMORY AND STORAGE OPTIMIZATION

### Buffer Pool and Memory Management
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

### Storage Optimization
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

### CONCURRENCY AND LOCKING OPTIMIZATION

### Lock Analysis and Optimization
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

### Transaction Isolation Optimization
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

OUTPUT: Deliver comprehensive resource and concurrency optimization including:
1. Buffer pool analysis with hot/warm/cold data classification
2. Memory pressure indicators and recommendations
3. Storage I/O performance metrics and latency analysis
4. Lock contention analysis with blocking chain identification
5. Deadlock pattern analysis and prevention strategies
6. Transaction isolation level optimization recommendations
7. Automated concurrency improvements (Read Committed Snapshot)
8. Storage configuration optimization (filegroups, growth settings)
9. Performance improvement estimates and risk assessment
10. Implementation roadmap with prioritized actions
```

## Variables
[DATABASE_PLATFORM], [ORGANIZATION_NAME], [WORKLOAD_TYPE], [OPTIMIZATION_APPROACH], [CONCURRENT_USER_CAPACITY], [RESOURCE_CONSTRAINTS], [PERFORMANCE_TARGETS], [DATABASE_VERSION], [MEMORY_ALLOCATION], [STORAGE_SYSTEM], [CPU_CONFIGURATION], [CLOUD_PROVIDER], [LARGE_BUFFER_THRESHOLD], [HIGH_READ_LATENCY_THRESHOLD], [LARGE_TABLE_THRESHOLD], [MEMORY_THRESHOLD_KB], [HIGH_WRITE_LATENCY_THRESHOLD], [HIGH_TOTAL_STALL_THRESHOLD], [LARGE_FILE_THRESHOLD], [DATA_PATH], [INITIAL_FILEGROUP_SIZE], [FILEGROUP_GROWTH], [OPTIMAL_GROWTH_SIZE_MB], [MIN_SIZE_FOR_FIXED_GROWTH_MB], [LOG_PATH], [LONG_WAIT_THRESHOLD_MS], [LONG_TRANSACTION_THRESHOLD_MS], [CONCURRENCY_WAIT_THRESHOLD_MS]

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
MEMORY_ALLOCATION: "128GB"
LARGE_BUFFER_THRESHOLD: "5000"
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
CONCURRENCY_WAIT_THRESHOLD_MS: "1000"
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
STORAGE_SYSTEM: "Cloud object storage"
```

## Best Practices

1. **Monitor buffer pool efficiency** - Maintain >80% buffer cache hit ratio for optimal performance
2. **Use Read Committed Snapshot** - Enable to reduce reader-writer blocking in OLTP workloads
3. **Optimize file growth settings** - Use fixed-size increments instead of percentage-based growth
4. **Identify and resolve blocking chains** - Monitor blocking sessions and long-wait queries regularly
5. **Analyze deadlock patterns** - Review deadlocks weekly and implement prevention strategies
6. **Separate data and log files** - Place on different physical storage for better I/O performance
7. **Monitor memory pressure waits** - Address RESOURCE_SEMAPHORE waits through query or memory tuning
8. **Use appropriate isolation levels** - Balance consistency requirements with concurrency needs
9. **Implement query timeouts** - Set reasonable limits to prevent runaway queries
10. **Review transaction design** - Keep transactions short to minimize lock holding time

## Tips for Success

- Establish baseline buffer hit ratios before optimization (typically 90%+ is good)
- Monitor storage I/O latency: < 10ms read and < 5ms write for SSD storage
- Enable Read Committed Snapshot isolation for most OLTP applications
- Create separate filegroups for indexes on large tables (>10GB)
- Use fixed file growth of 512MB-1GB for data files, 256MB for log files
- Identify blocking root causes: missing indexes, long transactions, table scans
- Analyze deadlock graphs to understand resource contention patterns
- Consider application-level caching to reduce database memory pressure
- Implement connection pooling to manage concurrent user load efficiently
- Review and optimize long-running transactions that hold locks extensively
- Monitor dirty page counts - high values may indicate checkpoint tuning needed
- Use page compression for large tables with low update frequency
- Implement proper error handling for deadlock retries in application code
- Schedule resource-intensive operations during off-peak hours
- Document resource optimization decisions and their impact for future reference

## Customization Options

1. **Database Platforms**
   - SQL Server (2017, 2019, 2022)
   - PostgreSQL (12, 13, 14, 15)
   - Oracle Database (19c, 21c)
   - MySQL (8.0+)
   - Cloud platforms (Snowflake, Redshift, BigQuery, Azure SQL)
   - NoSQL databases (MongoDB, Cassandra)

2. **Workload Types**
   - OLTP (Online Transaction Processing)
   - OLAP (Online Analytical Processing)
   - Hybrid transactional/analytical (HTAP)
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
   - Resource governance and workload management

4. **Performance Objectives**
   - Response time optimization
   - Throughput maximization
   - Resource utilization optimization
   - Cost optimization (cloud environments)
   - Scalability improvements
   - Availability and reliability
   - Concurrent user capacity

5. **Industry Specializations**
   - Financial services (high-frequency trading, regulatory reporting)
   - Healthcare (large-scale analytical workloads, HIPAA compliance)
   - E-commerce (high-concurrency OLTP, inventory management)
   - Manufacturing (IoT data processing, supply chain analytics)
   - SaaS applications (multi-tenant architecture, resource isolation)
   - Gaming (real-time leaderboards, high write throughput)
