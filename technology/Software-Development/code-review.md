---
category: technology/software-development
last_updated: 2025-01-09
related_templates:
- api-design.md
- technology/Software-Development/architecture-design.md
- testing-strategy.md
tags:
- quality-assurance
- security
title: Comprehensive Code Review
use_cases:
- Pull request reviews
- Code quality assessment
- Security audits
- Performance optimization
- Technical debt analysis
- Onboarding code reviews
industries:
- manufacturing
- technology
---

# Code Review Template

## Purpose
Conduct comprehensive code reviews focusing on optimization, security, best practices, maintainability, performance, and adherence to coding standards with constructive feedback and actionable recommendations.

## Quick Start

**Need to review code quickly?** Use this minimal example:

### Minimal Example
```
Review the UserAuthentication module in our CustomerAPI (Node.js/Express). Focus on security vulnerabilities (OWASP Top 10), input validation, JWT implementation, and error handling. Check for SQL injection, XSS, and authentication bypass risks. Code coverage should be >80%.
```

### When to Use This
- Pull request reviews before merging to main
- Security audits for authentication/authorization code
- Pre-deployment quality checks
- Onboarding reviews for new team members

### Basic 3-Step Workflow
1. **Scan for critical issues** - Security vulnerabilities, logic errors, breaking changes
2. **Review code quality** - Readability, maintainability, test coverage, standards compliance
3. **Provide feedback** - Document issues with severity, suggest fixes, highlight strengths

**Time to complete**: 30-60 minutes for typical feature (200-400 lines)

---

## Template Structure

### Review Context
- **Review Type**: [REVIEW_TYPE]
- **Code Author**: [CODE_AUTHOR]
- **Reviewer**: [REVIEWER]
- **Review Date**: [REVIEW_DATE]
- **Programming Language**: [PROGRAMMING_LANGUAGE]
- **Framework**: [FRAMEWORK]
- **Project**: [PROJECT_NAME]
- **Feature/Module**: [FEATURE_MODULE]
- **Priority**: [REVIEW_PRIORITY]
- **Deadline**: [REVIEW_DEADLINE]

### Code Quality Assessment
- **Code Readability**: [CODE_READABILITY]
- **Code Maintainability**: [CODE_MAINTAINABILITY]
- **Code Complexity**: [CODE_COMPLEXITY]
- **Naming Conventions**: [NAMING_CONVENTIONS]
- **Code Organization**: [CODE_ORGANIZATION]
- **Documentation Quality**: [DOCUMENTATION_QUALITY]
- **Comment Quality**: [COMMENT_QUALITY]
- **Code Duplication**: [CODE_DUPLICATION]
- **Technical Debt**: [TECHNICAL_DEBT]
- **Refactoring Opportunities**: [REFACTORING_OPPORTUNITIES]

### Architecture and Design
- **Design Patterns**: [DESIGN_PATTERNS]
- **Architecture Compliance**: [ARCHITECTURE_COMPLIANCE]
- **SOLID Principles**: [SOLID_PRINCIPLES]
- **Separation of Concerns**: [SEPARATION_OF_CONCERNS]
- **Dependency Management**: [DEPENDENCY_MANAGEMENT]
- **Interface Design**: [INTERFACE_DESIGN]
- **Abstraction Level**: [ABSTRACTION_LEVEL]
- **Coupling**: [COUPLING]
- **Cohesion**: [COHESION]
- **Scalability**: [SCALABILITY_CONSIDERATIONS]

### Performance Review
- **Algorithm Efficiency**: [ALGORITHM_EFFICIENCY]
- **Time Complexity**: [TIME_COMPLEXITY]
- **Space Complexity**: [SPACE_COMPLEXITY]
- **Memory Usage**: [MEMORY_USAGE]
- **Resource Management**: [RESOURCE_MANAGEMENT]
- **Caching Strategy**: [CACHING_STRATEGY]
- **Database Operations**: [DATABASE_OPERATIONS]
- **I/O Operations**: [IO_OPERATIONS]
- **Concurrency Handling**: [CONCURRENCY_HANDLING]
- **Performance Bottlenecks**: [PERFORMANCE_BOTTLENECKS]

### Security Review
- **Input Validation**: [INPUT_VALIDATION]
- **Output Encoding**: [OUTPUT_ENCODING]
- **Authentication Implementation**: [AUTHENTICATION_IMPLEMENTATION]
- **Authorization Checks**: [AUTHORIZATION_CHECKS]
- **Data Encryption**: [DATA_ENCRYPTION]
- **Secure Communication**: [SECURE_COMMUNICATION]
- **Error Handling**: [ERROR_HANDLING_SECURITY]
- **Logging Security**: [LOGGING_SECURITY]
- **Sensitive Data Handling**: [SENSITIVE_DATA_HANDLING]
- **Vulnerability Assessment**: [VULNERABILITY_ASSESSMENT]

