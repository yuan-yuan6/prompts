# Prompt Repository Refactoring Guide

## Executive Summary

This guide documents the systematic refactoring approach for improving the usability of all 423 prompts in this repository. Based on comprehensive analysis, **only 1.7% of prompts currently meet quality standards**. This guide provides step-by-step instructions to bring all prompts to professional quality.

### Key Findings from Analysis
- **97% lack Quick Start sections** (398 of 411 prompts)
- **83% are too long** (over 400 lines)
- **79% have too many variables** (over 60 placeholders)
- **23% try to serve 3+ distinct use cases** (94 prompts need splitting)
- **Average prompt**: 694 lines with 262 variables (3-5x higher than optimal)

### Impact of Refactoring
**Before**: Overwhelming, difficult to use, low adoption
**After**: Clear, actionable, easy to start - 90%+ meet quality standards

---

## Table of Contents

1. [Refactoring Priorities](#refactoring-priorities)
2. [Adding Quick Start Sections](#adding-quick-start-sections)
3. [Splitting Complex Prompts](#splitting-complex-prompts)
4. [Simplifying Variable-Heavy Prompts](#simplifying-variable-heavy-prompts)
5. [Quality Standards](#quality-standards)
6. [Implementation Workflow](#implementation-workflow)
7. [Examples and Templates](#examples-and-templates)

---

## Refactoring Priorities

### Priority 1: Add Quick Start Sections (CRITICAL)
- **Target**: All 398 prompts missing Quick Start
- **Impact**: Immediate usability improvement
- **Time**: 5-10 minutes per prompt
- **Order**: Start with most frequently used categories
  1. technology/ (most used)
  2. business/ (high usage)
  3. creative/ (accessibility needed)
  4. data-analytics/ (complex, needs guidance)
  5. All remaining categories

### Priority 2: Split Multi-Use-Case Prompts (HIGH)
- **Target**: 63 prompts with 5+ use cases
- **Impact**: Transforms unusable prompts into focused, actionable ones
- **Time**: 2-4 hours per prompt split (creates 3-8 new prompts)
- **Order**: By use case count (highest first)
  - Top 10: 17-21 use cases each → Split into 8-12 focused prompts
  - Next 20: 7-12 use cases → Split into 5-8 focused prompts
  - Remaining: 5-6 use cases → Split into 3-5 focused prompts

### Priority 3: Simplify Variable-Heavy Prompts (MEDIUM)
- **Target**: 29 prompts with 500+ variables
- **Impact**: Makes prompts manageable and less overwhelming
- **Time**: 1-2 hours per prompt
- **Approach**: Group related variables, make some optional, provide defaults

---

## Adding Quick Start Sections

### Purpose
Quick Start sections allow users to immediately use a prompt without reading 400+ lines of documentation.

### Location
Place immediately after the `## Purpose` section, before `## Template` or `## Template Structure`.

### Required Format

```markdown
## Quick Start

**Need to [accomplish task] quickly?** Use this minimal example:

### Minimal Example
```
[Concrete, copy-paste-ready prompt with 3-5 key variables filled in with realistic examples]
```

### When to Use This
- [Specific scenario 1]
- [Specific scenario 2]
- [Specific scenario 3]

### Basic 3-Step Workflow
1. **[Action 1]** - [Brief one-sentence description]
2. **[Action 2]** - [Brief one-sentence description]
3. **[Action 3]** - [Brief one-sentence description]

**Time to complete**: [Realistic time estimate]

---
```

### Guidelines for Each Section

#### Minimal Example
- **Must be immediately usable** without customization
- Include **only 3-5 essential variables**
- Use **realistic, concrete values** (not "[specify value]")
- Should produce **useful output** on first try
- Keep to **3-5 lines** of text
- Can be a bullet list or paragraph

#### When to Use This
- List **3-5 specific scenarios**
- Be **concrete** not abstract
- Help users **self-select** if this prompt is right
- Start with verbs or specific situations

#### Basic Workflow
- **Exactly 3 steps** (not 2, not 4)
- Each step starts with an **action verb** (Define, Create, Analyze, etc.)
- Keep descriptions to **one sentence max**
- Focus on **what to do**, not explanations

#### Time Estimate
- Be **realistic** not aspirational
- Include setup/prep time
- Examples: "15-30 minutes", "2-3 hours", "1-2 days"

### Examples

#### Technology Prompt
```markdown
## Quick Start

**Need to generate code quickly?** Use this minimal example:

### Minimal Example
```
Generate a Python function that validates email addresses using regex. The function should:
- Accept an email string as input
- Return True if valid, False if invalid
- Handle edge cases (empty strings, special characters)
- Include docstring documentation and 3 unit tests with pytest
```

### When to Use This
- Creating new functions, classes, or modules from scratch
- Need production-ready code with tests and documentation
- Want to follow best practices and coding standards

### Basic 3-Step Workflow
1. **Specify requirements** - Define what the code should do and constraints
2. **Add context** - Mention language, framework, and key dependencies
3. **Request quality features** - Ask for tests, docs, and error handling

**Time to complete**: 5-15 minutes for functions, 30-60 minutes for classes

---
```

#### Business Prompt
```markdown
## Quick Start

**Need to create a business plan quickly?** Use this minimal example:

### Minimal Example
```
Create a business plan for a SaaS startup offering project management tools for small creative agencies. The company is pre-revenue, seeking $500K seed funding, targeting 50 customers in year one, and differentiating through design-first interface and agency-specific templates.
```

### When to Use This
- Creating business plans for funding or strategic direction
- Developing annual plans for existing divisions
- Planning new product launches or market entry

### Basic 3-Step Workflow
1. **Define core elements** - Company overview, market, and financial goals
2. **Develop strategy** - How you'll compete, grow, and succeed
3. **Create roadmap** - Timeline, milestones, and resource needs

**Time to complete**: 3-5 hours for focused plans, 1-2 days for comprehensive

---
```

---

## Splitting Complex Prompts

### When to Split a Prompt

Split a prompt if it meets **any** of these criteria:
- Has **5+ distinct use cases**
- Exceeds **1000 lines**
- Has **100+ sections** (headers)
- Tries to serve **different user personas**
- Covers **entire workflows** end-to-end

### Splitting Strategies

#### Strategy A: By Use Case
**When**: Prompt covers multiple distinct scenarios

**Process**:
1. Identify all distinct use cases (look at examples, customization sections)
2. Create separate prompt for each use case (typically 3-8 prompts)
3. Create lightweight overview/navigation prompt
4. Cross-link related prompts

**Example**: medical-diagnosis.md (21 use cases) →
- acute-care-diagnosis.md
- chronic-disease-diagnosis.md
- preventive-screening.md
- differential-diagnosis-complex-cases.md
- emergency-diagnosis.md
- + medical-diagnosis-overview.md (navigation)

#### Strategy B: By Workflow Stage
**When**: Prompt covers end-to-end process with distinct phases

**Process**:
1. Identify workflow stages
2. Create prompt for each stage (typically 4-6 prompts)
3. Ensure clear handoffs between stages
4. Create workflow overview prompt

**Example**: grant-writing.md →
- grant-opportunity-research.md
- grant-proposal-planning.md
- grant-narrative-writing.md
- grant-budget-development.md
- grant-review-submission.md
- + grant-writing-workflow-guide.md

#### Strategy C: By Depth Level
**When**: Users need different levels of detail

**Process**:
1. Create overview (navigation) prompt
2. Create quick-start/simple prompt
3. Create standard prompts for common cases
4. Create advanced prompts for complex cases

**Example**: dashboard-design →
- dashboard-design-overview.md (navigation)
- dashboard-quick-start.md (simple)
- dashboard-ux-design.md (standard)
- dashboard-technical-implementation.md (standard)
- dashboard-advanced-analytics.md (advanced)

#### Strategy D: By User Persona
**When**: Different users need different guidance

**Process**:
1. Identify primary user personas (typically 3-5)
2. Create role-specific prompts
3. Create overview for persona selection
4. Include persona-appropriate examples

**Example**: financial-planning.md →
- financial-planning-overview.md
- financial-planning-individuals.md
- financial-planning-small-business.md
- financial-planning-corporate.md
- financial-planning-nonprofit.md

### Creating the Overview/Navigation Prompt

When splitting a prompt, always create an overview prompt that helps users choose:

```markdown
# [Topic] Overview

## Purpose
Guide users to the appropriate [topic] prompt based on their specific needs.

## Available Prompts

### 1. [Focused Prompt Name]
**File:** `focused-prompt-name.md`

**Use this when:**
- [Specific scenario 1]
- [Specific scenario 2]
- [Specific scenario 3]

**Key features:**
- [Feature 1]
- [Feature 2]
- [Feature 3]

**Typical users:** [User types]
**Time investment:** [Time estimate]

---

[Repeat for each focused prompt...]

## Choosing the Right Prompt

Use this decision tree:
```
[Simple decision tree with 3-4 questions leading to specific prompts]
```

## Common Scenarios

| Your Need | Use This Prompt |
|-----------|----------------|
| [Scenario 1] | [Prompt A] |
| [Scenario 2] | [Prompt B] |
| [Scenario 3] | [Prompt C] |
```

### Splitting Checklist

Before committing a split:
- [ ] Each new prompt focuses on ONE specific use case/stage/persona
- [ ] Each new prompt is under 400 lines
- [ ] Each new prompt has under 60 variables
- [ ] Overview/navigation prompt created
- [ ] Cross-references updated in related prompts
- [ ] All new prompts have Quick Start sections
- [ ] File naming is consistent and clear
- [ ] Metadata (tags, related_templates) updated

---

## Simplifying Variable-Heavy Prompts

### Problem
Prompts with 100-500+ variables are overwhelming and unusable.

### Target
- Simple prompts: 10-30 variables
- Standard prompts: 30-60 variables
- Maximum: 60 variables (anything more needs splitting)

### Simplification Techniques

#### 1. Group Related Variables
Instead of:
```
- [SYMPTOM_1]
- [SYMPTOM_2]
- [SYMPTOM_3]
- [SYMPTOM_4]
- [SYMPTOM_5]
```

Use:
```
- [PRIMARY_SYMPTOMS] (e.g., "headache, fever, fatigue")
```

#### 2. Make Variables Optional
Mark non-essential variables as optional:
```
- [CORE_REQUIREMENT] **(required)**
- [NICE_TO_HAVE] *(optional, default: standard approach)*
```

#### 3. Provide Defaults
```
- [APPROACH] (default: agile methodology)
- [TIMELINE] (default: 3 months)
```

#### 4. Use Examples Instead of Variables
Instead of 50 variables for every field, provide a good example:
```
Provide project details similar to this example:
- Project: "Migrate legacy CRM to Salesforce"
- Timeline: "4 months"
- Team: "5 people (2 developers, 1 BA, 1 QA, 1 PM)"
- Budget: "$150K"
[Continue with fewer, essential variables...]
```

#### 5. Split If Still Too Complex
If you can't reduce below 60 variables, the prompt probably covers too much and needs splitting.

---

## Quality Standards

### Every Prompt Must Have:

1. **Quick Start Section** (after Purpose, before Template)
   - Minimal example (3-5 key variables)
   - When to Use (3-5 scenarios)
   - 3-step workflow
   - Time estimate

2. **Clear Purpose Statement** (1-2 sentences)
   - What the prompt does
   - Who it's for

3. **At Least One Complete Example**
   - Realistic scenario
   - Filled-in variables
   - Expected output described

4. **Best Practices Section** (5-10 tips)
   - Actionable advice
   - Common pitfalls to avoid

5. **Appropriate Length**
   - Action prompts: 200-500 lines
   - Overview prompts: 100-250 lines

6. **Manageable Variables**
   - 10-60 variables maximum
   - Clear descriptions
   - Realistic examples

7. **Proper Metadata**
   - Accurate tags
   - Related templates linked
   - Last updated date

### Quality Checklist

Before marking a prompt as "done":
- [ ] Has Quick Start section in correct location
- [ ] Quick Start has minimal example with 3-5 variables
- [ ] Quick Start has "When to Use" with 3-5 scenarios
- [ ] Quick Start has 3-step workflow
- [ ] Quick Start has realistic time estimate
- [ ] Under 500 lines (or is proper overview/navigation)
- [ ] Under 60 variables (or needs splitting)
- [ ] Has at least one complete example
- [ ] Has Best Practices section (5-10 tips)
- [ ] Purpose is clear (1-2 sentences)
- [ ] Metadata is accurate and complete
- [ ] Related templates are linked
- [ ] No obvious errors or placeholders

---

## Implementation Workflow

### For Individual Contributors

#### Adding Quick Starts (5-10 min per prompt)
1. Open prompt file
2. Find the `## Purpose` section
3. Add Quick Start section immediately after Purpose
4. Fill in all 4 required subsections
5. Add `---` separator
6. Verify against checklist
7. Commit with message: "Add Quick Start to [prompt-name]"

#### Splitting Prompts (2-4 hours per split)
1. Read full prompt to understand scope
2. Identify distinct use cases/stages/personas
3. Decide on splitting strategy
4. Create new files for each focused prompt
5. Write overview/navigation prompt
6. Add Quick Starts to all new prompts
7. Update cross-references
8. Commit with message: "Split [original-name] into [N] focused prompts"

#### Simplifying Variables (1-2 hours per prompt)
1. List all current variables
2. Group related variables
3. Mark optional variables
4. Provide defaults where possible
5. Rewrite prompt template with simplified variables
6. Update examples
7. Commit with message: "Simplify variables in [prompt-name] from [X] to [Y]"

### For Project Managers

#### Phase 1: Quick Wins (Week 1-2)
- Add Quick Starts to 50 most-used prompts
- Target: technology, business, creative categories
- Expected: Immediate usability improvement

#### Phase 2: Critical Splits (Week 3-4)
- Split top 10 multi-use-case prompts (17-21 use cases each)
- Creates 80-120 focused prompts from 10 bloated ones
- Expected: Major improvement in clarity

#### Phase 3: Category Refactoring (Week 5-8)
- Systematically refactor problem categories
  - data-analytics: 34 → 70 prompts
  - education: 37 → 80 prompts
  - professional-services: 43 → 90 prompts
- Expected: 90% of prompts meet standards

#### Phase 4: Polish & Complete (Week 9-12)
- Add Quick Starts to remaining prompts
- Simplify variable-heavy prompts
- Create automated validation
- Expected: 100% compliance

---

## Examples and Templates

### Quick Start Template
See `.templates/QUICK_START_TEMPLATE.md` for full template with examples.

### Prompts with Good Quick Starts (Reference These)
1. `/home/user/prompts/technology/Software Development/code-generation.md`
2. `/home/user/prompts/technology/AI & Machine Learning/prompt-engineering.md`
3. `/home/user/prompts/creative/Content Creation/article-writing.md`
4. `/home/user/prompts/business/Strategic Management/business-planning.md`
5. `/home/user/prompts/business/Sales & Marketing/market-research.md`
6. `/home/user/prompts/business/Operations & Processes/project-management.md`
7. `/home/user/prompts/personal/Personal Development/goal-setting.md`
8. `/home/user/prompts/data-analytics/Business Intelligence/report-generation.md`

### Overview/Navigation Prompts (Reference These)
1. `/home/user/prompts/healthcare/Clinical Practice/treatment-planning-overview.md`
2. `/home/user/prompts/data-analytics/Business Intelligence/dashboard-design-overview.md`

---

## Top Priorities: Prompts Requiring Immediate Attention

### Top 10 Most Critical (Split These First)

1. **medical-diagnosis.md** - 799 lines, 367 vars, **21 use cases**
   - Split by: diagnosis context (acute, chronic, preventive, emergency, etc.)
   - Creates: 8-10 focused prompts

2. **statistical-analysis.md** - 1,725 lines, 375 vars, **20 use cases**
   - Split by: analysis type (descriptive, inferential, regression, etc.)
   - Creates: 7 focused prompts

3. **risk-assessment.md** - 1,368 lines, 528 vars, **17 use cases**
   - Split by: risk type (market, credit, operational, etc.)
   - Creates: 6 focused prompts

4. **trading-portfolio-management.md** - 1,038 lines, 350 vars, **18 use cases**
   - Split by: investment strategy (value, growth, income, etc.)
   - Creates: 6 focused prompts

5. **lesson-planning.md** - 1,256 lines, 459 vars, **11 use cases**
   - Split by: subject area or education level
   - Creates: 6-8 focused prompts

6. **assessment-design.md** - 1,414 lines, 498 vars, **11 use cases**
   - Split by: assessment type (formative, summative, diagnostic, etc.)
   - Creates: 6 focused prompts

7. **process-automation-framework.md** - 730 lines, 456 vars, **9 use cases**
   - Split by: automation type or business function
   - Creates: 5-6 focused prompts

8. **academic-grant-writing.md** - 1,111 lines, 578 vars, **8 use cases**
   - Split by: workflow stage (research, planning, writing, budget, submission)
   - Creates: 5 focused prompts

9. **online-learning.md** - 1,764 lines, 670 vars, **8 use cases**
   - Split by: learning modality (synchronous, asynchronous, hybrid)
   - Creates: 6 focused prompts

10. **educational-content.md** - 1,346 lines, 449 vars, **7 use cases**
    - Split by: content type or education level
    - Creates: 5-7 focused prompts

### Analysis Data Files

Detailed analysis data available in `/tmp/`:
- `final_report.md` - Comprehensive analysis report
- `prompt_analysis.csv` - Sortable spreadsheet with all metrics
- `splitting_recommendations.md` - Detailed splitting strategies
- `prompt_analysis.json` - Raw data for all 411 prompts

---

## Success Metrics

### Target Outcomes (After Full Refactoring)

| Metric | Before | Target | Gap |
|--------|--------|--------|-----|
| Prompts meeting all criteria | 1.7% | 90% | +88.3% |
| Have Quick Start | 3% | 100% | +97% |
| Under 400 lines | 17% | 90% | +73% |
| Under 60 variables | 21% | 90% | +69% |
| Average lines per prompt | 694 | 300 | -57% |
| Average variables per prompt | 262 | 45 | -83% |

### User Experience

**Before Refactoring**:
- Overwhelming (400-1700 lines to read)
- Confusing (100-700 variables to fill)
- Slow to start (no quick examples)
- Low adoption

**After Refactoring**:
- Approachable (200-400 lines)
- Manageable (10-60 variables)
- Quick to start (copy-paste examples)
- High adoption

---

## Getting Help

### Questions?
1. Review examples of already-refactored prompts (listed above)
2. Check `.templates/QUICK_START_TEMPLATE.md`
3. Review analysis data in `/tmp/`
4. Consult this guide's examples

### Contributing
When refactoring prompts:
1. Follow this guide's standards
2. Use provided templates
3. Run quality checklist
4. Commit with clear messages
5. Link to this guide in PR description

---

**Last Updated**: 2025-11-10
**Analysis Date**: 2025-11-10
**Repository Status**: 423 prompts, 8 refactored, 415 remaining
