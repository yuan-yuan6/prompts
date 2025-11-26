---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- automation
- design
- documentation
- optimization
- security
- strategy
title: Testing & QA Template
use_cases:
- Creating design comprehensive testing strategies including unit tests, integration
  tests, end-to-end tests, performance testing, security testing, and automated quality
  assurance processes.
- Project planning and execution
- Strategy development
industries:
- finance
- government
- manufacturing
- retail
- technology
type: template
difficulty: intermediate
slug: testing-qa
---

# Testing & QA Template

## Purpose
Design comprehensive testing strategies including unit tests, integration tests, end-to-end tests, performance testing, security testing, and automated quality assurance processes.

## Quick Testing Prompt
Create testing strategy for [application] with [X users]. Unit tests: [Jest/pytest/JUnit], [Y%] coverage. Integration: [API tests with Postman/supertest]. E2E: [Cypress/Playwright] for [critical flows]. Performance: [K6/JMeter], handle [Z concurrent users]. Security: OWASP Top 10 scan. CI/CD: run all tests on [commit/PR]. Quality gates: coverage [X%], 0 critical bugs.

## Quick Start

**Need to create a testing strategy quickly?** Use this minimal example:

### Minimal Example
```
Create testing strategy for a web application with 50K users. Include: unit tests (80% coverage with Jest), integration tests for APIs (Postman), end-to-end tests for critical flows (Cypress), performance testing (handle 1000 concurrent users), security testing (OWASP Top 10). CI/CD pipeline runs all tests on every commit.
```

### When to Use This
- Establishing testing strategy for new projects
- Improving quality assurance processes
- Automating testing in CI/CD pipelines
- Planning test coverage and quality gates

### Basic 3-Step Workflow
1. **Define test scope** - What needs testing, quality standards, risk areas
2. **Choose test types** - Unit, integration, E2E, performance, security mix
3. **Implement automation** - Tools, frameworks, CI/CD integration, reporting

**Time to complete**: 2-3 days for strategy, 1-2 weeks for full implementation

---

## Template Structure

### Testing Strategy Overview
- **Application Type**: [APPLICATION_TYPE]
- **Testing Approach**: [TESTING_APPROACH]
- **Testing Philosophy**: [TESTING_PHILOSOPHY]
- **Quality Standards**: [QUALITY_STANDARDS]
- **Testing Budget**: [TESTING_BUDGET]
- **Timeline**: [TESTING_TIMELINE]
- **Team Structure**: [TEAM_STRUCTURE]
- **Risk Assessment**: [RISK_ASSESSMENT]
- **Success Criteria**: [SUCCESS_CRITERIA]
- **Reporting Requirements**: [REPORTING_REQUIREMENTS]

### Test Planning
- **Test Scope**: [TEST_SCOPE]
- **Test Objectives**: [TEST_OBJECTIVES]
- **Testing Types**: [TESTING_TYPES]
- **Test Environment**: [TEST_ENVIRONMENT]
- **Test Data Requirements**: [TEST_DATA_REQUIREMENTS]
- **Entry Criteria**: [ENTRY_CRITERIA]
- **Exit Criteria**: [EXIT_CRITERIA]
- **Suspension Criteria**: [SUSPENSION_CRITERIA]
- **Resumption Criteria**: [RESUMPTION_CRITERIA]
- **Test Deliverables**: [TEST_DELIVERABLES]

### Unit Testing
- **Testing Framework**: [UNIT_TESTING_FRAMEWORK]
- **Test Coverage Target**: [UNIT_COVERAGE_TARGET]
- **Mocking Strategy**: [MOCKING_STRATEGY]
- **Test Data Setup**: [UNIT_TEST_DATA]
- **Assertion Library**: [ASSERTION_LIBRARY]
- **Test Organization**: [TEST_ORGANIZATION]
- **Naming Conventions**: [TEST_NAMING_CONVENTIONS]
- **Test Documentation**: [UNIT_TEST_DOCUMENTATION]
- **Continuous Integration**: [UNIT_CI_INTEGRATION]
- **Code Coverage Tools**: [COVERAGE_TOOLS]

### Integration Testing
- **Integration Strategy**: [INTEGRATION_STRATEGY]
- **Integration Points**: [INTEGRATION_POINTS]
- **API Testing**: [API_TESTING]
- **Database Testing**: [DATABASE_TESTING]
- **External Service Testing**: [EXTERNAL_SERVICE_TESTING]
- **Message Queue Testing**: [MESSAGE_QUEUE_TESTING]
- **File System Testing**: [FILE_SYSTEM_TESTING]
- **Network Testing**: [NETWORK_TESTING]
- **Configuration Testing**: [CONFIGURATION_TESTING]
- **Environment Setup**: [INTEGRATION_ENVIRONMENT]

### End-to-End Testing
- **E2E Framework**: [E2E_FRAMEWORK]
- **Browser Support**: [BROWSER_SUPPORT]
- **Device Testing**: [DEVICE_TESTING]
- **User Journey Testing**: [USER_JOURNEY_TESTING]
- **Cross-Platform Testing**: [CROSS_PLATFORM_TESTING]
- **Accessibility Testing**: [ACCESSIBILITY_TESTING]
- **Visual Regression Testing**: [VISUAL_REGRESSION_TESTING]
- **Mobile Testing**: [MOBILE_TESTING]
- **Performance Monitoring**: [E2E_PERFORMANCE_MONITORING]
- **Test Data Management**: [E2E_TEST_DATA]

### Performance Testing
- **Performance Requirements**: [PERFORMANCE_REQUIREMENTS]
- **Load Testing**: [LOAD_TESTING]
- **Stress Testing**: [STRESS_TESTING]
- **Volume Testing**: [VOLUME_TESTING]
- **Spike Testing**: [SPIKE_TESTING]
- **Endurance Testing**: [ENDURANCE_TESTING]
- **Scalability Testing**: [SCALABILITY_TESTING]
- **Capacity Testing**: [CAPACITY_TESTING]
- **Resource Utilization**: [RESOURCE_UTILIZATION]
- **Response Time Targets**: [RESPONSE_TIME_TARGETS]

### Security Testing
- **Security Framework**: [SECURITY_FRAMEWORK]
- **Vulnerability Assessment**: [VULNERABILITY_ASSESSMENT]
- **Penetration Testing**: [PENETRATION_TESTING]
- **Authentication Testing**: [AUTHENTICATION_TESTING]
- **Authorization Testing**: [AUTHORIZATION_TESTING]
- **Session Management**: [SESSION_MANAGEMENT_TESTING]
- **Input Validation**: [INPUT_VALIDATION_TESTING]
- **SQL Injection Testing**: [SQL_INJECTION_TESTING]
- **XSS Testing**: [XSS_TESTING]
- **CSRF Testing**: [CSRF_TESTING]

