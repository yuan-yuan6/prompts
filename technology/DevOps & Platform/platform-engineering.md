---
category: technology/DevOps & Platform
last_updated: 2025-11-09
related_templates:
- cloud-architecture-framework.md
- site-reliability-engineering.md
- cloud-migration-strategy.md
tags:
- automation
- design
- development
- documentation
- framework
- management
- security
- strategy
title: Platform Engineering & Developer Experience Framework
use_cases:
- Creating comprehensive framework for building and managing internal developer platforms,
  self-service infrastructure, golden paths, developer productivity tools, and platform-as-a-product
  approaches.
- Project planning and execution
- Strategy development
---

# Platform Engineering & Developer Experience Framework

## Purpose
Comprehensive framework for building and managing internal developer platforms, self-service infrastructure, golden paths, developer productivity tools, and platform-as-a-product approaches.

## Quick Start

**To Launch Your Platform Engineering Initiative:**
1. **Assess Current State**: Survey developer pain points and measure current DORA metrics
2. **Define Golden Paths**: Create 2-3 standardized service templates (microservice, API, frontend)
3. **Build Self-Service Portal**: Deploy basic infrastructure provisioning for compute, databases, and storage
4. **Implement CI/CD Platform**: Set up automated build, test, and deployment pipelines
5. **Establish Observability**: Deploy metrics, logging, and tracing for all platform services

**Example Starting Point:**
Design platform engineering strategy for [TechCorp] supporting [500] developers across [50] teams, with [200] services, targeting [multiple] deployments/day and [1] hour MTTR.

## Template

Design platform engineering strategy for [ORGANIZATION_NAME] supporting [DEVELOPER_COUNT] developers across [TEAM_COUNT] teams, with [SERVICE_COUNT] services, targeting [DEPLOYMENT_FREQUENCY] deployments/day and [MTTR_TARGET] hour MTTR.

### 1. Platform Architecture Overview

| **Platform Component** | **Current State** | **Target State** | **Adoption Rate** | **Satisfaction** | **ROI** |
|----------------------|------------------|-----------------|------------------|-----------------|---------|
| Self-Service Portal | [PORTAL_CURRENT] | [PORTAL_TARGET] | [PORTAL_ADOPT]% | [PORTAL_SAT]/10 | [PORTAL_ROI]x |
| CI/CD Platform | [CICD_CURRENT] | [CICD_TARGET] | [CICD_ADOPT]% | [CICD_SAT]/10 | [CICD_ROI]x |
| Infrastructure Provisioning | [INFRA_CURRENT] | [INFRA_TARGET] | [INFRA_ADOPT]% | [INFRA_SAT]/10 | [INFRA_ROI]x |
| Observability Stack | [OBS_CURRENT] | [OBS_TARGET] | [OBS_ADOPT]% | [OBS_SAT]/10 | [OBS_ROI]x |
| Security Platform | [SEC_CURRENT] | [SEC_TARGET] | [SEC_ADOPT]% | [SEC_SAT]/10 | [SEC_ROI]x |
| Developer Portal | [DEV_CURRENT] | [DEV_TARGET] | [DEV_ADOPT]% | [DEV_SAT]/10 | [DEV_ROI]x |

### 2. Golden Paths & Service Templates

