---
title: Data Ingestion & Extraction
category: data-analytics/Analytics Engineering
tags: [automation, data-analytics, development, integration, extraction]
use_cases:
  - Designing and implementing data ingestion pipelines including batch extraction, real-time streaming, API integration, and change data capture (CDC) for enterprise data platforms.
  - Building source connectors and extraction logic for diverse data sources
related_templates:
  - pipeline-development-overview.md
  - pipeline-architecture-design.md
  - data-transformation-processing.md
  - pipeline-quality-validation.md
last_updated: 2025-11-09
---

# Data Ingestion & Extraction

## Purpose
Design and implement comprehensive data ingestion strategies including batch extraction, real-time streaming, API integration, and change data capture for connecting diverse source systems to data platforms.

## Template

```
You are a data engineering specialist focusing on data ingestion and extraction. Design ingestion pipelines for [ORGANIZATION_NAME] to extract data from [SOURCE_SYSTEMS] using [INGESTION_METHODOLOGY].

INGESTION REQUIREMENTS:
- Source systems: [SOURCE_SYSTEMS]
- Ingestion pattern: [INGESTION_PATTERN] (Batch/Streaming/CDC/Hybrid)
- Data volume: [DATA_VOLUME]
- Frequency: [INGESTION_FREQUENCY]
- Latency requirements: [LATENCY_REQUIREMENTS]
- Staging location: [STAGING_LOCATION]
- Processing framework: [PROCESSING_FRAMEWORK]

Provide complete implementation for:
1. Source connection configuration and security
2. Data extraction logic with error handling
3. Initial data validation and quality checks
4. Staging layer load procedures
5. Metadata and lineage tracking
6. Monitoring and alerting setup
```

## Batch Ingestion Patterns

### Pattern 1: Database Full Extract
```python
# Full table extraction from relational database
from [ORCHESTRATION_PLATFORM] import DAG, task
from [PROCESSING_FRAMEWORK] import DataFrame
import [DATABASE_CONNECTOR]

@task
def extract_full_table(
    connection_string: str,
    table_name: str,
    extraction_date: str
) -> DataFrame:
    """
    Extract complete table from source database

    Args:
        connection_string: [CONNECTION_DETAILS]
        table_name: [TABLE_NAME]
        extraction_date: [DATE_PARAMETER]

    Returns:
        DataFrame with extracted data
    """
    try:
        # Connection setup with retry logic
        conn = [DATABASE_CONNECTOR].connect(
            [CONNECTION_PARAMETERS],
            connect_timeout=[TIMEOUT_SECONDS],
            application_name='[PIPELINE_NAME]'
        )

        # Extract query
        query = f"""
        SELECT *
        FROM {table_name}
        WHERE [OPTIONAL_FILTER_CONDITION]
        """

        # Data extraction with chunking for large tables
        df = [PROCESSING_FRAMEWORK].read_sql(
            query,
            conn,
            chunksize=[CHUNK_SIZE],
            [READ_OPTIONS]
        )

        # Initial validation
        assert len(df) > 0, f"No data extracted from {table_name}"
        assert not df.duplicated([PRIMARY_KEY_COLUMNS]).any(), "Duplicate records found"

        # Add extraction metadata
        df['extraction_timestamp'] = [CURRENT_TIMESTAMP]
        df['source_system'] = '[SOURCE_SYSTEM_ID]'
        df['extraction_batch_id'] = [BATCH_ID_GENERATOR]

        return df

    except Exception as e:
        [LOGGING_FRAMEWORK].error(f"Extraction failed: {str(e)}")
        [ALERTING_SYSTEM].send_alert(
            severity="HIGH",
            message=f"{table_name} extraction failed: {str(e)}",
            recipients=[ERROR_NOTIFICATION_LIST]
        )
        raise
    finally:
        if 'conn' in locals():
            conn.close()
```

