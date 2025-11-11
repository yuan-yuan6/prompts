---
title: Analytics Process & Governance Documentation
category: data-analytics/Analytics Engineering
tags: ['documentation', 'governance', 'processes', 'standards']
use_cases:
  - Document analytics processes, workflows, governance policies, standards, and best practices for data analytics operations.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Analytics Process & Governance Documentation

## Purpose
Document analytics processes, workflows, governance policies, standards, and best practices for data analytics operations.

## Quick Start

### For Professionals

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific needs for document
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
- Document analytics processes, workflows, governance policies, standards, and best practices for data analytics operations.
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


# Documentation, Lineage & Governance Template


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


You are a data governance architect specializing in [GOVERNANCE_METHODOLOGY]. Design a comprehensive data documentation, lineage tracking, and governance framework for [ORGANIZATION_NAME] to ensure [GOVERNANCE_OBJECTIVES] using [GOVERNANCE_APPROACH] and [GOVERNANCE_TOOLS].

DATA GOVERNANCE FRAMEWORK OVERVIEW:

- Data governance maturity: [GOVERNANCE_MATURITY_LEVEL]

- Governance objectives: [GOVERNANCE_OBJECTIVES]

### Governance Strategy

- Governance methodology: [GOVERNANCE_METHODOLOGY] (Centralized/Federated/Decentralized/Hybrid)

- Governance approach: [GOVERNANCE_APPROACH] (Policy-driven/Risk-based/Value-driven/Compliance-focused)

- Governance tools: [GOVERNANCE_TOOLS]

- Documentation standards: [DOCUMENTATION_STANDARDS]

- Governance platform: [GOVERNANCE_PLATFORM]

- Workflow management: [WORKFLOW_MANAGEMENT_SYSTEM]

### Governance Scope

- Data volume: [GOVERNANCE_DATA_VOLUME]

- Complexity level: [GOVERNANCE_COMPLEXITY]

- Automation level: [GOVERNANCE_AUTOMATION_LEVEL]

- Update frequency: [GOVERNANCE_UPDATE_FREQUENCY]

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

