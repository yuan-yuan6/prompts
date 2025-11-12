---
category: data-analytics/Analytics-Engineering
last_updated: 2025-11-09
related_templates:
- data-analytics/dashboard-design-patterns.md
- data-analytics/data-governance-framework.md
- data-analytics/predictive-modeling-framework.md
tags:
- automation
- data-analytics
- design
- documentation
- ai-ml
- management
- security
title: Documentation, Lineage & Governance Template
use_cases:
- Creating design comprehensive data governance frameworks including data lineage
  tracking systems, data dictionary management, schema documentation automation, metadata
  management, and enterprise data governance programs for modern data platforms.
- Project planning and execution
- Strategy development
industries:
- finance
- government
- healthcare
- manufacturing
- retail
- technology
---

# Documentation, Lineage & Governance Template

## Purpose
Design comprehensive data governance frameworks including data lineage tracking systems, data dictionary management, schema documentation automation, metadata management, and enterprise data governance programs for modern data platforms.

## Quick Start

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

## Template

```
You are a data governance architect specializing in [GOVERNANCE_METHODOLOGY]. Design a comprehensive data documentation, lineage tracking, and governance framework for [ORGANIZATION_NAME] to ensure [GOVERNANCE_OBJECTIVES] using [GOVERNANCE_APPROACH] and [GOVERNANCE_TOOLS].

DATA GOVERNANCE FRAMEWORK OVERVIEW:
Organizational Context:
- Organization: [ORGANIZATION_NAME]
- Industry sector: [INDUSTRY_SECTOR]
- Data governance maturity: [GOVERNANCE_MATURITY_LEVEL]
- Governance objectives: [GOVERNANCE_OBJECTIVES]
- Regulatory requirements: [REGULATORY_REQUIREMENTS]
- Data domains: [DATA_DOMAINS]
- Stakeholder groups: [STAKEHOLDER_GROUPS]
- Geographic scope: [GEOGRAPHIC_SCOPE]
- Business drivers: [BUSINESS_DRIVERS]

### Governance Strategy
- Governance methodology: [GOVERNANCE_METHODOLOGY] (Centralized/Federated/Decentralized/Hybrid)
- Governance approach: [GOVERNANCE_APPROACH] (Policy-driven/Risk-based/Value-driven/Compliance-focused)
- Implementation model: [IMPLEMENTATION_MODEL] (Top-down/Bottom-up/Middle-out)
- Governance tools: [GOVERNANCE_TOOLS]
- Metadata strategy: [METADATA_STRATEGY]
- Lineage tracking approach: [LINEAGE_TRACKING_APPROACH]
- Documentation standards: [DOCUMENTATION_STANDARDS]
- Quality assurance model: [QUALITY_ASSURANCE_MODEL]

### Technical Architecture
- Governance platform: [GOVERNANCE_PLATFORM]
- Metadata repository: [METADATA_REPOSITORY]
- Lineage tracking tools: [LINEAGE_TRACKING_TOOLS]
- Documentation platform: [DOCUMENTATION_PLATFORM]
- Workflow management: [WORKFLOW_MANAGEMENT_SYSTEM]
- Policy enforcement: [POLICY_ENFORCEMENT_SYSTEM]
- Access control system: [ACCESS_CONTROL_SYSTEM]
- Audit and monitoring: [AUDIT_MONITORING_SYSTEM]

### Governance Scope
- Data assets coverage: [DATA_ASSETS_COVERAGE]
- System integration scope: [SYSTEM_INTEGRATION_SCOPE]
- User base size: [USER_BASE_SIZE]
- Data volume: [GOVERNANCE_DATA_VOLUME]
- Complexity level: [GOVERNANCE_COMPLEXITY]
- Automation level: [GOVERNANCE_AUTOMATION_LEVEL]
- Update frequency: [GOVERNANCE_UPDATE_FREQUENCY]
- Retention requirements: [RETENTION_REQUIREMENTS]

### METADATA MANAGEMENT FRAMEWORK
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

### Args
            data_sources: List of data sources to register

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

### Args
            asset_info: Data asset information
            discovery_method: Method used for discovery (AUTOMATED/MANUAL)

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

### Args
            scope: Dictionary scope (ENTERPRISE/DOMAIN/SYSTEM)

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
```

