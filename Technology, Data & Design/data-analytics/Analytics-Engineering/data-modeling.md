---
category: data-analytics
description: Design comprehensive data modeling architectures including dimensional models, normalized structures, Data Vault, and lakehouse patterns for enterprise analytics platforms
title: Data Modeling & Architecture
tags:
- data-modeling
- dimensional-modeling
- data-architecture
- analytics-engineering
use_cases:
- Designing dimensional models (star schema, snowflake) for analytics and BI
- Implementing Data Vault 2.0 for auditable enterprise data warehouses
- Creating lakehouse architectures with medallion (bronze-silver-gold) patterns
- Optimizing data models for query performance and storage efficiency
related_templates:
- data-analytics/Analytics-Engineering/analytics-data-quality.md
- data-analytics/Analytics-Engineering/analytics-documentation.md
- data-analytics/data-governance-framework.md
industries:
- finance
- healthcare
- retail
- technology
- manufacturing
type: framework
difficulty: intermediate
slug: data-modeling
---

# Data Modeling & Architecture

## Purpose
Design comprehensive data modeling architectures that transform raw data into analytics-ready structures. This framework covers dimensional modeling (Kimball), normalized approaches (Inmon), Data Vault 2.0, and modern lakehouse patterns, enabling informed architecture decisions based on business requirements, query patterns, and scalability needs.

## Template

Design a data modeling architecture for {BUSINESS_CONTEXT}, implementing {MODELING_REQUIREMENTS} to achieve {ARCHITECTURE_OBJECTIVES}.

**1. Modeling Approach Selection**

Begin by selecting the appropriate modeling methodology based on business requirements and technical constraints. Dimensional modeling (Kimball) suits business intelligence and analytics workloads where query performance and user understandability are paramount—star schemas with denormalized dimensions enable fast aggregations and intuitive navigation. Normalized modeling (Inmon) fits enterprise data warehouses requiring data consistency and flexibility—third normal form reduces redundancy and supports diverse analytical needs at the cost of query complexity. Data Vault 2.0 excels for auditable, scalable data warehouses with multiple source systems and frequent schema changes—hubs capture business keys, links represent relationships, and satellites store descriptive attributes with full history. Lakehouse architecture using medallion patterns (bronze-silver-gold) works for cloud-native platforms combining data lake flexibility with warehouse structure—raw data lands in bronze, cleaned data in silver, and business-ready aggregates in gold. Hybrid approaches combining multiple methodologies often provide optimal results—Data Vault for the integration layer feeding dimensional models for consumption.

**2. Conceptual Model Design**

Define the conceptual model capturing business entities, relationships, and processes independent of physical implementation. Identify core business entities representing the fundamental concepts your organization tracks—customers, products, orders, transactions, employees, locations—with clear definitions agreed upon by business stakeholders. Document entity relationships specifying cardinality (one-to-one, one-to-many, many-to-many) and optionality (required versus optional) based on business rules. Map business processes to events that generate data—sales transactions, customer interactions, inventory movements, financial postings—as these become fact tables in dimensional models. Define business hierarchies within entities—product category to subcategory to product, geography from country to region to city to store—as these structure dimension tables. Identify conformed dimensions shared across business processes—date, customer, product, employee—enabling consistent analysis across subject areas. Document business keys that uniquely identify entities in source systems, distinguishing from surrogate keys generated in the warehouse.

**3. Dimensional Model Design**

Design dimensional structures optimized for analytical queries and business user comprehension. Define fact tables specifying grain (what one row represents), measures (numeric values for aggregation), and foreign keys to dimensions. Choose fact table types based on business process: transaction facts capture individual events at atomic grain, periodic snapshots record status at regular intervals, accumulating snapshots track process milestones, and factless facts record events without measures. Design dimension tables with surrogate keys (warehouse-generated integers), business keys (source system identifiers), and descriptive attributes supporting filtering and grouping. Select slowly changing dimension (SCD) types for each attribute: Type 1 overwrites history (current value only), Type 2 tracks full history with effective dates, Type 3 stores current and previous values, and Type 6 combines approaches. Create conformed dimensions used consistently across fact tables ensuring enterprise-wide consistency—a customer dimension means the same thing everywhere. Design bridge tables for many-to-many relationships between facts and dimensions, and mini-dimensions for frequently changing attributes to reduce Type 2 explosion.

**4. Data Vault Design**

