---
title: Query Analysis & Profiling Template
category: data-analytics/Analytics Engineering
tags: ['database', 'query-optimization', 'performance', 'profiling']
use_cases:
  - Analyze query performance using execution plans, profiling tools, and performance metrics to identify optimization opportunities.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Query Analysis & Profiling Template

## Purpose
Analyze query performance using execution plans, profiling tools, and performance metrics to identify optimization opportunities.

## Quick Start

### For Data Engineers

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific analyze needs
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
- Analyze query performance using execution plans, profiling tools, and performance metrics to identify optimization opportunities.
- Project-specific implementations
- Research and analysis workflows



## Template

### QUERY ANALYSIS AND PROFILING

### Performance Baseline Assessment

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

1. Complete performance baseline analysis and metrics collection

4. Execution plan analysis and optimization

OPTIMIZATION_METHODOLOGY: "Comprehensive analysis with columnstore optimization"


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