### Automated Testing
- **Automation Strategy**: [AUTOMATION_STRATEGY]
- **Tool Selection**: [AUTOMATION_TOOLS]
- **Test Automation Framework**: [AUTOMATION_FRAMEWORK]
- **CI/CD Integration**: [CICD_INTEGRATION]
- **Automated Test Suite**: [AUTOMATED_TEST_SUITE]
- **Test Execution**: [TEST_EXECUTION]
- **Result Analysis**: [RESULT_ANALYSIS]
- **Maintenance Strategy**: [MAINTENANCE_STRATEGY]
- **ROI Metrics**: [AUTOMATION_ROI]
- **Skill Requirements**: [AUTOMATION_SKILLS]

### API Testing
- **API Testing Tools**: [API_TESTING_TOOLS]
- **Request Testing**: [REQUEST_TESTING]
- **Response Validation**: [RESPONSE_VALIDATION]
- **Status Code Testing**: [STATUS_CODE_TESTING]
- **Header Testing**: [HEADER_TESTING]
- **Payload Testing**: [PAYLOAD_TESTING]
- **Authentication Testing**: [API_AUTHENTICATION_TESTING]
- **Rate Limiting Testing**: [RATE_LIMITING_TESTING]
- **Error Handling Testing**: [ERROR_HANDLING_TESTING]
- **Contract Testing**: [CONTRACT_TESTING]

### Database Testing
- **Database Testing Strategy**: [DATABASE_TESTING_STRATEGY]
- **Data Integrity Testing**: [DATA_INTEGRITY_TESTING]
- **Transaction Testing**: [TRANSACTION_TESTING]
- **Concurrency Testing**: [CONCURRENCY_TESTING]
- **Backup/Recovery Testing**: [BACKUP_RECOVERY_TESTING]
- **Migration Testing**: [MIGRATION_TESTING]
- **Performance Testing**: [DB_PERFORMANCE_TESTING]
- **Security Testing**: [DB_SECURITY_TESTING]
- **Referential Integrity**: [REFERENTIAL_INTEGRITY]
- **Constraint Testing**: [CONSTRAINT_TESTING]

### Mobile Testing
- **Mobile Testing Strategy**: [MOBILE_TESTING_STRATEGY]
- **Device Coverage**: [DEVICE_COVERAGE]
- **Operating System Testing**: [OS_TESTING]
- **App Store Testing**: [APP_STORE_TESTING]
- **Offline Testing**: [OFFLINE_TESTING]
- **Battery Testing**: [BATTERY_TESTING]
- **Memory Testing**: [MEMORY_TESTING]
- **Network Testing**: [MOBILE_NETWORK_TESTING]
- **Usability Testing**: [MOBILE_USABILITY_TESTING]
- **Push Notification Testing**: [PUSH_NOTIFICATION_TESTING]

### Accessibility Testing
- **Accessibility Standards**: [ACCESSIBILITY_STANDARDS]
- **Screen Reader Testing**: [SCREEN_READER_TESTING]
- **Keyboard Navigation**: [KEYBOARD_NAVIGATION_TESTING]
- **Color Contrast Testing**: [COLOR_CONTRAST_TESTING]
- **Alt Text Testing**: [ALT_TEXT_TESTING]
- **Focus Management**: [FOCUS_MANAGEMENT_TESTING]
- **ARIA Testing**: [ARIA_TESTING]
- **Responsive Design**: [RESPONSIVE_DESIGN_TESTING]
- **Video/Audio Testing**: [MEDIA_TESTING]
- **Form Testing**: [FORM_ACCESSIBILITY_TESTING]

### Test Data Management
- **Test Data Strategy**: [TEST_DATA_STRATEGY]
- **Data Generation**: [DATA_GENERATION]
- **Data Masking**: [DATA_MASKING]
- **Data Privacy**: [DATA_PRIVACY]
- **Synthetic Data**: [SYNTHETIC_DATA]
- **Data Refresh**: [DATA_REFRESH]
- **Data Versioning**: [DATA_VERSIONING]
- **Data Cleanup**: [DATA_CLEANUP]
- **Data Backup**: [DATA_BACKUP]
- **Data Compliance**: [DATA_COMPLIANCE]

### Test Environment Management
- **Environment Strategy**: [ENVIRONMENT_STRATEGY]
- **Environment Types**: [ENVIRONMENT_TYPES]
- **Environment Setup**: [ENVIRONMENT_SETUP]
- **Configuration Management**: [CONFIG_MANAGEMENT]
- **Deployment Pipeline**: [DEPLOYMENT_PIPELINE]
- **Environment Monitoring**: [ENVIRONMENT_MONITORING]
- **Resource Management**: [RESOURCE_MANAGEMENT]
- **Access Control**: [ACCESS_CONTROL]
- **Environment Refresh**: [ENVIRONMENT_REFRESH]
- **Troubleshooting**: [ENVIRONMENT_TROUBLESHOOTING]

### Defect Management
- **Defect Lifecycle**: [DEFECT_LIFECYCLE]
- **Bug Tracking Tool**: [BUG_TRACKING_TOOL]
- **Severity Classification**: [SEVERITY_CLASSIFICATION]
- **Priority Classification**: [PRIORITY_CLASSIFICATION]
- **Escalation Process**: [ESCALATION_PROCESS]
- **Root Cause Analysis**: [ROOT_CAUSE_ANALYSIS]
- **Regression Testing**: [REGRESSION_TESTING]
- **Defect Metrics**: [DEFECT_METRICS]
- **Quality Gates**: [QUALITY_GATES]
- **Release Criteria**: [RELEASE_CRITERIA]

### Test Reporting
- **Reporting Framework**: [REPORTING_FRAMEWORK]
- **Test Metrics**: [TEST_METRICS]
- **Coverage Reports**: [COVERAGE_REPORTS]
- **Performance Reports**: [PERFORMANCE_REPORTS]
- **Defect Reports**: [DEFECT_REPORTS]
- **Dashboard Design**: [DASHBOARD_DESIGN]
- **Stakeholder Reports**: [STAKEHOLDER_REPORTS]
- **Executive Summary**: [EXECUTIVE_SUMMARY]
- **Trend Analysis**: [TREND_ANALYSIS]
- **Risk Assessment**: [RISK_ASSESSMENT_REPORTING]

### Quality Assurance Process
- **QA Methodology**: [QA_METHODOLOGY]
- **Review Process**: [REVIEW_PROCESS]
- **Code Review**: [CODE_REVIEW_PROCESS]
- **Test Review**: [TEST_REVIEW_PROCESS]
- **Documentation Review**: [DOCUMENTATION_REVIEW]
- **Process Improvement**: [PROCESS_IMPROVEMENT]
- **Best Practices**: [BEST_PRACTICES]
- **Training Requirements**: [TRAINING_REQUIREMENTS]
- **Certification Requirements**: [CERTIFICATION_REQUIREMENTS]
- **Knowledge Management**: [KNOWLEDGE_MANAGEMENT]

### Risk-Based Testing
- **Risk Identification**: [RISK_IDENTIFICATION]
- **Risk Assessment**: [RISK_ASSESSMENT_PROCESS]
- **Risk Mitigation**: [RISK_MITIGATION]
- **Test Prioritization**: [TEST_PRIORITIZATION]
- **Critical Path Testing**: [CRITICAL_PATH_TESTING]
- **Business Impact**: [BUSINESS_IMPACT]
- **Technical Risk**: [TECHNICAL_RISK]
- **Schedule Risk**: [SCHEDULE_RISK]
- **Resource Risk**: [RESOURCE_RISK]
- **Quality Risk**: [QUALITY_RISK]

