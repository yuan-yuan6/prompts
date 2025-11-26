---
category: product-management
last_updated: 2025-11-12
title: Pricing Strategy & Packaging
tags:
- product-management
- pricing
- strategy
- monetization
use_cases:
- Developing pricing strategy for new products or features
- Optimizing existing pricing and packaging
- Designing tier structures and value metrics
- Testing and iterating on pricing models
related_templates:
- product-management/Product-Strategy/product-strategy-vision.md
- product-management/Product-Development/go-to-market-planning.md
- product-management/Product-Strategy/market-competitive-analysis.md
- product-management/Product-Analytics/ab-testing-experimentation.md
- sales-marketing/Retail-Ecommerce/pricing-strategy.md  # Retail pricing & revenue optimization
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: pricing-strategy
---

# Pricing Strategy & Packaging Template

## Purpose
Develop comprehensive pricing and packaging strategies that align with customer value perception, competitive positioning, and business objectives to maximize revenue and market penetration.

## Quick Pricing Prompt
Design pricing for [product] with [business model: SaaS/usage/freemium]. Define value metric (what customers pay for). Create 3 tiers: entry (conversion), core (majority), premium (expansion). Set price points based on: value delivered, competitor benchmarks [list competitors + prices], willingness-to-pay research. Include: feature packaging per tier, free trial/freemium strategy, and target conversion rates.

## Quick Start

**Need pricing strategy quickly?** Use this streamlined approach:

### Minimal Example
```
Product: Team collaboration tool
Value Metric: Per active user
Model: Freemium + subscription tiers
Tiers:
- Free: 5 users, core features
- Pro: $12/user/month, advanced features
- Enterprise: $25/user/month, security + support
Anchor: Enterprise at $25, makes Pro feel like great value
Competition: Slack at $8, Asana at $11, we're premium but worth it
Target: 15% free→paid conversion, $50K MRR in 6 months
```

### When to Use This
- Launching new products or entering new markets
- Optimizing existing pricing for growth or profitability
- Responding to competitive pricing pressure
- Packaging new features or value propositions
- Preparing for fundraising or financial planning

### Basic 5-Step Workflow
1. **Value analysis** - Understand value delivered and willingness to pay (1 week)
2. **Model selection** - Choose pricing model and value metric (2-3 days)
3. **Tier design** - Create packaging tiers and price points (1 week)
4. **Testing & validation** - Test with customers, iterate (2-4 weeks)
5. **Launch & optimize** - Implement and continuously improve (ongoing)

---

## Template

