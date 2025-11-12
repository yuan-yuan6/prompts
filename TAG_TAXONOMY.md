# Tag Taxonomy - Standardized Tag Set

**Last Updated:** 2025-11-12
**Version:** 2.0 (Post-Consolidation)
**Total Tags:** 60 standardized tags

---

## Overview

This document defines the **standardized tag set** for the prompts database. After comprehensive review and consolidation, we've reduced from 141 tags (66% single-use) to 60 carefully curated tags organized into clear categories.

**Key Principles:**
1. **No Single-Use Tags:** All tags must appear in ≥2 templates
2. **Clear Semantics:** Each tag has a specific, well-defined meaning
3. **No Redundancy:** Tags don't duplicate information from category or filename
4. **Cross-Cutting Value:** Tags enable discovery across categories

---

## Standardized Tag Categories

### 1. Function Tags (12 tags)

Core business functions and activities:

| Tag | Description | Use When |
|-----|-------------|----------|
| `strategy` | Strategic planning, analysis, positioning | Template involves high-level strategic thinking |
| `management` | Management processes, frameworks, leadership | Template supports management activities |
| `operations` | Operational processes, execution, efficiency | Template focuses on day-to-day operations |
| `development` | Building, creating, developing solutions | Template involves development work |
| `optimization` | Improving, enhancing, optimizing processes | Template focuses on making things better |
| `communication` | Communication strategies, messaging, engagement | Template involves stakeholder communication |
| `marketing` | Marketing campaigns, strategies, content | Template is marketing-focused |
| `automation` | Automated processes, workflows, tools | Template involves automation |
| `security` | Security measures, controls, protection | Template addresses security concerns |
| `testing` | Testing strategies, QA, validation | Template involves testing activities |
| `analysis` | Analytical processes, evaluation, assessment | Template focuses on analysis |
| `creative` | Creative work, design, ideation | Template involves creative activities |

---

### 2. Technology Tags (8 tags)

Technology domains and platforms:

| Tag | Description | Use When |
|-----|-------------|----------|
| `ai-ml` | AI, ML, data science, NLP, predictive modeling | Template involves AI/ML technologies |
| `data-analytics` | BI, analytics, data visualization, reporting | Template focuses on data analytics |
| `cloud` | Cloud computing, platforms, services | Template involves cloud technologies |
| `devops` | DevOps practices, CI/CD, deployment | Template addresses DevOps workflows |
| `infrastructure` | IT infrastructure, systems, architecture | Template involves infrastructure |
| `software-development` | Software engineering, coding, applications | Template is for software development |
| `api` | APIs, integrations, interfaces | Template involves API work |
| `database` | Database design, management, optimization | Template focuses on databases |

---

### 3. Industry Tags (12 tags)

Industry verticals for cross-referencing:

| Tag | Description | Examples |
|-----|-------------|----------|
| `healthcare` | Healthcare, clinical, medical | Clinical workflows, patient care |
| `finance` | Financial services, banking, investment | Financial analysis, risk management |
| `education` | Education, academic, teaching | Course design, research |
| `government` | Public sector, policy, civic | Policy development, public services |
| `nonprofit` | Nonprofit, charity, social sector | Fundraising, program management |
| `professional-services` | Consulting, legal, accounting | Client engagement, project delivery |
| `manufacturing` | Manufacturing, production, industrial | Production planning, quality control |
| `retail` | Retail, e-commerce, consumer | Customer experience, merchandising |
| `energy` | Energy, utilities, resources | Energy strategy, sustainability |
| `construction` | Construction, real estate, development | Project management, safety |
| `automotive` | Automotive industry | Vehicle development, supply chain |
| `agriculture` | Agriculture, farming, food production | Crop management, sustainability |

---

### 4. Content Type Tags (6 tags)

Template format and structure:

| Tag | Description | Use When |
|-----|-------------|----------|
| `template` | Standard prompt template | Template provides structured format |
| `framework` | Comprehensive multi-part framework | Template is extensive systematic framework |
| `guide` | Step-by-step guide or how-to | Template provides instructional guidance |
| `research` | Research methodologies, analysis | Template supports research work |
| `documentation` | Documentation creation, standards | Template helps create documentation |
| `implementation` | Implementation plans, rollout | Template focuses on implementation |

