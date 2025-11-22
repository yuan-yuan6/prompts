---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Analytics-Engineering/pipeline-ingestion.md
- data-analytics/Analytics-Engineering/pipeline-transformation.md
- data-analytics/Analytics-Engineering/pipeline-observability.md
- data-analytics/Analytics-Engineering/pipeline-infrastructure.md
tags:
- automation
- data-analytics
title: Pipeline Orchestration Template
use_cases:
- Designing Apache Airflow DAGs for complex data pipeline workflows
- Implementing advanced orchestration patterns with branching and dynamic tasks
- Managing task dependencies, retries, and failure handling
- Scheduling and monitoring multi-step data processing workflows
industries:
- healthcare
- manufacturing
- retail
- technology
type: template
difficulty: intermediate
slug: pipeline-orchestration
---

# Pipeline Orchestration Template

## Purpose
Design and implement comprehensive workflow orchestration for data pipelines using Apache Airflow or similar platforms. This template covers DAG design, task dependencies, scheduling strategies, dynamic task generation, conditional workflows, and resource management.

## Quick Start

### For Data Engineers
Get started building orchestration workflows in 3 steps:

1. **Define DAG Structure**
   - **Schedule**: Set cron expression or schedule interval
   - **Dependencies**: Map task execution order and parallelism
   - **Retry Logic**: Configure retry attempts and delays
   - **Resources**: Assign tasks to pools and queues
   - Example: `DAG_ID: "daily_etl", SCHEDULE: "0 2 * * *", MAX_ACTIVE_RUNS: 1`

2. **Create Task Definitions**
   - **Extraction Tasks**: Pull data from sources in parallel where possible
   - **Transformation Tasks**: Process data with appropriate dependencies
   - **Validation Tasks**: Check data quality before downstream processing
   - **Notification Tasks**: Alert on success/failure
   - Start with template DAG structure (lines 69-308)

3. **Implement Advanced Patterns**
   - **Dynamic Tasks**: Generate tasks programmatically for multiple sources
   - **Branching**: Conditional execution based on data volume or quality
   - **Task Groups**: Organize related tasks for better visualization
   - Use advanced pattern examples (lines 310-401)

**Key Sections**: Workflow Definition (lines 69-308), Advanced Patterns (310-401)

## Template

```
You are a workflow orchestration architect specializing in [ORCHESTRATION_PLATFORM]. Design a comprehensive orchestration solution for [ORGANIZATION_NAME] to manage [PIPELINE_SCOPE] using [ORCHESTRATION_APPROACH] and [WORKFLOW_ENGINE].

ORCHESTRATION ARCHITECTURE OVERVIEW:
Project Specifications:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Pipeline scope: [PIPELINE_SCOPE]
- Business objectives: [DATA_PROCESSING_OBJECTIVES]
- SLA requirements: [SLA_REQUIREMENTS]
- Complexity level: [WORKFLOW_COMPLEXITY]

### Architecture Principles
- Orchestration platform: [ORCHESTRATION_PLATFORM] (Airflow/Prefect/Dagster)
- Orchestration approach: [ORCHESTRATION_APPROACH] (Code-first/UI-based/Hybrid)
- Execution model: [EXECUTION_MODEL] (Sequential/Parallel/Mixed)
- Dependency management: [DEPENDENCY_STRATEGY]
- Error handling: [ERROR_HANDLING_PHILOSOPHY]
- Resource allocation: [RESOURCE_ALLOCATION_STRATEGY]
- Scalability approach: [SCALABILITY_APPROACH]

### Technical Stack
- Workflow engine: [WORKFLOW_ENGINE]
- Task executor: [TASK_EXECUTOR] (Local/Celery/Kubernetes/Dask)
- Message broker: [MESSAGE_BROKER] (Redis/RabbitMQ)
- Metadata database: [METADATA_DB] (PostgreSQL/MySQL)
- Cloud provider: [CLOUD_PROVIDER]
- Container platform: [CONTAINER_PLATFORM]

### Workflow Requirements
- Pipeline pattern: [PIPELINE_PATTERN] (Batch/Streaming/Hybrid)
- Processing frequency: [PROCESSING_FREQUENCY]
- Data dependencies: [DATA_DEPENDENCIES]
- Catchup behavior: [CATCHUP_ENABLED]
- Max concurrent runs: [MAX_ACTIVE_RUNS]
- Timeout settings: [TIMEOUT_SETTINGS]
- Retry strategy: [RETRY_STRATEGY]

### ORCHESTRATION LAYER

### Workflow Definition (Apache Airflow)
```python
# Airflow DAG definition
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.[CLOUD_PROVIDER].operators import [CLOUD_OPERATORS]
from datetime import datetime, timedelta