### Continuous Testing
- **CI/CD Integration**: [CONTINUOUS_INTEGRATION]
- **Pipeline Testing**: [PIPELINE_TESTING]
- **Shift-Left Testing**: [SHIFT_LEFT_TESTING]
- **Test Automation**: [CONTINUOUS_AUTOMATION]
- **Feedback Loops**: [FEEDBACK_LOOPS]
- **Quality Gates**: [CONTINUOUS_QUALITY_GATES]
- **Monitoring Integration**: [MONITORING_INTEGRATION]
- **DevOps Collaboration**: [DEVOPS_COLLABORATION]
- **Tool Integration**: [TOOL_INTEGRATION]
- **Metrics Collection**: [CONTINUOUS_METRICS]

## Prompt Template

Design a comprehensive testing strategy for [APPLICATION_TYPE] using [TESTING_APPROACH] methodology. The testing should achieve [UNIT_COVERAGE_TARGET]% code coverage and meet [QUALITY_STANDARDS] quality requirements.

**Testing Framework Setup:**
- Implement [UNIT_TESTING_FRAMEWORK] for unit testing with [MOCKING_STRATEGY]
- Use [E2E_FRAMEWORK] for end-to-end testing across [BROWSER_SUPPORT]
- Set up [API_TESTING_TOOLS] for API testing with [CONTRACT_TESTING]
- Configure [AUTOMATION_FRAMEWORK] for test automation
- Integrate with [CICD_INTEGRATION] pipeline

**Test Coverage Requirements:**
- Unit tests covering [TEST_SCOPE] with [ASSERTION_LIBRARY]
- Integration tests for [INTEGRATION_POINTS] including [API_TESTING]
- End-to-end tests covering [USER_JOURNEY_TESTING] scenarios
- Performance tests meeting [PERFORMANCE_REQUIREMENTS]
- Security tests including [VULNERABILITY_ASSESSMENT]

**Quality Assurance Process:**
- Implement [QA_METHODOLOGY] with [REVIEW_PROCESS]
- Use [BUG_TRACKING_TOOL] for defect management
- Apply [SEVERITY_CLASSIFICATION] and [PRIORITY_CLASSIFICATION]
- Set up [QUALITY_GATES] and [RELEASE_CRITERIA]
- Create [REPORTING_FRAMEWORK] with [TEST_METRICS]

**Test Environment Setup:**
- Configure [ENVIRONMENT_TYPES] environments
- Implement [TEST_DATA_STRATEGY] with [DATA_GENERATION]
- Set up [CONFIG_MANAGEMENT] for environment consistency
- Use [DEPLOYMENT_PIPELINE] for automated deployments
- Monitor environments with [ENVIRONMENT_MONITORING]

**Automated Testing Pipeline:**
- Design [AUTOMATION_STRATEGY] with [TOOL_INTEGRATION]
- Implement [CONTINUOUS_AUTOMATION] in CI/CD
- Set up [PIPELINE_TESTING] with [QUALITY_GATES]
- Configure [FEEDBACK_LOOPS] for rapid iteration
- Monitor [CONTINUOUS_METRICS] for improvement

**Performance Testing Strategy:**
- Conduct [LOAD_TESTING] up to [RESPONSE_TIME_TARGETS]
- Perform [STRESS_TESTING] and [SCALABILITY_TESTING]
- Monitor [RESOURCE_UTILIZATION] during tests
- Test [SPIKE_TESTING] and [ENDURANCE_TESTING] scenarios
- Validate [CAPACITY_TESTING] requirements

**Security Testing Implementation:**
- Perform [PENETRATION_TESTING] and [VULNERABILITY_ASSESSMENT]
- Test [AUTHENTICATION_TESTING] and [AUTHORIZATION_TESTING]
- Validate [INPUT_VALIDATION_TESTING] and [SQL_INJECTION_TESTING]
- Check [XSS_TESTING] and [CSRF_TESTING] vulnerabilities
- Implement [SESSION_MANAGEMENT_TESTING]

**Risk Management:**
- Apply [RISK_IDENTIFICATION] and [RISK_ASSESSMENT_PROCESS]
- Prioritize testing with [TEST_PRIORITIZATION] based on [BUSINESS_IMPACT]
- Focus on [CRITICAL_PATH_TESTING] for high-risk areas
- Implement [RISK_MITIGATION] strategies
- Monitor [TECHNICAL_RISK] and [SCHEDULE_RISK]

Please provide detailed test plans, automation scripts, performance benchmarks, security test cases, and comprehensive reporting mechanisms. Include test data requirements, environment setup guides, and continuous improvement processes.

## Usage Examples