Implement Data Vault 2.0 structures for scalable, auditable data integration. Design hub tables containing unique business keys with hash keys for efficient joining, load timestamps for auditability, and record source tracking—one hub per core business concept (customer, product, account). Create link tables representing relationships between hubs, containing hash keys of participating hubs plus the link's own hash key, enabling flexible relationship modeling including hierarchies and many-to-many associations. Build satellite tables storing descriptive attributes attached to hubs or links, with hash difference columns enabling efficient change detection and full history through load timestamps. Implement point-in-time (PIT) tables pre-joining satellites at consistent timestamps to simplify downstream queries avoiding complex temporal joins. Create bridge tables in the business vault layer providing pre-computed relationship snapshots for common query patterns. Design reference tables for slowly changing code tables and lookups shared across the model. Apply consistent hashing algorithms (MD5, SHA-1) for hash keys ensuring reproducibility and efficient joins.

**5. Lakehouse Architecture Design**

Structure lakehouse layers following medallion architecture principles for cloud-native platforms. Design the bronze layer receiving raw data from source systems in original format with minimal transformation—append-only ingestion preserving complete history, schema-on-read flexibility, and metadata tagging for lineage tracking. Create the silver layer with cleaned, conformed data applying data quality rules, deduplication, schema enforcement, and standardized naming—this layer serves as the single source of truth for downstream consumption. Build the gold layer with business-ready aggregates, dimensional models, and feature stores optimized for specific use cases—reporting cubes, ML feature tables, and API-serving datasets. Implement incremental processing using change data capture or watermarks to efficiently process only new or modified records. Apply table formats (Delta Lake, Apache Iceberg, Apache Hudi) providing ACID transactions, time travel, and schema evolution on object storage. Design partitioning strategies by date or high-cardinality columns enabling partition pruning for common query patterns.

**6. Physical Design Optimization**

Optimize physical structures for query performance and storage efficiency. Implement partitioning dividing large tables into manageable segments—time-based partitioning for append-heavy fact tables, hash partitioning for even distribution across nodes, list partitioning for discrete categories. Apply clustering or sort keys ordering data within partitions to enable efficient range scans and predicate pushdown—cluster on frequently filtered columns appearing in WHERE clauses. Design indexing strategies appropriate to workload: B-tree indexes for point lookups and range scans in OLTP-style queries, columnstore indexes for analytical aggregations scanning many rows, and covering indexes including all columns needed by critical queries. Configure compression balancing storage savings against CPU overhead—columnar compression (dictionary, run-length, delta encoding) dramatically reduces analytical table sizes. Set appropriate fill factors for indexes on tables with frequent inserts, leaving space for new rows without immediate page splits. Consider materialized views or summary tables pre-computing expensive aggregations refreshed on schedule.

**7. Naming Conventions and Standards**

Establish consistent naming conventions enabling self-documenting models. Prefix tables by type: FACT_ for fact tables, DIM_ for dimensions, HUB_ for Data Vault hubs, LNK_ for links, SAT_ for satellites, STG_ for staging, and AGG_ for aggregates. Name fact tables for the business process measured (FACT_SALES, FACT_INVENTORY_SNAPSHOT) and dimensions for the entity described (DIM_CUSTOMER, DIM_PRODUCT). Use snake_case for column names with clear, business-meaningful terms—order_date rather than od, customer_name rather than cust_nm. Suffix columns by data type or role: _id for identifiers, _key or _sk for surrogate keys, _date for dates, _amt for amounts, _qty for quantities, _flag for booleans, _pct for percentages. Apply consistent grain indicators in fact tables—daily, monthly, transaction-level—in table names when multiple grains exist. Document all naming conventions in a data dictionary accessible to developers and analysts.

**8. Implementation and Deployment**

Plan implementation with appropriate governance and testing. Create DDL scripts with complete specifications including data types, constraints, defaults, indexes, and partitioning—version control all schema definitions. Implement in phases starting with highest-value subject areas, proving the architecture before expanding scope. Build ETL/ELT pipelines loading dimensions before facts, handling late-arriving dimensions gracefully, and implementing idempotent loads enabling safe reruns. Test data model correctness verifying referential integrity, grain compliance (no duplicates at declared grain), and measure accuracy against source system totals. Validate query performance against SLAs using representative query workloads, adjusting indexes and partitioning based on actual execution plans. Establish monitoring tracking data freshness, load success rates, and query performance trends. Document the model comprehensively including entity-relationship diagrams, data dictionaries, lineage documentation, and usage guidelines.

Deliver your data modeling architecture as:

