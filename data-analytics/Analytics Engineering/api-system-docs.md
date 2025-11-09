---
title: API and System Documentation Template
category: data-analytics/Analytics Engineering
tags: [api, automation, data-analytics, documentation, integration, template]
use_cases:
  - Creating comprehensive API documentation, integration guides, system interfaces, endpoint specifications, and developer resources for data platforms and services.
  - API documentation
  - Integration guides
related_templates:
  - analytics-documentation-overview.md
  - technical-documentation.md
last_updated: 2025-11-09
---

# API and System Documentation Template

## Purpose
Create comprehensive API documentation, integration guides, system interfaces, endpoint specifications, and developer resources for data platforms and services.

## Template

```
You are an API documentation specialist. Document [API_NAME] for [PLATFORM] covering [ENDPOINTS] with [DOC_STANDARD] format for [DEVELOPER_AUDIENCE].

### API DOCUMENTATION

```
API: [API_NAME]
Version: [VERSION]
Base URL: [BASE_URL]
Protocol: [REST/GraphQL/SOAP/gRPC]

Authentication:
- Method: [AUTH_METHOD]
- Header: Authorization: Bearer [TOKEN]
- API Key: [KEY_LOCATION]

Endpoint: [ENDPOINT_PATH]
Method: [GET/POST/PUT/DELETE/PATCH]
Description: [WHAT_IT_DOES]

Request:
Headers:
  Content-Type: application/json
  Authorization: Bearer {token}

Parameters:
- [PARAM_NAME] (required): [TYPE] - [DESCRIPTION]
- [PARAM_NAME] (optional): [TYPE] - [DESCRIPTION]

Request Body:
{
  "[FIELD]": "[TYPE]",
  "[FIELD]": "[TYPE]"
}

Response:
Status: 200 OK
Body:
{
  "status": "success",
  "data": {
    "[FIELD]": "[VALUE]"
  }
}

Error Responses:
400 Bad Request: [DESCRIPTION]
401 Unauthorized: [DESCRIPTION]
404 Not Found: [DESCRIPTION]
500 Server Error: [DESCRIPTION]

Example Request:
curl -X [METHOD] "[FULL_URL]" \
  -H "Authorization: Bearer [TOKEN]" \
  -H "Content-Type: application/json" \
  -d '[JSON_BODY]'

Example Response:
[SAMPLE_RESPONSE]

Rate Limiting:
- Limit: [REQUESTS] per [TIME_PERIOD]
- Headers: X-RateLimit-Remaining

Code Examples:
Python:
[CODE_EXAMPLE]

JavaScript:
[CODE_EXAMPLE]
```

### INTEGRATION GUIDE

```
Integration: [INTEGRATION_NAME]

Prerequisites:
- [REQUIREMENT_1]
- [REQUIREMENT_2]

Setup Steps:
1. [STEP_1]
2. [STEP_2]

Configuration:
{
  "endpoint": "[URL]",
  "api_key": "[KEY]",
  "timeout": [SECONDS]
}

Authentication Flow:
[DIAGRAM or DESCRIPTION]

Data Synchronization:
- Frequency: [FREQUENCY]
- Method: [PUSH/PULL/WEBHOOK]
- Payload: [FORMAT]

Error Handling:
- Retry logic: [STRATEGY]
- Failure notification: [METHOD]

Testing:
- Sandbox endpoint: [TEST_URL]
- Test credentials: [HOW_TO_OBTAIN]
```

OUTPUT: API reference, integration guides, code examples, SDKs
```

## Variables
- [API_NAME] - API name
- [PLATFORM] - Platform/system
- [ENDPOINTS] - API endpoints
- [DOC_STANDARD] - Documentation standard (OpenAPI/Swagger/etc.)
- [DEVELOPER_AUDIENCE] - Target developers

## Best Practices
1. **Follow OpenAPI standards** - Use standard formats
2. **Provide code examples** - Multiple languages
3. **Document errors clearly** - All error codes
4. **Include authentication** - Clear auth instructions
