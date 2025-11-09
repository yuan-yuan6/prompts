# Database Management Template

## Purpose
Comprehensive database management including schema design, query optimization, performance tuning, backup/recovery, security, maintenance, and monitoring for enterprise database systems.

## Template Structure

### Database Overview
- **Database Name**: {database_name}
- **Database Type**: {database_type}
- **Database Version**: {database_version}
- **Environment**: {environment}
- **Business Purpose**: {business_purpose}
- **Data Volume**: {data_volume}
- **User Base**: {user_base}
- **Performance Requirements**: {performance_requirements}
- **Availability Requirements**: {availability_requirements}
- **Compliance Requirements**: {compliance_requirements}

### Schema Design
- **Database Schema**: {database_schema}
- **Table Design**: {table_design}
- **Column Specifications**: {column_specifications}
- **Data Types**: {data_types}
- **Primary Keys**: {primary_keys}
- **Foreign Keys**: {foreign_keys}
- **Constraints**: {constraints}
- **Indexes**: {indexes}
- **Views**: {views}
- **Stored Procedures**: {stored_procedures}

### Query Optimization
- **Query Performance**: {query_performance}
- **Execution Plans**: {execution_plans}
- **Index Strategy**: {index_strategy}
- **Query Rewriting**: {query_rewriting}
- **Join Optimization**: {join_optimization}
- **Subquery Optimization**: {subquery_optimization}
- **Aggregate Optimization**: {aggregate_optimization}
- **Query Caching**: {query_caching}
- **Statistics Maintenance**: {statistics_maintenance}
- **Query Monitoring**: {query_monitoring}

### Performance Tuning
- **Performance Metrics**: {performance_metrics}
- **Bottleneck Analysis**: {bottleneck_analysis}
- **Resource Utilization**: {resource_utilization}
- **Memory Management**: {memory_management}
- **CPU Optimization**: {cpu_optimization}
- **I/O Optimization**: {io_optimization}
- **Storage Optimization**: {storage_optimization}
- **Connection Management**: {connection_management}
- **Lock Management**: {lock_management}
- **Transaction Optimization**: {transaction_optimization}

### Backup and Recovery
- **Backup Strategy**: {backup_strategy}
- **Backup Types**: {backup_types}
- **Backup Schedule**: {backup_schedule}
- **Backup Storage**: {backup_storage}
- **Backup Verification**: {backup_verification}
- **Recovery Procedures**: {recovery_procedures}
- **Recovery Testing**: {recovery_testing}
- **Point-in-Time Recovery**: {point_in_time_recovery}
- **Disaster Recovery**: {disaster_recovery}
- **Business Continuity**: {business_continuity}

### Security Management
- **Authentication**: {authentication}
- **Authorization**: {authorization}
- **Role-Based Access**: {role_based_access}
- **Data Encryption**: {data_encryption}
- **Network Security**: {network_security}
- **Audit Logging**: {audit_logging}
- **Security Policies**: {security_policies}
- **Vulnerability Management**: {vulnerability_management}
- **Compliance Monitoring**: {compliance_monitoring}
- **Access Controls**: {access_controls}

### Maintenance Operations
- **Routine Maintenance**: {routine_maintenance}
- **Index Maintenance**: {index_maintenance}
- **Statistics Updates**: {statistics_updates}
- **Data Archival**: {data_archival}
- **Data Purging**: {data_purging}
- **Space Management**: {space_management}
- **Log Management**: {log_management}
- **Integrity Checks**: {integrity_checks}
- **Health Checks**: {health_checks}
- **Preventive Maintenance**: {preventive_maintenance}

### Monitoring and Alerting
- **Monitoring Strategy**: {monitoring_strategy}
- **Key Metrics**: {key_metrics}
- **Performance Monitoring**: {performance_monitoring}
- **Availability Monitoring**: {availability_monitoring}
- **Capacity Monitoring**: {capacity_monitoring}
- **Security Monitoring**: {security_monitoring}
- **Alerting Rules**: {alerting_rules}
- **Dashboard Design**: {dashboard_design}
- **Reporting**: {monitoring_reporting}
- **Trend Analysis**: {trend_analysis}

