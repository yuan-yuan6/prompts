---
title: Pipeline Orchestration Template
category: data-analytics/Analytics Engineering
tags: ['data-engineering', 'orchestration', 'airflow', 'workflow']
use_cases:
  - Design pipeline orchestration using Airflow, Prefect, or Dagster with DAG management, dependency handling, and scheduling.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Pipeline Orchestration Template

## Purpose
Design pipeline orchestration using Airflow, Prefect, or Dagster with DAG management, dependency handling, and scheduling.

## Quick Start

### For Data Engineers

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific design needs
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
- Design pipeline orchestration using Airflow, Prefect, or Dagster with DAG management, dependency handling, and scheduling.
- Project-specific implementations
- Research and analysis workflows



## Template

---
title: Pipeline Development & Orchestration Template
category: data-analytics/Analytics Engineering
tags: [automation, data-analytics, design, development, machine-learning, security, strategy, template]
use_cases:
  - Creating design comprehensive etl/elt pipeline development strategies including data ingestion, transformation processing, orchestration workflows, monitoring systems, and automation frameworks for enterprise data platforms.

  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---


# Pipeline Development & Orchestration Template


## Purpose
Design comprehensive ETL/ELT pipeline development strategies including data ingestion, transformation processing, orchestration workflows, monitoring systems, and automation frameworks for enterprise data platforms.


### For Data Engineers
Get started building production pipelines in 3 steps:

1. **Define Your Pipeline Architecture**
   - Choose methodology: ETL (extract-transform-load) or ELT (extract-load-transform)
   - Select orchestration platform: Airflow, Prefect, Dagster, or cloud-native (Azure Data Factory, AWS Step Functions)
   - Determine processing framework: Spark, Pandas/Dask, or cloud services
   - Example: `PIPELINE_METHODOLOGY: "ELT", ORCHESTRATION_PLATFORM: "Apache Airflow", PROCESSING_FRAMEWORK: "PySpark"`

2. **Set Up Core Components**
   - **Ingestion Layer**: Configure source connectors, implement extraction logic with error handling
   - **Transformation Layer**: Build bronze→silver→gold transformations with data quality checks
   - **Orchestration**: Create DAG with task dependencies, retries, and monitoring
   - Start with template code blocks for batch ingestion, streaming, or CDC patterns

3. **Deploy with Monitoring**
   - Implement logging framework and alerting system
   - Configure performance metrics collection (execution time, throughput, error rates)
   - Set up SLA monitoring and automated notifications
   - Use provided monitoring dashboard configurations

**Key Template Sections**: Ingestion patterns (lines 71-347), Transformation logic (464-823), Orchestration (826-1068), Monitoring (1070-1282)


You are a data pipeline architect specializing in [PIPELINE_METHODOLOGY]. Design a comprehensive pipeline development and orchestration solution for [ORGANIZATION_NAME] to support [DATA_PROCESSING_OBJECTIVES] using [ORCHESTRATION_PLATFORM] and [PROCESSING_FRAMEWORK].

- Orchestration approach: [ORCHESTRATION_APPROACH] (Code-first/UI-based/Hybrid)

- Orchestration platform: [ORCHESTRATION_PLATFORM] (Airflow/Prefect/Dagster/Azure Data Factory)

- Workflow engine: [WORKFLOW_ENGINE]

# [SOURCE_SYSTEM_1] ingestion pipeline
from [ORCHESTRATION_PLATFORM] import DAG, task
from [PROCESSING_FRAMEWORK] import DataFrame
import [DATABASE_CONNECTOR]

@task
def extract_[SOURCE_1_SHORT]_data(
    connection_string: str,
    extraction_query: str,
    extraction_date: str
) -> DataFrame:
    """
    Extract data from [SOURCE_SYSTEM_1]


# Data transformation orchestration
from [TRANSFORMATION_FRAMEWORK] import TransformationEngine

class DataTransformationPipeline:
    def __init__(self, config: dict):
        self.config = config
        self.engine = TransformationEngine([ENGINE_CONFIG])
        self.lineage_tracker = [LINEAGE_TRACKER]([LINEAGE_CONFIG])

    @task
    def bronze_to_silver_transformation(
        self,
        source_table: str,
        target_table: str,
        transformation_date: str
    ) -> dict:
        """
        Transform raw data from bronze to silver layer


ORCHESTRATION LAYER:

Workflow Definition (Apache Airflow):
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


Advanced Orchestration Patterns:
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

# Orchestration platform deployment
resource "[CLOUD_PROVIDER]_[ORCHESTRATION_SERVICE]" "[ORCHESTRATION_INSTANCE]" {
  name                = "[ORCHESTRATION_INSTANCE_NAME]"
  service_version     = "[ORCHESTRATION_VERSION]"
  instance_type       = "[ORCHESTRATION_INSTANCE_TYPE]"

  # High availability configuration
  availability_zones  = [AVAILABILITY_ZONES]
  replica_count       = [REPLICA_COUNT]

  # Storage configuration
  storage {
    size              = [STORAGE_SIZE]
    type              = "[STORAGE_TYPE]"
    encryption        = true
  }

  # Networking
  vpc_configuration {
    vpc_id            = [VPC_ID]
    subnet_ids        = [PRIVATE_SUBNET_IDS]
    security_group_id = [ORCHESTRATION_SECURITY_GROUP_ID]
  }

  # Monitoring and logging
  monitoring {
    enabled           = true
    log_level         = "[LOG_LEVEL]"
    metrics_enabled   = true
  }
}


