---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- design
- documentation
- optimization
- security
- testing
title: Code Generation Template
use_cases:
- Creating generate high-quality code including functions, classes, algorithms, and
  complete applications with comprehensive documentation and best practices.
- Project planning and execution
- Strategy development
industries:
- government
- manufacturing
- technology
type: template
difficulty: intermediate
slug: code-generation
---

# Code Generation Template

## Purpose
Generate high-quality code including functions, classes, algorithms, and complete applications with comprehensive documentation and best practices.

## Quick Code Generation Prompt
Generate [language] [code type: function/class/module/API] that [functionality]. Requirements: [inputs], [outputs], [edge cases]. Include: type hints/annotations, docstrings, error handling, [X] unit tests with [pytest/Jest/etc]. Follow: [coding standard], SOLID principles, clean code practices. Performance: [O(n) target], handle [scale requirements].

## Quick Start

**Need to generate code quickly?** Use this minimal example:

### Minimal Example
```
Generate a Python function that validates email addresses using regex. The function should:
- Accept an email string as input
- Return True if valid, False if invalid
- Handle edge cases (empty strings, special characters)
- Include docstring documentation and 3 unit tests with pytest
```

### When to Use This
- Creating new functions, classes, or modules from scratch
- Need production-ready code with tests and documentation
- Want to follow best practices and coding standards
- Building APIs, algorithms, or data processing pipelines

### Basic 3-Step Workflow
1. **Specify requirements** - Define what the code should do and constraints
2. **Add context** - Mention language, framework, and key dependencies
3. **Request quality features** - Ask for tests, docs, and error handling

**Time to complete**: 5-15 minutes for functions, 30-60 minutes for complex classes

---

## Template Structure

### Project Context
- **Programming Language**: [PROGRAMMING_LANGUAGE]
- **Framework/Library**: [FRAMEWORK]
- **Version**: [VERSION]
- **Target Platform**: [TARGET_PLATFORM]
- **Architecture Pattern**: [ARCHITECTURE_PATTERN]
- **Code Style Guide**: [STYLE_GUIDE]
- **Testing Framework**: [TESTING_FRAMEWORK]
- **Documentation Standard**: [DOCUMENTATION_STANDARD]

### Requirements Specification
- **Primary Functionality**: [PRIMARY_FUNCTIONALITY]
- **Business Logic**: [BUSINESS_LOGIC]
- **Performance Requirements**: [PERFORMANCE_REQUIREMENTS]
- **Security Requirements**: [SECURITY_REQUIREMENTS]
- **Scalability Requirements**: [SCALABILITY_REQUIREMENTS]
- **Integration Requirements**: [INTEGRATION_REQUIREMENTS]
- **Compliance Requirements**: [COMPLIANCE_REQUIREMENTS]
- **Accessibility Requirements**: [ACCESSIBILITY_REQUIREMENTS]

### Function/Method Generation
- **Function Name**: [FUNCTION_NAME]
- **Purpose**: [FUNCTION_PURPOSE]
- **Input Parameters**: [INPUT_PARAMETERS]
- **Parameter Types**: [PARAMETER_TYPES]
- **Parameter Validation**: [PARAMETER_VALIDATION]
- **Return Type**: [RETURN_TYPE]
- **Return Value**: [RETURN_VALUE]
- **Exception Handling**: [EXCEPTION_HANDLING]
- **Error Messages**: [ERROR_MESSAGES]
- **Logging Level**: [LOGGING_LEVEL]
- **Performance Considerations**: [PERFORMANCE_CONSIDERATIONS]

### Class/Object Generation
- **Class Name**: [CLASS_NAME]
- **Class Purpose**: [CLASS_PURPOSE]
- **Inheritance**: [INHERITANCE]
- **Interfaces/Protocols**: [INTERFACES]
- **Properties**: [PROPERTIES]
- **Property Types**: [PROPERTY_TYPES]
- **Constructor Parameters**: [CONSTRUCTOR_PARAMETERS]
- **Methods**: [METHODS]
- **Static Methods**: [STATIC_METHODS]
- **Private Methods**: [PRIVATE_METHODS]
- **Abstract Methods**: [ABSTRACT_METHODS]
- **Method Visibility**: [METHOD_VISIBILITY]

### Algorithm Implementation
- **Algorithm Type**: [ALGORITHM_TYPE]
- **Complexity Requirements**: [COMPLEXITY_REQUIREMENTS]
- **Time Complexity**: [TIME_COMPLEXITY]
- **Space Complexity**: [SPACE_COMPLEXITY]
- **Input Size**: [INPUT_SIZE]
- **Data Structures**: [DATA_STRUCTURES]
- **Optimization Strategy**: [OPTIMIZATION_STRATEGY]
- **Edge Cases**: [EDGE_CASES]
- **Mathematical Formulas**: [MATHEMATICAL_FORMULAS]
- **Pseudocode**: [PSEUDOCODE]

### Code Quality Standards
- **Naming Conventions**: [NAMING_CONVENTIONS]
- **Code Formatting**: [CODE_FORMATTING]
- **Comment Style**: [COMMENT_STYLE]
- **Documentation Strings**: [DOCUMENTATION_STRINGS]
- **Type Hints**: [TYPE_HINTS]
- **Code Coverage**: [CODE_COVERAGE]
- **Static Analysis**: [STATIC_ANALYSIS]
- **Linting Rules**: [LINTING_RULES]
- **Code Metrics**: [CODE_METRICS]
- **Technical Debt**: [TECHNICAL_DEBT]

### Testing Specifications
- **Unit Test Requirements**: [UNIT_TEST_REQUIREMENTS]
- **Test Cases**: [TEST_CASES]
- **Mock Objects**: [MOCK_OBJECTS]
- **Test Data**: [TEST_DATA]
- **Assertion Types**: [ASSERTION_TYPES]
- **Edge Case Tests**: [EDGE_CASE_TESTS]
- **Performance Tests**: [PERFORMANCE_TESTS]
- **Integration Tests**: [INTEGRATION_TESTS]
- **Regression Tests**: [REGRESSION_TESTS]
- **Coverage Targets**: [COVERAGE_TARGETS]