### High Availability
- **HA Architecture**: {ha_architecture}
- **Replication Strategy**: {replication_strategy}
- **Clustering**: {clustering}
- **Load Balancing**: {load_balancing}
- **Failover Procedures**: {failover_procedures}
- **Split-Brain Prevention**: {split_brain_prevention}
- **Data Synchronization**: {data_synchronization}
- **Consistency Management**: {consistency_management}
- **Service Discovery**: {service_discovery}
- **Health Monitoring**: {health_monitoring}

### Scalability
- **Scaling Strategy**: {scaling_strategy}
- **Horizontal Scaling**: {horizontal_scaling}
- **Vertical Scaling**: {vertical_scaling}
- **Partitioning**: {partitioning}
- **Sharding**: {sharding}
- **Read Replicas**: {read_replicas}
- **Caching Layers**: {caching_layers}
- **Connection Pooling**: {connection_pooling}
- **Load Distribution**: {load_distribution}
- **Capacity Planning**: {capacity_planning}

### Data Migration
- **Migration Strategy**: {migration_strategy}
- **Source Assessment**: {source_assessment}
- **Target Preparation**: {target_preparation}
- **Data Mapping**: {data_mapping}
- **ETL Processes**: {etl_processes}
- **Validation Procedures**: {validation_procedures}
- **Cutover Planning**: {cutover_planning}
- **Rollback Procedures**: {rollback_procedures}
- **Testing Strategy**: {migration_testing}
- **Go-Live Support**: {go_live_support}

### Database Operations
- **Operational Procedures**: {operational_procedures}
- **Change Management**: {change_management}
- **Deployment Procedures**: {deployment_procedures}
- **Configuration Management**: {configuration_management}
- **Version Control**: {version_control}
- **Environment Management**: {environment_management}
- **Release Management**: {release_management}
- **Documentation**: {operational_documentation}
- **Training**: {operational_training}
- **Support Procedures**: {support_procedures}

### Cost Optimization
- **Cost Analysis**: {cost_analysis}
- **Resource Optimization**: {resource_optimization}
- **Storage Optimization**: {storage_cost_optimization}
- **Compute Optimization**: {compute_optimization}
- **Licensing Optimization**: {licensing_optimization}
- **Usage Monitoring**: {usage_monitoring}
- **Cost Allocation**: {cost_allocation}
- **Budget Management**: {budget_management}
- **ROI Analysis**: {roi_analysis}
- **Cost Reporting**: {cost_reporting}

### Compliance and Governance
- **Regulatory Compliance**: {regulatory_compliance}
- **Data Governance**: {data_governance}
- **Data Classification**: {data_classification}
- **Retention Policies**: {retention_policies}
- **Privacy Controls**: {privacy_controls}
- **Audit Requirements**: {audit_requirements}
- **Policy Enforcement**: {policy_enforcement}
- **Compliance Reporting**: {compliance_reporting}
- **Risk Management**: {risk_management}
- **Control Framework**: {control_framework}

### Troubleshooting
- **Common Issues**: {common_issues}
- **Diagnostic Procedures**: {diagnostic_procedures}
- **Performance Issues**: {performance_issues}
- **Connectivity Issues**: {connectivity_issues}
- **Replication Issues**: {replication_issues}
- **Backup Issues**: {backup_issues}
- **Security Issues**: {security_issues}
- **Corruption Issues**: {corruption_issues}
- **Space Issues**: {space_issues}
- **Lock Issues**: {lock_issues}

## Prompt Template

Design comprehensive database management for {database_name} {database_type} v{database_version} serving {user_base} users with {data_volume} data volume. Meet {performance_requirements} performance and {availability_requirements} availability requirements while ensuring {compliance_requirements} compliance.

**Schema Design:**
- Design {database_schema} with {table_design} architecture
- Define {column_specifications} using {data_types}
- Implement {primary_keys}, {foreign_keys}, and {constraints}
- Create {indexes} strategy and {views} for data access
- Develop {stored_procedures} for business logic

**Performance Optimization:**
- Achieve {query_performance} with optimized {execution_plans}
- Implement {index_strategy} and {query_caching}
- Optimize {join_optimization} and {aggregate_optimization}
- Monitor {performance_metrics} and conduct {bottleneck_analysis}
- Manage {memory_management} and {connection_management}

**Backup and Recovery:**
- Implement {backup_strategy} with {backup_types}
- Schedule {backup_schedule} to {backup_storage}
- Design {recovery_procedures} with {point_in_time_recovery}
- Plan {disaster_recovery} and {business_continuity}
- Test {recovery_testing} and {backup_verification}

