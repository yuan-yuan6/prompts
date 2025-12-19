---
category: education
related_templates:
- education/curriculum-development.md
- education/curriculum-development-framework.md
tags:
- wiki-systems
- knowledge-bases
- faq-documentation
- collaborative-platforms
- readiness-assessment
title: Documentation & Wikis Readiness Assessment
use_cases:
- Determining readiness to launch or overhaul a wiki/knowledge base/documentation system
- Identifying gaps in information architecture, content standards, governance, and platform UX
- Producing a concise blueprint and rollout plan for documentation programs
industries:
- education
- government
- technology
type: framework
difficulty: intermediate
slug: knowledge-documentation
---

# Documentation & Wikis Readiness Assessment

## Purpose
Assess whether you’re ready to implement or improve a documentation/wiki system by scoring six dimensions: Strategy & Audience, Information Architecture, Content Standards, Workflow & Governance, Platform & UX, and Operations & Measurement. Use this as a **go / revise-first** gate before building large volumes of pages.

## 🚀 Quick Assessment Prompt

> Assess **documentation/wiki readiness** for **{DOC_CONTEXT}** serving **{PRIMARY_USERS}** on **{PLATFORM_AND_CONSTRAINTS}**. Score each dimension 1–5 with brief evidence: (1) strategy & audience, (2) information architecture, (3) content standards & templates, (4) workflow & governance, (5) platform & UX/search, (6) operations & measurement. Provide an overall maturity level, a go/revise-first recommendation, top risks, and a prioritized 30–60 day rollout plan.

**Usage:** Replace the curly-brace placeholders with your specifics.

---

## Template

Conduct a documentation & wikis readiness assessment for {DOC_CONTEXT} serving {PRIMARY_USERS} on {PLATFORM_AND_CONSTRAINTS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. STRATEGY & AUDIENCE READINESS**
Evaluate whether the system has a clear purpose, boundaries, and audience. Confirm you can answer: what problems this solves, what content is in/out of scope, what “good” looks like (time-to-answer, ticket deflection, onboarding speed), and what adoption path exists.

**2. INFORMATION ARCHITECTURE READINESS**
Evaluate whether users will find information: top-level categories, taxonomy, tags, naming conventions, and cross-linking strategy. Confirm the structure matches user mental models and common journeys (onboarding, troubleshooting, policy lookup).

**3. CONTENT STANDARDS & TEMPLATES READINESS**
Evaluate whether content will be consistent and usable: page types (how-to, reference, tutorial, FAQ, policy), required sections, writing style, examples, and accessibility standards. Confirm you have templates, “definition of done,” and review criteria.

**4. WORKFLOW & GOVERNANCE READINESS**
Evaluate whether content can be created and maintained safely: roles (contributors/reviewers/approvers), review SLAs, versioning, change management, and decision rights. Confirm there’s a workable governance model that won’t block publishing or allow chaos.

**5. PLATFORM & UX/SEARCH READINESS**
Evaluate whether the chosen tool supports the needed UX: navigation, search quality, permissions, integrations (SSO, ticketing, repo links), analytics, and mobile. Confirm discoverability and findability are tested (search, synonyms, indexing, page titles).

**6. OPERATIONS & MEASUREMENT READINESS**
Evaluate whether the system is sustainable: ownership, content lifecycle (create → review → update → retire), maintenance cadence, feedback loops, and measurement (search success, engagement, content health). Confirm you can keep content current and improve based on data.

---

## Required Output Format

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, go/revise-first, top 3 risks

2. **DIMENSION SCORECARD** - Table: dimension, score (1–5), evidence, biggest gap, highest-impact fix

3. **ONE-PAGE BLUEPRINT**
- Purpose + scope (in/out)
- Primary user personas + top journeys
- IA sketch: top categories + tag strategy
- Content types + required templates
- Governance: roles, workflow, SLAs

4. **ROLL OUT PLAN (30–60 DAYS)**
- Phase 1 (week 1–2): foundation (IA, templates, governance)
- Phase 2 (week 3–4): seed content + pilot
- Phase 3 (week 5–8): scale + measurement loop

5. **RISKS & MITIGATIONS (TOP 5)** - Findability, ownership, staleness, permission complexity, contribution friction

---

## Maturity Scale (1–5)
- **1 — Initial:** No clear purpose/ownership; ad-hoc pages; low findability; high staleness risk.
- **2 — Developing:** Basic structure exists; inconsistent standards/workflows; weak search/navigation.
- **3 — Defined:** Coherent IA + templates + governance; ready for a pilot and seed content.
- **4 — Managed:** Reliable workflows; measurable outcomes; steady maintenance and adoption.
- **5 — Optimized:** Documentation is a product; continuous improvement; strong discoverability and high trust.

---

## Variables (Use Max 3)

| Variable | What to include | Example |
|---|---|---|
| `{DOC_CONTEXT}` | Org/project + domain + scope | “University IT services knowledge base (policies + how-tos)” |
| `{PRIMARY_USERS}` | Personas and needs | “Students, faculty, help desk agents; fast troubleshooting” |
| `{PLATFORM_AND_CONSTRAINTS}` | Platform + constraints | “Confluence with SSO; limited contributors; mobile-first” |

---

## Example (Filled)

**Input**
- `{DOC_CONTEXT}`: “Research lab wiki for onboarding + experiment SOPs.”
- `{PRIMARY_USERS}`: “New lab members and rotating students.”
- `{PLATFORM_AND_CONSTRAINTS}`: “Notion; must support permissioned pages; low admin time.”

**Output (abridged)**
- Executive summary: 3.1/5 (Defined), **go with a pilot**
- Biggest gaps: inconsistent page types; unclear review ownership; no content lifecycle
- Next actions (30 days): define 5 top categories + tag set; publish 4 templates (SOP, how-to, reference, FAQ); assign reviewer per category; seed 20 “golden path” pages; add monthly stale-content review and feedback intake

---

## Best Practices (8)

1. Design for user journeys (onboarding, troubleshooting), not departments.
2. Keep page types few and consistent; use templates and required sections.
3. Make findability a first-class feature: titles, tags, and cross-links.
4. Establish ownership and review SLAs to avoid staleness.
5. Start with seed content that covers top questions and pain points.
6. Build accessibility in (alt text, headings, readable structure).
7. Use analytics and feedback to drive the backlog.
8. Treat docs as a product: version, measure, iterate.

---

## Related Resources
- Curriculum structures and sequencing patterns: `curriculum-development.md`
- Program planning and rollout framing: `curriculum-development-framework.md`