**Standardized Application Patterns:**
```
Microservice Template:
- Languages Supported: [MICRO_LANGS]
- Framework: [MICRO_FRAMEWORK]
- Boilerplate Code: [MICRO_BOILER]
- CI/CD Pipeline: [MICRO_PIPELINE]
- Monitoring Setup: [MICRO_MONITOR]
- Security Scanning: [MICRO_SECURITY]
- Time to Production: [MICRO_TIME]

API Service Template:
- Specification: [API_SPEC]
- Gateway Integration: [API_GATEWAY]
- Authentication: [API_AUTH]
- Rate Limiting: [API_RATE]
- Documentation: [API_DOCS]
- Testing Suite: [API_TESTING]
- Deployment: [API_DEPLOY]

### Frontend Application
- Frameworks: [FRONT_FRAMEWORKS]
- Build System: [FRONT_BUILD]
- CDN Integration: [FRONT_CDN]
- Performance Monitoring: [FRONT_PERF]
- A/B Testing: [FRONT_AB]
- Analytics: [FRONT_ANALYTICS]
- Deployment: [FRONT_DEPLOY]

### Data Pipeline
- Processing Frameworks: [DATA_FRAMEWORKS]
- Orchestration: [DATA_ORCHESTRATION]
- Data Quality: [DATA_QUALITY]
- Lineage Tracking: [DATA_LINEAGE]
- Cost Management: [DATA_COST]
- Compliance: [DATA_COMPLIANCE]
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[ORGANIZATION_NAME]` | Name of the organization | "John Smith" |
| `[DEVELOPER_COUNT]` | Specify the developer count | "10" |
| `[TEAM_COUNT]` | Specify the team count | "10" |
| `[SERVICE_COUNT]` | Specify the service count | "10" |
| `[DEPLOYMENT_FREQUENCY]` | Specify the deployment frequency | "[specify value]" |
| `[MTTR_TARGET]` | Target or intended mttr | "[specify value]" |
| `[PORTAL_CURRENT]` | Specify the portal current | "[specify value]" |
| `[PORTAL_TARGET]` | Target or intended portal | "[specify value]" |
| `[PORTAL_ADOPT]` | Specify the portal adopt | "[specify value]" |
| `[PORTAL_SAT]` | Specify the portal sat | "[specify value]" |
| `[PORTAL_ROI]` | Specify the portal roi | "[specify value]" |
| `[CICD_CURRENT]` | Specify the cicd current | "[specify value]" |
| `[CICD_TARGET]` | Target or intended cicd | "[specify value]" |
| `[CICD_ADOPT]` | Specify the cicd adopt | "[specify value]" |
| `[CICD_SAT]` | Specify the cicd sat | "[specify value]" |
| `[CICD_ROI]` | Specify the cicd roi | "[specify value]" |
| `[INFRA_CURRENT]` | Specify the infra current | "[specify value]" |
| `[INFRA_TARGET]` | Target or intended infra | "[specify value]" |
| `[INFRA_ADOPT]` | Specify the infra adopt | "[specify value]" |
| `[INFRA_SAT]` | Specify the infra sat | "[specify value]" |
| `[INFRA_ROI]` | Specify the infra roi | "[specify value]" |
| `[OBS_CURRENT]` | Specify the obs current | "[specify value]" |
| `[OBS_TARGET]` | Target or intended obs | "[specify value]" |
| `[OBS_ADOPT]` | Specify the obs adopt | "[specify value]" |
| `[OBS_SAT]` | Specify the obs sat | "[specify value]" |
| `[OBS_ROI]` | Specify the obs roi | "[specify value]" |
| `[SEC_CURRENT]` | Specify the sec current | "[specify value]" |
| `[SEC_TARGET]` | Target or intended sec | "[specify value]" |
| `[SEC_ADOPT]` | Specify the sec adopt | "[specify value]" |
| `[SEC_SAT]` | Specify the sec sat | "[specify value]" |
| `[SEC_ROI]` | Specify the sec roi | "[specify value]" |
| `[DEV_CURRENT]` | Specify the dev current | "[specify value]" |
| `[DEV_TARGET]` | Target or intended dev | "[specify value]" |
| `[DEV_ADOPT]` | Specify the dev adopt | "[specify value]" |
| `[DEV_SAT]` | Specify the dev sat | "[specify value]" |
| `[DEV_ROI]` | Specify the dev roi | "[specify value]" |
| `[MICRO_LANGS]` | Specify the micro langs | "[specify value]" |
| `[MICRO_FRAMEWORK]` | Specify the micro framework | "[specify value]" |
| `[MICRO_BOILER]` | Specify the micro boiler | "[specify value]" |
| `[MICRO_PIPELINE]` | Specify the micro pipeline | "[specify value]" |
| `[MICRO_MONITOR]` | Specify the micro monitor | "[specify value]" |
| `[MICRO_SECURITY]` | Specify the micro security | "[specify value]" |
| `[MICRO_TIME]` | Specify the micro time | "[specify value]" |
| `[API_SPEC]` | Specify the api spec | "[specify value]" |
| `[API_GATEWAY]` | Specify the api gateway | "[specify value]" |
| `[API_AUTH]` | Specify the api auth | "[specify value]" |
| `[API_RATE]` | Specify the api rate | "[specify value]" |
| `[API_DOCS]` | Specify the api docs | "[specify value]" |
| `[API_TESTING]` | Specify the api testing | "[specify value]" |
| `[API_DEPLOY]` | Specify the api deploy | "[specify value]" |
| `[FRONT_FRAMEWORKS]` | Specify the front frameworks | "[specify value]" |
| `[FRONT_BUILD]` | Specify the front build | "[specify value]" |
| `[FRONT_CDN]` | Specify the front cdn | "[specify value]" |
| `[FRONT_PERF]` | Specify the front perf | "[specify value]" |
| `[FRONT_AB]` | Specify the front ab | "[specify value]" |
| `[FRONT_ANALYTICS]` | Specify the front analytics | "[specify value]" |
| `[FRONT_DEPLOY]` | Specify the front deploy | "[specify value]" |
| `[DATA_FRAMEWORKS]` | Specify the data frameworks | "[specify value]" |
| `[DATA_ORCHESTRATION]` | Specify the data orchestration | "[specify value]" |
| `[DATA_QUALITY]` | Specify the data quality | "[specify value]" |
| `[DATA_LINEAGE]` | Specify the data lineage | "[specify value]" |
| `[DATA_COST]` | Specify the data cost | "[specify value]" |
| `[DATA_COMPLIANCE]` | Specify the data compliance | "[specify value]" |
| `[COMPUTE_TIME]` | Specify the compute time | "[specify value]" |
| `[COMPUTE_AUTO]` | Specify the compute auto | "[specify value]" |
| `[COMPUTE_USAGE]` | Specify the compute usage | "[specify value]" |
| `[COMPUTE_SAVE]` | Specify the compute save | "[specify value]" |
| `[COMPUTE_ERROR]` | Specify the compute error | "[specify value]" |
| `[DB_TIME]` | Specify the db time | "[specify value]" |
| `[DB_AUTO]` | Specify the db auto | "[specify value]" |
| `[DB_USAGE]` | Specify the db usage | "[specify value]" |
| `[DB_SAVE]` | Specify the db save | "[specify value]" |
| `[DB_ERROR]` | Specify the db error | "[specify value]" |
| `[QUEUE_TIME]` | Specify the queue time | "[specify value]" |
| `[QUEUE_AUTO]` | Specify the queue auto | "[specify value]" |
| `[QUEUE_USAGE]` | Specify the queue usage | "[specify value]" |
| `[QUEUE_SAVE]` | Specify the queue save | "[specify value]" |
| `[QUEUE_ERROR]` | Specify the queue error | "[specify value]" |
| `[STORAGE_TIME]` | Specify the storage time | "[specify value]" |
| `[STORAGE_AUTO]` | Specify the storage auto | "[specify value]" |
| `[STORAGE_USAGE]` | Specify the storage usage | "[specify value]" |
| `[STORAGE_SAVE]` | Specify the storage save | "[specify value]" |
| `[STORAGE_ERROR]` | Specify the storage error | "[specify value]" |
| `[NET_TIME]` | Specify the net time | "[specify value]" |
| `[NET_AUTO]` | Specify the net auto | "[specify value]" |
| `[NET_USAGE]` | Specify the net usage | "[specify value]" |
| `[NET_SAVE]` | Specify the net save | "[specify value]" |
| `[NET_ERROR]` | Specify the net error | "[specify value]" |
| `[SEC_TIME]` | Specify the sec time | "[specify value]" |
| `[SEC_AUTO]` | Specify the sec auto | "[specify value]" |
| `[SEC_USAGE]` | Specify the sec usage | "[specify value]" |
| `[SEC_SAVE]` | Specify the sec save | "[specify value]" |
| `[SEC_ERROR]` | Specify the sec error | "[specify value]" |
| `[DEPLOY_CURRENT]` | Specify the deploy current | "[specify value]" |
| `[DEPLOY_TARGET]` | Target or intended deploy | "[specify value]" |
| `[DEPLOY_ELITE]` | Specify the deploy elite | "[specify value]" |
| `[DEPLOY_IMP]` | Specify the deploy imp | "[specify value]" |
| `[DEPLOY_ACTION]` | Specify the deploy action | "[specify value]" |
| `[LEAD_CURRENT]` | Specify the lead current | "[specify value]" |
| `[LEAD_TARGET]` | Target or intended lead | "[specify value]" |
| `[LEAD_ELITE]` | Specify the lead elite | "[specify value]" |
| `[LEAD_IMP]` | Specify the lead imp | "[specify value]" |
| `[LEAD_ACTION]` | Specify the lead action | "[specify value]" |
| `[MTTR_CURRENT]` | Specify the mttr current | "[specify value]" |
| `[MTTR_ELITE]` | Specify the mttr elite | "[specify value]" |
| `[MTTR_IMP]` | Specify the mttr imp | "[specify value]" |
| `[MTTR_ACTION]` | Specify the mttr action | "[specify value]" |
| `[FAIL_CURRENT]` | Specify the fail current | "[specify value]" |
| `[FAIL_TARGET]` | Target or intended fail | "[specify value]" |
| `[FAIL_ELITE]` | Specify the fail elite | "[specify value]" |
| `[FAIL_IMP]` | Specify the fail imp | "[specify value]" |
| `[FAIL_ACTION]` | Specify the fail action | "[specify value]" |
| `[SAT_CURRENT]` | Specify the sat current | "[specify value]" |
| `[SAT_TARGET]` | Target or intended sat | "[specify value]" |
| `[SAT_ELITE]` | Specify the sat elite | "[specify value]" |
| `[SAT_IMP]` | Specify the sat imp | "[specify value]" |
| `[SAT_ACTION]` | Specify the sat action | "[specify value]" |
| `[LOAD_CURRENT]` | Specify the load current | "[specify value]" |
| `[LOAD_TARGET]` | Target or intended load | "[specify value]" |
| `[LOAD_ELITE]` | Specify the load elite | "[specify value]" |
| `[LOAD_IMP]` | Specify the load imp | "[specify value]" |
| `[LOAD_ACTION]` | Specify the load action | "[specify value]" |
| `[SERVICE_1]` | Specify the service 1 | "[specify value]" |
| `[DESC_1]` | Specify the desc 1 | "[specify value]" |
| `[SLA_1]` | Specify the sla 1 | "[specify value]" |
| `[DEPS_1]` | Specify the deps 1 | "[specify value]" |
| `[MAINT_1]` | Specify the maint 1 | "[specify value]" |
| `[DOCS_1]` | Specify the docs 1 | "[specify value]" |
| `[SERVICE_2]` | Specify the service 2 | "[specify value]" |
| `[DESC_2]` | Specify the desc 2 | "[specify value]" |
| `[SLA_2]` | Specify the sla 2 | "[specify value]" |
| `[DEPS_2]` | Specify the deps 2 | "[specify value]" |
| `[MAINT_2]` | Specify the maint 2 | "[specify value]" |
| `[DOCS_2]` | Specify the docs 2 | "[specify value]" |
| `[SERVICE_3]` | Specify the service 3 | "[specify value]" |
| `[DESC_3]` | Specify the desc 3 | "[specify value]" |
| `[SLA_3]` | Specify the sla 3 | "[specify value]" |
| `[DEPS_3]` | Specify the deps 3 | "[specify value]" |
| `[MAINT_3]` | Specify the maint 3 | "[specify value]" |
| `[DOCS_3]` | Specify the docs 3 | "[specify value]" |
| `[SERVICE_4]` | Specify the service 4 | "[specify value]" |
| `[DESC_4]` | Specify the desc 4 | "[specify value]" |
| `[SLA_4]` | Specify the sla 4 | "[specify value]" |
| `[DEPS_4]` | Specify the deps 4 | "[specify value]" |
| `[MAINT_4]` | Specify the maint 4 | "[specify value]" |
| `[DOCS_4]` | Specify the docs 4 | "[specify value]" |
| `[SERVICE_5]` | Specify the service 5 | "[specify value]" |
| `[DESC_5]` | Specify the desc 5 | "[specify value]" |
| `[SLA_5]` | Specify the sla 5 | "[specify value]" |
| `[DEPS_5]` | Specify the deps 5 | "[specify value]" |
| `[MAINT_5]` | Specify the maint 5 | "[specify value]" |
| `[DOCS_5]` | Specify the docs 5 | "[specify value]" |
| `[DISCOVERY_CAPABILITY]` | Specify the discovery capability | "[specify value]" |
| `[CONFIG_CAPABILITY]` | Specify the config capability | "[specify value]" |
| `[SECRET_CAPABILITY]` | Specify the secret capability | "[specify value]" |
| `[CERT_CAPABILITY]` | Specify the cert capability | "[specify value]" |
| `[FEATURE_CAPABILITY]` | Specify the feature capability | "[specify value]" |
| `[CANARY_CAPABILITY]` | Specify the canary capability | "[specify value]" |
| `[BLUEGREEN_CAPABILITY]` | Specify the bluegreen capability | "[specify value]" |
| `[ROLLBACK_CAPABILITY]` | Specify the rollback capability | "[specify value]" |
| `[APP_TOOLS]` | Specify the app tools | "[specify value]" |
| `[APP_COVERAGE]` | Specify the app coverage | "[specify value]" |
| `[APP_MTTD]` | Specify the app mttd | "[specify value]" |
| `[APP_NOISE]` | Specify the app noise | "[specify value]" |
| `[APP_COST]` | Specify the app cost | "[specify value]" |
| `[INFRA_TOOLS]` | Specify the infra tools | "[specify value]" |
| `[INFRA_COVERAGE]` | Specify the infra coverage | "[specify value]" |
| `[INFRA_MTTD]` | Specify the infra mttd | "[specify value]" |
| `[INFRA_NOISE]` | Specify the infra noise | "[specify value]" |
| `[INFRA_COST]` | Specify the infra cost | "[specify value]" |
| `[TRACE_TOOLS]` | Specify the trace tools | "[specify value]" |
| `[TRACE_COVERAGE]` | Specify the trace coverage | "[specify value]" |
| `[TRACE_MTTD]` | Specify the trace mttd | "[specify value]" |
| `[TRACE_NOISE]` | Specify the trace noise | "[specify value]" |
| `[TRACE_COST]` | Specify the trace cost | "[specify value]" |
| `[LOG_TOOLS]` | Specify the log tools | "[specify value]" |
| `[LOG_COVERAGE]` | Specify the log coverage | "[specify value]" |
| `[LOG_MTTD]` | Specify the log mttd | "[specify value]" |
| `[LOG_NOISE]` | Specify the log noise | "[specify value]" |
| `[LOG_COST]` | Specify the log cost | "[specify value]" |
| `[SYNTH_TOOLS]` | Specify the synth tools | "[specify value]" |
| `[SYNTH_COVERAGE]` | Specify the synth coverage | "[specify value]" |
| `[SYNTH_MTTD]` | Specify the synth mttd | "[specify value]" |
| `[SYNTH_NOISE]` | Specify the synth noise | "[specify value]" |
| `[SYNTH_COST]` | Specify the synth cost | "[specify value]" |
| `[RUM_TOOLS]` | Specify the rum tools | "[specify value]" |
| `[RUM_COVERAGE]` | Specify the rum coverage | "[specify value]" |
| `[RUM_MTTD]` | Specify the rum mttd | "[specify value]" |
| `[RUM_NOISE]` | Specify the rum noise | "[specify value]" |
| `[RUM_COST]` | Specify the rum cost | "[specify value]" |
| `[SAST_INTEGRATION]` | Specify the sast integration | "[specify value]" |
| `[DAST_AUTOMATION]` | Specify the dast automation | "[specify value]" |
| `[DEP_SCANNING]` | Specify the dep scanning | "[specify value]" |
| `[CONTAINER_SCAN]` | Specify the container scan | "[specify value]" |
| `[IAC_SCANNING]` | Specify the iac scanning | "[specify value]" |
| `[SECRET_DETECT]` | Specify the secret detect | "[specify value]" |
| `[WAF_INTEGRATION]` | Specify the waf integration | "[specify value]" |
| `[RUNTIME_PROTECT]` | Specify the runtime protect | "[specify value]" |
| `[NET_POLICIES]` | Specify the net policies | "[specify value]" |
| `[ACCESS_CONTROLS]` | Specify the access controls | "[specify value]" |
| `[AUDIT_LOGGING]` | Specify the audit logging | "[specify value]" |
| `[COMPLIANCE_REPORT]` | Specify the compliance report | "[specify value]" |
| `[VULN_FOUND]` | Specify the vuln found | "[specify value]" |
| `[PATCH_TIME]` | Specify the patch time | "[specify value]" |
| `[SEC_DEBT]` | Specify the sec debt | "[specify value]" |
| `[COMPLIANCE_SCORE]` | Specify the compliance score | "[specify value]" |
| `[SEC_TRAINING]` | Specify the sec training | "[specify value]" |
| `[COMPUTE_SPEND]` | Specify the compute spend | "[specify value]" |
| `[COMPUTE_OPT]` | Specify the compute opt | "[specify value]" |
| `[COMPUTE_SAVINGS]` | Specify the compute savings | "[specify value]" |
| `[COMPUTE_OWNER]` | Specify the compute owner | "[specify value]" |
| `[COMPUTE_FORECAST]` | Specify the compute forecast | "[specify value]" |
| `[STORAGE_SPEND]` | Specify the storage spend | "[specify value]" |
| `[STORAGE_OPT]` | Specify the storage opt | "[specify value]" |
| `[STORAGE_SAVINGS]` | Specify the storage savings | "[specify value]" |
| `[STORAGE_OWNER]` | Specify the storage owner | "[specify value]" |
| `[STORAGE_FORECAST]` | Specify the storage forecast | "[specify value]" |
| `[NETWORK_SPEND]` | Specify the network spend | "[specify value]" |
| `[NETWORK_OPT]` | Specify the network opt | "[specify value]" |
| `[NETWORK_SAVINGS]` | Specify the network savings | "[specify value]" |
| `[NETWORK_OWNER]` | Specify the network owner | "[specify value]" |
| `[NETWORK_FORECAST]` | Specify the network forecast | "[specify value]" |
| `[DB_SPEND]` | Specify the db spend | "[specify value]" |
| `[DB_OPT]` | Specify the db opt | "[specify value]" |
| `[DB_SAVINGS]` | Specify the db savings | "[specify value]" |
| `[DB_OWNER]` | Specify the db owner | "[specify value]" |
| `[DB_FORECAST]` | Specify the db forecast | "[specify value]" |
| `[OBS_SPEND]` | Specify the obs spend | "[specify value]" |
| `[OBS_OPT]` | Specify the obs opt | "[specify value]" |
| `[OBS_SAVINGS]` | Specify the obs savings | "[specify value]" |
| `[OBS_OWNER]` | Specify the obs owner | "[specify value]" |
| `[OBS_FORECAST]` | Specify the obs forecast | "[specify value]" |
| `[THIRD_SPEND]` | Specify the third spend | "[specify value]" |
| `[THIRD_OPT]` | Specify the third opt | "[specify value]" |
| `[THIRD_SAVINGS]` | Specify the third savings | "[specify value]" |
| `[THIRD_OWNER]` | Specify the third owner | "[specify value]" |
| `[THIRD_FORECAST]` | Specify the third forecast | "[specify value]" |
| `[ONBOARD_PART]` | Specify the onboard part | "[specify value]" |
| `[ONBOARD_FREQ]` | Specify the onboard freq | "[specify value]" |
| `[ONBOARD_SAT]` | Specify the onboard sat | "[specify value]" |
| `[ONBOARD_SKILL]` | Specify the onboard skill | "[specify value]" |
| `[ONBOARD_IMPACT]` | Specify the onboard impact | "[specify value]" |
| `[TRAIN_PART]` | Specify the train part | "[specify value]" |
| `[TRAIN_FREQ]` | Specify the train freq | "[specify value]" |
| `[TRAIN_SAT]` | Specify the train sat | "[specify value]" |
| `[TRAIN_SKILL]` | Specify the train skill | "[specify value]" |
| `[TRAIN_IMPACT]` | Specify the train impact | "[specify value]" |
| `[OFFICE_PART]` | Specify the office part | "[specify value]" |
| `[OFFICE_FREQ]` | Specify the office freq | "[specify value]" |
| `[OFFICE_SAT]` | Specify the office sat | "[specify value]" |
| `[OFFICE_SKILL]` | Specify the office skill | "[specify value]" |
| `[OFFICE_IMPACT]` | Specify the office impact | "[specify value]" |
| `[DOC_PART]` | Specify the doc part | "[specify value]" |
| `[DOC_SAT]` | Specify the doc sat | "[specify value]" |
| `[DOC_SKILL]` | Specify the doc skill | "[specify value]" |
| `[DOC_IMPACT]` | Specify the doc impact | "[specify value]" |
| `[TALK_PART]` | Specify the talk part | "[specify value]" |
| `[TALK_FREQ]` | Specify the talk freq | "[specify value]" |
| `[TALK_SAT]` | Specify the talk sat | "[specify value]" |
| `[TALK_SKILL]` | Specify the talk skill | "[specify value]" |
| `[TALK_IMPACT]` | Specify the talk impact | "[specify value]" |
| `[HACK_PART]` | Specify the hack part | "[specify value]" |
| `[HACK_FREQ]` | Specify the hack freq | "[specify value]" |
| `[HACK_SAT]` | Specify the hack sat | "[specify value]" |
| `[HACK_SKILL]` | Specify the hack skill | "[specify value]" |
| `[HACK_IMPACT]` | Specify the hack impact | "[specify value]" |
| `[MESH_TIME]` | Specify the mesh time | "[specify value]" |
| `[MESH_INVEST]` | Specify the mesh invest | "[specify value]" |
| `[MESH_VALUE]` | Specify the mesh value | "[specify value]" |
| `[MESH_RISK]` | Specify the mesh risk | "[specify value]" |
| `[MESH_DEPS]` | Specify the mesh deps | "[specify value]" |
| `[GITOPS_TIME]` | Specify the gitops time | "[specify value]" |
| `[GITOPS_INVEST]` | Specify the gitops invest | "[specify value]" |
| `[GITOPS_VALUE]` | Specify the gitops value | "[specify value]" |
| `[GITOPS_RISK]` | Specify the gitops risk | "[specify value]" |
| `[GITOPS_DEPS]` | Specify the gitops deps | "[specify value]" |
| `[ML_TIME]` | Specify the ml time | "[specify value]" |
| `[ML_INVEST]` | Specify the ml invest | "[specify value]" |
| `[ML_VALUE]` | Specify the ml value | "[specify value]" |
| `[ML_RISK]` | Specify the ml risk | "[specify value]" |
| `[ML_DEPS]` | Specify the ml deps | "[specify value]" |
| `[EDGE_TIME]` | Specify the edge time | "[specify value]" |
| `[EDGE_INVEST]` | Specify the edge invest | "[specify value]" |
| `[EDGE_VALUE]` | Specify the edge value | "[specify value]" |
| `[EDGE_RISK]` | Specify the edge risk | "[specify value]" |
| `[EDGE_DEPS]` | Specify the edge deps | "[specify value]" |
| `[API_TIME]` | Specify the api time | "[specify value]" |
| `[API_INVEST]` | Specify the api invest | "[specify value]" |
| `[API_VALUE]` | Specify the api value | "[specify value]" |
| `[API_RISK]` | Specify the api risk | "[specify value]" |
| `[API_DEPS]` | Specify the api deps | "[specify value]" |