# DAG configuration
default_args = {
    'owner': '[PIPELINE_OWNER]',
    'depends_on_past': [DEPENDS_ON_PAST],
    'start_date': datetime([START_YEAR], [START_MONTH], [START_DAY]),
    'email_on_failure': [EMAIL_ON_FAILURE],
    'email_on_retry': [EMAIL_ON_RETRY],
    'retries': [RETRY_COUNT],
    'retry_delay': timedelta(minutes=[RETRY_DELAY_MINUTES]),
    'max_active_runs': [MAX_ACTIVE_RUNS],
    'concurrency': [CONCURRENCY_LIMIT]
}

dag = DAG(
    '[DAG_ID]',
    default_args=default_args,
    description='[DAG_DESCRIPTION]',
    schedule_interval='[SCHEDULE_INTERVAL]',
    catchup=[CATCHUP_ENABLED],
    max_active_runs=[MAX_ACTIVE_RUNS],
    tags=['[TAG_1]', '[TAG_2]', '[TAG_3]']
)

# Source system ingestion tasks
[SOURCE_1_TASK] = PythonOperator(
    task_id='extract_[SOURCE_1_SHORT]_data',
    python_callable=extract_[SOURCE_1_SHORT]_data,
    op_kwargs={
        'connection_string': '[SOURCE_1_CONNECTION]',
        'extraction_query': '[SOURCE_1_QUERY]',
        'extraction_date': '{{ ds }}'
    },
    dag=dag,
    pool='[RESOURCE_POOL_1]',
    retries=[SOURCE_1_RETRIES]
)

[SOURCE_2_TASK] = PythonOperator(
    task_id='extract_[SOURCE_2_SHORT]_data',
    python_callable=extract_[SOURCE_2_SHORT]_data,
    op_kwargs={
        'connection_string': '[SOURCE_2_CONNECTION]',
        'extraction_query': '[SOURCE_2_QUERY]',
        'extraction_date': '{{ ds }}'
    },
    dag=dag,
    pool='[RESOURCE_POOL_2]',
    retries=[SOURCE_2_RETRIES]
)

# Data validation tasks
validate_[SOURCE_1_SHORT] = PythonOperator(
    task_id='validate_[SOURCE_1_SHORT]_data',
    python_callable=validate_source_data,
    op_kwargs={
        'source_system': '[SOURCE_SYSTEM_1]',
        'validation_date': '{{ ds }}'
    },
    dag=dag
)

validate_[SOURCE_2_SHORT] = PythonOperator(
    task_id='validate_[SOURCE_2_SHORT]_data',
    python_callable=validate_source_data,
    op_kwargs={
        'source_system': '[SOURCE_SYSTEM_2]',
        'validation_date': '{{ ds }}'
    },
    dag=dag
)

# Transformation tasks
bronze_to_silver = PythonOperator(
    task_id='bronze_to_silver_transformation',
    python_callable=[BRONZE_TO_SILVER_FUNCTION],
    op_kwargs={
        'source_tables': ['[BRONZE_TABLE_1]', '[BRONZE_TABLE_2]'],
        'target_table': '[SILVER_TABLE]',
        'transformation_date': '{{ ds }}'
    },
    dag=dag,
    pool='[TRANSFORMATION_POOL]'
)

silver_to_gold = PythonOperator(
    task_id='silver_to_gold_transformation',
    python_callable=[SILVER_TO_GOLD_FUNCTION],
    op_kwargs={
        'source_tables': ['[SILVER_TABLE_1]', '[SILVER_TABLE_2]'],
        'target_table': '[GOLD_TABLE]',
        'transformation_date': '{{ ds }}'
    },
    dag=dag,
    pool='[TRANSFORMATION_POOL]'
)

# Data quality checks
data_quality_check = PythonOperator(
    task_id='data_quality_validation',
    python_callable=[DATA_QUALITY_FUNCTION],
    op_kwargs={
        'tables_to_validate': ['[SILVER_TABLE]', '[GOLD_TABLE]'],
        'validation_date': '{{ ds }}'
    },
    dag=dag
)

