# Template Classification Guide

**Purpose:** This guide provides clear rules and decision frameworks for classifying templates in the prompts repository, ensuring consistency as the repository grows.

**Last Updated:** 2025-11-11
**Version:** 2.0 - Function-First Classification System

---

## Classification Philosophy

This repository uses a **Function-First Classification System**, organizing templates primarily by **job function** rather than industry vertical. This approach:

✅ Aligns with how most users search ("I need a marketing template")
✅ Reduces duplication across industries
✅ Scales better as the repository grows
✅ Makes cross-industry patterns more discoverable

**Industry-specific context** is captured through:
- Tags in YAML frontmatter (`tags: [healthcare, finance, retail]`)
- Industry cross-reference views in INDEX.md
- Specialized categories for truly industry-unique functions (e.g., clinical-healthcare)

---

## Primary Classification System

### Top-Level Categories (Function-First)

| Category | Purpose | Example Templates |
|----------|---------|-------------------|
| **strategy** | Strategic planning, market analysis, competitive intelligence | Strategic planning, market research, competitive analysis |
| **operations** | Process management, quality assurance, project management | Project management, quality control, process optimization |
| **finance** | Financial planning, analysis, investment, risk management | Financial analysis, budgeting, investment evaluation, risk assessment |
| **sales-marketing** | Sales processes, marketing campaigns, customer engagement | Lead generation, campaign planning, customer engagement |
| **human-resources** | Recruitment, performance management, training, compensation | Hiring, performance reviews, training programs, compensation |
| **communication** | Internal, external, stakeholder, crisis communication | Internal comms, press releases, stakeholder management |
| **technology** | Software development, infrastructure, DevOps, cloud | Code review, architecture, CI/CD, cloud migration |
| **data-analytics** | Business intelligence, data science, analytics engineering | BI dashboards, predictive modeling, data pipelines |
| **security** | Cybersecurity, compliance, incident response, architecture | Security audit, incident response, threat intelligence |
| **design** | UX/UI design, product design, visual design | UX/UI design, product design, prototyping |
| **content-creation** | Writing, video, audio, multimedia content | Article writing, video production, podcast content |
| **media-journalism** | News production, investigative reporting, publishing | Investigative reporting, content strategy, publishing |
| **legal-compliance** | Contracts, regulatory, IP, governance | Contract drafting, regulatory compliance, IP management |
| **clinical-healthcare** | Medical, nursing, patient care (industry-specific) | Diagnosis, treatment planning, patient care |
| **education** | Teaching, research, curriculum, knowledge management | Course design, research papers, curriculum development |
| **personal** | Personal development, career, health, finance | Goal setting, career planning, personal finance |
| **government** | Policy, public services, civic engagement | Policy development, public services, citizen engagement |
| **nonprofit** | Fundraising, advocacy, program management | Grant writing, fundraising, program evaluation |

---

## Classification Decision Tree

Use this decision tree when classifying a new template:

```
START: What is the template's primary purpose?

1. Is it industry-specific and CANNOT be generalized?
   ├─ YES, Healthcare → /clinical-healthcare/
   ├─ YES, Government → /government/
   └─ NO → Continue to #2

2. What is the primary JOB FUNCTION?
   ├─ Strategic planning → /strategy/
   ├─ Process/project management → /operations/
   ├─ Financial analysis/planning → /finance/
   ├─ Sales or marketing → /sales-marketing/
   ├─ HR/people management → /human-resources/
   ├─ Internal/external communication → /communication/
   ├─ Software/infrastructure → /technology/
   ├─ Data analysis/ML → /data-analytics/
   ├─ Security/compliance → /security/
   ├─ Design (UX/product/visual) → /design/
   ├─ Content (articles/video/audio) → /content-creation/
   ├─ Journalism/news → /media-journalism/
   ├─ Legal/contracts → /legal-compliance/
   ├─ Teaching/research → /education/
   ├─ Personal development → /personal/
   └─ Nonprofit-specific → /nonprofit/

3. Is there a more specific SUBCATEGORY?
   Example: /finance/Investment-Management/
   Example: /technology/Software-Development/

4. Add INDUSTRY TAGS for cross-referencing:
   tags: [healthcare, finance, retail, manufacturing, etc.]
```

---

## Category Definitions

### /strategy/
**Purpose:** Templates for high-level strategic planning, market analysis, and competitive intelligence

**Includes:**
- Strategic planning and business planning
- Market research and analysis
- Competitive intelligence
- Growth strategy
- Innovation strategy
- Digital transformation strategy
- SWOT analysis, OKRs, strategic frameworks