**Security Management:**
- Configure {authentication} and {authorization}
- Implement {role_based_access} and {access_controls}
- Enable {data_encryption} and {network_security}
- Set up {audit_logging} and {compliance_monitoring}
- Manage {vulnerability_management} and {security_policies}

**High Availability:**
- Design {ha_architecture} with {replication_strategy}
- Implement {clustering} and {load_balancing}
- Plan {failover_procedures} and {split_brain_prevention}
- Ensure {data_synchronization} and {consistency_management}
- Monitor {health_monitoring} and {service_discovery}

**Monitoring and Maintenance:**
- Track {key_metrics} and {performance_monitoring}
- Set up {alerting_rules} and {dashboard_design}
- Schedule {routine_maintenance} and {index_maintenance}
- Perform {statistics_updates} and {integrity_checks}
- Manage {data_archival} and {space_management}

**Scalability Planning:**
- Plan {scaling_strategy} with {horizontal_scaling}
- Implement {partitioning} and {sharding}
- Deploy {read_replicas} and {caching_layers}
- Optimize {connection_pooling} and {load_distribution}
- Conduct {capacity_planning} analysis

Please provide detailed implementation plans, configuration examples, monitoring setup, operational procedures, and troubleshooting guides with specific recommendations for the target database platform.

## Usage Examples

### PostgreSQL Production Database
```
Design comprehensive database management for CustomerDB PostgreSQL v14 serving 10,000+ users with 5TB data volume. Meet <100ms query performance and 99.9% availability requirements while ensuring GDPR, SOX compliance.

Schema Design:
- Design normalized database schema with microservices-aligned table design architecture
- Define user, product, order column specifications using JSONB, UUID, timestamp data types
- Implement composite primary keys, cascading foreign keys, and check constraints
- Create B-tree, GIN indexes strategy and materialized views for analytics data access
- Develop PL/pgSQL stored procedures for complex business logic

Performance Optimization:
- Achieve sub-100ms query performance with parallel execution plans
- Implement covering index strategy and shared_buffers query caching
- Optimize hash join optimization and parallel aggregate optimization
- Monitor connection count, cache hit ratio performance metrics and conduct I/O bottleneck analysis
- Manage 16GB shared_buffers memory management and pgbouncer connection management

High Availability:
- Design master-replica ha architecture with streaming replication strategy
- Implement Patroni clustering and HAProxy load balancing
- Plan automatic failover procedures and etcd split brain prevention
- Ensure WAL shipping data synchronization and read-after-write consistency management
- Monitor Consul health monitoring and DNS service discovery
```

### MySQL E-commerce Database
```
Design comprehensive database management for EcommerceDB MySQL v8.0 serving 50,000+ users with 10TB data volume. Meet <50ms query performance and 99.95% availability requirements while ensuring PCI DSS compliance.

Schema Design:
- Design denormalized database schema with product-catalog optimized table design architecture
- Define customer, product, order, payment column specifications using JSON, DECIMAL, DATETIME data types
- Implement auto-increment primary keys, indexed foreign keys, and unique constraints
- Create composite, partial indexes strategy and indexed views for reporting data access
- Develop MySQL stored procedures for payment processing business logic

Scalability Planning:
- Plan read-write splitting scaling strategy with read replica horizontal scaling
- Implement range partitioning and consistent hashing sharding
- Deploy 5 read replicas and Redis caching layers
- Optimize ProxySQL connection pooling and weighted round-robin load distribution
- Conduct monthly capacity planning analysis

Security Management:
- Configure PAM authentication and role-based authorization
- Implement table-level role based access and column-level access controls
- Enable TDE data encryption and SSL network security
- Set up binary logging audit logging and automated compliance monitoring
- Manage quarterly vulnerability management and PCI DSS security policies
```

## Best Practices

1. **Design schema with normalization and performance balance**
2. **Implement comprehensive monitoring and alerting early**
3. **Plan for scalability and high availability from the start**
4. **Automate routine maintenance and backup procedures**
5. **Follow security best practices and compliance requirements**
6. **Test backup and recovery procedures regularly**
7. **Monitor and optimize query performance continuously**
8. **Document all procedures and maintain operational runbooks**
9. **Implement proper change management processes**
10. **Plan capacity and cost optimization strategies**