# Notification tasks
success_notification = PythonOperator(
    task_id='send_success_notification',
    python_callable=[SUCCESS_NOTIFICATION_FUNCTION],
    op_kwargs={
        'pipeline_name': '[PIPELINE_NAME]',
        'processing_date': '{{ ds }}'
    },
    dag=dag,
    trigger_rule='all_success'
)

failure_notification = PythonOperator(
    task_id='send_failure_notification',
    python_callable=[FAILURE_NOTIFICATION_FUNCTION],
    op_kwargs={
        'pipeline_name': '[PIPELINE_NAME]',
        'processing_date': '{{ ds }}'
    },
    dag=dag,
    trigger_rule='one_failed'
)

# Task dependencies
[SOURCE_1_TASK] >> validate_[SOURCE_1_SHORT]
[SOURCE_2_TASK] >> validate_[SOURCE_2_SHORT]

[validate_[SOURCE_1_SHORT], validate_[SOURCE_2_SHORT]] >> bronze_to_silver
bronze_to_silver >> silver_to_gold
silver_to_gold >> data_quality_check

data_quality_check >> success_notification
[SOURCE_1_TASK, SOURCE_2_TASK, bronze_to_silver, silver_to_gold, data_quality_check] >> failure_notification
```

### Advanced Orchestration Patterns
```python
# Dynamic task generation
from airflow.models import Variable

def create_dynamic_tasks(dag, source_systems):
    """
    Dynamically create tasks for multiple source systems
    """
    extraction_tasks = []
    validation_tasks = []

    for system in source_systems:
        # Create extraction task
        extraction_task = PythonOperator(
            task_id=f'extract_{system["name"]}_data',
            python_callable=extract_data,
            op_kwargs={
                'system_config': system,
                'extraction_date': '{{ ds }}'
            },
            dag=dag
        )
        extraction_tasks.append(extraction_task)

        # Create validation task
        validation_task = PythonOperator(
            task_id=f'validate_{system["name"]}_data',
            python_callable=validate_data,
            op_kwargs={
                'system_config': system,
                'validation_date': '{{ ds }}'
            },
            dag=dag
        )
        validation_tasks.append(validation_task)

        # Set dependency
        extraction_task >> validation_task

    return extraction_tasks, validation_tasks

# Conditional task execution
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator

def decide_processing_path(**context):
    """
    Decide which processing path to take based on data volume
    """
    data_volume = [DATA_VOLUME_CHECK_LOGIC]

    if data_volume > [LARGE_VOLUME_THRESHOLD]:
        return 'large_volume_processing'
    elif data_volume > [MEDIUM_VOLUME_THRESHOLD]:
        return 'medium_volume_processing'
    else:
        return 'small_volume_processing'

branch_task = BranchPythonOperator(
    task_id='decide_processing_path',
    python_callable=decide_processing_path,
    dag=dag
)

large_volume_task = PythonOperator(
    task_id='large_volume_processing',
    python_callable=[LARGE_VOLUME_PROCESSOR],
    dag=dag
)

medium_volume_task = PythonOperator(
    task_id='medium_volume_processing',
    python_callable=[MEDIUM_VOLUME_PROCESSOR],
    dag=dag
)

small_volume_task = PythonOperator(
    task_id='small_volume_processing',
    python_callable=[SMALL_VOLUME_PROCESSOR],
    dag=dag
)

join_task = DummyOperator(
    task_id='join_processing_paths',
    dag=dag,
    trigger_rule='none_failed_min_one_success'
)

branch_task >> [large_volume_task, medium_volume_task, small_volume_task]
[large_volume_task, medium_volume_task, small_volume_task] >> join_task
```

OUTPUT: Deliver comprehensive orchestration solution including:
1. Complete DAG definitions with task dependencies
2. Dynamic task generation for scalable workflows
3. Conditional branching and execution logic
4. Resource pool configuration and management
5. Retry strategies and error handling
6. Task dependency visualization
7. Scheduling and catchup strategies
8. XCom usage for task communication
9. SLA monitoring and alerting
10. Operational runbooks for common scenarios
```

## Variables