**Excludes:**
- Operational planning → /operations/
- Financial strategy → /finance/
- Marketing strategy → /sales-marketing/
- HR strategy → /human-resources/

**Decision Rule:** If the template focuses on *setting organizational direction* rather than *executing specific functions*, it belongs here.

---

### /operations/
**Purpose:** Templates for process management, quality assurance, and project execution

**Includes:**
- Project management
- Process optimization
- Quality assurance and control
- Supply chain management
- Vendor management
- Risk management (operational)
- Change management
- Lean/Six Sigma implementations

**Excludes:**
- Software development processes → /technology/
- Financial operations → /finance/
- HR operations → /human-resources/

**Decision Rule:** If the template focuses on *how work gets done* and *process improvement*, it belongs here.

---

### /finance/
**Purpose:** Templates for financial planning, analysis, investment, and risk management

**Includes:**
- Financial analysis and modeling
- Budgeting and forecasting
- Investment evaluation and portfolio management
- Financial planning (corporate and wealth)
- Risk assessment and management
- Treasury management
- Audit and compliance (financial)
- Banking and insurance operations
- Economics and econometrics

**Excludes:**
- Personal finance → /personal/
- Fundraising → /nonprofit/
- Regulatory compliance (non-financial) → /legal-compliance/

**Decision Rule:** If the template's primary focus is *financial metrics, money management, or investment*, it belongs here.

---

### /sales-marketing/
**Purpose:** Templates for sales processes, marketing campaigns, and customer engagement

**Includes:**
- Marketing strategy and campaigns
- Ad copywriting and creative
- Brand development
- Lead generation and scoring
- Sales processes and enablement
- Customer engagement
- Social media marketing
- Email marketing
- Content marketing (promotional)
- Market research (customer-focused)

**Excludes:**
- Strategic market analysis → /strategy/
- Customer service operations → /operations/ or /communication/
- Content creation (non-promotional) → /content-creation/

**Decision Rule:** If the template's goal is *acquiring customers, generating revenue, or building brand*, it belongs here.

---

### /human-resources/
**Purpose:** Templates for recruitment, performance management, training, and compensation

**Includes:**
- Recruitment and hiring
- Onboarding
- Performance reviews and management
- Training and development
- Compensation and benefits
- Employee relations
- HR policies and procedures
- Talent management
- Succession planning

**Excludes:**
- Team communication → /communication/
- Leadership development → /personal/ or /operations/

**Decision Rule:** If the template focuses on *managing people as employees*, it belongs here.

---

### /communication/
**Purpose:** Templates for internal, external, stakeholder, and crisis communication

**Includes:**
- Internal communication (company announcements, policy communication)
- External communication (press releases, public statements)
- Stakeholder management (board reporting, investor relations)
- Crisis communication
- Change communication
- Team communication (status updates, meeting management)
- Customer communication (support, knowledge base)
- Public relations

**Excludes:**
- Marketing communication → /sales-marketing/
- Clinical communication → /clinical-healthcare/
- Technical documentation → /technology/

**Decision Rule:** If the template's primary purpose is *conveying information* rather than *selling, teaching, or documenting*, it belongs here.

---

### /technology/
**Purpose:** Templates for software development, infrastructure, DevOps, and cloud computing

**Includes:**
- Software development (code review, architecture, testing)
- DevOps and CI/CD
- Cloud architecture and migration
- Infrastructure as code
- Site reliability engineering
- API design
- Data engineering (infrastructure focus)
- AI/ML engineering (implementation focus)
- Emerging technologies (blockchain, IoT, quantum)

**Excludes:**
- Cybersecurity → /security/
- Data analysis/science → /data-analytics/
- Product design → /design/

**Decision Rule:** If the template focuses on *building, deploying, or maintaining technical systems*, it belongs here.

---

### /data-analytics/
**Purpose:** Templates for business intelligence, data science, and analytics engineering

**Includes:**
- Business intelligence and dashboards
- Data science and predictive modeling
- Analytics engineering (pipelines, quality, documentation)
- Machine learning (analysis focus)
- Statistical analysis
- Research analytics
- Experimental design
- Data visualization (analytical)
- KPI development

**Excludes:**
- Data engineering (infrastructure) → /technology/
- Financial analysis → /finance/
- Marketing analytics → /sales-marketing/

**Decision Rule:** If the template focuses on *deriving insights from data* rather than *building data infrastructure*, it belongs here.

---

### /security/
**Purpose:** Templates for cybersecurity, compliance, incident response, and security architecture

**Includes:**
- Cybersecurity operations
- Incident response and forensics
- Security assessment and audit
- Security architecture
- Threat intelligence
- Compliance management (security-related)
- Identity and access management
- Application security
- Cloud security
- Network security

