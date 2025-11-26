---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Analytics-Engineering/pipeline-transformation.md
- data-analytics/Analytics-Engineering/pipeline-orchestration.md
- data-analytics/Analytics-Engineering/pipeline-observability.md
- data-analytics/data-governance-framework.md
tags:
- automation
- data-analytics
- development
title: Pipeline Data Ingestion Template
use_cases:
- Designing batch data ingestion pipelines with validation and error handling
- Implementing real-time streaming ingestion from message queues and event sources
- Setting up Change Data Capture (CDC) pipelines for database synchronization
- Building resilient data extraction layers with retry logic and monitoring
industries:
- manufacturing
- technology
type: template
difficulty: intermediate
slug: pipeline-ingestion
---

# Pipeline Data Ingestion Template

## Purpose
Design and implement robust data ingestion pipelines for extracting data from various sources using batch processing, real-time streaming, and Change Data Capture (CDC) patterns. This template covers the data extraction layer with comprehensive error handling, validation, and monitoring.

## Quick Ingestion Prompt
Build a [BATCH/STREAMING/CDC] ingestion pipeline to extract data from [SOURCE_TYPE] into [LANDING_ZONE]. Include connection pooling, [INCREMENTAL/FULL] extraction with [WATERMARK_COLUMN], validation rules for [CRITICAL_COLUMNS], retry logic with exponential backoff, dead letter queue handling, and extraction metadata tracking.

## Quick Start

### For Data Engineers
Get started building ingestion pipelines in 3 steps:

1. **Choose Your Ingestion Pattern**
   - **Batch Ingestion**: Scheduled extraction from databases, APIs, or files
   - **Streaming Ingestion**: Real-time data from Kafka, Kinesis, or event streams
   - **CDC (Change Data Capture)**: Capture database changes in near real-time
   - Example: `INGESTION_PATTERN: "Batch", SOURCE_TYPE: "PostgreSQL", SCHEDULE: "0 2 * * *"`

2. **Configure Source Connection**
   - Set up connection parameters with secure credential management
   - Define extraction queries or stream subscriptions
   - Implement validation rules for data quality checks
   - Start with template code blocks (lines 77-247 for batch, 249-348 for streaming, 350-463 for CDC)

3. **Add Error Handling & Monitoring**
   - Configure retry logic with exponential backoff
   - Set up dead letter queues for failed records
   - Implement extraction metadata tracking
   - Enable alerting for extraction failures

**Key Sections**: Batch Ingestion (lines 77-247), Streaming Ingestion (249-348), CDC (350-463)

## Template

