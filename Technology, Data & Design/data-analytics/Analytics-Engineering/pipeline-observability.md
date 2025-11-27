---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Analytics-Engineering/pipeline-ingestion.md
- data-analytics/Analytics-Engineering/pipeline-transformation.md
- data-analytics/Analytics-Engineering/pipeline-orchestration.md
- data-analytics/Analytics-Engineering/pipeline-infrastructure.md
tags:
- data-analytics
- observability
- monitoring
- error-handling
title: Pipeline Observability & Error Handling Template
use_cases:
- Implementing comprehensive pipeline monitoring and alerting systems
- Designing error handling frameworks with recovery strategies
- Building real-time streaming pipeline monitors
- Implementing circuit breakers and resilience patterns
industries:
- healthcare
- manufacturing
- retail
- technology
type: template
difficulty: intermediate
slug: pipeline-observability
---

# Pipeline Observability & Error Handling Template

## Purpose
Design and implement comprehensive monitoring, observability, and error handling systems for data pipelines. This template covers metrics collection, alerting, dashboard creation, error recovery strategies, circuit breakers, and operational resilience patterns.

## Quick Monitoring Prompt
Design an observability system for [PIPELINE_NAME] using [MONITORING_FRAMEWORK]. Track metrics: [EXECUTION_TIME/THROUGHPUT/ERROR_RATE], set SLA threshold at [SLA_MINUTES] minutes, implement [ERROR_SEVERITY] classification with [RETRY/QUARANTINE/DLQ] recovery strategies. Include circuit breaker with [FAILURE_THRESHOLD] failures triggering [COOLDOWN_SECONDS]s cooldown and alerting via [ALERT_CHANNEL].

## Quick Start

### For Data Engineers
Get started with pipeline observability in 3 steps:

1. **Set Up Monitoring Framework**
   - **Metrics Collection**: Track execution time, throughput, error rates, resource usage
   - **SLA Monitoring**: Define and monitor pipeline SLAs
   - **Dashboard Creation**: Build operational dashboards for pipeline health
   - Example: `METRICS: ["execution_duration", "records_processed", "error_count"], SLA_THRESHOLD: 120 minutes`

2. **Implement Error Handling**
   - **Error Classification**: Categorize errors by severity (LOW/MEDIUM/HIGH/CRITICAL)
   - **Recovery Strategies**: Implement retry with backoff, quarantine, dead letter queue
   - **Alerting**: Configure notifications based on error severity
   - Start with error handling framework (lines 357-633)

3. **Add Resilience Patterns**
   - **Circuit Breakers**: Prevent cascading failures from unreliable dependencies
   - **Dead Letter Queues**: Handle permanently failed records
   - **Graceful Degradation**: Continue processing good data when some fails
   - Use circuit breaker pattern (lines 635-679)

**Key Sections**: Pipeline Monitoring (lines 78-254), Streaming Monitor (256-320), Error Handling (357-633), Circuit Breaker (635-679)

## Template

