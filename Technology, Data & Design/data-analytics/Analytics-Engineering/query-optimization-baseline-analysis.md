---
title: Query Optimization - Baseline Analysis & Profiling
category: data-analytics/Analytics-Engineering
tags:
- data-analytics
- analysis
use_cases:
- Establishing performance baselines and identifying bottlenecks in database query
  execution
- Analyzing query execution patterns, resource consumption, and wait statistics
- Profiling query execution plans to identify optimization opportunities
related_templates:
- data-analytics/Analytics-Engineering/query-optimization-indexing-strategies.md
- data-analytics/Analytics-Engineering/query-optimization-monitoring-tuning.md
- data-analytics/Analytics-Engineering/query-optimization-overview.md
last_updated: 2025-11-10
industries:
- finance
- technology
type: template
difficulty: intermediate
slug: query-optimization-baseline-analysis
---

# Query Optimization - Baseline Analysis & Profiling

## Purpose
Establish comprehensive performance baselines and diagnostic frameworks for SQL queries, including execution plan analysis, workload pattern identification, and resource consumption profiling to identify optimization opportunities.

## Quick Start

### For Performance Analysis
Establish your query performance baseline in 3 steps:

1. **Identify Problem Queries**
   - Run the performance baseline queries (lines 88-177) to identify top resource consumers
   - Focus on queries with >1s execution time or >10M logical reads
   - Export results to track metrics: execution time, CPU, I/O, memory usage

2. **Analyze Execution Plans**
   - Execute the execution plan analysis queries (lines 182-250) on identified problem queries
   - Look for: table scans, missing indexes, hash joins on large datasets, expensive sorts
   - Document plan characteristics and estimated costs for comparison

3. **Profile Workload Patterns**
   - Run temporal query pattern analysis (lines 254-305) to identify peak load times
   - Analyze query complexity metrics to prioritize optimization efforts
   - Create baseline report with top 10 queries by performance impact score

**Key Outputs**: Performance baseline report, execution plan analysis, workload patterns, optimization priority list

**Key Variables**: `DATABASE_PLATFORM`, `ANALYSIS_PERIOD_DAYS`, `TOP_N_QUERIES`, `QUERY_PERFORMANCE_VIEW`

## Template

```
You are a database performance diagnostics expert specializing in [DATABASE_PLATFORM]. Establish a comprehensive performance baseline for [ORGANIZATION_NAME] to identify query optimization opportunities and performance bottlenecks using [ANALYSIS_METHODOLOGY] approach.

PERFORMANCE BASELINE ASSESSMENT:
Project Context:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Database platform: [DATABASE_PLATFORM]
- Workload type: [WORKLOAD_TYPE] (OLTP/OLAP/Hybrid/Analytics)
- Analysis period: [ANALYSIS_PERIOD_DAYS] days
- Performance objectives: [PERFORMANCE_OBJECTIVES]
- Current challenges: [CURRENT_PERFORMANCE_CHALLENGES]

### System Architecture
- Database version: [DATABASE_VERSION]
- Hardware specifications: [HARDWARE_SPECIFICATIONS]
- Server configuration: [SERVER_CONFIGURATION]
- Storage system: [STORAGE_SYSTEM]
- Memory allocation: [MEMORY_ALLOCATION]
- CPU configuration: [CPU_CONFIGURATION]

### Performance Requirements
- Query response time SLA: [QUERY_RESPONSE_TIME_SLA]
- Throughput requirements: [THROUGHPUT_REQUIREMENTS]
- Concurrent user capacity: [CONCURRENT_USER_CAPACITY]
- Data volume current: [CURRENT_DATA_VOLUME]
- Peak load characteristics: [PEAK_LOAD_CHARACTERISTICS]

### QUERY ANALYSIS AND PROFILING

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
```

### Query Execution Plan Analysis
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

### Workload Pattern Analysis
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