### Documentation Requirements
- **API Documentation**: [API_DOCUMENTATION]
- **Code Comments**: [CODE_COMMENTS]
- **Usage Examples**: [USAGE_EXAMPLES]
- **Installation Guide**: [INSTALLATION_GUIDE]
- **Configuration Guide**: [CONFIGURATION_GUIDE]
- **Troubleshooting Guide**: [TROUBLESHOOTING_GUIDE]
- **Change Log**: [CHANGE_LOG]
- **License Information**: [LICENSE_INFORMATION]
- **Contributing Guidelines**: [CONTRIBUTING_GUIDELINES]
- **Code Examples**: [CODE_EXAMPLES]

### Database Integration
- **Database Type**: [DATABASE_TYPE]
- **Connection String**: [CONNECTION_STRING]
- **Query Language**: [QUERY_LANGUAGE]
- **ORM Framework**: [ORM_FRAMEWORK]
- **Database Schema**: [DATABASE_SCHEMA]
- **Table Names**: [TABLE_NAMES]
- **Column Names**: [COLUMN_NAMES]
- **Relationships**: [RELATIONSHIPS]
- **Indexes**: [INDEXES]
- **Transactions**: [TRANSACTIONS]

### API Integration
- **API Type**: [API_TYPE]
- **API Version**: [API_VERSION]
- **Authentication Method**: [AUTHENTICATION_METHOD]
- **API Key**: [API_KEY]
- **Endpoints**: [ENDPOINTS]
- **HTTP Methods**: [HTTP_METHODS]
- **Request Headers**: [REQUEST_HEADERS]
- **Request Body**: [REQUEST_BODY]
- **Response Format**: [RESPONSE_FORMAT]
- **Error Handling**: [API_ERROR_HANDLING]

### User Interface Components
- **UI Framework**: [UI_FRAMEWORK]
- **Component Type**: [COMPONENT_TYPE]
- **Component Properties**: [COMPONENT_PROPERTIES]
- **Event Handlers**: [EVENT_HANDLERS]
- **State Management**: [STATE_MANAGEMENT]
- **Styling Approach**: [STYLING_APPROACH]
- **Responsive Design**: [RESPONSIVE_DESIGN]
- **Accessibility Features**: [ACCESSIBILITY_FEATURES]
- **Browser Support**: [BROWSER_SUPPORT]
- **Mobile Support**: [MOBILE_SUPPORT]

### Configuration Management
- **Configuration Files**: [CONFIGURATION_FILES]
- **Environment Variables**: [ENVIRONMENT_VARIABLES]
- **Default Values**: [DEFAULT_VALUES]
- **Configuration Validation**: [CONFIGURATION_VALIDATION]
- **Runtime Configuration**: [RUNTIME_CONFIGURATION]
- **Feature Flags**: [FEATURE_FLAGS]
- **Logging Configuration**: [LOGGING_CONFIGURATION]
- **Security Configuration**: [SECURITY_CONFIGURATION]
- **Performance Configuration**: [PERFORMANCE_CONFIGURATION]
- **Debug Settings**: [DEBUG_SETTINGS]

### Security Implementation
- **Authentication**: [AUTHENTICATION]
- **Authorization**: [AUTHORIZATION]
- **Input Validation**: [INPUT_VALIDATION]
- **Output Encoding**: [OUTPUT_ENCODING]
- **SQL Injection Prevention**: [SQL_INJECTION_PREVENTION]
- **XSS Prevention**: [XSS_PREVENTION]
- **CSRF Protection**: [CSRF_PROTECTION]
- **Encryption Methods**: [ENCRYPTION_METHODS]
- **Secure Communications**: [SECURE_COMMUNICATIONS]
- **Audit Logging**: [AUDIT_LOGGING]

### Performance Optimization
- **Caching Strategy**: [CACHING_STRATEGY]
- **Memory Management**: [MEMORY_MANAGEMENT]
- **CPU Optimization**: [CPU_OPTIMIZATION]
- **I/O Optimization**: [IO_OPTIMIZATION]
- **Database Optimization**: [DATABASE_OPTIMIZATION]
- **Network Optimization**: [NETWORK_OPTIMIZATION]
- **Lazy Loading**: [LAZY_LOADING]
- **Parallel Processing**: [PARALLEL_PROCESSING]
- **Asynchronous Processing**: [ASYNCHRONOUS_PROCESSING]
- **Resource Pooling**: [RESOURCE_POOLING]

### Deployment Configuration
- **Deployment Environment**: [DEPLOYMENT_ENVIRONMENT]
- **Build Process**: [BUILD_PROCESS]
- **Package Management**: [PACKAGE_MANAGEMENT]
- **Dependency Management**: [DEPENDENCY_MANAGEMENT]
- **Version Control**: [VERSION_CONTROL]
- **CI/CD Pipeline**: [CICD_PIPELINE]
- **Container Configuration**: [CONTAINER_CONFIGURATION]
- **Load Balancing**: [LOAD_BALANCING]
- **Monitoring Setup**: [MONITORING_SETUP]
- **Backup Strategy**: [BACKUP_STRATEGY]

### Maintenance and Support
- **Code Maintainability**: [CODE_MAINTAINABILITY]
- **Refactoring Guidelines**: [REFACTORING_GUIDELINES]
- **Bug Tracking**: [BUG_TRACKING]
- **Issue Resolution**: [ISSUE_RESOLUTION]
- **Code Reviews**: [CODE_REVIEWS]
- **Knowledge Transfer**: [KNOWLEDGE_TRANSFER]
- **Support Documentation**: [SUPPORT_DOCUMENTATION]
- **Training Materials**: [TRAINING_MATERIALS]
- **User Feedback**: [USER_FEEDBACK]
- **Continuous Improvement**: [CONTINUOUS_IMPROVEMENT]

## Prompt Template

Generate [PROGRAMMING_LANGUAGE] code for [PRIMARY_FUNCTIONALITY] using [FRAMEWORK] framework. The code should implement [ALGORITHM_TYPE] with [TIME_COMPLEXITY] time complexity and include:

**Core Implementation:**
- [FUNCTION_NAME] function that [FUNCTION_PURPOSE]
- Input parameters: [INPUT_PARAMETERS] of types [PARAMETER_TYPES]
- Return type: [RETURN_TYPE] with [RETURN_VALUE]
- Handle [EDGE_CASES] and implement [EXCEPTION_HANDLING]