### Returns
            Lineage discovery results
        """

        lineage_results = {
            'discovery_metadata': {
                'discovery_id': [LINEAGE_DISCOVERY_ID],
                'discovery_timestamp': [CURRENT_TIMESTAMP],
                'discovery_method': discovery_method,
                'discovery_scope': discovery_scope,
                'coverage_statistics': {}
            },
            'system_lineage': self.discover_system_level_lineage(discovery_scope),
            'table_lineage': self.discover_table_level_lineage(discovery_scope),
            'column_lineage': self.discover_column_level_lineage(discovery_scope),
            'transformation_lineage': self.discover_transformation_lineage(discovery_scope),
            'process_lineage': self.discover_process_lineage(discovery_scope),
            'impact_analysis': self.perform_impact_analysis(discovery_scope),
            'lineage_gaps': self.identify_lineage_gaps(discovery_scope),
            'recommendations': self.generate_lineage_recommendations()
        }

        # Store lineage in graph database
        self.store_lineage_graph(lineage_results)

        return lineage_results

    def discover_system_level_lineage(self, scope: dict) -> dict:
        """
        Discover lineage at system level
        """
        system_lineage = {
            'source_systems': [],
            'target_systems': [],
            'integration_flows': [],
            'system_dependencies': {},
            'data_movement_patterns': {}
        }

        # Discover source systems
        for system in scope.get('systems', []):
            system_info = {
                'system_id': system['id'],
                'system_name': system['name'],
                'system_type': system['type'],
                'technology_stack': system.get('technology', []),
                'data_outputs': self.discover_system_outputs(system),
                'data_inputs': self.discover_system_inputs(system),
                'integration_patterns': self.analyze_integration_patterns(system),
                'update_frequency': system.get('update_frequency'),
                'business_criticality': system.get('criticality', 'MEDIUM'),
                'operational_status': system.get('status', 'ACTIVE')
            }

            if system_info['data_outputs']:
                system_lineage['source_systems'].append(system_info)
            if system_info['data_inputs']:
                system_lineage['target_systems'].append(system_info)

        # Map integration flows
        system_lineage['integration_flows'] = self.map_integration_flows(
            system_lineage['source_systems'],
            system_lineage['target_systems']
        )

        return system_lineage

    def discover_column_level_lineage(self, scope: dict) -> dict:
        """
        Discover fine-grained column-level lineage
        """
        column_lineage = {
            'column_mappings': [],
            'transformation_logic': {},
            'derivation_rules': {},
            'column_dependencies': {}
        }

        # Process SQL-based transformations
        if 'sql_sources' in scope:
            for sql_source in scope['sql_sources']:
                parsed_lineage = self.parse_sql_lineage(sql_source)
                column_lineage['column_mappings'].extend(parsed_lineage['column_mappings'])
                column_lineage['transformation_logic'].update(parsed_lineage['transformations'])

        # Process ETL tool lineage
        if 'etl_sources' in scope:
            for etl_source in scope['etl_sources']:
                etl_lineage = self.extract_etl_lineage(etl_source)
                column_lineage['column_mappings'].extend(etl_lineage['mappings'])

        # Process API-based lineage
        if 'api_sources' in scope:
            for api_source in scope['api_sources']:
                api_lineage = self.discover_api_lineage(api_source)
                column_lineage['column_mappings'].extend(api_lineage['field_mappings'])

        return column_lineage

    def parse_sql_lineage(self, sql_source: dict) -> dict:
        """
        Parse SQL statements to extract column-level lineage
        """
        sql_statements = sql_source.get('sql_statements', [])
        lineage_results = {
            'column_mappings': [],
            'transformations': {}
        }

        for statement in sql_statements:
            try:
                # Parse SQL using advanced SQL parser
                parsed_query = self.parser_engine.parse_sql(statement['sql'])

                # Extract SELECT clause lineage
                select_lineage = self.extract_select_lineage(parsed_query)
                lineage_results['column_mappings'].extend(select_lineage)

                # Extract WHERE clause dependencies
                where_dependencies = self.extract_where_dependencies(parsed_query)

                # Extract JOIN relationships
                join_relationships = self.extract_join_relationships(parsed_query)

                # Extract transformation logic
                transformations = self.extract_transformation_logic(parsed_query)
                lineage_results['transformations'].update(transformations)

                # Create detailed lineage mapping
                for mapping in select_lineage:
                    detailed_mapping = {
                        'source_database': mapping.get('source_database'),
                        'source_schema': mapping.get('source_schema'),
                        'source_table': mapping.get('source_table'),
                        'source_column': mapping.get('source_column'),
                        'target_database': statement.get('target_database'),
                        'target_schema': statement.get('target_schema'),
                        'target_table': statement.get('target_table'),
                        'target_column': mapping.get('target_column'),
                        'transformation_type': mapping.get('transformation_type', 'DIRECT_COPY'),
                        'transformation_expression': mapping.get('expression'),
                        'transformation_function': mapping.get('function_used'),
                        'aggregation_applied': mapping.get('aggregation_applied', False),
                        'filter_conditions': where_dependencies,
                        'join_conditions': join_relationships,
                        'confidence_score': mapping.get('confidence', 1.0),
                        'parsing_method': 'SQL_PARSER',
                        'statement_id': statement.get('statement_id'),
                        'discovery_timestamp': [CURRENT_TIMESTAMP]
                    }

                    lineage_results['column_mappings'].append(detailed_mapping)

            except Exception as e:
                # Log parsing errors and continue
                [LOGGING_SYSTEM].log_error(
                    f"SQL parsing error: {str(e)}",
                    statement_id=statement.get('statement_id')
                )

        return lineage_results

    def perform_impact_analysis(self, scope: dict) -> dict:
        """
        Perform comprehensive impact analysis
        """
        impact_analysis = {
            'downstream_impact': {},
            'upstream_dependencies': {},
            'critical_path_analysis': {},
            'change_impact_matrix': {},
            'business_impact_assessment': {}
        }

        # Analyze downstream impact
        for asset in scope.get('assets', []):
            asset_id = asset['asset_id']

            downstream_assets = self.find_downstream_assets(asset_id)
            impact_analysis['downstream_impact'][asset_id] = {
                'directly_impacted': downstream_assets.get('direct', []),
                'indirectly_impacted': downstream_assets.get('indirect', []),
                'impact_levels': self.calculate_impact_levels(downstream_assets),
                'business_functions_affected': self.identify_affected_business_functions(downstream_assets),
                'estimated_users_affected': self.estimate_affected_users(downstream_assets),
                'estimated_recovery_time': self.estimate_recovery_time(downstream_assets)
            }

            # Analyze upstream dependencies
            upstream_assets = self.find_upstream_assets(asset_id)
            impact_analysis['upstream_dependencies'][asset_id] = {
                'direct_dependencies': upstream_assets.get('direct', []),
                'indirect_dependencies': upstream_assets.get('indirect', []),
                'dependency_criticality': self.assess_dependency_criticality(upstream_assets),
                'single_points_of_failure': self.identify_single_points_of_failure(upstream_assets),
                'dependency_health_score': self.calculate_dependency_health(upstream_assets)
            }

        return impact_analysis

    def generate_lineage_visualization(
        self,
        asset_id: str,
        visualization_type: str = 'INTERACTIVE_GRAPH',
        depth_levels: int = 3
    ) -> dict:
        """
        Generate comprehensive lineage visualization


