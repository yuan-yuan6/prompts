---
title: Data Transformation Pipelines Template
category: data-analytics/Analytics Engineering
tags: ['data-engineering', 'etl', 'transformation', 'data-quality']
use_cases:
  - Design data transformation pipelines using bronze-silver-gold architecture, data quality checks, and business logic implementation.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Data Transformation Pipelines Template

## Purpose
Design data transformation pipelines using bronze-silver-gold architecture, data quality checks, and business logic implementation.

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
- Design data transformation pipelines using bronze-silver-gold architecture, data quality checks, and business logic implementation.
- Project-specific implementations
- Research and analysis workflows



## Template

### Returns
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

TRANSFORMATION LAYER DESIGN:

Data Transformation Framework:

Core Transformation Pipeline:
```python

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


### Args
            source_table: Bronze layer source table
            target_table: Silver layer target table
            transformation_date: Processing date


### Returns
            Transformation statistics
        """
        try:
            # Load source data
            source_df = self.engine.read_table(
                table_name=source_table,
                filters={
                    '[DATE_COLUMN]': transformation_date,
                    '[QUALITY_FILTER]': [QUALITY_THRESHOLD]
                }
            )

            # Data cleaning transformations
            cleaned_df = source_df.transform([CLEANING_TRANSFORMATIONS])

            # Apply cleansing rules
            cleaned_df = self.apply_cleansing_rules(cleaned_df)

            # Standardization
            standardized_df = self.apply_standardization(cleaned_df)

            # Validation
            validated_df = self.apply_silver_validation(standardized_df)

            # Enrichment
            enriched_df = self.apply_enrichment(validated_df)

            # Write to silver layer
            write_stats = self.engine.write_table(
                df=enriched_df,
                table_name=target_table,
                mode='[WRITE_MODE]',
                partition_by=[PARTITION_COLUMNS]
            )

            # Track lineage
            self.lineage_tracker.record_transformation(
                source_table=source_table,
                target_table=target_table,
                transformation_type='BRONZE_TO_SILVER',
                transformation_date=transformation_date,
                record_count=len(enriched_df),
                transformations_applied=[TRANSFORMATION_LIST]
            )

            return write_stats

        except Exception as e:
            [ERROR_HANDLER].handle_transformation_error(
                source_table=source_table,
                target_table=target_table,
                error=e,
                processing_date=transformation_date
            )
            raise

    def apply_cleansing_rules(self, df):
        """Apply data cleansing rules"""
        # Null handling
        df = df.fillna({
            '[COLUMN_1]': '[DEFAULT_VALUE_1]',
            '[COLUMN_2]': '[DEFAULT_VALUE_2]',
            '[COLUMN_3]': '[DEFAULT_VALUE_3]'
        })

        # Data type conversions
        df = df.astype({
            '[COLUMN_4]': '[TARGET_TYPE_1]',
            '[COLUMN_5]': '[TARGET_TYPE_2]',
            '[COLUMN_6]': '[TARGET_TYPE_3]'
        })

        # Format standardization
        df['[PHONE_COLUMN]'] = df['[PHONE_COLUMN]'].apply([PHONE_STANDARDIZER])
        df['[EMAIL_COLUMN]'] = df['[EMAIL_COLUMN]'].str.lower().str.strip()
        df['[DATE_COLUMN]'] = [PROCESSING_FRAMEWORK].to_datetime(df['[DATE_COLUMN]'])

        # Outlier handling
        df = self.handle_outliers(df, [OUTLIER_COLUMNS])

        return df

    def apply_standardization(self, df):
        """Apply standardization rules"""
        # Reference data lookups
        df = df.merge(
            [REFERENCE_DATA_1],
            left_on='[LOOKUP_COLUMN_1]',
            right_on='[REFERENCE_KEY_1]',
            how='left'
        )

        # Code mappings
        df['[MAPPED_COLUMN]'] = df['[SOURCE_COLUMN]'].map([CODE_MAPPING_DICT])

        # Business rule applications
        df['[CALCULATED_COLUMN_1]'] = [CALCULATION_LOGIC_1]
        df['[CALCULATED_COLUMN_2]'] = [CALCULATION_LOGIC_2]

        # Hierarchy resolution
        df = self.resolve_hierarchies(df, [HIERARCHY_COLUMNS])

        return df

    def apply_enrichment(self, df):
        """Apply data enrichment"""
        # External API enrichment
        if [EXTERNAL_ENRICHMENT_ENABLED]:
            df = self.enrich_from_external_api(df, [API_CONFIG])

        # ML model predictions
        if [ML_ENRICHMENT_ENABLED]:
            df = self.apply_ml_enrichment(df, [ML_MODEL_CONFIG])

        # Geospatial enrichment
        if [GEOSPATIAL_ENRICHMENT_ENABLED]:
            df = self.enrich_geospatial_data(df, [GEO_CONFIG])

        return df

    @task
    def silver_to_gold_transformation(
        self,
        source_tables: list,
        target_table: str,
        transformation_date: str
    ) -> dict:
        """
        Transform silver data to gold layer (business ready)


### Args
            source_tables: List of silver layer source tables
            target_table: Gold layer target table
            transformation_date: Processing date


### Returns
            Transformation statistics
        """
        try:
            # Multi-table join logic
            joined_df = self.perform_multi_table_join(
                tables=source_tables,
                join_logic=[JOIN_CONFIGURATION],
                processing_date=transformation_date
            )

            # Business logic application
            business_df = self.apply_business_logic(joined_df)

            # Aggregation logic
            if [AGGREGATION_REQUIRED]:
                aggregated_df = self.apply_aggregations(business_df)
                final_df = aggregated_df
            else:
                final_df = business_df

            # Dimensional modeling transformations
            if [DIMENSIONAL_MODEL_ENABLED]:
                final_df = self.apply_dimensional_transformations(final_df)

            # Final validation
            validated_df = self.apply_gold_validation(final_df)

            # Write to gold layer
            write_stats = self.engine.write_table(
                df=validated_df,
                table_name=target_table,
                mode='[GOLD_WRITE_MODE]',
                partition_by=[GOLD_PARTITION_COLUMNS],
                optimize=[OPTIMIZATION_STRATEGY]
            )

            # Update metadata
            self.update_table_metadata(
                table_name=target_table,
                processing_date=transformation_date,
                record_count=len(validated_df),
                transformation_stats=write_stats
            )

            return write_stats

        except Exception as e:
            [ERROR_HANDLER].handle_gold_transformation_error(
                source_tables=source_tables,
                target_table=target_table,
                error=e,
                processing_date=transformation_date
            )
            raise

    def apply_business_logic(self, df):
        """Apply business-specific transformation logic"""
        # KPI calculations
        df['[KPI_1]'] = [KPI_1_CALCULATION]
        df['[KPI_2]'] = [KPI_2_CALCULATION]
        df['[KPI_3]'] = [KPI_3_CALCULATION]

        # Business categorizations
        df['[CATEGORY_COLUMN]'] = df.apply([CATEGORIZATION_LOGIC], axis=1)

        # Time-based calculations
        df['[TIME_PERIOD]'] = [TIME_PERIOD_LOGIC]
        df['[FISCAL_PERIOD]'] = [FISCAL_PERIOD_LOGIC]

        # Ranking and scoring
        df['[RANK_COLUMN]'] = df['[SCORE_COLUMN]'].rank(
            method='[RANK_METHOD]',
            ascending=[RANK_ASCENDING]
        )

        return df

Complex Transformation Logic:
```python

