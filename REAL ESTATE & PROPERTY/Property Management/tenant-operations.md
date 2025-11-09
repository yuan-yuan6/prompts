# Property Management & Tenant Operations Framework

## Purpose
Comprehensive framework for managing residential and commercial properties including tenant relations, maintenance operations, financial management, compliance, and portfolio optimization.

## Template

Manage property portfolio for [COMPANY_NAME] with [UNIT_COUNT] units across [PROPERTY_COUNT] properties, [TOTAL_SQFT] square feet, targeting [OCCUPANCY_TARGET]% occupancy and [NOI_TARGET]% NOI growth.

### 1. Portfolio Overview

| **Property Type** | **Units/Spaces** | **Square Feet** | **Occupancy** | **Avg Rent** | **NOI** |
|------------------|-----------------|----------------|--------------|-------------|---------|
| Residential Multi-family | [RES_UNITS] | [RES_SQFT] | [RES_OCC]% | $[RES_RENT] | $[RES_NOI] |
| Commercial Office | [OFF_UNITS] | [OFF_SQFT] | [OFF_OCC]% | $[OFF_RENT]/sf | $[OFF_NOI] |
| Retail Space | [RET_UNITS] | [RET_SQFT] | [RET_OCC]% | $[RET_RENT]/sf | $[RET_NOI] |
| Industrial | [IND_UNITS] | [IND_SQFT] | [IND_OCC]% | $[IND_RENT]/sf | $[IND_NOI] |
| Mixed Use | [MIX_UNITS] | [MIX_SQFT] | [MIX_OCC]% | $[MIX_RENT] | $[MIX_NOI] |

### 2. Tenant Acquisition & Screening

**Leasing Funnel:**
```
Lead Generation:
- Inquiries/Month: [INQUIRIES]
- Sources: [LEAD_SOURCES]
- Response Time: [RESPONSE_TIME] hours
- Conversion to Tour: [TOUR_CONV]%

Screening Process:
- Applications/Month: [APPLICATIONS]
- Credit Score Minimum: [CREDIT_MIN]
- Income Requirement: [INCOME_REQ]x rent
- Background Check: [BACKGROUND_CHECK]
- Reference Verification: [REFERENCE_CHECK]

Approval Metrics:
- Approval Rate: [APPROVAL_RATE]%
- Time to Decision: [DECISION_TIME] hours
- Denial Reasons: [DENIAL_REASONS]
- Appeal Process: [APPEAL_PROCESS]
- Fair Housing Compliance: [FAIR_HOUSING]
```

### 3. Lease Management & Renewals

| **Lease Status** | **Count** | **Avg Term** | **Avg Rent** | **Expiring 30d** | **Expiring 90d** |
|-----------------|----------|-------------|-------------|-----------------|-----------------|
| Active Leases | [ACTIVE_COUNT] | [ACTIVE_TERM] mo | $[ACTIVE_RENT] | [EXP_30] | [EXP_90] |
| Month-to-Month | [MTM_COUNT] | N/A | $[MTM_RENT] | N/A | N/A |
| Renewal Pending | [RENEW_PEND] | [RENEW_TERM] mo | $[RENEW_RENT] | [RENEW_30] | [RENEW_90] |
| Notice Given | [NOTICE_COUNT] | N/A | $[NOTICE_RENT] | [NOTICE_30] | [NOTICE_90] |
| Vacant Ready | [VACANT_COUNT] | N/A | $[MARKET_RENT] | N/A | N/A |

**Renewal Strategy:**
```
Renewal Timing: [RENEWAL_START] days before expiration
Renewal Incentives: [RENEWAL_INCENTIVES]
Rent Increase: [RENT_INCREASE]% average
Renewal Rate: [RENEWAL_RATE]%
Retention Cost: $[RETENTION_COST] per unit
```

### 4. Maintenance Operations

**Work Order Management:**
| **Category** | **Monthly Volume** | **Avg Response** | **Completion Time** | **Cost/Order** | **Satisfaction** |
|-------------|-------------------|-----------------|-------------------|---------------|-----------------|
| Emergency | [EMERG_VOL] | [EMERG_RESP] hrs | [EMERG_COMP] hrs | $[EMERG_COST] | [EMERG_SAT]/5 |
| Urgent | [URGENT_VOL] | [URGENT_RESP] hrs | [URGENT_COMP] days | $[URGENT_COST] | [URGENT_SAT]/5 |
| Routine | [ROUTINE_VOL] | [ROUTINE_RESP] days | [ROUTINE_COMP] days | $[ROUTINE_COST] | [ROUTINE_SAT]/5 |
| Preventive | [PREVENT_VOL] | Scheduled | [PREVENT_COMP] days | $[PREVENT_COST] | [PREVENT_SAT]/5 |
| Tenant Request | [TENANT_VOL] | [TENANT_RESP] days | [TENANT_COMP] days | $[TENANT_COST] | [TENANT_SAT]/5 |