## Schema Statistics
- **Total Tables:** {[TABLE_COUNT]}
- **Total Views:** {[VIEW_COUNT]}
- **Total Functions:** {[FUNCTION_COUNT]}
- **Total Procedures:** {[PROCEDURE_COUNT]}
- **Total Storage Size:** {[TOTAL_SIZE_MB]} MB
- **Estimated Row Count:** {[TOTAL_ROWS]}


GOVERNANCE WORKFLOWS:

Automated Governance Processes:
```python

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
                'ACCESS_LEVEL_CHANGE_REQUESTED',
                'EMERGENCY_ACCESS_REQUESTED'
            ],
            'workflow_steps': [
                {
                    'step_id': 'REQUEST_INTAKE',
                    'step_name': 'Request Intake and Validation',
                    'description': 'Validate access request completeness',
                    'assigned_role': '[ACCESS_REQUEST_COORDINATOR]',
                    'automated': True,
                    'duration_hours': 1,
                    'actions': [
                        'validate_request_completeness',
                        'verify_requestor_identity',
                        'check_existing_access_levels',
                        'assess_request_urgency'
                    ]
                },
                {
                    'step_id': 'BUSINESS_JUSTIFICATION_REVIEW',
                    'step_name': 'Business Justification Review',
                    'description': 'Review business justification for access',
                    'assigned_role': '[DATA_OWNER]',
                    'automated': False,
                    'duration_hours': 24,
                    'actions': [
                        'review_business_justification',
                        'validate_data_usage_purpose',
                        'assess_access_duration_appropriateness',
                        'recommend_minimal_access_principle'
                    ]
                },
                {
                    'step_id': 'PRIVACY_IMPACT_ASSESSMENT',
                    'step_name': 'Privacy Impact Assessment',
                    'description': 'Assess privacy implications of data access',
                    'assigned_role': '[DATA_PRIVACY_OFFICER]',
                    'automated': False,
                    'duration_hours': 8,
                    'conditions': [
                        'access_includes_pii',
                        'access_includes_sensitive_data'
                    ],
                    'actions': [
                        'assess_privacy_risks',
                        'validate_lawful_basis',
                        'recommend_privacy_safeguards',
                        'document_privacy_assessment'
                    ]
                },
                {
                    'step_id': 'SECURITY_REVIEW',
                    'step_name': 'Security Assessment',
                    'description': 'Review security implications',
                    'assigned_role': '[SECURITY_OFFICER]',
                    'automated': False,
                    'duration_hours': 4,
                    'actions': [
                        'assess_security_risks',
                        'validate_access_controls',
                        'recommend_additional_safeguards',
                        'approve_or_modify_access_level'
                    ]
                },
                {
                    'step_id': 'FINAL_APPROVAL',
                    'step_name': 'Final Access Approval',
                    'description': 'Final approval and access provisioning',
                    'assigned_role': '[DATA_STEWARD]',
                    'automated': True,
                    'duration_hours': 2,
                    'actions': [
                        'provision_data_access',
                        'setup_access_monitoring',
                        'schedule_access_review',
                        'notify_stakeholders'
                    ]
                }
            ],
            'approval_matrix': {
                'PUBLIC_DATA': ['data_steward'],
                'INTERNAL_DATA': ['data_owner', 'data_steward'],
                'CONFIDENTIAL_DATA': ['data_owner', 'privacy_officer', 'data_steward'],
                'RESTRICTED_DATA': ['data_owner', 'privacy_officer', 'security_officer', 'governance_committee']
            },
            'sla_requirements': {
                'STANDARD_REQUEST': '5_business_days',
                'URGENT_REQUEST': '2_business_days',
                'EMERGENCY_REQUEST': '4_hours'
            }
        }

        return access_workflow


# Data governance policy engine
class GovernancePolicyEngine:
    def __init__(self, config: dict):
        self.config = config
        self.policy_repository = [POLICY_REPO]([POLICY_CONFIG])
        self.rule_engine = [RULE_ENGINE]([RULE_CONFIG])
        self.compliance_monitor = [COMPLIANCE_MONITOR]([COMPLIANCE_CONFIG])

    def define_governance_policies(self) -> dict:
        """
        Define comprehensive data governance policies
        """
        governance_policies = {
            'data_classification_policy': self.create_data_classification_policy(),
            'data_access_policy': self.create_data_access_policy(),
            'data_retention_policy': self.create_data_retention_policy(),
            'data_quality_policy': self.create_data_quality_policy(),
            'data_privacy_policy': self.create_data_privacy_policy(),
            'data_security_policy': self.create_data_security_policy(),
            'data_lineage_policy': self.create_data_lineage_policy(),
            'metadata_management_policy': self.create_metadata_policy()
        }

        return governance_policies

    def create_data_classification_policy(self) -> dict:
        """
        Create comprehensive data classification policy
        """
        classification_policy = {
            'policy_id': 'DATA_CLASSIFICATION_001',
            'policy_name': 'Data Classification and Sensitivity Labeling Policy',
            'version': '1.0',
            'effective_date': '[POLICY_EFFECTIVE_DATE]',
            'review_date': '[POLICY_REVIEW_DATE]',
            'policy_owner': '[POLICY_OWNER]',
            'approval_authority': '[APPROVAL_AUTHORITY]',

            'policy_statement': '''
            All data assets within the organization must be classified according to their
            sensitivity level and business criticality to ensure appropriate protection
            and governance controls are applied.
            ''',

            'classification_levels': {
                'PUBLIC': {
                    'description': 'Data that can be freely shared publicly without harm',
                    'examples': ['Marketing materials', 'Public reports', 'Press releases'],
                    'protection_requirements': 'Basic integrity protection',
                    'access_controls': 'No restrictions',
                    'retention_period': 'As per business need',
                    'disposal_method': 'Standard deletion'
                },
                'INTERNAL': {
                    'description': 'Data for internal use within the organization',
                    'examples': ['Internal reports', 'Employee directories', 'Process documents'],
                    'protection_requirements': 'Standard security controls',
                    'access_controls': 'Authenticated organization members',
                    'retention_period': '[INTERNAL_RETENTION_PERIOD]',
                    'disposal_method': 'Secure deletion'
                },
                'CONFIDENTIAL': {
                    'description': 'Sensitive data requiring protection from unauthorized access',
                    'examples': ['Customer data', 'Financial information', 'Strategic plans'],
                    'protection_requirements': 'Enhanced security controls and encryption',
                    'access_controls': 'Role-based access with business justification',
                    'retention_period': '[CONFIDENTIAL_RETENTION_PERIOD]',
                    'disposal_method': 'Certified secure destruction'
                },
                'RESTRICTED': {
                    'description': 'Highly sensitive data with severe impact if compromised',
                    'examples': ['PII', 'PHI', 'Payment card data', 'Trade secrets'],
                    'protection_requirements': 'Maximum security controls and monitoring',
                    'access_controls': 'Strict need-to-know with approval workflow',
                    'retention_period': '[RESTRICTED_RETENTION_PERIOD]',
                    'disposal_method': 'Certified secure destruction with audit trail'
                }
            },


[Content truncated for length - see original for full details]


## Variables

[GOVERNANCE_METHODOLOGY], [ORGANIZATION_NAME], [GOVERNANCE_OBJECTIVES], [GOVERNANCE_APPROACH], [GOVERNANCE_TOOLS], [INDUSTRY_SECTOR], [GOVERNANCE_MATURITY_LEVEL], [REGULATORY_REQUIREMENTS], [DATA_DOMAINS], [STAKEHOLDER_GROUPS], [GEOGRAPHIC_SCOPE], [BUSINESS_DRIVERS], [IMPLEMENTATION_MODEL], [METADATA_STRATEGY], [LINEAGE_TRACKING_APPROACH], [DOCUMENTATION_STANDARDS], [QUALITY_ASSURANCE_MODEL], [GOVERNANCE_PLATFORM], [METADATA_REPOSITORY], [LINEAGE_TRACKING_TOOLS], [DOCUMENTATION_PLATFORM], [WORKFLOW_MANAGEMENT_SYSTEM], [POLICY_ENFORCEMENT_SYSTEM], [ACCESS_CONTROL_SYSTEM], [AUDIT_MONITORING_SYSTEM], [DATA_ASSETS_COVERAGE], [SYSTEM_INTEGRATION_SCOPE], [USER_BASE_SIZE], [GOVERNANCE_DATA_VOLUME], [GOVERNANCE_COMPLEXITY], [GOVERNANCE_AUTOMATION_LEVEL], [GOVERNANCE_UPDATE_FREQUENCY], [RETENTION_REQUIREMENTS], [METADATA_LIBRARY], [METADATA_ALIAS], [GOVERNANCE_FRAMEWORK], [GOVERNANCE_COMPONENTS], [LINEAGE_LIBRARY], [LINEAGE_TRACKER], [METADATA_REPO_CONFIG], [SCHEMA_REGISTRY], [SCHEMA_CONFIG], [LINEAGE_CONFIG], [GOV_CONFIG], [ASSET_ID_GENERATOR], [CURRENT_TIMESTAMP], [COMPLETENESS_THRESHOLD], [DICTIONARY_ID_GENERATOR], [DICTIONARY_UPDATE_FREQUENCY], [CATEGORY_1], [CATEGORY_1_DESCRIPTION], [CATEGORY_1_OWNER], [CATEGORY_2], [CATEGORY_2_DESCRIPTION], [CATEGORY_2_OWNER], [TERM_ID], [BUSINESS_TERM_NAME], [BUSINESS_TERM_DEFINITION], [TERM_CATEGORY], [SYNONYM_1], [SYNONYM_2], [RELATED_TERM_1], [RELATED_TERM_2], [TERM_BUSINESS_OWNER], [TERM_DATA_STEWARD], [EXAMPLE_1], [EXAMPLE_2], [TERM_USAGE_CONTEXT], [BUSINESS_RULE_1], [BUSINESS_RULE_2], [DATA_SOURCE_1], [DATA_SOURCE_2], [QUALITY_REQUIREMENTS], [REGULATION_1], [REGULATION_2], [APPROVAL_STATUS], [APPROVAL_DATE], [LINEAGE_REPO], [LINEAGE_REPO_CONFIG], [GRAPH_DATABASE], [GRAPH_CONFIG], [PARSER_ENGINE], [PARSER_CONFIG], [IMPACT_ANALYZER], [IMPACT_CONFIG], [LINEAGE_DISCOVERY_ID], [LOGGING_SYSTEM], [CENTRAL_NODE_COLOR], [CENTRAL_NODE_SIZE], [CENTRAL_NODE_SHAPE], [UPSTREAM_NODE_COLOR], [UPSTREAM_NODE_SIZE], [UPSTREAM_NODE_SHAPE], [DOWNSTREAM_NODE_COLOR], [DOWNSTREAM_NODE_SIZE], [DOWNSTREAM_NODE_SHAPE], [TRACKING_PERIOD], [DOC_GENERATOR], [DOC_CONFIG], [TEMPLATE_ENGINE], [TEMPLATE_CONFIG], [VALIDATION_ENGINE], [VALIDATION_CONFIG], [DOC_GENERATION_ID], [TEMPLATE_VERSION], [WORKFLOW_ENGINE], [WORKFLOW_CONFIG], [APPROVAL_SYSTEM], [APPROVAL_CONFIG], [NOTIFICATION_SYSTEM], [NOTIFICATION_CONFIG], [AUDIT_SYSTEM], [AUDIT_CONFIG], [DATA_STEWARD_ROLE], [BUSINESS_ANALYST_ROLE], [DATA_ENGINEER_ROLE], [DATA_PRIVACY_OFFICER_ROLE], [GOVERNANCE_COMMITTEE_ROLE], [ACCESS_REQUEST_COORDINATOR], [DATA_OWNER], [DATA_PRIVACY_OFFICER], [SECURITY_OFFICER], [DATA_STEWARD], [POLICY_REPO], [POLICY_CONFIG], [RULE_ENGINE], [RULE_CONFIG], [COMPLIANCE_MONITOR], [COMPLIANCE_CONFIG], [POLICY_EFFECTIVE_DATE], [POLICY_REVIEW_DATE], [POLICY_OWNER], [APPROVAL_AUTHORITY], [INTERNAL_RETENTION_PERIOD], [CONFIDENTIAL_RETENTION_PERIOD], [RESTRICTED_RETENTION_PERIOD], [LAYOUT_ALGORITHM]

## Usage Examples

### Example 1: Financial Services Governance
```
GOVERNANCE_METHODOLOGY: "Centralized governance with federated execution"
ORGANIZATION_NAME: "Global Investment Bank"
GOVERNANCE_APPROACH: "Compliance-focused with risk-based prioritization"
GOVERNANCE_OBJECTIVES: "Ensure regulatory compliance and reduce operational risk"
REGULATORY_REQUIREMENTS: ["SOX", "GDPR", "BCBS 239", "CCAR", "FRTB"]
GOVERNANCE_MATURITY_LEVEL: "Defined (Level 3)"
DATA_DOMAINS: ["Trading", "Risk Management", "Customer Data", "Regulatory Reporting"]
STAKEHOLDER_GROUPS: ["Risk Officers", "Compliance", "IT", "Business Units"]
```


### Example 2: Healthcare Data Governance
```
GOVERNANCE_METHODOLOGY: "Hybrid governance model"
ORGANIZATION_NAME: "Regional Health System"
GOVERNANCE_APPROACH: "Privacy-focused with clinical quality emphasis"
GOVERNANCE_OBJECTIVES: "Protect patient privacy while enabling clinical insights"
REGULATORY_REQUIREMENTS: ["HIPAA", "HITECH", "FDA 21 CFR Part 11", "State Privacy Laws"]
GOVERNANCE_MATURITY_LEVEL: "Managed (Level 4)"
DATA_DOMAINS: ["Electronic Health Records", "Medical Imaging", "Claims", "Research"]
GEOGRAPHIC_SCOPE: "Multi-state operations with varying regulations"
```


### Example 3: Technology Company Governance
```
GOVERNANCE_METHODOLOGY: "Decentralized with automated enforcement"
ORGANIZATION_NAME: "CloudTech Solutions"
GOVERNANCE_APPROACH: "Value-driven with innovation enablement"
GOVERNANCE_OBJECTIVES: "Enable data-driven innovation while managing privacy risks"
REGULATORY_REQUIREMENTS: ["GDPR", "CCPA", "SOC 2", "ISO 27001"]
GOVERNANCE_AUTOMATION_LEVEL: "Highly Automated (80%+)"
DATA_DOMAINS: ["Customer Analytics", "Product Telemetry", "Marketing", "Operations"]
IMPLEMENTATION_MODEL: "Bottom-up with executive oversight"
```


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