### 3. Self-Service Infrastructure

| **Service Type** | **Provisioning Time** | **Automation Level** | **Usage/Month** | **Cost Savings** | **Error Rate** |
|-----------------|---------------------|---------------------|----------------|-----------------|---------------|
| Compute Resources | [COMPUTE_TIME] | [COMPUTE_AUTO]% | [COMPUTE_USAGE] | $[COMPUTE_SAVE] | [COMPUTE_ERROR]% |
| Databases | [DB_TIME] | [DB_AUTO]% | [DB_USAGE] | $[DB_SAVE] | [DB_ERROR]% |
| Message Queues | [QUEUE_TIME] | [QUEUE_AUTO]% | [QUEUE_USAGE] | $[QUEUE_SAVE] | [QUEUE_ERROR]% |
| Storage | [STORAGE_TIME] | [STORAGE_AUTO]% | [STORAGE_USAGE] | $[STORAGE_SAVE] | [STORAGE_ERROR]% |
| Networking | [NET_TIME] | [NET_AUTO]% | [NET_USAGE] | $[NET_SAVE] | [NET_ERROR]% |
| Security Services | [SEC_TIME] | [SEC_AUTO]% | [SEC_USAGE] | $[SEC_SAVE] | [SEC_ERROR]% |

### 4. Developer Productivity Metrics

