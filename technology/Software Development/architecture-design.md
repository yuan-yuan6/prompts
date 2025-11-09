---
title: Architecture Design Template
category: technology/Software Development
tags: [communication, design, security, technology, template]
use_cases:
  - Implementing design comprehensive system architectures including distributed systems, apis, d...
  - Project planning and execution
  - Strategy development
related_templates:
  - cloud-architecture-framework.md
  - site-reliability-engineering.md
  - cloud-migration-strategy.md
last_updated: 2025-11-09
---

# Architecture Design Template

## Purpose
Design comprehensive system architectures including distributed systems, APIs, databases, microservices, and enterprise solutions with scalability, security, and maintainability considerations.

## Template Structure

### System Overview
- **System Name**: {system_name}
- **System Purpose**: {system_purpose}
- **Business Domain**: {business_domain}
- **Target Users**: {target_users}
- **Expected Load**: {expected_load}
- **Geographic Distribution**: {geographic_distribution}
- **Regulatory Requirements**: {regulatory_requirements}
- **Budget Constraints**: {budget_constraints}
- **Timeline**: {timeline}
- **Success Metrics**: {success_metrics}

### Architecture Patterns
- **Primary Pattern**: {primary_pattern}
- **Secondary Patterns**: {secondary_patterns}
- **Design Principles**: {design_principles}
- **Architecture Style**: {architecture_style}
- **Communication Pattern**: {communication_pattern}
- **Data Flow Pattern**: {data_flow_pattern}
- **Integration Pattern**: {integration_pattern}
- **Deployment Pattern**: {deployment_pattern}
- **Security Pattern**: {security_pattern}
- **Resilience Pattern**: {resilience_pattern}

### System Components
- **Frontend Components**: {frontend_components}
- **Backend Services**: {backend_services}
- **Database Layer**: {database_layer}
- **Cache Layer**: {cache_layer}
- **Message Queue**: {message_queue}
- **API Gateway**: {api_gateway}
- **Load Balancer**: {load_balancer}
- **Service Mesh**: {service_mesh}
- **Monitoring System**: {monitoring_system}
- **Security Components**: {security_components}

### Technology Stack
- **Programming Languages**: {programming_languages}
- **Frontend Framework**: {frontend_framework}
- **Backend Framework**: {backend_framework}
- **Database Technology**: {database_technology}
- **Caching Solution**: {caching_solution}
- **Message Broker**: {message_broker}
- **Container Platform**: {container_platform}
- **Orchestration Tool**: {orchestration_tool}
- **Cloud Provider**: {cloud_provider}
- **Development Tools**: {development_tools}

### Scalability Design
- **Horizontal Scaling**: {horizontal_scaling}
- **Vertical Scaling**: {vertical_scaling}
- **Auto Scaling**: {auto_scaling}
- **Load Distribution**: {load_distribution}
- **Caching Strategy**: {caching_strategy}
- **Database Sharding**: {database_sharding}
- **CDN Strategy**: {cdn_strategy}
- **Resource Optimization**: {resource_optimization}
- **Performance Targets**: {performance_targets}
- **Capacity Planning**: {capacity_planning}

### Security Architecture
- **Authentication Method**: {authentication_method}
- **Authorization Model**: {authorization_model}
- **Data Encryption**: {data_encryption}
- **Network Security**: {network_security}
- **API Security**: {api_security}
- **Database Security**: {database_security}
- **Infrastructure Security**: {infrastructure_security}
- **Application Security**: {application_security}
- **Monitoring Security**: {monitoring_security}
- **Compliance Framework**: {compliance_framework}

### Data Architecture
- **Data Model**: {data_model}
- **Database Design**: {database_design}
- **Data Storage**: {data_storage}
- **Data Processing**: {data_processing}
- **Data Integration**: {data_integration}
- **Data Governance**: {data_governance}
- **Data Quality**: {data_quality}
- **Data Backup**: {data_backup}
- **Data Recovery**: {data_recovery}
- **Data Archival**: {data_archival}