### Testing Review
- **Test Coverage**: [TEST_COVERAGE]
- **Test Quality**: [TEST_QUALITY]
- **Test Cases**: [TEST_CASES]
- **Edge Cases**: [EDGE_CASES]
- **Mock Usage**: [MOCK_USAGE]
- **Test Maintainability**: [TEST_MAINTAINABILITY]
- **Integration Tests**: [INTEGRATION_TESTS]
- **Performance Tests**: [PERFORMANCE_TESTS]
- **Security Tests**: [SECURITY_TESTS]
- **Test Documentation**: [TEST_DOCUMENTATION]

### Error Handling Review
- **Exception Management**: [EXCEPTION_MANAGEMENT]
- **Error Messages**: [ERROR_MESSAGES]
- **Graceful Degradation**: [GRACEFUL_DEGRADATION]
- **Recovery Mechanisms**: [RECOVERY_MECHANISMS]
- **Logging Strategy**: [LOGGING_STRATEGY]
- **Monitoring Integration**: [MONITORING_INTEGRATION]
- **Alerting**: [ALERTING]
- **Timeout Handling**: [TIMEOUT_HANDLING]
- **Circuit Breaker**: [CIRCUIT_BREAKER]
- **Retry Logic**: [RETRY_LOGIC]

### Code Standards Compliance
- **Coding Standards**: [CODING_STANDARDS]
- **Style Guide**: [STYLE_GUIDE]
- **Formatting**: [FORMATTING]
- **Linting Results**: [LINTING_RESULTS]
- **Static Analysis**: [STATIC_ANALYSIS]
- **Type Safety**: [TYPE_SAFETY]
- **Documentation Standards**: [DOCUMENTATION_STANDARDS]
- **Commit Message Quality**: [COMMIT_MESSAGE_QUALITY]
- **Branch Strategy**: [BRANCH_STRATEGY]
- **Version Control**: [VERSION_CONTROL]

### Database Review
- **Query Optimization**: [QUERY_OPTIMIZATION]
- **Index Usage**: [INDEX_USAGE]
- **Transaction Management**: [TRANSACTION_MANAGEMENT]
- **Connection Management**: [CONNECTION_MANAGEMENT]
- **Data Integrity**: [DATA_INTEGRITY]
- **Schema Design**: [SCHEMA_DESIGN]
- **Migration Scripts**: [MIGRATION_SCRIPTS]
- **Backup Considerations**: [BACKUP_CONSIDERATIONS]
- **Performance Impact**: [DB_PERFORMANCE_IMPACT]
- **Concurrency Control**: [CONCURRENCY_CONTROL]

### API Review
- **API Design**: [API_DESIGN]
- **REST Compliance**: [REST_COMPLIANCE]
- **Request/Response Format**: [REQUEST_RESPONSE_FORMAT]
- **Status Codes**: [STATUS_CODES]
- **Error Responses**: [ERROR_RESPONSES]
- **Versioning Strategy**: [VERSIONING_STRATEGY]
- **Documentation**: [API_DOCUMENTATION]
- **Rate Limiting**: [RATE_LIMITING]
- **Caching Headers**: [CACHING_HEADERS]
- **CORS Implementation**: [CORS_IMPLEMENTATION]

### Frontend Review
- **UI/UX Implementation**: [UI_UX_IMPLEMENTATION]
- **Responsive Design**: [RESPONSIVE_DESIGN]
- **Accessibility**: [ACCESSIBILITY]
- **Performance Optimization**: [FRONTEND_PERFORMANCE]
- **Browser Compatibility**: [BROWSER_COMPATIBILITY]
- **JavaScript Quality**: [JAVASCRIPT_QUALITY]
- **CSS Organization**: [CSS_ORGANIZATION]
- **Asset Optimization**: [ASSET_OPTIMIZATION]
- **SEO Considerations**: [SEO_CONSIDERATIONS]
- **Progressive Enhancement**: [PROGRESSIVE_ENHANCEMENT]

### DevOps and Deployment
- **Containerization**: [CONTAINERIZATION]
- **Configuration Management**: [CONFIGURATION_MANAGEMENT]
- **Environment Variables**: [ENVIRONMENT_VARIABLES]
- **Deployment Scripts**: [DEPLOYMENT_SCRIPTS]
- **CI/CD Integration**: [CICD_INTEGRATION]
- **Monitoring Setup**: [MONITORING_SETUP]
- **Logging Configuration**: [LOGGING_CONFIGURATION]
- **Health Checks**: [HEALTH_CHECKS]
- **Scaling Configuration**: [SCALING_CONFIGURATION]
- **Security Configuration**: [SECURITY_CONFIGURATION]