**DORA Metrics & Beyond:**
| **Metric** | **Current** | **Target** | **Industry Elite** | **Improvement** | **Action Plan** |
|-----------|------------|----------|------------------|----------------|---------------|
| Deployment Frequency | [DEPLOY_CURRENT] | [DEPLOY_TARGET] | [DEPLOY_ELITE] | [DEPLOY_IMP]% | [DEPLOY_ACTION] |
| Lead Time for Changes | [LEAD_CURRENT] | [LEAD_TARGET] | [LEAD_ELITE] | [LEAD_IMP]% | [LEAD_ACTION] |
| MTTR | [MTTR_CURRENT] | [MTTR_TARGET] | [MTTR_ELITE] | [MTTR_IMP]% | [MTTR_ACTION] |
| Change Failure Rate | [FAIL_CURRENT]% | [FAIL_TARGET]% | [FAIL_ELITE]% | [FAIL_IMP]% | [FAIL_ACTION] |
| Developer Satisfaction | [SAT_CURRENT]/10 | [SAT_TARGET]/10 | [SAT_ELITE]/10 | [SAT_IMP]% | [SAT_ACTION] |
| Cognitive Load | [LOAD_CURRENT] | [LOAD_TARGET] | [LOAD_ELITE] | [LOAD_IMP]% | [LOAD_ACTION] |