### API Design
- **API Architecture**: {api_architecture}
- **API Protocol**: {api_protocol}
- **API Versioning**: {api_versioning}
- **API Documentation**: {api_documentation}
- **Rate Limiting**: {rate_limiting}
- **API Testing**: {api_testing}
- **API Monitoring**: {api_monitoring}
- **API Security**: {api_security_measures}
- **Error Handling**: {api_error_handling}
- **Response Format**: {api_response_format}

### Microservices Design
- **Service Boundaries**: {service_boundaries}
- **Service Communication**: {service_communication}
- **Service Discovery**: {service_discovery}
- **Circuit Breaker**: {circuit_breaker}
- **Service Mesh**: {service_mesh_implementation}
- **Event Sourcing**: {event_sourcing}
- **CQRS Pattern**: {cqrs_pattern}
- **Saga Pattern**: {saga_pattern}
- **Bulkhead Pattern**: {bulkhead_pattern}
- **Retry Logic**: {retry_logic}

### Infrastructure Design
- **Cloud Architecture**: {cloud_architecture}
- **Network Topology**: {network_topology}
- **Server Configuration**: {server_configuration}
- **Container Strategy**: {container_strategy}
- **Storage Architecture**: {storage_architecture}
- **Backup Strategy**: {backup_strategy}
- **Disaster Recovery**: {disaster_recovery}
- **High Availability**: {high_availability}
- **Fault Tolerance**: {fault_tolerance}
- **Resource Management**: {resource_management}

### Deployment Architecture
- **Deployment Strategy**: {deployment_strategy}
- **Environment Setup**: {environment_setup}
- **CI/CD Pipeline**: {cicd_pipeline_design}
- **Release Management**: {release_management}
- **Blue-Green Deployment**: {blue_green_deployment}
- **Canary Deployment**: {canary_deployment}
- **Rolling Updates**: {rolling_updates}
- **Rollback Strategy**: {rollback_strategy}
- **Configuration Management**: {configuration_management}
- **Secrets Management**: {secrets_management}

### Monitoring and Observability
- **Logging Strategy**: {logging_strategy}
- **Metrics Collection**: {metrics_collection}
- **Distributed Tracing**: {distributed_tracing}
- **Health Checks**: {health_checks}
- **Alerting System**: {alerting_system}
- **Dashboard Design**: {dashboard_design}
- **SLA Monitoring**: {sla_monitoring}
- **Performance Monitoring**: {performance_monitoring}
- **Error Tracking**: {error_tracking}
- **Business Metrics**: {business_metrics}

### Integration Architecture
- **External Integrations**: {external_integrations}
- **Third Party APIs**: {third_party_apis}
- **Data Synchronization**: {data_synchronization}
- **Event-Driven Architecture**: {event_driven_architecture}
- **Message Patterns**: {message_patterns}
- **Webhook Management**: {webhook_management}
- **File Transfer**: {file_transfer}
- **Real-time Communication**: {realtime_communication}
- **Batch Processing**: {batch_processing}
- **Stream Processing**: {stream_processing}

### Performance Optimization
- **Caching Layers**: {caching_layers}
- **Database Optimization**: {database_optimization}
- **Query Optimization**: {query_optimization}
- **Connection Pooling**: {connection_pooling}
- **Lazy Loading**: {lazy_loading}
- **Compression**: {compression}
- **Minification**: {minification}
- **Image Optimization**: {image_optimization}
- **Content Delivery**: {content_delivery}
- **Resource Bundling**: {resource_bundling}

### Quality Attributes
- **Availability**: {availability}
- **Reliability**: {reliability}
- **Scalability**: {scalability}
- **Performance**: {performance}
- **Security**: {security}
- **Maintainability**: {maintainability}
- **Testability**: {testability}
- **Usability**: {usability}
- **Portability**: {portability}
- **Interoperability**: {interoperability}

### Risk Management
- **Technical Risks**: {technical_risks}
- **Security Risks**: {security_risks}
- **Performance Risks**: {performance_risks}
- **Scalability Risks**: {scalability_risks}
- **Integration Risks**: {integration_risks}
- **Operational Risks**: {operational_risks}
- **Business Risks**: {business_risks}
- **Mitigation Strategies**: {mitigation_strategies}
- **Contingency Plans**: {contingency_plans}
- **Risk Monitoring**: {risk_monitoring}