### Core Configuration
[ORCHESTRATION_PLATFORM], [ORGANIZATION_NAME], [PIPELINE_SCOPE], [DATA_PROCESSING_OBJECTIVES], [SLA_REQUIREMENTS], [WORKFLOW_COMPLEXITY]

### Architecture Settings
[ORCHESTRATION_APPROACH], [EXECUTION_MODEL], [DEPENDENCY_STRATEGY], [ERROR_HANDLING_PHILOSOPHY], [RESOURCE_ALLOCATION_STRATEGY], [SCALABILITY_APPROACH]

### Technical Stack
[WORKFLOW_ENGINE], [TASK_EXECUTOR], [MESSAGE_BROKER], [METADATA_DB], [CLOUD_PROVIDER], [CONTAINER_PLATFORM]

### Workflow Requirements
[PIPELINE_PATTERN], [PROCESSING_FREQUENCY], [DATA_DEPENDENCIES], [CATCHUP_ENABLED], [MAX_ACTIVE_RUNS], [TIMEOUT_SETTINGS], [RETRY_STRATEGY]

### DAG Configuration
[DAG_ID], [PIPELINE_OWNER], [DEPENDS_ON_PAST], [START_YEAR], [START_MONTH], [START_DAY], [EMAIL_ON_FAILURE], [EMAIL_ON_RETRY], [RETRY_COUNT], [RETRY_DELAY_MINUTES], [CONCURRENCY_LIMIT], [DAG_DESCRIPTION], [SCHEDULE_INTERVAL], [TAG_1], [TAG_2], [TAG_3]

### Task Configuration
[SOURCE_1_TASK], [SOURCE_1_SHORT], [SOURCE_1_CONNECTION], [SOURCE_1_QUERY], [RESOURCE_POOL_1], [SOURCE_1_RETRIES], [SOURCE_2_TASK], [SOURCE_2_SHORT], [SOURCE_2_CONNECTION], [SOURCE_2_QUERY], [RESOURCE_POOL_2], [SOURCE_2_RETRIES], [SOURCE_SYSTEM_1], [SOURCE_SYSTEM_2]

### Transformation Tasks
[BRONZE_TO_SILVER_FUNCTION], [BRONZE_TABLE_1], [BRONZE_TABLE_2], [SILVER_TABLE], [TRANSFORMATION_POOL], [SILVER_TO_GOLD_FUNCTION], [SILVER_TABLE_1], [SILVER_TABLE_2], [GOLD_TABLE], [DATA_QUALITY_FUNCTION]

### Notification Tasks
[SUCCESS_NOTIFICATION_FUNCTION], [PIPELINE_NAME], [FAILURE_NOTIFICATION_FUNCTION]

### Advanced Patterns
[DATA_VOLUME_CHECK_LOGIC], [LARGE_VOLUME_THRESHOLD], [MEDIUM_VOLUME_THRESHOLD], [LARGE_VOLUME_PROCESSOR], [MEDIUM_VOLUME_PROCESSOR], [SMALL_VOLUME_PROCESSOR]

### Cloud Operators
[CLOUD_OPERATORS]

## Usage Examples

### Example 1: Daily E-commerce ETL Pipeline
```
DAG_ID: "ecommerce_daily_etl"
SCHEDULE_INTERVAL: "0 2 * * *"  # Daily at 2 AM
PIPELINE_OWNER: "data-engineering-team"
MAX_ACTIVE_RUNS: 1
CATCHUP_ENABLED: false
DEPENDENCIES:
  - extract_orders >> validate_orders >> transform_orders
  - extract_customers >> validate_customers >> transform_customers
  - [transform_orders, transform_customers] >> create_customer_360 >> quality_check
RETRY_COUNT: 3
RETRY_DELAY_MINUTES: 5
POOLS: {extraction: 5, transformation: 3, quality: 2}
```

### Example 2: Hourly Real-time Data Processing
```
DAG_ID: "streaming_aggregation_hourly"
SCHEDULE_INTERVAL: "0 * * * *"  # Every hour
EXECUTION_MODEL: "Parallel with task groups"
TASK_GROUPS:
  - ingestion: [kafka_consumer_1, kafka_consumer_2, kafka_consumer_3]
  - aggregation: [hourly_metrics, user_sessions, event_counts]
  - publishing: [update_dashboards, send_alerts]
DEPENDENCIES: ingestion >> aggregation >> publishing
DEPENDS_ON_PAST: true  # Must complete previous hour before starting next
CATCHUP_ENABLED: true  # Backfill missed hours
SLA_MINUTES: 15  # Alert if hourly run exceeds 15 minutes
```

