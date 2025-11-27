```markdown
---
category: ai-ml-applications
last_updated: 2025-11-25
title: AI Readiness Assessment
tags:
- ai-readiness
- ai-maturity
- capability-assessment
- ai-adoption
use_cases:
- Evaluating organizational readiness for AI adoption
- Identifying gaps and investment priorities for AI capability building
- Benchmarking AI maturity against industry standards
- Creating capability development roadmaps
related_templates:
- ai-ml-applications/AI-Strategy/ai-strategy-roadmap.md
- ai-ml-applications/AI-Strategy/ai-use-case-identification.md
- ai-ml-applications/AI-Product-Development/ai-data-strategy.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: ai-readiness-assessment
---

# AI Readiness Assessment

## Purpose
Comprehensively assess an organization's readiness to adopt and scale AI across six dimensions: Data, Technology, Talent, Process, Culture, and Governance. This framework identifies gaps, prioritizes investments, and creates a capability development roadmap.

## 🚀 Quick Assessment Prompt

> Assess **AI readiness** for **[ORGANIZATION]** planning to implement **[AI USE CASES]**. Evaluate across: (1) **Data readiness**—what's the data quality, availability, accessibility, and governance maturity? Are there data silos or integration challenges? (2) **Technical infrastructure**—what compute, ML platforms, and MLOps capabilities exist? Cloud vs on-premise? (3) **Talent & skills**—what AI/ML expertise exists? What gaps in data science, ML engineering, and AI product management? (4) **Organizational readiness**—is there executive sponsorship, change appetite, and cross-functional collaboration? What's the AI literacy level? Provide a maturity scorecard (1-5 per dimension), gap analysis, prioritized recommendations, and a 12-month capability building plan.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid AI readiness evaluation.

---

## Quick Start

### Minimal Example
```
AI READINESS ASSESSMENT: Mid-Size Insurance Company

DIMENSION SCORES (1-5 scale):
┌─────────────────┬───────┬─────────────────────────────┐
│ Dimension       │ Score │ Key Finding                 │
├─────────────────┼───────┼─────────────────────────────┤
│ Data            │  2.5  │ Good claims data, siloed    │
│ Technology      │  2.0  │ Legacy infrastructure       │
│ Talent          │  1.5  │ 2 data analysts, no ML eng  │
│ Process         │  2.0  │ No MLOps, ad-hoc projects   │
│ Culture         │  3.0  │ Exec support, some resistance│
│ Governance      │  2.5  │ Basic data governance only  │
├─────────────────┼───────┼─────────────────────────────┤
│ OVERALL         │  2.3  │ DEVELOPING stage            │
└─────────────────┴───────┴─────────────────────────────┘

TOP PRIORITIES:
1. Data integration - Break down silos between claims/policy/customer
2. Cloud ML platform - Migrate from on-prem to cloud-native
3. Talent acquisition - Hire 2 ML engineers + 1 AI PM

INVESTMENT REQUIRED: $2.5M over 18 months
READINESS FOR TARGET USE CASES: Medium (claims automation feasible,
   fraud detection requires data work first)
```

### When to Use This
- Starting an AI transformation and need to understand current state
- Evaluating feasibility of specific AI use cases
- Building business case for AI capability investments
- Benchmarking against industry or competitors
- Annual AI program health check

### Basic 6-Step Workflow
1. **Scope** - Define assessment scope and target AI ambitions
2. **Gather** - Collect data through interviews, surveys, and analysis
3. **Score** - Rate each dimension using maturity rubrics
4. **Analyze** - Identify gaps between current and required state
5. **Prioritize** - Rank investments by impact and urgency
6. **Plan** - Create capability development roadmap

---

## Template

```markdown
# AI Readiness Assessment: [ORGANIZATION_NAME]

## Assessment Overview

| Field | Value |
|-------|-------|
| Organization | [NAME] |
| Industry | [INDUSTRY] |
| Revenue/Size | [REVENUE] / [EMPLOYEES] |
| Assessment Date | [DATE] |
| Assessment Team | [NAMES] |
| Target AI Ambition | [DESCRIPTION] |