### Documentation Review
- **Code Comments**: [CODE_COMMENTS]
- **API Documentation**: [API_DOCUMENTATION_REVIEW]
- **README Files**: [README_FILES]
- **Architecture Documentation**: [ARCHITECTURE_DOCUMENTATION]
- **Deployment Instructions**: [DEPLOYMENT_INSTRUCTIONS]
- **Troubleshooting Guides**: [TROUBLESHOOTING_GUIDES]
- **Change Logs**: [CHANGE_LOGS]
- **User Guides**: [USER_GUIDES]
- **Developer Guides**: [DEVELOPER_GUIDES]
- **Knowledge Transfer**: [KNOWLEDGE_TRANSFER]

### Business Logic Review
- **Requirements Compliance**: [REQUIREMENTS_COMPLIANCE]
- **Business Rules**: [BUSINESS_RULES]
- **Data Validation**: [DATA_VALIDATION]
- **Workflow Implementation**: [WORKFLOW_IMPLEMENTATION]
- **Edge Case Handling**: [BUSINESS_EDGE_CASES]
- **Integration Points**: [INTEGRATION_POINTS]
- **External Dependencies**: [EXTERNAL_DEPENDENCIES]
- **Backward Compatibility**: [BACKWARD_COMPATIBILITY]
- **Migration Strategy**: [MIGRATION_STRATEGY]
- **Rollback Plans**: [ROLLBACK_PLANS]

### Code Metrics
- **Cyclomatic Complexity**: [CYCLOMATIC_COMPLEXITY]
- **Lines of Code**: [LINES_OF_CODE]
- **Code Coverage**: [CODE_COVERAGE_METRICS]
- **Technical Debt Ratio**: [TECHNICAL_DEBT_RATIO]
- **Duplication Ratio**: [DUPLICATION_RATIO]
- **Maintainability Index**: [MAINTAINABILITY_INDEX]
- **Coupling Metrics**: [COUPLING_METRICS]
- **Cohesion Metrics**: [COHESION_METRICS]
- **Defect Density**: [DEFECT_DENSITY]
- **Code Quality Score**: [CODE_QUALITY_SCORE]

### Review Feedback
- **Strengths**: [STRENGTHS]
- **Areas for Improvement**: [AREAS_FOR_IMPROVEMENT]
- **Critical Issues**: [CRITICAL_ISSUES]
- **Major Issues**: [MAJOR_ISSUES]
- **Minor Issues**: [MINOR_ISSUES]
- **Suggestions**: [SUGGESTIONS]
- **Best Practices**: [BEST_PRACTICES_FEEDBACK]
- **Learning Opportunities**: [LEARNING_OPPORTUNITIES]
- **Action Items**: [ACTION_ITEMS]
- **Follow-up Required**: [FOLLOW_UP_REQUIRED]

### Approval Criteria
- **Code Quality Gate**: [CODE_QUALITY_GATE]
- **Security Gate**: [SECURITY_GATE]
- **Performance Gate**: [PERFORMANCE_GATE]
- **Test Coverage Gate**: [TEST_COVERAGE_GATE]
- **Documentation Gate**: [DOCUMENTATION_GATE]
- **Standards Compliance**: [STANDARDS_COMPLIANCE]
- **Business Requirements**: [BUSINESS_REQUIREMENTS_GATE]
- **Deployment Readiness**: [DEPLOYMENT_READINESS]
- **Risk Assessment**: [RISK_ASSESSMENT]
- **Approval Status**: [APPROVAL_STATUS]

### Improvement Recommendations
- **Immediate Fixes**: [IMMEDIATE_FIXES]
- **Short-term Improvements**: [SHORT_TERM_IMPROVEMENTS]
- **Long-term Refactoring**: [LONG_TERM_REFACTORING]
- **Performance Optimizations**: [PERFORMANCE_OPTIMIZATIONS]
- **Security Enhancements**: [SECURITY_ENHANCEMENTS]
- **Code Quality Improvements**: [CODE_QUALITY_IMPROVEMENTS]
- **Documentation Updates**: [DOCUMENTATION_UPDATES]
- **Testing Enhancements**: [TESTING_ENHANCEMENTS]
- **Architecture Changes**: [ARCHITECTURE_CHANGES]
- **Tool Recommendations**: [TOOL_RECOMMENDATIONS]

