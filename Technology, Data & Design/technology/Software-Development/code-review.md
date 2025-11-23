---
category: technology
last_updated: 2025-11-23
related_templates:
- technology/Software-Development/architecture-design.md
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
type: template
difficulty: intermediate
slug: code-review
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
| `[REVIEW_TYPE]` | Type of code review being conducted | "Pull Request Review, Security Audit, Architecture Review" |
| `[CODE_AUTHOR]` | Developer who wrote the code under review | "Sarah Chen, Senior Backend Developer" |
| `[REVIEWER]` | Person conducting the code review | "Marcus Johnson, Tech Lead" |
| `[REVIEW_DATE]` | Date when review is conducted | "2025-01-15" |
| `[PROGRAMMING_LANGUAGE]` | Primary programming language used | "Python 3.11, TypeScript 5.3, Go 1.21" |
| `[FRAMEWORK]` | Framework or libraries in use | "Django 4.2, FastAPI 0.104, React 18.2, Next.js 14" |
| `[PROJECT_NAME]` | Name of the project being reviewed | "CustomerAPI, PaymentGateway, EcommercePortal" |
| `[FEATURE_MODULE]` | Specific feature or module under review | "UserAuthentication/jwt-handler, OrderService/checkout-flow" |
| `[REVIEW_PRIORITY]` | Priority level for the review | "Critical - blocking release, High - security-related, Medium - feature enhancement" |
| `[REVIEW_DEADLINE]` | Deadline for completing the review | "2025-01-20 EOD, before v2.3 release, within 24 hours" |
| `[CODE_READABILITY]` | Assessment of code clarity and understandability | "Clear variable names, consistent formatting, self-documenting functions" |
| `[CODE_MAINTAINABILITY]` | Ease of future modifications | "Modular design, low coupling, comprehensive unit tests, documented APIs" |
| `[CODE_COMPLEXITY]` | Measure of code complexity | "Cyclomatic complexity <10 per function, max nesting depth 3, no god classes" |
| `[NAMING_CONVENTIONS]` | Variable and function naming standards | "camelCase for functions, PascalCase for classes, UPPER_SNAKE for constants, descriptive names" |
| `[CODE_ORGANIZATION]` | Structure and organization of code | "Feature-based folder structure, separation of concerns, logical file grouping" |
| `[DOCUMENTATION_QUALITY]` | Quality of inline and external documentation | "JSDoc comments on public APIs, README with setup instructions, architecture decision records" |
| `[COMMENT_QUALITY]` | Quality and usefulness of code comments | "Explains 'why' not 'what', updated with code changes, no commented-out code blocks" |
| `[CODE_DUPLICATION]` | Amount of duplicated code | "DRY principle followed, <5% duplication ratio, shared utilities extracted" |
| `[TECHNICAL_DEBT]` | Accumulated technical debt assessment | "2 TODO items, 1 deprecated API usage, legacy auth system needs migration" |
| `[REFACTORING_OPPORTUNITIES]` | Areas that could benefit from refactoring | "Extract PaymentProcessor class, consolidate validation logic, simplify nested conditionals" |
| `[DESIGN_PATTERNS]` | Design patterns used or recommended | "Repository pattern for data access, Factory for object creation, Strategy for payment methods" |
| `[ARCHITECTURE_COMPLIANCE]` | Adherence to architectural standards | "Follows hexagonal architecture, respects layer boundaries, uses defined interfaces" |
| `[SOLID_PRINCIPLES]` | Adherence to SOLID principles | "SRP: Each class has single purpose, OCP: Extensible via interfaces, DIP: Dependencies injected" |
| `[SEPARATION_OF_CONCERNS]` | Proper separation between layers | "Business logic isolated from presentation, data access abstracted, cross-cutting concerns centralized" |
| `[DEPENDENCY_MANAGEMENT]` | How dependencies are handled | "npm/pip packages pinned, no circular dependencies, minimal external dependencies" |
| `[INTERFACE_DESIGN]` | Quality of interface definitions | "Clear contracts, typed parameters, documented return values, versioned APIs" |
| `[ABSTRACTION_LEVEL]` | Appropriateness of abstraction | "Right level of abstraction, no leaky abstractions, appropriate use of generics" |
| `[COUPLING]` | Degree of interdependence between modules | "Loose coupling via interfaces, event-driven communication, dependency injection used" |
| `[COHESION]` | How well module elements belong together | "High cohesion, related functionality grouped, focused modules with clear purpose" |
| `[SCALABILITY_CONSIDERATIONS]` | Design for scale | "Stateless services, horizontal scaling ready, database sharding supported, caching layer" |
| `[ALGORITHM_EFFICIENCY]` | Efficiency of algorithms used | "Optimal sorting algorithm, efficient search using hash maps, streaming for large datasets" |
| `[TIME_COMPLEXITY]` | Time complexity analysis | "O(n log n) for sorting, O(1) for lookups, O(n) for list processing, no O(n^2) in hot paths" |
| `[SPACE_COMPLEXITY]` | Space complexity analysis | "O(n) memory usage, streaming processing for large files, no memory leaks detected" |
| `[MEMORY_USAGE]` | Memory consumption patterns | "Peak memory <512MB, proper cleanup of resources, no unbounded growth, weak references for caches" |
| `[RESOURCE_MANAGEMENT]` | Handling of system resources | "Connection pooling, file handles closed in finally blocks, context managers used" |
| `[CACHING_STRATEGY]` | Caching implementation approach | "Redis for session data, in-memory LRU for hot data, cache invalidation on updates, TTL: 1 hour" |
| `[DATABASE_OPERATIONS]` | Database interaction patterns | "Parameterized queries, batch operations for bulk updates, read replicas for queries" |
| `[IO_OPERATIONS]` | Input/output handling | "Async I/O for network calls, buffered file reading, streaming for large responses" |
| `[CONCURRENCY_HANDLING]` | Multi-threading and async handling | "Thread-safe collections, async/await patterns, no race conditions, proper lock usage" |
| `[PERFORMANCE_BOTTLENECKS]` | Identified performance issues | "N+1 query in user listing, synchronous external API call, unoptimized image processing" |
| `[INPUT_VALIDATION]` | Input validation implementation | "Joi/Zod schema validation, sanitization of HTML, length limits enforced, type checking" |
| `[OUTPUT_ENCODING]` | Output encoding for security | "HTML entity encoding, JSON serialization escaping, Content-Type headers set correctly" |
| `[AUTHENTICATION_IMPLEMENTATION]` | Authentication mechanism details | "JWT with RS256, refresh token rotation, session timeout 30min, MFA support" |
| `[AUTHORIZATION_CHECKS]` | Authorization control implementation | "RBAC with permission checks, resource-level access control, principle of least privilege" |
| `[DATA_ENCRYPTION]` | Encryption implementation | "AES-256 for data at rest, bcrypt cost factor 12 for passwords, TLS 1.3 in transit" |
| `[SECURE_COMMUNICATION]` | Secure communication protocols | "HTTPS enforced, certificate pinning for mobile, HSTS enabled, secure WebSocket" |
| `[ERROR_HANDLING_SECURITY]` | Security of error handling | "Generic error messages to users, detailed logs internally, no stack traces exposed" |
| `[LOGGING_SECURITY]` | Security considerations in logging | "PII masked in logs, no passwords logged, structured logging, log injection prevented" |
| `[SENSITIVE_DATA_HANDLING]` | Handling of sensitive information | "PII encrypted, credit cards tokenized, secrets in vault, data classification followed" |
| `[VULNERABILITY_ASSESSMENT]` | Security vulnerability analysis | "OWASP Top 10 checked, Snyk scan passed, no known CVEs in dependencies" |
| `[TEST_COVERAGE]` | Test coverage metrics | "Unit: 85%, Integration: 70%, E2E: 50% critical paths, branch coverage: 80%" |
| `[TEST_QUALITY]` | Quality of test implementations | "Meaningful assertions, isolated tests, no flaky tests, fast execution (<5min)" |
| `[TEST_CASES]` | Test case coverage | "Happy path, error cases, boundary conditions, null/empty inputs covered" |
| `[EDGE_CASES]` | Edge case handling | "Empty arrays, null values, max integer, unicode characters, concurrent access" |
| `[MOCK_USAGE]` | Use of mocks and stubs | "External services mocked, database stubbed for unit tests, realistic fixtures" |
| `[TEST_MAINTAINABILITY]` | Maintainability of tests | "Page Object pattern, shared fixtures, no test interdependence, clear naming" |
| `[INTEGRATION_TESTS]` | Integration test coverage | "API endpoint tests, database integration, third-party service contracts verified" |
| `[PERFORMANCE_TESTS]` | Performance test implementation | "Load tests with k6, p95 latency <200ms, 1000 concurrent users baseline" |
| `[SECURITY_TESTS]` | Security testing implementation | "OWASP ZAP scan passed, SQL injection tests, XSS prevention verified, auth bypass tests" |
| `[TEST_DOCUMENTATION]` | Documentation of test approach | "Test plan documented, coverage reports generated, test data management guide" |
| `[EXCEPTION_MANAGEMENT]` | Exception handling approach | "Custom exception hierarchy, specific catch blocks, no silent failures, proper propagation" |
| `[ERROR_MESSAGES]` | Error message quality | "User-friendly messages, error codes for support, actionable guidance, i18n ready" |
| `[GRACEFUL_DEGRADATION]` | Fallback behavior implementation | "Fallback to cache, degraded mode for non-critical features, partial results returned" |
| `[RECOVERY_MECHANISMS]` | Recovery from failures | "Automatic retry with backoff, dead letter queue for failed messages, self-healing" |
| `[LOGGING_STRATEGY]` | Logging implementation approach | "Structured JSON logs, correlation IDs, log levels appropriate, ELK stack integration" |
| `[MONITORING_INTEGRATION]` | Monitoring system integration | "Prometheus metrics, custom dashboards, business KPI tracking, distributed tracing" |
| `[ALERTING]` | Alert configuration | "PagerDuty integration, severity-based routing, runbook links, alert fatigue prevention" |
| `[TIMEOUT_HANDLING]` | Timeout configuration and handling | "30s API timeout, 5s database timeout, timeout exceptions handled, user notification" |
| `[CIRCUIT_BREAKER]` | Circuit breaker implementation | "Hystrix/Resilience4j pattern, 50% failure threshold, 30s open state, half-open testing" |
| `[RETRY_LOGIC]` | Retry mechanism implementation | "Exponential backoff, max 3 retries, jitter added, idempotency ensured, non-retriable errors excluded" |
| `[CODING_STANDARDS]` | Coding standard adherence | "Google Style Guide, team conventions documented, consistent across codebase" |
| `[STYLE_GUIDE]` | Style guide followed | "Airbnb JavaScript, PEP 8 for Python, team-specific extensions documented" |
| `[FORMATTING]` | Code formatting approach | "Prettier configured, consistent indentation (2 spaces), max line length 100, auto-format on save" |
| `[LINTING_RESULTS]` | Linting tool results | "ESLint: 0 errors, 3 warnings, Pylint: 9.5/10 score, all rules enforced in CI" |
| `[STATIC_ANALYSIS]` | Static analysis results | "SonarQube: A rating, 0 critical issues, 2 minor code smells, no security hotspots" |
| `[TYPE_SAFETY]` | Type safety implementation | "TypeScript strict mode, no any types, runtime validation at boundaries, generics used appropriately" |
| `[DOCUMENTATION_STANDARDS]` | Documentation requirements | "JSDoc for public APIs, README per module, architecture diagrams updated, changelog maintained" |
| `[COMMIT_MESSAGE_QUALITY]` | Commit message standards | "Conventional commits, descriptive messages, issue references, atomic commits" |
| `[BRANCH_STRATEGY]` | Branch naming and management | "GitFlow, feature/JIRA-123-description format, squash merge to main" |
| `[VERSION_CONTROL]` | Version control practices | "Semantic versioning, tagged releases, protected main branch, required reviews" |
| `[QUERY_OPTIMIZATION]` | Database query optimization | "EXPLAIN ANALYZE run, indexes used, no full table scans, query time <100ms" |
| `[INDEX_USAGE]` | Database index utilization | "Composite indexes for common queries, covering indexes used, no redundant indexes" |
| `[TRANSACTION_MANAGEMENT]` | Transaction handling | "ACID compliance, appropriate isolation levels, short transactions, deadlock prevention" |
| `[CONNECTION_MANAGEMENT]` | Database connection handling | "Connection pooling (HikariCP), pool size: 10-50, connection timeout: 30s, leak detection" |
| `[DATA_INTEGRITY]` | Data integrity measures | "Foreign key constraints, unique constraints, check constraints, referential integrity" |
| `[SCHEMA_DESIGN]` | Database schema quality | "Normalized to 3NF, appropriate denormalization for read performance, clear naming" |
| `[MIGRATION_SCRIPTS]` | Database migration approach | "Flyway/Liquibase migrations, reversible scripts, version controlled, tested in staging" |
| `[BACKUP_CONSIDERATIONS]` | Data backup approach | "Daily automated backups, point-in-time recovery, cross-region replication, tested restore" |
| `[DB_PERFORMANCE_IMPACT]` | Database performance effects | "New queries analyzed, index impact assessed, no table locks, minimal load increase" |
| `[CONCURRENCY_CONTROL]` | Database concurrency handling | "Optimistic locking with version field, row-level locks, conflict resolution strategy" |
| `[API_DESIGN]` | API design quality | "RESTful principles, OpenAPI 3.0 documented, versioned /v1/, consistent naming" |
| `[REST_COMPLIANCE]` | REST standards adherence | "Proper HTTP methods, HATEOAS links, stateless, resource-oriented URLs" |
| `[REQUEST_RESPONSE_FORMAT]` | API data format | "JSON with camelCase, consistent pagination format, envelope pattern for lists" |
| `[STATUS_CODES]` | HTTP status code usage | "200/201/204 for success, 400/401/403/404 for client errors, 500/503 for server errors" |
| `[ERROR_RESPONSES]` | API error response format | "RFC 7807 Problem Details, error codes, helpful messages, documentation links" |
| `[VERSIONING_STRATEGY]` | API versioning approach | "URL path versioning /v1/, backward compatible changes, deprecation notices, migration guides" |
| `[API_DOCUMENTATION]` | API documentation quality | "OpenAPI/Swagger spec, interactive docs, request/response examples, authentication guide" |
| `[RATE_LIMITING]` | Rate limiting implementation | "100 requests/minute per user, 429 responses with Retry-After, token bucket algorithm" |
| `[CACHING_HEADERS]` | HTTP caching headers | "ETag for conditional requests, Cache-Control: max-age=3600, Vary headers set" |
| `[CORS_IMPLEMENTATION]` | CORS configuration | "Allowed origins whitelist, credentials support, preflight caching, restricted methods" |
| `[UI_UX_IMPLEMENTATION]` | UI/UX implementation quality | "Design system components, consistent spacing, loading states, error boundaries" |
| `[RESPONSIVE_DESIGN]` | Responsive design implementation | "Mobile-first approach, breakpoints at 768px/1024px/1440px, fluid typography" |
| `[ACCESSIBILITY]` | Accessibility compliance | "WCAG 2.1 AA compliant, keyboard navigation, screen reader tested, color contrast 4.5:1" |
| `[FRONTEND_PERFORMANCE]` | Frontend performance metrics | "LCP <2.5s, FID <100ms, CLS <0.1, bundle size <200KB gzipped, code splitting" |
| `[BROWSER_COMPATIBILITY]` | Browser support | "Chrome 90+, Firefox 88+, Safari 14+, Edge 90+, graceful degradation for IE11" |
| `[JAVASCRIPT_QUALITY]` | JavaScript code quality | "ES2020+ features, no var usage, proper async handling, no memory leaks, TypeScript strict" |
| `[CSS_ORGANIZATION]` | CSS architecture | "CSS Modules/Tailwind, BEM naming, no !important, design tokens, theme support" |
| `[ASSET_OPTIMIZATION]` | Asset optimization approach | "Images: WebP with fallback, lazy loading, responsive images, SVG for icons, CDN delivery" |
| `[SEO_CONSIDERATIONS]` | SEO implementation | "Meta tags, semantic HTML, structured data, sitemap, canonical URLs, SSR/SSG" |
| `[PROGRESSIVE_ENHANCEMENT]` | Progressive enhancement approach | "Core functionality without JS, service worker for offline, lazy loading enhancements" |
| `[CONTAINERIZATION]` | Container implementation | "Multi-stage Dockerfile, Alpine base image, non-root user, health checks, <100MB image" |
| `[CONFIGURATION_MANAGEMENT]` | Configuration handling | "12-factor app config, environment-based settings, secrets management, feature flags" |
| `[ENVIRONMENT_VARIABLES]` | Environment variable usage | "Validated at startup, documented in .env.example, no defaults for secrets, type-safe" |
| `[DEPLOYMENT_SCRIPTS]` | Deployment automation | "Helm charts, Terraform modules, idempotent scripts, rollback capability, blue-green ready" |
| `[CICD_INTEGRATION]` | CI/CD pipeline integration | "GitHub Actions/GitLab CI, automated tests, security scans, staging deployment, approval gates" |
| `[MONITORING_SETUP]` | Production monitoring | "Datadog/New Relic APM, custom metrics, distributed tracing, log aggregation, dashboards" |
| `[LOGGING_CONFIGURATION]` | Logging setup | "JSON structured logs, log levels configurable, rotation configured, centralized collection" |
| `[HEALTH_CHECKS]` | Health check implementation | "/health endpoint, liveness/readiness probes, dependency checks, detailed status response" |
| `[SCALING_CONFIGURATION]` | Auto-scaling setup | "HPA configured, CPU/memory thresholds 70%, min 2 replicas, max 10, scale-down delay 5min" |
| `[SECURITY_CONFIGURATION]` | Security settings | "Network policies, secrets in Kubernetes secrets/Vault, RBAC, pod security policies" |
| `[CODE_COMMENTS]` | In-code comment quality | "Complex logic explained, TODO with ticket references, no outdated comments, API documented" |
| `[API_DOCUMENTATION_REVIEW]` | API docs completeness | "All endpoints documented, request/response examples, error codes listed, changelog current" |
| `[README_FILES]` | README file quality | "Setup instructions, prerequisites, development workflow, deployment guide, troubleshooting" |
| `[ARCHITECTURE_DOCUMENTATION]` | Architecture docs status | "System diagrams current, ADRs for decisions, component interactions documented, data flow charts" |
| `[DEPLOYMENT_INSTRUCTIONS]` | Deployment documentation | "Step-by-step guide, environment requirements, rollback procedures, verification steps" |
| `[TROUBLESHOOTING_GUIDES]` | Troubleshooting documentation | "Common issues documented, debug procedures, log analysis guide, escalation path" |
| `[CHANGE_LOGS]` | Changelog maintenance | "CHANGELOG.md updated, semantic versioning, breaking changes highlighted, migration notes" |
| `[USER_GUIDES]` | End-user documentation | "Feature documentation, screenshots, video tutorials, FAQ section, searchable help center" |
| `[DEVELOPER_GUIDES]` | Developer documentation | "Onboarding guide, coding standards, architecture overview, local setup, contribution guide" |
| `[KNOWLEDGE_TRANSFER]` | Knowledge sharing approach | "Documentation reviewed, pair programming session, recorded demo, Q&A completed" |
| `[REQUIREMENTS_COMPLIANCE]` | Requirements fulfillment | "All acceptance criteria met, edge cases handled, non-functional requirements verified" |
| `[BUSINESS_RULES]` | Business rule implementation | "Discount calculation accurate, tax rules applied correctly, regulatory compliance met" |
| `[DATA_VALIDATION]` | Business data validation | "Email format validated, phone number normalized, date ranges enforced, currency precision" |
| `[WORKFLOW_IMPLEMENTATION]` | Workflow logic correctness | "State machine transitions correct, approval flows implemented, notifications triggered" |
| `[BUSINESS_EDGE_CASES]` | Business edge case handling | "Zero quantity orders, expired promotions, concurrent bookings, timezone boundaries" |
| `[INTEGRATION_POINTS]` | External integration design | "Stripe payment, SendGrid email, Twilio SMS, documented contracts, error handling" |
| `[EXTERNAL_DEPENDENCIES]` | Third-party dependency assessment | "Vendor reliability, SLA compliance, fallback options, version compatibility" |
| `[BACKWARD_COMPATIBILITY]` | Backward compatibility maintenance | "API v1 still supported, database migrations non-breaking, feature flags for gradual rollout" |
| `[MIGRATION_STRATEGY]` | Data migration approach | "Incremental migration, dual-write period, data validation, rollback plan, zero downtime" |
| `[ROLLBACK_PLANS]` | Rollback procedures | "Database rollback scripts tested, feature flags for instant disable, previous version tagged" |
| `[CYCLOMATIC_COMPLEXITY]` | Complexity metric values | "Average: 5, Max: 15, functions >10 flagged, simplified with extract method refactoring" |
| `[LINES_OF_CODE]` | Lines of code metrics | "Feature: 450 LOC, tests: 320 LOC, no file >300 lines, functions <50 lines average" |
| `[CODE_COVERAGE_METRICS]` | Detailed coverage metrics | "Line: 87%, Branch: 82%, Function: 91%, critical paths: 95%, new code: 90%" |
| `[TECHNICAL_DEBT_RATIO]` | Technical debt measurement | "SonarQube: 3.2% ratio, 4 hours estimated remediation, prioritized in backlog" |
| `[DUPLICATION_RATIO]` | Code duplication metrics | "3.1% duplication, 2 blocks identified, extraction planned for next sprint" |
| `[MAINTAINABILITY_INDEX]` | Maintainability score | "SonarQube: A rating, 85/100 maintainability index, no critical maintainability issues" |
| `[COUPLING_METRICS]` | Module coupling measurements | "Afferent coupling: 3, Efferent coupling: 5, instability: 0.63, within acceptable range" |
| `[COHESION_METRICS]` | Module cohesion measurements | "LCOM4: 1 (ideal), no god classes, single responsibility verified" |
| `[DEFECT_DENSITY]` | Defect density metric | "0.5 defects per KLOC, below team target of 1.0, trending downward" |
| `[CODE_QUALITY_SCORE]` | Overall quality score | "SonarQube: A rating, 0 critical issues, 2 major issues, 5 minor code smells" |
| `[STRENGTHS]` | Code strengths identified | "Clean separation of concerns, comprehensive error handling, excellent test coverage" |
| `[AREAS_FOR_IMPROVEMENT]` | Improvement areas identified | "Add more integration tests, improve logging consistency, document edge cases better" |
| `[CRITICAL_ISSUES]` | Critical issues found | "SQL injection vulnerability in search, missing authentication on admin endpoint" |
| `[MAJOR_ISSUES]` | Major issues found | "N+1 query in user list, missing input validation on file upload, no rate limiting" |
| `[MINOR_ISSUES]` | Minor issues found | "Inconsistent error message format, TODO comment without ticket, unused import statements" |
| `[SUGGESTIONS]` | Improvement suggestions | "Consider caching for repeated queries, extract validation logic to middleware, add OpenTelemetry" |
| `[BEST_PRACTICES_FEEDBACK]` | Best practices adherence | "Excellent use of dependency injection, good logging practices, clean commit history" |
| `[LEARNING_OPPORTUNITIES]` | Learning recommendations | "Review circuit breaker patterns, explore property-based testing, study CQRS pattern" |
| `[ACTION_ITEMS]` | Required action items | "Fix SQL injection (P0), add rate limiting (P1), improve test coverage to 85% (P2)" |
| `[FOLLOW_UP_REQUIRED]` | Follow-up requirements | "Security review after SQL fix, performance test after caching, architecture review for v2" |
| `[CODE_QUALITY_GATE]` | Quality gate criteria | "SonarQube A rating, 0 critical issues, <5% duplication, 80% coverage minimum" |
| `[SECURITY_GATE]` | Security gate criteria | "OWASP ZAP scan passed, no high/critical findings, dependency scan clean" |
| `[PERFORMANCE_GATE]` | Performance gate criteria | "API response <200ms p95, throughput >500 RPS, no memory leaks under load" |
| `[TEST_COVERAGE_GATE]` | Coverage gate criteria | "80% line coverage minimum, 100% critical path coverage, no decrease from baseline" |
| `[DOCUMENTATION_GATE]` | Documentation requirements | "All public APIs documented, README updated, changelog entry added, architecture current" |
| `[STANDARDS_COMPLIANCE]` | Standards compliance verification | "ESLint/Prettier passed, type checking passed, security scan passed, all CI checks green" |
| `[BUSINESS_REQUIREMENTS_GATE]` | Business requirements verification | "All acceptance criteria verified, PO sign-off obtained, demo completed, UAT passed" |
| `[DEPLOYMENT_READINESS]` | Deployment readiness assessment | "Staging tested, monitoring configured, runbook updated, rollback verified, team notified" |
| `[RISK_ASSESSMENT]` | Risk level assessment | "Low risk: isolated feature, Medium risk: affects payment flow, High risk: database migration" |
| `[APPROVAL_STATUS]` | Review approval decision | "Approved, Approved with minor changes, Changes requested, Blocked pending security fix" |
| `[IMMEDIATE_FIXES]` | Fixes required before merge | "Fix SQL injection vulnerability, add missing null check, correct error status code" |
| `[SHORT_TERM_IMPROVEMENTS]` | Improvements for next sprint | "Add integration tests for payment flow, implement request validation, optimize database queries" |
| `[LONG_TERM_REFACTORING]` | Future refactoring plans | "Migrate to event-driven architecture, extract payment service, implement CQRS pattern" |
| `[PERFORMANCE_OPTIMIZATIONS]` | Performance improvement recommendations | "Add Redis caching for user sessions, implement database connection pooling, optimize image loading" |
| `[SECURITY_ENHANCEMENTS]` | Security improvement recommendations | "Implement rate limiting, add CSRF protection, enable security headers, audit logging" |
| `[CODE_QUALITY_IMPROVEMENTS]` | Code quality recommendations | "Extract common validation logic, reduce function complexity, add integration test coverage" |
| `[DOCUMENTATION_UPDATES]` | Documentation update requirements | "Update API docs with new endpoints, add architecture diagram, update deployment guide" |
| `[TESTING_ENHANCEMENTS]` | Testing improvement recommendations | "Add contract tests for external APIs, implement mutation testing, increase edge case coverage" |
| `[ARCHITECTURE_CHANGES]` | Architecture change recommendations | "Consider message queue for async processing, evaluate microservice extraction, implement API gateway" |
| `[TOOL_RECOMMENDATIONS]` | Tool and library suggestions | "Adopt SonarQube for quality gates, implement Sentry for error tracking, use k6 for load testing" |
| `[REVIEW_DISCUSSION]` | Discussion points from review | "Discussed caching strategy, agreed on error handling approach, clarified business requirements" |
| `[CLARIFICATIONS_NEEDED]` | Items requiring clarification | "Confirm expected behavior for edge case X, verify security requirements with team, check API contract" |
| `[KNOWLEDGE_SHARING]` | Knowledge transfer notes | "Explained new authentication flow, shared best practices for error handling, documented design decisions" |
| `[MENTORING_OPPORTUNITIES]` | Mentoring suggestions | "Pair on TDD approach, review design patterns together, walk through architecture decisions" |
| `[TEAM_LEARNING]` | Team learning opportunities | "Share findings on performance optimization, present security best practices, document lessons learned" |
| `[PROCESS_IMPROVEMENTS]` | Process improvement suggestions | "Add automated security scanning, implement code review checklist, define quality gates in CI" |
| `[TOOL_USAGE]` | Tool usage observations | "Leverage IDE refactoring tools, use pre-commit hooks, adopt code coverage reporting" |
| `[COMMUNICATION_STYLE]` | Feedback communication approach | "Constructive and specific, focused on code not author, includes positive reinforcement" |
| `[FEEDBACK_QUALITY]` | Quality of review feedback | "Actionable suggestions with examples, prioritized by impact, includes references and resources" |
| `[RESOLUTION_TRACKING]` | Issue resolution tracking | "GitHub issue #123 created, Jira ticket PROJ-456 linked, follow-up review scheduled for Friday" |

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