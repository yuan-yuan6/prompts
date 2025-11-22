# Canonical Taxonomy

This repository uses a structured taxonomy to ensure prompts are discoverable, maintainable, and correctly categorized.

## Core Categories

Use these slugs as the `category` in front-matter.

### Business Functions
- **`strategy`**: Corporate strategy, digital transformation, business model innovation.
- **`operations`**: Process optimization, supply chain, project management, daily ops.
- **`finance`**: Financial planning, analysis, accounting, investment, risk management.
- **`sales-marketing`**: Customer acquisition, branding, campaigns, sales processes.
- **`human-resources`**: Talent acquisition, employee development, culture, org design.
- **`legal-compliance`**: Contracts, regulatory adherence, corporate governance, IP.

### Technology, Data & Design
- **`ai-ml-applications`**: **PRIMARY HOME** for AI/ML. LLMs, RAG, agents, prompt engineering, MLOps.
- **`technology`**: Software engineering, DevOps, cloud infrastructure, cybersecurity, emerging tech.
- **`data-analytics`**: Business intelligence, data science (analysis), visualization, reporting.
- **`security`**: InfoSec, compliance governance, network security.
- **`design`**: UX/UI, graphic design, design systems, creative direction.
- **`product-management`**: Product strategy, roadmapping, user research, product lifecycle.

### Communication & Media
- **`communication`**: Internal/external comms, public relations, crisis management.
- **`content-creation`**: Writing, multimedia production, social media content.
- **`media-journalism`**: News reporting, editorial, investigative journalism.

### Education & Personal Growth
- **`education`**: Academic, corporate training, curriculum development.
- **`personal`**: Personal development, productivity, career growth.


---

## Semantic Boundaries & Decision Guide

When categories overlap, use these rules to decide where a prompt belongs.

### 1. AI & Machine Learning
**Rule:** All *production* AI/ML content goes in `ai-ml-applications`.
- **`ai-ml-applications`**: Building/deploying AI products, LLM apps, RAG, Agents.
- **`data-analytics`**: Using ML for *analysis* or *insights* (e.g., predictive modeling for a report).
- **`technology`**: Core infrastructure that supports AI (e.g., CUDA drivers, server provisioning) but not the AI application itself.

### 2. Data Engineering vs. Analytics
- **`data-analytics`**: For *analysts*. SQL queries, dashboards, KPI definitions, statistical analysis.
- **`technology/Data-Engineering`**: For *engineers*. Pipelines, ETL jobs, data warehouse architecture.

### 3. Product vs. Design
- **`product-management`**: The "What" and "Why". Strategy, requirements, roadmaps, metrics.
- **`design`**: The "How" (Visual/Interaction). Mockups, prototypes, style guides, user flows.

### 4. Communication vs. Marketing
- **`communication`**: Corporate voice, internal memos, PR, crisis response, stakeholder updates.
- **`sales-marketing`**: Revenue-focused. Lead gen, ad copy, campaign strategy, sales scripts.

### 5. Legal vs. Security
- **`legal-compliance`**: The *Law*. Contracts, privacy policies (text), regulatory filings.
- **`security`**: The *Implementation*. Audits, access controls, SOC2 technical controls.

---

## Metadata Guidelines

### Front-matter Format
```yaml
title: "Prompt Title"
category: ai-ml-applications  # Must be one of the Core Categories above
subcategory: LLM-Applications # Optional, CamelCase-Hyphenated
tags: [llm, python, architecture]
industry: [technology, finance] # Optional
last_updated: 2025-11-21
```

### Tags (Canonical List)
Prefer these tags to ensure searchability:
- **Types**: `template`, `framework`, `checklist`, `guide`
- **AI/ML**: `llm`, `rag`, `prompt-engineering`, `agents`, `nlp`, `gen-ai`
- **Business**: `strategy`, `startup`, `enterprise`, `kpi`, `okr`
- **Tech**: `python`, `javascript`, `cloud`, `api`, `architecture`
- **Data**: `analytics`, `sql`, `visualization`, `dashboard`

### Industries
Use the `industry` field for vertical-specific context, rather than creating new root categories.
- `technology`, `finance`, `healthcare`, `education`, `government`, `retail`, `manufacturing`, `nonprofit`, `media`

---

## Maintenance Notes
- **`government`**, **`healthcare`**, **`nonprofit`**, **`sustainability`** are NOT root categories. Use `industry` tags or subcategories within functional roots (e.g., `operations/Healthcare-Ops`).
- **`education`** IS a root category due to its distinct domain nature.