---

## 1. Data Readiness

### 1.1 Data Availability
| Data Domain | Exists | Accessible | Volume | Quality | Score |
|-------------|--------|------------|--------|---------|-------|
| Customer | [Y/N] | [Y/N] | [VOLUME] | [H/M/L] | [1-5] |
| Transaction | [Y/N] | [Y/N] | [VOLUME] | [H/M/L] | [1-5] |
| Product | [Y/N] | [Y/N] | [VOLUME] | [H/M/L] | [1-5] |
| Operational | [Y/N] | [Y/N] | [VOLUME] | [H/M/L] | [1-5] |
| External | [Y/N] | [Y/N] | [VOLUME] | [H/M/L] | [1-5] |

### 1.2 Data Quality
| Factor | Assessment | Score |
|--------|------------|-------|
| Completeness | [DESCRIPTION] | [1-5] |
| Accuracy | [DESCRIPTION] | [1-5] |
| Consistency | [DESCRIPTION] | [1-5] |
| Timeliness | [DESCRIPTION] | [1-5] |
| Uniqueness | [DESCRIPTION] | [1-5] |

### 1.3 Data Integration
| Factor | Assessment | Score |
|--------|------------|-------|
| Data silos | [# of silos, integration status] | [1-5] |
| Master data management | [DESCRIPTION] | [1-5] |
| Data catalog | [EXISTS/PARTIAL/NONE] | [1-5] |
| API accessibility | [DESCRIPTION] | [1-5] |

### 1.4 Data for AI
| Factor | Assessment | Score |
|--------|------------|-------|
| Feature engineering capability | [DESCRIPTION] | [1-5] |
| Labeled training data | [AVAILABILITY] | [1-5] |
| Real-time data access | [DESCRIPTION] | [1-5] |
| Data versioning | [DESCRIPTION] | [1-5] |

**Data Readiness Score:** [AVERAGE] / 5
**Key Gaps:** [LIST]

---

## 2. Technology Readiness

### 2.1 Infrastructure
| Component | Current State | Score |
|-----------|---------------|-------|
| Cloud adoption | [ON-PREM/HYBRID/CLOUD] | [1-5] |
| Compute capacity | [DESCRIPTION] | [1-5] |
| GPU availability | [DESCRIPTION] | [1-5] |
| Storage | [DESCRIPTION] | [1-5] |
| Network | [DESCRIPTION] | [1-5] |

### 2.2 ML/AI Platform
| Component | Current State | Score |
|-----------|---------------|-------|
| ML platform | [TOOL/NONE] | [1-5] |
| Experiment tracking | [TOOL/NONE] | [1-5] |
| Model registry | [TOOL/NONE] | [1-5] |
| Feature store | [TOOL/NONE] | [1-5] |
| Model serving | [TOOL/NONE] | [1-5] |

### 2.3 MLOps Maturity
| Capability | Current State | Score |
|------------|---------------|-------|
| CI/CD for ML | [DESCRIPTION] | [1-5] |
| Model monitoring | [DESCRIPTION] | [1-5] |
| Automated retraining | [DESCRIPTION] | [1-5] |
| A/B testing | [DESCRIPTION] | [1-5] |
| Drift detection | [DESCRIPTION] | [1-5] |

### 2.4 Integration Capabilities
| Capability | Current State | Score |
|------------|---------------|-------|
| API infrastructure | [DESCRIPTION] | [1-5] |
| Event streaming | [DESCRIPTION] | [1-5] |
| ETL/ELT pipelines | [DESCRIPTION] | [1-5] |
| Application integration | [DESCRIPTION] | [1-5] |

**Technology Readiness Score:** [AVERAGE] / 5
**Key Gaps:** [LIST]

---

## 3. Talent Readiness

### 3.1 Current AI/ML Team
| Role | Current Count | Required | Gap |
|------|---------------|----------|-----|
| Data Scientists | [#] | [#] | [+/-#] |
| ML Engineers | [#] | [#] | [+/-#] |
| Data Engineers | [#] | [#] | [+/-#] |
| AI Product Managers | [#] | [#] | [+/-#] |
| AI/ML Architects | [#] | [#] | [+/-#] |
| AI Ethics/Governance | [#] | [#] | [+/-#] |

### 3.2 Skill Assessment
| Skill Area | Current Level | Score |
|------------|---------------|-------|
| Classical ML | [NONE/BASIC/PROFICIENT/EXPERT] | [1-5] |
| Deep Learning | [NONE/BASIC/PROFICIENT/EXPERT] | [1-5] |
| NLP/LLM | [NONE/BASIC/PROFICIENT/EXPERT] | [1-5] |
| Computer Vision | [NONE/BASIC/PROFICIENT/EXPERT] | [1-5] |
| MLOps | [NONE/BASIC/PROFICIENT/EXPERT] | [1-5] |
| GenAI/Prompting | [NONE/BASIC/PROFICIENT/EXPERT] | [1-5] |

### 3.3 Talent Strategy
| Factor | Assessment | Score |
|--------|------------|-------|
| Ability to hire | [EASY/MODERATE/DIFFICULT] | [1-5] |
| Retention | [DESCRIPTION] | [1-5] |
| Upskilling programs | [DESCRIPTION] | [1-5] |
| Partner/vendor access | [DESCRIPTION] | [1-5] |
| University partnerships | [DESCRIPTION] | [1-5] |

### 3.4 Business AI Literacy
| Stakeholder Group | AI Literacy Level | Score |
|-------------------|-------------------|-------|
| Executive team | [LOW/MEDIUM/HIGH] | [1-5] |
| Middle management | [LOW/MEDIUM/HIGH] | [1-5] |
| Front-line staff | [LOW/MEDIUM/HIGH] | [1-5] |
| IT team | [LOW/MEDIUM/HIGH] | [1-5] |

**Talent Readiness Score:** [AVERAGE] / 5
**Key Gaps:** [LIST]

---

## 4. Process Readiness

### 4.1 AI Development Process
| Factor | Current State | Score |
|--------|---------------|-------|
| AI project methodology | [AD-HOC/BASIC/MATURE] | [1-5] |
| Requirements gathering | [DESCRIPTION] | [1-5] |
| Model development lifecycle | [DESCRIPTION] | [1-5] |
| Testing & validation | [DESCRIPTION] | [1-5] |
| Deployment process | [DESCRIPTION] | [1-5] |

### 4.2 Business Process Integration
| Factor | Current State | Score |
|--------|---------------|-------|
| Process documentation | [DESCRIPTION] | [1-5] |
| Process automation level | [DESCRIPTION] | [1-5] |
| Human-AI workflow design | [DESCRIPTION] | [1-5] |
| Decision integration points | [DESCRIPTION] | [1-5] |

### 4.3 Operational Excellence
| Factor | Current State | Score |
|--------|---------------|-------|
| Model performance monitoring | [DESCRIPTION] | [1-5] |
| Incident response | [DESCRIPTION] | [1-5] |
| Feedback loops | [DESCRIPTION] | [1-5] |
| Continuous improvement | [DESCRIPTION] | [1-5] |

**Process Readiness Score:** [AVERAGE] / 5
**Key Gaps:** [LIST]

---

## 5. Culture Readiness

### 5.1 Leadership Commitment
| Factor | Assessment | Score |
|--------|------------|-------|
| Executive sponsorship | [NONE/LIMITED/STRONG] | [1-5] |
| AI vision clarity | [DESCRIPTION] | [1-5] |
| Resource commitment | [DESCRIPTION] | [1-5] |
| Long-term patience | [DESCRIPTION] | [1-5] |

### 5.2 Organizational Appetite
| Factor | Assessment | Score |
|--------|------------|-------|
| Innovation culture | [RISK-AVERSE/MODERATE/INNOVATIVE] | [1-5] |
| Change readiness | [DESCRIPTION] | [1-5] |
| Experimentation tolerance | [DESCRIPTION] | [1-5] |
| Failure acceptance | [DESCRIPTION] | [1-5] |

### 5.3 Collaboration
| Factor | Assessment | Score |
|--------|------------|-------|
| Cross-functional collaboration | [DESCRIPTION] | [1-5] |
| Business-IT alignment | [DESCRIPTION] | [1-5] |
| Data sharing culture | [DESCRIPTION] | [1-5] |
| External partnerships | [DESCRIPTION] | [1-5] |

### 5.4 Trust & Adoption
| Factor | Assessment | Score |
|--------|------------|-------|
| AI trust level | [SKEPTICAL/NEUTRAL/TRUSTING] | [1-5] |
| Willingness to adopt | [DESCRIPTION] | [1-5] |
| Job displacement concerns | [HIGH/MEDIUM/LOW concern] | [1-5] |
| AI augmentation mindset | [DESCRIPTION] | [1-5] |

**Culture Readiness Score:** [AVERAGE] / 5
**Key Gaps:** [LIST]

---

## 6. Governance Readiness

### 6.1 AI Ethics & Principles
| Factor | Current State | Score |
|--------|---------------|-------|
| AI ethics framework | [NONE/DRAFT/IMPLEMENTED] | [1-5] |
| Responsible AI principles | [DESCRIPTION] | [1-5] |
| Bias monitoring | [DESCRIPTION] | [1-5] |
| Fairness standards | [DESCRIPTION] | [1-5] |

### 6.2 Risk Management
| Factor | Current State | Score |
|--------|---------------|-------|
| AI risk framework | [NONE/BASIC/COMPREHENSIVE] | [1-5] |
| Model risk management | [DESCRIPTION] | [1-5] |
| Explainability requirements | [DESCRIPTION] | [1-5] |
| Audit capabilities | [DESCRIPTION] | [1-5] |

### 6.3 Regulatory Compliance
| Factor | Current State | Score |
|--------|---------------|-------|
| Regulatory awareness | [DESCRIPTION] | [1-5] |
| EU AI Act readiness | [NOT STARTED/IN PROGRESS/READY] | [1-5] |
| Industry-specific regs | [DESCRIPTION] | [1-5] |
| Privacy compliance | [DESCRIPTION] | [1-5] |

### 6.4 Governance Structure
| Factor | Current State | Score |
|--------|---------------|-------|
| AI governance body | [NONE/INFORMAL/FORMAL] | [1-5] |
| Decision rights | [DESCRIPTION] | [1-5] |
| Policy documentation | [DESCRIPTION] | [1-5] |
| Review processes | [DESCRIPTION] | [1-5] |

**Governance Readiness Score:** [AVERAGE] / 5
**Key Gaps:** [LIST]

---

## 7. Overall Assessment

### Maturity Scorecard
```
DIMENSION          SCORE    MATURITY LEVEL
─────────────────────────────────────────────
Data               [X.X]    [LEVEL]
Technology         [X.X]    [LEVEL]
Talent             [X.X]    [LEVEL]
Process            [X.X]    [LEVEL]
Culture            [X.X]    [LEVEL]
Governance         [X.X]    [LEVEL]
─────────────────────────────────────────────
OVERALL            [X.X]    [LEVEL]

Maturity Levels:
1.0-1.9: Initial (Ad-hoc, minimal capabilities)
2.0-2.9: Developing (Some capabilities, significant gaps)
3.0-3.9: Defined (Solid foundation, scaling challenges)
4.0-4.9: Managed (Mature capabilities, optimization focus)
5.0: Optimized (Industry-leading, continuous innovation)
```

### Visual Assessment
```
        Data         
          5          
          4          
          3     ●    
          2          
          1          
Culture ─────────────── Technology
          ●         ●
          
          
          ●         ●
Governance ────────── Talent
          
          ●          
        Process      

● = Current Score
```

### Readiness for Target Use Cases
| Use Case | Data | Tech | Talent | Process | Culture | Gov | Ready? |
|----------|------|------|--------|---------|---------|-----|--------|
| [UC_1] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [Y/N] |
| [UC_2] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [Y/N] |
| [UC_3] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [✓/△/✗] | [Y/N] |

✓ = Ready  △ = Partially Ready  ✗ = Not Ready

---

## 8. Gap Analysis & Recommendations

### Priority Gaps
| Rank | Dimension | Gap | Impact | Urgency | Investment |
|------|-----------|-----|--------|---------|------------|
| 1 | [DIM] | [GAP] | [H/M/L] | [H/M/L] | $[AMOUNT] |
| 2 | [DIM] | [GAP] | [H/M/L] | [H/M/L] | $[AMOUNT] |
| 3 | [DIM] | [GAP] | [H/M/L] | [H/M/L] | $[AMOUNT] |
| 4 | [DIM] | [GAP] | [H/M/L] | [H/M/L] | $[AMOUNT] |
| 5 | [DIM] | [GAP] | [H/M/L] | [H/M/L] | $[AMOUNT] |

### Recommendations by Dimension

**Data:**
1. [RECOMMENDATION_1]
2. [RECOMMENDATION_2]

**Technology:**
1. [RECOMMENDATION_1]
2. [RECOMMENDATION_2]

**Talent:**
1. [RECOMMENDATION_1]
2. [RECOMMENDATION_2]

**Process:**
1. [RECOMMENDATION_1]
2. [RECOMMENDATION_2]

**Culture:**
1. [RECOMMENDATION_1]
2. [RECOMMENDATION_2]

**Governance:**
1. [RECOMMENDATION_1]
2. [RECOMMENDATION_2]

---

## 9. Capability Development Roadmap

### 12-Month Plan
| Month | Data | Technology | Talent | Process | Culture | Governance |
|-------|------|------------|--------|---------|---------|------------|
| 1-3 | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] |
| 4-6 | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] |
| 7-9 | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] |
| 10-12 | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] | [ACTION] |

### Investment Summary
| Category | Q1 | Q2 | Q3 | Q4 | Total |
|----------|-----|-----|-----|-----|-------|
| Data | $[AMT] | $[AMT] | $[AMT] | $[AMT] | $[TOTAL] |
| Technology | $[AMT] | $[AMT] | $[AMT] | $[AMT] | $[TOTAL] |
| Talent | $[AMT] | $[AMT] | $[AMT] | $[AMT] | $[TOTAL] |
| Process/Gov | $[AMT] | $[AMT] | $[AMT] | $[AMT] | $[TOTAL] |
| **TOTAL** | **$[AMT]** | **$[AMT]** | **$[AMT]** | **$[AMT]** | **$[TOTAL]** |

### Success Metrics
| Dimension | Current Score | 6-Month Target | 12-Month Target |
|-----------|---------------|----------------|-----------------|
| Data | [X.X] | [X.X] | [X.X] |
| Technology | [X.X] | [X.X] | [X.X] |
| Talent | [X.X] | [X.X] | [X.X] |
| Process | [X.X] | [X.X] | [X.X] |
| Culture | [X.X] | [X.X] | [X.X] |
| Governance | [X.X] | [X.X] | [X.X] |
| **Overall** | **[X.X]** | **[X.X]** | **[X.X]** |
```

---

## Maturity Rubrics

### Data Maturity Levels
| Level | Score | Characteristics |
|-------|-------|-----------------|
| Initial | 1 | Data scattered across silos, poor quality, no governance |
| Developing | 2 | Some data consolidated, basic quality controls, limited access |
| Defined | 3 | Enterprise data platform, quality monitoring, catalog exists |
| Managed | 4 | Integrated data, automated quality, feature engineering capability |
| Optimized | 5 | Real-time data, AI-ready features, self-service analytics |

### Technology Maturity Levels
| Level | Score | Characteristics |
|-------|-------|-----------------|
| Initial | 1 | No ML infrastructure, ad-hoc tools, manual processes |
| Developing | 2 | Basic cloud, some ML tools, limited automation |
| Defined | 3 | ML platform deployed, experiment tracking, basic MLOps |
| Managed | 4 | Full MLOps pipeline, model monitoring, automated deployment |
| Optimized | 5 | Advanced ML platform, real-time serving, continuous learning |

### Talent Maturity Levels
| Level | Score | Characteristics |
|-------|-------|-----------------|
| Initial | 1 | No dedicated AI talent, reliance on external consultants |
| Developing | 2 | 1-2 data scientists, limited ML engineering, no AI PM |
| Defined | 3 | Small AI team, key skills covered, upskilling in progress |
| Managed | 4 | Full AI organization, specialized roles, talent pipeline |
| Optimized | 5 | Industry-leading team, research capability, AI academy |

---

## Usage Examples

### Example 1: Healthcare Provider
```
AI READINESS: Regional Hospital Network

OVERALL SCORE: 2.4 (Developing)

DIMENSION BREAKDOWN:
- Data: 3.0 (Good EHR data, but siloed across facilities)
- Technology: 2.0 (Legacy on-prem, no ML platform)
- Talent: 1.5 (2 analysts, no data scientists)
- Process: 2.5 (Some analytics processes, no ML lifecycle)
- Culture: 3.0 (Strong clinical leadership support)
- Governance: 2.5 (HIPAA compliance, no AI-specific governance)

KEY GAPS:
1. No ML engineering capability
2. Lack of cloud ML infrastructure
3. Data integration across facilities
4. AI governance framework needed for clinical AI

RECOMMENDATIONS:
1. IMMEDIATE: Hire ML lead, establish cloud ML pilot
2. 6-MONTH: Deploy unified data platform, start AI governance
3. 12-MONTH: Scale team, operationalize first clinical AI use case

INVESTMENT REQUIRED: $3.2M over 12 months
```

### Example 2: E-commerce Company
```
AI READINESS: D2C E-commerce ($200M Revenue)

OVERALL SCORE: 3.2 (Defined)

DIMENSION BREAKDOWN:
- Data: 4.0 (Rich customer data, good e-commerce analytics)
- Technology: 3.5 (Cloud-native, some ML tools)
- Talent: 2.5 (3 data scientists, need ML engineers)
- Process: 3.0 (Basic ML workflow, manual deployment)
- Culture: 3.5 (Data-driven culture, experimentation mindset)
- Governance: 2.5 (Basic data governance, no AI ethics)

READY FOR:
✓ Personalization and recommendations
✓ Demand forecasting
△ Dynamic pricing (needs better governance)
✗ Customer service AI (needs more labeled data)

PRIORITY ACTIONS:
1. Hire 2 ML engineers for production deployment
2. Implement MLOps pipeline for continuous deployment
3. Establish AI governance for pricing fairness
```

---

## Best Practices

1. **Be Honest in Assessment** - Overestimating readiness leads to failed projects. Better to know your gaps.

2. **Involve Multiple Stakeholders** - Get input from IT, business, and leadership for balanced view.

3. **Benchmark Appropriately** - Compare to industry peers, not to AI-native companies.

4. **Prioritize Ruthlessly** - You can't fix everything at once. Focus on critical path to target use cases.

5. **Reassess Regularly** - AI readiness changes. Conduct annual reassessment.

6. **Connect to Use Cases** - Always tie readiness to specific AI initiatives, not abstract maturity.

---

## Common Pitfalls

❌ **Assuming Data is Ready** - Most common failure. Always assess data for specific use cases.
✅ Instead: Conduct detailed data audits for each target use case

❌ **Overweighting Technology** - Tools don't create AI success; talent and process do.
✅ Instead: Balance technology investment with talent and process development

❌ **Ignoring Culture** - Technical readiness means nothing if organization won't adopt AI.
✅ Instead: Include change management and adoption in readiness assessment

❌ **One-Time Assessment** - AI readiness is dynamic, not static.
✅ Instead: Build regular reassessment into AI governance rhythm

---

## Related Resources

**Frameworks:**
- Gartner AI Maturity Model
- MIT Sloan AI Readiness Index
- McKinsey AI Adoption Framework

**Related Templates:**
- AI Strategy Roadmap - For strategic planning after assessment
- AI Use Case Identification - For prioritizing what AI to build
- AI Data Strategy - For addressing data readiness gaps

---

**Last Updated:** 2025-11-25
**Category:** AI/ML Applications > AI-Strategy
**Difficulty:** Intermediate
**Estimated Time:** 2-4 weeks for comprehensive assessment
```