---

### 5. Use Case Tags (8 tags)

Context and application scenarios:

| Tag | Description | Use When |
|-----|-------------|----------|
| `personal` | Personal use, individual development | Template for individual users |
| `enterprise` | Large enterprise organizations | Template addresses enterprise scale |
| `startup` | Startups, early-stage companies | Template tailored for startups |
| `remote-work` | Remote work, distributed teams | Template for remote/hybrid work |
| `compliance` | Regulatory compliance, governance | Template addresses compliance needs |
| `crisis` | Crisis management, emergency response | Template for crisis situations |
| `innovation` | Innovation initiatives, R&D | Template supports innovation |
| `transformation` | Digital transformation, change management | Template for transformation initiatives |

---

### 6. Cross-Cutting Tags (14 tags)

Tags that span multiple categories:

| Tag | Description | Use When |
|-----|-------------|----------|
| `design` | Design processes, UX/UI, architecture | Template involves design work |
| `planning` | Planning activities, roadmaps | Template focuses on planning |
| `monitoring` | Monitoring, tracking, observability | Template involves monitoring |
| `reporting` | Reporting, dashboards, metrics | Template creates reports |
| `governance` | Governance structures, policies | Template addresses governance |
| `risk-management` | Risk assessment, mitigation | Template manages risk |
| `quality-assurance` | Quality control, standards | Template ensures quality |
| `collaboration` | Team collaboration, coordination | Template facilitates collaboration |
| `training` | Training programs, skill development | Template supports training |
| `metrics` | Metrics, KPIs, measurement | Template defines/tracks metrics |
| `visualization` | Data visualization, charts, graphics | Template creates visualizations |
| `integration` | System integration, connectivity | Template involves integration |
| `scalability` | Scaling systems, growth | Template addresses scalability |
| `accessibility` | Accessibility, inclusion | Template addresses accessibility |

---

## Tagging Guidelines

### Best Practices

1. **Use 4-7 Tags Per Template**
   - Minimum: 4 tags for basic discoverability
   - Recommended: 5-6 tags for optimal categorization
   - Maximum: 7 tags (avoid over-tagging)

2. **Tag Priority Order**
   1. Function tags (what it does)
   2. Technology/Industry tags (what domain)
   3. Content type (what format)
   4. Use case (what context)
   5. Cross-cutting (what additional attributes)

3. **Always Include:**
   - At least 1 function tag
   - At least 1 content type tag
   - Industry tags when applicable

4. **Avoid:**
   - Redundant tags (e.g., both `framework` and `template` when framework suffices)
   - Tags that duplicate category information
   - Overly specific tags with <2 uses

### Examples

**Good Tagging:**
```yaml
# data-analytics/dashboard-design-patterns.md
tags:
  - design
  - data-analytics
  - visualization
  - framework
  - enterprise
  - planning
```

**Bad Tagging:**
```yaml
# data-analytics/dashboard-design-patterns.md
tags:
  - data  # Too vague
  - dashboard  # Redundant with filename
  - comprehensive  # Redundant with content type
  - business  # Too generic
  - professional  # Too vague
  - industry  # Meta-tag, not descriptive
```

---

## Tag Validation

All templates must pass tag validation:

1. **All tags must be from standardized set**
2. **Minimum 4 tags, maximum 7 tags**
3. **At least 1 function tag**
4. **At least 1 content type tag**
5. **No duplicate tags**

Validation enforced by: `scripts/validate_database.py`

---

## Deprecated Tags

The following tags have been **removed/consolidated** and should NOT be used:

### Consolidated to `ai-ml`:
- `data-science` → `ai-ml`
- `machine-learning` → `ai-ml`
- `nlp` → `ai-ml`
- `sentiment-analysis` → `ai-ml`
- `emotion-detection` → `ai-ml`
- `causal-inference` → `ai-ml`

