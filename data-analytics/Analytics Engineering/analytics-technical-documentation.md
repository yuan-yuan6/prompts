---
title: Analytics Technical Documentation
category: data-analytics/Analytics Engineering
tags: ['documentation', 'technical-docs', 'data-engineering', 'analytics']
use_cases:
  - Create technical documentation for data models, ETL pipelines, data architecture, and technical specifications for analytics platforms.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Analytics Technical Documentation

## Purpose
Create technical documentation for data models, ETL pipelines, data architecture, and technical specifications for analytics platforms.

## Quick Start

### For Data Engineers & Analytics Teams

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific needs for create
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine based on results

**Common Use Cases:**
- Create technical documentation for data models, ETL pipelines, data architecture, and technical specifications for analytics platforms.
- Project-specific implementations
- Practical applications and workflows




## Template

---
title: Documentation, Lineage & Governance Template
category: data-analytics/Analytics Engineering
tags: [automation, data-analytics, design, documentation, machine-learning, management, security, strategy]
use_cases:
  - Creating design comprehensive data governance frameworks including data lineage tracking systems, data dictionary management, schema documentation automation, metadata management, and enterprise data governance programs for modern data platforms.

  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---


## Purpose
Design comprehensive data governance frameworks including data lineage tracking systems, data dictionary management, schema documentation automation, metadata management, and enterprise data governance programs for modern data platforms.


### For Data Engineers
Set up data documentation and lineage in 3 steps:

1. **Initialize Metadata Repository**
   - Deploy metadata management system with schema registry and lineage tracker
   - Register data assets: Use `register_data_asset()` (lines 108-214) for tables, APIs, files
   - Capture metadata: Business context, technical specs, quality scores, governance tags
   - Example: Include `business_owner`, `data_domain`, `sensitivity_tags`, `compliance_tags` for each asset

2. **Implement Lineage Tracking**
   - **Automated Discovery**: Parse SQL, ETL configs, and API calls to extract lineage (lines 365-548)
   - **Column-Level Tracking**: Map source columns to targets with transformation logic
   - **Impact Analysis**: Identify upstream dependencies and downstream impacts (lines 549-585)
   - Use `DataLineageTracker` to discover system, table, and column-level lineage

3. **Generate Documentation**
   - **Schema Docs**: Auto-generate table and column documentation from metadata (lines 738-1055)
   - **Data Dictionary**: Create business glossary with terms, definitions, and usage context
   - **Lineage Visualization**: Generate interactive graphs showing data flow with `generate_lineage_visualization()` (587-620)
   - Set up automated doc generation in HTML, PDF, or Confluence formats

**Key Template Sections**: Metadata management (69-361), Lineage tracking (363-733), Documentation generation (736-1055), Governance workflows (1057-1491)


### Technical Architecture

