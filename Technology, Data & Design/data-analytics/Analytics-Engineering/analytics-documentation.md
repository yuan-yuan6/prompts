---
category: data-analytics
description: Design data governance frameworks including lineage tracking, data dictionaries, schema documentation, metadata management, and governance workflows for enterprise data platforms
title: Documentation, Lineage and Governance
tags:
- data-governance
- data-lineage
- metadata-management
- analytics-engineering
use_cases:
- Building data catalogs with comprehensive metadata and business context
- Implementing data lineage tracking for impact analysis and compliance
- Creating automated schema documentation and data dictionaries
- Establishing governance workflows for data access and quality stewardship
related_templates:
- data-analytics/Analytics-Engineering/analytics-data-quality.md
- data-analytics/Analytics-Engineering/analytics-data-modeling.md
- data-analytics/data-governance-framework.md
industries:
- finance
- healthcare
- retail
- technology
- government
type: framework
difficulty: intermediate
slug: analytics-documentation
---

# Documentation, Lineage and Governance

## Purpose
Design comprehensive data governance frameworks covering data lineage tracking, metadata management, data dictionaries, schema documentation automation, and governance workflows. This framework ensures data assets are discoverable, understood, trusted, and compliant across enterprise data platforms.

## 🚀 Quick Start Prompt

> Design a **data governance framework** for **[DATA PLATFORM]** covering **[SCOPE]** data assets. Implement: (1) **Metadata catalog**—technical and business metadata for all tables, columns, and pipelines; (2) **Data lineage**—source-to-target tracking at column level with transformation documentation; (3) **Data dictionary**—business glossary with terms, definitions, and ownership; (4) **Governance workflows**—access requests, quality stewardship, and change management. Deliver catalog structure, lineage visualization approach, dictionary template, and governance process designs.

---

## Template

Design a comprehensive governance framework for {DATA_PLATFORM_CONTEXT}, documenting {ASSET_SCOPE} to achieve {GOVERNANCE_OBJECTIVES}.

**1. Metadata Management Architecture**

Begin by designing the metadata management foundation that captures all information about your data assets. Define metadata categories: technical metadata (schema, data types, constraints, indexes, partitioning, storage format), operational metadata (row counts, size, freshness, access patterns, performance metrics), business metadata (descriptions, owners, domains, glossary terms, usage context), and governance metadata (classification, sensitivity, compliance tags, retention policies, access restrictions). Design the metadata repository schema to store this information with versioning for change tracking. Implement automated metadata extraction from source systems—database catalogs, ETL tools, BI platforms, and API schemas. Create metadata quality scoring based on completeness (percentage of fields documented), accuracy (verified against reality), and currency (last updated timestamp). Establish metadata update triggers—schema changes should automatically update technical metadata, while business metadata requires human review workflows.

**2. Data Asset Registration and Cataloging**

Design the data catalog structure for asset discovery and understanding. Create a hierarchical organization: data domains (logical business areas like Customer, Product, Finance), systems (source applications and databases), schemas (logical groupings within systems), and assets (tables, views, files, APIs). For each asset, capture identity information (unique ID, name, location, type), ownership (business owner, data steward, technical owner), classification (sensitivity level, compliance requirements, retention policy), and relationships (upstream sources, downstream consumers, related assets). Implement asset scoring combining data quality scores, documentation completeness, usage frequency, and governance compliance. Design search and discovery interfaces enabling users to find assets by name, description, domain, owner, tags, or related business terms. Create asset profiles showing statistics, sample data, quality metrics, lineage, and access information in a single view.

**3. Data Lineage Tracking System**

Implement comprehensive lineage tracking showing how data flows from source to consumption. Design lineage at multiple granularities: system-level (which applications exchange data), table-level (which tables feed which), and column-level (specific field transformations and mappings). Capture lineage through multiple methods—automated parsing of SQL queries and ETL configurations, API call logging, and manual documentation for complex transformations. For each lineage edge, document the transformation logic (SQL, code reference, or description), timing (batch schedule, real-time, event-triggered), and data quality impact (filtering, aggregation, enrichment). Build lineage visualization showing upstream sources (where data comes from), downstream consumers (where data goes), and transformation steps. Implement impact analysis answering "if this source changes, what is affected?" and root cause analysis answering "where did this data value originate?"

