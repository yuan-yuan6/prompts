---
title: Lead Scoring Criteria & Rules
category: business/Sales & Marketing/Lead Generation
tags: [business, marketing, scoring, criteria]
use_cases:
  - Defining scoring rules
  - Setting point values
  - Establishing criteria
related_templates:
  - lead-scoring-overview.md
  - lead-scoring-framework.md
last_updated: 2025-11-09
---

# Lead Scoring Criteria & Rules

## Purpose
Define specific scoring rules, point values, and criteria for demographic, firmographic, behavioral, and temporal factors in your lead scoring model.

## Template

```
Building on the framework established, create detailed scoring criteria for:

## 1. FIRMOGRAPHIC SCORING

Company Size (Weight: [COMPANY_SIZE_WEIGHT]%):
- Enterprise (>1000 employees): [ENTERPRISE_SIZE_POINTS] points
- Mid-market (251-1000 employees): [MID_MARKET_SIZE_POINTS] points
- SMB (51-250 employees): [SMB_SIZE_POINTS] points
- Small business (<50 employees): [SMALL_BIZ_SIZE_POINTS] points

Annual Revenue (Weight: [REVENUE_WEIGHT]%):
- $100M+: [LARGE_REVENUE_POINTS] points
- $50M-$100M: [MEDIUM_HIGH_REVENUE_POINTS] points
- $10M-$50M: [MEDIUM_REVENUE_POINTS] points
- $1M-$10M: [SMALL_MEDIUM_REVENUE_POINTS] points
- <$1M: [SMALL_REVENUE_POINTS] points

Industry Vertical (Weight: [INDUSTRY_WEIGHT]%):
- Primary target industry: [PRIMARY_INDUSTRY_POINTS] points
- Secondary target industry: [SECONDARY_INDUSTRY_POINTS] points
- Tertiary target industry: [TERTIARY_INDUSTRY_POINTS] points
- Non-target industry: [NON_TARGET_INDUSTRY_POINTS] points
- Restricted/excluded industry: [RESTRICTED_INDUSTRY_POINTS] points

Geographic Location (Weight: [GEOGRAPHY_WEIGHT]%):
- Primary market: [PRIMARY_GEO_POINTS] points
- Secondary market: [SECONDARY_GEO_POINTS] points
- International target: [INTERNATIONAL_POINTS] points
- Non-target geography: [NON_TARGET_GEO_POINTS] points

Technology Stack (Weight: [TECH_STACK_WEIGHT]%):
- Complementary technology: [COMPLEMENTARY_TECH_POINTS] points
- Competitive technology: [COMPETITIVE_TECH_POINTS] points
- Legacy systems: [LEGACY_SYSTEM_POINTS] points
- No relevant technology: [NO_TECH_POINTS] points

## 2. DEMOGRAPHIC SCORING

Job Title/Role (Weight: [JOB_TITLE_WEIGHT]%):
- C-Level executive: [C_LEVEL_POINTS] points
- VP/Director level: [VP_DIRECTOR_POINTS] points
- Manager level: [MANAGER_LEVEL_POINTS] points
- Individual contributor: [IC_LEVEL_POINTS] points
- Non-decision maker: [NON_DECISION_MAKER_POINTS] points

Department/Function (Weight: [DEPARTMENT_WEIGHT]%):
- Primary buying department: [PRIMARY_DEPT_POINTS] points
- Secondary buying department: [SECONDARY_DEPT_POINTS] points
- Influencer department: [INFLUENCER_DEPT_POINTS] points
- Non-relevant department: [NON_RELEVANT_DEPT_POINTS] points

Seniority Level (Weight: [SENIORITY_WEIGHT]%):
- Senior leadership: [SENIOR_LEADERSHIP_POINTS] points
- Middle management: [MIDDLE_MGMT_POINTS] points
- Junior level: [JUNIOR_LEVEL_POINTS] points
- Entry level: [ENTRY_LEVEL_POINTS] points

Budget Authority (Weight: [BUDGET_AUTHORITY_WEIGHT]%):
- Final decision maker: [FINAL_DECISION_POINTS] points
- Budget influencer: [BUDGET_INFLUENCER_POINTS] points
- Budget recommender: [BUDGET_RECOMMENDER_POINTS] points
- No budget authority: [NO_BUDGET_POINTS] points

Contact Information Quality (Weight: [CONTACT_QUALITY_WEIGHT]%):
- Complete business contact: [COMPLETE_CONTACT_POINTS] points
- Business email only: [BUSINESS_EMAIL_POINTS] points
- Personal contact info: [PERSONAL_CONTACT_POINTS] points
- Incomplete information: [INCOMPLETE_INFO_POINTS] points

## 3. BEHAVIORAL ENGAGEMENT SCORING

Website Engagement (Weight: [WEBSITE_ENGAGEMENT_WEIGHT]%):

Page Views:
- Homepage visits: [HOMEPAGE_VISIT_POINTS] points per visit
- Product/service pages: [PRODUCT_PAGE_POINTS] points per view
- Pricing page views: [PRICING_PAGE_POINTS] points per view
- Case study/testimonial views: [CASE_STUDY_POINTS] points per view
- Blog post engagement: [BLOG_POST_POINTS] points per read
- Resource downloads: [RESOURCE_DOWNLOAD_POINTS] points per download

Session Behavior:
- Time on site: [TIME_ON_SITE_POINTS] points per minute (cap: [TIME_ON_SITE_CAP] points)
- Pages per session: [PAGES_PER_SESSION_POINTS] points per page
- Return visitor: [RETURN_VISITOR_POINTS] points
- Direct traffic: [DIRECT_TRAFFIC_POINTS] points
- Referral traffic: [REFERRAL_TRAFFIC_POINTS] points

Form Interactions:
- Contact form submission: [CONTACT_FORM_POINTS] points
- Newsletter signup: [NEWSLETTER_SIGNUP_POINTS] points
- Demo request: [DEMO_REQUEST_POINTS] points
- Trial signup: [TRIAL_SIGNUP_POINTS] points
- Webinar registration: [WEBINAR_REGISTRATION_POINTS] points

Content Engagement (Weight: [CONTENT_ENGAGEMENT_WEIGHT]%):

Email Marketing:
- Email opens: [EMAIL_OPEN_POINTS] points per open
- Email clicks: [EMAIL_CLICK_POINTS] points per click
- Email forwards: [EMAIL_FORWARD_POINTS] points per forward
- Email replies: [EMAIL_REPLY_POINTS] points per reply
- Unsubscribes: [UNSUBSCRIBE_NEGATIVE_POINTS] points (negative)

Social Media:
- Social media follows: [SOCIAL_FOLLOW_POINTS] points per follow
- Social media shares: [SOCIAL_SHARE_POINTS] points per share
- Social media comments: [SOCIAL_COMMENT_POINTS] points per comment
- Social media mentions: [SOCIAL_MENTION_POINTS] points per mention
- LinkedIn profile views: [LINKEDIN_VIEW_POINTS] points per view

Content Consumption:
- Whitepaper downloads: [WHITEPAPER_POINTS] points per download
- Ebook downloads: [EBOOK_POINTS] points per download
- Video views: [VIDEO_VIEW_POINTS] points per view (>50% completion)
- Podcast subscriptions: [PODCAST_SUBSCRIPTION_POINTS] points
- Webinar attendance: [WEBINAR_ATTENDANCE_POINTS] points

Sales Interaction (Weight: [SALES_INTERACTION_WEIGHT]%):

Direct Communication:
- Phone calls answered: [PHONE_ANSWERED_POINTS] points per call
- Phone calls missed: [PHONE_MISSED_POINTS] points per call
- Voicemail responses: [VOICEMAIL_RESPONSE_POINTS] points
- Sales email responses: [SALES_EMAIL_RESPONSE_POINTS] points
- Meeting acceptances: [MEETING_ACCEPTANCE_POINTS] points

Meeting Engagement:
- Demo attendance: [DEMO_ATTENDANCE_POINTS] points
- Discovery call participation: [DISCOVERY_CALL_POINTS] points
- Proposal presentation attendance: [PROPOSAL_PRESENTATION_POINTS] points
- Multiple stakeholder meetings: [MULTI_STAKEHOLDER_POINTS] points
- Follow-up meeting scheduling: [FOLLOW_UP_MEETING_POINTS] points

Purchase Intent Indicators:
- Pricing inquiries: [PRICING_INQUIRY_POINTS] points
- Contract/terms requests: [CONTRACT_REQUEST_POINTS] points
- Implementation timeline discussions: [IMPLEMENTATION_TIMELINE_POINTS] points
- Budget confirmation: [BUDGET_CONFIRMATION_POINTS] points
- Reference requests: [REFERENCE_REQUEST_POINTS] points

## 4. LEAD SOURCE SCORING

Lead Source Scoring (Weight: [LEAD_SOURCE_WEIGHT]%):

Inbound Marketing:
- Organic search: [ORGANIC_SEARCH_POINTS] points
- Paid search (Google Ads): [PAID_SEARCH_POINTS] points
- Social media organic: [SOCIAL_ORGANIC_POINTS] points
- Social media paid: [SOCIAL_PAID_POINTS] points
- Content marketing: [CONTENT_MARKETING_POINTS] points
- SEO/organic traffic: [SEO_TRAFFIC_POINTS] points

Referral Sources:
- Customer referrals: [CUSTOMER_REFERRAL_POINTS] points
- Partner referrals: [PARTNER_REFERRAL_POINTS] points
- Employee referrals: [EMPLOYEE_REFERRAL_POINTS] points
- Industry referrals: [INDUSTRY_REFERRAL_POINTS] points
- Vendor referrals: [VENDOR_REFERRAL_POINTS] points

Direct Marketing:
- Email campaigns: [EMAIL_CAMPAIGN_POINTS] points
- Direct mail: [DIRECT_MAIL_POINTS] points
- Cold calling: [COLD_CALLING_POINTS] points
- LinkedIn outreach: [LINKEDIN_OUTREACH_POINTS] points
- Sales prospecting: [SALES_PROSPECTING_POINTS] points

Event Marketing:
- Trade shows: [TRADE_SHOW_POINTS] points
- Webinars: [WEBINAR_SOURCE_POINTS] points
- Conferences: [CONFERENCE_POINTS] points
- Networking events: [NETWORKING_EVENT_POINTS] points
- Speaking engagements: [SPEAKING_ENGAGEMENT_POINTS] points

## 5. TEMPORAL & FREQUENCY SCORING

Recency Scoring (Weight: [RECENCY_WEIGHT]%):

Activity Recency:
- Last 24 hours: [LAST_24_HOURS_POINTS] points
- Last 3 days: [LAST_3_DAYS_POINTS] points
- Last 7 days: [LAST_7_DAYS_POINTS] points
- Last 30 days: [LAST_30_DAYS_POINTS] points
- Last 90 days: [LAST_90_DAYS_POINTS] points
- Over 90 days: [OVER_90_DAYS_POINTS] points

Frequency Scoring (Weight: [FREQUENCY_WEIGHT]%):

Website Visit Frequency:
- Daily visits: [DAILY_VISITS_POINTS] points
- Weekly visits: [WEEKLY_VISITS_POINTS] points
- Monthly visits: [MONTHLY_VISITS_POINTS] points
- Sporadic visits: [SPORADIC_VISITS_POINTS] points
- Single visit: [SINGLE_VISIT_POINTS] points

Email Engagement Frequency:
- Consistent opener: [CONSISTENT_OPENER_POINTS] points
- Regular clicker: [REGULAR_CLICKER_POINTS] points
- Occasional engager: [OCCASIONAL_ENGAGER_POINTS] points
- Rare engager: [RARE_ENGAGER_POINTS] points
- Non-engager: [NON_ENGAGER_POINTS] points

Momentum Scoring (Weight: [MOMENTUM_WEIGHT]%):

Engagement Acceleration:
- Increasing engagement: [INCREASING_ENGAGEMENT_POINTS] points
- Consistent engagement: [CONSISTENT_ENGAGEMENT_POINTS] points
- Decreasing engagement: [DECREASING_ENGAGEMENT_POINTS] points
- Sporadic engagement: [SPORADIC_ENGAGEMENT_POINTS] points
- Dormant engagement: [DORMANT_ENGAGEMENT_POINTS] points

## 6. NEGATIVE SCORING

Company Disqualifiers (Weight: [COMPANY_DISQUALIFIER_WEIGHT]%):
- Competitor company: [COMPETITOR_NEGATIVE_POINTS] points
- Restricted industry: [RESTRICTED_INDUSTRY_NEGATIVE] points
- Insufficient budget: [INSUFFICIENT_BUDGET_NEGATIVE] points
- Wrong company size: [WRONG_SIZE_NEGATIVE] points
- Geographic restrictions: [GEO_RESTRICTION_NEGATIVE] points
- Blacklisted domain: [BLACKLISTED_DOMAIN_NEGATIVE] points

Contact Quality Issues:
- Personal email domain: [PERSONAL_EMAIL_NEGATIVE] points
- Incomplete contact information: [INCOMPLETE_CONTACT_NEGATIVE] points
- Unverified email address: [UNVERIFIED_EMAIL_NEGATIVE] points
- Bounced email addresses: [BOUNCED_EMAIL_NEGATIVE] points
- Role-based email (info@, admin@): [ROLE_EMAIL_NEGATIVE] points

Behavioral Red Flags:
- Multiple email unsubscribes: [UNSUBSCRIBE_NEGATIVE] points
- Spam complaints: [SPAM_COMPLAINT_NEGATIVE] points
- Repeated no-shows: [NO_SHOW_NEGATIVE] points
- Rude/inappropriate behavior: [INAPPROPRIATE_BEHAVIOR_NEGATIVE] points
- Unrealistic timeline: [UNREALISTIC_TIMELINE_NEGATIVE] points

Please provide specific point values for each criterion based on your business model and historical data.
```

## Best Practices

1. **Base on Data**: Use historical conversion data to inform point values
2. **Test Incrementally**: Start with key criteria and add complexity
3. **Involve Sales**: Get sales team input on criteria importance
4. **Balance Weights**: Ensure total weights equal 100%
5. **Include Negatives**: Don't forget disqualification criteria
6. **Set Caps**: Limit maximum points from any single activity
7. **Review Regularly**: Update criteria quarterly based on performance
8. **Document Logic**: Maintain clear documentation of all rules

---

*This template helps you build comprehensive, data-driven scoring criteria that accurately predict lead quality and conversion probability.*
