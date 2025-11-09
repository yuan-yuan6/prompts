# Insurance Underwriting & Risk Assessment Framework

## Purpose
Comprehensive framework for insurance underwriting operations including risk assessment, pricing, portfolio management, automation strategies, and profitability optimization across multiple lines of business.

## Template

Optimize underwriting operations for [COMPANY_NAME] managing [PREMIUM_VOLUME] in annual premiums across [PRODUCT_LINES] with target combined ratio of [CR_TARGET]% and ROE of [ROE_TARGET]%.

### 1. Portfolio Risk Assessment

| **Line of Business** | **Premium Volume** | **Loss Ratio** | **Expense Ratio** | **Combined Ratio** | **Growth Rate** |
|--------------------|-------------------|---------------|------------------|-------------------|----------------|
| Personal Auto | $[AUTO_PREMIUM] | [AUTO_LOSS]% | [AUTO_EXPENSE]% | [AUTO_CR]% | [AUTO_GROWTH]% |
| Homeowners | $[HOME_PREMIUM] | [HOME_LOSS]% | [HOME_EXPENSE]% | [HOME_CR]% | [HOME_GROWTH]% |
| Commercial Property | $[PROP_PREMIUM] | [PROP_LOSS]% | [PROP_EXPENSE]% | [PROP_CR]% | [PROP_GROWTH]% |
| General Liability | $[GL_PREMIUM] | [GL_LOSS]% | [GL_EXPENSE]% | [GL_CR]% | [GL_GROWTH]% |
| Life Insurance | $[LIFE_PREMIUM] | [LIFE_LOSS]% | [LIFE_EXPENSE]% | [LIFE_CR]% | [LIFE_GROWTH]% |
| Health Insurance | $[HEALTH_PREMIUM] | [HEALTH_LOSS]% | [HEALTH_EXPENSE]% | [HEALTH_CR]% | [HEALTH_GROWTH]% |

### 2. Underwriting Guidelines & Authority

**Authority Matrix:**
```
Underwriter Levels:
Junior Underwriter:
- Authority Limit: $[JUNIOR_LIMIT]
- Approval Rate: [JUNIOR_APPROVAL]%
- Referral Rate: [JUNIOR_REFERRAL]%
- Average TAT: [JUNIOR_TAT] hours
- Quality Score: [JUNIOR_QUALITY]/10

Senior Underwriter:
- Authority Limit: $[SENIOR_LIMIT]
- Approval Rate: [SENIOR_APPROVAL]%
- Referral Rate: [SENIOR_REFERRAL]%
- Average TAT: [SENIOR_TAT] hours
- Quality Score: [SENIOR_QUALITY]/10

Chief Underwriter:
- Authority Limit: $[CHIEF_LIMIT]
- Approval Rate: [CHIEF_APPROVAL]%
- Referral Rate: [CHIEF_REFERRAL]%
- Average TAT: [CHIEF_TAT] hours
- Quality Score: [CHIEF_QUALITY]/10

Automated Decisions:
- Straight-Through Rate: [STP_RATE]%
- Auto-Approval: [AUTO_APPROVE]%
- Auto-Decline: [AUTO_DECLINE]%
- Manual Review: [MANUAL_REVIEW]%
```

### 3. Risk Selection Criteria

| **Risk Factor** | **Weight** | **Scoring Range** | **Threshold** | **Impact on Premium** | **Decline Criteria** |
|----------------|-----------|------------------|--------------|---------------------|-------------------|
| Credit Score | [CREDIT_WEIGHT]% | [CREDIT_RANGE] | [CREDIT_THRESH] | [CREDIT_IMPACT]% | [CREDIT_DECLINE] |
| Claims History | [CLAIMS_WEIGHT]% | [CLAIMS_RANGE] | [CLAIMS_THRESH] | [CLAIMS_IMPACT]% | [CLAIMS_DECLINE] |
| Location/Territory | [LOC_WEIGHT]% | [LOC_RANGE] | [LOC_THRESH] | [LOC_IMPACT]% | [LOC_DECLINE] |
| Property/Asset Value | [VALUE_WEIGHT]% | [VALUE_RANGE] | [VALUE_THRESH] | [VALUE_IMPACT]% | [VALUE_DECLINE] |
| Industry/Occupation | [IND_WEIGHT]% | [IND_RANGE] | [IND_THRESH] | [IND_IMPACT]% | [IND_DECLINE] |
| Coverage Limits | [LIMIT_WEIGHT]% | [LIMIT_RANGE] | [LIMIT_THRESH] | [LIMIT_IMPACT]% | [LIMIT_DECLINE] |