# Advanced transformation patterns
class AdvancedTransformations:

    @staticmethod
    def slowly_changing_dimension_type_2(
        current_df,
        new_df,
        business_key: str,
        scd_columns: list
    ):
        """
        Implement SCD Type 2 logic for dimension updates
        """
        # Identify changed records
        changed_records = new_df.merge(
            current_df,
            on=business_key,
            how='inner',
            suffixes=('_new', '_current')
        )

        # Detect changes in SCD columns
        change_detected = False
        for col in scd_columns:
            change_detected |= (
                changed_records[f'[COL]_new'] != changed_records[f'[COL]_current']
            )

        # Expire current versions
        expire_updates = changed_records[change_detected].copy()
        expire_updates['[EXPIRATION_DATE]'] = [CURRENT_DATE]
        expire_updates['[IS_CURRENT]'] = False

        # Create new versions
        new_versions = new_df[new_df[business_key].isin(
            expire_updates[business_key]
        )].copy()
        new_versions['[EFFECTIVE_DATE]'] = [CURRENT_DATE]
        new_versions['[EXPIRATION_DATE]'] = [HIGH_DATE]
        new_versions['[IS_CURRENT]'] = True
        new_versions['[VERSION_NUMBER]'] = [NEW_VERSION_LOGIC]

        # Combine results
        result_df = [CONCATENATION_LOGIC]

        return result_df

    @staticmethod
    def window_function_analytics(df, partition_cols: list, order_cols: list):
        """
        Apply advanced window function analytics
        """
        from [PROCESSING_FRAMEWORK].sql import functions as F
        from [PROCESSING_FRAMEWORK].sql.window import Window

        # Define window specifications
        window_spec = Window.partitionBy(partition_cols).orderBy(order_cols)

        # Running totals
        df = df.withColumn(
            '[RUNNING_TOTAL]',
            F.sum('[AMOUNT_COLUMN]').over(window_spec)
        )

        # Moving averages
        moving_window = window_spec.rowsBetween(-[WINDOW_SIZE], 0)
        df = df.withColumn(
            '[MOVING_AVERAGE]',
            F.avg('[VALUE_COLUMN]').over(moving_window)
        )

        # Lag/Lead calculations
        df = df.withColumn(
            '[PREVIOUS_VALUE]',
            F.lag('[VALUE_COLUMN]', [LAG_PERIODS]).over(window_spec)
        )

        # Rank calculations
        df = df.withColumn(
            '[RANK]',
            F.row_number().over(window_spec)
        )

        # Percentile calculations
        df = df.withColumn(
            '[PERCENTILE_RANK]',
            F.percent_rank().over(window_spec)
        )

        return df

    @staticmethod
    def data_deduplication_strategy(df, dedup_columns: list, ranking_column: str):
        """
        Advanced deduplication with ranking
        """
        from [PROCESSING_FRAMEWORK].sql import functions as F
        from [PROCESSING_FRAMEWORK].sql.window import Window

        # Define deduplication window
        dedup_window = Window.partitionBy(dedup_columns).orderBy(
            F.desc(ranking_column)
        )

        # Add row number for deduplication
        df_with_rank = df.withColumn(
            'dedup_rank',
            F.row_number().over(dedup_window)
        )

        # Keep only the first (highest ranked) record
        deduplicated_df = df_with_rank.filter(F.col('dedup_rank') == 1).drop('dedup_rank')

        return deduplicated_df

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