```
You are an experienced pricing strategist. Develop comprehensive pricing and packaging strategy for [PRODUCT_NAME] serving [TARGET_CUSTOMERS] with [VALUE_PROPOSITION] using [PRICING_MODEL] to achieve [REVENUE_GOALS] while maintaining [COMPETITIVE_POSITION].

PRICING CONTEXT:
Product Information:
- Product name: [PRODUCT_NAME]
- Category: [PRODUCT_CATEGORY]
- Stage: [NEW_LAUNCH/OPTIMIZATION/GROWTH]
- Target market: [CUSTOMER_SEGMENTS]
- Value proposition: [CORE_VALUE]

Business Objectives:
- Revenue target: [GOAL]
- Growth strategy: [LAND_AND_EXPAND/PENETRATION/PREMIUM]
- Market position: [CHALLENGER/LEADER/NICHE]
- Unit economics: [TARGET_LTV:CAC]

Current State (if applicable):
- Current pricing: [EXISTING_MODEL]
- Conversion rate: [%]
- ARPU: [AMOUNT]
- Churn: [%]
- Issues: [PROBLEMS_TO_SOLVE]

### 1. VALUE ANALYSIS

Customer Value Delivered:
Quantifiable Value:
- Value 1: [SPECIFIC_BENEFIT]
  - Customer gains: [REVENUE_INCREASE/COST_SAVINGS/TIME_SAVED]
  - Quantification: [DOLLAR_AMOUNT_OR_PERCENTAGE]
  - Evidence: [DATA_OR_TESTIMONIAL]

Example:
"Automated reporting saves 10 hours/week"
- Customer gains: 40 hours/month saved
- Quantification: $4,000/month (at $100/hour fully loaded cost)
- Evidence: Time study with 20 customers

- Value 2: [BENEFIT]
  (Same structure)

- Value 3: [BENEFIT]
  (Same structure)

Qualitative Value:
- Emotional benefit: [HOW_IT_MAKES_THEM_FEEL]
- Risk reduction: [WHAT_RISKS_ELIMINATED]
- Status/identity: [SOCIAL_VALUE]

Total Value Delivered: [ESTIMATED_MONTHLY/ANNUAL_VALUE]

Value:Price Ratio:
- Total value delivered: [AMOUNT]
- Current price: [AMOUNT]
- Ratio: [X:1]
- Target: [10:1_OR_HIGHER]

Willingness to Pay Research:
Van Westendorp Price Sensitivity:
Questions asked:
1. Too expensive (would not consider): [PRICE_POINT]
2. Expensive but would consider: [PRICE_POINT]
3. Good value: [PRICE_POINT]
4. Too cheap (suspect quality): [PRICE_POINT]

Results:
- Optimal price point: [RANGE]
- Acceptable range: [MIN_TO_MAX]
- Premium acceptable: [UPPER_BOUND]

Sample: [NUMBER_OF_RESPONDENTS]
Segments: [HOW_WTP_VARIES]

Competitive Pricing Context:
| Competitor | Product | Price | Value Perception |
|------------|---------|-------|------------------|
| [COMP_1] | [PRODUCT] | [PRICE] | [HIGH/MEDIUM/LOW] |
| [COMP_2] | [PRODUCT] | [PRICE] | [HIGH/MEDIUM/LOW] |
| [COMP_3] | [PRODUCT] | [PRICE] | [HIGH/MEDIUM/LOW] |

Our Target: [PRICE] - [POSITIONING]

### 2. PRICING MODEL SELECTION

Pricing Model Options:
Option 1: [MODEL_NAME]
- Description: [HOW_IT_WORKS]
- Examples: [WHO_USES_THIS]
- Pros:
  - [ADVANTAGE_1]
  - [ADVANTAGE_2]
- Cons:
  - [DISADVANTAGE_1]
  - [DISADVANTAGE_2]
- Fit for us: [HIGH/MEDIUM/LOW]

Common Models:
1. **Per-user (seat-based)**: $X per user per month
   - Best for: Team collaboration, SaaS tools
   - Pros: Simple, scalable, predictable
   - Cons: Discourages adding users, not tied to value

2. **Usage-based**: $X per API call, GB, transaction
   - Best for: Infrastructure, APIs, platforms
   - Pros: Aligns price with value, fair for all sizes
   - Cons: Unpredictable revenue, hard to forecast

3. **Flat-rate subscription**: $X per month per company
   - Best for: Unlimited use cases, want predictability
   - Pros: Simple, encourages adoption, high value perception
   - Cons: Leaves money on table with large customers

4. **Tiered subscription**: Good/Better/Best packages
   - Best for: Serving multiple segments with one product
   - Pros: Captures different willingness to pay, upsell path
   - Cons: Complex to design, can overwhelm buyers

5. **Freemium**: Free tier + paid upgrades
   - Best for: PLG, viral products, need large user base
   - Pros: Low friction adoption, network effects
   - Cons: Low conversion rates, support costs

6. **Usage + seat hybrid**: $X/user + $Y/1000 API calls
   - Best for: Platform products with multiple value drivers
   - Pros: Captures value from different dimensions
   - Cons: Complex to understand and forecast

Recommended Model: [CHOICE]
Rationale: [WHY_THIS_MODEL_FITS_BEST]

Value Metric Selection:
What to charge for: [METRIC]
- Why this metric: [ALIGNMENT_WITH_VALUE]
- Easy to understand: [YES/NO]
- Easy to measure: [YES/NO]
- Grows with value: [YES/NO]
- Predictable: [YES/NO]

Examples:
- Good: Active users (grows with team, measures engagement)
- Bad: Features (doesn't reflect value, hard to package)
- Good: Projects managed (scales with usage)
- Bad: Logins (doesn't correlate with value)

### 3. PACKAGING & TIERS

Tier Strategy:
Number of Tiers: [COUNT]
- Rationale: [WHY_THIS_NUMBER]
- Segments served: [WHO_EACH_TIER_FOR]

Good/Better/Best Framework:
Tier 1: [TIER_NAME] (Entry/Free)
- Target customer: [WHO_THIS_FOR]
- Price: [AMOUNT_OR_FREE]
- Core value: [MAIN_BENEFIT]
- Key features:
  - [FEATURE_1]
  - [FEATURE_2]
  - [FEATURE_3]
- Limitations:
  - [LIMIT_1]
  - [LIMIT_2]
- Goal: [ACQUISITION/LAND/TRIAL]

Tier 2: [TIER_NAME] (Most Popular)
- Target customer: [WHO_THIS_FOR]
- Price: [AMOUNT]
- Additional value: [WHAT_MORE_THEY_GET]
- Key features:
  - Everything in [TIER_1]
  - [FEATURE_1]
  - [FEATURE_2]
  - [FEATURE_3]
- Limitations:
  - [LIMIT_1]
- Goal: [PRIMARY_REVENUE_DRIVER]
- % of customers: [TARGET_%]

Tier 3: [TIER_NAME] (Premium/Enterprise)
- Target customer: [WHO_THIS_FOR]
- Price: [AMOUNT_OR_CUSTOM]
- Additional value: [WHAT_MORE_THEY_GET]
- Key features:
  - Everything in [TIER_2]
  - [FEATURE_1]
  - [FEATURE_2]
  - [FEATURE_3]
- Goal: [EXPANSION/ENTERPRISE]
- % of customers: [TARGET_%]

Feature Allocation:
Table Stakes (All Tiers):
- [FEATURE_1]
- [FEATURE_2]

Differentiation (Higher Tiers):
- [TIER_2_EXCLUSIVE]
- [TIER_3_EXCLUSIVE]

Tier Anchoring:
- Anchor tier: [HIGHEST_TIER]
- Decoy: [MIDDLE_TIER_POSITIONED_AS_VALUE]
- Target: [TIER_YOU_WANT_MOST_TO_CHOOSE]

Example:
- Enterprise: $25/user (anchor, expensive)
- Pro: $12/user (feels like great value vs Enterprise)
- Free: $0 (gets them in door)
- Goal: Most choose Pro (seems cheap vs $25)

### 4. PRICE POINTS

Pricing Psychology:
Charm Pricing:
- Use: $99 instead of $100
- Why: Feels significantly cheaper
- When: Consumer products, SMB

Prestige Pricing:
- Use: $500 instead of $499
- Why: Signals quality
- When: Premium products, enterprise

Price Anchoring:
- Show: [HIGHER_PRICE] crossed out, [ACTUAL_PRICE]
- Effect: Makes actual price feel like deal
- Example: Annual plan shows monthly equivalent savings

Tier Pricing Math:
Tier 1: [PRICE]
Tier 2: [PRICE] (2-3x Tier 1)
Tier 3: [PRICE] (2-3x Tier 2)

Rationale:
- Gaps large enough to feel meaningful
- Not so large that Tier 3 feels unattainable
- Tier 2 feels like sweet spot

Annual vs Monthly:
Monthly: [PRICE]
Annual: [PRICE] ([DISCOUNT_%] off monthly)
- Annual discount: [15-25%_TYPICAL]
- Why: Reduces churn, improves cash flow
- Positioning: [MONTHS_FREE] (e.g., "2 months free")

### 5. DISCOUNTING STRATEGY

Discount Framework:
Standard Discounts:
- Annual prepay: [%_DISCOUNT]
- Volume: [DISCOUNT_STRUCTURE]
  - Example: 10% at 50 seats, 20% at 100 seats
- Non-profit/education: [%_DISCOUNT]

Strategic Discounts:
- Competitive displacement: Up to [%]
  - When: Switching from competitor
  - Requires: Proof of current solution
  - Duration: [TEMPORARY/PERMANENT]

- Upmarket expansion: Up to [%]
  - When: Large enterprise deals
  - Requires: Reference customer agreement
  - Duration: [YEAR_1_ONLY]

Discount Guardrails:
- Max discount: [%]
- Approval required: [WHO_CAN_APPROVE]
- Never discount: [WHAT_STAYS_FULL_PRICE]
- Grandfather clause: [EXISTING_CUSTOMER_PROTECTION]

Promotional Pricing:
Launch Promotion:
- Offer: [DISCOUNT_OR_BONUS]
- Duration: [TIMEFRAME]
- Goal: [OBJECTIVE]
- Exit strategy: [HOW_TO_END]

Seasonal Promotions:
- When: [TIMING]
- Offer: [DISCOUNT]
- Goal: [REVENUE_OR_ACQUISITION_TARGET]

### 6. PRICING VALIDATION & TESTING

Pre-Launch Testing:
Conjoint Analysis:
- Features tested: [LIST]
- Price points tested: [RANGE]
- Sample: [NUMBER_OF_CUSTOMERS]
- Findings: [OPTIMAL_COMBINATION]

A/B Testing Plan:
Test 1: Price Point Test
- Control: [CURRENT_PRICE]
- Variant: [TEST_PRICE]
- Hypothesis: [WHAT_YOU_BELIEVE]
- Metric: [CONVERSION_RATE/REVENUE]
- Duration: [TIMELINE]
- Sample size: [USERS_NEEDED]

Test 2: Packaging Test
- Control: [CURRENT_TIERS]
- Variant: [NEW_TIER_STRUCTURE]
- Hypothesis: [WHAT_YOU_BELIEVE]
- Metric: [TIER_MIX/ARPU]

Price Sensitivity Analysis:
- Elasticity: [PRICE_ELASTICITY_COEFFICIENT]
- Interpretation: [WHAT_IT_MEANS]
  - Elastic (>1): Volume drops significantly with price increase
  - Inelastic (<1): Can raise prices without losing volume

Customer Interviews:
Questions:
1. "At what price is this a no-brainer?"
2. "At what price would you start to hesitate?"
3. "At what price is it too expensive?"
4. "What would make you pay 2x our current price?"

Insights: [KEY_THEMES]

### 7. COMPETITIVE PRICING STRATEGY

Competitive Positioning:
Strategy: [PREMIUM/PARITY/PENETRATION]

Premium Pricing (+20-50% vs competition):
- When: Superior value, strong brand, differentiated
- Justification: [WHY_WORTH_MORE]
- Risk: Lower volume
- Mitigation: [HOW_TO_PROVE_VALUE]

Parity Pricing (±10% vs competition):
- When: Similar value, competitive market
- Differentiation: [NON_PRICE_FACTORS]
- Risk: Price war
- Mitigation: [VALUE_FOCUS]

Penetration Pricing (-20-40% vs competition):
- When: New entrant, land grab, scale advantages
- Goal: [MARKET_SHARE_TARGET]
- Risk: Hard to raise later
- Timeline: [HOW_LONG_TO_STAY_LOW]

Competitive Response Plan:
If Competitor Cuts Price:
- Threshold: [WHEN_TO_RESPOND]
- Response 1: [MAINTAIN_PRICE_EMPHASIZE_VALUE]
- Response 2: [MATCH_FOR_COMPETITIVE_DEALS]
- Response 3: [ADD_VALUE_VS_CUT_PRICE]
- Never: [RACE_TO_BOTTOM]

### 8. ENTERPRISE VS SMB PRICING

SMB Pricing:
- Model: [SELF_SERVE/LOW_TOUCH]
- Price point: [AMOUNT]
- Payment: [CREDIT_CARD/MONTHLY]
- Sales: [PRODUCT_LED/INSIDE_SALES]
- Support: [SELF_SERVICE/EMAIL]

Mid-Market Pricing:
- Model: [HYBRID]
- Price point: [AMOUNT]
- Payment: [ANNUAL_CONTRACT]
- Sales: [INSIDE_SALES]
- Support: [EMAIL+PHONE]

Enterprise Pricing:
- Model: [CUSTOM/NEGOTIATED]
- Starting point: [BASE_PRICE]
- Payment: [ANNUAL/MULTI_YEAR]
- Sales: [FIELD_SALES/ACCOUNT_EXEC]
- Support: [DEDICATED_CSM]

Enterprise Customization:
What's Negotiable:
- Price: [WITHIN_BOUNDS]
- Volume discounts: [STRUCTURE]
- Payment terms: [NET_30/60/90]
- Contract length: [1-3_YEARS]

What's Not:
- Product features: [NO_CUSTOM_DEVELOPMENT]
- Core pricing model: [STAYS_CONSISTENT]
- Security/compliance: [STANDARD_FOR_ALL]

### 9. IMPLEMENTATION PLAN

Pricing Launch:
Phase 1: Internal Alignment (Week 1-2)
- [ ] Present pricing to leadership
- [ ] Train sales team
- [ ] Update sales materials
- [ ] Brief customer success
- [ ] Prepare FAQ

Phase 2: Infrastructure (Week 2-3)
- [ ] Update billing system
- [ ] Configure pricing in product
- [ ] Test checkout flow
- [ ] Set up analytics
- [ ] Prepare communications

Phase 3: Launch (Week 4)
- [ ] Announce to market
- [ ] Grandfather existing customers
- [ ] Monitor closely
- [ ] Support handles questions
- [ ] Collect feedback

Phase 4: Optimize (Ongoing)
- [ ] Weekly metrics review
- [ ] Monthly pricing analysis
- [ ] Quarterly adjustments
- [ ] Annual comprehensive review

Existing Customer Migration:
Grandfather Clause:
- Who: [EXISTING_CUSTOMERS_AS_OF_DATE]
- Duration: [HOW_LONG_PROTECTED]
- Conditions: [WHEN_CLAUSE_ENDS]

Migration Strategy:
- Timeline: [WHEN_TO_MIGRATE]
- Communication: [HOW_TO_ANNOUNCE]
- Incentive: [EARLY_MIGRATION_BONUS]
- Support: [HELP_AVAILABLE]

### 10. METRICS & OPTIMIZATION

Pricing Health Metrics:
Conversion Metrics:
- Trial to paid: [CURRENT_%] → [TARGET_%]
- Tier mix: [FREE_%/PRO_%/ENT_%]
- Average selling price (ASP): [CURRENT] → [TARGET]
- Discount rate: [AVERAGE_%_DISCOUNT]

Revenue Metrics:
- ARPU: [CURRENT] → [TARGET]
- Customer LTV: [CURRENT] → [TARGET]
- LTV:CAC ratio: [CURRENT_RATIO] → [TARGET_3:1+]
- Expansion revenue: [%_OF_TOTAL]

Pricing Power:
- Price increase acceptance: [%_WHO_ACCEPT]
- Churn due to price: [%]
- Expansion rate: [%_UPSELL/CROSSSELL]
- Negotiation discount: [AVERAGE_%_OFF]

Review Cadence:
Monthly:
- Conversion rates by tier
- ARPU trends
- Discount analysis
- Win/loss by price objection

Quarterly:
- Pricing test results
- Competitive pricing moves
- Tier mix optimization
- Price increase analysis

Annually:
- Comprehensive pricing review
- Market positioning assessment
- Tier restructure consideration
- Major pricing changes

Optimization Opportunities:
- Opportunity 1: [WHAT_TO_TEST]
  - Hypothesis: [BELIEF]
  - Expected impact: [REVENUE_INCREASE]
  - Test plan: [APPROACH]

- Opportunity 2: [WHAT_TO_TEST]
  (Same structure)

### 11. PACKAGING EVOLUTION

Feature Release Pricing:
New Feature: [FEATURE_NAME]
- Value: [WHAT_IT_PROVIDES]
- Pricing decision:
  - Option A: Add to existing tier [WHICH_TIER]
  - Option B: Create new tier
  - Option C: Charge separately (add-on)
- Recommendation: [CHOICE]
- Rationale: [WHY]

Add-Ons & Modules:
Add-On: [MODULE_NAME]
- Price: [AMOUNT]
- Attach rate target: [%_OF_CUSTOMERS]
- Bundling strategy: [SEPARATE/BUNDLE_WITH]

Tier Evolution:
When to Add Tier:
- Signal: [CUSTOMER_REQUEST_PATTERN]
- Threshold: [WHEN_TO_DO_IT]
- Design: [HOW_TO_STRUCTURE]

When to Remove Tier:
- Signal: [LOW_ADOPTION_OR_CONFUSION]
- Migration: [HOW_TO_HANDLE]

### 12. INTERNATIONAL PRICING

Currency Strategy:
- Price in local currency: [YES/NO]
- Exchange rate handling: [FIXED/DYNAMIC]
- Payment methods: [OPTIONS_BY_REGION]

Regional Pricing:
Region: [GEOGRAPHY]
- Base price: [USD_EQUIVALENT]
- Local price: [LOCAL_CURRENCY]
- Purchasing power adjustment: [%_DIFFERENCE]
- Rationale: [WHY_THIS_PRICE]

Example:
- US: $100/month (base)
- Europe: €95/month (5% premium for VAT)
- India: $60/month (40% discount for purchasing power)

Price Parity Management:
- Risk: [ARBITRAGE_CONCERN]
- Mitigation: [GEOGRAPHIC_RESTRICTIONS]
```

