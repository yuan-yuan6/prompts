# CLAUDE.md - AI Assistant Guide for Prompt Template Library

This document provides guidance for AI assistants working with this repository.

## Project Overview

This is a **Prompt Template Library** containing **456 production-ready AI prompt templates** across professional domains. Each template is a Markdown file with YAML front-matter metadata, designed for business, technical, creative, and specialized use cases.

**Repository Purpose:** Centralized, searchable collection of vetted, reusable prompt templates for various industries and functions.

## Repository Structure

```
/prompts/
├── Business Functions/           # Core business operations
│   ├── finance/                  # 31 templates - Financial planning, analysis, investment
│   ├── human-resources/          # 14 templates - Recruitment, performance, training
│   ├── legal-compliance/         # 19 templates - Contracts, regulatory, IP
│   ├── operations/               # 39 templates - Project mgmt, supply chain, manufacturing
│   ├── sales-marketing/          # 38 templates - Sales, campaigns, branding
│   └── strategy/                 # 12 templates - Strategic planning, market analysis
│
├── Communication & Media/        # External and internal communications
│   ├── communication/            # 33 templates - PR, crisis, stakeholder comms
│   ├── content-creation/         # 25 templates - Writing, multimedia, social
│   └── media-journalism/         # 9 templates - Reporting, editorial
│
├── Education & Personal Growth/  # Learning and development
│   ├── education/                # 29 templates - Academic, curriculum, training
│   └── personal/                 # 25 templates - Career, productivity, wellness
│
├── Technology, Data & Design/    # Technical domains
│   ├── ai-ml-applications/       # 17 templates - LLMs, RAG, agents, MLOps
│   ├── data-analytics/           # 71 templates - BI, data science, visualization
│   ├── design/                   # 14 templates - UX/UI, graphic design
│   ├── product-management/       # 15 templates - Product strategy, roadmaps
│   ├── security/                 # 20 templates - Cybersecurity, compliance
│   └── technology/               # 45 templates - Software dev, DevOps, cloud
│
├── tools/                        # Utility scripts
│   └── fix_metadata.py           # Auto-fill missing metadata fields
│
├── .templates/                   # Template planning documents (internal)
├── .github/workflows/            # CI/CD validation
│
├── README.md                     # Main library documentation
├── CONTRIBUTING.md               # Contributor guidelines
├── TAXONOMY.md                   # Category definitions and decision guide
├── STRUCTURAL_ANALYSIS.md        # Architecture analysis and recommendations
├── INDEX.md                      # Auto-generated searchable index
└── category_report.json          # Statistics and category distribution
```

## Template Structure

Every template follows this standardized Markdown structure:

### Required YAML Front-Matter

```yaml
---
title: "Template Name"
category: category-slug              # From TAXONOMY.md (e.g., ai-ml-applications)
last_updated: YYYY-MM-DD             # ISO date format
tags: [tag1, tag2, tag3]             # Canonical tags from taxonomy.json
use_cases:                           # Specific use case descriptions
  - "Use case 1"
  - "Use case 2"
type: template                       # template|framework|generator|comprehensive
difficulty: intermediate             # quick|intermediate|comprehensive
slug: unique-identifier              # File stem, auto-generated if missing
---
```

**Optional fields:** `industries`, `related_templates`, `subcategory`

### Required Content Sections

```markdown
# Template Name

## Purpose
[1-2 sentence description of what this template does]

## Quick Start

### Minimal Example
[Copy-paste ready example]

### When to Use This
[3-5 specific scenarios]

### Basic N-Step Workflow
[Sequential actions]

## Template
[Full prompt text with [VARIABLE_NAME] placeholders]

## Variables
### VARIABLE_NAME
[Definition and examples]

## Usage Examples
[2-5 real-world examples with filled variables]

## Best Practices
[Tips for optimal results]
```

### Variable Naming Convention

- Use `[VARIABLE_NAME]` format with square brackets
- UPPERCASE_WITH_UNDERSCORES for clarity
- Examples: `[COMPANY_NAME]`, `[PROJECT_TYPE]`, `[TARGET_AUDIENCE]`

## Development Workflow

### Setting Up Environment

```bash
# Create virtual environment and install dependencies
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh

# Activate environment
source .venv/bin/activate
```

### Validation Commands

```bash
# Validate all template metadata
./.venv/bin/python3 scripts/lint_metadata.py

# Generate INDEX.md and statistics
./.venv/bin/python3 scripts/generate_index.py

# Check for broken inter-template links
./.venv/bin/python3 scripts/link_validator.py

# Fix missing metadata fields (type, difficulty, slug)
python tools/fix_metadata.py

# Apply category mapping changes
./.venv/bin/python3 scripts/apply_category_mapping.py --report
```

### CI/CD Pipeline

On push to `main` or `claude/**` branches:
1. Runs `scripts/validate_database.py`
2. Validates YAML front-matter
3. Checks required fields: `title`, `category`, `last_updated`
4. Reports issues/warnings in `validation_report.txt`