### Pattern 2: Incremental Extraction
```python
@task
def extract_incremental_data(
    connection_string: str,
    table_name: str,
    watermark_column: str,
    last_watermark: str
) -> DataFrame:
    """
    Extract only new/modified records since last run

    Args:
        connection_string: Database connection string
        table_name: Source table name
        watermark_column: Column to track changes (timestamp/ID)
        last_watermark: Last successfully extracted watermark value

    Returns:
        DataFrame with incremental data
    """
    try:
        conn = [DATABASE_CONNECTOR].connect([CONNECTION_PARAMETERS])

        # Get current watermark first
        current_watermark = conn.execute(
            f"SELECT MAX({watermark_column}) FROM {table_name}"
        ).fetchone()[0]

        # Incremental extraction query
        query = f"""
        SELECT *
        FROM {table_name}
        WHERE {watermark_column} > '{last_watermark}'
          AND {watermark_column} <= '{current_watermark}'
        ORDER BY {watermark_column}
        """

        df = [PROCESSING_FRAMEWORK].read_sql(query, conn)

        # Update watermark if extraction successful
        if len(df) > 0:
            [WATERMARK_TRACKER].update_watermark(
                source_system='[SOURCE_SYSTEM]',
                table_name=table_name,
                watermark_column=watermark_column,
                watermark_value=current_watermark
            )

        # Add metadata
        df['extraction_type'] = 'INCREMENTAL'
        df['watermark_start'] = last_watermark
        df['watermark_end'] = current_watermark

        return df

    except Exception as e:
        [ERROR_HANDLER].handle_extraction_error(
            source=table_name,
            error=e,
            watermark=last_watermark
        )
        raise
```

### Pattern 3: API Data Extraction
```python
@task
def extract_api_data(
    api_endpoint: str,
    api_key: str,
    extraction_params: dict
) -> DataFrame:
    """
    Extract data from REST API with pagination

    Args:
        api_endpoint: API base URL
        api_key: Authentication key
        extraction_params: Query parameters

    Returns:
        DataFrame with API response data
    """
    import requests
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    # Configure retry strategy
    retry_strategy = Retry(
        total=[MAX_RETRIES],
        backoff_factor=[BACKOFF_FACTOR],
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    all_records = []
    page = 1

    try:
        while True:
            # API request with headers
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }

            params = {
                **extraction_params,
                'page': page,
                'limit': [PAGE_SIZE]
            }

            response = session.get(
                api_endpoint,
                headers=headers,
                params=params,
                timeout=[REQUEST_TIMEOUT]
            )

            response.raise_for_status()
            data = response.json()

            # Extract records from response
            records = data.get('[RECORDS_KEY]', [])
            if not records:
                break

            all_records.extend(records)

            # Check pagination
            if not data.get('[HAS_MORE_KEY]', False):
                break

            page += 1

            # Rate limiting
            time.sleep([RATE_LIMIT_DELAY])

        # Convert to DataFrame
        df = [PROCESSING_FRAMEWORK].DataFrame(all_records)

        # Add metadata
        df['api_extraction_timestamp'] = [CURRENT_TIMESTAMP]
        df['api_endpoint'] = api_endpoint

        return df

    except requests.exceptions.RequestException as e:
        [ERROR_HANDLER].handle_api_error(
            endpoint=api_endpoint,
            error=e,
            params=extraction_params
        )
        raise
```

## Streaming Ingestion Patterns