### Comprehensive Metadata Architecture
```python

# Advanced metadata management system
import [METADATA_LIBRARY] as [METADATA_ALIAS]
from [GOVERNANCE_FRAMEWORK] import [GOVERNANCE_COMPONENTS]
from [LINEAGE_LIBRARY] import [LINEAGE_TRACKER]

class MetadataManagementSystem:
    def __init__(self, config: dict):
        self.config = config
        self.metadata_repository = [METADATA_ALIAS].Repository([METADATA_REPO_CONFIG])
        self.schema_registry = [SCHEMA_REGISTRY]([SCHEMA_CONFIG])
        self.lineage_tracker = [LINEAGE_TRACKER]([LINEAGE_CONFIG])
        self.governance_engine = [GOVERNANCE_COMPONENTS].GovernanceEngine([GOV_CONFIG])

    def initialize_metadata_framework(self, data_sources: list) -> dict:
        """
        Initialize comprehensive metadata management framework


### Returns
            Metadata framework initialization results
        """

        framework_results = {
            'metadata_repository_setup': self.setup_metadata_repository(),
            'schema_registry_init': self.initialize_schema_registry(),
            'lineage_tracking_setup': self.setup_lineage_tracking(),
            'governance_policies_init': self.initialize_governance_policies(),
            'data_catalog_creation': self.create_data_catalog(),
            'automated_discovery': self.setup_automated_discovery(data_sources),
            'quality_monitoring_init': self.setup_metadata_quality_monitoring()
        }

        return framework_results

    def register_data_asset(
        self,
        asset_info: dict,
        discovery_method: str = 'AUTOMATED'
    ) -> dict:
        """
        Register a new data asset with comprehensive metadata


### Returns
            Asset registration results
        """

        asset_metadata = {
            # Core identification
            'asset_id': [ASSET_ID_GENERATOR],
            'asset_name': asset_info['name'],
            'asset_type': asset_info['type'],
            'source_system': asset_info['source_system'],
            'database_name': asset_info.get('database'),
            'schema_name': asset_info.get('schema'),
            'table_name': asset_info.get('table'),

            # Business metadata
            'business_name': asset_info.get('business_name'),
            'business_description': asset_info.get('description'),
            'business_owner': asset_info.get('business_owner'),
            'data_domain': asset_info.get('data_domain'),
            'business_glossary_terms': asset_info.get('glossary_terms', []),
            'business_rules': asset_info.get('business_rules', []),
            'usage_context': asset_info.get('usage_context', []),

            # Technical metadata
            'technical_description': self.generate_technical_description(asset_info),
            'data_types': self.extract_data_types(asset_info),
            'column_metadata': self.extract_column_metadata(asset_info),
            'constraints': self.extract_constraints(asset_info),
            'indexes': self.extract_indexes(asset_info),
            'partitioning': self.extract_partitioning_info(asset_info),
            'storage_format': asset_info.get('storage_format'),
            'compression_type': asset_info.get('compression'),
            'encryption_status': asset_info.get('encryption_status'),

            # Operational metadata
            'creation_date': asset_info.get('creation_date', [CURRENT_TIMESTAMP]),
            'last_modified_date': asset_info.get('last_modified_date'),
            'last_accessed_date': asset_info.get('last_accessed_date'),
            'update_frequency': asset_info.get('update_frequency'),
            'data_freshness': self.calculate_data_freshness(asset_info),
            'size_metrics': self.extract_size_metrics(asset_info),
            'usage_statistics': self.extract_usage_statistics(asset_info),
            'performance_metrics': self.extract_performance_metrics(asset_info),

            # Governance metadata
            'classification_level': asset_info.get('classification_level'),
            'sensitivity_tags': asset_info.get('sensitivity_tags', []),
            'compliance_tags': asset_info.get('compliance_tags', []),
            'retention_policy': asset_info.get('retention_policy'),
            'access_restrictions': asset_info.get('access_restrictions', []),
            'data_steward': asset_info.get('data_steward'),
            'quality_score': self.calculate_initial_quality_score(asset_info),
            'governance_status': asset_info.get('governance_status', 'UNVERIFIED'),

            # Lineage metadata
            'upstream_dependencies': [],
            'downstream_dependencies': [],
            'transformation_lineage': [],
            'impact_analysis': {},

            # Discovery metadata
            'discovery_method': discovery_method,
            'discovery_timestamp': [CURRENT_TIMESTAMP],
            'discovery_agent': asset_info.get('discovery_agent'),
            'confidence_score': asset_info.get('confidence_score', 1.0),

            # Version control
            'metadata_version': '1.0',
            'schema_version': asset_info.get('schema_version'),
            'change_history': [],

            # Custom attributes
            'custom_attributes': asset_info.get('custom_attributes', {})
        }

        # Register in metadata repository
        registration_result = self.metadata_repository.register_asset(asset_metadata)

        # Update schema registry
        if asset_info.get('schema'):
            self.schema_registry.register_schema(
                asset_metadata['asset_id'],
                asset_info['schema']
            )

        # Initialize lineage tracking
        self.lineage_tracker.initialize_asset_tracking(asset_metadata['asset_id'])

        return {
            'asset_id': asset_metadata['asset_id'],
            'registration_status': registration_result['status'],
            'metadata_completeness': self.calculate_metadata_completeness(asset_metadata),
            'governance_actions_required': self.identify_governance_actions(asset_metadata),
            'next_steps': self.generate_asset_onboarding_steps(asset_metadata)
        }

    def extract_column_metadata(self, asset_info: dict) -> list:
        """
        Extract comprehensive column-level metadata
        """
        column_metadata = []

        if 'columns' in asset_info:
            for column_info in asset_info['columns']:
                column_meta = {
                    'column_name': column_info['name'],
                    'data_type': column_info['type'],
                    'length': column_info.get('length'),
                    'precision': column_info.get('precision'),
                    'scale': column_info.get('scale'),
                    'nullable': column_info.get('nullable', True),
                    'default_value': column_info.get('default_value'),

                    # Business metadata
                    'business_name': column_info.get('business_name'),
                    'description': column_info.get('description'),
                    'business_glossary_term': column_info.get('glossary_term'),
                    'examples': column_info.get('examples', []),
                    'valid_values': column_info.get('valid_values', []),

                    # Quality metadata
                    'data_quality_rules': column_info.get('quality_rules', []),
                    'null_percentage': column_info.get('null_percentage'),
                    'unique_percentage': column_info.get('unique_percentage'),
                    'completeness_score': column_info.get('completeness_score'),

                    # Statistical metadata
                    'min_value': column_info.get('min_value'),
                    'max_value': column_info.get('max_value'),
                    'avg_value': column_info.get('avg_value'),
                    'std_deviation': column_info.get('std_deviation'),
                    'distinct_count': column_info.get('distinct_count'),
                    'value_distribution': column_info.get('value_distribution', {}),

                    # Governance metadata
                    'sensitivity_classification': column_info.get('sensitivity'),
                    'pii_indicator': column_info.get('is_pii', False),
                    'privacy_tags': column_info.get('privacy_tags', []),
                    'masking_required': column_info.get('masking_required', False),
                    'access_restrictions': column_info.get('access_restrictions', []),

                    # Technical metadata
                    'column_position': column_info.get('position'),
                    'foreign_key_references': column_info.get('fk_references', []),
                    'primary_key': column_info.get('is_primary_key', False),
                    'index_participation': column_info.get('indexes', []),
                    'encoding': column_info.get('encoding'),
                    'compression': column_info.get('compression')
                }

                column_metadata.append(column_meta)

        return column_metadata

    def create_data_dictionary(self, scope: str = 'ENTERPRISE') -> dict:
        """
        Create comprehensive data dictionary


### Returns
            Data dictionary creation results
        """

        dictionary_structure = {
            'dictionary_metadata': {
                'dictionary_id': [DICTIONARY_ID_GENERATOR],
                'scope': scope,
                'creation_timestamp': [CURRENT_TIMESTAMP],
                'version': '1.0',
                'coverage_statistics': {},
                'update_frequency': [DICTIONARY_UPDATE_FREQUENCY]
            },
            'business_glossary': self.create_business_glossary(),
            'data_domains': self.define_data_domains(),
            'asset_catalog': self.generate_asset_catalog(),
            'schema_documentation': self.generate_schema_documentation(),
            'relationship_mappings': self.generate_relationship_mappings(),
            'governance_policies': self.document_governance_policies(),
            'usage_guidelines': self.create_usage_guidelines()
        }

        return dictionary_structure

    def create_business_glossary(self) -> dict:
        """
        Create comprehensive business glossary
        """
        business_glossary = {
            'glossary_metadata': {
                'total_terms': 0,
                'categories': [],
                'last_updated': [CURRENT_TIMESTAMP],
                'approval_status': 'DRAFT'
            },
            'business_terms': {},
            'categories': {
                '[CATEGORY_1]': {
                    'category_name': '[CATEGORY_1]',
                    'description': '[CATEGORY_1_DESCRIPTION]',
                    'owner': '[CATEGORY_1_OWNER]',
                    'terms': []
                },
                '[CATEGORY_2]': {
                    'category_name': '[CATEGORY_2]',
                    'description': '[CATEGORY_2_DESCRIPTION]',
                    'owner': '[CATEGORY_2_OWNER]',
                    'terms': []
                }
            },
            'relationships': {
                'synonyms': {},
                'related_terms': {},
                'hierarchies': {}
            }
        }

        # Sample business term structure
        sample_term = {
            'term_id': '[TERM_ID]',
            'term_name': '[BUSINESS_TERM_NAME]',
            'definition': '[BUSINESS_TERM_DEFINITION]',
            'category': '[TERM_CATEGORY]',
            'synonyms': ['[SYNONYM_1]', '[SYNONYM_2]'],
            'related_terms': ['[RELATED_TERM_1]', '[RELATED_TERM_2]'],
            'business_owner': '[TERM_BUSINESS_OWNER]',
            'data_steward': '[TERM_DATA_STEWARD]',
            'examples': ['[EXAMPLE_1]', '[EXAMPLE_2]'],
            'usage_context': '[TERM_USAGE_CONTEXT]',
            'business_rules': ['[BUSINESS_RULE_1]', '[BUSINESS_RULE_2]'],
            'data_sources': ['[DATA_SOURCE_1]', '[DATA_SOURCE_2]'],
            'quality_requirements': '[QUALITY_REQUIREMENTS]',
            'regulatory_requirements': ['[REGULATION_1]', '[REGULATION_2]'],
            'approval_status': '[APPROVAL_STATUS]',
            'approval_date': '[APPROVAL_DATE]',
            'version': '1.0',
            'change_history': []
        }

        return business_glossary

SCHEMA DOCUMENTATION AUTOMATION:

# Comprehensive schema documentation system
class SchemaDocumentationEngine:
    def __init__(self, config: dict):
        self.config = config
        self.documentation_generator = [DOC_GENERATOR]([DOC_CONFIG])
        self.template_engine = [TEMPLATE_ENGINE]([TEMPLATE_CONFIG])
        self.validation_engine = [VALIDATION_ENGINE]([VALIDATION_CONFIG])

    def generate_comprehensive_documentation(
        self,
        documentation_scope: dict,
        output_formats: list = ['HTML', 'PDF', 'CONFLUENCE']
    ) -> dict:
        """
        Generate comprehensive schema documentation


### Returns
            Documentation generation results
        """

        documentation_results = {
            'generation_metadata': {
                'generation_id': [DOC_GENERATION_ID],
                'generation_timestamp': [CURRENT_TIMESTAMP],
                'scope': documentation_scope,
                'output_formats': output_formats,
                'template_version': '[TEMPLATE_VERSION]'
            },
            'schema_documentation': self.generate_schema_documentation(documentation_scope),
            'api_documentation': self.generate_api_documentation(documentation_scope),
            'data_dictionary': self.generate_data_dictionary_docs(documentation_scope),
            'lineage_documentation': self.generate_lineage_documentation(documentation_scope),
            'governance_documentation': self.generate_governance_documentation(documentation_scope),
            'usage_documentation': self.generate_usage_documentation(documentation_scope),
            'output_files': {}
        }

        # Generate output files in requested formats
        for output_format in output_formats:
            output_result = self.generate_output_format(
                documentation_results,
                output_format
            )
            documentation_results['output_files'][output_format] = output_result

        return documentation_results

    def generate_schema_documentation(self, scope: dict) -> dict:
        """
        Generate detailed schema documentation
        """
        schema_docs = {
            'schema_overview': {},
            'table_documentation': {},
            'relationship_diagrams': {},
            'constraint_documentation': {},
            'index_documentation': {}
        }

        for schema in scope.get('schemas', []):
            schema_id = schema['schema_id']

            # Generate schema overview
            schema_docs['schema_overview'][schema_id] = {
                'schema_name': schema['name'],
                'description': schema.get('description', ''),
                'purpose': schema.get('purpose', ''),
                'owner': schema.get('owner', ''),
                'creation_date': schema.get('creation_date', ''),
                'last_modified': schema.get('last_modified', ''),
                'table_count': len(schema.get('tables', [])),
                'view_count': len(schema.get('views', [])),
                'function_count': len(schema.get('functions', [])),
                'procedure_count': len(schema.get('procedures', [])),
                'dependencies': schema.get('dependencies', []),
                'business_context': schema.get('business_context', ''),
                'usage_patterns': schema.get('usage_patterns', [])
            }

            # Generate table documentation
            schema_docs['table_documentation'][schema_id] = {}
            for table in schema.get('tables', []):
                table_doc = self.generate_table_documentation(table)
                schema_docs['table_documentation'][schema_id][table['name']] = table_doc

            # Generate relationship diagrams
            schema_docs['relationship_diagrams'][schema_id] = self.generate_erd_documentation(schema)

            # Generate constraint documentation
            schema_docs['constraint_documentation'][schema_id] = self.generate_constraint_docs(schema)

        return schema_docs

    def generate_table_documentation(self, table: dict) -> dict:
        """
        Generate comprehensive table documentation
        """
        table_documentation = {
            'table_metadata': {
                'table_name': table['name'],
                'physical_name': table.get('physical_name', table['name']),
                'description': table.get('description', ''),
                'purpose': table.get('purpose', ''),
                'business_owner': table.get('business_owner', ''),
                'technical_owner': table.get('technical_owner', ''),
                'creation_date': table.get('creation_date', ''),
                'last_modified': table.get('last_modified', ''),
                'row_count': table.get('row_count', 0),
                'size_mb': table.get('size_mb', 0),
                'growth_rate': table.get('growth_rate', ''),
                'retention_policy': table.get('retention_policy', ''),
                'update_frequency': table.get('update_frequency', ''),
                'business_criticality': table.get('criticality', 'MEDIUM')
            },
            'column_documentation': self.generate_column_documentation(table.get('columns', [])),
            'relationship_documentation': self.generate_relationship_docs(table),
            'business_rules': table.get('business_rules', []),
            'data_quality_rules': table.get('quality_rules', []),
            'usage_examples': self.generate_usage_examples(table),
            'performance_considerations': self.generate_performance_docs(table),
            'security_considerations': self.generate_security_docs(table),
            'sample_data': self.generate_sample_data_docs(table)
        }

        return table_documentation

    def generate_column_documentation(self, columns: list) -> list:
        """
        Generate detailed column documentation
        """
        column_docs = []

        for column in columns:
            column_doc = {
                # Basic Information
                'column_name': column['name'],
                'physical_name': column.get('physical_name', column['name']),
                'data_type': column['type'],
                'length': column.get('length', ''),
                'precision': column.get('precision', ''),
                'scale': column.get('scale', ''),
                'nullable': column.get('nullable', True),
                'default_value': column.get('default_value', ''),
                'auto_increment': column.get('auto_increment', False),

                # Business Information
                'business_name': column.get('business_name', ''),
                'description': column.get('description', ''),
                'business_definition': column.get('business_definition', ''),
                'calculation_logic': column.get('calculation_logic', ''),
                'derivation_rules': column.get('derivation_rules', []),
                'business_owner': column.get('business_owner', ''),
                'subject_area': column.get('subject_area', ''),
                'glossary_terms': column.get('glossary_terms', []),

                # Technical Information
                'source_system': column.get('source_system', ''),
                'source_table': column.get('source_table', ''),
                'source_column': column.get('source_column', ''),
                'transformation_logic': column.get('transformation_logic', ''),
                'encoding': column.get('encoding', ''),
                'compression': column.get('compression', ''),
                'indexing': column.get('indexes', []),

                # Data Quality Information
                'data_quality_rules': column.get('quality_rules', []),
                'validation_rules': column.get('validation_rules', []),
                'acceptable_values': column.get('acceptable_values', []),
                'format_patterns': column.get('format_patterns', []),
                'completeness_target': column.get('completeness_target', ''),
                'accuracy_target': column.get('accuracy_target', ''),

                # Statistical Information
                'distinct_count': column.get('distinct_count', ''),
                'null_percentage': column.get('null_percentage', ''),
                'min_value': column.get('min_value', ''),
                'max_value': column.get('max_value', ''),
                'avg_value': column.get('avg_value', ''),
                'std_deviation': column.get('std_deviation', ''),
                'most_common_values': column.get('most_common_values', []),
                'value_distribution': column.get('value_distribution', {}),

                # Governance Information
                'classification_level': column.get('classification', ''),
                'sensitivity_tags': column.get('sensitivity_tags', []),
                'privacy_tags': column.get('privacy_tags', []),
                'pii_indicator': column.get('is_pii', False),
                'phi_indicator': column.get('is_phi', False),
                'masking_rules': column.get('masking_rules', []),
                'access_restrictions': column.get('access_restrictions', []),
                'compliance_requirements': column.get('compliance_requirements', []),

                # Usage Information
                'usage_frequency': column.get('usage_frequency', ''),
                'query_patterns': column.get('query_patterns', []),
                'reporting_usage': column.get('reporting_usage', []),
                'analytical_usage': column.get('analytical_usage', []),
                'application_dependencies': column.get('app_dependencies', []),

                # Change Management
                'version_history': column.get('version_history', []),
                'change_requests': column.get('change_requests', []),
                'deprecation_timeline': column.get('deprecation_timeline', ''),
                'migration_instructions': column.get('migration_instructions', ''),

                # Examples and Samples
                'example_values': column.get('example_values', []),
                'invalid_examples': column.get('invalid_examples', []),
                'edge_cases': column.get('edge_cases', []),
                'testing_scenarios': column.get('testing_scenarios', [])
            }

            column_docs.append(column_doc)

        return column_docs

    def generate_automated_documentation_templates(self) -> dict:
        """
        Generate automated documentation templates
        """
        templates = {
            'schema_overview_template': self.create_schema_overview_template(),
            'table_documentation_template': self.create_table_documentation_template(),
            'api_documentation_template': self.create_api_documentation_template(),
            'lineage_report_template': self.create_lineage_report_template(),
            'governance_report_template': self.create_governance_report_template(),
            'data_dictionary_template': self.create_data_dictionary_template(),
            'change_log_template': self.create_change_log_template()
        }

        return templates

    def create_schema_overview_template(self) -> str:
        """
        Create schema overview documentation template
        """
        template = """

# Schema Documentation: {[SCHEMA_NAME]}


## Overview
**Schema Name:** {[SCHEMA_NAME]}
**Description:** {[DESCRIPTION]}
**Owner:** {[OWNER]}
**Business Contact:** {[BUSINESS_CONTACT]}
**Technical Contact:** {[TECHNICAL_CONTACT]}
**Last Updated:** {[LAST_UPDATED]}


## Schema Statistics
- **Total Tables:** {[TABLE_COUNT]}
- **Total Views:** {[VIEW_COUNT]}
- **Total Functions:** {[FUNCTION_COUNT]}
- **Total Procedures:** {[PROCEDURE_COUNT]}
- **Total Storage Size:** {[TOTAL_SIZE_MB]} MB
- **Estimated Row Count:** {[TOTAL_ROWS]}


## Contact Information
- **Schema Owner:** {[OWNER_CONTACT]}
- **Data Steward:** {[STEWARD_CONTACT]}
- **Technical Lead:** {[TECHNICAL_LEAD_CONTACT]}
"""
        return template

# Comprehensive data governance workflow system
class GovernanceWorkflowEngine:
    def __init__(self, config: dict):
        self.config = config
        self.workflow_engine = [WORKFLOW_ENGINE]([WORKFLOW_CONFIG])
        self.approval_system = [APPROVAL_SYSTEM]([APPROVAL_CONFIG])
        self.notification_system = [NOTIFICATION_SYSTEM]([NOTIFICATION_CONFIG])
        self.audit_system = [AUDIT_SYSTEM]([AUDIT_CONFIG])

    def initialize_governance_workflows(self) -> dict:
        """
        Initialize all governance workflows
        """
        workflow_initialization = {
            'data_asset_onboarding': self.create_asset_onboarding_workflow(),
            'schema_change_approval': self.create_schema_change_workflow(),
            'data_access_request': self.create_data_access_workflow(),
            'data_quality_incident': self.create_quality_incident_workflow(),
            'data_classification': self.create_classification_workflow(),
            'data_retention': self.create_retention_workflow(),
            'privacy_impact_assessment': self.create_pia_workflow(),
            'data_lineage_validation': self.create_lineage_validation_workflow()
        }

        return workflow_initialization

    def create_asset_onboarding_workflow(self) -> dict:
        """
        Create data asset onboarding workflow
        """
        onboarding_workflow = {
            'workflow_id': 'DATA_ASSET_ONBOARDING',
            'workflow_name': 'Data Asset Onboarding Process',
            'description': 'Comprehensive workflow for onboarding new data assets',
            'trigger_events': [
                'NEW_DATA_SOURCE_DISCOVERED',
                'MANUAL_ASSET_REGISTRATION',
                'SYSTEM_INTEGRATION_REQUEST'
            ],
            'workflow_steps': [
                {
                    'step_id': 'INITIAL_DISCOVERY',
                    'step_name': 'Initial Asset Discovery',
                    'description': 'Discover and catalog basic asset information',
                    'assigned_role': '[DATA_STEWARD_ROLE]',
                    'automated': True,
                    'duration_hours': 1,
                    'prerequisites': [],
                    'actions': [
                        'extract_basic_metadata',
                        'identify_data_types',
                        'estimate_data_volume',
                        'identify_potential_owners'
                    ],
                    'outputs': [
                        'initial_asset_profile',
                        'metadata_discovery_report'
                    ]
                },
                {
                    'step_id': 'BUSINESS_CONTEXT_GATHERING',
                    'step_name': 'Business Context Assessment',
                    'description': 'Gather business context and ownership information',
                    'assigned_role': '[BUSINESS_ANALYST_ROLE]',
                    'automated': False,
                    'duration_hours': 8,
                    'prerequisites': ['INITIAL_DISCOVERY'],
                    'actions': [
                        'identify_business_owner',
                        'document_business_purpose',
                        'define_business_glossary_terms',
                        'assess_business_criticality'
                    ],
                    'outputs': [
                        'business_context_document',
                        'owner_assignment'
                    ]
                },
                {
                    'step_id': 'TECHNICAL_ASSESSMENT',
                    'step_name': 'Technical Assessment',
                    'description': 'Perform detailed technical assessment',
                    'assigned_role': '[DATA_ENGINEER_ROLE]',
                    'automated': False,
                    'duration_hours': 4,
                    'prerequisites': ['INITIAL_DISCOVERY'],
                    'actions': [
                        'validate_technical_metadata',
                        'assess_data_quality',
                        'identify_integration_requirements',
                        'document_technical_constraints'
                    ],
                    'outputs': [
                        'technical_assessment_report',
                        'integration_requirements'
                    ]
                },
                {
                    'step_id': 'CLASSIFICATION_AND_TAGGING',
                    'step_name': 'Data Classification',
                    'description': 'Classify data and apply appropriate tags',
                    'assigned_role': '[DATA_PRIVACY_OFFICER_ROLE]',
                    'automated': False,
                    'duration_hours': 2,
                    'prerequisites': ['BUSINESS_CONTEXT_GATHERING', 'TECHNICAL_ASSESSMENT'],
                    'actions': [
                        'classify_data_sensitivity',
                        'identify_pii_phi_data',
                        'apply_compliance_tags',
                        'define_access_restrictions'
                    ],
                    'outputs': [
                        'data_classification_report',
                        'compliance_assessment'
                    ]
                },
                {
                    'step_id': 'GOVERNANCE_APPROVAL',
                    'step_name': 'Governance Committee Approval',
                    'description': 'Review and approve asset onboarding',
                    'assigned_role': '[GOVERNANCE_COMMITTEE_ROLE]',
                    'automated': False,
                    'duration_hours': 24,
                    'prerequisites': ['CLASSIFICATION_AND_TAGGING'],
                    'actions': [
                        'review_onboarding_package',
                        'validate_compliance_requirements',
                        'approve_or_reject_onboarding'
                    ],
                    'outputs': [
                        'approval_decision',
                        'governance_feedback'
                    ],
                    'approval_required': True
                },
                {
                    'step_id': 'ASSET_REGISTRATION',
                    'step_name': 'Final Asset Registration',
                    'description': 'Register asset in governance systems',
                    'assigned_role': '[DATA_STEWARD_ROLE]',
                    'automated': True,
                    'duration_hours': 1,
                    'prerequisites': ['GOVERNANCE_APPROVAL'],
                    'actions': [
                        'register_in_data_catalog',
                        'setup_monitoring_alerts',
                        'configure_access_controls',
                        'initialize_lineage_tracking'
                    ],
                    'outputs': [
                        'asset_registration_confirmation',
                        'monitoring_setup_confirmation'
                    ]
                }
            ],
            'escalation_rules': [
                {
                    'condition': 'step_overdue_24_hours',
                    'action': 'notify_manager',
                    'severity': 'MEDIUM'
                },
                {
                    'condition': 'step_overdue_72_hours',
                    'action': 'escalate_to_governance_committee',
                    'severity': 'HIGH'
                }
            ],
            'notification_rules': [
                {
                    'trigger': 'workflow_started',
                    'recipients': ['assigned_steward', 'business_owner'],
                    'template': 'onboarding_started_notification'
                },
                {
                    'trigger': 'approval_required',
                    'recipients': ['governance_committee'],
                    'template': 'approval_required_notification'
                },
                {
                    'trigger': 'workflow_completed',
                    'recipients': ['all_stakeholders'],
                    'template': 'onboarding_completed_notification'
                }
            ]
        }

        return onboarding_workflow

    def create_data_access_workflow(self) -> dict:
        """
        Create data access request workflow
        """
        access_workflow = {
            'workflow_id': 'DATA_ACCESS_REQUEST',
            'workflow_name': 'Data Access Request Process',
            'description': 'Workflow for processing data access requests',
            'trigger_events': [
                'ACCESS_REQUEST_SUBMITTED',

[Content truncated for length - see original for full details]


## Variables

[GOVERNANCE_METHODOLOGY], [ORGANIZATION_NAME], [GOVERNANCE_OBJECTIVES], [GOVERNANCE_APPROACH], [GOVERNANCE_TOOLS], [INDUSTRY_SECTOR], [GOVERNANCE_MATURITY_LEVEL], [REGULATORY_REQUIREMENTS], [DATA_DOMAINS], [STAKEHOLDER_GROUPS], [GEOGRAPHIC_SCOPE], [BUSINESS_DRIVERS], [IMPLEMENTATION_MODEL], [METADATA_STRATEGY], [LINEAGE_TRACKING_APPROACH], [DOCUMENTATION_STANDARDS], [QUALITY_ASSURANCE_MODEL], [GOVERNANCE_PLATFORM], [METADATA_REPOSITORY], [LINEAGE_TRACKING_TOOLS], [DOCUMENTATION_PLATFORM], [WORKFLOW_MANAGEMENT_SYSTEM], [POLICY_ENFORCEMENT_SYSTEM], [ACCESS_CONTROL_SYSTEM], [AUDIT_MONITORING_SYSTEM], [DATA_ASSETS_COVERAGE], [SYSTEM_INTEGRATION_SCOPE], [USER_BASE_SIZE], [GOVERNANCE_DATA_VOLUME], [GOVERNANCE_COMPLEXITY], [GOVERNANCE_AUTOMATION_LEVEL], [GOVERNANCE_UPDATE_FREQUENCY], [RETENTION_REQUIREMENTS], [METADATA_LIBRARY], [METADATA_ALIAS], [GOVERNANCE_FRAMEWORK], [GOVERNANCE_COMPONENTS], [LINEAGE_LIBRARY], [LINEAGE_TRACKER], [METADATA_REPO_CONFIG], [SCHEMA_REGISTRY], [SCHEMA_CONFIG], [LINEAGE_CONFIG], [GOV_CONFIG], [ASSET_ID_GENERATOR], [CURRENT_TIMESTAMP], [COMPLETENESS_THRESHOLD], [DICTIONARY_ID_GENERATOR], [DICTIONARY_UPDATE_FREQUENCY], [CATEGORY_1], [CATEGORY_1_DESCRIPTION], [CATEGORY_1_OWNER], [CATEGORY_2], [CATEGORY_2_DESCRIPTION], [CATEGORY_2_OWNER], [TERM_ID], [BUSINESS_TERM_NAME], [BUSINESS_TERM_DEFINITION], [TERM_CATEGORY], [SYNONYM_1], [SYNONYM_2], [RELATED_TERM_1], [RELATED_TERM_2], [TERM_BUSINESS_OWNER], [TERM_DATA_STEWARD], [EXAMPLE_1], [EXAMPLE_2], [TERM_USAGE_CONTEXT], [BUSINESS_RULE_1], [BUSINESS_RULE_2], [DATA_SOURCE_1], [DATA_SOURCE_2], [QUALITY_REQUIREMENTS], [REGULATION_1], [REGULATION_2], [APPROVAL_STATUS], [APPROVAL_DATE], [LINEAGE_REPO], [LINEAGE_REPO_CONFIG], [GRAPH_DATABASE], [GRAPH_CONFIG], [PARSER_ENGINE], [PARSER_CONFIG], [IMPACT_ANALYZER], [IMPACT_CONFIG], [LINEAGE_DISCOVERY_ID], [LOGGING_SYSTEM], [CENTRAL_NODE_COLOR], [CENTRAL_NODE_SIZE], [CENTRAL_NODE_SHAPE], [UPSTREAM_NODE_COLOR], [UPSTREAM_NODE_SIZE], [UPSTREAM_NODE_SHAPE], [DOWNSTREAM_NODE_COLOR], [DOWNSTREAM_NODE_SIZE], [DOWNSTREAM_NODE_SHAPE], [TRACKING_PERIOD], [DOC_GENERATOR], [DOC_CONFIG], [TEMPLATE_ENGINE], [TEMPLATE_CONFIG], [VALIDATION_ENGINE], [VALIDATION_CONFIG], [DOC_GENERATION_ID], [TEMPLATE_VERSION], [WORKFLOW_ENGINE], [WORKFLOW_CONFIG], [APPROVAL_SYSTEM], [APPROVAL_CONFIG], [NOTIFICATION_SYSTEM], [NOTIFICATION_CONFIG], [AUDIT_SYSTEM], [AUDIT_CONFIG], [DATA_STEWARD_ROLE], [BUSINESS_ANALYST_ROLE], [DATA_ENGINEER_ROLE], [DATA_PRIVACY_OFFICER_ROLE], [GOVERNANCE_COMMITTEE_ROLE], [ACCESS_REQUEST_COORDINATOR], [DATA_OWNER], [DATA_PRIVACY_OFFICER], [SECURITY_OFFICER], [DATA_STEWARD], [POLICY_REPO], [POLICY_CONFIG], [RULE_ENGINE], [RULE_CONFIG], [COMPLIANCE_MONITOR], [COMPLIANCE_CONFIG], [POLICY_EFFECTIVE_DATE], [POLICY_REVIEW_DATE], [POLICY_OWNER], [APPROVAL_AUTHORITY], [INTERNAL_RETENTION_PERIOD], [CONFIDENTIAL_RETENTION_PERIOD], [RESTRICTED_RETENTION_PERIOD], [LAYOUT_ALGORITHM]

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