### 5. Financial Management

**Revenue & Collections:**
| **Revenue Stream** | **Monthly Amount** | **Collection Rate** | **Days Outstanding** | **Bad Debt** | **Growth** |
|-------------------|-------------------|--------------------|--------------------|-------------|-----------|
| Base Rent | $[BASE_RENT] | [BASE_COLLECT]% | [BASE_DAYS] | $[BASE_BAD] | [BASE_GROWTH]% |
| CAM/NNN | $[CAM_AMOUNT] | [CAM_COLLECT]% | [CAM_DAYS] | $[CAM_BAD] | [CAM_GROWTH]% |
| Utilities | $[UTIL_AMOUNT] | [UTIL_COLLECT]% | [UTIL_DAYS] | $[UTIL_BAD] | [UTIL_GROWTH]% |
| Parking | $[PARK_AMOUNT] | [PARK_COLLECT]% | [PARK_DAYS] | $[PARK_BAD] | [PARK_GROWTH]% |
| Other Income | $[OTHER_AMOUNT] | [OTHER_COLLECT]% | [OTHER_DAYS] | $[OTHER_BAD] | [OTHER_GROWTH]% |

### 6. Operating Expense Management

**Expense Categories:**
```
Fixed Expenses:
- Property Tax: $[PROP_TAX] ([TAX_PSF]/sf)
- Insurance: $[INSURANCE] ([INS_PSF]/sf)
- Management Fee: $[MGMT_FEE] ([MGMT_PCT]% of revenue)
- HOA/Common: $[HOA_FEE]

Variable Expenses:
- Utilities: $[UTILITIES] ([UTIL_PSF]/sf)
- Maintenance: $[MAINTENANCE] ([MAINT_PSF]/sf)
- Repairs: $[REPAIRS] ([REPAIR_PSF]/sf)
- Admin: $[ADMIN] ([ADMIN_PSF]/sf)
- Marketing: $[MARKETING] ([MARKET_PSF]/sf)

Expense Ratio: [EXPENSE_RATIO]%
YoY Change: [EXPENSE_CHANGE]%
Budget Variance: [BUDGET_VAR]%
```

### 7. Vendor & Contractor Management

| **Service Category** | **Primary Vendor** | **Backup Vendor** | **Annual Spend** | **Performance** | **Contract Expiry** |
|--------------------|-------------------|------------------|-----------------|----------------|-------------------|
| HVAC | [HVAC_PRIMARY] | [HVAC_BACKUP] | $[HVAC_SPEND] | [HVAC_PERF]/10 | [HVAC_EXPIRY] |
| Plumbing | [PLUMB_PRIMARY] | [PLUMB_BACKUP] | $[PLUMB_SPEND] | [PLUMB_PERF]/10 | [PLUMB_EXPIRY] |
| Electrical | [ELEC_PRIMARY] | [ELEC_BACKUP] | $[ELEC_SPEND] | [ELEC_PERF]/10 | [ELEC_EXPIRY] |
| Landscaping | [LAND_PRIMARY] | [LAND_BACKUP] | $[LAND_SPEND] | [LAND_PERF]/10 | [LAND_EXPIRY] |
| Cleaning | [CLEAN_PRIMARY] | [CLEAN_BACKUP] | $[CLEAN_SPEND] | [CLEAN_PERF]/10 | [CLEAN_EXPIRY] |
| Security | [SEC_PRIMARY] | [SEC_BACKUP] | $[SEC_SPEND] | [SEC_PERF]/10 | [SEC_EXPIRY] |

### 8. Compliance & Risk Management