### 5. Platform Services Catalog

```
Core Services:
Service | Description | SLA | Dependencies | Maintainer | Documentation
--------|------------|-----|--------------|-----------|---------------
[SERVICE_1] | [DESC_1] | [SLA_1] | [DEPS_1] | [MAINT_1] | [DOCS_1]
[SERVICE_2] | [DESC_2] | [SLA_2] | [DEPS_2] | [MAINT_2] | [DOCS_2]
[SERVICE_3] | [DESC_3] | [SLA_3] | [DEPS_3] | [MAINT_3] | [DOCS_3]
[SERVICE_4] | [DESC_4] | [SLA_4] | [DEPS_4] | [MAINT_4] | [DOCS_4]
[SERVICE_5] | [DESC_5] | [SLA_5] | [DEPS_5] | [MAINT_5] | [DOCS_5]

Platform Capabilities:
- Service Discovery: [DISCOVERY_CAPABILITY]
- Configuration Management: [CONFIG_CAPABILITY]
- Secret Management: [SECRET_CAPABILITY]
- Certificate Management: [CERT_CAPABILITY]
- Feature Flags: [FEATURE_CAPABILITY]
- Canary Deployments: [CANARY_CAPABILITY]
- Blue-Green Deployments: [BLUEGREEN_CAPABILITY]
- Rollback Automation: [ROLLBACK_CAPABILITY]
```

