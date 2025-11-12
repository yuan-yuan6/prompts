---
category: data-analytics/Analytics-Engineering
last_updated: 2025-11-10
related_templates:
- data-analytics/Analytics-Engineering/query-optimization-baseline-analysis.md
- data-analytics/Analytics-Engineering/query-optimization-indexing-strategies.md
- data-analytics/Analytics-Engineering/query-optimization-overview.md
tags:
- data-analytics
- automation
title: Query Optimization - Performance Monitoring & Tuning
use_cases:
- Implementing real-time performance monitoring and alerting systems
- Creating automated performance tuning procedures
- Establishing continuous performance optimization workflows
industries:
- manufacturing
- technology
---

# Query Optimization - Performance Monitoring & Tuning

## Purpose
Implement comprehensive real-time performance monitoring, automated alerting systems, and self-tuning procedures to continuously optimize database query performance and proactively address performance issues.

## Quick Start

### For Performance Monitoring Setup
Set up monitoring and automated tuning in 3 steps:

1. **Deploy Real-Time Monitoring**
   - Create the performance metrics view (lines 813-940) to track active queries
   - Set up monitoring dashboard to display: long-running queries, blocked sessions, high CPU/IO
   - Configure refresh interval (30-60 seconds) for near real-time visibility
   - Document performance thresholds: >5min = long-running, >80% CPU = high CPU

2. **Configure Performance Alerts**
   - Implement alert monitoring procedure (lines 943-1031) with JSON threshold configuration
   - Set alert thresholds: long_running (>10min), high_cpu (>75%), blocked (>5min)
   - Configure notification methods: email, SMS, Slack, PagerDuty
   - Test alerts with simulated performance issues

3. **Enable Automated Tuning**
   - Deploy auto-tuning procedure (lines 1037-1210) with REPORT mode first
   - Review recommended actions: missing indexes, outdated statistics, fragmented indexes
   - Schedule automated execution: daily statistics updates, weekly index maintenance
   - Set execution limits: max 60 minutes, high/medium impact only

**Key Outputs**: Monitoring dashboard, alert configuration, automated tuning schedule

**Key Variables**: `LONG_RUNNING_THRESHOLD_MS`, `HIGH_CPU_ALERT_PERCENTAGE`, `MAINTENANCE_MAXDOP`

## Template

```
You are a database performance monitoring and automation expert for [DATABASE_PLATFORM]. Design a comprehensive monitoring and automated tuning system for [ORGANIZATION_NAME] to maintain [PERFORMANCE_SLA_TARGETS] using [MONITORING_APPROACH] methodology.

PERFORMANCE MONITORING CONTEXT:
Project Context:
- Organization: [ORGANIZATION_NAME]
- Database platform: [DATABASE_PLATFORM]
- Workload type: [WORKLOAD_TYPE]
- Performance SLA: [PERFORMANCE_SLA_TARGETS]
- Monitoring scope: [MONITORING_SCOPE]
- Alert requirements: [ALERT_REQUIREMENTS]

### System Configuration
- Database version: [DATABASE_VERSION]
- Monitoring tools: [MONITORING_TOOLS]
- Alert channels: [ALERT_CHANNELS]
- Maintenance windows: [MAINTENANCE_WINDOWS]

### PERFORMANCE MONITORING AND TUNING

### Real-time Performance Monitoring
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
        -- Session information
        s.host_name,
        s.program_name,
        s.host_process_id,
        s.client_version,
        s.client_interface_name,
        s.login_name,
        s.nt_domain,
        s.nt_user_name,
        s.login_time,
        s.is_user_process
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

### Automated Performance Tuning
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

OUTPUT: Deliver comprehensive monitoring and tuning system including:
1. Real-time performance metrics view with active query tracking
2. Automated alert system with configurable thresholds
3. Performance categorization (long-running, high CPU, high I/O, blocked)
4. Self-tuning procedures for indexes and statistics
5. Execution status tracking and error handling
6. Notification integration for critical alerts
7. Automated maintenance scheduling framework
8. Performance trend analysis capabilities
```

