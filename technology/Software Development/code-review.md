---
title: Comprehensive Code Review
category: technology/software-development
tags: [code-review, software-engineering, quality-assurance, best-practices, security, performance]
use_cases:
  - Pull request reviews
  - Code quality assessment
  - Security audits
  - Performance optimization
  - Technical debt analysis
  - Onboarding code reviews
related_templates:
  - api-design.md
  - architecture-design.md
  - testing-strategy.md
last_updated: 2025-01-09
---

# Code Review Template

## Purpose
Conduct comprehensive code reviews focusing on optimization, security, best practices, maintainability, performance, and adherence to coding standards with constructive feedback and actionable recommendations.

## Template Structure

### Review Context
- **Review Type**: {review_type}
- **Code Author**: {code_author}
- **Reviewer**: {reviewer}
- **Review Date**: {review_date}
- **Programming Language**: {programming_language}
- **Framework**: {framework}
- **Project**: {project_name}
- **Feature/Module**: {feature_module}
- **Priority**: {review_priority}
- **Deadline**: {review_deadline}

### Code Quality Assessment
- **Code Readability**: {code_readability}
- **Code Maintainability**: {code_maintainability}
- **Code Complexity**: {code_complexity}
- **Naming Conventions**: {naming_conventions}
- **Code Organization**: {code_organization}
- **Documentation Quality**: {documentation_quality}
- **Comment Quality**: {comment_quality}
- **Code Duplication**: {code_duplication}
- **Technical Debt**: {technical_debt}
- **Refactoring Opportunities**: {refactoring_opportunities}

### Architecture and Design
- **Design Patterns**: {design_patterns}
- **Architecture Compliance**: {architecture_compliance}
- **SOLID Principles**: {solid_principles}
- **Separation of Concerns**: {separation_of_concerns}
- **Dependency Management**: {dependency_management}
- **Interface Design**: {interface_design}
- **Abstraction Level**: {abstraction_level}
- **Coupling**: {coupling}
- **Cohesion**: {cohesion}
- **Scalability**: {scalability_considerations}

### Performance Review
- **Algorithm Efficiency**: {algorithm_efficiency}
- **Time Complexity**: {time_complexity}
- **Space Complexity**: {space_complexity}
- **Memory Usage**: {memory_usage}
- **Resource Management**: {resource_management}
- **Caching Strategy**: {caching_strategy}
- **Database Operations**: {database_operations}
- **I/O Operations**: {io_operations}
- **Concurrency Handling**: {concurrency_handling}
- **Performance Bottlenecks**: {performance_bottlenecks}

### Security Review
- **Input Validation**: {input_validation}
- **Output Encoding**: {output_encoding}
- **Authentication Implementation**: {authentication_implementation}
- **Authorization Checks**: {authorization_checks}
- **Data Encryption**: {data_encryption}
- **Secure Communication**: {secure_communication}
- **Error Handling**: {error_handling_security}
- **Logging Security**: {logging_security}
- **Sensitive Data Handling**: {sensitive_data_handling}
- **Vulnerability Assessment**: {vulnerability_assessment}

### Testing Review
- **Test Coverage**: {test_coverage}
- **Test Quality**: {test_quality}
- **Test Cases**: {test_cases}
- **Edge Cases**: {edge_cases}
- **Mock Usage**: {mock_usage}
- **Test Maintainability**: {test_maintainability}
- **Integration Tests**: {integration_tests}
- **Performance Tests**: {performance_tests}
- **Security Tests**: {security_tests}
- **Test Documentation**: {test_documentation}

### Error Handling Review
- **Exception Management**: {exception_management}
- **Error Messages**: {error_messages}
- **Graceful Degradation**: {graceful_degradation}
- **Recovery Mechanisms**: {recovery_mechanisms}
- **Logging Strategy**: {logging_strategy}
- **Monitoring Integration**: {monitoring_integration}
- **Alerting**: {alerting}
- **Timeout Handling**: {timeout_handling}
- **Circuit Breaker**: {circuit_breaker}
- **Retry Logic**: {retry_logic}

### Code Standards Compliance
- **Coding Standards**: {coding_standards}
- **Style Guide**: {style_guide}
- **Formatting**: {formatting}
- **Linting Results**: {linting_results}
- **Static Analysis**: {static_analysis}
- **Type Safety**: {type_safety}
- **Documentation Standards**: {documentation_standards}
- **Commit Message Quality**: {commit_message_quality}
- **Branch Strategy**: {branch_strategy}
- **Version Control**: {version_control}

### Database Review
- **Query Optimization**: {query_optimization}
- **Index Usage**: {index_usage}
- **Transaction Management**: {transaction_management}
- **Connection Management**: {connection_management}
- **Data Integrity**: {data_integrity}
- **Schema Design**: {schema_design}
- **Migration Scripts**: {migration_scripts}
- **Backup Considerations**: {backup_considerations}
- **Performance Impact**: {db_performance_impact}
- **Concurrency Control**: {concurrency_control}