### Documentation Requirements
- **Architecture Documentation**: {architecture_documentation}
- **Design Decisions**: {design_decisions}
- **Trade-off Analysis**: {tradeoff_analysis}
- **Implementation Guide**: {implementation_guide}
- **Deployment Guide**: {deployment_guide}
- **Operations Manual**: {operations_manual}
- **Troubleshooting Guide**: {troubleshooting_guide}
- **API Documentation**: {api_documentation_details}
- **Database Schema**: {database_schema}
- **Security Guidelines**: {security_guidelines}

### Testing Strategy
- **Unit Testing**: {unit_testing}
- **Integration Testing**: {integration_testing}
- **End-to-End Testing**: {end_to_end_testing}
- **Performance Testing**: {performance_testing}
- **Security Testing**: {security_testing}
- **Load Testing**: {load_testing}
- **Stress Testing**: {stress_testing}
- **Chaos Engineering**: {chaos_engineering}
- **A/B Testing**: {ab_testing}
- **Test Automation**: {test_automation}

### Migration Strategy
- **Migration Approach**: {migration_approach}
- **Legacy System**: {legacy_system}
- **Migration Timeline**: {migration_timeline}
- **Data Migration**: {data_migration}
- **Cutover Strategy**: {cutover_strategy}
- **Rollback Plan**: {rollback_plan}
- **Parallel Running**: {parallel_running}
- **User Training**: {user_training}
- **Change Management**: {change_management}
- **Success Criteria**: {success_criteria}

## Prompt Template

Design a {architecture_style} architecture for {system_name} that serves {target_users} with {expected_load} load requirements. The system should implement {primary_pattern} pattern and support {business_domain} domain.

**Core Architecture Requirements:**
- Implement {frontend_components} frontend using {frontend_framework}
- Design {backend_services} backend services with {backend_framework}
- Use {database_technology} for data persistence with {database_design}
- Integrate {message_broker} for {service_communication}
- Deploy on {cloud_provider} with {container_platform}

**Scalability and Performance:**
- Support {horizontal_scaling} and {auto_scaling}
- Implement {caching_strategy} with {caching_solution}
- Achieve {performance_targets} response times
- Handle {load_distribution} across multiple instances
- Use {cdn_strategy} for content delivery

**Security Implementation:**
- Implement {authentication_method} and {authorization_model}
- Use {data_encryption} for data protection
- Apply {network_security} and {api_security}
- Follow {compliance_framework} requirements
- Include {monitoring_security} measures

**Integration and Communication:**
- Design {api_architecture} APIs with {api_protocol}
- Implement {service_discovery} for microservices
- Use {event_driven_architecture} for loose coupling
- Handle {external_integrations} with {third_party_apis}
- Support {realtime_communication} where needed

**Reliability and Monitoring:**
- Implement {high_availability} with {fault_tolerance}
- Use {circuit_breaker} and {retry_logic} patterns
- Design {disaster_recovery} and {backup_strategy}
- Monitor with {distributed_tracing} and {metrics_collection}
- Set up {alerting_system} for {sla_monitoring}

**Deployment Strategy:**
- Use {deployment_strategy} with {cicd_pipeline_design}
- Implement {blue_green_deployment} or {canary_deployment}
- Manage configuration with {configuration_management}
- Handle secrets with {secrets_management}
- Support {rolling_updates} with {rollback_strategy}

**Quality Attributes:**
- Ensure {availability}% uptime and {reliability}
- Support {scalability} to handle growth
- Maintain {performance} under peak load
- Implement {security} best practices
- Design for {maintainability} and {testability}

Please provide detailed architecture diagrams, component specifications, technology recommendations, deployment plans, and risk mitigation strategies. Include trade-off analysis for major design decisions and compliance with {regulatory_requirements}.

## Usage Examples