## Variables
[DATABASE_PLATFORM], [ORGANIZATION_NAME], [WORKLOAD_TYPE], [MONITORING_APPROACH], [PERFORMANCE_SLA_TARGETS], [MONITORING_SCOPE], [ALERT_REQUIREMENTS], [DATABASE_VERSION], [MONITORING_TOOLS], [ALERT_CHANNELS], [MAINTENANCE_WINDOWS], [LONG_RUNNING_THRESHOLD_MS], [HIGH_CPU_THRESHOLD_MS], [HIGH_IO_THRESHOLD], [LONG_RUNNING_ALERT_MINUTES], [HIGH_CPU_ALERT_PERCENTAGE], [BLOCKED_QUERY_ALERT_MINUTES], [HIGH_IO_ALERT_THRESHOLD], [DEADLOCK_ALERT_COUNT], [WAIT_TIME_ALERT_MINUTES], [DEFAULT_TUNING_MINUTES], [MIN_INDEX_IMPACT_THRESHOLD], [MIN_INDEX_USAGE_THRESHOLD], [STATS_UPDATE_THRESHOLD_DAYS], [REORGANIZE_FRAGMENTATION_THRESHOLD], [MIN_PAGES_FOR_MAINTENANCE]

## Usage Examples

### Example 1: OLTP Real-Time Monitoring
```
DATABASE_PLATFORM: "SQL Server 2022"
ORGANIZATION_NAME: "E-commerce Platform"
WORKLOAD_TYPE: "OLTP"
LONG_RUNNING_THRESHOLD_MS: "5000"
HIGH_CPU_ALERT_PERCENTAGE: "75"
BLOCKED_QUERY_ALERT_MINUTES: "2"
ALERT_CHANNELS: "Email, Slack, PagerDuty"
MONITORING_APPROACH: "Real-time with immediate alerting"
```

### Example 2: OLAP Automated Tuning
```
DATABASE_PLATFORM: "PostgreSQL 15"
ORGANIZATION_NAME: "Analytics Data Warehouse"
WORKLOAD_TYPE: "OLAP"
DEFAULT_TUNING_MINUTES: "120"
MIN_INDEX_IMPACT_THRESHOLD: "70"
STATS_UPDATE_THRESHOLD_DAYS: "7"
REORGANIZE_FRAGMENTATION_THRESHOLD: "20"
MONITORING_SCOPE: "Query performance and resource utilization"
```

### Example 3: Hybrid Comprehensive Monitoring
```
DATABASE_PLATFORM: "Azure SQL Database"
ORGANIZATION_NAME: "SaaS Application"
WORKLOAD_TYPE: "Hybrid"
LONG_RUNNING_ALERT_MINUTES: "10"
HIGH_IO_ALERT_THRESHOLD: "50000000"
MIN_INDEX_USAGE_THRESHOLD: "1000"
ALERT_REQUIREMENTS: "Multi-channel with escalation"
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Query Optimization Baseline Analysis](query-optimization-baseline-analysis.md)** - Complementary approaches and methodologies
- **[Query Optimization Indexing Strategies](query-optimization-indexing-strategies.md)** - Complementary approaches and methodologies
- **[Query Optimization Overview](query-optimization-overview.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Query Optimization - Performance Monitoring & Tuning)
2. Use [Query Optimization Baseline Analysis](query-optimization-baseline-analysis.md) for deeper analysis
3. Apply [Query Optimization Indexing Strategies](query-optimization-indexing-strategies.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Analytics Engineering](../../data-analytics/Analytics Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Implementing real-time performance monitoring and alerting systems**: Combine this template with related analytics and strategy frameworks
- **Creating automated performance tuning procedures**: Combine this template with related analytics and strategy frameworks
- **Establishing continuous performance optimization workflows**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Set realistic alert thresholds** - Avoid alert fatigue with appropriate limits
2. **Test alerts in non-production** - Validate notification delivery before production
3. **Review tuning actions first** - Run in REPORT mode before EXECUTE mode
4. **Schedule automated tuning carefully** - Execute during low-activity periods
5. **Monitor the monitors** - Ensure monitoring system itself is reliable
6. **Document alert responses** - Create runbooks for common performance issues
7. **Archive historical metrics** - Keep performance data for trend analysis
8. **Integrate with incident management** - Connect alerts to ticketing systems
9. **Review false positives regularly** - Adjust thresholds based on experience
10. **Automate routine tasks only** - Keep critical decisions manual with approval

## Tips for Success

- Start with conservative thresholds and adjust based on baseline analysis
- Create separate alert channels for different severity levels
- Implement alert suppression during maintenance windows
- Use JSON configuration for flexible threshold management
- Monitor long-running queries relative to their typical execution time
- Set up automated statistics updates daily, index maintenance weekly
- Track tuning action success rates and adjust strategies accordingly
- Create dashboards showing alerts over time to identify patterns
- Include query text in alerts for faster troubleshooting
- Set maximum execution time limits to prevent runaway tuning operations
- Archive and analyze historical alerts to improve threshold tuning
- Integrate monitoring with application performance management (APM) tools