DATA LINEAGE TRACKING SYSTEM:
Advanced Lineage Management:
```python
# Comprehensive data lineage tracking framework
class DataLineageTracker:
    def __init__(self, config: dict):
        self.config = config
        self.lineage_repository = [LINEAGE_REPO]([LINEAGE_REPO_CONFIG])
        self.graph_database = [GRAPH_DATABASE]([GRAPH_CONFIG])
        self.parser_engine = [PARSER_ENGINE]([PARSER_CONFIG])
        self.impact_analyzer = [IMPACT_ANALYZER]([IMPACT_CONFIG])

    def comprehensive_lineage_discovery(
        self,
        discovery_scope: dict,
        discovery_method: str = 'AUTOMATED'
    ) -> dict:
        """
        Perform comprehensive data lineage discovery

### Args
            discovery_scope: Scope configuration for lineage discovery
            discovery_method: Discovery method (AUTOMATED/MANUAL/HYBRID)

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

### Args
            asset_id: Asset to visualize lineage for
            visualization_type: Type of visualization (GRAPH/FLOWCHART/HIERARCHICAL)
            depth_levels: Number of levels to include (upstream and downstream)

### Returns
            Visualization configuration and data
        """

        visualization_config = {
            'visualization_metadata': {
                'asset_id': asset_id,
                'visualization_type': visualization_type,
                'depth_levels': depth_levels,
                'generation_timestamp': [CURRENT_TIMESTAMP],
                'layout_algorithm': '[LAYOUT_ALGORITHM]'
            },
            'nodes': self.generate_lineage_nodes(asset_id, depth_levels),
            'edges': self.generate_lineage_edges(asset_id, depth_levels),
            'styling': self.generate_visualization_styling(),
            'interactivity': self.define_interaction_features(),
            'export_options': self.define_export_options()
        }

        return visualization_config

    def generate_lineage_nodes(self, asset_id: str, depth: int) -> list:
        """
        Generate nodes for lineage visualization
        """
        nodes = []

        # Get central asset
        central_asset = self.get_asset_metadata(asset_id)
        nodes.append({
            'id': asset_id,
            'label': central_asset['name'],
            'type': central_asset['type'],
            'category': 'CENTRAL',
            'metadata': central_asset,
            'position': {'x': 0, 'y': 0},
            'styling': {
                'color': '[CENTRAL_NODE_COLOR]',
                'size': '[CENTRAL_NODE_SIZE]',
                'shape': '[CENTRAL_NODE_SHAPE]'
            }
        })

        # Get upstream nodes
        upstream_assets = self.get_upstream_assets(asset_id, depth)
        for level, assets in enumerate(upstream_assets.items()):
            for asset in assets:
                nodes.append({
                    'id': asset['asset_id'],
                    'label': asset['name'],
                    'type': asset['type'],
                    'category': 'UPSTREAM',
                    'level': level + 1,
                    'metadata': asset,
                    'position': self.calculate_upstream_position(level, asset['position_index']),
                    'styling': {
                        'color': '[UPSTREAM_NODE_COLOR]',
                        'size': '[UPSTREAM_NODE_SIZE]',
                        'shape': '[UPSTREAM_NODE_SHAPE]'
                    }
                })

        # Get downstream nodes
        downstream_assets = self.get_downstream_assets(asset_id, depth)
        for level, assets in enumerate(downstream_assets.items()):
            for asset in assets:
                nodes.append({
                    'id': asset['asset_id'],
                    'label': asset['name'],
                    'type': asset['type'],
                    'category': 'DOWNSTREAM',
                    'level': level + 1,
                    'metadata': asset,
                    'position': self.calculate_downstream_position(level, asset['position_index']),
                    'styling': {
                        'color': '[DOWNSTREAM_NODE_COLOR]',
                        'size': '[DOWNSTREAM_NODE_SIZE]',
                        'shape': '[DOWNSTREAM_NODE_SHAPE]'
                    }
                })

        return nodes

    def track_lineage_changes(self, change_events: list) -> dict:
        """
        Track changes to data lineage over time
        """
        lineage_change_tracking = {
            'change_summary': {
                'total_changes': len(change_events),
                'change_types': {},
                'affected_assets': set(),
                'tracking_period': '[TRACKING_PERIOD]'
            },
            'change_details': [],
            'impact_assessment': {},
            'notification_sent': []
        }

        for change_event in change_events:
            change_detail = {
                'change_id': change_event.get('change_id'),
                'change_type': change_event.get('type'),  # ADDED/MODIFIED/REMOVED
                'change_timestamp': change_event.get('timestamp'),
                'changed_asset': change_event.get('asset_id'),
                'change_description': change_event.get('description'),
                'change_source': change_event.get('source'),  # USER/AUTOMATED/DISCOVERY
                'previous_lineage': change_event.get('previous_lineage'),
                'new_lineage': change_event.get('new_lineage'),
                'confidence_score': change_event.get('confidence', 1.0),
                'validation_status': 'PENDING'
            }

            lineage_change_tracking['change_details'].append(change_detail)
            lineage_change_tracking['change_summary']['affected_assets'].add(change_event.get('asset_id'))

            # Track change types
            change_type = change_event.get('type')
            if change_type in lineage_change_tracking['change_summary']['change_types']:
                lineage_change_tracking['change_summary']['change_types'][change_type] += 1
            else:
                lineage_change_tracking['change_summary']['change_types'][change_type] = 1

            # Perform impact assessment for the change
            impact = self.assess_change_impact(change_event)
            lineage_change_tracking['impact_assessment'][change_event.get('change_id')] = impact

            # Send notifications if necessary
            if impact.get('severity') in ['HIGH', 'CRITICAL']:
                notification_result = self.send_lineage_change_notification(change_event, impact)
                lineage_change_tracking['notification_sent'].append(notification_result)

        return lineage_change_tracking
```