**Class Structure:** (if applicable)
- [CLASS_NAME] class inheriting from [INHERITANCE]
- Properties: [PROPERTIES] with types [PROPERTY_TYPES]
- Methods: [METHODS] with [METHOD_VISIBILITY]
- Constructor accepting [CONSTRUCTOR_PARAMETERS]

**Quality Requirements:**
- Follow [STYLE_GUIDE] coding standards
- Include [DOCUMENTATION_STRINGS] documentation
- Add [CODE_COMMENTS] for complex logic
- Implement [UNIT_TEST_REQUIREMENTS] unit tests
- Achieve [CODE_COVERAGE]% test coverage

**Integration Requirements:**
- Connect to [DATABASE_TYPE] database using [ORM_FRAMEWORK]
- Integrate with [API_TYPE] API using [AUTHENTICATION_METHOD]
- Handle [REQUEST_HEADERS] and [RESPONSE_FORMAT]
- Implement [CACHING_STRATEGY] for performance

**Security Implementation:**
- Add [INPUT_VALIDATION] for all inputs
- Implement [AUTHENTICATION] and [AUTHORIZATION]
- Prevent [SQL_INJECTION_PREVENTION] and [XSS_PREVENTION]
- Use [ENCRYPTION_METHODS] for sensitive data

**Performance Optimization:**
- Implement [OPTIMIZATION_STRATEGY] for efficiency
- Use [PARALLEL_PROCESSING] where appropriate
- Add [MEMORY_MANAGEMENT] for resource efficiency
- Include [LOGGING_LEVEL] logging with [AUDIT_LOGGING]

**Documentation:**
- Generate [API_DOCUMENTATION] with examples
- Include [USAGE_EXAMPLES] and [INSTALLATION_GUIDE]
- Add [TROUBLESHOOTING_GUIDE] for common issues
- Create [CONFIGURATION_GUIDE] for setup

Please ensure the code is production-ready, follows [COMPLIANCE_REQUIREMENTS], supports [TARGET_PLATFORM], and includes comprehensive error handling with meaningful [ERROR_MESSAGES]. The implementation should be scalable to handle [SCALABILITY_REQUIREMENTS] and maintain [PERFORMANCE_REQUIREMENTS].

## Usage Examples