### E-commerce Application Testing
```
Design a comprehensive testing strategy for ShopFlow e-commerce web application using Agile testing methodology. The testing should achieve 85% code coverage and meet enterprise-grade quality requirements.

Testing Framework Setup:
- Implement Jest for unit testing with Sinon mocking strategy
- Use Cypress for end-to-end testing across Chrome, Firefox, Safari browsers
- Set up Postman/Newman for API testing with OpenAPI contract testing
- Configure TestCafe automation framework for cross-browser testing
- Integrate with Jenkins CI/CD pipeline

Test Coverage Requirements:
- Unit tests covering payment processing, cart management, user authentication with Chai assertion library
- Integration tests for payment gateway, inventory system, user service APIs
- End-to-end tests covering purchase journey, user registration, order management scenarios
- Performance tests meeting <2s page load, 1000 concurrent users requirements
- Security tests including OWASP Top 10 vulnerability assessment

### Quality Assurance Process
- Implement Agile QA methodology with peer review process
- Use Jira for defect management
- Apply Critical/High/Medium/Low severity and P1/P2/P3/P4 priority classification
- Set up automated quality gates and 95% test pass release criteria
- Create Allure reporting framework with coverage, performance, defect metrics
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[APPLICATION_TYPE]` | Application type | "Web application (React SPA)", "Mobile app (iOS/Android)", "REST API service", "Microservices platform", "Desktop application" |
| `[TESTING_APPROACH]` | Testing approach | "Agile testing methodology", "Risk-based testing", "Behavior-driven development (BDD)", "Test-driven development (TDD)" |
| `[TESTING_PHILOSOPHY]` | Testing philosophy | "Shift-left testing", "Continuous testing", "Quality built-in, not tested-in", "Test early, test often, test automatically" |
| `[QUALITY_STANDARDS]` | Quality standards | "ISO 25010 quality model", "80% code coverage minimum", "Zero critical defects at release", "OWASP compliance" |
| `[TESTING_BUDGET]` | Testing budget | "$50,000 annually", "20% of development budget", "2 dedicated QA engineers", "Cloud testing infrastructure included" |
| `[TESTING_TIMELINE]` | Testing timeline | "2-week sprint testing cycles", "Continuous testing in CI/CD", "3-month test automation buildout", "Release testing: 1 week" |
| `[TEAM_STRUCTURE]` | Team structure | "2 QA Engineers, 1 SDET, 1 QA Lead", "Embedded QA in each scrum team", "Centralized QA COE", "Developers own unit tests, QA owns E2E" |
| `[RISK_ASSESSMENT]` | Risk assessment | "Payment flows: High risk", "User registration: Medium risk", "Static content: Low risk", "Third-party integrations: High risk" |
| `[SUCCESS_CRITERIA]` | Success criteria | "95% test pass rate", "Zero P1 defects in production", "Test execution < 30 minutes", "< 5% test flakiness" |
| `[REPORTING_REQUIREMENTS]` | Reporting requirements | "Daily test execution reports", "Weekly quality dashboards", "Sprint test summary", "Release readiness report" |
| `[TEST_SCOPE]` | Test scope | "All user-facing features", "API endpoints v2.x", "Critical business workflows only", "Full regression suite" |
| `[TEST_OBJECTIVES]` | Test objectives | "Validate functional requirements", "Ensure 99.9% uptime", "Verify security compliance", "Confirm performance SLAs" |
| `[TESTING_TYPES]` | Testing types | "Unit, Integration, E2E, Performance, Security", "Functional, Non-functional, Regression", "Smoke, Sanity, Full regression" |
| `[TEST_ENVIRONMENT]` | Test environment | "Dedicated QA environment on AWS", "Docker containers for isolation", "Staging mirror of production", "Local dev + CI environment" |
| `[TEST_DATA_REQUIREMENTS]` | Test data requirements | "Anonymized production data subset", "Synthetic data generated via Faker.js", "Seed database scripts", "Test fixtures in JSON" |
| `[ENTRY_CRITERIA]` | Entry criteria | "Code complete and deployed to QA", "Unit tests passing (80%+)", "Feature documentation available", "Test environment stable" |
| `[EXIT_CRITERIA]` | Exit criteria | "All P1/P2 defects resolved", "95% test cases passed", "Performance benchmarks met", "Security scan passed" |
| `[SUSPENSION_CRITERIA]` | Suspension criteria | "Critical defect blocking testing", "Environment instability > 2 hours", "Missing test data", "Build failures" |
| `[RESUMPTION_CRITERIA]` | Resumption criteria | "Blocking defect resolved", "Environment restored", "Build green", "Test data available" |
| `[TEST_DELIVERABLES]` | Test deliverables | "Test plan document", "Test cases in TestRail", "Automation scripts in Git", "Test execution reports", "Defect summary" |
| `[UNIT_TESTING_FRAMEWORK]` | Unit testing framework | "Jest for JavaScript/TypeScript", "pytest for Python", "JUnit 5 for Java", "XCTest for Swift", "NUnit for .NET" |
| `[UNIT_COVERAGE_TARGET]` | Unit coverage target | "80% line coverage", "70% branch coverage", "100% for critical paths", "Increase 5% per sprint" |
| `[MOCKING_STRATEGY]` | Mocking strategy | "Jest mocks for modules", "Sinon.js for stubs/spies", "Mockito for Java", "unittest.mock for Python", "WireMock for HTTP" |
| `[UNIT_TEST_DATA]` | Unit test data | "Factory functions for test objects", "Fixtures in __tests__/fixtures/", "Builder pattern for complex objects", "Faker.js for random data" |
| `[ASSERTION_LIBRARY]` | Assertion library | "Jest expect matchers", "Chai assertions", "AssertJ for Java", "pytest assertions", "Fluent Assertions for .NET" |
| `[TEST_ORGANIZATION]` | Test organization | "Mirror src/ structure in tests/", "Co-located with source files", "Grouped by feature/module", "Separate unit/integration folders" |
| `[TEST_NAMING_CONVENTIONS]` | Test naming conventions | "describe('Component', () => it('should...'))", "test_function_condition_expected_result", "MethodName_StateUnderTest_ExpectedBehavior" |
| `[UNIT_TEST_DOCUMENTATION]` | Unit test documentation | "JSDoc comments for complex tests", "README in test directories", "Test case descriptions in BDD style", "Coverage reports as docs" |
| `[UNIT_CI_INTEGRATION]` | Unit CI integration | "Run on every commit", "Block PR on test failure", "Parallel test execution", "Test results published to PR comments" |
| `[COVERAGE_TOOLS]` | Coverage tools | "Istanbul/nyc for JavaScript", "coverage.py for Python", "JaCoCo for Java", "Codecov for reporting", "SonarQube for analysis" |
| `[INTEGRATION_STRATEGY]` | Integration strategy | "Bottom-up integration", "Top-down with stubs", "Big bang for small systems", "Continuous integration testing" |
| `[INTEGRATION_POINTS]` | Integration points | "Database connections", "External APIs (Stripe, SendGrid)", "Message queues (RabbitMQ, Kafka)", "Cache layer (Redis)" |
| `[API_TESTING]` | API testing approach | "Supertest for Node.js APIs", "REST Assured for Java", "requests + pytest for Python", "Postman/Newman for automation" |
| `[DATABASE_TESTING]` | Database testing | "Test containers for isolated DB", "Seed data before tests, cleanup after", "Transaction rollback for isolation" |
| `[EXTERNAL_SERVICE_TESTING]` | External service testing | "WireMock for HTTP service mocks", "LocalStack for AWS services", "Mock server for third-party APIs" |
| `[MESSAGE_QUEUE_TESTING]` | Message queue testing | "Testcontainers for RabbitMQ/Kafka", "In-memory queue for unit tests", "Contract tests for message schemas" |
| `[FILE_SYSTEM_TESTING]` | File system testing | "Temp directories for isolation", "mock-fs for Node.js", "Virtual file system for tests" |
| `[NETWORK_TESTING]` | Network testing | "Nock for HTTP mocking", "Test with network latency simulation", "Chaos engineering with tc/netem" |
| `[CONFIGURATION_TESTING]` | Configuration testing | "Test all environment configurations", "Validate config schema", "Test feature flag combinations" |
| `[INTEGRATION_ENVIRONMENT]` | Integration environment | "Docker Compose for local stack", "Kubernetes namespace per PR", "Shared integration server", "Ephemeral environments" |
| `[E2E_FRAMEWORK]` | E2E framework | "Cypress for web apps", "Playwright for cross-browser", "Selenium WebDriver", "TestCafe", "Puppeteer for Chrome" |
| `[BROWSER_SUPPORT]` | Browser support | "Chrome (latest 2 versions), Firefox, Safari, Edge", "Mobile Chrome/Safari", "IE11 for legacy support" |
| `[DEVICE_TESTING]` | Device testing | "BrowserStack for real devices", "Sauce Labs cloud", "Local device lab", "Responsive testing with viewport emulation" |
| `[USER_JOURNEY_TESTING]` | User journey testing | "Critical paths: signup, checkout, login", "Happy path + error scenarios", "User persona-based journeys" |
| `[CROSS_PLATFORM_TESTING]` | Cross-platform testing | "macOS, Windows, Linux for desktop", "iOS 14+, Android 10+ for mobile", "Electron for desktop apps" |
| `[ACCESSIBILITY_TESTING]` | Accessibility testing approach | "axe-core automated checks", "Manual screen reader testing", "Lighthouse accessibility audit", "WAVE browser extension" |
| `[VISUAL_REGRESSION_TESTING]` | Visual regression testing | "Percy for visual diffs", "Chromatic for Storybook", "BackstopJS for screenshots", "Applitools for AI visual testing" |
| `[MOBILE_TESTING]` | Mobile E2E testing | "Appium for cross-platform", "Detox for React Native", "XCUITest for iOS", "Espresso for Android" |
| `[E2E_PERFORMANCE_MONITORING]` | E2E performance monitoring | "Lighthouse CI for web vitals", "Custom timing markers", "Network waterfall analysis", "Core Web Vitals tracking" |
| `[E2E_TEST_DATA]` | E2E test data | "Dedicated test accounts", "API-seeded test data", "Database snapshots", "Test data cleanup hooks" |
| `[PERFORMANCE_REQUIREMENTS]` | Performance requirements | "P99 < 200ms", "Support 1000 concurrent users", "Page load < 2s", "API response < 100ms" |
| `[LOAD_TESTING]` | Load testing | "k6 scripts for API load testing", "Gatling for high-volume tests", "JMeter for distributed load", "Locust for Python-based tests" |
| `[STRESS_TESTING]` | Stress testing | "Gradually increase to 150% normal load", "Find breaking point", "Monitor error rates under stress", "Test graceful degradation" |
| `[VOLUME_TESTING]` | Volume testing | "Test with 1M records in database", "Large file uploads (100MB+)", "Bulk API operations", "Data retention testing" |
| `[SPIKE_TESTING]` | Spike testing | "Sudden 10x traffic increase", "Flash sale simulation", "Recovery time measurement", "Auto-scaling validation" |
| `[ENDURANCE_TESTING]` | Endurance testing | "24-hour sustained load test", "Memory leak detection", "Resource exhaustion monitoring", "Long-running transaction testing" |
| `[SCALABILITY_TESTING]` | Scalability testing | "Horizontal scaling validation", "Database connection pooling limits", "Cache invalidation at scale", "Message queue throughput" |
| `[CAPACITY_TESTING]` | Capacity testing | "Maximum concurrent users", "Storage limits testing", "API rate limit validation", "Infrastructure threshold testing" |
| `[RESOURCE_UTILIZATION]` | Resource utilization monitoring | "CPU, Memory, Disk I/O during tests", "Network bandwidth usage", "Database connection pool usage", "Prometheus metrics during load" |
| `[RESPONSE_TIME_TARGETS]` | Response time targets | "P50 < 50ms, P95 < 150ms, P99 < 200ms", "Time to first byte < 100ms", "Full page render < 2s" |
| `[SECURITY_FRAMEWORK]` | Security testing framework | "OWASP Testing Guide", "NIST Cybersecurity Framework", "PTES (Penetration Testing Execution Standard)", "CIS Controls" |
| `[VULNERABILITY_ASSESSMENT]` | Vulnerability assessment | "OWASP ZAP automated scans", "Snyk for dependency scanning", "Trivy for container scanning", "SonarQube security rules" |
| `[PENETRATION_TESTING]` | Penetration testing | "Annual third-party pentest", "Bug bounty program", "Internal red team exercises", "Automated DAST in CI/CD" |
| `[AUTHENTICATION_TESTING]` | Authentication testing | "Brute force protection", "Password policy enforcement", "MFA bypass testing", "OAuth flow validation", "Session fixation tests" |
| `[AUTHORIZATION_TESTING]` | Authorization testing | "IDOR vulnerability testing", "Privilege escalation tests", "Role-based access verification", "Horizontal/vertical authz testing" |
| `[SESSION_MANAGEMENT_TESTING]` | Session management testing | "Session timeout validation", "Secure cookie attributes", "Concurrent session handling", "Session invalidation on logout" |
| `[INPUT_VALIDATION_TESTING]` | Input validation testing | "Boundary value testing", "Special character handling", "Maximum length validation", "Type coercion testing" |
| `[SQL_INJECTION_TESTING]` | SQL injection testing | "SQLMap automated testing", "Parameterized query verification", "Stored procedure injection", "Second-order injection tests" |
| `[XSS_TESTING]` | XSS testing | "Reflected XSS testing", "Stored XSS in user content", "DOM-based XSS", "CSP header validation" |
| `[CSRF_TESTING]` | CSRF testing | "CSRF token validation", "SameSite cookie testing", "Referer header checks", "State-changing request protection" |
| `[AUTOMATION_STRATEGY]` | Automation strategy | "Automate regression tests first", "80% automation, 20% manual exploratory", "Page Object Model design pattern", "Data-driven test approach" |
| `[AUTOMATION_TOOLS]` | Automation tools | "Cypress + Playwright for E2E", "Jest for unit tests", "k6 for performance", "GitHub Actions for CI" |
| `[AUTOMATION_FRAMEWORK]` | Automation framework | "Custom framework built on Playwright", "Robot Framework for keyword-driven", "Cucumber for BDD", "TestNG for Java test organization" |
| `[CICD_INTEGRATION]` | CI/CD integration | "GitHub Actions workflow", "Jenkins pipeline", "GitLab CI/CD", "Azure DevOps pipelines", "CircleCI orbs" |
| `[AUTOMATED_TEST_SUITE]` | Automated test suite | "500 unit tests, 100 integration, 50 E2E", "Smoke suite (15 min), Full regression (2 hr)", "Nightly full suite execution" |
| `[TEST_EXECUTION]` | Test execution | "Parallel execution across 10 workers", "Retry flaky tests 2x", "Fail-fast on critical test failures", "Test sharding for speed" |
| `[RESULT_ANALYSIS]` | Result analysis | "Allure reports for detailed results", "Slack notifications on failure", "Test trend analysis in dashboard", "Flaky test detection" |
| `[MAINTENANCE_STRATEGY]` | Maintenance strategy | "Refactor tests with code changes", "Quarantine flaky tests", "Weekly test review sessions", "Delete obsolete tests" |
| `[AUTOMATION_ROI]` | Automation ROI | "30% reduction in regression time", "Catch bugs 3x faster", "50% less manual testing effort", "Track savings per sprint" |
| `[AUTOMATION_SKILLS]` | Automation skills required | "JavaScript/TypeScript for Cypress/Playwright", "Python for pytest", "Git for version control", "Docker basics for containerized tests" |
| `[API_TESTING_TOOLS]` | API testing tools | "Postman/Newman for collections", "REST Assured for Java", "Supertest for Node.js", "httpx for Python", "Insomnia for manual testing" |
| `[REQUEST_TESTING]` | Request testing | "Valid/invalid parameter combinations", "Required vs optional fields", "Data type validation", "Boundary values for parameters" |
| `[RESPONSE_VALIDATION]` | Response validation | "JSON Schema validation", "Response time assertions", "Data accuracy verification", "Pagination correctness" |
| `[STATUS_CODE_TESTING]` | Status code testing | "200 OK for success", "201 Created for POST", "400 Bad Request validation", "401/403 for auth errors", "404 for missing resources", "500 for server errors" |
| `[HEADER_TESTING]` | Header testing | "Content-Type validation", "Authorization header handling", "CORS header verification", "Cache-Control headers", "Custom header propagation" |
| `[PAYLOAD_TESTING]` | Payload testing | "Large payload handling", "Empty payload behavior", "Malformed JSON rejection", "Encoding validation (UTF-8)", "Nested object depth limits" |
| `[API_AUTHENTICATION_TESTING]` | API authentication testing | "JWT token validation", "API key authentication", "OAuth token flow", "Token expiration handling", "Invalid credentials rejection" |
| `[RATE_LIMITING_TESTING]` | Rate limiting testing | "Verify 429 responses at limit", "Check Retry-After header", "Test limit reset behavior", "Validate per-user vs global limits" |
| `[ERROR_HANDLING_TESTING]` | Error handling testing | "Error message format validation", "Error codes documentation match", "Stack trace not exposed", "Graceful error responses" |
| `[CONTRACT_TESTING]` | Contract testing | "Pact for consumer-driven contracts", "OpenAPI schema validation", "Breaking change detection", "Backward compatibility verification" |
| `[DATABASE_TESTING_STRATEGY]` | Database testing strategy | "Testcontainers for isolated testing", "Seed data per test suite", "Transaction rollback after each test", "Separate DB per test environment" |
| `[DATA_INTEGRITY_TESTING]` | Data integrity testing | "Verify CRUD operations correctness", "Check data after batch operations", "Validate data transformation accuracy", "Audit trail verification" |
| `[TRANSACTION_TESTING]` | Transaction testing | "ACID property validation", "Rollback on failure testing", "Nested transaction behavior", "Deadlock handling verification" |
| `[CONCURRENCY_TESTING]` | Concurrency testing | "Race condition detection", "Optimistic locking validation", "Concurrent write conflict handling", "Connection pool exhaustion testing" |
| `[BACKUP_RECOVERY_TESTING]` | Backup recovery testing | "Point-in-time recovery testing", "Full backup restoration", "Data consistency after recovery", "Recovery time measurement" |
| `[MIGRATION_TESTING]` | Migration testing | "Up/down migration reversibility", "Data preservation during migration", "Schema version tracking", "Zero-downtime migration validation" |
| `[DB_PERFORMANCE_TESTING]` | DB performance testing | "Slow query detection", "Index effectiveness validation", "Query execution plan analysis", "Connection pool performance" |
| `[DB_SECURITY_TESTING]` | DB security testing | "Encryption at rest verification", "Access control validation", "SQL injection prevention", "Audit logging completeness" |
| `[REFERENTIAL_INTEGRITY]` | Referential integrity testing | "Foreign key constraint validation", "Cascade delete behavior", "Orphan record detection", "Cross-table relationship consistency" |
| `[CONSTRAINT_TESTING]` | Constraint testing | "NOT NULL enforcement", "UNIQUE constraint validation", "CHECK constraint behavior", "DEFAULT value application" |
| `[MOBILE_TESTING_STRATEGY]` | Mobile testing strategy | "Appium for cross-platform automation", "Real device cloud (BrowserStack)", "Emulator for quick dev testing", "Beta testing via TestFlight/Play Console" |
| `[DEVICE_COVERAGE]` | Device coverage | "Top 10 devices by market share", "iPhone 12-15 series, Samsung Galaxy S21-S24", "Tablets: iPad Pro, Samsung Tab", "Various screen sizes and densities" |
| `[OS_TESTING]` | OS version testing | "iOS 15+, Android 10+", "Latest 3 major versions", "Beta OS testing before release", "OS-specific feature validation" |
| `[APP_STORE_TESTING]` | App store testing | "Pre-submission compliance checks", "Screenshot accuracy verification", "In-app purchase flow testing", "App Store review guideline compliance" |
| `[OFFLINE_TESTING]` | Offline testing | "Graceful offline degradation", "Data sync after reconnection", "Offline queue processing", "Local storage functionality" |
| `[BATTERY_TESTING]` | Battery testing | "Battery drain during active use", "Background battery consumption", "Profiling with Instruments/Battery Historian", "Power-intensive feature optimization" |
| `[MEMORY_TESTING]` | Memory testing | "Memory leak detection", "Large dataset handling", "Low memory condition behavior", "Memory profiling with Xcode/Android Studio" |
| `[MOBILE_NETWORK_TESTING]` | Mobile network testing | "3G/4G/5G performance", "Network transition handling", "Airplane mode behavior", "Slow network simulation (Charles Proxy)" |
| `[MOBILE_USABILITY_TESTING]` | Mobile usability testing | "Touch target size validation", "Gesture responsiveness", "One-handed usability", "Accessibility compliance (VoiceOver/TalkBack)" |
| `[PUSH_NOTIFICATION_TESTING]` | Push notification testing | "Notification delivery reliability", "Deep link handling from notification", "Permission request flow", "Notification grouping behavior" |
| `[ACCESSIBILITY_STANDARDS]` | Accessibility standards | "WCAG 2.1 AA compliance", "Section 508 for government", "ADA compliance", "EN 301 549 for EU" |
| `[SCREEN_READER_TESTING]` | Screen reader testing | "VoiceOver on iOS/macOS", "NVDA and JAWS on Windows", "TalkBack on Android", "Verify reading order and announcements" |
| `[KEYBOARD_NAVIGATION_TESTING]` | Keyboard navigation testing | "Tab order validation", "Focus visible indicator", "Skip links functionality", "Keyboard trap prevention" |
| `[COLOR_CONTRAST_TESTING]` | Color contrast testing | "4.5:1 ratio for normal text", "3:1 for large text", "axe-core automated checks", "Manual verification for gradients" |
| `[ALT_TEXT_TESTING]` | Alt text testing | "Descriptive alt text for images", "Empty alt for decorative images", "Complex image descriptions", "Chart/graph accessibility" |
| `[FOCUS_MANAGEMENT_TESTING]` | Focus management testing | "Modal focus trapping", "Focus restoration after close", "Dynamic content focus handling", "Skip to main content link" |
| `[ARIA_TESTING]` | ARIA testing | "Correct ARIA roles", "Live region announcements", "ARIA labels and descriptions", "Widget patterns compliance" |
| `[RESPONSIVE_DESIGN_TESTING]` | Responsive design testing | "320px to 4K viewport testing", "Touch target sizing (44x44px)", "Landscape/portrait orientation", "Zoom up to 200% usability" |
| `[MEDIA_TESTING]` | Media accessibility testing | "Video captions accuracy", "Audio descriptions availability", "Media player keyboard controls", "Transcript availability" |
| `[FORM_ACCESSIBILITY_TESTING]` | Form accessibility testing | "Label association with inputs", "Error message announcements", "Required field indicators", "Autocomplete attributes" |
| `[TEST_DATA_STRATEGY]` | Test data strategy | "Synthetic data for most tests", "Masked production data for integration", "Dedicated test accounts for E2E", "API-driven test data creation" |
| `[DATA_GENERATION]` | Data generation | "Faker.js for realistic fake data", "Factory patterns for object creation", "SQL scripts for bulk data", "JSON fixtures for static scenarios" |
| `[DATA_MASKING]` | Data masking | "PII anonymization (names, emails)", "Credit card number masking", "Address generalization", "Consistent masking across related fields" |
| `[DATA_PRIVACY]` | Data privacy | "No production PII in test environments", "GDPR-compliant test data", "Data retention policies for test data", "Secure deletion after testing" |
| `[SYNTHETIC_DATA]` | Synthetic data | "Statistically representative distributions", "Edge cases and boundary conditions", "Locale-specific data (addresses, names)", "Time-series data generation" |
| `[DATA_REFRESH]` | Data refresh | "Weekly refresh from masked production", "On-demand refresh for specific tests", "Incremental updates vs full refresh", "Refresh validation checks" |
| `[DATA_VERSIONING]` | Data versioning | "Git-tracked seed scripts", "Versioned database snapshots", "Migration-aligned test data", "Rollback capability for test data" |
| `[DATA_CLEANUP]` | Data cleanup | "AfterEach hooks for cleanup", "Database truncation between suites", "Orphan data detection", "Automated cleanup jobs nightly" |
| `[DATA_BACKUP]` | Data backup | "Test data snapshots before major changes", "Quick restore capability", "Shared test data repository", "Version control for fixtures" |
| `[DATA_COMPLIANCE]` | Data compliance | "Data classification for test data", "Audit trail for data access", "Compliance checks in CI pipeline", "Regular data compliance reviews" |
| `[ENVIRONMENT_STRATEGY]` | Environment strategy | "Environment per feature branch", "Shared staging environment", "Production-like performance environment", "Ephemeral environments for PR testing" |
| `[ENVIRONMENT_TYPES]` | Environment types | "Local dev, CI, QA, Staging, UAT, Production", "Performance testing environment", "Security testing sandbox", "DR environment" |
| `[ENVIRONMENT_SETUP]` | Environment setup | "Infrastructure as Code (Terraform)", "Docker Compose for local", "Kubernetes manifests for cloud", "Automated provisioning scripts" |
| `[CONFIG_MANAGEMENT]` | Configuration management | "Environment variables in secrets manager", "Feature flags per environment", "Config validation on startup", "Diff tool for config changes" |
| `[DEPLOYMENT_PIPELINE]` | Deployment pipeline | "GitHub Actions for CI", "ArgoCD for GitOps deployment", "Blue-green deployments", "Canary releases for production" |
| `[ENVIRONMENT_MONITORING]` | Environment monitoring | "Health checks for all services", "Resource utilization dashboards", "Alert on environment drift", "Synthetic monitoring probes" |
| `[RESOURCE_MANAGEMENT]` | Resource management | "Auto-scaling for load tests", "Resource quotas per environment", "Cost allocation tracking", "Cleanup unused environments" |
| `[ACCESS_CONTROL]` | Access control | "RBAC for environment access", "SSO integration", "Audit logs for environment changes", "Least privilege principle" |
| `[ENVIRONMENT_REFRESH]` | Environment refresh | "Nightly refresh of QA from staging", "On-demand refresh triggers", "Data sync between environments", "Schema migration verification" |
| `[ENVIRONMENT_TROUBLESHOOTING]` | Environment troubleshooting | "Centralized logging (ELK)", "Distributed tracing", "Environment health dashboard", "Runbook for common issues" |
| `[DEFECT_LIFECYCLE]` | Defect lifecycle | "New -> Triaged -> In Progress -> Fixed -> Verified -> Closed", "Reopened state for regressions", "Won't Fix with justification" |
| `[BUG_TRACKING_TOOL]` | Bug tracking tool | "Jira for enterprise", "Linear for startups", "GitHub Issues for open source", "Azure DevOps Boards", "Bugzilla" |
| `[SEVERITY_CLASSIFICATION]` | Severity classification | "Critical: System down, data loss", "High: Major feature broken", "Medium: Feature degraded", "Low: Cosmetic issues" |
| `[PRIORITY_CLASSIFICATION]` | Priority classification | "P1: Fix immediately", "P2: Fix this sprint", "P3: Fix next sprint", "P4: Backlog" |
| `[ESCALATION_PROCESS]` | Escalation process | "P1 bugs escalate to tech lead immediately", "48hr SLA for P2 triage", "Weekly review for P3/P4", "Stakeholder notification for blockers" |
| `[ROOT_CAUSE_ANALYSIS]` | Root cause analysis | "5 Whys technique", "Fishbone diagram for complex issues", "Post-mortem for production bugs", "Prevention action items required" |
| `[REGRESSION_TESTING]` | Regression testing | "Automated regression suite on every build", "Risk-based regression selection", "Full regression before release", "Regression test for every bug fix" |
| `[DEFECT_METRICS]` | Defect metrics | "Defect density (bugs/KLOC)", "Defect escape rate", "Mean time to resolution", "Defect aging report", "Reopened defect rate" |
| `[QUALITY_GATES]` | Quality gates | "No P1/P2 bugs open", "80%+ code coverage", "All security scans passed", "Performance benchmarks met" |
| `[RELEASE_CRITERIA]` | Release criteria | "95% test pass rate", "Zero critical bugs", "Sign-off from QA lead", "Regression suite green", "Performance within SLA" |
| `[REPORTING_FRAMEWORK]` | Reporting framework | "Allure for test reports", "ReportPortal for aggregation", "Grafana dashboards", "Custom reports in Confluence" |
| `[TEST_METRICS]` | Test metrics | "Test pass/fail rate", "Test execution time", "Flaky test percentage", "Automation coverage ratio" |
| `[COVERAGE_REPORTS]` | Coverage reports | "Line and branch coverage", "Coverage trend over time", "Uncovered critical paths highlighted", "PR coverage diff reports" |
| `[PERFORMANCE_REPORTS]` | Performance reports | "Response time percentiles (P50/P95/P99)", "Throughput graphs", "Error rate under load", "Resource utilization during tests" |
| `[DEFECT_REPORTS]` | Defect reports | "Open bugs by severity/priority", "Bug burndown chart", "Defect aging report", "Bugs by component/feature" |
| `[DASHBOARD_DESIGN]` | Dashboard design | "Real-time test execution status", "Quality trends over sprints", "Release readiness scorecard", "Team performance metrics" |
| `[STAKEHOLDER_REPORTS]` | Stakeholder reports | "Weekly quality summary email", "Sprint retrospective quality section", "Release go/no-go report", "Monthly quality trends" |
| `[EXECUTIVE_SUMMARY]` | Executive summary | "Overall quality health score", "Key risks and blockers", "Release confidence level", "Comparison to previous releases" |
| `[TREND_ANALYSIS]` | Trend analysis | "Defect trend over releases", "Test automation growth", "Quality improvement over time", "Predictive quality metrics" |
| `[RISK_ASSESSMENT_REPORTING]` | Risk assessment reporting | "High-risk areas identified", "Test coverage gaps", "Technical debt impact", "Mitigation status tracking" |
| `[QA_METHODOLOGY]` | QA methodology | "Agile testing methodology", "Risk-based testing", "Exploratory testing sessions", "Shift-left quality approach" |
| `[REVIEW_PROCESS]` | Review process | "Peer review for test cases", "Test plan review by stakeholders", "Automation code review", "Sprint retrospective quality review" |
| `[CODE_REVIEW_PROCESS]` | Code review process | "PR required for all changes", "2 approvals minimum", "CI checks must pass", "Test coverage check in review" |
| `[TEST_REVIEW_PROCESS]` | Test review process | "Test case peer review", "Automation script review", "Test plan approval", "Post-execution review for findings" |
| `[DOCUMENTATION_REVIEW]` | Documentation review | "Test documentation kept current", "Runbook review quarterly", "API documentation accuracy check", "Release notes review" |
| `[PROCESS_IMPROVEMENT]` | Process improvement | "Sprint retrospectives for QA", "Defect root cause analysis", "Automation ROI tracking", "Continuous improvement backlog" |
| `[BEST_PRACTICES]` | Best practices | "Test pyramid adherence", "Independent test execution", "Meaningful test names", "Avoid test interdependencies", "Clean test data management" |
| `[TRAINING_REQUIREMENTS]` | Training requirements | "Automation framework training", "Security testing basics", "Performance testing tools", "New team member onboarding" |
| `[CERTIFICATION_REQUIREMENTS]` | Certification requirements | "ISTQB Foundation for QA team", "AWS certification for cloud testing", "Security testing certification (CEH)", "Tool-specific certifications" |
| `[KNOWLEDGE_MANAGEMENT]` | Knowledge management | "Confluence for test documentation", "Wiki for testing guides", "Recorded training sessions", "Cross-training sessions" |
| `[RISK_IDENTIFICATION]` | Risk identification | "Feature complexity analysis", "Historical defect patterns", "New technology risks", "Integration complexity assessment" |
| `[RISK_ASSESSMENT_PROCESS]` | Risk assessment process | "Risk matrix (likelihood x impact)", "Risk scoring 1-5 scale", "Risk owner assignment", "Regular risk review meetings" |
| `[RISK_MITIGATION]` | Risk mitigation | "Additional testing for high-risk areas", "Spike for unknown technologies", "Parallel testing tracks", "Contingency time buffer" |
| `[TEST_PRIORITIZATION]` | Test prioritization | "Critical business flows first", "Recently changed code priority", "High-risk areas prioritized", "Customer-impacting features first" |
| `[CRITICAL_PATH_TESTING]` | Critical path testing | "User authentication flow", "Payment processing", "Core business transactions", "Data integrity operations" |
| `[BUSINESS_IMPACT]` | Business impact assessment | "Revenue impact if feature fails", "Customer satisfaction impact", "Regulatory compliance impact", "Reputation risk" |
| `[TECHNICAL_RISK]` | Technical risk | "New framework/library risks", "Performance scalability concerns", "Security vulnerability potential", "Integration complexity" |
| `[SCHEDULE_RISK]` | Schedule risk | "Test environment availability", "Third-party dependencies", "Resource availability", "Scope creep impact on testing" |
| `[RESOURCE_RISK]` | Resource risk | "QA team capacity", "Specialized skill availability", "Tool/license availability", "Knowledge transfer gaps" |
| `[QUALITY_RISK]` | Quality risk | "Insufficient test coverage", "Inadequate test data", "Flaky test impact", "Technical debt in test suite" |
| `[CONTINUOUS_INTEGRATION]` | Continuous integration | "Tests run on every commit", "Branch protection with test gates", "Parallel test execution", "Fast feedback (< 10 min for PR checks)" |
| `[PIPELINE_TESTING]` | Pipeline testing | "Unit tests -> Integration -> E2E", "Staged test execution", "Environment-specific test suites", "Deployment verification tests" |
| `[SHIFT_LEFT_TESTING]` | Shift-left testing | "Unit tests written with code", "Test review in PR process", "Early involvement in requirements", "Static analysis in pre-commit hooks" |
| `[CONTINUOUS_AUTOMATION]` | Continuous automation | "Auto-generate tests from specs", "Self-healing test locators", "AI-assisted test maintenance", "Continuous automation backlog" |
| `[FEEDBACK_LOOPS]` | Feedback loops | "Instant test failure notifications", "Daily quality standup", "Sprint quality retrospective", "Customer feedback integration" |
| `[CONTINUOUS_QUALITY_GATES]` | Continuous quality gates | "Coverage threshold enforcement", "No high-severity bugs", "Performance regression check", "Security scan must pass" |
| `[MONITORING_INTEGRATION]` | Monitoring integration | "Test results in Datadog/Grafana", "Quality metrics in dashboards", "Alert on test failures", "Correlation with production metrics" |
| `[DEVOPS_COLLABORATION]` | DevOps collaboration | "Shared ownership of quality", "QA in deployment pipeline design", "Joint incident response", "Infrastructure as code for test environments" |
| `[TOOL_INTEGRATION]` | Tool integration | "CI/CD <-> Test framework integration", "Bug tracker <-> Test management", "Slack notifications", "Single sign-on across tools" |
| `[CONTINUOUS_METRICS]` | Continuous metrics | "Build success rate", "Test execution duration trends", "Defect escape rate", "MTTR for test failures", "Automation ROI tracking" |

