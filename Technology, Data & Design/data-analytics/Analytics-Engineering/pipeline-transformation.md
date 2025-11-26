---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Analytics-Engineering/pipeline-ingestion.md
- data-analytics/Analytics-Engineering/pipeline-orchestration.md
- data-analytics/Analytics-Engineering/pipeline-observability.md
- data-analytics/data-governance-framework.md
tags:
- automation
- data-analytics
- development
- data-quality
title: Pipeline Data Transformation Template
use_cases:
- Designing medallion architecture transformations (Bronze → Silver → Gold)
- Implementing data cleansing, standardization, and enrichment logic
- Building slowly changing dimensions (SCD Type 2) and dimensional models
- Applying complex transformations with window functions and aggregations
industries:
- government
- manufacturing
- retail
- technology
type: template
difficulty: intermediate
slug: pipeline-transformation
---

# Pipeline Data Transformation Template

## Purpose
Design and implement comprehensive data transformation pipelines following medallion architecture patterns (Bronze → Silver → Gold). This template covers data cleansing, standardization, enrichment, business logic application, and advanced transformation patterns including slowly changing dimensions and window analytics.

## Quick Transformation Prompt
Build a [BRONZE_TO_SILVER/SILVER_TO_GOLD] transformation for [DOMAIN_ENTITY] using [PROCESSING_FRAMEWORK]. Apply cleansing rules: [NULL_HANDLING], [DEDUPLICATION_KEY], [TYPE_CONVERSIONS]. Standardize using [REFERENCE_LOOKUPS], enrich with [CALCULATED_FIELDS], implement SCD Type [1/2] for [DIMENSION_COLUMNS], and add validation checks for [QUALITY_RULES].

## Quick Start

### For Data Engineers
Get started building transformation pipelines in 3 steps:

1. **Define Transformation Layers**
   - **Bronze Layer**: Raw data ingestion with minimal transformation
   - **Silver Layer**: Cleansed, standardized, validated data
   - **Gold Layer**: Business-ready aggregated and dimensional data
   - Example: `TRANSFORMATION_TYPE: "Bronze to Silver", FOCUS: "Data cleansing and standardization"`

2. **Implement Transformation Logic**
   - **Cleansing**: Handle nulls, fix data types, remove duplicates
   - **Standardization**: Apply reference data lookups, code mappings
   - **Enrichment**: Add calculated fields, ML predictions, external API data
   - **Validation**: Check data quality rules at each layer
   - Start with template code blocks (lines 76-272 for core pipeline, 274-390 for advanced patterns)

3. **Add Quality Controls**
   - Implement data quality checks between layers
   - Track data lineage and transformation metadata
   - Configure validation thresholds and alerts
   - Enable performance monitoring for transformations

**Key Sections**: Core Transformation Pipeline (lines 76-272), Complex Transformations (274-390)

## Template

```
You are a data transformation architect specializing in [TRANSFORMATION_METHODOLOGY]. Design a comprehensive data transformation solution for [ORGANIZATION_NAME] implementing medallion architecture (Bronze → Silver → Gold) using [PROCESSING_FRAMEWORK] and [TRANSFORMATION_FRAMEWORK].

TRANSFORMATION ARCHITECTURE OVERVIEW:
Project Specifications:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Data processing domain: [DATA_PROCESSING_DOMAIN]
- Transformation scope: [TRANSFORMATION_SCOPE]
- Business objectives: [DATA_PROCESSING_OBJECTIVES]
- Data quality requirements: [DATA_QUALITY_REQUIREMENTS]
- Compliance standards: [COMPLIANCE_STANDARDS]

### Architecture Principles
- Transformation methodology: [TRANSFORMATION_METHODOLOGY] (Medallion/Star Schema/Data Vault)
- Processing approach: [PROCESSING_APPROACH] (Batch/Micro-batch/Streaming)
- Data quality strategy: [DATA_QUALITY_STRATEGY]
- Lineage tracking: [LINEAGE_TRACKING_ENABLED]
- Error handling: [ERROR_HANDLING_PHILOSOPHY]
- Performance optimization: [OPTIMIZATION_STRATEGY]

### Technical Stack
- Transformation framework: [TRANSFORMATION_FRAMEWORK]
- Processing framework: [PROCESSING_FRAMEWORK] (Spark/Pandas/Dask)
- Orchestration platform: [ORCHESTRATION_PLATFORM]
- Cloud provider: [CLOUD_PROVIDER]
- Storage format: [STORAGE_FORMAT] (Parquet/Delta/Iceberg)
- Data catalog: [DATA_CATALOG_SYSTEM]

### Data Layer Architecture
- Bronze layer path: [BRONZE_LAYER_PATH]
- Silver layer path: [SILVER_LAYER_PATH]
- Gold layer path: [GOLD_LAYER_PATH]
- Partition strategy: [PARTITION_STRATEGY]
- Retention policy: [RETENTION_POLICY]

### TRANSFORMATION LAYER DESIGN

### Core Transformation Pipeline
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

        Args:
            source_table: Bronze layer source table
            target_table: Silver layer target table
            transformation_date: Processing date

        Returns:
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

        Args:
            source_tables: List of silver layer source tables
            target_table: Gold layer target table
            transformation_date: Processing date

        Returns:
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
```

