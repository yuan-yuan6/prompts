---
title: Data Transformation & Processing
category: data-analytics/Analytics Engineering
tags: [data-analytics, development, etl, transformation, processing]
use_cases:
  - Designing and implementing data transformation logic including ETL/ELT transformations, business rules, dimensional modeling, and complex analytical processing for data pipelines.
  - Building bronze-to-silver and silver-to-gold transformation layers
related_templates:
  - pipeline-development-overview.md
  - data-ingestion-extraction.md
  - pipeline-quality-validation.md
  - pipeline-deployment-orchestration.md
last_updated: 2025-11-09
---

# Data Transformation & Processing

## Purpose
Design and implement comprehensive data transformation logic including cleansing, enrichment, business rules, dimensional modeling, and analytical transformations for multi-layer data architectures.

## Template

```
You are a data transformation specialist. Design transformation logic for [ORGANIZATION_NAME] to process data from [SOURCE_LAYER] to [TARGET_LAYER] using [TRANSFORMATION_METHODOLOGY].

TRANSFORMATION REQUIREMENTS:
- Source layer: [SOURCE_LAYER] (Bronze/Silver/Raw)
- Target layer: [TARGET_LAYER] (Silver/Gold/Business)
- Transformation type: [TRANSFORMATION_TYPE] (Cleansing/Enrichment/Aggregation/Dimensional)
- Processing framework: [PROCESSING_FRAMEWORK]
- Business rules: [BUSINESS_RULES]
- Data model: [DATA_MODEL] (Dimensional/Normalized/Denormalized)

Provide complete implementation for:
1. Data cleansing and standardization logic
2. Business rule transformations
3. Data enrichment from reference sources
4. Aggregation and analytical calculations
5. Dimensional modeling (if applicable)
6. Performance optimization strategies
```

## Bronze to Silver Transformations

