---
title: Retail Banking Operations & Customer Management Framework
category: finance/Banking
tags: [data-science, finance, framework, management, optimization, research]
use_cases:
  - Implementing comprehensive framework for managing retail banking operations including account...
  - Project planning and execution
  - Strategy development
related_templates:
  - investment-portfolio-management.md
  - digital-banking-strategy.md
  - risk-management-framework.md
last_updated: 2025-11-09
---

# Retail Banking Operations & Customer Management Framework

## Purpose
Comprehensive framework for managing retail banking operations including account management, lending products, digital banking services, branch operations, and customer experience optimization.

## Template

Optimize retail banking operations for [BANK_NAME] serving [CUSTOMER_COUNT] customers across [BRANCH_COUNT] branches with [ASSET_SIZE] in assets, targeting [NPS_TARGET] NPS score and [ROE_TARGET]% ROE.

### 1. Product Portfolio Analysis

| **Product Category** | **Customers** | **Balance** | **Revenue** | **Profitability** | **Growth Rate** |
|--------------------|--------------|------------|-----------|------------------|----------------|
| Checking Accounts | [CHECK_CUST] | $[CHECK_BAL] | $[CHECK_REV] | [CHECK_PROFIT]% | [CHECK_GROWTH]% |
| Savings Accounts | [SAVE_CUST] | $[SAVE_BAL] | $[SAVE_REV] | [SAVE_PROFIT]% | [SAVE_GROWTH]% |
| Personal Loans | [LOAN_CUST] | $[LOAN_BAL] | $[LOAN_REV] | [LOAN_PROFIT]% | [LOAN_GROWTH]% |
| Mortgages | [MORT_CUST] | $[MORT_BAL] | $[MORT_REV] | [MORT_PROFIT]% | [MORT_GROWTH]% |
| Credit Cards | [CARD_CUST] | $[CARD_BAL] | $[CARD_REV] | [CARD_PROFIT]% | [CARD_GROWTH]% |
| Investment Products | [INV_CUST] | $[INV_BAL] | $[INV_REV] | [INV_PROFIT]% | [INV_GROWTH]% |

### 2. Customer Segmentation & Analytics