### Mobile Banking App Testing
```
Design a comprehensive testing strategy for SecureBank mobile banking application using risk-based testing methodology. The testing should achieve 90% code coverage and meet financial regulatory quality requirements.

Testing Framework Setup:
- Implement XCTest/Espresso for native mobile unit testing with Mock/Stub mocking strategy
- Use Appium for cross-platform mobile testing across iOS/Android devices
- Set up REST Assured for API testing with JSON Schema contract testing
- Configure BrowserStack automation framework for device cloud testing
- Integrate with Azure DevOps CI/CD pipeline

Security Testing Implementation:
- Perform automated penetration testing and SAST/DAST vulnerability assessment
- Test OAuth 2.0/biometric authentication and role-based authorization
- Validate all input validation and SQL injection prevention testing
- Check XSS prevention and CSRF protection vulnerabilities
- Implement secure session management and token validation testing
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Testing & QA Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Software Development](../../technology/Software Development/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating design comprehensive testing strategies including unit tests, integration tests, end-to-end tests, performance testing, security testing, and automated quality assurance processes.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Start testing early in the development cycle (shift-left)**
2. **Implement test automation for repetitive and regression tests**
3. **Use risk-based testing to prioritize critical functionality**
4. **Maintain comprehensive test documentation and reporting**
5. **Integrate testing into CI/CD pipelines for continuous feedback**
6. **Focus on user experience and business-critical scenarios**
7. **Implement proper test data management and environment control**
8. **Use appropriate testing tools for each testing type**
9. **Monitor and analyze test metrics for continuous improvement**
10. **Ensure security and accessibility testing are integral parts of the strategy**