### Pattern 1: Data Cleansing Pipeline
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
                    'processing_date': transformation_date,
                    'quality_score': [QUALITY_THRESHOLD]
                }
            )

            # Data cleaning transformations
            cleaned_df = self.apply_cleansing_rules(source_df)

            # Standardization
            standardized_df = self.apply_standardization(cleaned_df)

            # Enrichment
            enriched_df = self.apply_enrichment(standardized_df)

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
        df['phone_number'] = df['phone_number'].apply([PHONE_STANDARDIZER])
        df['email'] = df['email'].str.lower().str.strip()
        df['date_column'] = [PROCESSING_FRAMEWORK].to_datetime(df['date_column'])

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
        df['mapped_category'] = df['source_code'].map([CODE_MAPPING_DICT])

        # Business rule applications
        df['calculated_field_1'] = [CALCULATION_LOGIC_1]
        df['calculated_field_2'] = [CALCULATION_LOGIC_2]

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
```

## Silver to Gold Transformations

### Pattern 1: Business Layer Aggregations
```python
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

        # Write to gold layer
        write_stats = self.engine.write_table(
            df=final_df,
            table_name=target_table,
            mode='[GOLD_WRITE_MODE]',
            partition_by=[GOLD_PARTITION_COLUMNS],
            optimize=[OPTIMIZATION_STRATEGY]
        )

        # Update metadata
        self.update_table_metadata(
            table_name=target_table,
            processing_date=transformation_date,
            record_count=len(final_df),
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
    df['revenue'] = [KPI_1_CALCULATION]
    df['profit_margin'] = [KPI_2_CALCULATION]
    df['customer_lifetime_value'] = [KPI_3_CALCULATION]

    # Business categorizations
    df['customer_segment'] = df.apply([CATEGORIZATION_LOGIC], axis=1)

    # Time-based calculations
    df['fiscal_quarter'] = [TIME_PERIOD_LOGIC]
    df['fiscal_year'] = [FISCAL_PERIOD_LOGIC]

    # Ranking and scoring
    df['customer_rank'] = df['total_spend'].rank(
        method='[RANK_METHOD]',
        ascending=[RANK_ASCENDING]
    )

    return df
```

## Advanced Transformation Patterns

### Pattern 1: Slowly Changing Dimension (SCD) Type 2
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

        Args:
            current_df: Current dimension table state
            new_df: New dimension records
            business_key: Natural business key column
            scd_columns: Columns to track for changes

        Returns:
            Updated dimension DataFrame with versioning
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
        expire_updates['expiration_date'] = [CURRENT_DATE]
        expire_updates['is_current'] = False

        # Create new versions
        new_versions = new_df[new_df[business_key].isin(
            expire_updates[business_key]
        )].copy()
        new_versions['effective_date'] = [CURRENT_DATE]
        new_versions['expiration_date'] = '9999-12-31'
        new_versions['is_current'] = True
        new_versions['version_number'] = [NEW_VERSION_LOGIC]

        # Combine results
        result_df = [CONCATENATION_LOGIC]

        return result_df
```

### Pattern 2: Window Function Analytics
```python
@staticmethod
def window_function_analytics(df, partition_cols: list, order_cols: list):
    """
    Apply advanced window function analytics

    Args:
        df: Input DataFrame
        partition_cols: Columns to partition by
        order_cols: Columns to order by

    Returns:
        DataFrame with window function calculations
    """
    from [PROCESSING_FRAMEWORK].sql import functions as F
    from [PROCESSING_FRAMEWORK].sql.window import Window

    # Define window specifications
    window_spec = Window.partitionBy(partition_cols).orderBy(order_cols)

    # Running totals
    df = df.withColumn(
        'running_total',
        F.sum('amount').over(window_spec)
    )

    # Moving averages
    moving_window = window_spec.rowsBetween(-[WINDOW_SIZE], 0)
    df = df.withColumn(
        'moving_average',
        F.avg('value').over(moving_window)
    )

    # Lag/Lead calculations
    df = df.withColumn(
        'previous_value',
        F.lag('value', [LAG_PERIODS]).over(window_spec)
    )

    # Rank calculations
    df = df.withColumn(
        'rank',
        F.row_number().over(window_spec)
    )

    # Percentile calculations
    df = df.withColumn(
        'percentile_rank',
        F.percent_rank().over(window_spec)
    )

    return df
```

### Pattern 3: Data Deduplication
```python
@staticmethod
def data_deduplication_strategy(df, dedup_columns: list, ranking_column: str):
    """
    Advanced deduplication with ranking

    Args:
        df: Input DataFrame with duplicates
        dedup_columns: Columns to identify duplicates
        ranking_column: Column to determine which record to keep

    Returns:
        Deduplicated DataFrame
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
    deduplicated_df = df_with_rank.filter(
        F.col('dedup_rank') == 1
    ).drop('dedup_rank')

    return deduplicated_df
```

### Pattern 4: Complex Joins
```python
def perform_multi_table_join(
    self,
    tables: list,
    join_logic: dict,
    processing_date: str
) -> DataFrame:
    """
    Perform complex multi-table joins

    Args:
        tables: List of table names to join
        join_logic: Join configuration
        processing_date: Processing date for filtering

    Returns:
        Joined DataFrame
    """
    # Load base table
    base_df = self.engine.read_table(
        table_name=tables[0],
        filters={'processing_date': processing_date}
    )

    # Sequential joins
    for i, table_name in enumerate(tables[1:], 1):
        join_config = join_logic.get(table_name, {})

        # Load table to join
        join_df = self.engine.read_table(
            table_name=table_name,
            filters={'processing_date': processing_date}
        )

        # Perform join
        base_df = base_df.merge(
            join_df,
            left_on=join_config.get('left_keys', []),
            right_on=join_config.get('right_keys', []),
            how=join_config.get('join_type', 'inner'),
            suffixes=join_config.get('suffixes', ('', f'_{i}'))
        )

    return base_df
```

### Pattern 5: Pivot and Unpivot
```python
def pivot_transformation(df, index_cols: list, pivot_col: str, value_col: str):
    """
    Pivot transformation for wide-format conversion

    Args:
        df: Input DataFrame
        index_cols: Columns to use as index
        pivot_col: Column to pivot on
        value_col: Column with values

    Returns:
        Pivoted DataFrame
    """
    pivoted_df = df.pivot_table(
        index=index_cols,
        columns=pivot_col,
        values=value_col,
        aggfunc=[AGGREGATION_FUNCTION],
        fill_value=[FILL_VALUE]
    ).reset_index()

    return pivoted_df

def unpivot_transformation(df, id_cols: list, value_cols: list):
    """
    Unpivot transformation for long-format conversion

    Args:
        df: Input DataFrame
        id_cols: Identifier columns to preserve
        value_cols: Columns to unpivot

    Returns:
        Unpivoted DataFrame
    """
    unpivoted_df = df.melt(
        id_vars=id_cols,
        value_vars=value_cols,
        var_name='metric_name',
        value_name='metric_value'
    )

    return unpivoted_df
```

## Performance Optimization Techniques

### Technique 1: Predicate Pushdown
```python
# Push filters down to data source for efficiency
def optimized_read(table_name: str, filters: dict):
    """
    Read data with predicate pushdown optimization
    """
    # Build filter expression
    filter_expr = " AND ".join([
        f"{col} = '{val}'" if isinstance(val, str) else f"{col} = {val}"
        for col, val in filters.items()
    ])

    # Read with pushed-down predicates
    df = [PROCESSING_FRAMEWORK].read_table(
        table_name,
        filter=filter_expr,
        columns=[REQUIRED_COLUMNS_ONLY]  # Column pruning
    )

    return df
```

### Technique 2: Partition Pruning
```python
# Leverage partitioning for efficient data access
def partition_aware_processing(
    table_name: str,
    partition_col: str,
    partition_values: list
):
    """
    Process data with partition pruning
    """
    # Read only required partitions
    df = [PROCESSING_FRAMEWORK].read_table(
        table_name,
        filters={partition_col: partition_values}
    )

    return df
```

### Technique 3: Broadcast Joins
```python
# Use broadcast joins for small dimension tables
from [PROCESSING_FRAMEWORK].sql import functions as F

def optimized_dimension_join(fact_df, dim_df, join_keys: list):
    """
    Join large fact table with small dimension using broadcast
    """
    # Broadcast small dimension table
    broadcast_dim = F.broadcast(dim_df)

    # Perform join
    joined_df = fact_df.join(
        broadcast_dim,
        on=join_keys,
        how='left'
    )

    return joined_df
```

## Variables
[ORGANIZATION_NAME], [SOURCE_LAYER], [TARGET_LAYER], [TRANSFORMATION_METHODOLOGY], [TRANSFORMATION_TYPE], [PROCESSING_FRAMEWORK], [BUSINESS_RULES], [DATA_MODEL], [TRANSFORMATION_FRAMEWORK], [ENGINE_CONFIG], [LINEAGE_TRACKER], [LINEAGE_CONFIG], [QUALITY_THRESHOLD], [WRITE_MODE], [PARTITION_COLUMNS], [TRANSFORMATION_LIST], [ERROR_HANDLER], [COLUMN_1], [DEFAULT_VALUE_1], [COLUMN_2], [DEFAULT_VALUE_2], [COLUMN_3], [DEFAULT_VALUE_3], [COLUMN_4], [TARGET_TYPE_1], [COLUMN_5], [TARGET_TYPE_2], [COLUMN_6], [TARGET_TYPE_3], [PHONE_STANDARDIZER], [OUTLIER_COLUMNS], [REFERENCE_DATA_1], [LOOKUP_COLUMN_1], [REFERENCE_KEY_1], [CODE_MAPPING_DICT], [CALCULATION_LOGIC_1], [CALCULATION_LOGIC_2], [HIERARCHY_COLUMNS], [EXTERNAL_ENRICHMENT_ENABLED], [API_CONFIG], [ML_ENRICHMENT_ENABLED], [ML_MODEL_CONFIG], [GEOSPATIAL_ENRICHMENT_ENABLED], [GEO_CONFIG], [JOIN_CONFIGURATION], [AGGREGATION_REQUIRED], [DIMENSIONAL_MODEL_ENABLED], [GOLD_WRITE_MODE], [GOLD_PARTITION_COLUMNS], [OPTIMIZATION_STRATEGY], [KPI_1_CALCULATION], [KPI_2_CALCULATION], [KPI_3_CALCULATION], [CATEGORIZATION_LOGIC], [TIME_PERIOD_LOGIC], [FISCAL_PERIOD_LOGIC], [RANK_METHOD], [RANK_ASCENDING], [CURRENT_DATE], [NEW_VERSION_LOGIC], [CONCATENATION_LOGIC], [WINDOW_SIZE], [LAG_PERIODS], [AGGREGATION_FUNCTION], [FILL_VALUE], [REQUIRED_COLUMNS_ONLY]

## Best Practices

1. **Minimize data movement** - Filter and select columns early
2. **Use appropriate join types** - Choose inner/left/outer based on requirements
3. **Leverage partitioning** - Partition by date or high-cardinality columns
4. **Cache intermediate results** - For iterative transformations
5. **Broadcast small tables** - For efficient dimension joins
6. **Handle nulls explicitly** - Define clear null handling strategies
7. **Document business logic** - Explain complex calculations
8. **Version transformations** - Track changes to transformation logic
9. **Test with production-like data** - Validate transformations at scale
10. **Monitor transformation metrics** - Track duration, volume, and quality