Container Orchestration:
```yaml

OUTPUT: Deliver comprehensive pipeline development and orchestration solution including:

2. Source code for ingestion, transformation, and orchestration components

## Variables
[PIPELINE_METHODOLOGY], [ORGANIZATION_NAME], [DATA_PROCESSING_OBJECTIVES], [ORCHESTRATION_PLATFORM], [PROCESSING_FRAMEWORK], [INDUSTRY_SECTOR], [DATA_PROCESSING_DOMAIN], [PIPELINE_SCOPE], [SLA_REQUIREMENTS], [COMPLIANCE_STANDARDS], [BUDGET_CONSTRAINTS], [PROJECT_TIMELINE], [PIPELINE_PATTERN], [ORCHESTRATION_APPROACH], [DATA_MOVEMENT_STRATEGY], [ERROR_HANDLING_PHILOSOPHY], [SCALABILITY_APPROACH], [SECURITY_MODEL], [MONITORING_STRATEGY], [CLOUD_PROVIDER], [COMPUTE_PLATFORM], [STORAGE_SYSTEMS], [MESSAGE_QUEUE_SYSTEM], [WORKFLOW_ENGINE], [CONTAINER_PLATFORM], [IAC_TOOL], [SOURCE_SYSTEMS], [TARGET_SYSTEMS], [CURRENT_DATA_VOLUME], [PROJECTED_DATA_VOLUME], [DATA_VELOCITY], [DATA_VARIETY], [LATENCY_REQUIREMENTS], [FRESHNESS_REQUIREMENTS], [RETENTION_POLICIES], [SOURCE_SYSTEM_1], [CONNECTION_DETAILS], [EXTRACTION_QUERY_TEMPLATE], [DATE_PARAMETER], [DATABASE_CONNECTOR], [CONNECTION_PARAMETERS], [DATE_FORMAT], [FILTER_PARAMETER_1], [FILTER_VALUE_1], [FILTER_PARAMETER_2], [FILTER_VALUE_2], [CHUNK_SIZE], [READ_OPTIONS], [PRIMARY_KEY_COLUMNS], [EXTRACTION_TIMESTAMP], [SOURCE_SYSTEM_ID], [EXTRACTION_BATCH_ID], [BATCH_ID_GENERATOR], [CURRENT_TIMESTAMP], [LOGGING_FRAMEWORK], [ALERTING_SYSTEM], [ERROR_NOTIFICATION_LIST], [COMPLETENESS_RULE_1], [COMPLETENESS_CHECK_1], [COMPLETENESS_RULE_2], [COMPLETENESS_CHECK_2], [VALIDITY_CHECK_1], [VALIDITY_RULE_1], [VALIDITY_CHECK_2], [VALIDITY_RULE_2], [CONSISTENCY_CHECK_1], [CONSISTENCY_RULE_1], [CONSISTENCY_CHECK_2], [CONSISTENCY_RULE_2], [BUSINESS_RULE_1], [BUSINESS_VALIDATION_1], [BUSINESS_RULE_2], [BUSINESS_VALIDATION_2], [VALIDATION_LOGGER], [PROCESSING_DATE], [QUALITY_CALCULATION_LOGIC], [DATA_QUALITY_SCORE], [STAGING_DB_CONNECTOR], [STAGING_CONNECTION], [LOAD_STRATEGY], [IF_EXISTS_STRATEGY], [LOAD_METHOD], [LOAD_CHUNK_SIZE], [BATCH_COLUMN], [CURRENT_BATCH], [CONTROL_TABLE_MANAGER], [LOAD_DURATION], [LOAD_TIMESTAMP], [STREAMING_SOURCE], [STREAMING_FRAMEWORK], [MESSAGE_QUEUE], [CONSUMER_CONFIG], [PRODUCER_CONFIG], [SOURCE_FORMAT], [KAFKA_BROKERS], [SOURCE_TOPICS], [STARTING_OFFSET_STRATEGY], [MAX_OFFSETS_PER_TRIGGER], [FAIL_ON_DATA_LOSS], [MESSAGE_SCHEMA], [INGESTION_TIMESTAMP], [SOURCE_PARTITION], [PARTITION_LOGIC], [MESSAGE_KEY], [KEY_GENERATION_LOGIC], [FILTER_CONDITIONS], [DEDUPLICATION_COLUMNS], [SINK_FORMAT], [OUTPUT_MODE], [SINK_PATH], [SINK_SPECIFIC_OPTIONS], [SINK_VALUES], [TRIGGER_INTERVAL], [NULL_CHECK_CONDITIONS], [RANGE_VALIDATION_CONDITIONS], [BUSINESS_RULE_CONDITIONS], [QUALITY_FLAG], [QUALITY_FLAG_LOGIC], [DLQ_CONSUMER_CONFIG], [REPROCESSING_LOGIC], [ERROR_TRACKING], [CDC_SOURCE], [CDC_FRAMEWORK], [CDC_CONFIG], [SOURCE_HOST], [SOURCE_DATABASE], [SOURCE_USERNAME], [SOURCE_PASSWORD], [SOURCE_PORT], [SSL_MODE], [CDC_TABLE_LIST], [CAPTURE_MODE], [INITIAL_SNAPSHOT_REQUIRED], [MAX_BATCH_SIZE], [POLL_INTERVAL], [HEARTBEAT_INTERVAL], [MAX_EVENTS_PER_BATCH], [FETCH_TIMEOUT], [EVENT_TYPE_COLUMN], [TABLE_NAME_COLUMN], [EVENT_DATA_COLUMN], [INSERT_PROCESSING_LOGIC], [UPDATE_PROCESSING_LOGIC], [DELETE_PROCESSING_LOGIC], [CHECKPOINT_COLUMN], [ERROR_HANDLER], [TRANSFORMATION_FRAMEWORK], [ENGINE_CONFIG], [LINEAGE_TRACKER], [LINEAGE_CONFIG], [DATE_COLUMN], [QUALITY_FILTER], [QUALITY_THRESHOLD], [CLEANING_TRANSFORMATIONS], [WRITE_MODE], [PARTITION_COLUMNS], [TRANSFORMATION_LIST], [COLUMN_1], [DEFAULT_VALUE_1], [COLUMN_2], [DEFAULT_VALUE_2], [COLUMN_3], [DEFAULT_VALUE_3], [COLUMN_4], [TARGET_TYPE_1], [COLUMN_5], [TARGET_TYPE_2], [COLUMN_6], [TARGET_TYPE_3], [PHONE_COLUMN], [PHONE_STANDARDIZER], [EMAIL_COLUMN], [OUTLIER_COLUMNS], [REFERENCE_DATA_1], [LOOKUP_COLUMN_1], [REFERENCE_KEY_1], [MAPPED_COLUMN], [SOURCE_COLUMN], [CODE_MAPPING_DICT], [CALCULATED_COLUMN_1], [CALCULATION_LOGIC_1], [CALCULATED_COLUMN_2], [CALCULATION_LOGIC_2], [HIERARCHY_COLUMNS], [EXTERNAL_ENRICHMENT_ENABLED], [API_CONFIG], [ML_ENRICHMENT_ENABLED], [ML_MODEL_CONFIG], [GEOSPATIAL_ENRICHMENT_ENABLED], [GEO_CONFIG], [JOIN_CONFIGURATION], [AGGREGATION_REQUIRED], [DIMENSIONAL_MODEL_ENABLED], [GOLD_WRITE_MODE], [GOLD_PARTITION_COLUMNS], [OPTIMIZATION_STRATEGY], [KPI_1], [KPI_1_CALCULATION], [KPI_2], [KPI_2_CALCULATION], [KPI_3], [KPI_3_CALCULATION], [CATEGORY_COLUMN], [CATEGORIZATION_LOGIC], [TIME_PERIOD], [TIME_PERIOD_LOGIC], [FISCAL_PERIOD], [FISCAL_PERIOD_LOGIC], [RANK_COLUMN], [SCORE_COLUMN], [RANK_METHOD], [RANK_ASCENDING], [EXPIRATION_DATE], [CURRENT_DATE], [IS_CURRENT], [EFFECTIVE_DATE], [HIGH_DATE], [VERSION_NUMBER], [NEW_VERSION_LOGIC], [CONCATENATION_LOGIC], [WINDOW_SIZE], [VALUE_COLUMN], [LAG_PERIODS], [AMOUNT_COLUMN], [RUNNING_TOTAL], [MOVING_AVERAGE], [PREVIOUS_VALUE], [RANK], [PERCENTILE_RANK], [DAG_ID], [PIPELINE_OWNER], [DEPENDS_ON_PAST], [START_YEAR], [START_MONTH], [START_DAY], [EMAIL_ON_FAILURE], [EMAIL_ON_RETRY], [RETRY_COUNT], [RETRY_DELAY_MINUTES], [MAX_ACTIVE_RUNS], [CONCURRENCY_LIMIT], [DAG_DESCRIPTION], [SCHEDULE_INTERVAL], [CATCHUP_ENABLED], [TAG_1], [TAG_2], [TAG_3], [SOURCE_1_TASK], [SOURCE_1_SHORT], [SOURCE_1_CONNECTION], [SOURCE_1_QUERY], [RESOURCE_POOL_1], [SOURCE_1_RETRIES], [SOURCE_2_TASK], [SOURCE_2_SHORT], [SOURCE_2_CONNECTION], [SOURCE_2_QUERY], [RESOURCE_POOL_2], [SOURCE_2_RETRIES], [SOURCE_SYSTEM_2], [BRONZE_TO_SILVER_FUNCTION], [BRONZE_TABLE_1], [BRONZE_TABLE_2], [SILVER_TABLE], [TRANSFORMATION_POOL], [SILVER_TO_GOLD_FUNCTION], [SILVER_TABLE_1], [SILVER_TABLE_2], [GOLD_TABLE], [DATA_QUALITY_FUNCTION], [SUCCESS_NOTIFICATION_FUNCTION], [PIPELINE_NAME], [FAILURE_NOTIFICATION_FUNCTION], [DATA_VOLUME_CHECK_LOGIC], [LARGE_VOLUME_THRESHOLD], [MEDIUM_VOLUME_THRESHOLD], [LARGE_VOLUME_PROCESSOR], [MEDIUM_VOLUME_PROCESSOR], [SMALL_VOLUME_PROCESSOR], [MONITORING_FRAMEWORK], [METRICS_CONFIG], [ALERT_CONFIG], [PIPELINE_DASHBOARD_NAME], [STATUS_REFRESH_INTERVAL], [DURATION_TIME_RANGE], [VOLUME_GROUPING], [CRITICAL_NOTIFICATION_CHANNEL], [HIGH_NOTIFICATION_CHANNEL], [MEDIUM_NOTIFICATION_CHANNEL], [METRICS_STREAMING_SYSTEM], [STREAM_CONFIG], [METRICS_TABLE], [MONITORING_WINDOW], [LATENCY_THRESHOLD_MS], [THROUGHPUT_THRESHOLD], [BACKLOG_THRESHOLD], [PIPELINE_LOGGER], [ERROR_STORAGE_SYSTEM], [ERROR_STORE_CONFIG], [STACK_TRACE_EXTRACTION], [MAX_CONNECTION_RETRIES], [DEFAULT_BATCH_SIZE], [CURRENT_TIME], [QUARANTINE_SCHEMA], [DATABASE_EXECUTOR], [PERFORMANCE_METRICS_COLLECTOR], [ANALYSIS_TIME_RANGE], [AVG_DURATION_CALCULATION], [P95_DURATION_CALCULATION], [AVG_THROUGHPUT_CALCULATION], [PEAK_CPU_CALCULATION], [PEAK_MEMORY_CALCULATION], [AVG_ERROR_RATE_CALCULATION], [DATA_VOLUME_TREND_CALCULATION], [PARALLELIZATION_IMPROVEMENT_ESTIMATE], [BATCH_SIZE_IMPROVEMENT_ESTIMATE], [SCALING_IMPROVEMENT_ESTIMATE], [CACHING_IMPROVEMENT_ESTIMATE], [MEMORY_IMPROVEMENT_ESTIMATE], [STREAMING_IMPROVEMENT_ESTIMATE], [IMPROVEMENT_WEIGHT], [EFFORT_WEIGHT], [MAX_BATCH_SIZE_MULTIPLIER], [MIN_BATCH_SIZE], [MAX_BATCH_SIZE], [CPU_SCALE_UP_THRESHOLD], [CPU_SCALE_DOWN_THRESHOLD], [MEMORY_SCALE_UP_THRESHOLD], [MEMORY_SCALE_DOWN_THRESHOLD], [MIN_INSTANCES], [MAX_INSTANCES], [SCALE_UP_COOLDOWN], [SCALE_DOWN_COOLDOWN], [COMPUTE_RESOURCE], [CLUSTER_NAME], [VERSION], [NODE_COUNT], [NODE_TYPE], [DISK_SIZE], [MIN_NODES], [MAX_NODES], [TARGET_CPU_UTILIZATION], [TARGET_MEMORY_UTILIZATION], [VPC_ID], [SUBNET_IDS], [SECURITY_GROUP_IDS], [ENVIRONMENT], [PROJECT_NAME], [TEAM_OWNER], [ORCHESTRATION_SERVICE], [ORCHESTRATION_INSTANCE], [ORCHESTRATION_INSTANCE_NAME], [ORCHESTRATION_VERSION], [ORCHESTRATION_INSTANCE_TYPE], [AVAILABILITY_ZONES], [REPLICA_COUNT], [STORAGE_SIZE], [STORAGE_TYPE], [PRIVATE_SUBNET_IDS], [ORCHESTRATION_SECURITY_GROUP_ID], [LOG_LEVEL], [STORAGE_SERVICE], [DATA_LAKE_STORAGE], [DATA_LAKE_BUCKET_NAME], [STORAGE_CLASS], [TRANSITION_TO_IA_DAYS], [INFREQUENT_ACCESS_CLASS], [TRANSITION_TO_GLACIER_DAYS], [ARCHIVE_CLASS], [EXPIRATION_DAYS], [ENCRYPTION_ALGORITHM], [KMS_KEY_ID], [DATABASE_SERVICE], [DATA_WAREHOUSE], [DATA_WAREHOUSE_IDENTIFIER], [DATABASE_ENGINE], [DATABASE_VERSION], [DATABASE_INSTANCE_CLASS], [DATABASE_STORAGE_SIZE], [MULTI_AZ_ENABLED], [BACKUP_RETENTION_DAYS], [BACKUP_WINDOW], [MAINTENANCE_WINDOW], [DATABASE_SECURITY_GROUP_IDS], [DATABASE_SUBNET_GROUP], [DATABASE_KMS_KEY_ID], [MONITORING_INTERVAL], [PIPELINE_SERVICE_NAME], [NAMESPACE], [SERVICE_VERSION], [CONTAINER_NAME], [CONTAINER_IMAGE], [IMAGE_TAG], [CONTAINER_PORT], [ENV_VAR_1], [ENV_VALUE_1], [ENV_VAR_2], [SECRET_NAME], [SECRET_KEY], [MEMORY_REQUEST], [CPU_REQUEST], [MEMORY_LIMIT], [CPU_LIMIT], [VOLUME_NAME], [MOUNT_PATH], [HEALTH_CHECK_PATH], [HEALTH_CHECK_PORT], [LIVENESS_INITIAL_DELAY], [LIVENESS_PERIOD], [READINESS_CHECK_PATH], [READINESS_CHECK_PORT], [READINESS_INITIAL_DELAY], [READINESS_PERIOD], [PVC_NAME], [SERVICE_NAME], [SERVICE_PORT], [SERVICE_TYPE], [HPA_NAME], [MIN_REPLICAS], [MAX_REPLICAS], [CPU_TARGET_UTILIZATION], [MEMORY_TARGET_UTILIZATION], [DEPLOYMENT_REGION]


ORCHESTRATION_PLATFORM: "Apache Airflow"

ORCHESTRATION_PLATFORM: "Prefect"

ORCHESTRATION_PLATFORM: "Azure Data Factory"

## Customization Options

1. **Pipeline Methodologies**
   - Traditional ETL (Extract-Transform-Load)
   - Modern ELT (Extract-Load-Transform)
   - Reverse ETL (Warehouse to operational systems)
   - Change Data Capture (CDC)
   - Real-time streaming
   - Hybrid batch and streaming

2. **Orchestration Platforms**
   - Apache Airflow
   - Prefect
   - Dagster
   - Azure Data Factory
   - Google Cloud Composer
   - AWS Step Functions
   - Apache NiFi

3. **Processing Frameworks**
   - Apache Spark (PySpark/Scala)
   - Apache Flink
   - Pandas/Dask (Python)
   - Ray
   - Apache Beam
   - Native cloud processing services

4. **Architecture Patterns**
   - Lambda architecture
   - Kappa architecture
   - Data mesh
   - Medallion architecture (Bronze-Silver-Gold)
   - Hub and spoke
   - Event-driven architecture

5. **Industry Specializations**
   - Financial services (real-time fraud detection)
   - Healthcare (HIPAA-compliant pipelines)
   - Retail/E-commerce (customer 360 view)
   - Manufacturing (IoT sensor data)
   - Media/Entertainment (content processing)
   - Government (compliance-heavy workflows)

## Variables

[PIPELINE_METHODOLOGY], [ORGANIZATION_NAME], [DATA_PROCESSING_OBJECTIVES], [ORCHESTRATION_PLATFORM], [PROCESSING_FRAMEWORK], [INDUSTRY_SECTOR], [DATA_PROCESSING_DOMAIN], [PIPELINE_SCOPE], [SLA_REQUIREMENTS], [COMPLIANCE_STANDARDS], [BUDGET_CONSTRAINTS], [PROJECT_TIMELINE], [PIPELINE_PATTERN], [ORCHESTRATION_APPROACH], [DATA_MOVEMENT_STRATEGY], [ERROR_HANDLING_PHILOSOPHY], [SCALABILITY_APPROACH], [SECURITY_MODEL], [MONITORING_STRATEGY], [CLOUD_PROVIDER], [COMPUTE_PLATFORM], [STORAGE_SYSTEMS], [MESSAGE_QUEUE_SYSTEM], [WORKFLOW_ENGINE], [CONTAINER_PLATFORM], [IAC_TOOL], [SOURCE_SYSTEMS], [TARGET_SYSTEMS], [CURRENT_DATA_VOLUME], [PROJECTED_DATA_VOLUME], [DATA_VELOCITY], [DATA_VARIETY], [LATENCY_REQUIREMENTS], [FRESHNESS_REQUIREMENTS], [RETENTION_POLICIES], [SOURCE_SYSTEM_1], [CONNECTION_DETAILS], [EXTRACTION_QUERY_TEMPLATE], [DATE_PARAMETER], [DATABASE_CONNECTOR], [CONNECTION_PARAMETERS], [DATE_FORMAT], [FILTER_PARAMETER_1], [FILTER_VALUE_1], [FILTER_PARAMETER_2], [FILTER_VALUE_2], [CHUNK_SIZE], [READ_OPTIONS], [PRIMARY_KEY_COLUMNS], [EXTRACTION_TIMESTAMP], [SOURCE_SYSTEM_ID], [EXTRACTION_BATCH_ID], [BATCH_ID_GENERATOR], [CURRENT_TIMESTAMP], [LOGGING_FRAMEWORK], [ALERTING_SYSTEM], [ERROR_NOTIFICATION_LIST], [COMPLETENESS_RULE_1], [COMPLETENESS_CHECK_1], [COMPLETENESS_RULE_2], [COMPLETENESS_CHECK_2], [VALIDITY_CHECK_1], [VALIDITY_RULE_1], [VALIDITY_CHECK_2], [VALIDITY_RULE_2], [CONSISTENCY_CHECK_1], [CONSISTENCY_RULE_1], [CONSISTENCY_CHECK_2], [CONSISTENCY_RULE_2], [BUSINESS_RULE_1], [BUSINESS_VALIDATION_1], [BUSINESS_RULE_2], [BUSINESS_VALIDATION_2], [VALIDATION_LOGGER], [PROCESSING_DATE], [QUALITY_CALCULATION_LOGIC], [DATA_QUALITY_SCORE], [STAGING_DB_CONNECTOR], [STAGING_CONNECTION], [LOAD_STRATEGY], [IF_EXISTS_STRATEGY], [LOAD_METHOD], [LOAD_CHUNK_SIZE], [BATCH_COLUMN], [CURRENT_BATCH], [CONTROL_TABLE_MANAGER], [LOAD_DURATION], [LOAD_TIMESTAMP], [STREAMING_SOURCE], [STREAMING_FRAMEWORK], [MESSAGE_QUEUE], [CONSUMER_CONFIG], [PRODUCER_CONFIG], [SOURCE_FORMAT], [KAFKA_BROKERS], [SOURCE_TOPICS], [STARTING_OFFSET_STRATEGY], [MAX_OFFSETS_PER_TRIGGER], [FAIL_ON_DATA_LOSS], [MESSAGE_SCHEMA], [INGESTION_TIMESTAMP], [SOURCE_PARTITION], [PARTITION_LOGIC], [MESSAGE_KEY], [KEY_GENERATION_LOGIC], [FILTER_CONDITIONS], [DEDUPLICATION_COLUMNS], [SINK_FORMAT], [OUTPUT_MODE], [SINK_PATH], [SINK_SPECIFIC_OPTIONS], [SINK_VALUES], [TRIGGER_INTERVAL], [NULL_CHECK_CONDITIONS], [RANGE_VALIDATION_CONDITIONS], [BUSINESS_RULE_CONDITIONS], [QUALITY_FLAG], [QUALITY_FLAG_LOGIC], [DLQ_CONSUMER_CONFIG], [REPROCESSING_LOGIC], [ERROR_TRACKING], [CDC_SOURCE], [CDC_FRAMEWORK], [CDC_CONFIG], [SOURCE_HOST], [SOURCE_DATABASE], [SOURCE_USERNAME], [SOURCE_PASSWORD], [SOURCE_PORT], [SSL_MODE], [CDC_TABLE_LIST], [CAPTURE_MODE], [INITIAL_SNAPSHOT_REQUIRED], [MAX_BATCH_SIZE], [POLL_INTERVAL], [HEARTBEAT_INTERVAL], [MAX_EVENTS_PER_BATCH], [FETCH_TIMEOUT], [EVENT_TYPE_COLUMN], [TABLE_NAME_COLUMN], [EVENT_DATA_COLUMN], [INSERT_PROCESSING_LOGIC], [UPDATE_PROCESSING_LOGIC], [DELETE_PROCESSING_LOGIC], [CHECKPOINT_COLUMN], [ERROR_HANDLER], [TRANSFORMATION_FRAMEWORK], [ENGINE_CONFIG], [LINEAGE_TRACKER], [LINEAGE_CONFIG], [DATE_COLUMN], [QUALITY_FILTER], [QUALITY_THRESHOLD], [CLEANING_TRANSFORMATIONS], [WRITE_MODE], [PARTITION_COLUMNS], [TRANSFORMATION_LIST], [COLUMN_1], [DEFAULT_VALUE_1], [COLUMN_2], [DEFAULT_VALUE_2], [COLUMN_3], [DEFAULT_VALUE_3], [COLUMN_4], [TARGET_TYPE_1], [COLUMN_5], [TARGET_TYPE_2], [COLUMN_6], [TARGET_TYPE_3], [PHONE_COLUMN], [PHONE_STANDARDIZER], [EMAIL_COLUMN], [OUTLIER_COLUMNS], [REFERENCE_DATA_1], [LOOKUP_COLUMN_1], [REFERENCE_KEY_1], [MAPPED_COLUMN], [SOURCE_COLUMN], [CODE_MAPPING_DICT], [CALCULATED_COLUMN_1], [CALCULATION_LOGIC_1], [CALCULATED_COLUMN_2], [CALCULATION_LOGIC_2], [HIERARCHY_COLUMNS], [EXTERNAL_ENRICHMENT_ENABLED], [API_CONFIG], [ML_ENRICHMENT_ENABLED], [ML_MODEL_CONFIG], [GEOSPATIAL_ENRICHMENT_ENABLED], [GEO_CONFIG], [JOIN_CONFIGURATION], [AGGREGATION_REQUIRED], [DIMENSIONAL_MODEL_ENABLED], [GOLD_WRITE_MODE], [GOLD_PARTITION_COLUMNS], [OPTIMIZATION_STRATEGY], [KPI_1], [KPI_1_CALCULATION], [KPI_2], [KPI_2_CALCULATION], [KPI_3], [KPI_3_CALCULATION], [CATEGORY_COLUMN], [CATEGORIZATION_LOGIC], [TIME_PERIOD], [TIME_PERIOD_LOGIC], [FISCAL_PERIOD], [FISCAL_PERIOD_LOGIC], [RANK_COLUMN], [SCORE_COLUMN], [RANK_METHOD], [RANK_ASCENDING], [EXPIRATION_DATE], [CURRENT_DATE], [IS_CURRENT], [EFFECTIVE_DATE], [HIGH_DATE], [VERSION_NUMBER], [NEW_VERSION_LOGIC], [CONCATENATION_LOGIC], [WINDOW_SIZE], [VALUE_COLUMN], [LAG_PERIODS], [AMOUNT_COLUMN], [RUNNING_TOTAL], [MOVING_AVERAGE], [PREVIOUS_VALUE], [RANK], [PERCENTILE_RANK], [DAG_ID], [PIPELINE_OWNER], [DEPENDS_ON_PAST], [START_YEAR], [START_MONTH], [START_DAY], [EMAIL_ON_FAILURE], [EMAIL_ON_RETRY], [RETRY_COUNT], [RETRY_DELAY_MINUTES], [MAX_ACTIVE_RUNS], [CONCURRENCY_LIMIT], [DAG_DESCRIPTION], [SCHEDULE_INTERVAL], [CATCHUP_ENABLED], [TAG_1], [TAG_2], [TAG_3], [SOURCE_1_TASK], [SOURCE_1_SHORT], [SOURCE_1_CONNECTION], [SOURCE_1_QUERY], [RESOURCE_POOL_1], [SOURCE_1_RETRIES], [SOURCE_2_TASK], [SOURCE_2_SHORT], [SOURCE_2_CONNECTION], [SOURCE_2_QUERY], [RESOURCE_POOL_2], [SOURCE_2_RETRIES], [SOURCE_SYSTEM_2], [BRONZE_TO_SILVER_FUNCTION], [BRONZE_TABLE_1], [BRONZE_TABLE_2], [SILVER_TABLE], [TRANSFORMATION_POOL], [SILVER_TO_GOLD_FUNCTION], [SILVER_TABLE_1], [SILVER_TABLE_2], [GOLD_TABLE], [DATA_QUALITY_FUNCTION], [SUCCESS_NOTIFICATION_FUNCTION], [PIPELINE_NAME], [FAILURE_NOTIFICATION_FUNCTION], [DATA_VOLUME_CHECK_LOGIC], [LARGE_VOLUME_THRESHOLD], [MEDIUM_VOLUME_THRESHOLD], [LARGE_VOLUME_PROCESSOR], [MEDIUM_VOLUME_PROCESSOR], [SMALL_VOLUME_PROCESSOR], [MONITORING_FRAMEWORK], [METRICS_CONFIG], [ALERT_CONFIG], [PIPELINE_DASHBOARD_NAME], [STATUS_REFRESH_INTERVAL], [DURATION_TIME_RANGE], [VOLUME_GROUPING], [CRITICAL_NOTIFICATION_CHANNEL], [HIGH_NOTIFICATION_CHANNEL], [MEDIUM_NOTIFICATION_CHANNEL], [METRICS_STREAMING_SYSTEM], [STREAM_CONFIG], [METRICS_TABLE], [MONITORING_WINDOW], [LATENCY_THRESHOLD_MS], [THROUGHPUT_THRESHOLD], [BACKLOG_THRESHOLD], [PIPELINE_LOGGER], [ERROR_STORAGE_SYSTEM], [ERROR_STORE_CONFIG], [STACK_TRACE_EXTRACTION], [MAX_CONNECTION_RETRIES], [DEFAULT_BATCH_SIZE], [CURRENT_TIME], [QUARANTINE_SCHEMA], [DATABASE_EXECUTOR], [PERFORMANCE_METRICS_COLLECTOR], [ANALYSIS_TIME_RANGE], [AVG_DURATION_CALCULATION], [P95_DURATION_CALCULATION], [AVG_THROUGHPUT_CALCULATION], [PEAK_CPU_CALCULATION], [PEAK_MEMORY_CALCULATION], [AVG_ERROR_RATE_CALCULATION], [DATA_VOLUME_TREND_CALCULATION], [PARALLELIZATION_IMPROVEMENT_ESTIMATE], [BATCH_SIZE_IMPROVEMENT_ESTIMATE], [SCALING_IMPROVEMENT_ESTIMATE], [CACHING_IMPROVEMENT_ESTIMATE], [MEMORY_IMPROVEMENT_ESTIMATE], [STREAMING_IMPROVEMENT_ESTIMATE], [IMPROVEMENT_WEIGHT], [EFFORT_WEIGHT], [MAX_BATCH_SIZE_MULTIPLIER], [MIN_BATCH_SIZE], [MAX_BATCH_SIZE], [CPU_SCALE_UP_THRESHOLD], [CPU_SCALE_DOWN_THRESHOLD], [MEMORY_SCALE_UP_THRESHOLD], [MEMORY_SCALE_DOWN_THRESHOLD], [MIN_INSTANCES], [MAX_INSTANCES], [SCALE_UP_COOLDOWN], [SCALE_DOWN_COOLDOWN], [COMPUTE_RESOURCE], [CLUSTER_NAME], [VERSION], [NODE_COUNT], [NODE_TYPE], [DISK_SIZE], [MIN_NODES], [MAX_NODES], [TARGET_CPU_UTILIZATION], [TARGET_MEMORY_UTILIZATION], [VPC_ID], [SUBNET_IDS], [SECURITY_GROUP_IDS], [ENVIRONMENT], [PROJECT_NAME], [TEAM_OWNER], [ORCHESTRATION_SERVICE], [ORCHESTRATION_INSTANCE], [ORCHESTRATION_INSTANCE_NAME], [ORCHESTRATION_VERSION], [ORCHESTRATION_INSTANCE_TYPE], [AVAILABILITY_ZONES], [REPLICA_COUNT], [STORAGE_SIZE], [STORAGE_TYPE], [PRIVATE_SUBNET_IDS], [ORCHESTRATION_SECURITY_GROUP_ID], [LOG_LEVEL], [STORAGE_SERVICE], [DATA_LAKE_STORAGE], [DATA_LAKE_BUCKET_NAME], [STORAGE_CLASS], [TRANSITION_TO_IA_DAYS], [INFREQUENT_ACCESS_CLASS], [TRANSITION_TO_GLACIER_DAYS], [ARCHIVE_CLASS], [EXPIRATION_DAYS], [ENCRYPTION_ALGORITHM], [KMS_KEY_ID], [DATABASE_SERVICE], [DATA_WAREHOUSE], [DATA_WAREHOUSE_IDENTIFIER], [DATABASE_ENGINE], [DATABASE_VERSION], [DATABASE_INSTANCE_CLASS], [DATABASE_STORAGE_SIZE], [MULTI_AZ_ENABLED], [BACKUP_RETENTION_DAYS], [BACKUP_WINDOW], [MAINTENANCE_WINDOW], [DATABASE_SECURITY_GROUP_IDS], [DATABASE_SUBNET_GROUP], [DATABASE_KMS_KEY_ID], [MONITORING_INTERVAL], [PIPELINE_SERVICE_NAME], [NAMESPACE], [SERVICE_VERSION], [CONTAINER_NAME], [CONTAINER_IMAGE], [IMAGE_TAG], [CONTAINER_PORT], [ENV_VAR_1], [ENV_VALUE_1], [ENV_VAR_2], [SECRET_NAME], [SECRET_KEY], [MEMORY_REQUEST], [CPU_REQUEST], [MEMORY_LIMIT], [CPU_LIMIT], [VOLUME_NAME], [MOUNT_PATH], [HEALTH_CHECK_PATH], [HEALTH_CHECK_PORT], [LIVENESS_INITIAL_DELAY], [LIVENESS_PERIOD], [READINESS_CHECK_PATH], [READINESS_CHECK_PORT], [READINESS_INITIAL_DELAY], [READINESS_PERIOD], [PVC_NAME], [SERVICE_NAME], [SERVICE_PORT], [SERVICE_TYPE], [HPA_NAME], [MIN_REPLICAS], [MAX_REPLICAS], [CPU_TARGET_UTILIZATION], [MEMORY_TARGET_UTILIZATION], [DEPLOYMENT_REGION]

## Usage Examples

### Example 1: E-commerce ETL Pipeline
```
PIPELINE_METHODOLOGY: "ETL with batch processing"
ORGANIZATION_NAME: "RetailCorp"
ORCHESTRATION_PLATFORM: "Apache Airflow"
PROCESSING_FRAMEWORK: "Apache Spark"
PIPELINE_PATTERN: "Batch processing with CDC"
SOURCE_SYSTEMS: ["PostgreSQL", "Shopify API", "Google Analytics"]
TARGET_SYSTEMS: ["Snowflake Data Warehouse"]
```


### Example 2: Real-time Streaming Pipeline
```
PIPELINE_METHODOLOGY: "ELT with real-time streaming"
ORGANIZATION_NAME: "FinTech Solutions"
ORCHESTRATION_PLATFORM: "Prefect"
PROCESSING_FRAMEWORK: "Apache Kafka + Spark Streaming"
PIPELINE_PATTERN: "Streaming with Lambda architecture"
SOURCE_SYSTEMS: ["Kafka Topics", "REST APIs", "Database CDC"]
CLOUD_PROVIDER: "AWS"
```


### Example 3: Healthcare Data Integration
```
PIPELINE_METHODOLOGY: "Hybrid ETL/ELT"
ORGANIZATION_NAME: "HealthSystem Network"
ORCHESTRATION_PLATFORM: "Azure Data Factory"
PROCESSING_FRAMEWORK: "Azure Databricks"
COMPLIANCE_STANDARDS: ["HIPAA", "SOC 2"]
PIPELINE_PATTERN: "Batch with near real-time updates"
SOURCE_SYSTEMS: ["Epic EHR", "Lab Systems", "IoT Devices"]
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