### 6. Observability & Monitoring Platform

| **Observability Pillar** | **Tools** | **Coverage** | **MTTD** | **Alert Noise** | **Cost/Month** |
|-------------------------|----------|-------------|----------|----------------|---------------|
| Application Metrics | [APP_TOOLS] | [APP_COVERAGE]% | [APP_MTTD] min | [APP_NOISE]% | $[APP_COST] |
| Infrastructure Metrics | [INFRA_TOOLS] | [INFRA_COVERAGE]% | [INFRA_MTTD] min | [INFRA_NOISE]% | $[INFRA_COST] |
| Distributed Tracing | [TRACE_TOOLS] | [TRACE_COVERAGE]% | [TRACE_MTTD] min | [TRACE_NOISE]% | $[TRACE_COST] |
| Log Aggregation | [LOG_TOOLS] | [LOG_COVERAGE]% | [LOG_MTTD] min | [LOG_NOISE]% | $[LOG_COST] |
| Synthetic Monitoring | [SYNTH_TOOLS] | [SYNTH_COVERAGE]% | [SYNTH_MTTD] min | [SYNTH_NOISE]% | $[SYNTH_COST] |
| Real User Monitoring | [RUM_TOOLS] | [RUM_COVERAGE]% | [RUM_MTTD] min | [RUM_NOISE]% | $[RUM_COST] |