**4. Business Glossary and Data Dictionary**

Create a business glossary that bridges technical data and business understanding. Define glossary term structure: term name, definition (clear, unambiguous business meaning), synonyms and related terms, examples, business owner, data steward, source systems, and associated data elements. Establish term governance—who can create terms, approval workflow for definitions, conflict resolution when teams disagree on meanings. Link glossary terms to physical data assets—which columns represent "Customer" or "Revenue" across systems. Design the data dictionary at column level: column name, data type, description, business glossary term linkage, valid values or domain, business rules, and transformation logic if derived. Implement semantic search enabling users to find data by business concept rather than technical name. Track term usage across queries, reports, and documentation to identify most important concepts.

**5. Schema Documentation Automation**

Automate documentation generation to reduce manual effort and maintain currency. Extract schema information directly from source systems—database metadata catalogs, schema registries, API specifications. Generate documentation templates automatically with technical details populated (columns, types, constraints, relationships) and placeholders for business context requiring human input. Implement documentation formats for different audiences: technical reference (full schema details for developers), business overview (simplified descriptions for analysts), executive summary (key metrics and ownership for stakeholders). Create change detection comparing current schema to documented version—flag additions, modifications, and deletions for review. Generate documentation outputs in multiple formats: searchable web catalog, exportable PDF, wiki integration (Confluence, Notion), and API for programmatic access. Track documentation staleness—time since last human review—and trigger refresh workflows.

**6. Governance Workflow Design**

Design governance workflows that balance control with agility. Create data access request workflow: requester submits justification, system checks classification and compliance requirements, routes to appropriate approvers (data owner for business approval, security for sensitive data), tracks SLA for response time, provisions access upon approval, and logs for audit. Design data quality stewardship workflow: quality issues detected by automated monitoring are routed to responsible data steward, steward investigates and documents root cause, remediation is assigned and tracked, resolution is verified and closed. Implement change management workflow: proposed changes to data assets (schema, ownership, classification) require impact analysis, stakeholder notification, approval chain, implementation tracking, and rollback procedures. Create governance escalation paths for disputes, urgent access needs, and policy exceptions.

**7. Compliance and Audit Support**

Build governance capabilities supporting regulatory compliance and audit readiness. Implement data classification automation suggesting sensitivity levels based on column names, data patterns, and content analysis—with human validation for final assignment. Create compliance mapping linking data assets to regulatory requirements (GDPR for personal data, HIPAA for health information, SOX for financial data) with documentation of controls applied. Design audit trail capturing who accessed what data, when, for what purpose, and what actions were taken—with tamper-evident logging. Generate compliance reports showing data inventory by classification, access patterns for sensitive data, retention policy adherence, and control effectiveness. Implement data subject rights support: ability to find all data about an individual across systems (for access requests), document processing purposes and legal bases (for transparency), and support deletion or anonymization (for erasure requests).

**8. Governance Metrics and Continuous Improvement**

Establish metrics to measure governance effectiveness and drive improvement. Track documentation coverage: percentage of assets with complete metadata, percentage of columns with descriptions, percentage of business terms with approved definitions. Measure lineage completeness: percentage of data flows documented, percentage of transformations with logic documented, lineage gaps identified and remediated. Monitor governance workflow performance: average time to provision access, percentage of requests meeting SLA, data quality issue resolution time, change request cycle time. Assess data discoverability: search success rate, time to find relevant assets, user satisfaction scores. Create governance maturity scoring combining coverage, accuracy, timeliness, and adoption metrics. Establish improvement targets and track progress quarterly. Implement feedback mechanisms for users to report documentation gaps, suggest improvements, and rate asset quality.

Deliver your governance framework as:

1. **Metadata architecture** specifying categories, schema, extraction methods, and quality scoring
2. **Catalog design** with hierarchy, asset attributes, scoring, and search capabilities
3. **Lineage system** covering granularity levels, capture methods, visualization, and analysis features
4. **Glossary structure** with term template, governance workflow, and system linkage
5. **Documentation automation** specifying extraction, templates, formats, and staleness tracking
6. **Workflow designs** for access requests, quality stewardship, and change management
7. **Compliance capabilities** including classification, audit trails, and regulatory mapping
8. **Governance metrics** with coverage, performance, and maturity measurements

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{DATA_PLATFORM_CONTEXT}` | Platform, systems, and scale | "Snowflake data warehouse with 500 tables, dbt transformations, and Tableau dashboards" |
| `{ASSET_SCOPE}` | What assets need governance | "customer data domain including CRM, marketing, and support system data" |
| `{GOVERNANCE_OBJECTIVES}` | Why governance matters | "GDPR compliance, self-service analytics enablement, and M&A due diligence readiness" |

---

## Usage Examples

### Example 1: Financial Services Data Governance
**Prompt:** "Design a comprehensive governance framework for {DATA_PLATFORM_CONTEXT: enterprise data lake on AWS with 2,000 tables across trading, risk, and regulatory reporting domains, Informatica ETL, and Power BI reporting}, documenting {ASSET_SCOPE: all data assets with priority on regulatory reporting feeds and customer financial data}, to achieve {GOVERNANCE_OBJECTIVES: BCBS 239 compliance for data lineage, SOX audit readiness, and reducing time-to-insight for risk analysts}."

**Expected Output:** Metadata architecture with mandatory fields for regulatory data (effective date, reporting period, submission deadline), Informatica lineage integration via metadata export, and Power BI dataset documentation. Catalog organized by regulatory domain (Basel, CCAR, liquidity) with compliance tagging. Column-level lineage from source systems through transformations to regulatory reports with reconciliation checkpoints. Glossary with regulatory term definitions (Tier 1 Capital, RWA, LCR) linked to official regulatory glossaries. Automated documentation from Informatica mappings with attestation workflow for business sign-off. Access workflow with mandatory compliance training verification, time-limited access for contractors, quarterly recertification. Audit reports showing data lineage from any regulatory figure back to source system records.

### Example 2: Healthcare Data Governance
**Prompt:** "Design a comprehensive governance framework for {DATA_PLATFORM_CONTEXT: clinical data warehouse integrating Epic EHR, claims processing, and research databases with 800 tables and Tableau analytics}, documenting {ASSET_SCOPE: patient data, clinical outcomes, and research datasets across 15 hospital facilities}, to achieve {GOVERNANCE_OBJECTIVES: HIPAA compliance, enabling federated research analytics, and supporting value-based care reporting}."

**Expected Output:** Metadata architecture with PHI indicators, de-identification status, and consent tracking at column level. Catalog organized by clinical domain (encounters, diagnoses, procedures, medications) with facility and IRB protocol tagging. Lineage tracking from EHR source fields through de-identification transforms to research datasets with audit trail of PHI access. Clinical glossary with ICD-10, CPT, and clinical terminology linked to standard ontologies (SNOMED, LOINC). Automated documentation from Epic data model with clinical SME validation workflow. Access workflow with IRB approval verification for research data, minimum necessary enforcement, and break-glass procedures for emergencies. HIPAA audit reports showing PHI access patterns, de-identification validation, and consent compliance.

### Example 3: E-commerce Data Governance
**Prompt:** "Design a comprehensive governance framework for {DATA_PLATFORM_CONTEXT: Databricks lakehouse with 400 tables from Shopify, Salesforce, and marketing platforms, dbt transformations, and Looker dashboards}, documenting {ASSET_SCOPE: customer behavior, product catalog, and marketing attribution data}, to achieve {GOVERNANCE_OBJECTIVES: CCPA/GDPR compliance, enabling marketing self-service analytics, and supporting customer 360 initiatives}."

**Expected Output:** Metadata architecture with PII flags, consent status, and data subject identifiers for privacy compliance. Catalog organized by customer journey stage (acquisition, conversion, retention) with marketing channel tagging. Lineage from source platforms through identity resolution and attribution models to marketing dashboards with dbt documentation integration. Business glossary defining marketing metrics (CAC, LTV, attribution) with calculation methodology and Looker measure linkage. Automated documentation from dbt YAML with Looker explore descriptions synced. Self-service access for marketing team to non-PII aggregates with approval workflow for individual-level data. Privacy reports showing personal data inventory, consent rates by purpose, and data subject request fulfillment metrics.

---

## Cross-References

- [analytics-data-quality.md](analytics-data-quality.md) - Quality validation that feeds governance metrics
- [analytics-data-modeling.md](analytics-data-modeling.md) - Data modeling patterns to document
- [data-governance-framework.md](../data-governance-framework.md) - Enterprise governance strategy