**Customer Segments:**
```
Mass Market:
- Customers: [MASS_COUNT]
- Average Balance: $[MASS_BALANCE]
- Products per Customer: [MASS_PRODUCTS]
- Lifetime Value: $[MASS_LTV]
- Attrition Rate: [MASS_ATTRITION]%

Affluent:
- Customers: [AFF_COUNT]
- Average Balance: $[AFF_BALANCE]
- Products per Customer: [AFF_PRODUCTS]
- Lifetime Value: $[AFF_LTV]
- Attrition Rate: [AFF_ATTRITION]%

High Net Worth:
- Customers: [HNW_COUNT]
- Average Balance: $[HNW_BALANCE]
- Products per Customer: [HNW_PRODUCTS]
- Lifetime Value: $[HNW_LTV]
- Attrition Rate: [HNW_ATTRITION]%

Digital Native:
- Customers: [DIGITAL_COUNT]
- Average Balance: $[DIGITAL_BALANCE]
- Digital Engagement: [DIGITAL_ENGAGE]%
- Cost to Serve: $[DIGITAL_COST]
- Growth Rate: [DIGITAL_GROWTH]%
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[BANK_NAME]` | Name of the bank | "John Smith" |
| `[CUSTOMER_COUNT]` | Specify the customer count | "10" |
| `[BRANCH_COUNT]` | Specify the branch count | "10" |
| `[ASSET_SIZE]` | Specify the asset size | "[specify value]" |
| `[NPS_TARGET]` | Target or intended nps | "[specify value]" |
| `[ROE_TARGET]` | Target or intended roe | "[specify value]" |
| `[CHECK_CUST]` | Specify the check cust | "[specify value]" |
| `[CHECK_BAL]` | Specify the check bal | "[specify value]" |
| `[CHECK_REV]` | Specify the check rev | "[specify value]" |
| `[CHECK_PROFIT]` | Specify the check profit | "[specify value]" |
| `[CHECK_GROWTH]` | Specify the check growth | "[specify value]" |
| `[SAVE_CUST]` | Specify the save cust | "[specify value]" |
| `[SAVE_BAL]` | Specify the save bal | "[specify value]" |
| `[SAVE_REV]` | Specify the save rev | "[specify value]" |
| `[SAVE_PROFIT]` | Specify the save profit | "[specify value]" |
| `[SAVE_GROWTH]` | Specify the save growth | "[specify value]" |
| `[LOAN_CUST]` | Specify the loan cust | "[specify value]" |
| `[LOAN_BAL]` | Specify the loan bal | "[specify value]" |
| `[LOAN_REV]` | Specify the loan rev | "[specify value]" |
| `[LOAN_PROFIT]` | Specify the loan profit | "[specify value]" |
| `[LOAN_GROWTH]` | Specify the loan growth | "[specify value]" |
| `[MORT_CUST]` | Specify the mort cust | "[specify value]" |
| `[MORT_BAL]` | Specify the mort bal | "[specify value]" |
| `[MORT_REV]` | Specify the mort rev | "[specify value]" |
| `[MORT_PROFIT]` | Specify the mort profit | "[specify value]" |
| `[MORT_GROWTH]` | Specify the mort growth | "[specify value]" |
| `[CARD_CUST]` | Specify the card cust | "[specify value]" |
| `[CARD_BAL]` | Specify the card bal | "[specify value]" |
| `[CARD_REV]` | Specify the card rev | "[specify value]" |
| `[CARD_PROFIT]` | Specify the card profit | "[specify value]" |
| `[CARD_GROWTH]` | Specify the card growth | "[specify value]" |
| `[INV_CUST]` | Specify the inv cust | "[specify value]" |
| `[INV_BAL]` | Specify the inv bal | "[specify value]" |
| `[INV_REV]` | Specify the inv rev | "[specify value]" |
| `[INV_PROFIT]` | Specify the inv profit | "[specify value]" |
| `[INV_GROWTH]` | Specify the inv growth | "[specify value]" |
| `[MASS_COUNT]` | Specify the mass count | "10" |
| `[MASS_BALANCE]` | Specify the mass balance | "[specify value]" |
| `[MASS_PRODUCTS]` | Specify the mass products | "[specify value]" |
| `[MASS_LTV]` | Specify the mass ltv | "[specify value]" |
| `[MASS_ATTRITION]` | Specify the mass attrition | "[specify value]" |
| `[AFF_COUNT]` | Specify the aff count | "10" |
| `[AFF_BALANCE]` | Specify the aff balance | "[specify value]" |
| `[AFF_PRODUCTS]` | Specify the aff products | "[specify value]" |
| `[AFF_LTV]` | Specify the aff ltv | "[specify value]" |
| `[AFF_ATTRITION]` | Specify the aff attrition | "[specify value]" |
| `[HNW_COUNT]` | Specify the hnw count | "10" |
| `[HNW_BALANCE]` | Specify the hnw balance | "[specify value]" |
| `[HNW_PRODUCTS]` | Specify the hnw products | "[specify value]" |
| `[HNW_LTV]` | Specify the hnw ltv | "[specify value]" |
| `[HNW_ATTRITION]` | Specify the hnw attrition | "[specify value]" |
| `[DIGITAL_COUNT]` | Specify the digital count | "10" |
| `[DIGITAL_BALANCE]` | Specify the digital balance | "[specify value]" |
| `[DIGITAL_ENGAGE]` | Specify the digital engage | "[specify value]" |
| `[DIGITAL_COST]` | Specify the digital cost | "[specify value]" |
| `[DIGITAL_GROWTH]` | Specify the digital growth | "[specify value]" |
| `[MOBILE_USERS]` | Specify the mobile users | "[specify value]" |
| `[MOBILE_TRANS]` | Specify the mobile trans | "[specify value]" |
| `[MOBILE_COST]` | Specify the mobile cost | "[specify value]" |
| `[MOBILE_SAT]` | Specify the mobile sat | "[specify value]" |
| `[MOBILE_INVEST]` | Specify the mobile invest | "[specify value]" |
| `[ONLINE_USERS]` | Specify the online users | "[specify value]" |
| `[ONLINE_TRANS]` | Specify the online trans | "[specify value]" |
| `[ONLINE_COST]` | Specify the online cost | "[specify value]" |
| `[ONLINE_SAT]` | Specify the online sat | "[specify value]" |
| `[ONLINE_INVEST]` | Specify the online invest | "[specify value]" |
| `[ATM_USERS]` | Specify the atm users | "[specify value]" |
| `[ATM_TRANS]` | Specify the atm trans | "[specify value]" |
| `[ATM_COST]` | Specify the atm cost | "[specify value]" |
| `[ATM_SAT]` | Specify the atm sat | "[specify value]" |
| `[ATM_INVEST]` | Specify the atm invest | "[specify value]" |
| `[CALL_USERS]` | Specify the call users | "[specify value]" |
| `[CALL_TRANS]` | Specify the call trans | "[specify value]" |
| `[CALL_COST]` | Specify the call cost | "[specify value]" |
| `[CALL_SAT]` | Specify the call sat | "[specify value]" |
| `[CALL_INVEST]` | Specify the call invest | "[specify value]" |
| `[BRANCH_USERS]` | Specify the branch users | "[specify value]" |
| `[BRANCH_TRANS]` | Specify the branch trans | "[specify value]" |
| `[BRANCH_COST]` | Specify the branch cost | "[specify value]" |
| `[BRANCH_SAT]` | Specify the branch sat | "[specify value]" |
| `[BRANCH_INVEST]` | Specify the branch invest | "[specify value]" |
| `[PL_OUTSTANDING]` | Specify the pl outstanding | "[specify value]" |
| `[PL_ORIG]` | Specify the pl orig | "[specify value]" |
| `[PL_DEFAULT]` | Specify the pl default | "[specify value]" |
| `[PL_APR]` | Specify the pl apr | "[specify value]" |
| `[PL_TIME]` | Specify the pl time | "[specify value]" |
| `[AUTO_OUTSTANDING]` | Specify the auto outstanding | "[specify value]" |
| `[AUTO_ORIG]` | Specify the auto orig | "[specify value]" |
| `[AUTO_DEFAULT]` | Specify the auto default | "[specify value]" |
| `[AUTO_APR]` | Specify the auto apr | "[specify value]" |
| `[AUTO_TIME]` | Specify the auto time | "[specify value]" |
| `[HE_OUTSTANDING]` | Specify the he outstanding | "[specify value]" |
| `[HE_ORIG]` | Specify the he orig | "[specify value]" |
| `[HE_DEFAULT]` | Specify the he default | "[specify value]" |
| `[HE_APR]` | Specify the he apr | "[specify value]" |
| `[HE_TIME]` | Specify the he time | "[specify value]" |
| `[MORT_OUTSTANDING]` | Specify the mort outstanding | "[specify value]" |
| `[MORT_ORIG]` | Specify the mort orig | "[specify value]" |
| `[MORT_DEFAULT]` | Specify the mort default | "[specify value]" |
| `[MORT_APR]` | Specify the mort apr | "[specify value]" |
| `[MORT_TIME]` | Specify the mort time | "[specify value]" |
| `[CC_OUTSTANDING]` | Specify the cc outstanding | "[specify value]" |
| `[CC_ORIG]` | Specify the cc orig | "[specify value]" |
| `[CC_DEFAULT]` | Specify the cc default | "[specify value]" |
| `[CC_APR]` | Specify the cc apr | "[specify value]" |
| `[CC_TIME]` | Specify the cc time | "[specify value]" |
| `[NPL_RATIO]` | Specify the npl ratio | "[specify value]" |
| `[COVERAGE_RATIO]` | Specify the coverage ratio | "[specify value]" |
| `[EXPECTED_LOSS]` | Specify the expected loss | "[specify value]" |
| `[RAROC]` | Specify the raroc | "[specify value]" |
| `[PROVISION]` | Specify the provision | "[specify value]" |
| `[FRAUD_LOSS]` | Specify the fraud loss | "[specify value]" |
| `[OP_LOSS]` | Specify the op loss | "[specify value]" |
| `[DOWNTIME]` | Specify the downtime | "[specify value]" |
| `[ERROR_RATE]` | Specify the error rate | "[specify value]" |
| `[BREACHES]` | Specify the breaches | "[specify value]" |
| `[IR_RISK]` | Specify the ir risk | "[specify value]" |
| `[FX_EXPOSURE]` | Specify the fx exposure | "[specify value]" |
| `[LCR]` | Specify the lcr | "[specify value]" |
| `[NSFR]` | Specify the nsfr | "[specify value]" |
| `[DURATION_GAP]` | Specify the duration gap | "6 months" |
| `[FULL_COUNT]` | Specify the full count | "10" |
| `[FULL_TRANS]` | Specify the full trans | "[specify value]" |
| `[FULL_REV]` | Specify the full rev | "[specify value]" |
| `[FULL_COST]` | Specify the full cost | "[specify value]" |
| `[FULL_RATIO]` | Specify the full ratio | "[specify value]" |
| `[LIMITED_COUNT]` | Specify the limited count | "10" |
| `[LIMITED_TRANS]` | Specify the limited trans | "[specify value]" |
| `[LIMITED_REV]` | Specify the limited rev | "[specify value]" |
| `[LIMITED_COST]` | Specify the limited cost | "[specify value]" |
| `[LIMITED_RATIO]` | Specify the limited ratio | "[specify value]" |
| `[KIOSK_COUNT]` | Specify the kiosk count | "10" |
| `[KIOSK_TRANS]` | Specify the kiosk trans | "[specify value]" |
| `[KIOSK_REV]` | Specify the kiosk rev | "[specify value]" |
| `[KIOSK_COST]` | Specify the kiosk cost | "[specify value]" |
| `[KIOSK_RATIO]` | Specify the kiosk ratio | "[specify value]" |
| `[MOBILE_COUNT]` | Specify the mobile count | "10" |
| `[MOBILE_REV]` | Specify the mobile rev | "[specify value]" |
| `[MOBILE_RATIO]` | Specify the mobile ratio | "[specify value]" |
| `[PARTNER_COUNT]` | Specify the partner count | "10" |
| `[PARTNER_TRANS]` | Specify the partner trans | "[specify value]" |
| `[PARTNER_REV]` | Specify the partner rev | "[specify value]" |
| `[PARTNER_COST]` | Specify the partner cost | "[specify value]" |
| `[PARTNER_RATIO]` | Specify the partner ratio | "[specify value]" |
| `[DIG_APPS]` | Specify the dig apps | "[specify value]" |
| `[DIG_APPROVAL]` | Specify the dig approval | "[specify value]" |
| `[DIG_ACTIVATE]` | Specify the dig activate | "[specify value]" |
| `[DIG_CAC]` | Specify the dig cac | "[specify value]" |
| `[DIG_FYV]` | Specify the dig fyv | "[specify value]" |
| `[BRANCH_APPS]` | Specify the branch apps | "[specify value]" |
| `[BRANCH_APPROVAL]` | Specify the branch approval | "[specify value]" |
| `[BRANCH_ACTIVATE]` | Specify the branch activate | "[specify value]" |
| `[BRANCH_CAC]` | Specify the branch cac | "[specify value]" |
| `[BRANCH_FYV]` | Specify the branch fyv | "[specify value]" |
| `[REF_APPS]` | Specify the ref apps | "[specify value]" |
| `[REF_APPROVAL]` | Specify the ref approval | "[specify value]" |
| `[REF_ACTIVATE]` | Specify the ref activate | "[specify value]" |
| `[REF_CAC]` | Specify the ref cac | "[specify value]" |
| `[REF_FYV]` | Specify the ref fyv | "[specify value]" |
| `[PART_APPS]` | Specify the part apps | "[specify value]" |
| `[PART_APPROVAL]` | Specify the part approval | "[specify value]" |
| `[PART_ACTIVATE]` | Specify the part activate | "[specify value]" |
| `[PART_CAC]` | Specify the part cac | "[specify value]" |
| `[PART_FYV]` | Specify the part fyv | "[specify value]" |
| `[MAIL_APPS]` | Specify the mail apps | "[specify value]" |
| `[MAIL_APPROVAL]` | Specify the mail approval | "[specify value]" |
| `[MAIL_ACTIVATE]` | Specify the mail activate | "[specify value]" |
| `[MAIL_CAC]` | Specify the mail cac | "[specify value]" |
| `[MAIL_FYV]` | Specify the mail fyv | "[specify value]" |
| `[CAR]` | Specify the car | "[specify value]" |
| `[CAR_MIN]` | Specify the car min | "[specify value]" |
| `[TIER1]` | Specify the tier1 | "[specify value]" |
| `[TIER1_MIN]` | Specify the tier1 min | "[specify value]" |
| `[LEVERAGE]` | Specify the leverage | "[specify value]" |
| `[LEV_MIN]` | Specify the lev min | "[specify value]" |
| `[CCAR_STATUS]` | Specify the ccar status | "In Progress" |
| `[BASEL_STATUS]` | Specify the basel status | "In Progress" |
| `[CDD_COVERAGE]` | Specify the cdd coverage | "[specify value]" |
| `[TM_ALERTS]` | Specify the tm alerts | "[specify value]" |
| `[SAR_COUNT]` | Specify the sar count | "10" |
| `[AML_TRAINING]` | Specify the aml training | "[specify value]" |
| `[AML_RATING]` | Specify the aml rating | "[specify value]" |
| `[FAIR_LENDING]` | Specify the fair lending | "[specify value]" |
| `[UDAAP_COUNT]` | Specify the udaap count | "10" |
| `[PRIVACY_BREACH]` | Specify the privacy breach | "[specify value]" |
| `[COMPLAINT_TIME]` | Specify the complaint time | "[specify value]" |
| `[EXAM_RATING]` | Specify the exam rating | "[specify value]" |
| `[NIM_CURRENT]` | Specify the nim current | "[specify value]" |
| `[NIM_TARGET]` | Target or intended nim | "[specify value]" |
| `[NIM_INDUSTRY]` | Specify the nim industry | "Technology" |
| `[NIM_CHANGE]` | Specify the nim change | "[specify value]" |
| `[NIM_ACTION]` | Specify the nim action | "[specify value]" |
| `[CTI_CURRENT]` | Specify the cti current | "[specify value]" |
| `[CTI_TARGET]` | Target or intended cti | "[specify value]" |
| `[CTI_INDUSTRY]` | Specify the cti industry | "Technology" |
| `[CTI_CHANGE]` | Specify the cti change | "[specify value]" |
| `[CTI_ACTION]` | Specify the cti action | "[specify value]" |
| `[ROE_CURRENT]` | Specify the roe current | "[specify value]" |
| `[ROE_INDUSTRY]` | Specify the roe industry | "Technology" |
| `[ROE_CHANGE]` | Specify the roe change | "[specify value]" |
| `[ROE_ACTION]` | Specify the roe action | "[specify value]" |
| `[ROA_CURRENT]` | Specify the roa current | "[specify value]" |
| `[ROA_TARGET]` | Target or intended roa | "[specify value]" |
| `[ROA_INDUSTRY]` | Specify the roa industry | "Technology" |
| `[ROA_CHANGE]` | Specify the roa change | "[specify value]" |
| `[ROA_ACTION]` | Specify the roa action | "[specify value]" |
| `[FEE_CURRENT]` | Specify the fee current | "[specify value]" |
| `[FEE_TARGET]` | Target or intended fee | "[specify value]" |
| `[FEE_INDUSTRY]` | Specify the fee industry | "Technology" |
| `[FEE_CHANGE]` | Specify the fee change | "[specify value]" |
| `[FEE_ACTION]` | Specify the fee action | "[specify value]" |
| `[OPEN_INVEST]` | Specify the open invest | "[specify value]" |
| `[OPEN_TIME]` | Specify the open time | "[specify value]" |
| `[OPEN_IMPACT]` | Specify the open impact | "[specify value]" |
| `[OPEN_METRICS]` | Specify the open metrics | "[specify value]" |
| `[OPEN_RISK]` | Specify the open risk | "[specify value]" |
| `[AI_INVEST]` | Specify the ai invest | "[specify value]" |
| `[AI_TIME]` | Specify the ai time | "[specify value]" |
| `[AI_IMPACT]` | Specify the ai impact | "[specify value]" |
| `[AI_METRICS]` | Specify the ai metrics | "[specify value]" |
| `[AI_RISK]` | Specify the ai risk | "[specify value]" |
| `[BLOCK_INVEST]` | Specify the block invest | "[specify value]" |
| `[BLOCK_TIME]` | Specify the block time | "[specify value]" |
| `[BLOCK_IMPACT]` | Specify the block impact | "[specify value]" |
| `[BLOCK_METRICS]` | Specify the block metrics | "[specify value]" |
| `[BLOCK_RISK]` | Specify the block risk | "[specify value]" |
| `[BAAS_INVEST]` | Specify the baas invest | "[specify value]" |
| `[BAAS_TIME]` | Specify the baas time | "[specify value]" |
| `[BAAS_IMPACT]` | Specify the baas impact | "[specify value]" |
| `[BAAS_METRICS]` | Specify the baas metrics | "[specify value]" |
| `[BAAS_RISK]` | Specify the baas risk | "[specify value]" |
| `[GREEN_INVEST]` | Specify the green invest | "[specify value]" |
| `[GREEN_TIME]` | Specify the green time | "[specify value]" |
| `[GREEN_IMPACT]` | Specify the green impact | "[specify value]" |
| `[GREEN_METRICS]` | Specify the green metrics | "[specify value]" |
| `[GREEN_RISK]` | Specify the green risk | "[specify value]" |