**Excludes:**
- Non-security compliance → /legal-compliance/
- Data privacy (legal focus) → /legal-compliance/

**Decision Rule:** If the template focuses on *protecting systems, data, or networks from threats*, it belongs here.

---

### /design/
**Purpose:** Templates for UX/UI, product design, and visual design

**Includes:**
- UX/UI design
- Product design
- Graphic design
- Motion graphics
- 3D design
- Design systems
- Prototyping
- User research (design-focused)

**Excludes:**
- Marketing creative → /sales-marketing/
- Content design (articles, video) → /content-creation/
- Architecture design (software) → /technology/

**Decision Rule:** If the template focuses on *designing user experiences or visual artifacts*, it belongs here.

---

### /content-creation/
**Purpose:** Templates for creating articles, videos, audio, and multimedia content

**Includes:**
- Article writing
- Blog content
- Video production
- Podcast content
- Social media content (organic)
- Creative writing (non-fiction)
- Content strategy (editorial)
- Scriptwriting (non-entertainment)

**Excludes:**
- Marketing content → /sales-marketing/
- News/journalism → /media-journalism/
- Entertainment → /entertainment/ (if created)
- Technical writing → /technology/ or /education/

**Decision Rule:** If the template focuses on *creating informational or educational content*, it belongs here.

---

### /media-journalism/
**Purpose:** Templates for news production, investigative reporting, and digital publishing

**Includes:**
- Investigative reporting
- News production
- Digital publishing
- Content production strategy (news)
- Audience analytics (journalism)
- Podcasting strategy (news/journalism)
- Fact-checking and verification

**Excludes:**
- Content marketing → /sales-marketing/
- General content creation → /content-creation/
- Academic research → /education/

**Decision Rule:** If the template is specifically for *journalistic practices and news organizations*, it belongs here.

---

### /legal-compliance/
**Purpose:** Templates for contracts, regulatory compliance, IP, and governance

**Includes:**
- Contract drafting and management
- Regulatory compliance (non-financial)
- Intellectual property management
- Corporate governance
- Data privacy and GDPR
- Legal research
- Corporate legal operations

**Excludes:**
- Financial compliance → /finance/
- Security compliance → /security/
- HR policies → /human-resources/

**Decision Rule:** If the template focuses on *legal requirements, contracts, or regulatory obligations*, it belongs here.

---

### /clinical-healthcare/
**Purpose:** Templates for medical, nursing, and patient care (industry-specific exception)

**Includes:**
- Medical diagnosis
- Treatment planning
- Patient care plans
- Clinical documentation
- Telemedicine
- Medical research
- Clinical trials
- Healthcare operations (clinical)

**Excludes:**
- Healthcare IT → /technology/
- Healthcare analytics → /data-analytics/
- Healthcare administration (non-clinical) → /operations/

**Decision Rule:** This is an *industry-specific exception*. Healthcare clinical practice has unique requirements that don't generalize. Use this category when the template requires medical expertise.

---

### /education/
**Purpose:** Templates for teaching, academic research, curriculum, and knowledge management

**Includes:**
- Course design and curriculum development
- Lesson planning
- Academic research and publication
- Knowledge management
- Scientific communication
- Assessment design
- Online learning
- Educational technology

**Excludes:**
- Corporate training → /human-resources/
- Product documentation → /technology/
- Marketing education → /sales-marketing/

**Decision Rule:** If the template is for *formal education or academic research*, it belongs here.

---

### /personal/
**Purpose:** Templates for personal development, career, health, and personal finance

**Includes:**
- Goal setting and planning
- Career development
- Personal finance management
- Health and wellness (personal)
- Skill building
- Life planning
- Personal productivity
- Communication skills (personal development)

**Excludes:**
- Professional HR processes → /human-resources/
- Clinical health → /clinical-healthcare/
- Corporate finance → /finance/

**Decision Rule:** If the template is for *individual personal use* rather than organizational/professional use, it belongs here.

---

### /government/
**Purpose:** Templates for policy development, public services, and civic engagement

**Includes:**
- Policy development and research
- Public services design
- Civic engagement
- Government operations
- Legislative analysis
- Public administration

**Excludes:**
- Public communication → /communication/
- Public health → /clinical-healthcare/

**Decision Rule:** If the template is specifically for *government/public sector operations*, it belongs here.

---

### /nonprofit/
**Purpose:** Templates for fundraising, advocacy, and nonprofit program management

**Includes:**
- Fundraising and grant writing
- Donor relations
- Advocacy and campaigns
- Program management (nonprofit-specific)
- Impact measurement (nonprofit)
- Volunteer management
- Nonprofit governance