# Task dependencies
[SOURCE_1_TASK] >> validate_[SOURCE_1_SHORT]
[SOURCE_2_TASK] >> validate_[SOURCE_2_SHORT]

[validate_[SOURCE_1_SHORT], validate_[SOURCE_2_SHORT]] >> bronze_to_silver
bronze_to_silver >> silver_to_gold
silver_to_gold >> data_quality_check

data_quality_check >> success_notification
[SOURCE_1_TASK, SOURCE_2_TASK, bronze_to_silver, silver_to_gold, data_quality_check] >> failure_notification

# Comprehensive monitoring system
from [MONITORING_FRAMEWORK] import MetricsCollector, AlertManager

class PipelineMonitor:
    def __init__(self, config: dict):
        self.metrics_collector = MetricsCollector([METRICS_CONFIG])
        self.alert_manager = AlertManager([ALERT_CONFIG])
        self.thresholds = config['thresholds']

    def monitor_pipeline_execution(self, pipeline_id: str, execution_context: dict):
        """
        Monitor pipeline execution metrics
        """
        # Collect execution metrics
        execution_metrics = {
            'pipeline_id': pipeline_id,
            'start_time': execution_context['start_time'],
            'end_time': execution_context.get('end_time'),
            'duration': execution_context.get('duration'),
            'status': execution_context['status'],
            'records_processed': execution_context.get('records_processed', 0),
            'records_failed': execution_context.get('records_failed', 0),
            'data_volume_gb': execution_context.get('data_volume_gb', 0),
            'cpu_usage_avg': execution_context.get('cpu_usage_avg', 0),
            'memory_usage_max': execution_context.get('memory_usage_max', 0),
            'error_count': execution_context.get('error_count', 0)
        }

        # Send metrics to monitoring system
        self.metrics_collector.send_metrics(
            metric_type='PIPELINE_EXECUTION',
            metrics=execution_metrics,
            timestamp=execution_context['end_time']
        )

        # Check SLA compliance
        self.check_sla_compliance(execution_metrics)

        # Check data quality thresholds
        self.check_data_quality_thresholds(execution_metrics)

        # Resource utilization monitoring
        self.monitor_resource_utilization(execution_metrics)

    def check_sla_compliance(self, metrics: dict):
        """
        Check if pipeline execution meets SLA requirements
        """
        pipeline_id = metrics['pipeline_id']
        duration = metrics.get('duration', 0)
        sla_threshold = self.thresholds.get(f'[PIPELINE_ID]_sla_minutes', [DEFAULT_SLA_MINUTES])

        if duration > sla_threshold * 60:  # Convert minutes to seconds
            self.alert_manager.send_alert(
                alert_type='SLA_BREACH',
                severity='HIGH',
                message=f'Pipeline [PIPELINE_ID] exceeded SLA: {duration/60:.2f} minutes > [SLA_THRESHOLD] minutes',
                pipeline_id=pipeline_id,
                metadata={'duration': duration, 'sla_threshold': sla_threshold}
            )

    def check_data_quality_thresholds(self, metrics: dict):
        """
        Monitor data quality metrics against thresholds
        """
        pipeline_id = metrics['pipeline_id']
        records_processed = metrics.get('records_processed', 0)
        records_failed = metrics.get('records_failed', 0)

        if records_processed > 0:
            failure_rate = records_failed / records_processed
            failure_threshold = self.thresholds.get(f'[PIPELINE_ID]_failure_rate', [DEFAULT_FAILURE_RATE])

            if failure_rate > failure_threshold:
                self.alert_manager.send_alert(
                    alert_type='DATA_QUALITY_BREACH',
                    severity='MEDIUM',
                    message=f'Pipeline [PIPELINE_ID] data quality threshold breached: {failure_rate:.2%} > {failure_threshold:.2%}',
                    pipeline_id=pipeline_id,
                    metadata={'failure_rate': failure_rate, 'threshold': failure_threshold}
                )

    def create_monitoring_dashboard(self):
        """
        Create monitoring dashboard configuration
        """
        dashboard_config = {
            'dashboard_name': '[PIPELINE_DASHBOARD_NAME]',
            'panels': [
                {
                    'panel_name': 'Pipeline Execution Status',
                    'panel_type': 'status_grid',
                    'metrics': ['pipeline_status', 'execution_count', 'failure_rate'],
                    'refresh_interval': '[STATUS_REFRESH_INTERVAL]'
                },
                {
                    'panel_name': 'Execution Duration Trends',
                    'panel_type': 'time_series',
                    'metrics': ['avg_duration', 'max_duration', 'sla_threshold'],
                    'time_range': '[DURATION_TIME_RANGE]'
                },
                {
                    'panel_name': 'Data Volume Processed',
                    'panel_type': 'bar_chart',
                    'metrics': ['records_processed', 'data_volume_gb'],
                    'grouping': '[VOLUME_GROUPING]'
                },
                {
                    'panel_name': 'Resource Utilization',
                    'panel_type': 'gauge',
                    'metrics': ['cpu_usage', 'memory_usage', 'disk_io'],
                    'thresholds': self.thresholds['resource_utilization']
                },
                {
                    'panel_name': 'Error Analysis',
                    'panel_type': 'table',
                    'metrics': ['error_type', 'error_count', 'error_trend'],
                    'filters': ['severity', 'time_range']
                }
            ],
            'alerts': [
                {
                    'alert_name': 'Pipeline Failure',
                    'condition': "status == 'FAILED'",
                    'severity': 'CRITICAL',
                    'notification_channels': ['[CRITICAL_NOTIFICATION_CHANNEL]']
                },
                {
                    'alert_name': 'SLA Breach',
                    'condition': 'duration > sla_threshold',
                    'severity': 'HIGH',
                    'notification_channels': ['[HIGH_NOTIFICATION_CHANNEL]']
                },
                {
                    'alert_name': 'Data Quality Issue',
                    'condition': 'failure_rate > threshold',
                    'severity': 'MEDIUM',
                    'notification_channels': ['[MEDIUM_NOTIFICATION_CHANNEL]']
                }
            ]
        }

        return dashboard_config