## Variables

### PRODUCT_NAME
Your product.
**Examples:**
- "Team collaboration platform"
- "Mobile analytics app"
- "Enterprise data warehouse"

### TARGET_CUSTOMERS
Who you serve.
**Examples:**
- "SMB teams (10-50 employees)"
- "Consumer mobile users"
- "Enterprise data teams"

### VALUE_PROPOSITION
Core value you deliver.
**Examples:**
- "10x faster project planning with AI"
- "Understand your health through wearable data"
- "Query petabyte-scale data in seconds"

### PRICING_MODEL
How you charge.
**Examples:**
- "Freemium with per-user subscription tiers"
- "Usage-based on API calls"
- "Flat annual subscription"

### REVENUE_GOALS
Financial targets.
**Examples:**
- "$1M ARR in Year 1, $50K MRR"
- "$100K MRR, 15% free-to-paid conversion"
- "$10M ARR, $100K ACV target"

### COMPETITIVE_POSITION
Market positioning.
**Examples:**
- "Premium tier (+30% vs Asana)"
- "Value alternative (-40% vs Salesforce)"
- "Parity pricing to capture market share"

## Usage Examples

### Example 1: B2B SaaS Freemium
```
Product: Email marketing platform
Model: Freemium + tiered subscription
Free: 1,000 contacts, basic features
Pro: $29/month (up to 5,000 contacts)
Premium: $99/month (up to 25,000 contacts)
Enterprise: Custom (50K+ contacts, dedicated support)
Value Metric: Email contacts
Conversion: 10% free→paid target
Rationale: Freemium drives adoption, contacts scale with business growth
```