### Pattern 1: Kafka Stream Ingestion
```python
# Real-time ingestion from Kafka topics
from [STREAMING_FRAMEWORK] import StreamingQuery
from [MESSAGE_QUEUE] import Consumer, Producer

class KafkaStreamIngestion:
    def __init__(self, config: dict):
        self.config = config
        self.consumer = Consumer([CONSUMER_CONFIG])
        self.checkpoint_location = config['checkpoint_location']

    def create_streaming_pipeline(self):
        """
        Create Kafka streaming ingestion pipeline
        """
        # Source stream configuration
        source_stream = [STREAMING_FRAMEWORK].readStream \
            .format("kafka") \
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
            .withColumn("ingestion_timestamp", [CURRENT_TIMESTAMP]) \
            .withColumn("source_partition", [PARTITION_LOGIC]) \
            .withColumn("message_key", [KEY_GENERATION_LOGIC]) \
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
            "quality_flag",
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

## Change Data Capture (CDC) Patterns

### Pattern 1: Log-based CDC
```python
# CDC pipeline for capturing database changes
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
        'host': source_config['host'],
        'database': source_config['database'],
        'username': source_config['username'],
        'password': source_config['password'],
        'port': source_config['port'],
        'ssl_mode': '[SSL_MODE]'
    }

    # CDC capture configuration
    capture_config = {
        'tables': [CDC_TABLE_LIST],
        'capture_mode': 'LOG_BASED',  # LOG_BASED/TRIGGER_BASED/TIMESTAMP_BASED
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
        'capture_mode': 'LOG_BASED'
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
                event_type = event['event_type']
                table_name = event['table_name']
                event_data = event['event_data']

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
                cdc_processor.update_checkpoint(event['checkpoint_position'])

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

### Pattern 2: Staging Layer Load
```python
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
            staging_conn.execute(f"TRUNCATE TABLE {staging_table}")

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
            f"SELECT COUNT(*) FROM {staging_table} WHERE batch_id = '[CURRENT_BATCH]'"
        ).fetchone()[0]

        assert loaded_count == len(df), f"Load count mismatch: expected {len(df)}, got {loaded_count}"

        # Update control table
        [CONTROL_TABLE_MANAGER].update_load_status(
            source_system='[SOURCE_SYSTEM]',
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
            source_system='[SOURCE_SYSTEM]',
            target_table=staging_table,
            load_date=[PROCESSING_DATE],
            record_count=0,
            status='FAILED',
            error_message=str(e)
        )
        raise
```

## Variables
[ORGANIZATION_NAME], [SOURCE_SYSTEMS], [INGESTION_METHODOLOGY], [INGESTION_PATTERN], [DATA_VOLUME], [INGESTION_FREQUENCY], [LATENCY_REQUIREMENTS], [STAGING_LOCATION], [PROCESSING_FRAMEWORK], [ORCHESTRATION_PLATFORM], [DATABASE_CONNECTOR], [CONNECTION_PARAMETERS], [TIMEOUT_SECONDS], [PIPELINE_NAME], [CHUNK_SIZE], [READ_OPTIONS], [PRIMARY_KEY_COLUMNS], [CURRENT_TIMESTAMP], [SOURCE_SYSTEM_ID], [BATCH_ID_GENERATOR], [LOGGING_FRAMEWORK], [ALERTING_SYSTEM], [ERROR_NOTIFICATION_LIST], [WATERMARK_TRACKER], [ERROR_HANDLER], [MAX_RETRIES], [BACKOFF_FACTOR], [PAGE_SIZE], [REQUEST_TIMEOUT], [RECORDS_KEY], [HAS_MORE_KEY], [RATE_LIMIT_DELAY], [STREAMING_FRAMEWORK], [MESSAGE_QUEUE], [CONSUMER_CONFIG], [KAFKA_BROKERS], [SOURCE_TOPICS], [STARTING_OFFSET_STRATEGY], [MAX_OFFSETS_PER_TRIGGER], [FAIL_ON_DATA_LOSS], [MESSAGE_SCHEMA], [PARTITION_LOGIC], [KEY_GENERATION_LOGIC], [FILTER_CONDITIONS], [DEDUPLICATION_COLUMNS], [SINK_FORMAT], [OUTPUT_MODE], [SINK_PATH], [TRIGGER_INTERVAL], [NULL_CHECK_CONDITIONS], [RANGE_VALIDATION_CONDITIONS], [BUSINESS_RULE_CONDITIONS], [QUALITY_FLAG_LOGIC], [DLQ_CONSUMER_CONFIG], [REPROCESSING_LOGIC], [ERROR_TRACKING], [CDC_FRAMEWORK], [CDC_CONFIG], [SSL_MODE], [CDC_TABLE_LIST], [INITIAL_SNAPSHOT_REQUIRED], [MAX_BATCH_SIZE], [POLL_INTERVAL], [HEARTBEAT_INTERVAL], [MAX_EVENTS_PER_BATCH], [FETCH_TIMEOUT], [INSERT_PROCESSING_LOGIC], [UPDATE_PROCESSING_LOGIC], [DELETE_PROCESSING_LOGIC], [STAGING_DB_CONNECTOR], [STAGING_CONNECTION], [LOAD_STRATEGY], [IF_EXISTS_STRATEGY], [LOAD_METHOD], [LOAD_CHUNK_SIZE], [CURRENT_BATCH], [CONTROL_TABLE_MANAGER], [PROCESSING_DATE], [LOAD_DURATION], [LOAD_TIMESTAMP]

## Best Practices

1. **Use incremental loads** - Extract only changed data when possible
2. **Implement watermarking** - Track extraction progress for resumability
3. **Add extraction metadata** - Always include timestamps and batch IDs
4. **Handle API rate limits** - Implement backoff and retry strategies
5. **Validate at ingestion** - Catch data quality issues early
6. **Use connection pooling** - Reuse database connections for efficiency
7. **Implement circuit breakers** - Prevent cascade failures
8. **Log extraction metrics** - Track volume, duration, and failures
9. **Secure credentials** - Use secret management systems
10. **Test failure scenarios** - Ensure graceful degradation