### Basic Function Generation
```
Generate Python code for data validation using pandas framework. The code should implement input_sanitizer algorithm with O(n) time complexity and include:

Core Implementation:
- validate_user_input function that sanitizes and validates user form data
- Input parameters: raw_data (dict), validation_rules (list) of types dict and list
- Return type: dict with cleaned and validated data
- Handle empty fields, invalid formats and implement ValueError exceptions

Quality Requirements:
- Follow PEP8 coding standards
- Include docstring documentation
- Add inline comments for regex patterns
- Implement pytest unit tests
- Achieve 95% test coverage
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[PROGRAMMING_LANGUAGE]` | Specify the programming language | "Python 3.11", "TypeScript 5.x", "Java 17", "Go 1.21", "Rust 1.70" |
| `[FRAMEWORK]` | Specify the framework | "FastAPI", "Express.js", "Spring Boot 3.x", "Django 4.x", "NestJS" |
| `[VERSION]` | Specify the version | "3.11.0", "18.2.0", "17.0.2", "1.21.0", "5.2.0" |
| `[TARGET_PLATFORM]` | Specify the target platform | "Linux (Ubuntu 22.04)", "AWS Lambda", "Kubernetes", "Docker containers", "Serverless" |
| `[ARCHITECTURE_PATTERN]` | Specify the architecture pattern | "Clean Architecture", "Hexagonal (Ports & Adapters)", "MVC", "CQRS", "Event-driven" |
| `[STYLE_GUIDE]` | Specify the style guide | "PEP 8 for Python", "Airbnb JavaScript Style Guide", "Google Java Style", "Effective Go", "Rust API Guidelines" |
| `[TESTING_FRAMEWORK]` | Specify the testing framework | "pytest with pytest-cov", "Jest with Testing Library", "JUnit 5 with Mockito", "Go testing package", "Vitest" |
| `[DOCUMENTATION_STANDARD]` | Specify the documentation standard | "Google docstrings", "JSDoc with TypeDoc", "Javadoc", "GoDoc", "rustdoc" |
| `[PRIMARY_FUNCTIONALITY]` | Specify the primary functionality | "RESTful API for user management", "Payment processing service", "Data validation pipeline", "Authentication middleware", "File upload handler" |
| `[BUSINESS_LOGIC]` | Specify the business logic | "Order total calculation with discounts and taxes", "Inventory stock management with reservations", "User role-based access control", "Subscription billing cycles" |
| `[PERFORMANCE_REQUIREMENTS]` | Specify the performance requirements | "< 100ms response time for 95th percentile", "Handle 1000 concurrent requests", "Process 10K records/second", "Memory footprint < 512MB" |
| `[SECURITY_REQUIREMENTS]` | Specify the security requirements | "Input validation and sanitization", "SQL injection prevention with parameterized queries", "XSS protection", "CSRF tokens", "Rate limiting" |
| `[SCALABILITY_REQUIREMENTS]` | Specify the scalability requirements | "Horizontal scaling with stateless design", "Support 10x traffic growth", "Connection pooling for database", "Async processing for heavy operations" |
| `[INTEGRATION_REQUIREMENTS]` | Specify the integration requirements | "REST API with OpenAPI 3.0 spec", "GraphQL endpoint", "Webhook callbacks", "Message queue (RabbitMQ/Kafka)", "gRPC for internal services" |
| `[COMPLIANCE_REQUIREMENTS]` | Specify the compliance requirements | "GDPR data handling", "PCI DSS for payment data", "HIPAA for health information", "SOC 2 audit logging", "WCAG 2.1 AA accessibility" |
| `[ACCESSIBILITY_REQUIREMENTS]` | Specify the accessibility requirements | "ARIA labels for screen readers", "Keyboard navigation support", "Color contrast ratio 4.5:1", "Focus indicators", "Alt text for images" |
| `[FUNCTION_NAME]` | Specify the function name | "validate_user_input", "calculate_order_total", "process_payment", "generate_auth_token", "fetch_user_data" |
| `[FUNCTION_PURPOSE]` | Specify the function purpose | "Validates and sanitizes user form data", "Calculates order total with discounts and taxes", "Processes payment transactions via Stripe API", "Generates JWT tokens for authentication" |
| `[INPUT_PARAMETERS]` | Specify the input parameters | "user_data: dict, validation_rules: list", "items: List[OrderItem], coupon_code: Optional[str]", "request: PaymentRequest, api_key: str" |
| `[PARAMETER_TYPES]` | Specify the parameter types | "dict, list, Optional[str]", "int, float, bool, List[T]", "str, bytes, datetime", "Union[str, int], Callable[[T], R]" |
| `[PARAMETER_VALIDATION]` | Specify the parameter validation | "Pydantic model validation", "Type hints with runtime checking", "JSON Schema validation", "Custom validator decorators", "assert statements for preconditions" |
| `[RETURN_TYPE]` | Specify the return type | "dict", "Optional[User]", "Result[T, Error]", "List[ValidationError]", "Tuple[bool, str]", "AsyncIterator[Event]" |
| `[RETURN_VALUE]` | Specify the return value | "Cleaned and validated data dictionary", "User object if found, None otherwise", "Success/failure result with error details", "List of validation errors (empty if valid)" |
| `[EXCEPTION_HANDLING]` | Specify the exception handling | "try/except with specific exception types", "Custom exceptions (ValidationError, NotFoundError)", "Context managers for resource cleanup", "Error boundaries with fallback values" |
| `[ERROR_MESSAGES]` | Specify the error messages | "Invalid email format: {email}", "User not found with ID: {user_id}", "Payment failed: {reason}", "Rate limit exceeded. Retry after {seconds}s" |
| `[LOGGING_LEVEL]` | Specify the logging level | "DEBUG for development", "INFO for request/response", "WARNING for recoverable errors", "ERROR for exceptions", "CRITICAL for system failures" |
| `[PERFORMANCE_CONSIDERATIONS]` | Specify the performance considerations | "Lazy loading for large datasets", "Connection pooling for database access", "Caching frequently accessed data", "Async I/O for external API calls", "Batch processing for bulk operations" |
| `[CLASS_NAME]` | Specify the class name | "UserService", "PaymentProcessor", "OrderRepository", "AuthenticationManager", "DataValidator" |
| `[CLASS_PURPOSE]` | Specify the class purpose | "Handles all user-related business logic", "Processes payment transactions with multiple providers", "Data access layer for order persistence", "Manages authentication and session handling" |
| `[INHERITANCE]` | Specify the inheritance | "BaseService", "ABC (Abstract Base Class)", "Generic[T]", "Protocol", "Mixin classes for shared functionality" |
| `[INTERFACES]` | Specify the interfaces | "IRepository[T]", "IPaymentGateway", "IAuthProvider", "IEventHandler", "ISerializer" |
| `[PROPERTIES]` | Specify the properties | "id: int, email: str, created_at: datetime", "status: OrderStatus, items: List[Item]", "is_active: bool, role: UserRole" |
| `[PROPERTY_TYPES]` | Specify the property types | "int, str, float, bool, datetime", "List[T], Dict[K, V], Optional[T]", "Enum, dataclass, TypedDict", "UUID, Decimal, Path" |
| `[CONSTRUCTOR_PARAMETERS]` | Specify the constructor parameters | "db_session: Session, config: Config", "repository: IRepository, logger: Logger", "api_key: str, timeout: int = 30" |
| `[METHODS]` | Specify the methods | "create(), update(), delete(), find_by_id()", "validate(), process(), rollback()", "serialize(), deserialize()", "authenticate(), authorize()" |
| `[STATIC_METHODS]` | Specify the static methods | "from_dict(data: dict)", "parse_config(path: str)", "generate_id()", "validate_format(value: str)" |
| `[PRIVATE_METHODS]` | Specify the private methods | "_validate_input()", "_calculate_hash()", "_send_notification()", "_refresh_cache()", "_sanitize_output()" |
| `[ABSTRACT_METHODS]` | Specify the abstract methods | "process(data: T) -> R", "validate(input: Input) -> bool", "serialize() -> dict", "handle_event(event: Event) -> None" |
| `[METHOD_VISIBILITY]` | Specify the method visibility | "public for API methods", "protected for subclass access", "private for internal implementation", "package-private for module-level access" |
| `[ALGORITHM_TYPE]` | Specify the algorithm type | "Binary search for sorted data", "Hash-based lookup", "Graph traversal (BFS/DFS)", "Dynamic programming", "Divide and conquer" |
| `[COMPLEXITY_REQUIREMENTS]` | Specify the complexity requirements | "Time: O(n log n) or better", "Space: O(n) maximum", "Worst case must be bounded", "Average case optimization preferred" |
| `[TIME_COMPLEXITY]` | Specify the time complexity | "O(1) constant", "O(log n) logarithmic", "O(n) linear", "O(n log n) linearithmic", "O(n²) quadratic (avoid if possible)" |
| `[SPACE_COMPLEXITY]` | Specify the space complexity | "O(1) in-place", "O(n) proportional to input", "O(log n) for recursive stack", "Trade space for time with memoization" |
| `[INPUT_SIZE]` | Specify the input size | "Up to 10K items for real-time processing", "1M+ records for batch jobs", "Streaming for unbounded data", "Paginated for large result sets" |
| `[DATA_STRUCTURES]` | Specify the data structures | "HashMap for O(1) lookup", "PriorityQueue for scheduling", "Trie for prefix matching", "B-tree for database indexes", "Graph for relationships" |
| `[OPTIMIZATION_STRATEGY]` | Specify the optimization strategy | "Memoization for repeated computations", "Early termination when possible", "Lazy evaluation for large datasets", "Parallel processing for CPU-bound tasks" |
| `[EDGE_CASES]` | Specify the edge cases | "Empty input, null values, boundary values", "Unicode characters, special symbols", "Max/min integer values, floating point precision", "Concurrent access, race conditions" |
| `[MATHEMATICAL_FORMULAS]` | Specify the mathematical formulas | "Compound interest: A = P(1 + r/n)^(nt)", "Haversine distance formula", "Percentile calculation", "Statistical mean/median/mode" |
| `[PSEUDOCODE]` | Specify the pseudocode | "FOR each item IN collection: process(item)", "IF condition THEN action ELSE fallback", "WHILE not_done: iterate()", "TRY operation CATCH handle_error" |
| `[NAMING_CONVENTIONS]` | Specify the naming conventions | "snake_case for functions/variables (Python)", "camelCase for JavaScript", "PascalCase for classes", "UPPER_SNAKE_CASE for constants" |
| `[CODE_FORMATTING]` | Specify the code formatting | "Black formatter for Python", "Prettier for JavaScript/TypeScript", "google-java-format", "gofmt for Go", "rustfmt for Rust" |
| `[COMMENT_STYLE]` | Specify the comment style | "Docstrings for public APIs", "Inline comments for complex logic", "TODO/FIXME with ticket numbers", "No obvious comments" |
| `[DOCUMENTATION_STRINGS]` | Specify the documentation strings | "Google-style docstrings with Args/Returns/Raises", "NumPy-style for scientific code", "JSDoc with @param and @returns", "Markdown in rustdoc" |
| `[TYPE_HINTS]` | Specify the type hints | "Full type annotations (Python 3.10+)", "TypeScript strict mode", "Generic types for reusable code", "Optional and Union for nullable values" |
| `[CODE_COVERAGE]` | Specify the code coverage | "Minimum 80% line coverage", "90% branch coverage for critical paths", "100% coverage for public APIs", "Exclude generated code from coverage" |
| `[STATIC_ANALYSIS]` | Specify the static analysis | "SonarQube for quality gates", "mypy for Python type checking", "ESLint with TypeScript parser", "Clippy for Rust lints" |
| `[LINTING_RULES]` | Specify the linting rules | "flake8 + pylint for Python", "ESLint Airbnb config", "Checkstyle for Java", "golangci-lint with multiple linters", "cargo clippy --all-targets" |
| `[CODE_METRICS]` | Specify the code metrics | "Cyclomatic complexity < 10", "Max function length 50 lines", "Max file length 500 lines", "Maintainability index > 70", "Cognitive complexity < 15" |
| `[TECHNICAL_DEBT]` | Specify the technical debt | "Track with TODO comments and Jira tickets", "SonarQube debt ratio < 5%", "Refactoring sprints quarterly", "Deprecation warnings before removal" |
| `[UNIT_TEST_REQUIREMENTS]` | Specify the unit test requirements | "One test class per source class", "Test happy path and error cases", "Isolated tests with mocks", "Fast execution (< 100ms per test)" |
| `[TEST_CASES]` | Specify the test cases | "test_valid_input_returns_expected_output", "test_invalid_email_raises_validation_error", "test_empty_list_returns_empty_result", "test_concurrent_access_is_thread_safe" |
| `[MOCK_OBJECTS]` | Specify the mock objects | "Mock database connections with unittest.mock", "Stub external API responses", "Fake implementations for interfaces", "Spy objects for verification" |
| `[TEST_DATA]` | Specify the test data | "Factory Boy for model fixtures", "Faker for realistic test data", "JSON fixtures for API responses", "Parameterized tests for multiple inputs" |
| `[ASSERTION_TYPES]` | Specify the assertion types | "assertEqual, assertTrue, assertRaises", "expect().toBe(), toEqual(), toThrow()", "Assert.assertEquals, assertThrows", "assert!, assert_eq!, should_panic" |
| `[EDGE_CASE_TESTS]` | Specify the edge case tests | "test_empty_input", "test_null_parameter", "test_max_integer_value", "test_unicode_characters", "test_concurrent_modification" |
| `[PERFORMANCE_TESTS]` | Specify the performance tests | "pytest-benchmark for function timing", "Load testing with k6 or Locust", "Memory profiling with memory_profiler", "Benchmark comparisons with baseline" |
| `[INTEGRATION_TESTS]` | Specify the integration tests | "Testcontainers for database integration", "WireMock for external service simulation", "End-to-end API testing with Postman/Newman", "Contract testing with Pact" |
| `[REGRESSION_TESTS]` | Specify the regression tests | "Automated test suite in CI pipeline", "Snapshot testing for UI components", "Golden file tests for output validation", "Mutation testing for test quality" |
| `[COVERAGE_TARGETS]` | Specify the coverage targets | "80% overall, 90% for business logic", "100% for security-critical code", "Branch coverage > 75%", "Path coverage for complex algorithms" |
| `[API_DOCUMENTATION]` | Specify the api documentation | "OpenAPI 3.0 spec with Swagger UI", "Postman collection with examples", "README with quick start guide", "Auto-generated from docstrings (pdoc, typedoc)" |
| `[CODE_COMMENTS]` | Specify the code comments | "Explain why, not what", "Document non-obvious business rules", "Reference ticket numbers for workarounds", "Mark technical debt with TODO tags" |
| `[USAGE_EXAMPLES]` | Specify the usage examples | "Quick start code snippet in README", "Jupyter notebook tutorials", "CLI help with --help flag", "Interactive REPL examples" |
| `[INSTALLATION_GUIDE]` | Specify the installation guide | "pip install package_name", "npm install --save dependency", "Docker Compose for local development", "Homebrew for CLI tools" |
| `[CONFIGURATION_GUIDE]` | Specify the configuration guide | "Environment variables with .env.example", "YAML/JSON config file templates", "CLI flags with defaults", "Config validation on startup" |
| `[TROUBLESHOOTING_GUIDE]` | Specify the troubleshooting guide | "Common error messages and solutions", "Debug logging instructions", "Health check endpoints", "FAQ section for known issues" |
| `[CHANGE_LOG]` | Specify the change log | "Keep a Changelog format", "Semantic versioning (MAJOR.MINOR.PATCH)", "Breaking changes highlighted", "Migration guides for major versions" |
| `[LICENSE_INFORMATION]` | Specify the license information | "MIT License for open source", "Apache 2.0 with patent grant", "Proprietary with EULA", "GPL v3 for copyleft" |
| `[CONTRIBUTING_GUIDELINES]` | Specify the contributing guidelines | "CONTRIBUTING.md with PR process", "Code of conduct", "Issue templates", "Development setup instructions" |
| `[CODE_EXAMPLES]` | Specify the code examples | "Runnable examples in /examples directory", "Copy-paste ready snippets", "Progressive complexity (basic to advanced)", "Real-world use case demonstrations" |
| `[DATABASE_TYPE]` | Specify the database type | "PostgreSQL 15 for relational data", "MongoDB 7 for documents", "Redis 7 for caching", "Elasticsearch 8 for search", "SQLite for embedded" |
| `[CONNECTION_STRING]` | Specify the connection string | "postgresql://user:pass@localhost:5432/dbname", "mongodb://localhost:27017/database", "redis://localhost:6379/0", "mysql://root@localhost/app" |
| `[QUERY_LANGUAGE]` | Specify the query language | "SQL with parameterized queries", "MongoDB query operators", "GraphQL queries/mutations", "Elasticsearch Query DSL", "Cypher for Neo4j" |
| `[ORM_FRAMEWORK]` | Specify the orm framework | "SQLAlchemy 2.0 with async support", "Prisma for TypeScript", "Hibernate/JPA for Java", "GORM for Go", "Diesel for Rust" |
| `[DATABASE_SCHEMA]` | Specify the database schema | "Normalized 3NF for OLTP", "Star schema for analytics", "Document schema with embedded objects", "Versioned migrations with Alembic/Flyway" |
| `[TABLE_NAMES]` | Specify the table names | "users, orders, products, payments", "audit_logs, sessions, permissions", "customers, invoices, line_items" |
| `[COLUMN_NAMES]` | Specify the column names | "id, created_at, updated_at", "email, password_hash, is_active", "status, amount, currency", "user_id (foreign key)" |
| `[RELATIONSHIPS]` | Specify the relationships | "One-to-many: User has many Orders", "Many-to-many: Users and Roles through user_roles", "One-to-one: User has one Profile", "Self-referential: Employee has manager" |
| `[INDEXES]` | Specify the indexes | "Primary key on id", "Unique index on email", "Composite index on (user_id, created_at)", "Full-text index for search", "Partial index for active records" |
| `[TRANSACTIONS]` | Specify the transactions | "ACID transactions for financial operations", "Optimistic locking with version column", "Savepoints for partial rollback", "Read committed isolation level" |
| `[API_TYPE]` | Specify the api type | "REST with JSON", "GraphQL", "gRPC with Protocol Buffers", "WebSocket for real-time", "Server-Sent Events" |
| `[API_VERSION]` | Specify the api version | "v1, v2 (URL path versioning)", "Accept-Version header", "api-version query parameter", "Semantic versioning for breaking changes" |
| `[AUTHENTICATION_METHOD]` | Specify the authentication method | "JWT Bearer tokens", "OAuth 2.0 with refresh tokens", "API key in header", "Basic auth over HTTPS", "mTLS for service-to-service" |
| `[API_KEY]` | Specify the api key | "X-API-Key header", "Authorization: ApiKey {key}", "Query parameter ?api_key=", "Environment variable for server-side" |
| `[ENDPOINTS]` | Specify the endpoints | "GET /users, POST /users, GET /users/{id}", "PUT /orders/{id}/status", "DELETE /sessions/{token}", "POST /auth/login, POST /auth/refresh" |
| `[HTTP_METHODS]` | Specify the http methods | "GET for read operations", "POST for create", "PUT/PATCH for update", "DELETE for removal", "OPTIONS for CORS preflight" |
| `[REQUEST_HEADERS]` | Specify the request headers | "Authorization: Bearer {token}", "Content-Type: application/json", "Accept: application/json", "X-Request-ID for tracing", "Accept-Language for i18n" |
| `[REQUEST_BODY]` | Specify the request body | "JSON object with required fields", "Multipart form for file uploads", "URL-encoded for simple forms", "Binary for file content" |
| `[RESPONSE_FORMAT]` | Specify the response format | "JSON with consistent envelope", "Pagination with links", "Error response with code and message", "HATEOAS links for discoverability" |
| `[API_ERROR_HANDLING]` | Specify the api error handling | "RFC 7807 Problem Details", "HTTP status codes (4xx client, 5xx server)", "Error code enum for programmatic handling", "Retry-After header for rate limits" |
| `[UI_FRAMEWORK]` | Specify the ui framework | "React 18 with Next.js", "Vue 3 with Composition API", "Angular 17", "Svelte/SvelteKit", "Solid.js" |
| `[COMPONENT_TYPE]` | Specify the component type | "Functional component with hooks", "Class component (legacy)", "Server component (Next.js)", "Presentational vs Container", "Higher-order component (HOC)" |
| `[COMPONENT_PROPERTIES]` | Specify the component properties | "children: ReactNode, onClick: () => void", "disabled: boolean, variant: 'primary' | 'secondary'", "data: T[], renderItem: (item: T) => JSX.Element" |
| `[EVENT_HANDLERS]` | Specify the event handlers | "onClick, onChange, onSubmit", "onMouseEnter, onMouseLeave", "onKeyDown, onKeyUp", "onFocus, onBlur", "custom events with emit" |
| `[STATE_MANAGEMENT]` | Specify the state management | "useState/useReducer for local state", "Redux Toolkit for global state", "Zustand for lightweight state", "React Query for server state", "Context API for prop drilling" |
| `[STYLING_APPROACH]` | Specify the styling approach | "Tailwind CSS utility classes", "CSS Modules for scoped styles", "styled-components CSS-in-JS", "Sass/SCSS with BEM methodology", "CSS custom properties (variables)" |
| `[RESPONSIVE_DESIGN]` | Specify the responsive design | "Mobile-first with breakpoints", "CSS Grid and Flexbox", "Container queries for components", "Fluid typography with clamp()", "Responsive images with srcset" |
| `[ACCESSIBILITY_FEATURES]` | Specify the accessibility features | "ARIA labels and roles", "Keyboard navigation (Tab, Enter, Escape)", "Focus management and skip links", "Screen reader announcements", "Reduced motion support" |
| `[BROWSER_SUPPORT]` | Specify the browser support | "Last 2 versions of major browsers", "Chrome 90+, Firefox 88+, Safari 14+", "IE11 not supported", "Polyfills via core-js", "Browserslist configuration" |
| `[MOBILE_SUPPORT]` | Specify the mobile support | "Touch events and gestures", "Viewport meta tag", "Safe area insets for notch", "PWA with service worker", "Responsive touch targets (44x44px)" |
| `[CONFIGURATION_FILES]` | Specify the configuration files | "config.yaml, settings.json", ".env files for environment-specific", "tsconfig.json, package.json", "docker-compose.yml", "Dockerfile" |
| `[ENVIRONMENT_VARIABLES]` | Specify the environment variables | "DATABASE_URL, API_KEY, SECRET_KEY", "NODE_ENV, DEBUG, LOG_LEVEL", "AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY", "REDIS_URL, ELASTICSEARCH_URL" |
| `[DEFAULT_VALUES]` | Specify the default values | "PORT=3000, TIMEOUT=30000", "LOG_LEVEL=INFO, DEBUG=false", "MAX_CONNECTIONS=100, POOL_SIZE=10", "CACHE_TTL=3600, RETRY_COUNT=3" |
| `[CONFIGURATION_VALIDATION]` | Specify the configuration validation | "Pydantic Settings for Python", "Joi/Yup schema validation", "JSON Schema validation", "Type-safe config with TypeScript", "Fail fast on startup if invalid" |
| `[RUNTIME_CONFIGURATION]` | Specify the runtime configuration | "Feature flags from remote config", "Hot reload for development", "Environment-based config selection", "Consul/etcd for distributed config", "AWS Parameter Store/Secrets Manager" |
| `[FEATURE_FLAGS]` | Specify the feature flags | "LaunchDarkly for feature management", "Split.io for A/B testing", "Environment variable toggles", "Database-backed feature flags", "Percentage rollout support" |
| `[LOGGING_CONFIGURATION]` | Specify the logging configuration | "Structured JSON logging", "Log levels: DEBUG, INFO, WARNING, ERROR", "Correlation ID in all logs", "Log rotation and retention", "ELK Stack or CloudWatch integration" |
| `[SECURITY_CONFIGURATION]` | Specify the security configuration | "CORS allowed origins", "Rate limiting thresholds", "JWT secret and expiration", "HTTPS enforcement", "Content Security Policy headers" |
| `[PERFORMANCE_CONFIGURATION]` | Specify the performance configuration | "Connection pool sizes", "Cache TTL settings", "Timeout values for external calls", "Batch sizes for bulk operations", "Worker thread counts" |
| `[DEBUG_SETTINGS]` | Specify the debug settings | "DEBUG=true for verbose logging", "Source maps enabled", "Hot module replacement", "Profiler enabled", "Debug endpoints exposed (dev only)" |
| `[AUTHENTICATION]` | Specify the authentication | "JWT with RS256 signing", "OAuth 2.0 authorization code flow", "Session-based with secure cookies", "API key authentication", "SAML for enterprise SSO" |
| `[AUTHORIZATION]` | Specify the authorization | "Role-based access control (RBAC)", "Attribute-based access control (ABAC)", "Permission-based with scopes", "Resource-level ACLs", "Policy engine (OPA, Casbin)" |
| `[INPUT_VALIDATION]` | Specify the input validation | "Whitelist validation for allowed characters", "Length and format constraints", "Type coercion with strict checking", "Sanitize HTML with DOMPurify", "Validate against JSON Schema" |
| `[OUTPUT_ENCODING]` | Specify the output encoding | "HTML entity encoding for display", "JSON encoding for API responses", "URL encoding for query parameters", "Base64 for binary data", "UTF-8 throughout" |
| `[SQL_INJECTION_PREVENTION]` | Specify the sql injection prevention | "Parameterized queries exclusively", "ORM with query builder", "Stored procedures with parameters", "Input validation before queries", "Principle of least privilege for DB users" |
| `[XSS_PREVENTION]` | Specify the xss prevention | "Content Security Policy headers", "Output encoding by context", "HttpOnly and Secure cookie flags", "Sanitize user-generated HTML", "React auto-escapes by default" |
| `[CSRF_PROTECTION]` | Specify the csrf protection | "CSRF tokens in forms", "SameSite cookie attribute", "Double submit cookie pattern", "Custom request headers for APIs", "Referer validation" |
| `[ENCRYPTION_METHODS]` | Specify the encryption methods | "AES-256-GCM for symmetric encryption", "RSA-2048 for asymmetric", "bcrypt/Argon2 for password hashing", "PBKDF2 for key derivation", "TLS 1.3 for transport" |
| `[SECURE_COMMUNICATIONS]` | Specify the secure communications | "HTTPS only (HSTS enabled)", "Certificate pinning for mobile", "mTLS for service-to-service", "Encrypted message queues", "VPN for sensitive networks" |
| `[AUDIT_LOGGING]` | Specify the audit logging | "Log all authentication events", "Record data access and modifications", "Include user ID, timestamp, action, resource", "Tamper-proof log storage", "SIEM integration for analysis" |
| `[CACHING_STRATEGY]` | Specify the caching strategy | "Redis for distributed caching", "In-memory cache with TTL", "Cache-aside pattern", "Write-through for consistency", "CDN for static assets" |
| `[MEMORY_MANAGEMENT]` | Specify the memory management | "Object pooling for frequent allocations", "Streaming for large files", "Garbage collection tuning", "Memory limits with OOM handling", "Weak references for caches" |
| `[CPU_OPTIMIZATION]` | Specify the cpu optimization | "Avoid unnecessary computations", "Use efficient algorithms (O(n log n) vs O(n²))", "Compile-time optimizations", "SIMD for data parallelism", "Profile and optimize hot paths" |
| `[IO_OPTIMIZATION]` | Specify the io optimization | "Async I/O with event loop", "Buffered reads/writes", "Connection pooling", "Batch database operations", "Compress large payloads" |
| `[DATABASE_OPTIMIZATION]` | Specify the database optimization | "Proper indexing strategy", "Query plan analysis (EXPLAIN)", "Connection pooling (PgBouncer)", "Read replicas for scaling", "Denormalization for read performance" |
| `[NETWORK_OPTIMIZATION]` | Specify the network optimization | "HTTP/2 multiplexing", "Gzip/Brotli compression", "Connection keep-alive", "DNS prefetching", "CDN for static content" |
| `[LAZY_LOADING]` | Specify the lazy loading | "Lazy load images below fold", "Dynamic imports for code splitting", "Virtual scrolling for long lists", "Pagination for large datasets", "On-demand data fetching" |
| `[PARALLEL_PROCESSING]` | Specify the parallel processing | "Thread pool for CPU-bound tasks", "Process pool for isolation", "Map-reduce for distributed processing", "Parallel streams in Java", "Rayon for Rust parallelism" |
| `[ASYNCHRONOUS_PROCESSING]` | Specify the asynchronous processing | "async/await for I/O operations", "Message queues for background jobs", "Event-driven architecture", "Promises/Futures for non-blocking", "Worker threads for CPU tasks" |
| `[RESOURCE_POOLING]` | Specify the resource pooling | "Database connection pools", "HTTP client pools", "Thread pools with configurable size", "Object pools for expensive objects", "Graceful pool exhaustion handling" |
| `[DEPLOYMENT_ENVIRONMENT]` | Specify the deployment environment | "AWS EKS Kubernetes cluster", "Heroku for simple deployments", "Vercel for frontend", "AWS Lambda for serverless", "On-premises Docker Swarm" |
| `[BUILD_PROCESS]` | Specify the build process | "npm run build with Webpack/Vite", "Maven package for Java", "go build with CGO disabled", "Docker multi-stage builds", "CI/CD automated builds" |
| `[PACKAGE_MANAGEMENT]` | Specify the package management | "npm/yarn/pnpm for JavaScript", "pip/poetry for Python", "Maven/Gradle for Java", "go mod for Go", "Cargo for Rust" |
| `[DEPENDENCY_MANAGEMENT]` | Specify the dependency management | "Lock files for reproducible builds", "Semantic versioning constraints", "Dependabot for updates", "Security scanning with Snyk", "Private registry for internal packages" |
| `[VERSION_CONTROL]` | Specify the version control | "Git with GitHub/GitLab", "Trunk-based development", "Feature branches with PRs", "Conventional commits", "Git tags for releases" |
| `[CICD_PIPELINE]` | Specify the cicd pipeline | "GitHub Actions workflow", "GitLab CI/CD", "Jenkins declarative pipeline", "CircleCI orbs", "ArgoCD for GitOps" |
| `[CONTAINER_CONFIGURATION]` | Specify the container configuration | "Dockerfile with multi-stage build", "docker-compose for local dev", "Kubernetes manifests/Helm charts", "Resource limits and health checks", "Non-root user for security" |
| `[LOAD_BALANCING]` | Specify the load balancing | "AWS ALB for HTTP traffic", "NGINX as reverse proxy", "HAProxy for TCP/HTTP", "Kubernetes Ingress", "CloudFlare for CDN and DDoS" |
| `[MONITORING_SETUP]` | Specify the monitoring setup | "Prometheus + Grafana stack", "Datadog APM", "New Relic", "AWS CloudWatch", "ELK Stack for logs" |
| `[BACKUP_STRATEGY]` | Specify the backup strategy | "Daily automated database backups", "Point-in-time recovery enabled", "Cross-region replication", "30-day retention policy", "Regular restore testing" |
| `[CODE_MAINTAINABILITY]` | Specify the code maintainability | "Single responsibility principle", "Small, focused functions (<50 lines)", "Meaningful names", "DRY - Don't Repeat Yourself", "YAGNI - You Aren't Gonna Need It" |
| `[REFACTORING_GUIDELINES]` | Specify the refactoring guidelines | "Red-green-refactor cycle", "Extract method for duplication", "Rename for clarity", "Move to appropriate module", "Test coverage before refactoring" |
| `[BUG_TRACKING]` | Specify the bug tracking | "Jira for enterprise", "GitHub Issues for open source", "Linear for startups", "Sentry for error tracking", "Bug templates with reproduction steps" |
| `[ISSUE_RESOLUTION]` | Specify the issue resolution | "Triage by severity and priority", "Root cause analysis for critical bugs", "Post-mortems for incidents", "Hotfix process for production issues", "SLA-based response times" |
| `[CODE_REVIEWS]` | Specify the code reviews | "Pull request required for main branch", "At least one approval needed", "Automated checks must pass", "Review checklist for consistency", "Constructive feedback culture" |
| `[KNOWLEDGE_TRANSFER]` | Specify the knowledge transfer | "Pair programming sessions", "Technical documentation in wiki", "Architecture Decision Records (ADRs)", "Onboarding documentation", "Regular tech talks/demos" |
| `[SUPPORT_DOCUMENTATION]` | Specify the support documentation | "Runbooks for common issues", "FAQ for support team", "Escalation procedures", "SLA definitions", "Contact information" |
| `[TRAINING_MATERIALS]` | Specify the training materials | "Video tutorials for setup", "Interactive coding exercises", "Best practices guide", "Code examples repository", "Office hours for Q&A" |
| `[USER_FEEDBACK]` | Specify the user feedback | "In-app feedback widget", "User surveys quarterly", "Feature request voting", "Beta testing program", "Customer interviews" |
| `[CONTINUOUS_IMPROVEMENT]` | Specify the continuous improvement | "Sprint retrospectives", "Tech debt backlog", "Performance monitoring dashboards", "A/B testing for features", "Regular dependency updates" |