### 3. Digital Banking Services

| **Channel** | **Users** | **Transactions/Month** | **Cost/Transaction** | **Satisfaction** | **Investment** |
|------------|----------|----------------------|---------------------|-----------------|---------------|
| Mobile Banking | [MOBILE_USERS] | [MOBILE_TRANS] | $[MOBILE_COST] | [MOBILE_SAT]/10 | $[MOBILE_INVEST] |
| Online Banking | [ONLINE_USERS] | [ONLINE_TRANS] | $[ONLINE_COST] | [ONLINE_SAT]/10 | $[ONLINE_INVEST] |
| ATM Network | [ATM_USERS] | [ATM_TRANS] | $[ATM_COST] | [ATM_SAT]/10 | $[ATM_INVEST] |
| Contact Center | [CALL_USERS] | [CALL_TRANS] | $[CALL_COST] | [CALL_SAT]/10 | $[CALL_INVEST] |
| Branch Network | [BRANCH_USERS] | [BRANCH_TRANS] | $[BRANCH_COST] | [BRANCH_SAT]/10 | $[BRANCH_INVEST] |

### 4. Lending Operations

**Credit Portfolio Management:**
| **Loan Type** | **Outstanding** | **Originations/Month** | **Default Rate** | **Avg APR** | **Processing Time** |
|--------------|----------------|----------------------|-----------------|------------|-------------------|
| Personal Loans | $[PL_OUTSTANDING] | $[PL_ORIG] | [PL_DEFAULT]% | [PL_APR]% | [PL_TIME] days |
| Auto Loans | $[AUTO_OUTSTANDING] | $[AUTO_ORIG] | [AUTO_DEFAULT]% | [AUTO_APR]% | [AUTO_TIME] days |
| Home Equity | $[HE_OUTSTANDING] | $[HE_ORIG] | [HE_DEFAULT]% | [HE_APR]% | [HE_TIME] days |
| Mortgages | $[MORT_OUTSTANDING] | $[MORT_ORIG] | [MORT_DEFAULT]% | [MORT_APR]% | [MORT_TIME] days |
| Credit Cards | $[CC_OUTSTANDING] | $[CC_ORIG] | [CC_DEFAULT]% | [CC_APR]% | [CC_TIME] hours |