### 4. Pricing & Rating Models

**Pricing Components:**
| **Component** | **Base Rate** | **Factors** | **Adjustments** | **Competitive Position** | **Profitability** |
|--------------|-------------|-----------|----------------|----------------------|------------------|
| Base Premium | $[BASE_PREM] | [BASE_FACTORS] | [BASE_ADJUST] | [BASE_COMPETE] | [BASE_PROFIT]% |
| Risk Loading | [RISK_LOAD]% | [RISK_FACTORS] | [RISK_ADJUST] | [RISK_COMPETE] | [RISK_PROFIT]% |
| Expense Loading | [EXP_LOAD]% | [EXP_FACTORS] | [EXP_ADJUST] | [EXP_COMPETE] | [EXP_PROFIT]% |
| Profit Margin | [PROFIT_MARGIN]% | [PROFIT_FACTORS] | [PROFIT_ADJUST] | [PROFIT_COMPETE] | [PROFIT_TARGET]% |
| Discounts/Credits | [DISCOUNT]% | [DISC_FACTORS] | [DISC_ADJUST] | [DISC_COMPETE] | [DISC_IMPACT]% |

### 5. Automation & Technology

**Digital Underwriting Capabilities:**
```
Automated Processes:
- Application Intake: [INTAKE_AUTO]% automated
- Data Enrichment: [ENRICH_AUTO]% automated
- Risk Scoring: [SCORE_AUTO]% automated
- Decision Making: [DECISION_AUTO]% automated
- Policy Issuance: [ISSUE_AUTO]% automated

Technology Stack:
- Core System: [CORE_SYSTEM]
- Rating Engine: [RATING_ENGINE]
- Rules Engine: [RULES_ENGINE]
- Predictive Models: [PRED_MODELS]
- External Data: [EXT_DATA]

AI/ML Applications:
- Fraud Detection: [FRAUD_ACCURACY]% accuracy
- Risk Prediction: [RISK_ACCURACY]% accuracy
- Price Optimization: [PRICE_LIFT]% lift
- Text Analytics: [TEXT_COVERAGE]% coverage
- Image Analysis: [IMAGE_USE] use cases
```

### 6. Reinsurance Strategy

| **Treaty Type** | **Coverage** | **Retention** | **Limit** | **Premium Ceded** | **Recovery Rate** |
|----------------|-------------|--------------|----------|------------------|------------------|
| Quota Share | [QS_COVERAGE] | [QS_RETENTION]% | $[QS_LIMIT] | [QS_PREMIUM]% | [QS_RECOVERY]% |
| Excess of Loss | [XOL_COVERAGE] | $[XOL_RETENTION] | $[XOL_LIMIT] | $[XOL_PREMIUM] | [XOL_RECOVERY]% |
| Catastrophe | [CAT_COVERAGE] | $[CAT_RETENTION] | $[CAT_LIMIT] | $[CAT_PREMIUM] | [CAT_RECOVERY]% |
| Facultative | [FAC_COVERAGE] | Case-by-case | $[FAC_LIMIT] | $[FAC_PREMIUM] | [FAC_RECOVERY]% |
| Stop Loss | [STOP_COVERAGE] | [STOP_RETENTION]% | [STOP_LIMIT]% | $[STOP_PREMIUM] | [STOP_RECOVERY]% |

### 7. Claims & Loss Management

**Loss Development Analysis:**
| **Accident Year** | **Reported Claims** | **Incurred Loss** | **Paid Loss** | **IBNR** | **Ultimate Loss** |
|------------------|-------------------|------------------|-------------|----------|------------------|
| [YEAR_1] | [CLAIMS_1] | $[INCURRED_1] | $[PAID_1] | $[IBNR_1] | $[ULTIMATE_1] |
| [YEAR_2] | [CLAIMS_2] | $[INCURRED_2] | $[PAID_2] | $[IBNR_2] | $[ULTIMATE_2] |
| [YEAR_3] | [CLAIMS_3] | $[INCURRED_3] | $[PAID_3] | $[IBNR_3] | $[ULTIMATE_3] |
| [YEAR_4] | [CLAIMS_4] | $[INCURRED_4] | $[PAID_4] | $[IBNR_4] | $[ULTIMATE_4] |
| [YEAR_5] | [CLAIMS_5] | $[INCURRED_5] | $[PAID_5] | $[IBNR_5] | $[ULTIMATE_5] |

### 8. Regulatory & Compliance