### Complex Class Generation
```
Generate Java code for user authentication using Spring Boot framework. The code should implement JWT token authentication with O(1) time complexity and include:

Class Structure:
- UserAuthService class inheriting from BaseAuthService
- Properties: tokenManager (JwtTokenManager), userRepository (UserRepository)
- Methods: authenticate, validateToken, refreshToken with public visibility
- Constructor accepting TokenManager and UserRepository dependencies

Security Implementation:
- Add input validation for username/password
- Implement JWT token authentication and role-based authorization
- Prevent SQL injection and XSS attacks
- Use BCrypt encryption for password hashing

### Integration Requirements
- Connect to MySQL database using JPA/Hibernate
- Integrate with REST API using Bearer token authentication
- Handle Authorization headers and JSON response format
- Implement Redis caching for performance
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Code Generation Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Software Development](../../technology/Software Development/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating generate high-quality code including functions, classes, algorithms, and complete applications with comprehensive documentation and best practices.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Always specify the exact programming language and framework**
2. **Include comprehensive error handling and validation**
3. **Specify performance and security requirements**
4. **Request both implementation and test code**
5. **Ask for documentation and usage examples**
6. **Define clear input/output specifications**
7. **Include deployment and configuration considerations**
8. **Specify coding standards and style guidelines**
9. **Request scalability and maintainability features**
10. **Include integration requirements and dependencies**