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

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `{review_type}` | Specify the review type | "Standard" |
| `{code_author}` | Specify the code author | "[specify value]" |
| `{reviewer}` | Specify the reviewer | "[specify value]" |
| `{review_date}` | Specify the review date | "2025-01-15" |
| `{programming_language}` | Specify the programming language | "[specify value]" |
| `{framework}` | Specify the framework | "[specify value]" |
| `{project_name}` | Specify the project name | "Digital Transformation Initiative" |
| `{feature_module}` | Specify the feature module | "[specify value]" |
| `{review_priority}` | Specify the review priority | "High" |
| `{review_deadline}` | Specify the review deadline | "[specify value]" |
| `{code_readability}` | Specify the code readability | "[specify value]" |
| `{code_maintainability}` | Specify the code maintainability | "[specify value]" |
| `{code_complexity}` | Specify the code complexity | "[specify value]" |
| `{naming_conventions}` | Specify the naming conventions | "[specify value]" |
| `{code_organization}` | Specify the code organization | "[specify value]" |
| `{documentation_quality}` | Specify the documentation quality | "[specify value]" |
| `{comment_quality}` | Specify the comment quality | "[specify value]" |
| `{code_duplication}` | Specify the code duplication | "[specify value]" |
| `{technical_debt}` | Specify the technical debt | "[specify value]" |
| `{refactoring_opportunities}` | Specify the refactoring opportunities | "[specify value]" |
| `{design_patterns}` | Specify the design patterns | "[specify value]" |
| `{architecture_compliance}` | Specify the architecture compliance | "[specify value]" |
| `{solid_principles}` | Specify the solid principles | "[specify value]" |
| `{separation_of_concerns}` | Specify the separation of concerns | "[specify value]" |
| `{dependency_management}` | Specify the dependency management | "[specify value]" |
| `{interface_design}` | Specify the interface design | "[specify value]" |
| `{abstraction_level}` | Specify the abstraction level | "[specify value]" |
| `{coupling}` | Specify the coupling | "[specify value]" |
| `{cohesion}` | Specify the cohesion | "[specify value]" |
| `{scalability_considerations}` | Specify the scalability considerations | "[specify value]" |
| `{algorithm_efficiency}` | Specify the algorithm efficiency | "[specify value]" |
| `{time_complexity}` | Specify the time complexity | "[specify value]" |
| `{space_complexity}` | Specify the space complexity | "[specify value]" |
| `{memory_usage}` | Specify the memory usage | "[specify value]" |
| `{resource_management}` | Specify the resource management | "[specify value]" |
| `{caching_strategy}` | Specify the caching strategy | "[specify value]" |
| `{database_operations}` | Specify the database operations | "[specify value]" |
| `{io_operations}` | Specify the io operations | "[specify value]" |
| `{concurrency_handling}` | Specify the concurrency handling | "[specify value]" |
| `{performance_bottlenecks}` | Specify the performance bottlenecks | "[specify value]" |
| `{input_validation}` | Specify the input validation | "[specify value]" |
| `{output_encoding}` | Specify the output encoding | "[specify value]" |
| `{authentication_implementation}` | Specify the authentication implementation | "[specify value]" |
| `{authorization_checks}` | Specify the authorization checks | "[specify value]" |
| `{data_encryption}` | Specify the data encryption | "[specify value]" |
| `{secure_communication}` | Specify the secure communication | "[specify value]" |
| `{error_handling_security}` | Specify the error handling security | "[specify value]" |
| `{logging_security}` | Specify the logging security | "[specify value]" |
| `{sensitive_data_handling}` | Specify the sensitive data handling | "[specify value]" |
| `{vulnerability_assessment}` | Specify the vulnerability assessment | "[specify value]" |
| `{test_coverage}` | Specify the test coverage | "[specify value]" |
| `{test_quality}` | Specify the test quality | "[specify value]" |
| `{test_cases}` | Specify the test cases | "[specify value]" |
| `{edge_cases}` | Specify the edge cases | "[specify value]" |
| `{mock_usage}` | Specify the mock usage | "[specify value]" |
| `{test_maintainability}` | Specify the test maintainability | "[specify value]" |
| `{integration_tests}` | Specify the integration tests | "[specify value]" |
| `{performance_tests}` | Specify the performance tests | "[specify value]" |
| `{security_tests}` | Specify the security tests | "[specify value]" |
| `{test_documentation}` | Specify the test documentation | "[specify value]" |
| `{exception_management}` | Specify the exception management | "[specify value]" |
| `{error_messages}` | Specify the error messages | "[specify value]" |
| `{graceful_degradation}` | Specify the graceful degradation | "[specify value]" |
| `{recovery_mechanisms}` | Specify the recovery mechanisms | "[specify value]" |
| `{logging_strategy}` | Specify the logging strategy | "[specify value]" |
| `{monitoring_integration}` | Specify the monitoring integration | "[specify value]" |
| `{alerting}` | Specify the alerting | "[specify value]" |
| `{timeout_handling}` | Specify the timeout handling | "[specify value]" |
| `{circuit_breaker}` | Specify the circuit breaker | "[specify value]" |
| `{retry_logic}` | Specify the retry logic | "[specify value]" |
| `{coding_standards}` | Specify the coding standards | "[specify value]" |
| `{style_guide}` | Specify the style guide | "[specify value]" |
| `{formatting}` | Specify the formatting | "[specify value]" |
| `{linting_results}` | Specify the linting results | "[specify value]" |
| `{static_analysis}` | Specify the static analysis | "[specify value]" |
| `{type_safety}` | Specify the type safety | "Standard" |
| `{documentation_standards}` | Specify the documentation standards | "[specify value]" |
| `{commit_message_quality}` | Specify the commit message quality | "[specify value]" |
| `{branch_strategy}` | Specify the branch strategy | "[specify value]" |
| `{version_control}` | Specify the version control | "[specify value]" |
| `{query_optimization}` | Specify the query optimization | "[specify value]" |
| `{index_usage}` | Specify the index usage | "[specify value]" |
| `{transaction_management}` | Specify the transaction management | "[specify value]" |
| `{connection_management}` | Specify the connection management | "[specify value]" |
| `{data_integrity}` | Specify the data integrity | "[specify value]" |
| `{schema_design}` | Specify the schema design | "[specify value]" |
| `{migration_scripts}` | Specify the migration scripts | "[specify value]" |
| `{backup_considerations}` | Specify the backup considerations | "[specify value]" |
| `{db_performance_impact}` | Specify the db performance impact | "[specify value]" |
| `{concurrency_control}` | Specify the concurrency control | "[specify value]" |
| `{api_design}` | Specify the api design | "[specify value]" |
| `{rest_compliance}` | Specify the rest compliance | "[specify value]" |
| `{request_response_format}` | Specify the request response format | "[specify value]" |
| `{status_codes}` | Specify the status codes | "In Progress" |
| `{error_responses}` | Specify the error responses | "[specify value]" |
| `{versioning_strategy}` | Specify the versioning strategy | "[specify value]" |
| `{api_documentation}` | Specify the api documentation | "[specify value]" |
| `{rate_limiting}` | Specify the rate limiting | "[specify value]" |
| `{caching_headers}` | Specify the caching headers | "[specify value]" |
| `{cors_implementation}` | Specify the cors implementation | "[specify value]" |
| `{ui_ux_implementation}` | Specify the ui ux implementation | "[specify value]" |
| `{responsive_design}` | Specify the responsive design | "[specify value]" |
| `{accessibility}` | Specify the accessibility | "[specify value]" |
| `{frontend_performance}` | Specify the frontend performance | "[specify value]" |
| `{browser_compatibility}` | Specify the browser compatibility | "[specify value]" |
| `{javascript_quality}` | Specify the javascript quality | "[specify value]" |
| `{css_organization}` | Specify the css organization | "[specify value]" |
| `{asset_optimization}` | Specify the asset optimization | "[specify value]" |
| `{seo_considerations}` | Specify the seo considerations | "[specify value]" |
| `{progressive_enhancement}` | Specify the progressive enhancement | "[specify value]" |
| `{containerization}` | Specify the containerization | "[specify value]" |
| `{configuration_management}` | Specify the configuration management | "[specify value]" |
| `{environment_variables}` | Specify the environment variables | "[specify value]" |
| `{deployment_scripts}` | Specify the deployment scripts | "[specify value]" |
| `{cicd_integration}` | Specify the cicd integration | "[specify value]" |
| `{monitoring_setup}` | Specify the monitoring setup | "[specify value]" |
| `{logging_configuration}` | Specify the logging configuration | "[specify value]" |
| `{health_checks}` | Specify the health checks | "[specify value]" |
| `{scaling_configuration}` | Specify the scaling configuration | "[specify value]" |
| `{security_configuration}` | Specify the security configuration | "[specify value]" |
| `{code_comments}` | Specify the code comments | "[specify value]" |
| `{api_documentation_review}` | Specify the api documentation review | "[specify value]" |
| `{readme_files}` | Specify the readme files | "[specify value]" |
| `{architecture_documentation}` | Specify the architecture documentation | "[specify value]" |
| `{deployment_instructions}` | Specify the deployment instructions | "[specify value]" |
| `{troubleshooting_guides}` | Specify the troubleshooting guides | "[specify value]" |
| `{change_logs}` | Specify the change logs | "[specify value]" |
| `{user_guides}` | Specify the user guides | "[specify value]" |
| `{developer_guides}` | Specify the developer guides | "[specify value]" |
| `{knowledge_transfer}` | Specify the knowledge transfer | "[specify value]" |
| `{requirements_compliance}` | Specify the requirements compliance | "[specify value]" |
| `{business_rules}` | Specify the business rules | "[specify value]" |
| `{data_validation}` | Specify the data validation | "[specify value]" |
| `{workflow_implementation}` | Specify the workflow implementation | "[specify value]" |
| `{business_edge_cases}` | Specify the business edge cases | "[specify value]" |
| `{integration_points}` | Specify the integration points | "[specify value]" |
| `{external_dependencies}` | Specify the external dependencies | "[specify value]" |
| `{backward_compatibility}` | Specify the backward compatibility | "[specify value]" |
| `{migration_strategy}` | Specify the migration strategy | "[specify value]" |
| `{rollback_plans}` | Specify the rollback plans | "[specify value]" |
| `{cyclomatic_complexity}` | Specify the cyclomatic complexity | "[specify value]" |
| `{lines_of_code}` | Specify the lines of code | "[specify value]" |
| `{code_coverage_metrics}` | Specify the code coverage metrics | "[specify value]" |
| `{technical_debt_ratio}` | Specify the technical debt ratio | "[specify value]" |
| `{duplication_ratio}` | Specify the duplication ratio | "[specify value]" |
| `{maintainability_index}` | Specify the maintainability index | "[specify value]" |
| `{coupling_metrics}` | Specify the coupling metrics | "[specify value]" |
| `{cohesion_metrics}` | Specify the cohesion metrics | "[specify value]" |
| `{defect_density}` | Specify the defect density | "[specify value]" |
| `{code_quality_score}` | Specify the code quality score | "[specify value]" |
| `{strengths}` | Specify the strengths | "[specify value]" |
| `{areas_for_improvement}` | Specify the areas for improvement | "[specify value]" |
| `{critical_issues}` | Specify the critical issues | "[specify value]" |
| `{major_issues}` | Specify the major issues | "[specify value]" |
| `{minor_issues}` | Specify the minor issues | "[specify value]" |
| `{suggestions}` | Specify the suggestions | "[specify value]" |
| `{best_practices_feedback}` | Specify the best practices feedback | "[specify value]" |
| `{learning_opportunities}` | Specify the learning opportunities | "[specify value]" |
| `{action_items}` | Specify the action items | "[specify value]" |
| `{follow_up_required}` | Specify the follow up required | "[specify value]" |
| `{code_quality_gate}` | Specify the code quality gate | "[specify value]" |
| `{security_gate}` | Specify the security gate | "[specify value]" |
| `{performance_gate}` | Specify the performance gate | "[specify value]" |
| `{test_coverage_gate}` | Specify the test coverage gate | "[specify value]" |
| `{documentation_gate}` | Specify the documentation gate | "[specify value]" |
| `{standards_compliance}` | Specify the standards compliance | "[specify value]" |
| `{business_requirements_gate}` | Specify the business requirements gate | "[specify value]" |
| `{deployment_readiness}` | Specify the deployment readiness | "[specify value]" |
| `{risk_assessment}` | Specify the risk assessment | "[specify value]" |
| `{approval_status}` | Specify the approval status | "In Progress" |
| `{immediate_fixes}` | Specify the immediate fixes | "[specify value]" |
| `{short_term_improvements}` | Specify the short term improvements | "[specify value]" |
| `{long_term_refactoring}` | Specify the long term refactoring | "[specify value]" |
| `{performance_optimizations}` | Specify the performance optimizations | "[specify value]" |
| `{security_enhancements}` | Specify the security enhancements | "[specify value]" |
| `{code_quality_improvements}` | Specify the code quality improvements | "[specify value]" |
| `{documentation_updates}` | Specify the documentation updates | "2025-01-15" |
| `{testing_enhancements}` | Specify the testing enhancements | "[specify value]" |
| `{architecture_changes}` | Specify the architecture changes | "[specify value]" |
| `{tool_recommendations}` | Specify the tool recommendations | "[specify value]" |
| `{review_discussion}` | Specify the review discussion | "[specify value]" |
| `{clarifications_needed}` | Specify the clarifications needed | "[specify value]" |
| `{knowledge_sharing}` | Specify the knowledge sharing | "[specify value]" |
| `{mentoring_opportunities}` | Specify the mentoring opportunities | "[specify value]" |
| `{team_learning}` | Specify the team learning | "[specify value]" |
| `{process_improvements}` | Specify the process improvements | "[specify value]" |
| `{tool_usage}` | Specify the tool usage | "[specify value]" |
| `{communication_style}` | Specify the communication style | "[specify value]" |
| `{feedback_quality}` | Specify the feedback quality | "[specify value]" |
| `{resolution_tracking}` | Specify the resolution tracking | "[specify value]" |



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