### Collaboration and Communication
- **Review Discussion**: [REVIEW_DISCUSSION]
- **Clarifications Needed**: [CLARIFICATIONS_NEEDED]
- **Knowledge Sharing**: [KNOWLEDGE_SHARING]
- **Mentoring Opportunities**: [MENTORING_OPPORTUNITIES]
- **Team Learning**: [TEAM_LEARNING]
- **Process Improvements**: [PROCESS_IMPROVEMENTS]
- **Tool Usage**: [TOOL_USAGE]
- **Communication Style**: [COMMUNICATION_STYLE]
- **Feedback Quality**: [FEEDBACK_QUALITY]
- **Resolution Tracking**: [RESOLUTION_TRACKING]

## Prompt Template

Conduct a comprehensive code review for [FEATURE_MODULE] in [PROJECT_NAME] written in [PROGRAMMING_LANGUAGE] using [FRAMEWORK]. Focus on [REVIEW_PRIORITY] aspects and provide detailed feedback on code quality, security, performance, and best practices.

**Review Scope:**
- Analyze [CODE_COMPLEXITY] and [CODE_MAINTAINABILITY]
- Evaluate [NAMING_CONVENTIONS] and [CODE_ORGANIZATION]
- Assess [DESIGN_PATTERNS] and [ARCHITECTURE_COMPLIANCE]
- Check [SOLID_PRINCIPLES] and [SEPARATION_OF_CONCERNS]
- Review [DEPENDENCY_MANAGEMENT] and [INTERFACE_DESIGN]

**Performance Analysis:**
- Evaluate [ALGORITHM_EFFICIENCY] and [TIME_COMPLEXITY]
- Check [MEMORY_USAGE] and [RESOURCE_MANAGEMENT]
- Review [DATABASE_OPERATIONS] and [CACHING_STRATEGY]
- Assess [CONCURRENCY_HANDLING] and identify [PERFORMANCE_BOTTLENECKS]
- Analyze [IO_OPERATIONS] efficiency

**Security Review:**
- Validate [INPUT_VALIDATION] and [OUTPUT_ENCODING]
- Check [AUTHENTICATION_IMPLEMENTATION] and [AUTHORIZATION_CHECKS]
- Review [DATA_ENCRYPTION] and [SECURE_COMMUNICATION]
- Assess [SENSITIVE_DATA_HANDLING] and [VULNERABILITY_ASSESSMENT]
- Evaluate [ERROR_HANDLING_SECURITY] and [LOGGING_SECURITY]

**Testing Assessment:**
- Review [TEST_COVERAGE] and [TEST_QUALITY]
- Evaluate [TEST_CASES] including [EDGE_CASES]
- Check [MOCK_USAGE] and [TEST_MAINTAINABILITY]
- Assess [INTEGRATION_TESTS] and [PERFORMANCE_TESTS]
- Review [SECURITY_TESTS] and [TEST_DOCUMENTATION]

**Code Standards:**
- Verify [CODING_STANDARDS] and [STYLE_GUIDE] compliance
- Check [FORMATTING] and [LINTING_RESULTS]
- Review [STATIC_ANALYSIS] results and [TYPE_SAFETY]
- Evaluate [DOCUMENTATION_STANDARDS] and [COMMIT_MESSAGE_QUALITY]
- Assess [VERSION_CONTROL] practices

**Quality Gates:**
- Check [CODE_QUALITY_GATE] and [SECURITY_GATE]
- Verify [PERFORMANCE_GATE] and [TEST_COVERAGE_GATE]
- Review [DOCUMENTATION_GATE] and [STANDARDS_COMPLIANCE]
- Assess [BUSINESS_REQUIREMENTS_GATE] and [DEPLOYMENT_READINESS]
- Conduct [RISK_ASSESSMENT]

**Feedback Structure:**
- Identify [STRENGTHS] and [AREAS_FOR_IMPROVEMENT]
- List [CRITICAL_ISSUES], [MAJOR_ISSUES], and [MINOR_ISSUES]
- Provide [SUGGESTIONS] and [BEST_PRACTICES_FEEDBACK]
- Highlight [LEARNING_OPPORTUNITIES] and [ACTION_ITEMS]
- Specify [FOLLOW_UP_REQUIRED]

**Recommendations:**
- Suggest [IMMEDIATE_FIXES] and [SHORT_TERM_IMPROVEMENTS]
- Recommend [PERFORMANCE_OPTIMIZATIONS] and [SECURITY_ENHANCEMENTS]
- Propose [CODE_QUALITY_IMPROVEMENTS] and [TESTING_ENHANCEMENTS]
- Identify [LONG_TERM_REFACTORING] opportunities
- Suggest [TOOL_RECOMMENDATIONS]

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