### Returns
            Recovery action results
        """
        error_id = self.generate_error_id()

        # Log error details
        error_details = {
            'error_id': error_id,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'severity': severity.value,
            'pipeline_id': context.get('pipeline_id'),
            'task_id': context.get('task_id'),
            'execution_date': context.get('execution_date'),
            'retry_count': context.get('retry_count', 0),
            'stack_trace': [STACK_TRACE_EXTRACTION],
            'system_context': self.gather_system_context(),
            'data_context': context.get('data_context', {}),
            'timestamp': [CURRENT_TIMESTAMP]
        }

        # Store error for analysis
        self.error_store.store_error(error_details)

        # Log error
        self.logger.error(f"Pipeline error [ERROR_ID]: [ERROR_DETAILS]")

        # Determine recovery strategy
        recovery_strategy = self.determine_recovery_strategy(error_details)

        # Execute recovery actions
        recovery_result = self.execute_recovery_strategy(
            recovery_strategy,
            error_details,
            context
        )

        # Send notifications based on severity
        self.send_error_notifications(error_details, recovery_result)

        return {
            'error_id': error_id,
            'recovery_strategy': recovery_strategy,
            'recovery_result': recovery_result,
            'next_action': self.determine_next_action(recovery_result)
        }

    def determine_recovery_strategy(self, error_details: dict) -> str:
        """
        Determine appropriate recovery strategy based on error type
        """
        error_type = error_details['error_type']
        pipeline_id = error_details['pipeline_id']
        retry_count = error_details['retry_count']

        # Connection errors
        if error_type in ['ConnectionError', 'TimeoutError', 'DatabaseError']:
            if retry_count < [MAX_CONNECTION_RETRIES]:
                return 'EXPONENTIAL_BACKOFF_RETRY'
            else:
                return 'DEAD_LETTER_QUEUE'

        # Data quality errors
        elif error_type in ['ValidationError', 'DataQualityError']:
            return 'QUARANTINE_AND_CONTINUE'

        # Resource errors
        elif error_type in ['MemoryError', 'DiskSpaceError']:
            return 'REDUCE_BATCH_SIZE_AND_RETRY'

        # Schema errors
        elif error_type in ['SchemaError', 'ColumnNotFoundError']:
            return 'SCHEMA_EVOLUTION_HANDLER'

        # Business logic errors
        elif error_type in ['BusinessRuleError', 'CalculationError']:
            return 'MANUAL_INTERVENTION_REQUIRED'

        # Default strategy
        else:
            return 'STANDARD_RETRY'

    def execute_recovery_strategy(
        self,
        strategy: str,
        error_details: dict,
        context: dict
    ) -> dict:
        """
        Execute the determined recovery strategy
        """
        recovery_result = {
            'strategy_executed': strategy,
            'success': False,
            'actions_taken': [],
            'next_retry_time': None
        }

        try:
            if strategy == 'EXPONENTIAL_BACKOFF_RETRY':
                retry_delay = self.calculate_exponential_backoff(
                    error_details['retry_count']
                )
                recovery_result['next_retry_time'] = [CURRENT_TIME] + retry_delay
                recovery_result['actions_taken'].append(f'Scheduled retry in [RETRY_DELAY] seconds')
                recovery_result['success'] = True

            elif strategy == 'QUARANTINE_AND_CONTINUE':
                quarantine_result = self.quarantine_bad_data(
                    error_details,
                    context
                )
                recovery_result['actions_taken'].append('Quarantined bad data')
                recovery_result['actions_taken'].append('Continuing with good data')
                recovery_result['success'] = quarantine_result['success']

            elif strategy == 'REDUCE_BATCH_SIZE_AND_RETRY':
                new_batch_size = self.calculate_reduced_batch_size(
                    context.get('current_batch_size', [DEFAULT_BATCH_SIZE])
                )
                recovery_result['actions_taken'].append(f'Reduced batch size to [NEW_BATCH_SIZE]')
                recovery_result['success'] = True

            elif strategy == 'DEAD_LETTER_QUEUE':
                dlq_result = self.send_to_dead_letter_queue(error_details, context)
                recovery_result['actions_taken'].append('Sent to dead letter queue')
                recovery_result['success'] = dlq_result['success']

            elif strategy == 'SCHEMA_EVOLUTION_HANDLER':
                evolution_result = self.handle_schema_evolution(error_details, context)
                recovery_result['actions_taken'] = evolution_result['actions']
                recovery_result['success'] = evolution_result['success']

            elif strategy == 'MANUAL_INTERVENTION_REQUIRED':
                intervention_result = self.request_manual_intervention(error_details, context)
                recovery_result['actions_taken'].append('Manual intervention requested')
                recovery_result['success'] = intervention_result['ticket_created']

        except Exception as recovery_error:
            recovery_result['recovery_error'] = str(recovery_error)
            self.logger.error(f"Recovery strategy [STRATEGY] failed: [RECOVERY_ERROR]")

        return recovery_result

    def quarantine_bad_data(self, error_details: dict, context: dict) -> dict:
        """
        Quarantine problematic data for later analysis
        """
        try:
            quarantine_table = f"{[QUARANTINE_SCHEMA]}.{context['table_name']}_quarantine"

            # Move bad records to quarantine
            quarantine_query = f"""
            INSERT INTO [QUARANTINE_TABLE]
            SELECT *,
                   '{error_details['error_id']}' as error_id,
                   '{error_details['error_message']}' as error_reason,
                   CURRENT_TIMESTAMP as quarantine_timestamp
            FROM {context['source_table']}
            WHERE {context['error_filter_condition']}
            """

            [DATABASE_EXECUTOR].execute(quarantine_query)

            # Remove bad records from processing
            cleanup_query = f"""
            DELETE FROM {context['source_table']}

