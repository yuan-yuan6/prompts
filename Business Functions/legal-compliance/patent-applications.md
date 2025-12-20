---
category: legal-compliance
title: Patent Application Readiness Assessment
tags:
- patent-applications
- claims-drafting
- prior-art
- patent-prosecution
- readiness-assessment
use_cases:
- Assessing readiness to draft and file a patent application with a defensible claim strategy
- Identifying gaps in invention disclosure quality, prior art coverage, and prosecution planning
- Producing an application plan, claims outline, and filing roadmap with clear owners and timelines
related_templates:
- legal-compliance/intellectual-property-management.md
- legal-compliance/regulatory-compliance-management.md
- legal-compliance/corporate-contract-management.md
industries:
- education
- finance
- government
- healthcare
- manufacturing
- retail
- technology
type: framework
difficulty: intermediate
slug: patent-application-readiness-assessment
---

# Patent Application Readiness Assessment

## Purpose
Assess readiness to draft and file a patent application across six dimensions: Invention Disclosure, Prior Art & Patentability, Claim Strategy, Specification & Drawings, Filing & Prosecution Strategy, and Governance & Business Alignment. Identify gaps, prioritize fixes, and produce an application package plan.

## 🚀 Quick Prompt

> Assess **patent application readiness** for **[INVENTION]** in **[TECH_FIELD]** targeting **[JURISDICTIONS]** with desired scope **[PROTECTION_GOAL]**. Evaluate across: (1) **Invention disclosure**—is the invention described clearly with alternatives and implementation details? (2) **Prior art & patentability**—is there a reasonable search and novelty/non-obviousness story? (3) **Claim strategy**—are independent and dependent claim themes defined with fallbacks? (4) **Specification & drawings**—is there sufficient written description and enablement, with figure plan tied to claims? (5) **Filing/prosecution**—is there a roadmap (provisional/PCT/national) with timelines and cost constraints? (6) **Governance & alignment**—are inventorship, ownership, and publication timing controlled and aligned to product strategy? Provide a 1–5 scorecard, top gaps, and a filing-ready plan.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid readiness evaluation.

---

## Template

Conduct a patent application readiness assessment for {INVENTION} in {TECH_FIELD} targeting {JURISDICTIONS} to achieve {PROTECTION_GOAL}.

Assess readiness across six dimensions, scoring each 1–5:

**1. INVENTION DISCLOSURE READINESS**
- Problem statement and technical solution are clearly articulated
- Novel features are enumerated (what is new vs current solutions)
- Embodiments and alternatives are described (avoid single-point disclosures)
- Implementation details exist (data flows, components, parameters, constraints)
- Inventor contributions and dates are documented

**2. PRIOR ART & PATENTABILITY READINESS**
- Prior art search scope is reasonable for the space
- Key references are summarized with claim-relevant differences
- Novelty is plausible for the core concepts
- Non-obviousness theory is articulated (technical effect, unexpected results, teaching away)
- Potential §101/eligibility risks (if applicable) are identified and mitigations considered

**3. CLAIM STRATEGY READINESS**
- Clear claim themes exist (system/method/CRM as applicable)
- At least one broad independent claim concept is defined
- Dependent claim set provides meaningful fallback positions
- Definitions and terminology are consistent (avoid self-inflicted narrowness)
- Competitive design-around risks are considered and addressed with variants

**4. SPECIFICATION & DRAWINGS READINESS**
- Written description supports the planned claim breadth
- Enablement is credible (how to make and use; not just high-level concepts)
- Figure plan exists and maps to claim elements
- Examples and implementation variants are included (edge cases, optional components)
- Consistency checks planned (terms, numerals, cross-references)

**5. FILING & PROSECUTION STRATEGY READINESS**
- Filing approach chosen (provisional vs non-provisional vs PCT) with rationale
- Jurisdiction priorities reflect business needs and budget constraints
- Publication strategy is aligned (defensive publication vs secrecy)
- Prosecution plan exists (office action response posture, continuations/divisionals)
- Freedom-to-operate considerations are scoped (if needed) separately from patentability

**6. GOVERNANCE & BUSINESS ALIGNMENT READINESS**
- Inventorship and assignment/ownership are clear
- Confidentiality and disclosure controls exist (publications, demos, customer materials)
- Counsel handoff is clear (what is provided, timelines, decision points)
- Portfolio alignment exists (how this filing fits the broader IP strategy)
- Post-filing maintenance expectations are understood (fees, pruning, continuation strategy)

Deliver your assessment as:

1. **EXECUTIVE SUMMARY** - Overall score, maturity level, top 3 gaps
2. **DIMENSION SCORECARD** - Table with score (X.X/5) and key finding per dimension
3. **DISCLOSURE CHECKLIST** - Missing inputs needed to draft filing-ready materials
4. **CLAIM OUTLINE** - Broad claim concept + fallback dependent themes
5. **FIGURE PLAN** - List of figures mapped to claim elements
6. **FILING ROADMAP** - Timeline and jurisdiction plan (incl. costs at a high level)

Use this maturity scale:
- 1.0-1.9: Initial (insufficient disclosure; high risk of narrow/invalid claims)
- 2.0-2.9: Developing (basic disclosure; gaps in prior art, claim fallbacks, enablement)
- 3.0-3.9: Defined (solid disclosure and strategy; manageable drafting risks)
- 4.0-4.9: Managed (strong support, clear fallbacks, disciplined filing plan)
- 5.0: Optimized (high-quality drafting inputs, efficient prosecution posture, portfolio fit)

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[INVENTION]` | Invention name | "Adaptive anomaly detection for streaming telemetry" |
| `[TECH_FIELD]` | Technology field | "ML + observability" |
| `[JURISDICTIONS]` | Target jurisdictions | "US + PCT" |
| `[PROTECTION_GOAL]` | Desired protection scope | "Broad coverage of method + system variants" |

## Example

**Software/AI - Utility Filing**

> Assess patent application readiness for **Adaptive anomaly detection for streaming telemetry** in **ML + observability** targeting **US + PCT** to achieve **broad coverage of method + system variants**. Disclosure describes the core method but lacks alternative embodiments and parameter ranges; prior art search is thin for adjacent telemetry/forecasting work; claim themes exist but dependent fallbacks are not planned; specification needs enablement detail for training/inference and edge cases; filing approach is unclear (provisional vs non-provisional first); inventorship and publication timing need confirmation before any marketing launch. Provide scorecard, a disclosure checklist, a claim outline, and a filing roadmap.