### 5. Risk Management

**Risk Metrics Dashboard:**
```
Credit Risk:
- NPL Ratio: [NPL_RATIO]%
- Coverage Ratio: [COVERAGE_RATIO]%
- Expected Loss: $[EXPECTED_LOSS]
- Risk-Adjusted Return: [RAROC]%
- Provision Expense: $[PROVISION]

Operational Risk:
- Fraud Losses: $[FRAUD_LOSS]
- Operational Losses: $[OP_LOSS]
- System Downtime: [DOWNTIME] hours
- Error Rate: [ERROR_RATE]%
- Compliance Breaches: [BREACHES]

Market Risk:
- Interest Rate Risk: [IR_RISK]
- FX Exposure: $[FX_EXPOSURE]
- Liquidity Coverage: [LCR]%
- Net Stable Funding: [NSFR]%
- Duration Gap: [DURATION_GAP]
```

### 6. Branch Network Optimization

| **Branch Type** | **Count** | **Transactions** | **Revenue** | **Cost** | **Efficiency Ratio** |
|----------------|----------|-----------------|-----------|---------|-------------------|
| Full Service | [FULL_COUNT] | [FULL_TRANS] | $[FULL_REV] | $[FULL_COST] | [FULL_RATIO]% |
| Limited Service | [LIMITED_COUNT] | [LIMITED_TRANS] | $[LIMITED_REV] | $[LIMITED_COST] | [LIMITED_RATIO]% |
| Digital Kiosk | [KIOSK_COUNT] | [KIOSK_TRANS] | $[KIOSK_REV] | $[KIOSK_COST] | [KIOSK_RATIO]% |
| Mobile Branch | [MOBILE_COUNT] | [MOBILE_TRANS] | $[MOBILE_REV] | $[MOBILE_COST] | [MOBILE_RATIO]% |
| Partner Location | [PARTNER_COUNT] | [PARTNER_TRANS] | $[PARTNER_REV] | $[PARTNER_COST] | [PARTNER_RATIO]% |