### 7. Security & Compliance Platform

**Security Integration:**
```
Shift-Left Security:
- SAST Integration: [SAST_INTEGRATION]
- DAST Automation: [DAST_AUTOMATION]
- Dependency Scanning: [DEP_SCANNING]
- Container Scanning: [CONTAINER_SCAN]
- IaC Scanning: [IAC_SCANNING]
- Secret Detection: [SECRET_DETECT]

Runtime Security:
- WAF Integration: [WAF_INTEGRATION]
- Runtime Protection: [RUNTIME_PROTECT]
- Network Policies: [NET_POLICIES]
- Access Controls: [ACCESS_CONTROLS]
- Audit Logging: [AUDIT_LOGGING]
- Compliance Reporting: [COMPLIANCE_REPORT]

### Security Metrics
- Vulnerabilities Found: [VULN_FOUND]/month
- Mean Time to Patch: [PATCH_TIME] days
- Security Debt: [SEC_DEBT] issues
- Compliance Score: [COMPLIANCE_SCORE]%
- Security Training: [SEC_TRAINING]% completed
```

### 8. Cost Management & FinOps

| **Cost Category** | **Monthly Spend** | **Optimization** | **Savings** | **Ownership** | **Forecast** |
|------------------|------------------|-----------------|------------|--------------|-------------|
| Compute | $[COMPUTE_SPEND] | [COMPUTE_OPT] | $[COMPUTE_SAVINGS] | [COMPUTE_OWNER] | $[COMPUTE_FORECAST] |
| Storage | $[STORAGE_SPEND] | [STORAGE_OPT] | $[STORAGE_SAVINGS] | [STORAGE_OWNER] | $[STORAGE_FORECAST] |
| Network | $[NETWORK_SPEND] | [NETWORK_OPT] | $[NETWORK_SAVINGS] | [NETWORK_OWNER] | $[NETWORK_FORECAST] |
| Databases | $[DB_SPEND] | [DB_OPT] | $[DB_SAVINGS] | [DB_OWNER] | $[DB_FORECAST] |
| Observability | $[OBS_SPEND] | [OBS_OPT] | $[OBS_SAVINGS] | [OBS_OWNER] | $[OBS_FORECAST] |
| Third-party Services | $[THIRD_SPEND] | [THIRD_OPT] | $[THIRD_SAVINGS] | [THIRD_OWNER] | $[THIRD_FORECAST] |

