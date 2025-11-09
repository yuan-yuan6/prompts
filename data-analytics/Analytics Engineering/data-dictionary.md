---
title: Data Dictionary Management Template
category: data-analytics/Analytics Engineering
tags: [data-analytics, data-dictionary, documentation, metadata, template]
use_cases:
  - Creating and managing comprehensive data dictionaries including business glossaries, data catalogs, metadata repositories, and data asset documentation for enterprise data platforms.
  - Data dictionary creation
  - Metadata management
related_templates:
  - analytics-documentation-overview.md
  - technical-documentation.md
  - data-governance-standards.md
last_updated: 2025-11-09
---

# Data Dictionary Management Template

## Purpose
Create and manage comprehensive data dictionaries including business glossaries, data catalogs, metadata repositories, and detailed data asset documentation for enterprise data platforms.

## Template

```
You are a data dictionary specialist. Create a data dictionary for [DATA_DOMAIN] covering [SCOPE] with [DETAIL_LEVEL] detail using [DICTIONARY_TOOLS] for [AUDIENCE].

DATA DICTIONARY FRAMEWORK:
Context:
- Data domain: [DATA_DOMAIN]
- Scope: [SCOPE] (Enterprise/Domain/System)
- Detail level: [DETAIL_LEVEL] (Basic/Standard/Comprehensive)
- Dictionary tools: [DICTIONARY_TOOLS]
- Target audience: [AUDIENCE]
- Update frequency: [UPDATE_FREQUENCY]
- Governance: [GOVERNANCE_APPROACH]

### BUSINESS GLOSSARY

```
Business Term: [TERM_NAME]

Definition: [CLEAR_BUSINESS_DEFINITION]

Business Context: [HOW_TERM_IS_USED_IN_BUSINESS]

Related Terms:
- Synonyms: [ALTERNATIVE_NAMES]
- Related concepts: [RELATED_TERMS]
- Parent term: [BROADER_TERM]
- Child terms: [MORE_SPECIFIC_TERMS]

Data Sources:
- Primary source: [PRIMARY_SYSTEM]
- Supporting sources: [SUPPORTING_SYSTEMS]

Business Rules:
- Rule 1: [BUSINESS_RULE_DESCRIPTION]
- Rule 2: [BUSINESS_RULE_DESCRIPTION]

Examples:
- Valid: [EXAMPLE_1]
- Invalid: [COUNTER_EXAMPLE]

Owner: [BUSINESS_OWNER]
Steward: [DATA_STEWARD]
Last Updated: [DATE]
Version: [VERSION_NUMBER]
```

### DATA CATALOG

```
Table/Dataset: [TABLE_NAME]

Business Name: [BUSINESS_FRIENDLY_NAME]

Description: [COMPREHENSIVE_DESCRIPTION]

Purpose: [WHY_THIS_DATA_EXISTS]

Classification: [CLASSIFICATION_LEVEL]
- Sensitivity: [PUBLIC/INTERNAL/CONFIDENTIAL/RESTRICTED]
- PII Indicator: [YES/NO]
- Compliance tags: [GDPR/HIPAA/SOX/etc.]

Technical Details:
- Database: [DATABASE_NAME]
- Schema: [SCHEMA_NAME]
- Table type: [TYPE] (Fact/Dimension/Reference/Transactional)
- Row count: [APPROXIMATE_ROWS]
- Update frequency: [FREQUENCY]
- Retention period: [RETENTION_POLICY]

Columns:

Column: [COLUMN_NAME]
├─ Business name: [BUSINESS_NAME]
├─ Description: [WHAT_IT_REPRESENTS]
├─ Data type: [DATA_TYPE]
├─ Length: [LENGTH]
├─ Nullable: [YES/NO]
├─ Primary key: [YES/NO]
├─ Foreign key: [REFERENCES]
├─ Business rules: [RULES]
├─ Valid values: [VALUE_LIST or RANGE]
├─ Example values: [EXAMPLES]
└─ Sensitivity: [CLASSIFICATION]