### Example 2: Infrastructure/Platform
```
Product: API platform
Model: Usage-based + base fee
Pricing: $99/month base + $0.01 per API call
Free Tier: 10,000 calls/month
Rationale: Aligns cost with value, fair for all sizes
Customers: Startups pay little, enterprises pay appropriately
```

### Example 3: Enterprise SaaS
```
Product: Customer data platform
Model: Annual contracts, custom pricing
Starting: $50K/year (up to 1M profiles)
$150K/year (up to 10M profiles)
$500K+/year (enterprise features, unlimited profiles)
Sales: Enterprise sales team, 6-month cycles
Rationale: High ACV justifies sales investment, pricing reflects value
```

### Example 4: Consumer Mobile App
```
Product: Premium meditation app
Model: Subscription
Monthly: $12.99/month
Annual: $69.99/year (55% savings vs monthly)
Free Trial: 7 days
Rationale: Low monthly for trial, annual for retention and cash flow
Conversion: 5% trial→paid target
```

## Best Practices

### Pricing Strategy
1. **Value-based pricing** - Price on value delivered, not cost
2. **Simple is better** - Easy to understand beats clever
3. **Grow with customer** - Value metric that scales
4. **Leave room to expand** - Upsell and expansion revenue
5. **Test continuously** - Pricing is never "done"