### 9. Platform Adoption & Education

**Developer Enablement:**
| **Program** | **Participants** | **Frequency** | **Satisfaction** | **Skill Improvement** | **Business Impact** |
|------------|-----------------|--------------|-----------------|---------------------|-------------------|
| Onboarding Program | [ONBOARD_PART] | [ONBOARD_FREQ] | [ONBOARD_SAT]/10 | [ONBOARD_SKILL]% | [ONBOARD_IMPACT] |
| Platform Training | [TRAIN_PART] | [TRAIN_FREQ] | [TRAIN_SAT]/10 | [TRAIN_SKILL]% | [TRAIN_IMPACT] |
| Office Hours | [OFFICE_PART] | [OFFICE_FREQ] | [OFFICE_SAT]/10 | [OFFICE_SKILL]% | [OFFICE_IMPACT] |
| Documentation | [DOC_PART] | Continuous | [DOC_SAT]/10 | [DOC_SKILL]% | [DOC_IMPACT] |
| Internal Tech Talks | [TALK_PART] | [TALK_FREQ] | [TALK_SAT]/10 | [TALK_SKILL]% | [TALK_IMPACT] |
| Hackathons | [HACK_PART] | [HACK_FREQ] | [HACK_SAT]/10 | [HACK_SKILL]% | [HACK_IMPACT] |

### 10. Platform Roadmap & Evolution

**Strategic Initiatives:**
| **Initiative** | **Timeline** | **Investment** | **Expected Value** | **Risk Level** | **Dependencies** |
|---------------|-------------|---------------|-------------------|---------------|------------------|
| Service Mesh Adoption | [MESH_TIME] | $[MESH_INVEST] | [MESH_VALUE] | [MESH_RISK] | [MESH_DEPS] |
| GitOps Implementation | [GITOPS_TIME] | $[GITOPS_INVEST] | [GITOPS_VALUE] | [GITOPS_RISK] | [GITOPS_DEPS] |
| AI/ML Platform | [ML_TIME] | $[ML_INVEST] | [ML_VALUE] | [ML_RISK] | [ML_DEPS] |
| Edge Computing | [EDGE_TIME] | $[EDGE_INVEST] | [EDGE_VALUE] | [EDGE_RISK] | [EDGE_DEPS] |
| Platform APIs | [API_TIME] | $[API_INVEST] | [API_VALUE] | [API_RISK] | [API_DEPS] |

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: Enterprise Platform Team
```
Organization: Fortune 500 Tech Company
Developers: 5000+
Teams: 200+
Services: 1500 microservices
Platform: Kubernetes-based, multi-cloud
Focus: Developer productivity, self-service
Results: 70% reduction in deployment time
```

### Example 2: Scale-up SaaS Platform
```
Organization: Fast-growing SaaS
Developers: 200
Teams: 25
Platform: AWS-native, serverless-first
Golden Paths: 5 standardized patterns
Focus: Rapid scaling, cost optimization
Results: 10x growth with 2x platform team
```

### Example 3: Digital Transformation Platform
```
Organization: Traditional Enterprise
Developers: 500 (growing)
Migration: Monolith to microservices
Platform: Hybrid cloud, progressive adoption
Focus: Culture change, skills development
Timeline: 3-year transformation
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Platform Engineering & Developer Experience Framework)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/DevOps & Platform](../../technology/DevOps & Platform/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive framework for building and managing internal developer platforms, self-service infrastructure, golden paths, developer productivity tools, and platform-as-a-product approaches.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Customization Options

### 1. Organization Size
- Startup (<50 developers)
- Scale-up (50-200)
- Mid-size (200-1000)
- Enterprise (1000-5000)
- Large Enterprise (5000+)

### 2. Platform Maturity
- Initial (ad-hoc tools)
- Developing (some automation)
- Defined (standardized)
- Managed (measured)
- Optimized (continuous improvement)

### 3. Technology Stack
- Cloud-native
- Hybrid cloud
- On-premises
- Multi-cloud
- Edge-focused

### 4. Development Model
- Microservices
- Serverless
- Monolithic
- Event-driven
- Mixed architecture

### 5. Industry Focus
- Technology/Software
- Financial Services
- Healthcare
- Retail/E-commerce
- Government/Public Sector