### API Review
- **API Design**: {api_design}
- **REST Compliance**: {rest_compliance}
- **Request/Response Format**: {request_response_format}
- **Status Codes**: {status_codes}
- **Error Responses**: {error_responses}
- **Versioning Strategy**: {versioning_strategy}
- **Documentation**: {api_documentation}
- **Rate Limiting**: {rate_limiting}
- **Caching Headers**: {caching_headers}
- **CORS Implementation**: {cors_implementation}

### Frontend Review
- **UI/UX Implementation**: {ui_ux_implementation}
- **Responsive Design**: {responsive_design}
- **Accessibility**: {accessibility}
- **Performance Optimization**: {frontend_performance}
- **Browser Compatibility**: {browser_compatibility}
- **JavaScript Quality**: {javascript_quality}
- **CSS Organization**: {css_organization}
- **Asset Optimization**: {asset_optimization}
- **SEO Considerations**: {seo_considerations}
- **Progressive Enhancement**: {progressive_enhancement}

### DevOps and Deployment
- **Containerization**: {containerization}
- **Configuration Management**: {configuration_management}
- **Environment Variables**: {environment_variables}
- **Deployment Scripts**: {deployment_scripts}
- **CI/CD Integration**: {cicd_integration}
- **Monitoring Setup**: {monitoring_setup}
- **Logging Configuration**: {logging_configuration}
- **Health Checks**: {health_checks}
- **Scaling Configuration**: {scaling_configuration}
- **Security Configuration**: {security_configuration}

### Documentation Review
- **Code Comments**: {code_comments}
- **API Documentation**: {api_documentation_review}
- **README Files**: {readme_files}
- **Architecture Documentation**: {architecture_documentation}
- **Deployment Instructions**: {deployment_instructions}
- **Troubleshooting Guides**: {troubleshooting_guides}
- **Change Logs**: {change_logs}
- **User Guides**: {user_guides}
- **Developer Guides**: {developer_guides}
- **Knowledge Transfer**: {knowledge_transfer}

### Business Logic Review
- **Requirements Compliance**: {requirements_compliance}
- **Business Rules**: {business_rules}
- **Data Validation**: {data_validation}
- **Workflow Implementation**: {workflow_implementation}
- **Edge Case Handling**: {business_edge_cases}
- **Integration Points**: {integration_points}
- **External Dependencies**: {external_dependencies}
- **Backward Compatibility**: {backward_compatibility}
- **Migration Strategy**: {migration_strategy}
- **Rollback Plans**: {rollback_plans}

### Code Metrics
- **Cyclomatic Complexity**: {cyclomatic_complexity}
- **Lines of Code**: {lines_of_code}
- **Code Coverage**: {code_coverage_metrics}
- **Technical Debt Ratio**: {technical_debt_ratio}
- **Duplication Ratio**: {duplication_ratio}
- **Maintainability Index**: {maintainability_index}
- **Coupling Metrics**: {coupling_metrics}
- **Cohesion Metrics**: {cohesion_metrics}
- **Defect Density**: {defect_density}
- **Code Quality Score**: {code_quality_score}

### Review Feedback
- **Strengths**: {strengths}
- **Areas for Improvement**: {areas_for_improvement}
- **Critical Issues**: {critical_issues}
- **Major Issues**: {major_issues}
- **Minor Issues**: {minor_issues}
- **Suggestions**: {suggestions}
- **Best Practices**: {best_practices_feedback}
- **Learning Opportunities**: {learning_opportunities}
- **Action Items**: {action_items}
- **Follow-up Required**: {follow_up_required}

### Approval Criteria
- **Code Quality Gate**: {code_quality_gate}
- **Security Gate**: {security_gate}
- **Performance Gate**: {performance_gate}
- **Test Coverage Gate**: {test_coverage_gate}
- **Documentation Gate**: {documentation_gate}
- **Standards Compliance**: {standards_compliance}
- **Business Requirements**: {business_requirements_gate}
- **Deployment Readiness**: {deployment_readiness}
- **Risk Assessment**: {risk_assessment}
- **Approval Status**: {approval_status}

### Improvement Recommendations
- **Immediate Fixes**: {immediate_fixes}
- **Short-term Improvements**: {short_term_improvements}
- **Long-term Refactoring**: {long_term_refactoring}
- **Performance Optimizations**: {performance_optimizations}
- **Security Enhancements**: {security_enhancements}
- **Code Quality Improvements**: {code_quality_improvements}
- **Documentation Updates**: {documentation_updates}
- **Testing Enhancements**: {testing_enhancements}
- **Architecture Changes**: {architecture_changes}
- **Tool Recommendations**: {tool_recommendations}

### Collaboration and Communication
- **Review Discussion**: {review_discussion}
- **Clarifications Needed**: {clarifications_needed}
- **Knowledge Sharing**: {knowledge_sharing}
- **Mentoring Opportunities**: {mentoring_opportunities}
- **Team Learning**: {team_learning}
- **Process Improvements**: {process_improvements}
- **Tool Usage**: {tool_usage}
- **Communication Style**: {communication_style}
- **Feedback Quality**: {feedback_quality}
- **Resolution Tracking**: {resolution_tracking}

## Prompt Template

