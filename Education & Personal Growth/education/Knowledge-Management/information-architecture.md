---
category: education
related_templates:
- education/curriculum-development.md
- education/curriculum-development-framework.md
tags:
- information-architecture
- taxonomy-design
- metadata-schemas
- knowledge-organization
- readiness-assessment
title: Information Architecture & Taxonomy Readiness Assessment
use_cases:
- Determining readiness to design or refactor information architecture (IA) and taxonomy
- Identifying gaps in user research, content modeling, metadata, navigation/search, and governance
- Producing an IA blueprint and an actionable 30–60 day plan
industries:
- education
- technology
type: framework
difficulty: intermediate
slug: information-architecture
---

# Information Architecture & Taxonomy Readiness Assessment

## Purpose
Assess whether you’re ready to design (or redesign) an information architecture and taxonomy by scoring six dimensions: Goals & Users, Content Inventory & Model, Taxonomy & Vocabulary, Metadata & Schemas, Navigation & Search, and Governance & Evolution. Use this as a **go / revise-first** gate before reorganizing content or rebuilding navigation.

## 🚀 Quick Prompt

> Assess **information architecture readiness** for **{IA_CONTEXT}** supporting **{PRIMARY_USER_JOURNEYS}** under **{SYSTEM_CONSTRAINTS}**. Score each dimension 1–5 with brief evidence: (1) goals & users, (2) content inventory & model, (3) taxonomy & vocabulary, (4) metadata & schemas, (5) navigation & search, (6) governance & evolution. Provide an overall maturity level, go/revise-first, top risks, and a prioritized 30–60 day IA plan.


---

## Template

Conduct an information architecture & taxonomy readiness assessment for {IA_CONTEXT} supporting {PRIMARY_USER_JOURNEYS} under {SYSTEM_CONSTRAINTS}.

Assess readiness across six dimensions, scoring each 1–5:

**1. GOALS & USERS READINESS**
Evaluate whether objectives and user needs are clear. Confirm personas, tasks, success metrics (findability, task completion time, search success), and the most important journeys.

**2. CONTENT INVENTORY & MODEL READINESS**
Evaluate whether you understand what content exists and how it behaves. Confirm a lightweight inventory (types, owners, freshness), content problems (duplication, gaps), and a content model (types + relationships) where needed.

**3. TAXONOMY & VOCABULARY READINESS**
Evaluate whether you can classify content in a user-centered way. Confirm top-level categories, facets, controlled vocabulary, synonyms, and rules for term creation and deprecation.

**4. METADATA & SCHEMAS READINESS**
Evaluate whether metadata supports discovery and governance. Confirm minimal required fields (title, summary, owner, last reviewed, audience, type), validation rules, and how metadata is captured/maintained.

**5. NAVIGATION & SEARCH READINESS**
Evaluate whether users can navigate and search successfully. Confirm navigation patterns (menus, breadcrumbs), filtering, search tuning, and testing approach (tree testing, first-click, query log review).

**6. GOVERNANCE & EVOLUTION READINESS**
Evaluate whether IA can be maintained. Confirm ownership, review cadence, change management, analytics loop, and how taxonomy/metadata updates are rolled out without breaking findability.

---

## Required Output Format

1. **EXECUTIVE SUMMARY** - Overall readiness score (X.X/5.0), maturity level, go/revise-first, top 3 risks

2. **DIMENSION SCORECARD** - Table: dimension, score (1–5), evidence, biggest gap, highest-impact fix

3. **IA BLUEPRINT (ONE PAGE)**
- Goals + key journeys
- Proposed top-level categories + 3–6 facets
- Metadata schema (minimum fields) + ownership
- Navigation approach + search strategy

4. **PLAN (30–60 DAYS)**
- Week 1–2: user needs + content inventory + baseline metrics
- Week 3–4: taxonomy/facets + metadata schema + prototypes
- Week 5–8: validation tests + iteration + rollout plan

5. **RISKS & MITIGATIONS (TOP 5)** - Broken findability, unclear ownership, weak metadata, taxonomy sprawl, insufficient testing

---

## Maturity Scale (1–5)
- **1 — Initial:** IA is ad-hoc; users rely on tribal knowledge; no governance.
- **2 — Developing:** Basic navigation exists; taxonomy/metadata inconsistent; limited validation.
- **3 — Defined:** Clear IA direction; inventory + taxonomy baseline; ready to test and pilot.
- **4 — Managed:** Evidence-based improvements; governed taxonomy/metadata; measurable gains.
- **5 — Optimized:** Continuous IA evolution; strong search + navigation; high confidence and low maintenance friction.

---

## Variables (Use Max 3)

| Variable | What to include | Example |
|---|---|---|
| `{IA_CONTEXT}` | System + domain | “Internal knowledge base for an engineering org” |
| `{PRIMARY_USER_JOURNEYS}` | Top tasks/journeys | “Onboarding, incident response, architecture decisions” |
| `{SYSTEM_CONSTRAINTS}` | Constraints | “Confluence; legacy category pages; SSO; limited dev time” |

---

## Example (Filled)

**Input**
- `{IA_CONTEXT}`: “Customer support help center for a SaaS product.”
- `{PRIMARY_USER_JOURNEYS}`: “Troubleshooting, billing questions, feature how-tos.”
- `{SYSTEM_CONSTRAINTS}`: “Zendesk; must preserve existing URLs; small content team.”

**Output (abridged)**
- Executive summary: 2.9/5 (Developing), **revise-first**
- Biggest gaps: no content inventory; taxonomy duplicates; metadata not maintained
- Next actions (30 days): inventory top 200 pages; define 5 top categories + facets (product area, issue type, audience, plan tier, last updated); add required fields (owner, last reviewed); run tree testing on proposed IA; adjust based on search logs; publish governance rules and rollout checklist

---

## Related Resources
- Curriculum sequencing patterns: `curriculum-development.md`
- Rollout framing and iteration: `curriculum-development-framework.md`