### Quality Gates
- Check 85% code quality gate and OWASP security gate
- Verify <200ms performance gate and 90% test coverage gate
- Review complete documentation gate and ESLint standards compliance
- Assess functional requirements gate and containerization deployment readiness
- Conduct security, performance risk assessment
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[REVIEW_TYPE]` | Specify the review type | "Standard" |
| `[CODE_AUTHOR]` | Specify the code author | "[specify value]" |
| `[REVIEWER]` | Specify the reviewer | "[specify value]" |
| `[REVIEW_DATE]` | Specify the review date | "2025-01-15" |
| `[PROGRAMMING_LANGUAGE]` | Specify the programming language | "[specify value]" |
| `[FRAMEWORK]` | Specify the framework | "[specify value]" |
| `[PROJECT_NAME]` | Specify the project name | "Digital Transformation Initiative" |
| `[FEATURE_MODULE]` | Specify the feature module | "[specify value]" |
| `[REVIEW_PRIORITY]` | Specify the review priority | "High" |
| `[REVIEW_DEADLINE]` | Specify the review deadline | "[specify value]" |
| `[CODE_READABILITY]` | Specify the code readability | "[specify value]" |
| `[CODE_MAINTAINABILITY]` | Specify the code maintainability | "[specify value]" |
| `[CODE_COMPLEXITY]` | Specify the code complexity | "[specify value]" |
| `[NAMING_CONVENTIONS]` | Specify the naming conventions | "[specify value]" |
| `[CODE_ORGANIZATION]` | Specify the code organization | "[specify value]" |
| `[DOCUMENTATION_QUALITY]` | Specify the documentation quality | "[specify value]" |
| `[COMMENT_QUALITY]` | Specify the comment quality | "[specify value]" |
| `[CODE_DUPLICATION]` | Specify the code duplication | "[specify value]" |
| `[TECHNICAL_DEBT]` | Specify the technical debt | "[specify value]" |
| `[REFACTORING_OPPORTUNITIES]` | Specify the refactoring opportunities | "[specify value]" |
| `[DESIGN_PATTERNS]` | Specify the design patterns | "[specify value]" |
| `[ARCHITECTURE_COMPLIANCE]` | Specify the architecture compliance | "[specify value]" |
| `[SOLID_PRINCIPLES]` | Specify the solid principles | "[specify value]" |
| `[SEPARATION_OF_CONCERNS]` | Specify the separation of concerns | "[specify value]" |
| `[DEPENDENCY_MANAGEMENT]` | Specify the dependency management | "[specify value]" |
| `[INTERFACE_DESIGN]` | Specify the interface design | "[specify value]" |
| `[ABSTRACTION_LEVEL]` | Specify the abstraction level | "[specify value]" |
| `[COUPLING]` | Specify the coupling | "[specify value]" |
| `[COHESION]` | Specify the cohesion | "[specify value]" |
| `[SCALABILITY_CONSIDERATIONS]` | Specify the scalability considerations | "[specify value]" |
| `[ALGORITHM_EFFICIENCY]` | Specify the algorithm efficiency | "[specify value]" |
| `[TIME_COMPLEXITY]` | Specify the time complexity | "[specify value]" |
| `[SPACE_COMPLEXITY]` | Specify the space complexity | "[specify value]" |
| `[MEMORY_USAGE]` | Specify the memory usage | "[specify value]" |
| `[RESOURCE_MANAGEMENT]` | Specify the resource management | "[specify value]" |
| `[CACHING_STRATEGY]` | Specify the caching strategy | "[specify value]" |
| `[DATABASE_OPERATIONS]` | Specify the database operations | "[specify value]" |
| `[IO_OPERATIONS]` | Specify the io operations | "[specify value]" |
| `[CONCURRENCY_HANDLING]` | Specify the concurrency handling | "[specify value]" |
| `[PERFORMANCE_BOTTLENECKS]` | Specify the performance bottlenecks | "[specify value]" |
| `[INPUT_VALIDATION]` | Specify the input validation | "[specify value]" |
| `[OUTPUT_ENCODING]` | Specify the output encoding | "[specify value]" |
| `[AUTHENTICATION_IMPLEMENTATION]` | Specify the authentication implementation | "[specify value]" |
| `[AUTHORIZATION_CHECKS]` | Specify the authorization checks | "[specify value]" |
| `[DATA_ENCRYPTION]` | Specify the data encryption | "[specify value]" |
| `[SECURE_COMMUNICATION]` | Specify the secure communication | "[specify value]" |
| `[ERROR_HANDLING_SECURITY]` | Specify the error handling security | "[specify value]" |
| `[LOGGING_SECURITY]` | Specify the logging security | "[specify value]" |
| `[SENSITIVE_DATA_HANDLING]` | Specify the sensitive data handling | "[specify value]" |
| `[VULNERABILITY_ASSESSMENT]` | Specify the vulnerability assessment | "[specify value]" |
| `[TEST_COVERAGE]` | Specify the test coverage | "[specify value]" |
| `[TEST_QUALITY]` | Specify the test quality | "[specify value]" |
| `[TEST_CASES]` | Specify the test cases | "[specify value]" |
| `[EDGE_CASES]` | Specify the edge cases | "[specify value]" |
| `[MOCK_USAGE]` | Specify the mock usage | "[specify value]" |
| `[TEST_MAINTAINABILITY]` | Specify the test maintainability | "[specify value]" |
| `[INTEGRATION_TESTS]` | Specify the integration tests | "[specify value]" |
| `[PERFORMANCE_TESTS]` | Specify the performance tests | "[specify value]" |
| `[SECURITY_TESTS]` | Specify the security tests | "[specify value]" |
| `[TEST_DOCUMENTATION]` | Specify the test documentation | "[specify value]" |
| `[EXCEPTION_MANAGEMENT]` | Specify the exception management | "[specify value]" |
| `[ERROR_MESSAGES]` | Specify the error messages | "[specify value]" |
| `[GRACEFUL_DEGRADATION]` | Specify the graceful degradation | "[specify value]" |
| `[RECOVERY_MECHANISMS]` | Specify the recovery mechanisms | "[specify value]" |
| `[LOGGING_STRATEGY]` | Specify the logging strategy | "[specify value]" |
| `[MONITORING_INTEGRATION]` | Specify the monitoring integration | "[specify value]" |
| `[ALERTING]` | Specify the alerting | "[specify value]" |
| `[TIMEOUT_HANDLING]` | Specify the timeout handling | "[specify value]" |
| `[CIRCUIT_BREAKER]` | Specify the circuit breaker | "[specify value]" |
| `[RETRY_LOGIC]` | Specify the retry logic | "[specify value]" |
| `[CODING_STANDARDS]` | Specify the coding standards | "[specify value]" |
| `[STYLE_GUIDE]` | Specify the style guide | "[specify value]" |
| `[FORMATTING]` | Specify the formatting | "[specify value]" |
| `[LINTING_RESULTS]` | Specify the linting results | "[specify value]" |
| `[STATIC_ANALYSIS]` | Specify the static analysis | "[specify value]" |
| `[TYPE_SAFETY]` | Specify the type safety | "Standard" |
| `[DOCUMENTATION_STANDARDS]` | Specify the documentation standards | "[specify value]" |
| `[COMMIT_MESSAGE_QUALITY]` | Specify the commit message quality | "[specify value]" |
| `[BRANCH_STRATEGY]` | Specify the branch strategy | "[specify value]" |
| `[VERSION_CONTROL]` | Specify the version control | "[specify value]" |
| `[QUERY_OPTIMIZATION]` | Specify the query optimization | "[specify value]" |
| `[INDEX_USAGE]` | Specify the index usage | "[specify value]" |
| `[TRANSACTION_MANAGEMENT]` | Specify the transaction management | "[specify value]" |
| `[CONNECTION_MANAGEMENT]` | Specify the connection management | "[specify value]" |
| `[DATA_INTEGRITY]` | Specify the data integrity | "[specify value]" |
| `[SCHEMA_DESIGN]` | Specify the schema design | "[specify value]" |
| `[MIGRATION_SCRIPTS]` | Specify the migration scripts | "[specify value]" |
| `[BACKUP_CONSIDERATIONS]` | Specify the backup considerations | "[specify value]" |
| `[DB_PERFORMANCE_IMPACT]` | Specify the db performance impact | "[specify value]" |
| `[CONCURRENCY_CONTROL]` | Specify the concurrency control | "[specify value]" |
| `[API_DESIGN]` | Specify the api design | "[specify value]" |
| `[REST_COMPLIANCE]` | Specify the rest compliance | "[specify value]" |
| `[REQUEST_RESPONSE_FORMAT]` | Specify the request response format | "[specify value]" |
| `[STATUS_CODES]` | Specify the status codes | "In Progress" |
| `[ERROR_RESPONSES]` | Specify the error responses | "[specify value]" |
| `[VERSIONING_STRATEGY]` | Specify the versioning strategy | "[specify value]" |
| `[API_DOCUMENTATION]` | Specify the api documentation | "[specify value]" |
| `[RATE_LIMITING]` | Specify the rate limiting | "[specify value]" |
| `[CACHING_HEADERS]` | Specify the caching headers | "[specify value]" |
| `[CORS_IMPLEMENTATION]` | Specify the cors implementation | "[specify value]" |
| `[UI_UX_IMPLEMENTATION]` | Specify the ui ux implementation | "[specify value]" |
| `[RESPONSIVE_DESIGN]` | Specify the responsive design | "[specify value]" |
| `[ACCESSIBILITY]` | Specify the accessibility | "[specify value]" |
| `[FRONTEND_PERFORMANCE]` | Specify the frontend performance | "[specify value]" |
| `[BROWSER_COMPATIBILITY]` | Specify the browser compatibility | "[specify value]" |
| `[JAVASCRIPT_QUALITY]` | Specify the javascript quality | "[specify value]" |
| `[CSS_ORGANIZATION]` | Specify the css organization | "[specify value]" |
| `[ASSET_OPTIMIZATION]` | Specify the asset optimization | "[specify value]" |
| `[SEO_CONSIDERATIONS]` | Specify the seo considerations | "[specify value]" |
| `[PROGRESSIVE_ENHANCEMENT]` | Specify the progressive enhancement | "[specify value]" |
| `[CONTAINERIZATION]` | Specify the containerization | "[specify value]" |
| `[CONFIGURATION_MANAGEMENT]` | Specify the configuration management | "[specify value]" |
| `[ENVIRONMENT_VARIABLES]` | Specify the environment variables | "[specify value]" |
| `[DEPLOYMENT_SCRIPTS]` | Specify the deployment scripts | "[specify value]" |
| `[CICD_INTEGRATION]` | Specify the cicd integration | "[specify value]" |
| `[MONITORING_SETUP]` | Specify the monitoring setup | "[specify value]" |
| `[LOGGING_CONFIGURATION]` | Specify the logging configuration | "[specify value]" |
| `[HEALTH_CHECKS]` | Specify the health checks | "[specify value]" |
| `[SCALING_CONFIGURATION]` | Specify the scaling configuration | "[specify value]" |
| `[SECURITY_CONFIGURATION]` | Specify the security configuration | "[specify value]" |
| `[CODE_COMMENTS]` | Specify the code comments | "[specify value]" |
| `[API_DOCUMENTATION_REVIEW]` | Specify the api documentation review | "[specify value]" |
| `[README_FILES]` | Specify the readme files | "[specify value]" |
| `[ARCHITECTURE_DOCUMENTATION]` | Specify the architecture documentation | "[specify value]" |
| `[DEPLOYMENT_INSTRUCTIONS]` | Specify the deployment instructions | "[specify value]" |
| `[TROUBLESHOOTING_GUIDES]` | Specify the troubleshooting guides | "[specify value]" |
| `[CHANGE_LOGS]` | Specify the change logs | "[specify value]" |
| `[USER_GUIDES]` | Specify the user guides | "[specify value]" |
| `[DEVELOPER_GUIDES]` | Specify the developer guides | "[specify value]" |
| `[KNOWLEDGE_TRANSFER]` | Specify the knowledge transfer | "[specify value]" |
| `[REQUIREMENTS_COMPLIANCE]` | Specify the requirements compliance | "[specify value]" |
| `[BUSINESS_RULES]` | Specify the business rules | "[specify value]" |
| `[DATA_VALIDATION]` | Specify the data validation | "[specify value]" |
| `[WORKFLOW_IMPLEMENTATION]` | Specify the workflow implementation | "[specify value]" |
| `[BUSINESS_EDGE_CASES]` | Specify the business edge cases | "[specify value]" |
| `[INTEGRATION_POINTS]` | Specify the integration points | "[specify value]" |
| `[EXTERNAL_DEPENDENCIES]` | Specify the external dependencies | "[specify value]" |
| `[BACKWARD_COMPATIBILITY]` | Specify the backward compatibility | "[specify value]" |
| `[MIGRATION_STRATEGY]` | Specify the migration strategy | "[specify value]" |
| `[ROLLBACK_PLANS]` | Specify the rollback plans | "[specify value]" |
| `[CYCLOMATIC_COMPLEXITY]` | Specify the cyclomatic complexity | "[specify value]" |
| `[LINES_OF_CODE]` | Specify the lines of code | "[specify value]" |
| `[CODE_COVERAGE_METRICS]` | Specify the code coverage metrics | "[specify value]" |
| `[TECHNICAL_DEBT_RATIO]` | Specify the technical debt ratio | "[specify value]" |
| `[DUPLICATION_RATIO]` | Specify the duplication ratio | "[specify value]" |
| `[MAINTAINABILITY_INDEX]` | Specify the maintainability index | "[specify value]" |
| `[COUPLING_METRICS]` | Specify the coupling metrics | "[specify value]" |
| `[COHESION_METRICS]` | Specify the cohesion metrics | "[specify value]" |
| `[DEFECT_DENSITY]` | Specify the defect density | "[specify value]" |
| `[CODE_QUALITY_SCORE]` | Specify the code quality score | "[specify value]" |
| `[STRENGTHS]` | Specify the strengths | "[specify value]" |
| `[AREAS_FOR_IMPROVEMENT]` | Specify the areas for improvement | "[specify value]" |
| `[CRITICAL_ISSUES]` | Specify the critical issues | "[specify value]" |
| `[MAJOR_ISSUES]` | Specify the major issues | "[specify value]" |
| `[MINOR_ISSUES]` | Specify the minor issues | "[specify value]" |
| `[SUGGESTIONS]` | Specify the suggestions | "[specify value]" |
| `[BEST_PRACTICES_FEEDBACK]` | Specify the best practices feedback | "[specify value]" |
| `[LEARNING_OPPORTUNITIES]` | Specify the learning opportunities | "[specify value]" |
| `[ACTION_ITEMS]` | Specify the action items | "[specify value]" |
| `[FOLLOW_UP_REQUIRED]` | Specify the follow up required | "[specify value]" |
| `[CODE_QUALITY_GATE]` | Specify the code quality gate | "[specify value]" |
| `[SECURITY_GATE]` | Specify the security gate | "[specify value]" |
| `[PERFORMANCE_GATE]` | Specify the performance gate | "[specify value]" |
| `[TEST_COVERAGE_GATE]` | Specify the test coverage gate | "[specify value]" |
| `[DOCUMENTATION_GATE]` | Specify the documentation gate | "[specify value]" |
| `[STANDARDS_COMPLIANCE]` | Specify the standards compliance | "[specify value]" |
| `[BUSINESS_REQUIREMENTS_GATE]` | Specify the business requirements gate | "[specify value]" |
| `[DEPLOYMENT_READINESS]` | Specify the deployment readiness | "[specify value]" |
| `[RISK_ASSESSMENT]` | Specify the risk assessment | "[specify value]" |
| `[APPROVAL_STATUS]` | Specify the approval status | "In Progress" |
| `[IMMEDIATE_FIXES]` | Specify the immediate fixes | "[specify value]" |
| `[SHORT_TERM_IMPROVEMENTS]` | Specify the short term improvements | "[specify value]" |
| `[LONG_TERM_REFACTORING]` | Specify the long term refactoring | "[specify value]" |
| `[PERFORMANCE_OPTIMIZATIONS]` | Specify the performance optimizations | "[specify value]" |
| `[SECURITY_ENHANCEMENTS]` | Specify the security enhancements | "[specify value]" |
| `[CODE_QUALITY_IMPROVEMENTS]` | Specify the code quality improvements | "[specify value]" |
| `[DOCUMENTATION_UPDATES]` | Specify the documentation updates | "2025-01-15" |
| `[TESTING_ENHANCEMENTS]` | Specify the testing enhancements | "[specify value]" |
| `[ARCHITECTURE_CHANGES]` | Specify the architecture changes | "[specify value]" |
| `[TOOL_RECOMMENDATIONS]` | Specify the tool recommendations | "[specify value]" |
| `[REVIEW_DISCUSSION]` | Specify the review discussion | "[specify value]" |
| `[CLARIFICATIONS_NEEDED]` | Specify the clarifications needed | "[specify value]" |
| `[KNOWLEDGE_SHARING]` | Specify the knowledge sharing | "[specify value]" |
| `[MENTORING_OPPORTUNITIES]` | Specify the mentoring opportunities | "[specify value]" |
| `[TEAM_LEARNING]` | Specify the team learning | "[specify value]" |
| `[PROCESS_IMPROVEMENTS]` | Specify the process improvements | "[specify value]" |
| `[TOOL_USAGE]` | Specify the tool usage | "[specify value]" |
| `[COMMUNICATION_STYLE]` | Specify the communication style | "[specify value]" |
| `[FEEDBACK_QUALITY]` | Specify the feedback quality | "[specify value]" |
| `[RESOLUTION_TRACKING]` | Specify the resolution tracking | "[specify value]" |

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



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Api Design](api-design.md)** - Complementary approaches and methodologies
- **[Architecture Design](architecture-design.md)** - Complementary approaches and methodologies
- **[Testing Strategy](testing-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Comprehensive Code Review)
2. Use [Api Design](api-design.md) for deeper analysis
3. Apply [Architecture Design](architecture-design.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/software-development](../../technology/software-development/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Pull request reviews**: Combine this template with related analytics and strategy frameworks
- **Code quality assessment**: Combine this template with related analytics and strategy frameworks
- **Security audits**: Combine this template with related analytics and strategy frameworks

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