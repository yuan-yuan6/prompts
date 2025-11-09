# Security Architecture Template

## Purpose
Design comprehensive security architecture including security design principles, defensive strategies, implementation patterns, and governance frameworks for enterprise security systems.

## Template Structure

### Security Architecture Overview
- **Architecture Name**: {architecture_name}
- **Security Objectives**: {security_objectives}
- **Business Context**: {business_context}
- **Threat Landscape**: {threat_landscape}
- **Regulatory Requirements**: {regulatory_requirements}
- **Risk Profile**: {risk_profile}
- **Architecture Scope**: {architecture_scope}
- **Technology Stack**: {security_technology_stack}
- **Budget**: {architecture_budget}
- **Timeline**: {architecture_timeline}

### Security Principles
- **Defense in Depth**: {defense_in_depth}
- **Zero Trust**: {zero_trust}
- **Least Privilege**: {least_privilege}
- **Fail Secure**: {fail_secure}
- **Security by Design**: {security_by_design}
- **Separation of Duties**: {separation_of_duties}
- **Complete Mediation**: {complete_mediation}
- **Open Design**: {open_design}
- **Psychological Acceptability**: {psychological_acceptability}
- **Work Factor**: {work_factor}

### Identity and Access Management
- **Identity Strategy**: {identity_strategy}
- **Authentication Methods**: {authentication_methods}
- **Authorization Model**: {authorization_model}
- **Identity Providers**: {identity_providers}
- **Single Sign-On**: {single_sign_on}
- **Multi-Factor Authentication**: {multi_factor_authentication}
- **Privileged Access Management**: {privileged_access_management}
- **Identity Governance**: {identity_governance}
- **Access Reviews**: {access_reviews}
- **Identity Federation**: {identity_federation}

### Network Security Architecture
- **Network Segmentation**: {network_segmentation}
- **Perimeter Defense**: {perimeter_defense}
- **Internal Network Security**: {internal_network_security}
- **Remote Access**: {remote_access}
- **Wireless Security**: {wireless_security}
- **Network Monitoring**: {network_monitoring}
- **Intrusion Detection**: {intrusion_detection}
- **Intrusion Prevention**: {intrusion_prevention}
- **Network Access Control**: {network_access_control}
- **DDoS Protection**: {ddos_protection}

### Application Security Architecture
- **Secure Development**: {secure_development}
- **Application Security Testing**: {application_security_testing}
- **Runtime Protection**: {runtime_protection}
- **API Security**: {api_security}
- **Web Application Firewall**: {web_application_firewall}
- **Code Analysis**: {code_analysis}
- **Dependency Management**: {dependency_management}
- **Container Security**: {container_security}
- **Serverless Security**: {serverless_security}
- **Mobile Application Security**: {mobile_application_security}

### Data Security Architecture
- **Data Classification**: {data_classification}
- **Data Protection**: {data_protection}
- **Encryption Strategy**: {encryption_strategy}
- **Key Management**: {key_management}
- **Data Loss Prevention**: {data_loss_prevention}
- **Database Security**: {database_security}
- **Backup Security**: {backup_security}
- **Data Masking**: {data_masking}
- **Data Retention**: {data_retention}
- **Data Governance**: {security_data_governance}

Please provide detailed architecture diagrams, security controls mapping, implementation guides, and governance frameworks.

## Usage Examples

### Cloud Security Architecture
```
Design comprehensive security architecture for CloudFirst multi-cloud environment supporting zero trust security objectives with hybrid workforce business context.

Security Architecture Overview:
- Multi-cloud security architecture for AWS, Azure, GCP platforms
- Implement zero trust, defense in depth security objectives
- Support remote workforce, cloud migration business context
- Address APT, ransomware, insider threat landscape
- Ensure SOC2, ISO27001 regulatory requirements

Zero Trust Implementation:
- Never trust, always verify zero trust principles
- Implement continuous verification, least privilege access
- Use identity-centric security model identity strategy
- Deploy SAML, OAuth 2.0, certificate authentication methods
- Apply RBAC, ABAC authorization model with dynamic policies

Network Security Architecture:
- Implement micro-segmentation network segmentation
- Deploy cloud WAF, DDoS protection perimeter defense
- Use VPC flow logs, SIEM network monitoring
- Implement cloud CASB, SWG for remote access
- Deploy NIDS/NIPS intrusion detection systems

Data Security Architecture:
- Classify data as public, internal, confidential, restricted
- Encrypt data at rest with AES-256, in transit with TLS 1.3
- Implement FIPS 140-2 Level 3 HSM key management
- Deploy cloud DLP data loss prevention across SaaS/IaaS
- Apply tokenization, format-preserving encryption data masking
```

## Best Practices

1. **Align security architecture with business objectives**
2. **Apply defense in depth and zero trust principles**
3. **Design for scalability and adaptability**
4. **Integrate security controls throughout the architecture**
5. **Maintain architecture documentation and governance**