### 7. Customer Acquisition & Retention

**Acquisition Channels:**
| **Channel** | **Applications** | **Approval Rate** | **Activation Rate** | **CAC** | **First Year Value** |
|------------|-----------------|------------------|-------------------|---------|-------------------|
| Digital Marketing | [DIG_APPS] | [DIG_APPROVAL]% | [DIG_ACTIVATE]% | $[DIG_CAC] | $[DIG_FYV] |
| Branch Walk-ins | [BRANCH_APPS] | [BRANCH_APPROVAL]% | [BRANCH_ACTIVATE]% | $[BRANCH_CAC] | $[BRANCH_FYV] |
| Referrals | [REF_APPS] | [REF_APPROVAL]% | [REF_ACTIVATE]% | $[REF_CAC] | $[REF_FYV] |
| Partnerships | [PART_APPS] | [PART_APPROVAL]% | [PART_ACTIVATE]% | $[PART_CAC] | $[PART_FYV] |
| Direct Mail | [MAIL_APPS] | [MAIL_APPROVAL]% | [MAIL_ACTIVATE]% | $[MAIL_CAC] | $[MAIL_FYV] |

### 8. Regulatory Compliance

**Compliance Framework:**
```
Regulatory Requirements:
- Capital Adequacy: [CAR]% (Min: [CAR_MIN]%)
- Tier 1 Capital: [TIER1]% (Min: [TIER1_MIN]%)
- Leverage Ratio: [LEVERAGE]% (Min: [LEV_MIN]%)
- CCAR Stress Test: [CCAR_STATUS]
- Basel III Compliance: [BASEL_STATUS]

AML/KYC Program:
- Customer Due Diligence: [CDD_COVERAGE]%
- Transaction Monitoring: [TM_ALERTS]/month
- SAR Filings: [SAR_COUNT]/month
- Training Completion: [AML_TRAINING]%
- Audit Rating: [AML_RATING]

Consumer Protection:
- Fair Lending Compliance: [FAIR_LENDING]
- UDAAP Violations: [UDAAP_COUNT]
- Privacy Breaches: [PRIVACY_BREACH]
- Complaint Resolution: [COMPLAINT_TIME] days
- Regulatory Exams: [EXAM_RATING]
```