### E-commerce Platform Architecture
```
Design a microservices architecture for ShopFlow e-commerce platform that serves 1M+ users with 10K concurrent load requirements. The system should implement event-driven pattern and support retail domain.

Core Architecture Requirements:
- Implement React SPA frontend using Next.js framework
- Design 8 backend services (user, product, order, payment, inventory, recommendation, notification, analytics) with Node.js/Express
- Use PostgreSQL for transactional data with normalized database design
- Integrate Apache Kafka for asynchronous service communication
- Deploy on AWS with Kubernetes container platform

Scalability and Performance:
- Support horizontal pod scaling and cluster autoscaling
- Implement multi-layer caching with Redis and CloudFront CDN
- Achieve <200ms API response times
- Handle geographic load distribution across multiple regions
- Use CloudFront CDN for static asset delivery

### Security Implementation
- Implement OAuth 2.0/JWT authentication and RBAC authorization model
- Use AES-256 encryption for PII data protection
- Apply WAF, API Gateway rate limiting, and OAuth security
- Follow PCI DSS compliance requirements
- Include SIEM monitoring and threat detection measures
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `{system_name}` | Specify the system name | "John Smith" |
| `{system_purpose}` | Specify the system purpose | "[specify value]" |
| `{business_domain}` | Specify the business domain | "[specify value]" |
| `{target_users}` | Specify the target users | "[specify value]" |
| `{expected_load}` | Specify the expected load | "[specify value]" |
| `{geographic_distribution}` | Specify the geographic distribution | "[specify value]" |
| `{regulatory_requirements}` | Specify the regulatory requirements | "[specify value]" |
| `{budget_constraints}` | Specify the budget constraints | "$500,000" |
| `{timeline}` | Specify the timeline | "6 months" |
| `{success_metrics}` | Specify the success metrics | "[specify value]" |
| `{primary_pattern}` | Specify the primary pattern | "[specify value]" |
| `{secondary_patterns}` | Specify the secondary patterns | "[specify value]" |
| `{design_principles}` | Specify the design principles | "[specify value]" |
| `{architecture_style}` | Specify the architecture style | "[specify value]" |
| `{communication_pattern}` | Specify the communication pattern | "[specify value]" |
| `{data_flow_pattern}` | Specify the data flow pattern | "[specify value]" |
| `{integration_pattern}` | Specify the integration pattern | "[specify value]" |
| `{deployment_pattern}` | Specify the deployment pattern | "[specify value]" |
| `{security_pattern}` | Specify the security pattern | "[specify value]" |
| `{resilience_pattern}` | Specify the resilience pattern | "[specify value]" |
| `{frontend_components}` | Specify the frontend components | "[specify value]" |
| `{backend_services}` | Specify the backend services | "[specify value]" |
| `{database_layer}` | Specify the database layer | "[specify value]" |
| `{cache_layer}` | Specify the cache layer | "[specify value]" |
| `{message_queue}` | Specify the message queue | "[specify value]" |
| `{api_gateway}` | Specify the api gateway | "[specify value]" |
| `{load_balancer}` | Specify the load balancer | "[specify value]" |
| `{service_mesh}` | Specify the service mesh | "[specify value]" |
| `{monitoring_system}` | Specify the monitoring system | "[specify value]" |
| `{security_components}` | Specify the security components | "[specify value]" |
| `{programming_languages}` | Specify the programming languages | "[specify value]" |
| `{frontend_framework}` | Specify the frontend framework | "[specify value]" |
| `{backend_framework}` | Specify the backend framework | "[specify value]" |
| `{database_technology}` | Specify the database technology | "[specify value]" |
| `{caching_solution}` | Specify the caching solution | "[specify value]" |
| `{message_broker}` | Specify the message broker | "[specify value]" |
| `{container_platform}` | Specify the container platform | "[specify value]" |
| `{orchestration_tool}` | Specify the orchestration tool | "[specify value]" |
| `{cloud_provider}` | Specify the cloud provider | "[specify value]" |
| `{development_tools}` | Specify the development tools | "[specify value]" |
| `{horizontal_scaling}` | Specify the horizontal scaling | "[specify value]" |
| `{vertical_scaling}` | Specify the vertical scaling | "[specify value]" |
| `{auto_scaling}` | Specify the auto scaling | "[specify value]" |
| `{load_distribution}` | Specify the load distribution | "[specify value]" |
| `{caching_strategy}` | Specify the caching strategy | "[specify value]" |
| `{database_sharding}` | Specify the database sharding | "[specify value]" |
| `{cdn_strategy}` | Specify the cdn strategy | "[specify value]" |
| `{resource_optimization}` | Specify the resource optimization | "[specify value]" |
| `{performance_targets}` | Specify the performance targets | "[specify value]" |
| `{capacity_planning}` | Specify the capacity planning | "[specify value]" |
| `{authentication_method}` | Specify the authentication method | "[specify value]" |
| `{authorization_model}` | Specify the authorization model | "[specify value]" |
| `{data_encryption}` | Specify the data encryption | "[specify value]" |
| `{network_security}` | Specify the network security | "[specify value]" |
| `{api_security}` | Specify the api security | "[specify value]" |
| `{database_security}` | Specify the database security | "[specify value]" |
| `{infrastructure_security}` | Specify the infrastructure security | "[specify value]" |
| `{application_security}` | Specify the application security | "[specify value]" |
| `{monitoring_security}` | Specify the monitoring security | "[specify value]" |
| `{compliance_framework}` | Specify the compliance framework | "[specify value]" |
| `{data_model}` | Specify the data model | "[specify value]" |
| `{database_design}` | Specify the database design | "[specify value]" |
| `{data_storage}` | Specify the data storage | "[specify value]" |
| `{data_processing}` | Specify the data processing | "[specify value]" |
| `{data_integration}` | Specify the data integration | "[specify value]" |
| `{data_governance}` | Specify the data governance | "[specify value]" |
| `{data_quality}` | Specify the data quality | "[specify value]" |
| `{data_backup}` | Specify the data backup | "[specify value]" |
| `{data_recovery}` | Specify the data recovery | "[specify value]" |
| `{data_archival}` | Specify the data archival | "[specify value]" |
| `{api_architecture}` | Specify the api architecture | "[specify value]" |
| `{api_protocol}` | Specify the api protocol | "[specify value]" |
| `{api_versioning}` | Specify the api versioning | "[specify value]" |
| `{api_documentation}` | Specify the api documentation | "[specify value]" |
| `{rate_limiting}` | Specify the rate limiting | "[specify value]" |
| `{api_testing}` | Specify the api testing | "[specify value]" |
| `{api_monitoring}` | Specify the api monitoring | "[specify value]" |
| `{api_security_measures}` | Specify the api security measures | "[specify value]" |
| `{api_error_handling}` | Specify the api error handling | "[specify value]" |
| `{api_response_format}` | Specify the api response format | "[specify value]" |
| `{service_boundaries}` | Specify the service boundaries | "[specify value]" |
| `{service_communication}` | Specify the service communication | "[specify value]" |
| `{service_discovery}` | Specify the service discovery | "[specify value]" |
| `{circuit_breaker}` | Specify the circuit breaker | "[specify value]" |
| `{service_mesh_implementation}` | Specify the service mesh implementation | "[specify value]" |
| `{event_sourcing}` | Specify the event sourcing | "[specify value]" |
| `{cqrs_pattern}` | Specify the cqrs pattern | "[specify value]" |
| `{saga_pattern}` | Specify the saga pattern | "[specify value]" |
| `{bulkhead_pattern}` | Specify the bulkhead pattern | "[specify value]" |
| `{retry_logic}` | Specify the retry logic | "[specify value]" |
| `{cloud_architecture}` | Specify the cloud architecture | "[specify value]" |
| `{network_topology}` | Specify the network topology | "[specify value]" |
| `{server_configuration}` | Specify the server configuration | "[specify value]" |
| `{container_strategy}` | Specify the container strategy | "[specify value]" |
| `{storage_architecture}` | Specify the storage architecture | "[specify value]" |
| `{backup_strategy}` | Specify the backup strategy | "[specify value]" |
| `{disaster_recovery}` | Specify the disaster recovery | "[specify value]" |
| `{high_availability}` | Specify the high availability | "[specify value]" |
| `{fault_tolerance}` | Specify the fault tolerance | "[specify value]" |
| `{resource_management}` | Specify the resource management | "[specify value]" |
| `{deployment_strategy}` | Specify the deployment strategy | "[specify value]" |
| `{environment_setup}` | Specify the environment setup | "[specify value]" |
| `{cicd_pipeline_design}` | Specify the cicd pipeline design | "[specify value]" |
| `{release_management}` | Specify the release management | "[specify value]" |
| `{blue_green_deployment}` | Specify the blue green deployment | "[specify value]" |
| `{canary_deployment}` | Specify the canary deployment | "[specify value]" |
| `{rolling_updates}` | Specify the rolling updates | "2025-01-15" |
| `{rollback_strategy}` | Specify the rollback strategy | "[specify value]" |
| `{configuration_management}` | Specify the configuration management | "[specify value]" |
| `{secrets_management}` | Specify the secrets management | "[specify value]" |
| `{logging_strategy}` | Specify the logging strategy | "[specify value]" |
| `{metrics_collection}` | Specify the metrics collection | "[specify value]" |
| `{distributed_tracing}` | Specify the distributed tracing | "[specify value]" |
| `{health_checks}` | Specify the health checks | "[specify value]" |
| `{alerting_system}` | Specify the alerting system | "[specify value]" |
| `{dashboard_design}` | Specify the dashboard design | "[specify value]" |
| `{sla_monitoring}` | Specify the sla monitoring | "[specify value]" |
| `{performance_monitoring}` | Specify the performance monitoring | "[specify value]" |
| `{error_tracking}` | Specify the error tracking | "[specify value]" |
| `{business_metrics}` | Specify the business metrics | "[specify value]" |
| `{external_integrations}` | Specify the external integrations | "[specify value]" |
| `{third_party_apis}` | Specify the third party apis | "[specify value]" |
| `{data_synchronization}` | Specify the data synchronization | "[specify value]" |
| `{event_driven_architecture}` | Specify the event driven architecture | "[specify value]" |
| `{message_patterns}` | Specify the message patterns | "[specify value]" |
| `{webhook_management}` | Specify the webhook management | "[specify value]" |
| `{file_transfer}` | Specify the file transfer | "[specify value]" |
| `{realtime_communication}` | Specify the realtime communication | "[specify value]" |
| `{batch_processing}` | Specify the batch processing | "[specify value]" |
| `{stream_processing}` | Specify the stream processing | "[specify value]" |
| `{caching_layers}` | Specify the caching layers | "[specify value]" |
| `{database_optimization}` | Specify the database optimization | "[specify value]" |
| `{query_optimization}` | Specify the query optimization | "[specify value]" |
| `{connection_pooling}` | Specify the connection pooling | "[specify value]" |
| `{lazy_loading}` | Specify the lazy loading | "[specify value]" |
| `{compression}` | Specify the compression | "[specify value]" |
| `{minification}` | Specify the minification | "[specify value]" |
| `{image_optimization}` | Specify the image optimization | "[specify value]" |
| `{content_delivery}` | Specify the content delivery | "[specify value]" |
| `{resource_bundling}` | Specify the resource bundling | "[specify value]" |
| `{availability}` | Specify the availability | "[specify value]" |
| `{reliability}` | Specify the reliability | "[specify value]" |
| `{scalability}` | Specify the scalability | "[specify value]" |
| `{performance}` | Specify the performance | "[specify value]" |
| `{security}` | Specify the security | "[specify value]" |
| `{maintainability}` | Specify the maintainability | "[specify value]" |
| `{testability}` | Specify the testability | "[specify value]" |
| `{usability}` | Specify the usability | "[specify value]" |
| `{portability}` | Specify the portability | "[specify value]" |
| `{interoperability}` | Specify the interoperability | "[specify value]" |
| `{technical_risks}` | Specify the technical risks | "[specify value]" |
| `{security_risks}` | Specify the security risks | "[specify value]" |
| `{performance_risks}` | Specify the performance risks | "[specify value]" |
| `{scalability_risks}` | Specify the scalability risks | "[specify value]" |
| `{integration_risks}` | Specify the integration risks | "[specify value]" |
| `{operational_risks}` | Specify the operational risks | "[specify value]" |
| `{business_risks}` | Specify the business risks | "[specify value]" |
| `{mitigation_strategies}` | Specify the mitigation strategies | "[specify value]" |
| `{contingency_plans}` | Specify the contingency plans | "[specify value]" |
| `{risk_monitoring}` | Specify the risk monitoring | "[specify value]" |
| `{architecture_documentation}` | Specify the architecture documentation | "[specify value]" |
| `{design_decisions}` | Specify the design decisions | "[specify value]" |
| `{tradeoff_analysis}` | Specify the tradeoff analysis | "[specify value]" |
| `{implementation_guide}` | Specify the implementation guide | "[specify value]" |
| `{deployment_guide}` | Specify the deployment guide | "[specify value]" |
| `{operations_manual}` | Specify the operations manual | "[specify value]" |
| `{troubleshooting_guide}` | Specify the troubleshooting guide | "[specify value]" |
| `{api_documentation_details}` | Specify the api documentation details | "[specify value]" |
| `{database_schema}` | Specify the database schema | "[specify value]" |
| `{security_guidelines}` | Specify the security guidelines | "[specify value]" |
| `{unit_testing}` | Specify the unit testing | "[specify value]" |
| `{integration_testing}` | Specify the integration testing | "[specify value]" |
| `{end_to_end_testing}` | Specify the end to end testing | "[specify value]" |
| `{performance_testing}` | Specify the performance testing | "[specify value]" |
| `{security_testing}` | Specify the security testing | "[specify value]" |
| `{load_testing}` | Specify the load testing | "[specify value]" |
| `{stress_testing}` | Specify the stress testing | "[specify value]" |
| `{chaos_engineering}` | Specify the chaos engineering | "[specify value]" |
| `{ab_testing}` | Specify the ab testing | "[specify value]" |
| `{test_automation}` | Specify the test automation | "[specify value]" |
| `{migration_approach}` | Specify the migration approach | "[specify value]" |
| `{legacy_system}` | Specify the legacy system | "[specify value]" |
| `{migration_timeline}` | Specify the migration timeline | "6 months" |
| `{data_migration}` | Specify the data migration | "[specify value]" |
| `{cutover_strategy}` | Specify the cutover strategy | "[specify value]" |
| `{rollback_plan}` | Specify the rollback plan | "[specify value]" |
| `{parallel_running}` | Specify the parallel running | "[specify value]" |
| `{user_training}` | Specify the user training | "[specify value]" |
| `{change_management}` | Specify the change management | "[specify value]" |
| `{success_criteria}` | Specify the success criteria | "[specify value]" |



### Healthcare System Architecture
```
Design a HIPAA-compliant architecture for MedConnect patient management system that serves healthcare providers with enterprise-grade requirements. The system should implement layered architecture pattern and support healthcare domain.

Core Architecture Requirements:
- Implement Angular frontend using Angular Material framework
- Design modular backend services (patient, appointment, billing, EHR, reporting) with Java Spring Boot
- Use encrypted PostgreSQL for PHI data with audit logging
- Integrate HL7 FHIR messaging for healthcare interoperability
- Deploy on Azure with container orchestration

Security Implementation:
- Implement multi-factor authentication and attribute-based authorization
- Use end-to-end encryption for all PHI data protection
- Apply network segmentation, API security scanning, and access controls
- Follow HIPAA, HITECH compliance frameworks
- Include comprehensive audit logging and compliance monitoring
```

## Best Practices

1. **Start with business requirements and quality attributes**
2. **Consider scalability from day one, not as an afterthought**
3. **Design for failure - implement circuit breakers and fallbacks**
4. **Prioritize security throughout all architectural layers**
5. **Document architectural decisions and trade-offs**
6. **Plan for monitoring and observability early**
7. **Design APIs with versioning and backward compatibility**
8. **Consider data consistency patterns for distributed systems**
9. **Plan deployment and rollback strategies upfront**
10. **Include performance budgets and SLA requirements**