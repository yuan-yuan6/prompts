# Template Quality Checklist

**Version:** 1.0
**Last Updated:** 2025-11-12
**Purpose:** Ensure all templates meet quality standards before merging

---

## Overview

This checklist defines the **minimum quality standards** for all prompt templates in the database. Use this checklist when:
- Creating new templates
- Reviewing existing templates
- Conducting quarterly quality reviews
- Accepting community contributions

**Quality Philosophy:** Every template should be immediately usable, well-documented, and discoverable.

---

## Required Standards

### 1. YAML Frontmatter ✅

**All templates MUST have complete YAML frontmatter with required fields:**

```yaml
---
title: Clear, Descriptive Template Title
category: category/Subcategory (if applicable)
tags:
  - tag1  # 4-7 tags from standardized taxonomy
  - tag2
  - tag3
  - tag4
use_cases:
  - Specific use case description 1
  - Specific use case description 2
related_templates:
  - category/related-template-1.md  # Optional but recommended
  - category/subcategory/related-template-2.md
last_updated: YYYY-MM-DD
industries:  # Optional but recommended for cross-referencing
  - industry1
  - industry2
---
```

**Checklist:**
- [ ] YAML frontmatter present (delimited by `---`)
- [ ] `title` field present and descriptive
- [ ] `category` field matches file location
- [ ] `tags` field has 4-7 tags from [TAG_TAXONOMY.md](TAG_TAXONOMY.md)
- [ ] `use_cases` field has 2-5 specific use cases
- [ ] `related_templates` field present (if applicable)
- [ ] `last_updated` field in YYYY-MM-DD format
- [ ] `industries` field present for cross-industry templates
- [ ] All YAML syntax valid (no unquoted colons, proper indentation)

---

### 2. Template Structure ✅

**All templates MUST follow the standard structure:**

```markdown
---
[YAML Frontmatter]
---

# Template Title

## Purpose
Clear 1-2 sentence description of what this template does.

## Quick Start
**Minimal 3-step workflow with example:**
1. [First step with specific action]
2. [Second step with specific action]
3. [Third step with specific action]

## Template
[Full detailed prompt template with [VARIABLES]]

## Variables
| Variable | Description | Example |
|----------|-------------|---------|
| [VARIABLE_1] | What it represents | Example value |

## Usage Examples
### Example 1: [Specific Scenario]
[Concrete example]

## Customization Options (Optional)
[Adaptation guidance]

## Best Practices (Optional)
[Tips for optimal results]
```