### Packaging
1. **3 tiers maximum** - More confuses buyers
2. **Middle tier sweet spot** - Most should choose this
3. **Clear differentiation** - Obvious value between tiers
4. **Anchor high** - Highest tier makes middle seem reasonable
5. **Features aligned to value** - Not arbitrary feature gates

### Testing & Optimization
1. **Test before launch** - Validate with customers
2. **Grandfather existing** - Protect current customers
3. **Monitor closely** - Daily metrics post-launch
4. **Iterate quarterly** - Regular optimization
5. **Don't race to bottom** - Compete on value not price

### Psychology
1. **Charm pricing** - $99 not $100 for SMB
2. **Annual discount** - 15-20% to improve retention
3. **Decoy pricing** - Middle tier looks like value
4. **Loss aversion** - Show what they'd lose
5. **Social proof** - "Most popular" tier

## Common Pitfalls

❌ **Cost-plus pricing** - Pricing based on costs not value
✅ Instead: Value-based pricing on customer ROI

❌ **Too many tiers** - 5+ tiers confuses buyers
✅ Instead: 3 tiers maximum (Free/Pro/Enterprise)

❌ **Pricing too low** - Fear of losing customers
✅ Instead: Price on value, test willingness to pay

❌ **Feature-based packaging** - Random features per tier
✅ Instead: Value-aligned packaging that makes sense