OUTPUT: Deliver comprehensive performance baseline analysis including:
1. Query execution time metrics and resource consumption analysis
2. Wait statistics analysis identifying system bottlenecks
3. Index usage statistics for optimization opportunities
4. Execution plan analysis with problematic operators identified
5. Missing index recommendations with priority scoring
6. Temporal workload patterns for capacity planning
7. Query complexity metrics for optimization prioritization
8. Performance impact scores for focused optimization efforts
```

## Variables
[DATABASE_PLATFORM], [ORGANIZATION_NAME], [INDUSTRY_SECTOR], [WORKLOAD_TYPE], [ANALYSIS_METHODOLOGY], [ANALYSIS_PERIOD_DAYS], [PERFORMANCE_OBJECTIVES], [CURRENT_PERFORMANCE_CHALLENGES], [DATABASE_VERSION], [HARDWARE_SPECIFICATIONS], [SERVER_CONFIGURATION], [STORAGE_SYSTEM], [MEMORY_ALLOCATION], [CPU_CONFIGURATION], [QUERY_RESPONSE_TIME_SLA], [THROUGHPUT_REQUIREMENTS], [CONCURRENT_USER_CAPACITY], [CURRENT_DATA_VOLUME], [PEAK_LOAD_CHARACTERISTICS], [QUERY_ID_COLUMN], [QUERY_TEXT_COLUMN], [EXECUTION_COUNT], [TOTAL_EXECUTION_TIME_MS], [AVERAGE_EXECUTION_TIME_MS], [MAX_EXECUTION_TIME_MS], [MIN_EXECUTION_TIME_MS], [TOTAL_CPU_TIME_MS], [TOTAL_LOGICAL_READS], [TOTAL_PHYSICAL_READS], [TOTAL_LOGICAL_WRITES], [COMPILATION_TIME_MS], [LAST_EXECUTION_TIME], [QUERY_PERFORMANCE_VIEW], [QUERY_HASH], [DURATION_MS], [CPU_TIME_MS], [LOGICAL_READS], [PHYSICAL_READS], [QUERY_EXECUTION_LOG], [EXECUTION_DATE], [ANALYSIS_DAYS], [TOP_N_QUERIES], [DURATION_WEIGHT], [CPU_WEIGHT], [IO_WEIGHT], [WAIT_TYPE], [WAITING_TASKS_COUNT], [WAIT_TIME_MS], [MAX_WAIT_TIME_MS], [SIGNAL_WAIT_TIME_MS], [WAIT_STATS_VIEW], [OBJECT_ID], [INDEX_NAME], [USER_SEEKS], [USER_SCANS], [USER_LOOKUPS], [USER_UPDATES], [INDEX_USAGE_STATS_VIEW], [DATABASE_NAME], [PLAN_HASH], [CACHED_TIME], [TOTAL_WORKER_TIME], [TOTAL_ELAPSED_TIME], [QUERY_PLAN], [HIGH_IO_THRESHOLD], [HIGH_CPU_THRESHOLD], [HIGH_DURATION_THRESHOLD], [PLAN_CACHE_VIEW], [ANALYSIS_HOURS], [SCHEMA_NAME], [TABLE_NAME], [COLUMN_NAME], [COLUMN_USAGE], [AVG_TOTAL_USER_COST], [AVG_USER_IMPACT], [SYSTEM_SEEKS], [SYSTEM_SCANS], [MISSING_INDEX_DETAILS_VIEW], [INDEX_GROUP_HANDLE], [MISSING_INDEX_GROUPS_VIEW], [GROUP_HANDLE], [MISSING_INDEX_GROUP_STATS_VIEW], [TARGET_DATABASE], [PATTERN_ANALYSIS_DAYS], [EXECUTION_TIME], [COMPLEXITY_ANALYSIS_DAYS], [LENGTH_WEIGHT], [JOIN_WEIGHT], [WHERE_WEIGHT], [GROUP_WEIGHT], [ORDER_WEIGHT], [UNION_WEIGHT]

## Usage Examples

### Example 1: OLAP Data Warehouse Baseline
```
DATABASE_PLATFORM: "SQL Server 2022"
ORGANIZATION_NAME: "DataMart Solutions"
WORKLOAD_TYPE: "OLAP"
ANALYSIS_PERIOD_DAYS: "30"
TOP_N_QUERIES: "50"
ANALYSIS_METHODOLOGY: "Comprehensive baseline with execution plan analysis"
PERFORMANCE_OBJECTIVES: "Identify queries >30s execution time for optimization"
```

### Example 2: High-Volume OLTP Baseline
```
DATABASE_PLATFORM: "PostgreSQL 15"
ORGANIZATION_NAME: "E-commerce Platform"
WORKLOAD_TYPE: "OLTP"
ANALYSIS_PERIOD_DAYS: "7"
TOP_N_QUERIES: "100"
DURATION_WEIGHT: "2.0"
CPU_WEIGHT: "1.5"
IO_WEIGHT: "1.0"
```

### Example 3: Hybrid Workload Pattern Analysis
```
DATABASE_PLATFORM: "Snowflake"
ORGANIZATION_NAME: "Financial Analytics Corp"
WORKLOAD_TYPE: "Hybrid"
PATTERN_ANALYSIS_DAYS: "14"
COMPLEXITY_ANALYSIS_DAYS: "30"
HIGH_IO_THRESHOLD: "10000000"
HIGH_CPU_THRESHOLD: "5000"
```

## Best Practices

1. **Establish clear baselines** - Capture metrics before optimization for comparison
2. **Focus on high-impact queries** - Prioritize queries with highest performance impact score
3. **Analyze execution plans systematically** - Look for table scans, missing indexes, and expensive operators
4. **Consider workload patterns** - Identify peak load times and optimize accordingly
5. **Track wait statistics** - Understand where the database is spending time waiting
6. **Document findings thoroughly** - Create detailed reports for stakeholder review
7. **Set realistic thresholds** - Define what constitutes a performance problem for your workload
8. **Review index usage regularly** - Identify unused indexes and missing index opportunities
9. **Correlate metrics across dimensions** - Connect execution time with I/O, CPU, and waits
10. **Update baselines periodically** - Refresh benchmarks as workload evolves

## Tips for Success

- Run baseline queries during representative workload periods (not maintenance windows)
- Capture both average and peak performance metrics for complete picture
- Use performance impact scores to prioritize optimization efforts objectively
- Document query complexity metrics to justify optimization investments
- Archive baseline reports for trend analysis over time
- Cross-reference wait statistics with execution plan issues
- Include business context (e.g., report names, user impact) in analysis
- Set up automated baseline collection for continuous monitoring
- Share findings with stakeholders using clear, non-technical summaries
- Create visual dashboards from baseline data for easier consumption