## 17 Core Categories (Taxonomy)

Use these slugs in the `category` field:

| Category | Description |
|----------|-------------|
| `strategy` | Corporate strategy, digital transformation, business model |
| `operations` | Process optimization, supply chain, project management |
| `finance` | Financial planning, analysis, accounting, investment |
| `sales-marketing` | Customer acquisition, branding, campaigns |
| `human-resources` | Talent acquisition, employee development |
| `legal-compliance` | Contracts, regulatory adherence, IP |
| `ai-ml-applications` | **PRIMARY** for AI/ML: LLMs, RAG, agents, MLOps |
| `technology` | Software engineering, DevOps, cloud, infrastructure |
| `data-analytics` | BI, data science (analysis), visualization |
| `security` | InfoSec, compliance governance, network security |
| `design` | UX/UI, graphic design, design systems |
| `product-management` | Product strategy, roadmapping, user research |
| `communication` | Internal/external comms, PR, crisis management |
| `content-creation` | Writing, multimedia production, social media |
| `media-journalism` | News reporting, editorial, investigative |
| `education` | Academic, corporate training, curriculum |
| `personal` | Personal development, productivity, career growth |

### Category Decision Rules

- **AI/ML content** → `ai-ml-applications` (not `technology` or `data-analytics`)
- **Data engineering** → `technology/Data-Engineering` (pipelines, ETL)
- **Data analysis** → `data-analytics` (SQL, dashboards, statistics)
- **Product "what/why"** → `product-management`
- **Design "how"** → `design`
- **Corporate voice** → `communication`
- **Revenue-focused** → `sales-marketing`

## Common Tasks

### Creating a New Template

1. Create file in appropriate category directory
2. Use kebab-case naming: `new-template-name.md`
3. Add required YAML front-matter with `title`, `category`, `last_updated`
4. Follow the standard content structure
5. Run `scripts/lint_metadata.py` to validate
6. Run `scripts/generate_index.py` to update INDEX.md

### Updating an Existing Template

1. Update the `last_updated` field to current date
2. Preserve all existing sections
3. Run validation after changes

### Multi-Part Templates

For comprehensive templates split across files:
- Use `-01`, `-02`, `-03` suffix: `topic-01-foundation.md`, `topic-02-advanced.md`
- Create an overview file: `topic-overview.md`

### Adding a New Category

1. Update `scripts/taxonomy.json` with new category
2. Update `TAXONOMY.md` documentation
3. Create category directory with `README.md`
4. Submit PR with justification

## Quality Standards

### Required for All Templates

- Clear purpose statement
- Well-defined variables with examples
- At least 2 usage examples
- Proper YAML front-matter
- Valid Markdown formatting

### File Naming

- Use **kebab-case**: `strategic-planning.md`
- Avoid spaces or special characters
- Use descriptive, specific names
- Multi-part templates: `topic-01-section.md`

### Directory Naming

- Categories: kebab-case (`ai-ml-applications`)
- Subcategories: CamelCase-Hyphenated (`LLM-Applications`, `Data-Engineering`)

## Key Files Reference

| File | Purpose |
|------|---------|
| `README.md` | Library overview and quick start |
| `CONTRIBUTING.md` | How to contribute |
| `TAXONOMY.md` | Category definitions and decision guide |
| `STRUCTURAL_ANALYSIS.md` | Architecture analysis |
| `INDEX.md` | Auto-generated template index |
| `category_report.json` | Category statistics |
| `scripts/taxonomy.json` | Canonical tags/categories |
| `.github/workflows/validate.yml` | CI validation config |

## Common Issues and Fixes

### YAML Parsing Errors

- Quote titles containing colons: `title: "Strategy: Implementation Guide"`
- Use `|` for multiline values
- Ensure proper indentation

### Linter Failures

- Missing required fields: Add `title`, `category`, `last_updated`
- Non-canonical tags: Use tags from `scripts/taxonomy.json`
- Run `python tools/fix_metadata.py` to auto-fill `type`, `difficulty`, `slug`

### Category Confusion

- Refer to `TAXONOMY.md` for semantic boundaries
- AI/ML applications → `ai-ml-applications` (not scattered)
- Industry-specific → use `industries` field, not new root categories

## Tips for AI Assistants

1. **Always validate** - Run `lint_metadata.py` after creating/editing templates
2. **Check taxonomy** - Reference `TAXONOMY.md` before assigning categories
3. **Follow structure** - Use the standard template sections
4. **Update dates** - Set `last_updated` to current date on edits
5. **Be specific** - Templates should have clear, actionable content
6. **Use variables** - Employ `[VARIABLE_NAME]` format consistently
7. **Add examples** - Include practical, real-world usage examples
8. **Link related** - Use `related_templates` field for connections
9. **Generate index** - Run `generate_index.py` after adding templates
10. **Check links** - Run `link_validator.py` to verify inter-template links

---

**Last Updated:** 2025-11-22
**Templates:** 456 production-ready
**Categories:** 17 core taxonomy
**Maintained by:** yuan-yuan6