**Checklist:**
- [ ] Template has clear **Purpose** section (1-2 sentences)
- [ ] Template has **Quick Start** section with 3-step workflow
- [ ] Template has **Template** section with full prompt
- [ ] Template has **Variables** table defining all placeholders
- [ ] Template has **Usage Examples** (minimum 2 examples)
- [ ] Template has **Customization Options** or **Best Practices** (recommended)
- [ ] All section headers use proper markdown (##, ###)
- [ ] Template is at least 100 lines (excluding frontmatter)

---

### 3. Content Quality ✅

**Template content MUST be:**

**Checklist:**
- [ ] **Clear:** Easy to understand for target audience
- [ ] **Specific:** Provides concrete guidance, not vague statements
- [ ] **Actionable:** Users can immediately apply it
- [ ] **Complete:** Contains all information needed
- [ ] **Accurate:** Technically correct and up-to-date
- [ ] **Professional:** Free of typos, grammar errors, formatting issues
- [ ] **Original:** Not copied from external sources without attribution
- [ ] **Variables Clearly Marked:** All placeholders in [BRACKETS] or {CURLY_BRACES}

---

### 4. Discoverability ✅

**Templates MUST be discoverable through multiple pathways:**

**Checklist:**
- [ ] **Category Placement:** In correct category per [CLASSIFICATION_GUIDE.md](CLASSIFICATION_GUIDE.md)
- [ ] **File Naming:** kebab-case filename matching content
- [ ] **Tags:** 4-7 relevant tags from [TAG_TAXONOMY.md](TAG_TAXONOMY.md)
- [ ] **Related Templates:** Links to 2-5 related templates
- [ ] **Industries:** Industry tags for cross-industry applicability
- [ ] **Use Cases:** Specific, searchable use case descriptions
- [ ] **Keywords:** Title and purpose contain key search terms

---

### 5. Technical Requirements ✅

**Templates MUST meet technical standards:**

**Checklist:**
- [ ] **Valid Markdown:** Renders correctly in markdown viewers
- [ ] **Valid YAML:** Passes YAML parsing (no syntax errors)
- [ ] **Working Links:** All `related_templates` links resolve correctly
- [ ] **Consistent Formatting:** Uses standard markdown formatting
- [ ] **No Broken References:** All internal references are valid
- [ ] **File Size:** Under 50KB (split large templates into parts)
- [ ] **Character Encoding:** UTF-8 encoding
- [ ] **Line Endings:** Unix-style line endings (LF, not CRLF)

---

### 6. Validation Requirements ✅

**Templates MUST pass automated validation:**

**Run validation:**
```bash
python3 scripts/validate_database.py
```

**Checklist:**
- [ ] **No YAML Errors:** Valid YAML syntax
- [ ] **No Missing Fields:** All required fields present
- [ ] **No Invalid Categories:** Category in approved list
- [ ] **No Invalid Tags:** All tags in standardized taxonomy
- [ ] **No Broken Links:** Related templates exist
- [ ] **No Warnings:** Address all validation warnings

---

## Quality Levels

### ⭐ Minimum (Required)
- Passes all Required Standards above
- Functionally complete
- Documented sufficiently

### ⭐⭐ Good (Target)
- Meets minimum standards
- Has 3+ usage examples
- Has customization options
- Has best practices section
- Links to 3+ related templates

### ⭐⭐⭐ Excellent (Aspirational)
- Meets good standards
- Has 5+ usage examples
- Has comprehensive best practices
- Has industry-specific guidance
- Has advanced customization options
- Links to 5+ related templates
- Has visual diagrams or examples

---

## Template Types

### Standard Template
- Single-file template
- 100-500 lines
- Complete in one file

**Checklist:**
- [ ] Follows standard structure
- [ ] Self-contained
- [ ] Complete documentation

### Comprehensive Framework
- Multi-part template series
- 500+ total lines
- Split into logical parts

**Checklist:**
- [ ] Has overview file
- [ ] Has 2-4 part files
- [ ] Parts follow naming: `template-name-01-section.md`
- [ ] Each part cross-references others
- [ ] Overview provides navigation

### Quick Reference Guide
- Concise, focused template
- 50-100 lines
- Rapid-use format

**Checklist:**
- [ ] Concise purpose statement
- [ ] Quick Start section prominent
- [ ] Minimal but complete
- [ ] Fast to scan and use

---

## Special Requirements

### Split Templates (Part Series)

When templates exceed 50KB or 500 lines, split into parts:

**Naming Convention:**
```
template-name-overview.md
template-name-01-section-name.md
template-name-02-section-name.md
template-name-03-section-name.md
```

**Checklist:**
- [ ] Overview file provides complete navigation
- [ ] Parts numbered sequentially (01, 02, 03)
- [ ] Each part cross-references others
- [ ] Part titles include section focus
- [ ] Overview has table of contents linking all parts

### Industry-Specific Templates

Templates specific to an industry:

**Checklist:**
- [ ] `industries` field lists relevant industries
- [ ] Title indicates industry if not obvious from category
- [ ] Examples use industry-specific scenarios
- [ ] Terminology appropriate for industry
- [ ] Related templates include other industry templates

---

## Review Process

### Pre-Submission Review

**Before submitting template:**
1. Complete this checklist
2. Run `python3 scripts/validate_database.py`
3. Preview markdown rendering
4. Test template with real use case
5. Get peer review (recommended)

### Quarterly Template Review

**Every 3 months, review templates for:**
1. **Accuracy:** Is content still current?
2. **Completeness:** Missing anything?
3. **Relevance:** Still addressing user needs?
4. **Quality:** Meets current standards?
5. **Update `last_updated` field if changes made**

---

## Common Issues & Fixes

### Issue: YAML Syntax Error
**Symptom:** Validation fails with YAML parse error
**Fix:** Quote titles containing colons:
```yaml
# Bad
title: Template - Part 1: Section Name

# Good
title: "Template - Part 1: Section Name"
```

### Issue: Broken Related Templates Links
**Symptom:** Validation warns about broken links
**Fix:** Use full path from repository root:
```yaml
# Bad
related_templates:
  - template-name.md

# Good
related_templates:
  - category/subcategory/template-name.md
```

### Issue: Invalid Category
**Symptom:** Validation fails with invalid category
**Fix:** Use approved category from [CLASSIFICATION_GUIDE.md](CLASSIFICATION_GUIDE.md)

### Issue: Too Many/Few Tags
**Symptom:** Discoverability issues
**Fix:** Use 4-7 tags from [TAG_TAXONOMY.md](TAG_TAXONOMY.md)

### Issue: Missing Use Cases
**Symptom:** Template not discoverable by use case
**Fix:** Add 2-5 specific, actionable use cases

---

## Template Versioning (Optional)

**Consider adding version tracking for major templates:**

```yaml
---
title: Template Name
version: 2.1
version_history:
  - version: 2.1
    date: 2025-11-12
    changes: Added Quick Start section, updated examples
  - version: 2.0
    date: 2025-01-15
    changes: Complete rewrite for function-first organization
  - version: 1.0
    date: 2024-06-01
    changes: Initial release
---
```

---

## Approval Criteria

**Template approved for merge when:**
- [ ] ✅ All Required Standards met
- [ ] ✅ Passes automated validation
- [ ] ✅ Peer reviewed (for significant templates)
- [ ] ✅ No unresolved feedback
- [ ] ✅ Quality level: Minimum (⭐) or higher

---

## Tools & Resources

### Validation Tools
- **`scripts/validate_database.py`** - Automated validation
- **`scripts/validate_links.py`** - Link checking
- **Markdown linter** - Check markdown syntax

### Reference Documentation
- **[CLASSIFICATION_GUIDE.md](CLASSIFICATION_GUIDE.md)** - Category placement rules
- **[TAG_TAXONOMY.md](TAG_TAXONOMY.md)** - Standardized tag list
- **[QUICK_START_TEMPLATE_GUIDE.md](QUICK_START_TEMPLATE_GUIDE.md)** - Template creation guide
- **[VERSION_SELECTION_GUIDE.md](VERSION_SELECTION_GUIDE.md)** - Choosing template types

### Example Templates
- **[strategy/risk-management.md](strategy/risk-management.md)** - ⭐⭐⭐ Excellent example
- **[data-analytics/dashboard-design-patterns.md](data-analytics/dashboard-design-patterns.md)** - ⭐⭐ Good example

---

## Maintenance

**This checklist should be reviewed quarterly:**
- Update standards based on feedback
- Add new requirements as database evolves
- Remove obsolete requirements
- Update examples

**Last Review:** 2025-11-12
**Next Review:** 2026-02-12
**Owner:** Database Architecture Team

---

## Quick Reference

**Minimum requirements to pass review:**
1. ✅ Valid YAML frontmatter (all required fields)
2. ✅ Standard structure (Purpose, Quick Start, Template, Variables, Examples)
3. ✅ 4-7 tags from standardized taxonomy
4. ✅ 2-5 use cases
5. ✅ 2+ usage examples
6. ✅ Variables table
7. ✅ Passes automated validation
8. ✅ No broken links
9. ✅ Professional quality content
10. ✅ Correct category placement

---

**For questions or feedback on quality standards, consult [CLASSIFICATION_GUIDE.md](CLASSIFICATION_GUIDE.md) or submit an issue.**