[Content truncated for length - see original for full details]


## Variables

[PIPELINE_METHODOLOGY], [ORGANIZATION_NAME], [DATA_PROCESSING_OBJECTIVES], [ORCHESTRATION_PLATFORM], [PROCESSING_FRAMEWORK], [INDUSTRY_SECTOR], [DATA_PROCESSING_DOMAIN], [PIPELINE_SCOPE], [SLA_REQUIREMENTS], [COMPLIANCE_STANDARDS], [BUDGET_CONSTRAINTS], [PROJECT_TIMELINE], [PIPELINE_PATTERN], [ORCHESTRATION_APPROACH], [DATA_MOVEMENT_STRATEGY], [ERROR_HANDLING_PHILOSOPHY], [SCALABILITY_APPROACH], [SECURITY_MODEL], [MONITORING_STRATEGY], [CLOUD_PROVIDER], [COMPUTE_PLATFORM], [STORAGE_SYSTEMS], [MESSAGE_QUEUE_SYSTEM], [WORKFLOW_ENGINE], [CONTAINER_PLATFORM], [IAC_TOOL], [SOURCE_SYSTEMS], [TARGET_SYSTEMS], [CURRENT_DATA_VOLUME], [PROJECTED_DATA_VOLUME], [DATA_VELOCITY], [DATA_VARIETY], [LATENCY_REQUIREMENTS], [FRESHNESS_REQUIREMENTS], [RETENTION_POLICIES], [SOURCE_SYSTEM_1], [CONNECTION_DETAILS], [EXTRACTION_QUERY_TEMPLATE], [DATE_PARAMETER], [DATABASE_CONNECTOR], [CONNECTION_PARAMETERS], [DATE_FORMAT], [FILTER_PARAMETER_1], [FILTER_VALUE_1], [FILTER_PARAMETER_2], [FILTER_VALUE_2], [CHUNK_SIZE], [READ_OPTIONS], [PRIMARY_KEY_COLUMNS], [EXTRACTION_TIMESTAMP], [SOURCE_SYSTEM_ID], [EXTRACTION_BATCH_ID], [BATCH_ID_GENERATOR], [CURRENT_TIMESTAMP], [LOGGING_FRAMEWORK], [ALERTING_SYSTEM], [ERROR_NOTIFICATION_LIST], [COMPLETENESS_RULE_1], [COMPLETENESS_CHECK_1], [COMPLETENESS_RULE_2], [COMPLETENESS_CHECK_2], [VALIDITY_CHECK_1], [VALIDITY_RULE_1], [VALIDITY_CHECK_2], [VALIDITY_RULE_2], [CONSISTENCY_CHECK_1], [CONSISTENCY_RULE_1], [CONSISTENCY_CHECK_2], [CONSISTENCY_RULE_2], [BUSINESS_RULE_1], [BUSINESS_VALIDATION_1], [BUSINESS_RULE_2], [BUSINESS_VALIDATION_2], [VALIDATION_LOGGER], [PROCESSING_DATE], [QUALITY_CALCULATION_LOGIC], [DATA_QUALITY_SCORE], [STAGING_DB_CONNECTOR], [STAGING_CONNECTION], [LOAD_STRATEGY], [IF_EXISTS_STRATEGY], [LOAD_METHOD], [LOAD_CHUNK_SIZE], [BATCH_COLUMN], [CURRENT_BATCH], [CONTROL_TABLE_MANAGER], [LOAD_DURATION], [LOAD_TIMESTAMP], [STREAMING_SOURCE], [STREAMING_FRAMEWORK], [MESSAGE_QUEUE], [CONSUMER_CONFIG], [PRODUCER_CONFIG], [SOURCE_FORMAT], [KAFKA_BROKERS], [SOURCE_TOPICS], [STARTING_OFFSET_STRATEGY], [MAX_OFFSETS_PER_TRIGGER], [FAIL_ON_DATA_LOSS], [MESSAGE_SCHEMA], [INGESTION_TIMESTAMP], [SOURCE_PARTITION], [PARTITION_LOGIC], [MESSAGE_KEY], [KEY_GENERATION_LOGIC], [FILTER_CONDITIONS], [DEDUPLICATION_COLUMNS], [SINK_FORMAT], [OUTPUT_MODE], [SINK_PATH], [SINK_SPECIFIC_OPTIONS], [SINK_VALUES], [TRIGGER_INTERVAL], [NULL_CHECK_CONDITIONS], [RANGE_VALIDATION_CONDITIONS], [BUSINESS_RULE_CONDITIONS], [QUALITY_FLAG], [QUALITY_FLAG_LOGIC], [DLQ_CONSUMER_CONFIG], [REPROCESSING_LOGIC], [ERROR_TRACKING], [CDC_SOURCE], [CDC_FRAMEWORK], [CDC_CONFIG], [SOURCE_HOST], [SOURCE_DATABASE], [SOURCE_USERNAME], [SOURCE_PASSWORD], [SOURCE_PORT], [SSL_MODE], [CDC_TABLE_LIST], [CAPTURE_MODE], [INITIAL_SNAPSHOT_REQUIRED], [MAX_BATCH_SIZE], [POLL_INTERVAL], [HEARTBEAT_INTERVAL], [MAX_EVENTS_PER_BATCH], [FETCH_TIMEOUT], [EVENT_TYPE_COLUMN], [TABLE_NAME_COLUMN], [EVENT_DATA_COLUMN], [INSERT_PROCESSING_LOGIC], [UPDATE_PROCESSING_LOGIC], [DELETE_PROCESSING_LOGIC], [CHECKPOINT_COLUMN], [ERROR_HANDLER], [TRANSFORMATION_FRAMEWORK], [ENGINE_CONFIG], [LINEAGE_TRACKER], [LINEAGE_CONFIG], [DATE_COLUMN], [QUALITY_FILTER], [QUALITY_THRESHOLD], [CLEANING_TRANSFORMATIONS], [WRITE_MODE], [PARTITION_COLUMNS], [TRANSFORMATION_LIST], [COLUMN_1], [DEFAULT_VALUE_1], [COLUMN_2], [DEFAULT_VALUE_2], [COLUMN_3], [DEFAULT_VALUE_3], [COLUMN_4], [TARGET_TYPE_1], [COLUMN_5], [TARGET_TYPE_2], [COLUMN_6], [TARGET_TYPE_3], [PHONE_COLUMN], [PHONE_STANDARDIZER], [EMAIL_COLUMN], [OUTLIER_COLUMNS], [REFERENCE_DATA_1], [LOOKUP_COLUMN_1], [REFERENCE_KEY_1], [MAPPED_COLUMN], [SOURCE_COLUMN], [CODE_MAPPING_DICT], [CALCULATED_COLUMN_1], [CALCULATION_LOGIC_1], [CALCULATED_COLUMN_2], [CALCULATION_LOGIC_2], [HIERARCHY_COLUMNS], [EXTERNAL_ENRICHMENT_ENABLED], [API_CONFIG], [ML_ENRICHMENT_ENABLED], [ML_MODEL_CONFIG], [GEOSPATIAL_ENRICHMENT_ENABLED], [GEO_CONFIG], [JOIN_CONFIGURATION], [AGGREGATION_REQUIRED], [DIMENSIONAL_MODEL_ENABLED], [GOLD_WRITE_MODE], [GOLD_PARTITION_COLUMNS], [OPTIMIZATION_STRATEGY], [KPI_1], [KPI_1_CALCULATION], [KPI_2], [KPI_2_CALCULATION], [KPI_3], [KPI_3_CALCULATION], [CATEGORY_COLUMN], [CATEGORIZATION_LOGIC], [TIME_PERIOD], [TIME_PERIOD_LOGIC], [FISCAL_PERIOD], [FISCAL_PERIOD_LOGIC], [RANK_COLUMN], [SCORE_COLUMN], [RANK_METHOD], [RANK_ASCENDING], [EXPIRATION_DATE], [CURRENT_DATE], [IS_CURRENT], [EFFECTIVE_DATE], [HIGH_DATE], [VERSION_NUMBER], [NEW_VERSION_LOGIC], [CONCATENATION_LOGIC], [WINDOW_SIZE], [VALUE_COLUMN], [LAG_PERIODS], [AMOUNT_COLUMN], [RUNNING_TOTAL], [MOVING_AVERAGE], [PREVIOUS_VALUE], [RANK], [PERCENTILE_RANK], [DAG_ID], [PIPELINE_OWNER], [DEPENDS_ON_PAST], [START_YEAR], [START_MONTH], [START_DAY], [EMAIL_ON_FAILURE], [EMAIL_ON_RETRY], [RETRY_COUNT], [RETRY_DELAY_MINUTES], [MAX_ACTIVE_RUNS], [CONCURRENCY_LIMIT], [DAG_DESCRIPTION], [SCHEDULE_INTERVAL], [CATCHUP_ENABLED], [TAG_1], [TAG_2], [TAG_3], [SOURCE_1_TASK], [SOURCE_1_SHORT], [SOURCE_1_CONNECTION], [SOURCE_1_QUERY], [RESOURCE_POOL_1], [SOURCE_1_RETRIES], [SOURCE_2_TASK], [SOURCE_2_SHORT], [SOURCE_2_CONNECTION], [SOURCE_2_QUERY], [RESOURCE_POOL_2], [SOURCE_2_RETRIES], [SOURCE_SYSTEM_2], [BRONZE_TO_SILVER_FUNCTION], [BRONZE_TABLE_1], [BRONZE_TABLE_2], [SILVER_TABLE], [TRANSFORMATION_POOL], [SILVER_TO_GOLD_FUNCTION], [SILVER_TABLE_1], [SILVER_TABLE_2], [GOLD_TABLE], [DATA_QUALITY_FUNCTION], [SUCCESS_NOTIFICATION_FUNCTION], [PIPELINE_NAME], [FAILURE_NOTIFICATION_FUNCTION], [DATA_VOLUME_CHECK_LOGIC], [LARGE_VOLUME_THRESHOLD], [MEDIUM_VOLUME_THRESHOLD], [LARGE_VOLUME_PROCESSOR], [MEDIUM_VOLUME_PROCESSOR], [SMALL_VOLUME_PROCESSOR], [MONITORING_FRAMEWORK], [METRICS_CONFIG], [ALERT_CONFIG], [PIPELINE_DASHBOARD_NAME], [STATUS_REFRESH_INTERVAL], [DURATION_TIME_RANGE], [VOLUME_GROUPING], [CRITICAL_NOTIFICATION_CHANNEL], [HIGH_NOTIFICATION_CHANNEL], [MEDIUM_NOTIFICATION_CHANNEL], [METRICS_STREAMING_SYSTEM], [STREAM_CONFIG], [METRICS_TABLE], [MONITORING_WINDOW], [LATENCY_THRESHOLD_MS], [THROUGHPUT_THRESHOLD], [BACKLOG_THRESHOLD], [PIPELINE_LOGGER], [ERROR_STORAGE_SYSTEM], [ERROR_STORE_CONFIG], [STACK_TRACE_EXTRACTION], [MAX_CONNECTION_RETRIES], [DEFAULT_BATCH_SIZE], [CURRENT_TIME], [QUARANTINE_SCHEMA], [DATABASE_EXECUTOR], [PERFORMANCE_METRICS_COLLECTOR], [ANALYSIS_TIME_RANGE], [AVG_DURATION_CALCULATION], [P95_DURATION_CALCULATION], [AVG_THROUGHPUT_CALCULATION], [PEAK_CPU_CALCULATION], [PEAK_MEMORY_CALCULATION], [AVG_ERROR_RATE_CALCULATION], [DATA_VOLUME_TREND_CALCULATION], [PARALLELIZATION_IMPROVEMENT_ESTIMATE], [BATCH_SIZE_IMPROVEMENT_ESTIMATE], [SCALING_IMPROVEMENT_ESTIMATE], [CACHING_IMPROVEMENT_ESTIMATE], [MEMORY_IMPROVEMENT_ESTIMATE], [STREAMING_IMPROVEMENT_ESTIMATE], [IMPROVEMENT_WEIGHT], [EFFORT_WEIGHT], [MAX_BATCH_SIZE_MULTIPLIER], [MIN_BATCH_SIZE], [MAX_BATCH_SIZE], [CPU_SCALE_UP_THRESHOLD], [CPU_SCALE_DOWN_THRESHOLD], [MEMORY_SCALE_UP_THRESHOLD], [MEMORY_SCALE_DOWN_THRESHOLD], [MIN_INSTANCES], [MAX_INSTANCES], [SCALE_UP_COOLDOWN], [SCALE_DOWN_COOLDOWN], [COMPUTE_RESOURCE], [CLUSTER_NAME], [VERSION], [NODE_COUNT], [NODE_TYPE], [DISK_SIZE], [MIN_NODES], [MAX_NODES], [TARGET_CPU_UTILIZATION], [TARGET_MEMORY_UTILIZATION], [VPC_ID], [SUBNET_IDS], [SECURITY_GROUP_IDS], [ENVIRONMENT], [PROJECT_NAME], [TEAM_OWNER], [ORCHESTRATION_SERVICE], [ORCHESTRATION_INSTANCE], [ORCHESTRATION_INSTANCE_NAME], [ORCHESTRATION_VERSION], [ORCHESTRATION_INSTANCE_TYPE], [AVAILABILITY_ZONES], [REPLICA_COUNT], [STORAGE_SIZE], [STORAGE_TYPE], [PRIVATE_SUBNET_IDS], [ORCHESTRATION_SECURITY_GROUP_ID], [LOG_LEVEL], [STORAGE_SERVICE], [DATA_LAKE_STORAGE], [DATA_LAKE_BUCKET_NAME], [STORAGE_CLASS], [TRANSITION_TO_IA_DAYS], [INFREQUENT_ACCESS_CLASS], [TRANSITION_TO_GLACIER_DAYS], [ARCHIVE_CLASS], [EXPIRATION_DAYS], [ENCRYPTION_ALGORITHM], [KMS_KEY_ID], [DATABASE_SERVICE], [DATA_WAREHOUSE], [DATA_WAREHOUSE_IDENTIFIER], [DATABASE_ENGINE], [DATABASE_VERSION], [DATABASE_INSTANCE_CLASS], [DATABASE_STORAGE_SIZE], [MULTI_AZ_ENABLED], [BACKUP_RETENTION_DAYS], [BACKUP_WINDOW], [MAINTENANCE_WINDOW], [DATABASE_SECURITY_GROUP_IDS], [DATABASE_SUBNET_GROUP], [DATABASE_KMS_KEY_ID], [MONITORING_INTERVAL], [PIPELINE_SERVICE_NAME], [NAMESPACE], [SERVICE_VERSION], [CONTAINER_NAME], [CONTAINER_IMAGE], [IMAGE_TAG], [CONTAINER_PORT], [ENV_VAR_1], [ENV_VALUE_1], [ENV_VAR_2], [SECRET_NAME], [SECRET_KEY], [MEMORY_REQUEST], [CPU_REQUEST], [MEMORY_LIMIT], [CPU_LIMIT], [VOLUME_NAME], [MOUNT_PATH], [HEALTH_CHECK_PATH], [HEALTH_CHECK_PORT], [LIVENESS_INITIAL_DELAY], [LIVENESS_PERIOD], [READINESS_CHECK_PATH], [READINESS_CHECK_PORT], [READINESS_INITIAL_DELAY], [READINESS_PERIOD], [PVC_NAME], [SERVICE_NAME], [SERVICE_PORT], [SERVICE_TYPE], [HPA_NAME], [MIN_REPLICAS], [MAX_REPLICAS], [CPU_TARGET_UTILIZATION], [MEMORY_TARGET_UTILIZATION], [DEPLOYMENT_REGION]

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