1. **Approach selection** justifying methodology choice based on requirements
2. **Conceptual model** with entities, relationships, and business process mapping
3. **Logical design** specifying fact/dimension structures or hub/link/satellite patterns
4. **Physical design** with partitioning, clustering, indexing, and compression
5. **Optimization strategies** for query performance and storage efficiency
6. **Naming standards** ensuring consistency and self-documentation
7. **Implementation plan** with phasing, testing approach, and deployment procedures
8. **Governance artifacts** including data dictionary, lineage, and maintenance procedures

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{BUSINESS_CONTEXT}` | Domain, platform, and scale | "e-commerce analytics on Snowflake with 5 years of order history, 100M orders, 10M customers" |
| `{MODELING_REQUIREMENTS}` | What the model must support | "self-service BI for marketing and finance, real-time inventory visibility, customer 360 view" |
| `{ARCHITECTURE_OBJECTIVES}` | Success criteria | "sub-second dashboard queries, daily refresh by 6am, support 500 concurrent analysts" |

---

## Usage Examples

### Example 1: Retail Dimensional Model
**Prompt:** "Design a data modeling architecture for {BUSINESS_CONTEXT: multi-channel retail company on Databricks with 50 stores, e-commerce, and mobile app generating 2M daily transactions}, implementing {MODELING_REQUIREMENTS: Kimball dimensional model supporting sales analysis by product, store, customer, and promotion with inventory snapshots and customer lifetime value}, to achieve {ARCHITECTURE_OBJECTIVES: enable merchandising self-service analytics, support same-day sales reporting, and provide foundation for demand forecasting ML models}."

**Expected Output:** Approach selecting Kimball star schema for BI usability with lakehouse medallion layers for ML flexibility. Conceptual model identifying sales transaction, inventory snapshot, and customer interaction as core processes with product, store, customer, date, and promotion as conformed dimensions. Dimensional design with FACT_SALES at transaction line grain, FACT_INVENTORY_DAILY at store-product-day grain, DIM_CUSTOMER with Type 2 SCD for address changes and Type 1 for preferences. Physical design with FACT_SALES partitioned by sale_date, clustered on store_id and product_id, using Delta Lake format. Optimization including aggregate table for store-day sales and materialized view for customer lifetime value. Implementation phased as sales first, then inventory, then customer analytics.

### Example 2: Financial Services Data Vault
**Prompt:** "Design a data modeling architecture for {BUSINESS_CONTEXT: regional bank on Azure Synapse integrating core banking, CRM, and digital channels with strict audit requirements}, implementing {MODELING_REQUIREMENTS: Data Vault 2.0 for regulatory compliance and full history, business vault for risk reporting, and dimensional marts for executive dashboards}, to achieve {ARCHITECTURE_OBJECTIVES: pass regulatory audits with complete data lineage, support ad-hoc risk analysis, and deliver executive KPIs with 15-minute latency}."

**Expected Output:** Approach selecting Data Vault 2.0 for auditability with business vault acceleration and dimensional information marts. Conceptual model with customer, account, transaction, and product as hub entities, account-customer and transaction-account as links. Data Vault design with HUB_CUSTOMER containing customer_number business key, LNK_ACCOUNT_HOLDER connecting customers to accounts, SAT_CUSTOMER_DEMOGRAPHICS tracking address and contact changes with full history. Business vault with PIT_CUSTOMER for efficient point-in-time queries and BRG_CUSTOMER_PRODUCT for relationship snapshots. Information mart with star schema for executive dashboards built from business vault. Physical design with hash keys using SHA-256 for collision resistance, satellites partitioned by load_date. Implementation prioritizing regulatory reporting entities first.

### Example 3: Healthcare Lakehouse
**Prompt:** "Design a data modeling architecture for {BUSINESS_CONTEXT: healthcare system on Snowflake integrating Epic EHR, claims data, and wearable device streams for 2M patients}, implementing {MODELING_REQUIREMENTS: medallion architecture supporting clinical analytics, population health management, and research data sharing with HIPAA compliance}, to achieve {ARCHITECTURE_OBJECTIVES: enable clinical quality measure calculation, support real-time patient risk scoring, and provide de-identified research datasets}."

**Expected Output:** Approach selecting lakehouse medallion architecture for diverse data types and ML workloads with dimensional marts for structured reporting. Bronze layer receiving HL7 FHIR resources, claims files, and device telemetry in raw format with PHI encryption. Silver layer with patient master resolved across systems, encounter timeline, and clinical event normalization. Gold layer with dimensional model for quality measures (FACT_CLINICAL_ENCOUNTER, DIM_PATIENT, DIM_PROVIDER, DIM_DIAGNOSIS), feature store for risk models, and de-identified research views. Physical design with row-level security on patient dimensions, dynamic data masking on PHI columns, and separate secure shares for research. Partitioning by encounter_date with clustering on patient_id. Implementation starting with patient master and encounter facts before expanding to claims and device data.

---

## Cross-References

- [analytics-data-quality.md](analytics-data-quality.md) - Quality validation for modeled data
- [analytics-documentation.md](analytics-documentation.md) - Data dictionary and lineage documentation
- [data-governance-framework.md](../data-governance-framework.md) - Governance for data models