Conduct a comprehensive code review for {feature_module} in {project_name} written in {programming_language} using {framework}. Focus on {review_priority} aspects and provide detailed feedback on code quality, security, performance, and best practices.

**Review Scope:**
- Analyze {code_complexity} and {code_maintainability}
- Evaluate {naming_conventions} and {code_organization}
- Assess {design_patterns} and {architecture_compliance}
- Check {solid_principles} and {separation_of_concerns}
- Review {dependency_management} and {interface_design}

**Performance Analysis:**
- Evaluate {algorithm_efficiency} and {time_complexity}
- Check {memory_usage} and {resource_management}
- Review {database_operations} and {caching_strategy}
- Assess {concurrency_handling} and identify {performance_bottlenecks}
- Analyze {io_operations} efficiency

**Security Review:**
- Validate {input_validation} and {output_encoding}
- Check {authentication_implementation} and {authorization_checks}
- Review {data_encryption} and {secure_communication}
- Assess {sensitive_data_handling} and {vulnerability_assessment}
- Evaluate {error_handling_security} and {logging_security}

**Testing Assessment:**
- Review {test_coverage} and {test_quality}
- Evaluate {test_cases} including {edge_cases}
- Check {mock_usage} and {test_maintainability}
- Assess {integration_tests} and {performance_tests}
- Review {security_tests} and {test_documentation}

**Code Standards:**
- Verify {coding_standards} and {style_guide} compliance
- Check {formatting} and {linting_results}
- Review {static_analysis} results and {type_safety}
- Evaluate {documentation_standards} and {commit_message_quality}
- Assess {version_control} practices

**Quality Gates:**
- Check {code_quality_gate} and {security_gate}
- Verify {performance_gate} and {test_coverage_gate}
- Review {documentation_gate} and {standards_compliance}
- Assess {business_requirements_gate} and {deployment_readiness}
- Conduct {risk_assessment}

**Feedback Structure:**
- Identify {strengths} and {areas_for_improvement}
- List {critical_issues}, {major_issues}, and {minor_issues}
- Provide {suggestions} and {best_practices_feedback}
- Highlight {learning_opportunities} and {action_items}
- Specify {follow_up_required}

**Recommendations:**
- Suggest {immediate_fixes} and {short_term_improvements}
- Recommend {performance_optimizations} and {security_enhancements}
- Propose {code_quality_improvements} and {testing_enhancements}
- Identify {long_term_refactoring} opportunities
- Suggest {tool_recommendations}

Please provide specific, actionable feedback with code examples, explain the reasoning behind recommendations, and prioritize issues by severity. Include positive feedback to reinforce good practices and create a collaborative review environment.

## Usage Examples

### API Endpoint Review
```
Conduct a comprehensive code review for user authentication endpoint in CustomerAPI written in Node.js using Express framework. Focus on high priority security aspects and provide detailed feedback on code quality, security, performance, and best practices.

Review Scope:
- Analyze medium code complexity and good code maintainability
- Evaluate camelCase naming conventions and modular code organization
- Assess MVC design patterns and RESTful architecture compliance
- Check Single Responsibility, Open/Closed SOLID principles and proper separation of concerns
- Review npm dependency management and clean interface design

Security Review:
- Validate Joi input validation and helmet.js output encoding
- Check JWT authentication implementation and role-based authorization checks
- Review bcrypt data encryption and HTTPS secure communication
- Assess password hashing sensitive data handling and OWASP vulnerability assessment
- Evaluate structured error handling security and winston logging security

Quality Gates:
- Check 85% code quality gate and OWASP security gate
- Verify <200ms performance gate and 90% test coverage gate
- Review complete documentation gate and ESLint standards compliance
- Assess functional requirements gate and containerization deployment readiness
- Conduct security, performance risk assessment
```

### React Component Review
```
Conduct a comprehensive code review for UserProfile component in EcommerceFrontend written in TypeScript using React/Next.js framework. Focus on high priority performance aspects and provide detailed feedback on code quality, accessibility, performance, and best practices.

Performance Analysis:
- Evaluate React.memo algorithm efficiency and O(1) time complexity
- Check useState memory usage and useCallback resource management
- Review API calls database operations and localStorage caching strategy
- Assess useEffect concurrency handling and identify re-rendering performance bottlenecks
- Analyze image loading io operations efficiency

Frontend Review:
- Check responsive UI/UX implementation and mobile-first responsive design
- Verify WCAG 2.1 accessibility and lazy loading frontend performance
- Review Chrome, Firefox, Safari browser compatibility and ES6+ JavaScript quality
- Assess CSS modules organization and image optimization asset optimization
- Check meta tags SEO considerations and polyfills progressive enhancement
```

## Best Practices

1. **Be constructive and specific in feedback**
2. **Focus on the code, not the person**
3. **Provide examples and alternatives for suggested changes**
4. **Balance criticism with positive reinforcement**
5. **Prioritize issues by severity and impact**
6. **Use automated tools to catch basic issues**
7. **Review in manageable chunks (< 400 lines)**
8. **Include security and performance considerations**
9. **Verify business requirements are met**
10. **Document decisions and rationale for future reference**