**Excludes:**
- General project management → /operations/
- General fundraising (for-profit) → /finance/

**Decision Rule:** If the template is specifically for *nonprofit organization operations*, it belongs here.

---

## Metadata Requirements

### Required YAML Frontmatter

Every template MUST include:

```yaml
---
category: [primary-category]/[optional-subcategory]
last_updated: YYYY-MM-DD
title: Clear, Descriptive Title
tags:
  - tag1
  - tag2
  - tag3
use_cases:
  - Use case description 1
  - Use case description 2
related_templates:
  - template-file-1.md
  - template-file-2.md
---
```

### Tagging Guidelines

**Function Tags:** Primary job function (even if not the category)
- strategy, operations, finance, sales, marketing, hr, communication, etc.

**Industry Tags:** Applicable industries
- healthcare, finance, retail, manufacturing, technology, education, etc.

**Technology Tags:** Specific technologies mentioned
- python, javascript, aws, kubernetes, tensorflow, etc.

**Content Type Tags:** Type of artifact produced
- documentation, template, framework, comprehensive, research, etc.

**Use Case Tags:** Specific scenarios
- startup, enterprise, remote-work, ai-ml, data-science, etc.

---

## Special Cases and Exceptions

### Cross-Functional Templates

**Problem:** Template applies to multiple functions equally (e.g., "remote work communication" involves communication + operations)

**Solution:**
1. Choose the PRIMARY function based on main purpose
2. Add secondary functions as tags
3. List in related_templates for cross-category discovery

**Example:**
```yaml
category: communication/Team-Communication
tags: [communication, operations, remote-work, collaboration]
```

---

### Industry-Specific vs. Industry-Tagged

**Use industry-specific category** (like /clinical-healthcare/) ONLY when:
1. The template requires specialized domain knowledge
2. The template cannot be generalized to other industries
3. The industry has unique regulatory/compliance requirements
4. The workflow is fundamentally different from other industries

**Use industry tags** for everything else:
```yaml
category: sales-marketing/Customer-Engagement
tags: [marketing, retail, ecommerce, customer-experience]
```

---

### Comprehensive vs. Quick Templates

**File naming:**
- Standard: `topic-name.md`
- Comprehensive: `topic-name-comprehensive.md`
- Framework: `topic-name-framework.md`
- Overview (for split prompts): `topic-name-overview.md`
- Parts (for split prompts): `topic-name-01-section.md`

**Category:** Use the same category for both versions, differentiate by filename and title

---

### Split Templates

For templates over 1,500 lines:

1. Create overview: `template-name-overview.md`
2. Create parts: `template-name-01-part.md`, `template-name-02-part.md`, etc.
3. Keep original: `template-name.md` (for those who want complete version)
4. All should share the same category
5. Overview should link to all parts

---

## Migration Rules

When reclassifying existing templates:

1. **Check related_templates:** Update all templates that reference the moved template
2. **Update INDEX.md:** Ensure the template appears in correct category views
3. **Update category README:** Add to new category, remove from old category
4. **Preserve git history:** Use `git mv` when possible
5. **Test links:** Verify all related_templates links still work
6. **Document in commit message:** Explain reason for reclassification

---

## Common Mistakes to Avoid

❌ **Mixing industry and function:** "Healthcare Marketing" should be `/sales-marketing/` with `tags: [healthcare]`, not `/clinical-healthcare/`

❌ **Over-nesting subcategories:** Keep hierarchy to 2 levels max: `/category/Subcategory/`

❌ **Vague categories:** "Business" and "Professional Services" are too vague - use specific functions

❌ **Technology-centric bias:** Don't put everything tech-related in `/technology/` - e.g., data science is `/data-analytics/`

❌ **Industry silos:** Don't create industry categories unless truly necessary (like clinical healthcare)

---

## Questions? Decision Framework

**Question:** "Where should template X go?"

**Answer:**
1. What is the PRIMARY job function? → That's probably the category
2. Is it truly industry-specific and cannot be generalized? → Consider industry category
3. When in doubt → Choose the function the END USER identifies with
4. Still unsure → Ask: "What job title would primarily use this?" → That's your category

---

## Review and Updates

This guide should be reviewed:
- ✅ Whenever adding a new top-level category
- ✅ When classification disputes arise
- ✅ Quarterly to ensure alignment with repository growth
- ✅ When user feedback suggests confusion

**Maintained by:** Repository administrators
**Last Major Revision:** 2025-11-11 (Function-First reorganization)
**Next Review:** 2026-02-11

---

**Questions or suggestions?** Open an issue or contact repository maintainers.