SCHEMA DOCUMENTATION AUTOMATION:
Automated Documentation Generation:
```python
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

### Args
            documentation_scope: Scope of documentation to generate
            output_formats: List of output formats

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

## Purpose and Context
{[PURPOSE]}

## Business Context
{[BUSINESS_CONTEXT]}

## Schema Statistics
- **Total Tables:** {[TABLE_COUNT]}
- **Total Views:** {[VIEW_COUNT]}
- **Total Functions:** {[FUNCTION_COUNT]}
- **Total Procedures:** {[PROCEDURE_COUNT]}
- **Total Storage Size:** {[TOTAL_SIZE_MB]} MB
- **Estimated Row Count:** {[TOTAL_ROWS]}

## Tables Overview
| Table Name | Description | Row Count | Size (MB) | Last Modified |
|------------|-------------|-----------|-----------|---------------|
{% for table in tables %}
| {{table.name}} | {{table.description}} | {{table.row_count}} | {{table.size_mb}} | {{table.last_modified}} |
{% endfor %}

## Relationships
{[RELATIONSHIP_DIAGRAM]}

## Dependencies
### Upstream Dependencies
{% for dependency in upstream_dependencies %}
- **{{dependency.name}}**: {{dependency.description}}
{% endfor %}

### Downstream Dependencies
{% for dependency in downstream_dependencies %}
- **{{dependency.name}}**: {{dependency.description}}
{% endfor %}

## Data Quality Rules
{% for rule in data_quality_rules %}
- **{{rule.name}}**: {{rule.description}}
  - **Rule Type:** {{rule.type}}
  - **Threshold:** {{rule.threshold}}
  - **Action:** {{rule.action}}
{% endfor %}

## Security and Compliance
- **Classification Level:** {[CLASSIFICATION_LEVEL]}
- **Access Restrictions:** {[ACCESS_RESTRICTIONS]}
- **Compliance Requirements:** {[COMPLIANCE_REQUIREMENTS]}
- **Data Retention:** {[RETENTION_POLICY]}

## Usage Guidelines
{[USAGE_GUIDELINES]}

## Change History
| Date | Version | Change Description | Author |
|------|---------|-------------------|--------|
{% for change in change_history %}
| {{change.date}} | {{change.version}} | {{change.description}} | {{change.author}} |
{% endfor %}

## Contact Information
- **Schema Owner:** {[OWNER_CONTACT]}
- **Data Steward:** {[STEWARD_CONTACT]}
- **Technical Lead:** {[TECHNICAL_LEAD_CONTACT]}
"""
        return template
```

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

            'classification_criteria': {
                'data_sensitivity_indicators': [
                    'Contains personally identifiable information (PII)',
                    'Contains protected health information (PHI)',
                    'Contains financial information',
                    'Contains intellectual property',
                    'Contains trade secrets',
                    'Subject to regulatory requirements',
                    'Could cause competitive disadvantage if disclosed',
                    'Could cause reputational damage if disclosed'
                ],
                'business_impact_levels': {
                    'LOW': 'Minimal impact on business operations or reputation',
                    'MEDIUM': 'Moderate impact requiring management attention',
                    'HIGH': 'Significant impact affecting business objectives',
                    'CRITICAL': 'Severe impact threatening business viability'
                }
            },

            'classification_responsibilities': {
                'data_owners': [
                    'Initial classification of data assets',
                    'Review and approve classification changes',
                    'Ensure appropriate protection measures are implemented'
                ],
                'data_stewards': [
                    'Maintain classification accuracy',
                    'Monitor compliance with classification policies',
                    'Coordinate classification reviews'
                ],
                'data_users': [
                    'Handle data according to its classification',
                    'Report suspected misclassification',
                    'Follow access and usage guidelines'
                ]
            },

            'enforcement_mechanisms': [
                'Automated classification scanning',
                'Policy compliance monitoring',
                'Access control enforcement',
                'Regular audit and review cycles',
                'Training and awareness programs',
                'Incident response procedures'
            ]
        }

        return classification_policy