**Regulatory Compliance:**
```
Licensing & Permits:
- Business License: [BUS_LICENSE] (Exp: [BUS_EXP])
- Property Management License: [PM_LICENSE] (Exp: [PM_EXP])
- Rental Permits: [RENTAL_PERMITS]
- Certificate of Occupancy: [COO_STATUS]
- Fire Inspection: [FIRE_INSP] (Next: [FIRE_NEXT])

Fair Housing Compliance:
- Training Completed: [FH_TRAINING]%
- Complaints Filed: [FH_COMPLAINTS]
- Violations: [FH_VIOLATIONS]
- Audit Results: [FH_AUDIT]
- Reasonable Accommodations: [ACCOMMODATIONS]

Safety Compliance:
- Safety Inspections: [SAFETY_INSP]
- Incident Reports: [INCIDENTS]/year
- Workers Comp Claims: [WORK_COMP]
- Liability Claims: [LIABILITY]
- Insurance Coverage: $[INSURANCE_COV]
```

### 9. Technology & Systems

| **System** | **Platform** | **Users** | **Integration** | **Cost/Month** | **Satisfaction** |
|-----------|-------------|----------|----------------|---------------|-----------------|
| Property Management | [PMS_PLATFORM] | [PMS_USERS] | [PMS_INT] | $[PMS_COST] | [PMS_SAT]/10 |
| Accounting | [ACCT_PLATFORM] | [ACCT_USERS] | [ACCT_INT] | $[ACCT_COST] | [ACCT_SAT]/10 |
| Maintenance | [MAINT_PLATFORM] | [MAINT_USERS] | [MAINT_INT] | $[MAINT_COST] | [MAINT_SAT]/10 |
| Tenant Portal | [PORTAL_PLATFORM] | [PORTAL_USERS] | [PORTAL_INT] | $[PORTAL_COST] | [PORTAL_SAT]/10 |
| Marketing/Leasing | [MARKET_PLATFORM] | [MARKET_USERS] | [MARKET_INT] | $[MARKET_COST] | [MARKET_SAT]/10 |

### 10. Performance Metrics & KPIs

**Operational Dashboard:**
| **KPI** | **Current** | **Target** | **Industry Avg** | **Trend** | **Action Plan** |
|---------|------------|-----------|-----------------|----------|---------------|
| Occupancy Rate | [OCC_CURRENT]% | [OCC_TARGET]% | [OCC_IND]% | [OCC_TREND] | [OCC_ACTION] |
| Avg Days to Lease | [LEASE_CURRENT] | [LEASE_TARGET] | [LEASE_IND] | [LEASE_TREND] | [LEASE_ACTION] |
| Tenant Satisfaction | [SAT_CURRENT]/10 | [SAT_TARGET]/10 | [SAT_IND]/10 | [SAT_TREND] | [SAT_ACTION] |
| Maintenance Response | [MAINT_CURRENT] hrs | [MAINT_TARGET] hrs | [MAINT_IND] hrs | [MAINT_TREND] | [MAINT_ACTION] |
| Collection Rate | [COLL_CURRENT]% | [COLL_TARGET]% | [COLL_IND]% | [COLL_TREND] | [COLL_ACTION] |
| NOI Margin | [NOI_CURRENT]% | [NOI_TARGET]% | [NOI_IND]% | [NOI_TREND] | [NOI_ACTION] |

## Usage Examples

### Example 1: Multi-family Portfolio
```
Portfolio: 500 units across 10 properties
Location: Major metro area
Occupancy: 95%
Focus: Resident retention, expense control
Technology: Integrated PMS with resident app
Performance: 8% NOI growth
```

### Example 2: Commercial Office Management
```
Portfolio: 1.2M sq ft Class A/B office
Tenants: 150 businesses
Occupancy: 88%
Focus: Tenant experience, amenities
Services: Concierge, fitness, conferencing
Lease Terms: 3-10 years
```

### Example 3: Mixed-Use Development
```
Property: Urban mixed-use complex
Components: Retail, office, residential
Units: 200 residential, 50 commercial
Management: Integrated platform
Focus: Community building, sustainability
Technology: Smart building systems
```

## Customization Options

### 1. Property Type
- Residential only
- Commercial only
- Mixed-use
- Industrial/Flex
- Special purpose

### 2. Management Model
- Self-managed
- Third-party PM
- Hybrid model
- HOA/Condo
- Co-op

### 3. Portfolio Size
- Single property
- Small portfolio (<50 units)
- Mid-size (50-500 units)
- Large (500-5000 units)
- Institutional (5000+ units)

### 4. Geographic Scope
- Single market
- Regional
- Multi-state
- National
- International

### 5. Service Level
- Basic management
- Full service
- Luxury/concierge
- Affordable housing
- Student housing