❌ **Never changing price** - Set and forget
✅ Instead: Regular testing and optimization

❌ **Complex pricing** - Requires calculator to understand
✅ Instead: Simple, transparent pricing

❌ **Scaling before PMF** - Perfect pricing without product-market fit
✅ Instead: Get PMF first, optimize pricing later

❌ **Ignoring competition** - Pricing in vacuum
✅ Instead: Understand competitive context

## Pricing Strategy Checklist

Strategy Development:
- [ ] Customer value quantified
- [ ] Willingness to pay researched
- [ ] Pricing model selected
- [ ] Value metric identified
- [ ] Competitive analysis complete
- [ ] Business objectives aligned

Packaging Design:
- [ ] Tier structure defined
- [ ] Features allocated to tiers
- [ ] Price points set
- [ ] Discount strategy established
- [ ] Annual/monthly options defined

Validation:
- [ ] Customer interviews conducted
- [ ] Price sensitivity tested
- [ ] Competitive positioning validated
- [ ] Unit economics modeled
- [ ] Sales team input gathered

Launch:
- [ ] Billing system configured
- [ ] Team trained
- [ ] Materials updated
- [ ] Communication plan ready
- [ ] Monitoring dashboard set up

Optimization:
- [ ] Metrics tracking
- [ ] Regular reviews scheduled
- [ ] A/B tests planned
- [ ] Quarterly optimization

---

**Last Updated:** 2025-11-12
**Category:** Product Management > Product Strategy
**Difficulty:** Advanced
**Estimated Time:** 2-4 weeks for initial strategy; ongoing optimization