OUTPUT: Deliver comprehensive data governance framework including:
1. Complete metadata management system with automated discovery
2. Advanced data lineage tracking with impact analysis
3. Automated schema documentation generation
4. Comprehensive data dictionary and business glossary
5. Governance workflow automation and approval processes
6. Policy management and compliance monitoring systems
7. Data classification and sensitivity labeling frameworks
8. Interactive governance dashboards and reporting
9. Stakeholder communication and notification systems
10. Integration APIs for governance tool ecosystems
```

## Variables
[GOVERNANCE_METHODOLOGY], [ORGANIZATION_NAME], [GOVERNANCE_OBJECTIVES], [GOVERNANCE_APPROACH], [GOVERNANCE_TOOLS], [INDUSTRY_SECTOR], [GOVERNANCE_MATURITY_LEVEL], [REGULATORY_REQUIREMENTS], [DATA_DOMAINS], [STAKEHOLDER_GROUPS], [GEOGRAPHIC_SCOPE], [BUSINESS_DRIVERS], [IMPLEMENTATION_MODEL], [METADATA_STRATEGY], [LINEAGE_TRACKING_APPROACH], [DOCUMENTATION_STANDARDS], [QUALITY_ASSURANCE_MODEL], [GOVERNANCE_PLATFORM], [METADATA_REPOSITORY], [LINEAGE_TRACKING_TOOLS], [DOCUMENTATION_PLATFORM], [WORKFLOW_MANAGEMENT_SYSTEM], [POLICY_ENFORCEMENT_SYSTEM], [ACCESS_CONTROL_SYSTEM], [AUDIT_MONITORING_SYSTEM], [DATA_ASSETS_COVERAGE], [SYSTEM_INTEGRATION_SCOPE], [USER_BASE_SIZE], [GOVERNANCE_DATA_VOLUME], [GOVERNANCE_COMPLEXITY], [GOVERNANCE_AUTOMATION_LEVEL], [GOVERNANCE_UPDATE_FREQUENCY], [RETENTION_REQUIREMENTS], [METADATA_LIBRARY], [METADATA_ALIAS], [GOVERNANCE_FRAMEWORK], [GOVERNANCE_COMPONENTS], [LINEAGE_LIBRARY], [LINEAGE_TRACKER], [METADATA_REPO_CONFIG], [SCHEMA_REGISTRY], [SCHEMA_CONFIG], [LINEAGE_CONFIG], [GOV_CONFIG], [ASSET_ID_GENERATOR], [CURRENT_TIMESTAMP], [COMPLETENESS_THRESHOLD], [DICTIONARY_ID_GENERATOR], [DICTIONARY_UPDATE_FREQUENCY], [CATEGORY_1], [CATEGORY_1_DESCRIPTION], [CATEGORY_1_OWNER], [CATEGORY_2], [CATEGORY_2_DESCRIPTION], [CATEGORY_2_OWNER], [TERM_ID], [BUSINESS_TERM_NAME], [BUSINESS_TERM_DEFINITION], [TERM_CATEGORY], [SYNONYM_1], [SYNONYM_2], [RELATED_TERM_1], [RELATED_TERM_2], [TERM_BUSINESS_OWNER], [TERM_DATA_STEWARD], [EXAMPLE_1], [EXAMPLE_2], [TERM_USAGE_CONTEXT], [BUSINESS_RULE_1], [BUSINESS_RULE_2], [DATA_SOURCE_1], [DATA_SOURCE_2], [QUALITY_REQUIREMENTS], [REGULATION_1], [REGULATION_2], [APPROVAL_STATUS], [APPROVAL_DATE], [LINEAGE_REPO], [LINEAGE_REPO_CONFIG], [GRAPH_DATABASE], [GRAPH_CONFIG], [PARSER_ENGINE], [PARSER_CONFIG], [IMPACT_ANALYZER], [IMPACT_CONFIG], [LINEAGE_DISCOVERY_ID], [LOGGING_SYSTEM], [CENTRAL_NODE_COLOR], [CENTRAL_NODE_SIZE], [CENTRAL_NODE_SHAPE], [UPSTREAM_NODE_COLOR], [UPSTREAM_NODE_SIZE], [UPSTREAM_NODE_SHAPE], [DOWNSTREAM_NODE_COLOR], [DOWNSTREAM_NODE_SIZE], [DOWNSTREAM_NODE_SHAPE], [TRACKING_PERIOD], [DOC_GENERATOR], [DOC_CONFIG], [TEMPLATE_ENGINE], [TEMPLATE_CONFIG], [VALIDATION_ENGINE], [VALIDATION_CONFIG], [DOC_GENERATION_ID], [TEMPLATE_VERSION], [WORKFLOW_ENGINE], [WORKFLOW_CONFIG], [APPROVAL_SYSTEM], [APPROVAL_CONFIG], [NOTIFICATION_SYSTEM], [NOTIFICATION_CONFIG], [AUDIT_SYSTEM], [AUDIT_CONFIG], [DATA_STEWARD_ROLE], [BUSINESS_ANALYST_ROLE], [DATA_ENGINEER_ROLE], [DATA_PRIVACY_OFFICER_ROLE], [GOVERNANCE_COMMITTEE_ROLE], [ACCESS_REQUEST_COORDINATOR], [DATA_OWNER], [DATA_PRIVACY_OFFICER], [SECURITY_OFFICER], [DATA_STEWARD], [POLICY_REPO], [POLICY_CONFIG], [RULE_ENGINE], [RULE_CONFIG], [COMPLIANCE_MONITOR], [COMPLIANCE_CONFIG], [POLICY_EFFECTIVE_DATE], [POLICY_REVIEW_DATE], [POLICY_OWNER], [APPROVAL_AUTHORITY], [INTERNAL_RETENTION_PERIOD], [CONFIDENTIAL_RETENTION_PERIOD], [RESTRICTED_RETENTION_PERIOD], [LAYOUT_ALGORITHM]

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
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



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Dashboard Design Patterns](dashboard-design-patterns.md)** - Complementary approaches and methodologies
- **[Data Governance Framework](data-governance-framework.md)** - Leverage data analysis to drive informed decisions
- **[Predictive Modeling Framework](predictive-modeling-framework.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Documentation, Lineage & Governance Template)
2. Use [Dashboard Design Patterns](dashboard-design-patterns.md) for deeper analysis
3. Apply [Data Governance Framework](data-governance-framework.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Analytics Engineering](../../data-analytics/Analytics Engineering/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating design comprehensive data governance frameworks including data lineage tracking systems, data dictionary management, schema documentation automation, metadata management, and enterprise data governance programs for modern data platforms.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Customization Options

1. **Governance Methodologies**
   - Centralized governance (top-down control)
   - Federated governance (distributed ownership)
   - Decentralized governance (self-service model)
   - Hybrid approach (mixed models)
   - Data mesh governance (domain-oriented)
   - Agile governance (iterative approach)

2. **Implementation Approaches**
   - Policy-driven (comprehensive policies first)
   - Risk-based (prioritized by risk assessment)
   - Value-driven (business value focused)
   - Compliance-focused (regulatory requirements driven)
   - Technology-enabled (platform-first approach)
   - Culture-driven (change management focused)

3. **Technical Architectures**
   - Cloud-native governance platforms
   - Hybrid cloud and on-premises
   - Microservices-based architecture
   - Event-driven governance systems
   - API-first integration approach
   - Real-time governance enforcement

4. **Industry Specializations**
   - Financial services (regulatory heavy)
   - Healthcare (privacy focused)
   - Government (compliance and transparency)
   - Technology (innovation and agility)
   - Retail (customer-centric governance)
   - Manufacturing (operational excellence)

5. **Maturity Levels**
   - Initial (ad-hoc governance)
   - Repeatable (basic processes)
   - Defined (documented procedures)
   - Managed (measured and controlled)
   - Optimizing (continuous improvement)
   - Transformative (AI-enabled governance)