### Complex Transformation Logic
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
                changed_records[f'{col}_new'] != changed_records[f'{col}_current']
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
```

OUTPUT: Deliver comprehensive data transformation solution including:
1. Bronze to Silver transformation logic with data cleansing
2. Silver to Gold transformation with business logic
3. Data quality validation at each layer
4. Slowly changing dimension (SCD Type 2) implementation
5. Window function analytics for advanced calculations
6. Data deduplication strategies
7. Reference data lookups and code mappings
8. External enrichment integrations (API, ML models)
9. Data lineage tracking and metadata management
10. Performance optimization for large-scale transformations
```

## Variables

### Core Configuration
[TRANSFORMATION_METHODOLOGY], [ORGANIZATION_NAME], [INDUSTRY_SECTOR], [DATA_PROCESSING_DOMAIN], [TRANSFORMATION_SCOPE], [DATA_PROCESSING_OBJECTIVES], [DATA_QUALITY_REQUIREMENTS], [COMPLIANCE_STANDARDS]

### Architecture Settings
[PROCESSING_APPROACH], [DATA_QUALITY_STRATEGY], [LINEAGE_TRACKING_ENABLED], [ERROR_HANDLING_PHILOSOPHY], [OPTIMIZATION_STRATEGY]

### Technical Stack
[TRANSFORMATION_FRAMEWORK], [PROCESSING_FRAMEWORK], [ORCHESTRATION_PLATFORM], [CLOUD_PROVIDER], [STORAGE_FORMAT], [DATA_CATALOG_SYSTEM]

### Data Layer Paths
[BRONZE_LAYER_PATH], [SILVER_LAYER_PATH], [GOLD_LAYER_PATH], [PARTITION_STRATEGY], [RETENTION_POLICY]

### Transformation Engine
[ENGINE_CONFIG], [LINEAGE_TRACKER], [LINEAGE_CONFIG], [DATE_COLUMN], [QUALITY_FILTER], [QUALITY_THRESHOLD], [CLEANING_TRANSFORMATIONS], [WRITE_MODE], [PARTITION_COLUMNS], [TRANSFORMATION_LIST], [ERROR_HANDLER]

### Cleansing Variables
[COLUMN_1], [DEFAULT_VALUE_1], [COLUMN_2], [DEFAULT_VALUE_2], [COLUMN_3], [DEFAULT_VALUE_3], [COLUMN_4], [TARGET_TYPE_1], [COLUMN_5], [TARGET_TYPE_2], [COLUMN_6], [TARGET_TYPE_3], [PHONE_COLUMN], [PHONE_STANDARDIZER], [EMAIL_COLUMN], [OUTLIER_COLUMNS]

### Standardization Variables
[REFERENCE_DATA_1], [LOOKUP_COLUMN_1], [REFERENCE_KEY_1], [MAPPED_COLUMN], [SOURCE_COLUMN], [CODE_MAPPING_DICT], [CALCULATED_COLUMN_1], [CALCULATION_LOGIC_1], [CALCULATED_COLUMN_2], [CALCULATION_LOGIC_2], [HIERARCHY_COLUMNS]

### Enrichment Variables
[EXTERNAL_ENRICHMENT_ENABLED], [API_CONFIG], [ML_ENRICHMENT_ENABLED], [ML_MODEL_CONFIG], [GEOSPATIAL_ENRICHMENT_ENABLED], [GEO_CONFIG]

### Gold Layer Variables
[JOIN_CONFIGURATION], [AGGREGATION_REQUIRED], [DIMENSIONAL_MODEL_ENABLED], [GOLD_WRITE_MODE], [GOLD_PARTITION_COLUMNS]

### Business Logic Variables
[KPI_1], [KPI_1_CALCULATION], [KPI_2], [KPI_2_CALCULATION], [KPI_3], [KPI_3_CALCULATION], [CATEGORY_COLUMN], [CATEGORIZATION_LOGIC], [TIME_PERIOD], [TIME_PERIOD_LOGIC], [FISCAL_PERIOD], [FISCAL_PERIOD_LOGIC], [RANK_COLUMN], [SCORE_COLUMN], [RANK_METHOD], [RANK_ASCENDING]

### SCD Type 2 Variables
[EXPIRATION_DATE], [CURRENT_DATE], [IS_CURRENT], [EFFECTIVE_DATE], [HIGH_DATE], [VERSION_NUMBER], [NEW_VERSION_LOGIC], [CONCATENATION_LOGIC]