### 9. Financial Performance

| **Metric** | **Current** | **Target** | **Industry Avg** | **YoY Change** | **Action Plan** |
|-----------|------------|-----------|-----------------|---------------|---------------|
| Net Interest Margin | [NIM_CURRENT]% | [NIM_TARGET]% | [NIM_INDUSTRY]% | [NIM_CHANGE]% | [NIM_ACTION] |
| Cost-to-Income | [CTI_CURRENT]% | [CTI_TARGET]% | [CTI_INDUSTRY]% | [CTI_CHANGE]% | [CTI_ACTION] |
| ROE | [ROE_CURRENT]% | [ROE_TARGET]% | [ROE_INDUSTRY]% | [ROE_CHANGE]% | [ROE_ACTION] |
| ROA | [ROA_CURRENT]% | [ROA_TARGET]% | [ROA_INDUSTRY]% | [ROA_CHANGE]% | [ROA_ACTION] |
| Fee Income Ratio | [FEE_CURRENT]% | [FEE_TARGET]% | [FEE_INDUSTRY]% | [FEE_CHANGE]% | [FEE_ACTION] |

### 10. Innovation & Future Strategy

**Strategic Initiatives:**
| **Initiative** | **Investment** | **Timeline** | **Expected Impact** | **Success Metrics** | **Risk Level** |
|---------------|---------------|-------------|-------------------|-------------------|---------------|
| Open Banking Platform | $[OPEN_INVEST] | [OPEN_TIME] | [OPEN_IMPACT] | [OPEN_METRICS] | [OPEN_RISK] |
| AI/ML Implementation | $[AI_INVEST] | [AI_TIME] | [AI_IMPACT] | [AI_METRICS] | [AI_RISK] |
| Blockchain Payments | $[BLOCK_INVEST] | [BLOCK_TIME] | [BLOCK_IMPACT] | [BLOCK_METRICS] | [BLOCK_RISK] |
| BaaS Offering | $[BAAS_INVEST] | [BAAS_TIME] | [BAAS_IMPACT] | [BAAS_METRICS] | [BAAS_RISK] |
| Green Banking | $[GREEN_INVEST] | [GREEN_TIME] | [GREEN_IMPACT] | [GREEN_METRICS] | [GREEN_RISK] |