### Example 3: Dynamic Multi-Source Ingestion
```
DAG_ID: "multi_source_dynamic_ingestion"
DYNAMIC_TASK_GENERATION: true
SOURCE_SYSTEMS: Variable.get("source_systems_config", deserialize_json=True)
PATTERN: "For each source in SOURCE_SYSTEMS, create extract and validate tasks"
PARALLELISM: "Extract all sources in parallel, validate in parallel after extraction"
CONDITIONAL_LOGIC:
  - If data_volume > 1M rows: Use Spark cluster
  - If data_volume < 1M rows: Use Pandas single node
  - If validation fails: Send to DLQ and continue with other sources
TRIGGER_RULE: "none_failed_min_one_success for final aggregation"
```

### Example 4: Data Quality-Driven Workflow
```
DAG_ID: "quality_gated_pipeline"
SCHEDULE_INTERVAL: "@daily"
BRANCHING_LOGIC:
  - quality_check >> [good_data_path, bad_data_path]
  - If quality_score > 95: proceed to gold layer
  - If 90 < quality_score < 95: quarantine and alert
  - If quality_score < 90: halt pipeline and page on-call
TRIGGER_RULES:
  - gold_layer: requires 'all_success' from quality_check
  - quarantine: trigger on 'one_failed' from quality_check
  - on_call_alert: trigger on 'all_failed'
SENSORS: Wait for upstream data availability before starting
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Pipeline Ingestion](pipeline-ingestion.md)** - Complementary approaches and methodologies
- **[Pipeline Transformation](pipeline-transformation.md)** - Strategic framework for organizational change initiatives
- **[Pipeline Observability](pipeline-observability.md)** - Complementary approaches and methodologies
- **[Pipeline Infrastructure](pipeline-infrastructure.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Pipeline Orchestration Template)
2. Use [Pipeline Ingestion](pipeline-ingestion.md) for deeper analysis
3. Apply [Pipeline Transformation](pipeline-transformation.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Analytics Engineering](../../data-analytics/Analytics Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Designing Apache Airflow DAGs for complex data pipeline workflows**: Combine this template with related analytics and strategy frameworks
- **Implementing advanced orchestration patterns with branching and dynamic tasks**: Combine this template with related analytics and strategy frameworks
- **Managing task dependencies, retries, and failure handling**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Idempotent tasks** - Ensure tasks can be safely retried without side effects
2. **Task atomicity** - Keep tasks focused on single responsibilities
3. **Resource pools** - Limit concurrent tasks to prevent resource exhaustion
4. **Explicit dependencies** - Always define task dependencies explicitly
5. **Jinja templating** - Use {{ ds }} and {{ execution_date }} for date handling
6. **XCom sparingly** - Only pass small metadata, not large datasets
7. **Task timeouts** - Set appropriate execution timeouts to catch hangs
8. **SLA monitoring** - Define SLAs for critical pipeline segments
9. **Task groups** - Organize related tasks for better DAG visualization
10. **Sensor efficiency** - Use reschedule mode for sensors to free up worker slots

## Tips for Success

- Start with simple linear DAG and add complexity incrementally
- Use DummyOperator for visualization of complex dependencies
- Leverage pools to control concurrency per resource type
- Set `depends_on_past=False` for backfills unless truly needed
- Use `max_active_runs=1` for stateful pipelines
- Test DAGs with different execution dates before deploying
- Monitor task duration trends to identify performance degradation
- Use SubDAGs or TaskGroups for reusable workflow components
- Implement proper logging within task callables for debugging
- Document task purpose and dependencies in task descriptions
- Use Variables and Connections for configuration management
- Set appropriate task priority_weight for critical paths
- Implement task sensors for external system dependencies
- Use trigger_rule='all_done' for cleanup tasks that must always run
- Consider using ExternalTaskSensor for cross-DAG dependencies
- Implement backfill strategies with careful catchup configuration
- Use dag.partial() for reducing DAG code duplication
- Monitor Airflow scheduler and worker health metrics
- Implement circuit breakers for unreliable external dependencies
- Use dynamic DAG generation sparingly (can impact scheduler performance)