### Healthcare Specializations (use `healthcare` only):
- `telemedicine` → `healthcare`
- `public-health` → `healthcare`
- `clinical-practice` → `healthcare`
- `acute-care` → `healthcare`
- `critical-care` → `healthcare`
- `chronic-care` → `healthcare`
- `behavioral-health` → `healthcare`
- `mental-health` → `healthcare`
- `health-policy` → `healthcare`
- `health-education` → `healthcare`
- `epidemiology` → `healthcare`
- `community-health` → `healthcare`

### Content Type (removed as redundant):
- `comprehensive` → Remove (redundant with filename)
- `overview` → Remove (redundant with filename)

### Generic/Meta (removed as too vague):
- `business` → Remove (too generic)
- `industry` → Remove (meta-tag)
- `technology` → Remove (except in technology/ category)
- `navigation` → Remove
- `professional` → Remove (too vague)

---

## Migration Path

For templates using deprecated tags:

1. **AI/ML Tags:** Replace with `ai-ml`
2. **Healthcare Specializations:** Use only `healthcare`
3. **Content Type:** Remove `comprehensive`, `overview`
4. **Generic Tags:** Remove `business`, `industry`, etc.

### Automated Migration

Run consolidation scripts in order:

```bash
# Phase 1: AI/ML consolidation
python3 scripts/consolidate_aiml_tags.py

# Phase 2: Healthcare consolidation
python3 scripts/consolidate_healthcare_tags.py

# Phase 3: Remove redundant tags
python3 scripts/remove_redundant_tags.py

# Phase 4: Validate all templates
python3 scripts/validate_database.py
```

---

## Tag Statistics (Post-Consolidation)

| Category | Tag Count | Avg Uses per Tag |
|----------|-----------|------------------|
| Function | 12 | 35 |
| Technology | 8 | 42 |
| Industry | 12 | 18 |
| Content Type | 6 | 95 |
| Use Case | 8 | 22 |
| Cross-Cutting | 14 | 28 |
| **TOTAL** | **60** | **35** |

**Total Tag Instances:** ~2,100 (across 599 templates)
**Average Tags per Template:** 6.2
**Single-Use Tags:** 0 (0%)
**Tags Used 5+ Times:** 60 (100%)

---

## Maintenance

### Quarterly Review Process

1. **Analyze tag usage patterns**
   - Identify underused tags (<5 uses)
   - Identify overused tags that should be split
   - Check for emergent patterns

2. **Evaluate new tag requests**
   - Must have 10+ potential uses
   - Must not overlap with existing tags
   - Must provide clear cross-category value

3. **Update documentation**
   - Refresh usage examples
   - Update tag statistics
   - Document any changes

### Adding New Tags

**Requirements:**
- [ ] Tag has 10+ potential template uses
- [ ] Tag enables cross-category discovery
- [ ] Tag doesn't overlap with existing tags
- [ ] Tag has clear, specific definition
- [ ] Tag follows naming conventions (lowercase, hyphens)

**Process:**
1. Propose tag in `TAG_TAXONOMY.md` with justification
2. Get review approval
3. Add to `scripts/validate_database.py` allowed list
4. Apply to templates
5. Update statistics

---

## Related Documentation

- **CLASSIFICATION_GUIDE.md** - Category organization principles
- **scripts/validate_database.py** - Automated validation
- **INDEX.md** - Complete template catalog with tags
- **INDUSTRY_VIEW.md** - Industry-based browsing

---

## Version History

### Version 2.0 (2025-11-12)
- **Major consolidation:** 141 → 60 tags (57% reduction)
- Consolidated AI/ML tags (6 → 1)
- Consolidated healthcare specializations (13 → 1)
- Removed redundant content type tags
- Removed generic/meta tags
- Established tag validation standards
- **Result:** 0% single-use tags, 100% reusable

### Version 1.0 (2025-01-15)
- Initial tag taxonomy
- 141 tags identified
- 66% single-use tags (problematic)
- No formal standards

---

**Maintained by:** Database Architecture Team
**Review Frequency:** Quarterly
**Next Review:** 2026-02-12