**Compliance Framework:**
```
Regulatory Requirements:
- Solvency Ratio: [SOLVENCY]% (Min: [SOLV_MIN]%)
- Risk-Based Capital: [RBC]% (Min: [RBC_MIN]%)
- Reserve Adequacy: [RESERVE_ADEQ]%
- Rate Filing Status: [RATE_STATUS]
- Market Conduct: [CONDUCT_SCORE]

State Regulations:
- Filed States: [FILED_STATES]
- Approved States: [APPROVED_STATES]
- Pending Filings: [PENDING_FILES]
- Compliance Issues: [COMPLIANCE_ISSUES]
- Examination Status: [EXAM_STATUS]

Fair Practices:
- Discrimination Testing: [DISC_TEST]
- Affordability Index: [AFFORD_INDEX]
- Availability Metrics: [AVAIL_METRICS]
- Consumer Complaints: [COMPLAINT_RATIO]
- Regulatory Actions: [REG_ACTIONS]
```

### 9. Performance Metrics

| **KPI** | **Current** | **Target** | **Industry Benchmark** | **Trend** | **Action Plan** |
|---------|------------|-----------|----------------------|----------|---------------|
| New Business Hit Ratio | [HIT_CURRENT]% | [HIT_TARGET]% | [HIT_BENCH]% | [HIT_TREND] | [HIT_ACTION] |
| Retention Rate | [RET_CURRENT]% | [RET_TARGET]% | [RET_BENCH]% | [RET_TREND] | [RET_ACTION] |
| Average Premium | $[PREM_CURRENT] | $[PREM_TARGET] | $[PREM_BENCH] | [PREM_TREND] | [PREM_ACTION] |
| Loss Ratio | [LOSS_CURRENT]% | [LOSS_TARGET]% | [LOSS_BENCH]% | [LOSS_TREND] | [LOSS_ACTION] |
| Submission TAT | [TAT_CURRENT] hrs | [TAT_TARGET] hrs | [TAT_BENCH] hrs | [TAT_TREND] | [TAT_ACTION] |
| Quality Score | [QUAL_CURRENT]/10 | [QUAL_TARGET]/10 | [QUAL_BENCH]/10 | [QUAL_TREND] | [QUAL_ACTION] |

### 10. Market Strategy & Innovation

**Strategic Initiatives:**
| **Initiative** | **Investment** | **Timeline** | **Expected Impact** | **Success Metrics** | **Risk Assessment** |
|---------------|---------------|-------------|-------------------|-------------------|-------------------|
| Usage-Based Insurance | $[UBI_INVEST] | [UBI_TIME] | [UBI_IMPACT] | [UBI_METRICS] | [UBI_RISK] |
| Parametric Products | $[PARA_INVEST] | [PARA_TIME] | [PARA_IMPACT] | [PARA_METRICS] | [PARA_RISK] |
| Embedded Insurance | $[EMBED_INVEST] | [EMBED_TIME] | [EMBED_IMPACT] | [EMBED_METRICS] | [EMBED_RISK] |
| Digital Distribution | $[DIGITAL_INVEST] | [DIGITAL_TIME] | [DIGITAL_IMPACT] | [DIGITAL_METRICS] | [DIGITAL_RISK] |
| ESG Underwriting | $[ESG_INVEST] | [ESG_TIME] | [ESG_IMPACT] | [ESG_METRICS] | [ESG_RISK] |

## Usage Examples

### Example 1: P&C Insurance Carrier
```
Company: Regional P&C Insurer
Premium: $2B annual
Lines: Auto, Home, Commercial
Combined Ratio: 95%
Technology: AI-driven underwriting
Focus: Profitability improvement
```

### Example 2: Life Insurance Company
```
Company: National Life Insurer
Premium: $10B annual
Products: Term, Whole, Universal
Distribution: Agents, Direct, Digital
Underwriting: Accelerated, automated
Focus: Digital transformation
```

### Example 3: Health Insurance Plan
```
Company: Regional Health Plan
Members: 2 million
Premium: $8B annual
Network: 50,000 providers
Medical Loss Ratio: 85%
Focus: Value-based care, prevention
```

## Customization Options

### 1. Insurance Type
- Property & Casualty
- Life & Annuities
- Health & Medical
- Specialty Lines
- Reinsurance

### 2. Distribution Model
- Direct to consumer
- Agent/Broker
- Digital platforms
- Embedded/API
- Bancassurance

### 3. Market Segment
- Personal lines
- Commercial lines
- Small business
- Enterprise
- Specialty risks

### 4. Underwriting Approach
- Traditional manual
- Rules-based
- Predictive modeling
- AI/ML driven
- Automated/Straight-through

### 5. Growth Strategy
- Organic growth
- M&A expansion
- Product innovation
- Geographic expansion
- Partnership/Ecosystem