```
You are a data ingestion architect specializing in [INGESTION_PATTERN]. Design a comprehensive data ingestion solution for [ORGANIZATION_NAME] to extract data from [SOURCE_SYSTEMS] using [PROCESSING_FRAMEWORK] and [ORCHESTRATION_PLATFORM].

INGESTION ARCHITECTURE OVERVIEW:
Project Specifications:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Data processing domain: [DATA_PROCESSING_DOMAIN]
- Ingestion scope: [INGESTION_SCOPE]
- Business objectives: [DATA_PROCESSING_OBJECTIVES]
- SLA requirements: [SLA_REQUIREMENTS]
- Compliance standards: [COMPLIANCE_STANDARDS]

### Architecture Principles
- Ingestion pattern: [INGESTION_PATTERN] (Batch/Streaming/CDC/Hybrid)
- Processing methodology: [PIPELINE_METHODOLOGY] (ETL/ELT)
- Error handling philosophy: [ERROR_HANDLING_PHILOSOPHY]
- Data movement strategy: [DATA_MOVEMENT_STRATEGY]
- Security model: [SECURITY_MODEL]
- Monitoring strategy: [MONITORING_STRATEGY]

### Technical Stack
- Orchestration platform: [ORCHESTRATION_PLATFORM] (Airflow/Prefect/Dagster)
- Processing framework: [PROCESSING_FRAMEWORK] (Spark/Pandas/Dask)
- Cloud provider: [CLOUD_PROVIDER]
- Storage systems: [STORAGE_SYSTEMS]
- Message queuing: [MESSAGE_QUEUE_SYSTEM]
- Container platform: [CONTAINER_PLATFORM]

### Data Requirements
- Source systems: [SOURCE_SYSTEMS]
- Target systems: [TARGET_SYSTEMS]
- Data volume current: [CURRENT_DATA_VOLUME]
- Data volume projected: [PROJECTED_DATA_VOLUME]
- Data velocity: [DATA_VELOCITY]
- Latency requirements: [LATENCY_REQUIREMENTS]
- Freshness requirements: [FRESHNESS_REQUIREMENTS]
- Retention policies: [RETENTION_POLICIES]

### INGESTION LAYER DESIGN

### Batch Ingestion
Source System 1: [SOURCE_SYSTEM_1]
```python
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

    Args:
        connection_string: [CONNECTION_DETAILS]
        extraction_query: [EXTRACTION_QUERY_TEMPLATE]
        extraction_date: [DATE_PARAMETER]

    Returns:
        DataFrame with extracted data
    """
    try:
        # Connection setup
        conn = [DATABASE_CONNECTOR].connect([CONNECTION_PARAMETERS])

        # Query parameterization
        query = extraction_query.format(
            extraction_date=[DATE_FORMAT],
            [FILTER_PARAMETER_1]=[FILTER_VALUE_1],
            [FILTER_PARAMETER_2]=[FILTER_VALUE_2]
        )

        # Data extraction
        df = [PROCESSING_FRAMEWORK].read_sql(
            query,
            conn,
            chunksize=[CHUNK_SIZE],
            [READ_OPTIONS]
        )

        # Initial validation
        assert len(df) > 0, f"No data extracted for [EXTRACTION_DATE]"
        assert not df.duplicated([PRIMARY_KEY_COLUMNS]).any(), "Duplicate records found"

        # Add extraction metadata
        df['[EXTRACTION_TIMESTAMP]'] = [CURRENT_TIMESTAMP]
        df['[SOURCE_SYSTEM_ID]'] = '[SOURCE_SYSTEM_1]'
        df['[EXTRACTION_BATCH_ID]'] = [BATCH_ID_GENERATOR]

        return df

    except Exception as e:
        # Error handling and alerting
        [LOGGING_FRAMEWORK].error(f"Extraction failed: {str(e)}")
        [ALERTING_SYSTEM].send_alert(
            severity="HIGH",
            message=f"[SOURCE_SYSTEM_1] extraction failed: {str(e)}",
            recipients=[ERROR_NOTIFICATION_LIST]
        )
        raise
    finally:
        if 'conn' in locals():
            conn.close()

@task
def validate_source_data(df: DataFrame) -> DataFrame:
    """
    Validate extracted data quality and completeness

    Args:
        df: Raw extracted DataFrame

    Returns:
        Validated DataFrame with quality metrics
    """
    validation_results = {}

    # Completeness checks
    validation_results['[COMPLETENESS_CHECK_1]'] = [COMPLETENESS_RULE_1]
    validation_results['[COMPLETENESS_CHECK_2]'] = [COMPLETENESS_RULE_2]

    # Validity checks
    validation_results['[VALIDITY_CHECK_1]'] = [VALIDITY_RULE_1]
    validation_results['[VALIDITY_CHECK_2]'] = [VALIDITY_RULE_2]

    # Consistency checks
    validation_results['[CONSISTENCY_CHECK_1]'] = [CONSISTENCY_RULE_1]
    validation_results['[CONSISTENCY_CHECK_2]'] = [CONSISTENCY_RULE_2]

    # Business rule validation
    validation_results['[BUSINESS_RULE_1]'] = [BUSINESS_VALIDATION_1]
    validation_results['[BUSINESS_RULE_2]'] = [BUSINESS_VALIDATION_2]

    # Record validation results
    [VALIDATION_LOGGER].log_validation_results(
        source_system='[SOURCE_SYSTEM_1]',
        validation_date=[PROCESSING_DATE],
        results=validation_results,
        record_count=len(df)
    )

    # Add quality score
    quality_score = [QUALITY_CALCULATION_LOGIC]
    df['[DATA_QUALITY_SCORE]'] = quality_score

    return df

@task
def load_to_staging(df: DataFrame, staging_table: str) -> dict:
    """
    Load validated data to staging area

    Args:
        df: Validated DataFrame
        staging_table: Target staging table name

    Returns:
        Load statistics dictionary
    """
    try:
        # Pre-load preparation
        staging_conn = [STAGING_DB_CONNECTOR].connect([STAGING_CONNECTION])

        # Truncate/append strategy based on requirements
        if [LOAD_STRATEGY] == 'FULL_REFRESH':
            staging_conn.execute(f"TRUNCATE TABLE [STAGING_TABLE]")

        # Bulk load with error handling
        load_stats = df.to_sql(
            name=staging_table,
            con=staging_conn,
            if_exists='[IF_EXISTS_STRATEGY]',
            index=False,
            method='[LOAD_METHOD]',
            chunksize=[LOAD_CHUNK_SIZE]
        )

        # Post-load validation
        loaded_count = staging_conn.execute(
            f"SELECT COUNT(*) FROM [STAGING_TABLE] WHERE [BATCH_COLUMN] = '[CURRENT_BATCH]'"
        ).fetchone()[0]

        assert loaded_count == len(df), f"Load count mismatch: expected {len(df)}, got [LOADED_COUNT]"

        # Update control table
        [CONTROL_TABLE_MANAGER].update_load_status(
            source_system='[SOURCE_SYSTEM_1]',
            target_table=staging_table,
            load_date=[PROCESSING_DATE],
            record_count=loaded_count,
            status='SUCCESS'
        )

        return {
            'table': staging_table,
            'records_loaded': loaded_count,
            'load_duration': [LOAD_DURATION],
            'load_timestamp': [LOAD_TIMESTAMP]
        }

    except Exception as e:
        [CONTROL_TABLE_MANAGER].update_load_status(
            source_system='[SOURCE_SYSTEM_1]',
            target_table=staging_table,
            load_date=[PROCESSING_DATE],
            record_count=0,
            status='FAILED',
            error_message=str(e)
        )
        raise
```

### Streaming Ingestion
Real-time Source: [STREAMING_SOURCE]
```python
# Real-time ingestion from [STREAMING_SOURCE]
from [STREAMING_FRAMEWORK] import StreamingQuery
from [MESSAGE_QUEUE] import Consumer, Producer

class [STREAMING_SOURCE]Ingestion:
    def __init__(self, config: dict):
        self.config = config
        self.consumer = Consumer([CONSUMER_CONFIG])
        self.producer = Producer([PRODUCER_CONFIG])
        self.checkpoint_location = config['checkpoint_location']

    def create_streaming_pipeline(self):
        """
        Create streaming ingestion pipeline
        """
        # Source stream configuration
        source_stream = [STREAMING_FRAMEWORK].readStream \
            .format("[SOURCE_FORMAT]") \
            .option("kafka.bootstrap.servers", "[KAFKA_BROKERS]") \
            .option("subscribe", "[SOURCE_TOPICS]") \
            .option("startingOffsets", "[STARTING_OFFSET_STRATEGY]") \
            .option("maxOffsetsPerTrigger", "[MAX_OFFSETS_PER_TRIGGER]") \
            .option("failOnDataLoss", "[FAIL_ON_DATA_LOSS]") \
            .load()

        # Schema definition and parsing
        parsed_stream = source_stream.select(
            [STREAMING_FRAMEWORK].from_json(
                source_stream.value.cast("string"),
                [MESSAGE_SCHEMA]
            ).alias("data")
        ).select("data.*")

        # Real-time transformations
        enriched_stream = parsed_stream \
            .withColumn("[INGESTION_TIMESTAMP]", [CURRENT_TIMESTAMP]) \
            .withColumn("[SOURCE_PARTITION]", [PARTITION_LOGIC]) \
            .withColumn("[MESSAGE_KEY]", [KEY_GENERATION_LOGIC]) \
            .filter([FILTER_CONDITIONS]) \
            .dropDuplicates([DEDUPLICATION_COLUMNS])

        # Data quality checks
        validated_stream = self.apply_streaming_validation(enriched_stream)

        # Sink configuration
        query = validated_stream.writeStream \
            .format("[SINK_FORMAT]") \
            .outputMode("[OUTPUT_MODE]") \
            .option("checkpointLocation", self.checkpoint_location) \
            .option("path", "[SINK_PATH]") \
            .option("[SINK_SPECIFIC_OPTIONS]", "[SINK_VALUES]") \
            .trigger(processingTime='[TRIGGER_INTERVAL]') \
            .start()

        return query

    def apply_streaming_validation(self, stream):
        """
        Apply real-time data quality validation
        """
        # Null checks
        validated = stream.filter([NULL_CHECK_CONDITIONS])

        # Range validations
        validated = validated.filter([RANGE_VALIDATION_CONDITIONS])

        # Business rule validations
        validated = validated.filter([BUSINESS_RULE_CONDITIONS])

        # Add quality indicators
        validated = validated.withColumn(
            "[QUALITY_FLAG]",
            [QUALITY_FLAG_LOGIC]
        )

        return validated

# Dead letter queue handling
@task
def process_failed_messages():
    """
    Process messages that failed validation or transformation
    """
    dlq_consumer = Consumer([DLQ_CONSUMER_CONFIG])

    for message in dlq_consumer:
        try:
            # Attempt reprocessing with enhanced error handling
            [REPROCESSING_LOGIC]
        except Exception as e:
            # Log to error tracking system
            [ERROR_TRACKING].log_permanent_failure(
                message_id=message.key,
                error_details=str(e),
                retry_count=message.headers.get('retry_count', 0)
            )
```

### Change Data Capture (CDC)
CDC Pipeline: [CDC_SOURCE]
```python
# CDC pipeline for [CDC_SOURCE]
from [CDC_FRAMEWORK] import CDCProcessor

@task
def setup_cdc_pipeline(source_config: dict) -> dict:
    """
    Initialize CDC pipeline for source system

    Args:
        source_config: CDC source configuration

    Returns:
        Pipeline configuration details
    """
    cdc_processor = CDCProcessor([CDC_CONFIG])

    # Configure source connection
    source_connection = {
        'host': source_config['[SOURCE_HOST]'],
        'database': source_config['[SOURCE_DATABASE]'],
        'username': source_config['[SOURCE_USERNAME]'],
        'password': source_config['[SOURCE_PASSWORD]'],
        'port': source_config['[SOURCE_PORT]'],
        'ssl_mode': '[SSL_MODE]'
    }

    # CDC capture configuration
    capture_config = {
        'tables': [CDC_TABLE_LIST],
        'capture_mode': '[CAPTURE_MODE]',  # LOG_BASED/TRIGGER_BASED/TIMESTAMP_BASED
        'initial_snapshot': [INITIAL_SNAPSHOT_REQUIRED],
        'max_batch_size': [MAX_BATCH_SIZE],
        'poll_interval': '[POLL_INTERVAL]',
        'heartbeat_interval': '[HEARTBEAT_INTERVAL]'
    }

    # Initialize capture
    pipeline_id = cdc_processor.initialize_capture(
        source_connection,
        capture_config
    )

    return {
        'pipeline_id': pipeline_id,
        'status': 'INITIALIZED',
        'tables_monitored': len([CDC_TABLE_LIST]),
        'capture_mode': '[CAPTURE_MODE]'
    }

@task
def process_cdc_events(pipeline_id: str) -> dict:
    """
    Process CDC events and apply changes to target

    Args:
        pipeline_id: CDC pipeline identifier

    Returns:
        Processing statistics
    """
    cdc_processor = CDCProcessor.get_instance(pipeline_id)
    processing_stats = {
        'inserts': 0,
        'updates': 0,
        'deletes': 0,
        'errors': 0
    }

    try:
        # Fetch CDC events
        events = cdc_processor.fetch_events(
            max_events=[MAX_EVENTS_PER_BATCH],
            timeout=[FETCH_TIMEOUT]
        )

        # Process each event
        for event in events:
            try:
                event_type = event['[EVENT_TYPE_COLUMN]']
                table_name = event['[TABLE_NAME_COLUMN]']
                event_data = event['[EVENT_DATA_COLUMN]']

                if event_type == 'INSERT':
                    [INSERT_PROCESSING_LOGIC]
                    processing_stats['inserts'] += 1

                elif event_type == 'UPDATE':
                    [UPDATE_PROCESSING_LOGIC]
                    processing_stats['updates'] += 1

                elif event_type == 'DELETE':
                    [DELETE_PROCESSING_LOGIC]
                    processing_stats['deletes'] += 1

                # Update CDC checkpoint
                cdc_processor.update_checkpoint(event['[CHECKPOINT_COLUMN]'])

            except Exception as event_error:
                processing_stats['errors'] += 1
                [ERROR_HANDLER].handle_cdc_event_error(
                    event=event,
                    error=event_error,
                    pipeline_id=pipeline_id
                )

        return processing_stats

    except Exception as e:
        [LOGGING_FRAMEWORK].error(f"CDC processing failed: {str(e)}")
        raise
```

OUTPUT: Deliver comprehensive data ingestion solution including:
1. Source system connection configurations with secure credential management
2. Extraction logic with parameterized queries and filtering
3. Data validation framework with quality checks
4. Staging area load procedures with reconciliation
5. Real-time streaming ingestion with Kafka/event sources
6. CDC pipeline setup with change event processing
7. Error handling and retry mechanisms
8. Dead letter queue implementation for failed records
9. Extraction metadata tracking and lineage
10. Monitoring and alerting for ingestion failures
```

## Variables

### Core Configuration
[INGESTION_PATTERN], [ORGANIZATION_NAME], [SOURCE_SYSTEMS], [PROCESSING_FRAMEWORK], [ORCHESTRATION_PLATFORM], [INDUSTRY_SECTOR], [DATA_PROCESSING_DOMAIN], [INGESTION_SCOPE], [DATA_PROCESSING_OBJECTIVES], [SLA_REQUIREMENTS], [COMPLIANCE_STANDARDS]

### Architecture Settings
[PIPELINE_METHODOLOGY], [ERROR_HANDLING_PHILOSOPHY], [DATA_MOVEMENT_STRATEGY], [SECURITY_MODEL], [MONITORING_STRATEGY]

### Technical Stack
[CLOUD_PROVIDER], [STORAGE_SYSTEMS], [MESSAGE_QUEUE_SYSTEM], [CONTAINER_PLATFORM]

### Data Requirements
[TARGET_SYSTEMS], [CURRENT_DATA_VOLUME], [PROJECTED_DATA_VOLUME], [DATA_VELOCITY], [LATENCY_REQUIREMENTS], [FRESHNESS_REQUIREMENTS], [RETENTION_POLICIES]

### Batch Ingestion Variables
[SOURCE_SYSTEM_1], [SOURCE_1_SHORT], [DATABASE_CONNECTOR], [CONNECTION_PARAMETERS], [CONNECTION_DETAILS], [EXTRACTION_QUERY_TEMPLATE], [DATE_PARAMETER], [DATE_FORMAT], [FILTER_PARAMETER_1], [FILTER_VALUE_1], [FILTER_PARAMETER_2], [FILTER_VALUE_2], [CHUNK_SIZE], [READ_OPTIONS], [PRIMARY_KEY_COLUMNS], [EXTRACTION_TIMESTAMP], [SOURCE_SYSTEM_ID], [EXTRACTION_BATCH_ID], [BATCH_ID_GENERATOR], [CURRENT_TIMESTAMP]

### Validation Variables
[LOGGING_FRAMEWORK], [ALERTING_SYSTEM], [ERROR_NOTIFICATION_LIST], [COMPLETENESS_CHECK_1], [COMPLETENESS_RULE_1], [COMPLETENESS_CHECK_2], [COMPLETENESS_RULE_2], [VALIDITY_CHECK_1], [VALIDITY_RULE_1], [VALIDITY_CHECK_2], [VALIDITY_RULE_2], [CONSISTENCY_CHECK_1], [CONSISTENCY_RULE_1], [CONSISTENCY_CHECK_2], [CONSISTENCY_RULE_2], [BUSINESS_RULE_1], [BUSINESS_VALIDATION_1], [BUSINESS_RULE_2], [BUSINESS_VALIDATION_2], [VALIDATION_LOGGER], [PROCESSING_DATE], [QUALITY_CALCULATION_LOGIC], [DATA_QUALITY_SCORE]

### Staging Load Variables
[STAGING_DB_CONNECTOR], [STAGING_CONNECTION], [LOAD_STRATEGY], [STAGING_TABLE], [IF_EXISTS_STRATEGY], [LOAD_METHOD], [LOAD_CHUNK_SIZE], [BATCH_COLUMN], [CURRENT_BATCH], [CONTROL_TABLE_MANAGER], [LOAD_DURATION], [LOAD_TIMESTAMP]

### Streaming Variables
[STREAMING_SOURCE], [STREAMING_FRAMEWORK], [MESSAGE_QUEUE], [CONSUMER_CONFIG], [PRODUCER_CONFIG], [SOURCE_FORMAT], [KAFKA_BROKERS], [SOURCE_TOPICS], [STARTING_OFFSET_STRATEGY], [MAX_OFFSETS_PER_TRIGGER], [FAIL_ON_DATA_LOSS], [MESSAGE_SCHEMA], [INGESTION_TIMESTAMP], [SOURCE_PARTITION], [PARTITION_LOGIC], [MESSAGE_KEY], [KEY_GENERATION_LOGIC], [FILTER_CONDITIONS], [DEDUPLICATION_COLUMNS], [SINK_FORMAT], [OUTPUT_MODE], [SINK_PATH], [SINK_SPECIFIC_OPTIONS], [SINK_VALUES], [TRIGGER_INTERVAL]

### Streaming Validation Variables
[NULL_CHECK_CONDITIONS], [RANGE_VALIDATION_CONDITIONS], [BUSINESS_RULE_CONDITIONS], [QUALITY_FLAG], [QUALITY_FLAG_LOGIC], [DLQ_CONSUMER_CONFIG], [REPROCESSING_LOGIC], [ERROR_TRACKING]

### CDC Variables
[CDC_SOURCE], [CDC_FRAMEWORK], [CDC_CONFIG], [SOURCE_HOST], [SOURCE_DATABASE], [SOURCE_USERNAME], [SOURCE_PASSWORD], [SOURCE_PORT], [SSL_MODE], [CDC_TABLE_LIST], [CAPTURE_MODE], [INITIAL_SNAPSHOT_REQUIRED], [MAX_BATCH_SIZE], [POLL_INTERVAL], [HEARTBEAT_INTERVAL], [MAX_EVENTS_PER_BATCH], [FETCH_TIMEOUT], [EVENT_TYPE_COLUMN], [TABLE_NAME_COLUMN], [EVENT_DATA_COLUMN], [INSERT_PROCESSING_LOGIC], [UPDATE_PROCESSING_LOGIC], [DELETE_PROCESSING_LOGIC], [CHECKPOINT_COLUMN], [ERROR_HANDLER]

## Usage Examples

### Example 1: E-commerce Database Batch Ingestion
```
INGESTION_PATTERN: "Batch"
SOURCE_SYSTEM_1: "PostgreSQL Production Database"
SOURCE_1_SHORT: "prod_db"
DATABASE_CONNECTOR: "psycopg2"
EXTRACTION_QUERY_TEMPLATE: "SELECT * FROM orders WHERE order_date = '{extraction_date}'"
SCHEDULE: "0 2 * * *"  # Daily at 2 AM
CHUNK_SIZE: 10000
VALIDATION: "Check for null customer_ids, validate total amounts > 0"
```

### Example 2: Real-time Event Stream Ingestion
```
INGESTION_PATTERN: "Streaming"
STREAMING_SOURCE: "Kafka Clickstream Events"
STREAMING_FRAMEWORK: "pyspark.sql.streaming"
KAFKA_BROKERS: "kafka-broker-1:9092,kafka-broker-2:9092"
SOURCE_TOPICS: "user-events,page-views,transactions"
OUTPUT_MODE: "append"
TRIGGER_INTERVAL: "10 seconds"
CHECKPOINT_LOCATION: "s3://data-lake/checkpoints/clickstream"
```

### Example 3: CDC from MySQL to Data Warehouse
```
INGESTION_PATTERN: "CDC"
CDC_SOURCE: "MySQL Customer Database"
CDC_FRAMEWORK: "Debezium"
CAPTURE_MODE: "LOG_BASED"
CDC_TABLE_LIST: ["customers", "orders", "order_items", "products"]
POLL_INTERVAL: "1000ms"
TARGET_SYSTEM: "Snowflake Data Warehouse"
SYNC_MODE: "upsert"
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Pipeline Transformation](pipeline-transformation.md)** - Strategic framework for organizational change initiatives
- **[Pipeline Orchestration](pipeline-orchestration.md)** - Complementary approaches and methodologies
- **[Pipeline Observability](pipeline-observability.md)** - Complementary approaches and methodologies
- **[Data Governance Framework](data-governance-framework.md)** - Leverage data analysis to drive informed decisions

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Pipeline Data Ingestion Template)
2. Use [Pipeline Transformation](pipeline-transformation.md) for deeper analysis
3. Apply [Pipeline Orchestration](pipeline-orchestration.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Analytics Engineering](../../data-analytics/Analytics Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Designing batch data ingestion pipelines with validation and error handling**: Combine this template with related analytics and strategy frameworks
- **Implementing real-time streaming ingestion from message queues and event sources**: Combine this template with related analytics and strategy frameworks
- **Setting up Change Data Capture (CDC) pipelines for database synchronization**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Incremental extraction** - Use watermarks or timestamps to extract only new/changed data
2. **Idempotent operations** - Design extraction logic to handle retries safely
3. **Connection pooling** - Reuse database connections to reduce overhead
4. **Batch size optimization** - Balance memory usage and throughput
5. **Schema validation** - Verify source schema matches expectations
6. **Comprehensive logging** - Track extraction metrics and errors
7. **Graceful degradation** - Continue processing good records when some fail
8. **Secure credentials** - Use secret managers, never hardcode passwords
9. **Data profiling** - Monitor data distributions and anomalies
10. **Testing** - Validate extraction logic with sample data before production

## Tips for Success

- Start with small batch sizes and scale up after testing
- Implement extraction metadata (timestamp, batch ID, row count) for traceability
- Use parameterized queries to prevent SQL injection
- Set appropriate timeouts for external system connections
- Monitor source system load to avoid impacting production
- Implement circuit breakers for unreliable sources
- Use compression for large data transfers
- Partition large extractions by date or key ranges
- Maintain extraction control tables for restart capability
- Document source system dependencies and SLAs