[Repeat for each column]

Relationships:
- Parent tables: [UPSTREAM_DEPENDENCIES]
- Child tables: [DOWNSTREAM_DEPENDENCIES]

Access:
- Access level: [WHO_CAN_ACCESS]
- Request process: [HOW_TO_REQUEST_ACCESS]

Quality:
- Quality score: [SCORE]/100
- Quality rules: [DEFINED_QUALITY_RULES]

Contact:
- Business owner: [NAME]
- Technical owner: [NAME]
- Data steward: [NAME]
```

### METADATA REPOSITORY

```python
# Metadata management structure
metadata_schema = {
    'asset_id': 'Unique identifier',
    'asset_name': 'Technical name',
    'business_name': 'Business-friendly name',
    'description': 'Comprehensive description',
    'asset_type': 'Table/View/Report/Dashboard/etc.',
    
    # Business metadata
    'business_owner': 'Owner name',
    'data_steward': 'Steward name',
    'business_domain': 'Domain classification',
    'business_glossary_terms': ['List of terms'],
    'business_rules': ['List of rules'],
    
    # Technical metadata
    'source_system': 'System of record',
    'database': 'Database name',
    'schema': 'Schema name',
    'data_types': {'column': 'type'},
    'constraints': ['List of constraints'],
    'indexes': ['List of indexes'],
    
    # Operational metadata
    'creation_date': 'Date created',
    'last_modified': 'Last update date',
    'update_frequency': 'How often updated',
    'row_count': 'Approximate rows',
    'size_mb': 'Storage size',
    
    # Governance metadata
    'classification': 'Sensitivity level',
    'compliance_tags': ['Regulatory requirements'],
    'retention_policy': 'How long retained',
    'access_restrictions': ['Access rules'],
    
    # Lineage metadata
    'upstream_sources': ['Source dependencies'],
    'downstream_consumers': ['Data consumers'],
    'transformation_logic': 'How data is transformed',
    
    # Quality metadata
    'quality_score': 'Quality rating',
    'quality_rules': ['Quality validations'],
    'last_quality_check': 'Last QA date'
}
```

OUTPUT REQUIREMENTS:
1. **Business Glossary** - Comprehensive term definitions
2. **Data Catalog** - Detailed asset documentation
3. **Column Dictionary** - Field-level documentation
4. **Lineage Maps** - Data flow documentation
5. **Access Guide** - How to access and use data
```

## Variables

- [DATA_DOMAIN] - Data domain covered
- [SCOPE] - Scope of dictionary
- [DETAIL_LEVEL] - Level of detail
- [DICTIONARY_TOOLS] - Tools used
- [AUDIENCE] - Target users
- [UPDATE_FREQUENCY] - How often updated
- [GOVERNANCE_APPROACH] - Governance model

## Usage Examples

### Example 1: Customer Data Dictionary
```
DATA_DOMAIN: "Customer Master Data"
SCOPE: "Enterprise-wide"
DETAIL_LEVEL: "Comprehensive"
AUDIENCE: "Business analysts, data scientists, developers"
UPDATE_FREQUENCY: "Quarterly with continuous minor updates"
```

### Example 2: Financial Reporting Dictionary
```
DATA_DOMAIN: "Financial Reporting"
SCOPE: "Finance department"
DETAIL_LEVEL: "Comprehensive with regulatory mappings"
AUDIENCE: "Finance analysts, auditors, compliance"
UPDATE_FREQUENCY: "Monthly"
```

## Best Practices

1. **Use clear business language** - Avoid technical jargon
2. **Provide examples** - Show valid and invalid values
3. **Keep current** - Regular updates
4. **Version control** - Track changes over time
5. **Link related terms** - Create semantic relationships
6. **Include ownership** - Clear accountability
7. **Document business rules** - Not just technical constraints
8. **Make searchable** - Enable easy discovery