```
You are a data pipeline observability architect specializing in [MONITORING_STRATEGY]. Design a comprehensive monitoring, alerting, and error handling solution for [ORGANIZATION_NAME] to ensure [RELIABILITY_OBJECTIVES] using [MONITORING_FRAMEWORK] and [ALERTING_PLATFORM].

OBSERVABILITY ARCHITECTURE OVERVIEW:
Project Specifications:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Pipeline scope: [PIPELINE_SCOPE]
- Reliability objectives: [RELIABILITY_OBJECTIVES]
- SLA requirements: [SLA_REQUIREMENTS]
- On-call model: [ON_CALL_MODEL]

### Architecture Principles
- Monitoring strategy: [MONITORING_STRATEGY]
- Alerting philosophy: [ALERTING_PHILOSOPHY]
- Error handling approach: [ERROR_HANDLING_PHILOSOPHY]
- Recovery strategy: [RECOVERY_STRATEGY]
- Observability depth: [OBSERVABILITY_DEPTH] (Basic/Standard/Comprehensive)
- Incident response: [INCIDENT_RESPONSE_MODEL]

### Technical Stack
- Monitoring framework: [MONITORING_FRAMEWORK] (Prometheus/Datadog/CloudWatch)
- Alerting platform: [ALERTING_PLATFORM] (PagerDuty/Opsgenie/Slack)
- Logging system: [LOGGING_SYSTEM] (ELK/Splunk/CloudWatch Logs)
- Metrics storage: [METRICS_STORAGE] (InfluxDB/TimescaleDB/Prometheus)
- Dashboard platform: [DASHBOARD_PLATFORM] (Grafana/Tableau/DataDog)
- Tracing system: [TRACING_SYSTEM] (Jaeger/Zipkin/X-Ray)

### Monitoring Requirements
- Metrics frequency: [METRICS_COLLECTION_FREQUENCY]
- Retention period: [METRICS_RETENTION_PERIOD]
- Alert latency: [ALERT_LATENCY_REQUIREMENT]
- Dashboard refresh: [DASHBOARD_REFRESH_INTERVAL]
- Log retention: [LOG_RETENTION_PERIOD]
- Trace sampling: [TRACE_SAMPLING_RATE]

### MONITORING AND OBSERVABILITY

### Pipeline Monitoring Framework
```python
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
        sla_threshold = self.thresholds.get(f'{pipeline_id}_sla_minutes', [DEFAULT_SLA_MINUTES])

        if duration > sla_threshold * 60:  # Convert minutes to seconds
            self.alert_manager.send_alert(
                alert_type='SLA_BREACH',
                severity='HIGH',
                message=f'Pipeline {pipeline_id} exceeded SLA: {duration/60:.2f} minutes > {sla_threshold} minutes',
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
            failure_threshold = self.thresholds.get(f'{pipeline_id}_failure_rate', [DEFAULT_FAILURE_RATE])

            if failure_rate > failure_threshold:
                self.alert_manager.send_alert(
                    alert_type='DATA_QUALITY_BREACH',
                    severity='MEDIUM',
                    message=f'Pipeline {pipeline_id} data quality threshold breached: {failure_rate:.2%} > {failure_threshold:.2%}',
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
```

### Real-time Streaming Pipeline Monitor
```python
# Real-time monitoring for streaming pipelines
class StreamingPipelineMonitor:
    def __init__(self, config: dict):
        self.config = config
        self.metrics_stream = [METRICS_STREAMING_SYSTEM]([STREAM_CONFIG])

    def monitor_streaming_metrics(self, stream_name: str):
        """
        Monitor real-time streaming pipeline metrics
        """
        metrics_query = f"""
        SELECT
            stream_name,
            window_start,
            window_end,
            records_processed,
            processing_latency_ms,
            throughput_per_second,
            error_count,
            backlog_size
        FROM {[METRICS_TABLE]}
        WHERE stream_name = '{stream_name}'
        AND window_end >= NOW() - INTERVAL '[MONITORING_WINDOW]'
        """

        # Execute continuous monitoring query
        monitoring_stream = self.metrics_stream.sql(metrics_query)

        # Apply real-time alerting
        alerting_stream = monitoring_stream.map(self.check_streaming_thresholds)

        return alerting_stream

    def check_streaming_thresholds(self, metrics: dict):
        """
        Check streaming metrics against real-time thresholds
        """
        stream_name = metrics['stream_name']

        # Latency monitoring
        if metrics['processing_latency_ms'] > [LATENCY_THRESHOLD_MS]:
            self.send_realtime_alert(
                alert_type='HIGH_LATENCY',
                stream_name=stream_name,
                current_value=metrics['processing_latency_ms'],
                threshold=[LATENCY_THRESHOLD_MS]
            )

        # Throughput monitoring
        if metrics['throughput_per_second'] < [THROUGHPUT_THRESHOLD]:
            self.send_realtime_alert(
                alert_type='LOW_THROUGHPUT',
                stream_name=stream_name,
                current_value=metrics['throughput_per_second'],
                threshold=[THROUGHPUT_THRESHOLD]
            )

        # Backlog monitoring
        if metrics['backlog_size'] > [BACKLOG_THRESHOLD]:
            self.send_realtime_alert(
                alert_type='HIGH_BACKLOG',
                stream_name=stream_name,
                current_value=metrics['backlog_size'],
                threshold=[BACKLOG_THRESHOLD]
            )
```

### ERROR HANDLING AND RECOVERY

### Error Handling Framework
```python
# Comprehensive error handling system
import logging
from enum import Enum
from typing import Optional, Dict, Any

class ErrorSeverity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class PipelineErrorHandler:
    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger('[PIPELINE_LOGGER]')
        self.error_store = [ERROR_STORAGE_SYSTEM]([ERROR_STORE_CONFIG])
        self.recovery_strategies = self.load_recovery_strategies()

    def handle_pipeline_error(
        self,
        error: Exception,
        context: dict,
        severity: ErrorSeverity = ErrorSeverity.MEDIUM
    ) -> dict:
        """
        Centralized pipeline error handling

        Args:
            error: The exception that occurred
            context: Execution context information
            severity: Error severity level

        Returns:
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
        self.logger.error(f"Pipeline error {error_id}: {error_details}")

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
                recovery_result['actions_taken'].append(f'Scheduled retry in {retry_delay} seconds')
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
                recovery_result['actions_taken'].append(f'Reduced batch size to {new_batch_size}')
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
            self.logger.error(f"Recovery strategy {strategy} failed: {recovery_error}")

        return recovery_result

    def quarantine_bad_data(self, error_details: dict, context: dict) -> dict:
        """
        Quarantine problematic data for later analysis
        """
        try:
            quarantine_table = f"{[QUARANTINE_SCHEMA]}.{context['table_name']}_quarantine"

            # Move bad records to quarantine
            quarantine_query = f"""
            INSERT INTO {quarantine_table}
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
            WHERE {context['error_filter_condition']}
            """

            [DATABASE_EXECUTOR].execute(cleanup_query)

            return {'success': True, 'quarantine_table': quarantine_table}

        except Exception as e:
            return {'success': False, 'error': str(e)}
```

### Circuit Breaker Pattern Implementation
```python
# Circuit breaker pattern implementation
class CircuitBreaker:
    def __init__(self, failure_threshold: int, timeout: int, expected_exception: Exception = Exception):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.expected_exception = expected_exception
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN

    def call(self, func, *args, **kwargs):
        """
        Execute function with circuit breaker protection
        """
        if self.state == 'OPEN':
            if self.should_attempt_reset():
                self.state = 'HALF_OPEN'
            else:
                raise Exception(f"Circuit breaker is OPEN. Service unavailable.")

        try:
            result = func(*args, **kwargs)
            self.on_success()
            return result
        except self.expected_exception as e:
            self.on_failure()
            raise e

    def on_success(self):
        """Handle successful execution"""
        self.failure_count = 0
        if self.state == 'HALF_OPEN':
            self.state = 'CLOSED'

    def on_failure(self):
        """Handle failed execution"""
        self.failure_count += 1
        self.last_failure_time = [CURRENT_TIME]

        if self.failure_count >= self.failure_threshold:
            self.state = 'OPEN'

    def should_attempt_reset(self):
        """Check if circuit breaker should attempt reset"""
        return ([CURRENT_TIME] - self.last_failure_time) >= self.timeout
```

OUTPUT: Deliver comprehensive observability and error handling solution including:
1. Pipeline execution monitoring with metrics collection
2. SLA compliance tracking and alerting
3. Data quality threshold monitoring
4. Resource utilization dashboards
5. Real-time streaming pipeline monitors
6. Comprehensive error handling framework
7. Multiple recovery strategies (retry, quarantine, DLQ)
8. Circuit breaker implementation for resilience
9. Error classification by severity
10. Automated incident response workflows
11. Operational dashboards and visualizations
12. Alerting configurations with notification channels
```

## Variables

### Core Configuration
[MONITORING_STRATEGY], [ORGANIZATION_NAME], [PIPELINE_SCOPE], [RELIABILITY_OBJECTIVES], [SLA_REQUIREMENTS], [ON_CALL_MODEL]

### Architecture Settings
[ALERTING_PHILOSOPHY], [ERROR_HANDLING_PHILOSOPHY], [RECOVERY_STRATEGY], [OBSERVABILITY_DEPTH], [INCIDENT_RESPONSE_MODEL]

### Technical Stack
[MONITORING_FRAMEWORK], [ALERTING_PLATFORM], [LOGGING_SYSTEM], [METRICS_STORAGE], [DASHBOARD_PLATFORM], [TRACING_SYSTEM]

### Monitoring Requirements
[METRICS_COLLECTION_FREQUENCY], [METRICS_RETENTION_PERIOD], [ALERT_LATENCY_REQUIREMENT], [DASHBOARD_REFRESH_INTERVAL], [LOG_RETENTION_PERIOD], [TRACE_SAMPLING_RATE]

### Metrics Configuration
[METRICS_CONFIG], [ALERT_CONFIG], [DEFAULT_SLA_MINUTES], [DEFAULT_FAILURE_RATE]

### Dashboard Configuration
[PIPELINE_DASHBOARD_NAME], [STATUS_REFRESH_INTERVAL], [DURATION_TIME_RANGE], [VOLUME_GROUPING], [CRITICAL_NOTIFICATION_CHANNEL], [HIGH_NOTIFICATION_CHANNEL], [MEDIUM_NOTIFICATION_CHANNEL]

### Streaming Monitor
[METRICS_STREAMING_SYSTEM], [STREAM_CONFIG], [METRICS_TABLE], [MONITORING_WINDOW], [LATENCY_THRESHOLD_MS], [THROUGHPUT_THRESHOLD], [BACKLOG_THRESHOLD]

### Error Handling
[PIPELINE_LOGGER], [ERROR_STORAGE_SYSTEM], [ERROR_STORE_CONFIG], [STACK_TRACE_EXTRACTION], [CURRENT_TIMESTAMP], [MAX_CONNECTION_RETRIES], [DEFAULT_BATCH_SIZE], [CURRENT_TIME], [QUARANTINE_SCHEMA], [DATABASE_EXECUTOR]

## Usage Examples

### Example 1: E-commerce Pipeline Monitoring
```
MONITORING_FRAMEWORK: "Datadog"
PIPELINE_DASHBOARD_NAME: "Ecommerce ETL Health"
KEY_METRICS:
  - execution_duration: SLA 120 minutes, alert if > 150 minutes
  - records_processed: Expected 1M-5M daily, alert if < 500K
  - error_rate: Threshold 1%, alert if > 2%
  - data_freshness: Target < 30 minutes, alert if > 60 minutes
ALERTS:
  - CRITICAL: Pipeline failure → Page on-call engineer
  - HIGH: SLA breach → Send Slack alert to #data-engineering
  - MEDIUM: Data quality issues → Email team lead
DASHBOARD_PANELS: [Status grid, Duration trends, Error analysis, Data volume]
```

### Example 2: Real-time Streaming Monitor
```
STREAMING_SOURCE: "Kafka clickstream events"
METRICS_STREAMING_SYSTEM: "Flink SQL"
MONITORING_WINDOW: "5 minutes"
REAL_TIME_THRESHOLDS:
  - processing_latency_ms: 100 (alert if > 500)
  - throughput_per_second: 10000 (alert if < 5000)
  - backlog_size: 0 (alert if > 100000)
  - error_rate: 0.1% (alert if > 1%)
ALERTING: "Real-time alerts via PagerDuty for latency spikes"
DASHBOARD: "Live streaming metrics with 10-second refresh"
```

### Example 3: Error Handling with Recovery
```
ERROR_HANDLING_PHILOSOPHY: "Fail fast on critical, gracefully degrade on non-critical"
RECOVERY_STRATEGIES:
  - ConnectionError: Exponential backoff (1s, 2s, 4s, 8s, 16s)
  - ValidationError: Quarantine bad records, continue with good data
  - MemoryError: Reduce batch size by 50% and retry
  - SchemaError: Alert team, manual schema migration required
DEAD_LETTER_QUEUE: "S3 bucket for permanently failed records"
QUARANTINE_TABLE: "bronze.quarantine_[table_name]"
CIRCUIT_BREAKER:
  - failure_threshold: 5 consecutive failures
  - timeout: 60 seconds before attempting reset
  - apply_to: External API calls, unreliable data sources
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Pipeline Ingestion](pipeline-ingestion.md)** - Complementary approaches and methodologies
- **[Pipeline Transformation](pipeline-transformation.md)** - Strategic framework for organizational change initiatives
- **[Pipeline Orchestration](pipeline-orchestration.md)** - Complementary approaches and methodologies
- **[Pipeline Infrastructure](pipeline-infrastructure.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Pipeline Observability & Error Handling Template)
2. Use [Pipeline Ingestion](pipeline-ingestion.md) for deeper analysis
3. Apply [Pipeline Transformation](pipeline-transformation.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Analytics Engineering](../../data-analytics/Analytics Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Implementing comprehensive pipeline monitoring and alerting systems**: Combine this template with related analytics and strategy frameworks
- **Designing error handling frameworks with recovery strategies**: Combine this template with related analytics and strategy frameworks
- **Building real-time streaming pipeline monitors**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Monitor what matters** - Focus on business-critical metrics, not vanity metrics
2. **Set actionable alerts** - Every alert should have a clear response action
3. **Avoid alert fatigue** - Tune thresholds to minimize false positives
4. **Track SLA trends** - Monitor SLA compliance over time, not just breaches
5. **Implement graceful degradation** - Continue processing when non-critical components fail
6. **Use structured logging** - JSON logs for easy parsing and analysis
7. **Correlate metrics** - Link related metrics for root cause analysis
8. **Test error scenarios** - Regularly test error handling and recovery paths
9. **Document runbooks** - Provide clear operational procedures for common issues
10. **Review error patterns** - Regularly analyze errors to identify systemic issues

## Tips for Success

- Start with basic monitoring and add complexity incrementally
- Use percentiles (p50, p95, p99) instead of averages for latency metrics
- Implement health checks at multiple levels (task, DAG, infrastructure)
- Set up both technical and business metrics dashboards
- Use metric cardinality limits to prevent explosion of time series
- Implement sampling for high-volume trace data
- Create separate alert channels for different severities
- Use anomaly detection for metrics with unpredictable patterns
- Implement alerting on rate of change, not just absolute values
- Build self-healing capabilities where possible (auto-retry, auto-scale)
- Use distributed tracing for complex multi-system pipelines
- Implement data lineage tracking for debugging data quality issues
- Set up synthetic monitoring to test pipeline health proactively
- Use SLOs (Service Level Objectives) to drive reliability improvements
- Implement progressive alert escalation (Slack → Email → Page)
- Build error budgets to balance reliability and development velocity
- Use canary deployments to detect issues before full rollout
- Implement automated rollback on critical metric degradation
- Create team dashboards showing overall pipeline health at a glance
- Build alerting that includes context (recent changes, related metrics)