### Window Function Variables
[WINDOW_SIZE], [VALUE_COLUMN], [LAG_PERIODS], [AMOUNT_COLUMN], [RUNNING_TOTAL], [MOVING_AVERAGE], [PREVIOUS_VALUE], [RANK], [PERCENTILE_RANK]

## Usage Examples

### Example 1: E-commerce Customer 360 Transformation
```
TRANSFORMATION_METHODOLOGY: "Medallion Architecture"
BRONZE_TO_SILVER: "Cleanse customer data, standardize addresses, validate emails"
SILVER_TO_GOLD: "Create customer 360 view joining orders, interactions, preferences"
BUSINESS_LOGIC: "Calculate customer lifetime value, RFM scores, churn probability"
KPI_1: "customer_lifetime_value = SUM(order_total) over customer history"
SCD_TYPE: "Type 2 for customer attributes (address, preferences)"
PARTITION_STRATEGY: "Partition by date and customer_segment"
```

### Example 2: Financial Reporting Aggregation
```
TRANSFORMATION_METHODOLOGY: "Star Schema Dimensional Model"
SILVER_TO_GOLD: "Build fact_transactions and dim_accounts, dim_products"
AGGREGATION_REQUIRED: true
AGGREGATIONS: ["daily_balances", "monthly_revenue", "quarterly_metrics"]
FISCAL_PERIOD_LOGIC: "Custom fiscal calendar starting Q1 in February"
WINDOW_FUNCTIONS: ["running_balance", "moving_avg_30_days", "year_over_year_growth"]
GOLD_WRITE_MODE: "overwrite with partition pruning"
```

### Example 3: IoT Sensor Data Processing
```
TRANSFORMATION_METHODOLOGY: "Streaming Micro-batch Medallion"
BRONZE_TO_SILVER: "Parse JSON sensor payloads, filter invalid readings, deduplicate"
DEDUPLICATION_STRATEGY: "Keep latest reading per sensor_id within 1-minute window"
ENRICHMENT: "Add device metadata, location coordinates, weather data from API"
WINDOW_ANALYTICS: "Calculate 5-min moving averages, detect anomalies"
SILVER_TO_GOLD: "Aggregate to hourly metrics by device_type and location"
PARTITION_STRATEGY: "Partition by hour for fast time-range queries"
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Pipeline Ingestion](pipeline-ingestion.md)** - Complementary approaches and methodologies
- **[Pipeline Orchestration](pipeline-orchestration.md)** - Complementary approaches and methodologies
- **[Pipeline Observability](pipeline-observability.md)** - Complementary approaches and methodologies
- **[Data Governance Framework](data-governance-framework.md)** - Leverage data analysis to drive informed decisions

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Pipeline Data Transformation Template)
2. Use [Pipeline Ingestion](pipeline-ingestion.md) for deeper analysis
3. Apply [Pipeline Orchestration](pipeline-orchestration.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Analytics Engineering](../../data-analytics/Analytics Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Designing medallion architecture transformations (Bronze → Silver → Gold)**: Combine this template with related analytics and strategy frameworks
- **Implementing data cleansing, standardization, and enrichment logic**: Combine this template with related analytics and strategy frameworks
- **Building slowly changing dimensions (SCD Type 2) and dimensional models**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Immutable bronze layer** - Keep raw data unchanged for reprocessing capability
2. **Schema evolution** - Handle schema changes gracefully with explicit mappings
3. **Incremental processing** - Process only new/changed data to optimize performance
4. **Idempotent transformations** - Ensure reruns produce same results
5. **Data quality gates** - Fail fast on critical quality issues, quarantine minor issues
6. **Partition pruning** - Use effective partitioning for query performance
7. **Broadcast joins** - Use for small reference tables in distributed processing
8. **Column pruning** - Select only needed columns early in pipeline
9. **Predicate pushdown** - Apply filters before expensive transformations
10. **Lineage tracking** - Maintain transformation metadata for debugging and auditing

## Tips for Success

- Use Delta Lake or Iceberg for ACID transactions and time travel
- Implement data quality checks between each layer transformation
- Cache intermediate results for complex multi-step transformations
- Use Spark's adaptive query execution (AQE) for automatic optimization
- Profile transformation performance to identify bottlenecks
- Implement SCD Type 2 only when history tracking is truly needed
- Use window functions instead of self-joins for better performance
- Validate transformation logic on sample data before full pipeline runs
- Document business logic and calculation formulas in code comments
- Build reusable transformation functions for common patterns
- Monitor data drift in distributions and value ranges
- Implement soft deletes instead of hard deletes for data recovery
- Use temporary views for complex multi-step SQL transformations
- Leverage columnar storage formats (Parquet) for analytical workloads
- Test edge cases: nulls, duplicates, outliers, empty datasets