## Usage Examples

### Example 1: Large National Bank
```
Bank: National Retail Bank
Customers: 10 million
Branches: 2,000
Assets: $500 billion
Digital Adoption: 75%
Focus: Digital transformation, branch optimization
```

### Example 2: Regional Community Bank
```
Bank: Community First Bank
Customers: 500,000
Branches: 50
Assets: $10 billion
Market: 3-state region
Focus: Relationship banking, local presence
```

### Example 3: Digital-Only Bank
```
Bank: NextGen Digital Bank
Customers: 2 million
Branches: 0
Assets: $20 billion
Acquisition: 100% digital
Focus: Mobile-first, AI-driven services
```

## Customization Options

### 1. Bank Type
- National bank
- Regional bank
- Community bank
- Digital-only bank
- Credit union

### 2. Market Focus
- Mass market
- Affluent segment
- Youth/Students
- Small business
- Multicultural

### 3. Channel Strategy
- Branch-centric
- Digital-first
- Hybrid model
- Mobile-only
- Partnership-based

### 4. Product Emphasis
- Deposit-focused
- Lending-focused
- Fee-based services
- Wealth management
- Payments/Cards

### 5. Growth Strategy
- Organic growth
- M&A driven
- Digital expansion
- Geographic expansion
- Product diversification