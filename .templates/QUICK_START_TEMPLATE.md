# Quick Start Template for Prompts

This template should be added to EVERY prompt immediately after the "Purpose" or "Overview" section.

## Quick Start Template

```markdown
## Quick Start

**Need to get started quickly?** Use this minimal example:

### Minimal Example
[Provide a concrete, copy-paste-ready example with just the essential variables filled in]

```
[Specific prompt text with 3-5 key variables filled in with realistic examples]
```

### When to Use This
- [Specific scenario 1]
- [Specific scenario 2]
- [Specific scenario 3]

### Basic 3-Step Workflow
1. **[Action 1]** - [Brief description]
2. **[Action 2]** - [Brief description]
3. **[Action 3]** - [Brief description]

**Time to complete**: [Realistic time estimate]

---
```

## Guidelines

### Minimal Example
- Should be **immediately usable** without reading the full prompt
- Include **only 3-5 essential variables**
- Use **realistic, concrete examples** (not placeholders)
- Should produce **useful output** on first try

### When to Use This
- List **3-5 specific scenarios**
- Be **concrete** not abstract
- Help users **self-select** if this prompt is right for them

### Basic Workflow
- Exactly **3 steps** (not 2, not 4)
- Each step should be an **action verb**
- Keep descriptions to **one sentence max**
- Focus on **what to do**, not explanations

### Time Estimate
- Be **realistic** not aspirational
- Include setup time
- Example: "15-30 minutes" or "2-3 hours"

## Examples of Good Quick Starts

### Example 1: Technical Prompt
```markdown
## Quick Start

**Need to get started quickly?** Use this minimal example:

### Minimal Example
```
Design a REST API for a task management system with user authentication,
CRUD operations for tasks, and priority-based filtering. Use Node.js with
Express framework, implement JWT authentication, and include rate limiting.
```

### When to Use This
- Designing a new REST API from scratch
- Need to define API endpoints and data structures
- Planning authentication and authorization

### Basic 3-Step Workflow
1. **Define core resources** - Identify main entities (users, tasks, etc.)
2. **Design endpoints** - Map HTTP methods to CRUD operations
3. **Add security** - Implement authentication and authorization

**Time to complete**: 45-90 minutes

---
```

### Example 2: Business Prompt
```markdown
## Quick Start

**Need to get started quickly?** Use this minimal example:

### Minimal Example
```
Create a quarterly business review for a SaaS company with $2M ARR,
45% growth rate, focusing on customer acquisition cost ($450), churn rate (5%),
and expansion revenue. Target audience is the executive team and board of directors.
```

### When to Use This
- Preparing quarterly business reviews
- Need to communicate metrics to executives
- Analyzing SaaS business performance

### Basic 3-Step Workflow
1. **Gather key metrics** - Collect financial and operational data
2. **Identify trends** - Analyze performance vs. targets
3. **Create narrative** - Tell the story behind the numbers

**Time to complete**: 2-3 hours

---
```

### Example 3: Creative Prompt
```markdown
## Quick Start

**Need to get started quickly?** Use this minimal example:

### Minimal Example
```
Write a 500-word blog post about remote work best practices for software developers,
with a friendly and practical tone, targeting mid-level engineers. Include actionable
tips for maintaining work-life balance and staying productive.
```

### When to Use This
- Writing blog posts or articles quickly
- Need structured content with clear takeaways
- Targeting specific professional audiences

### Basic 3-Step Workflow
1. **Define topic and audience** - Be specific about who and what
2. **Outline key points** - List 3-5 main ideas to cover
3. **Generate draft** - Let AI create structured content

**Time to complete**: 15-30 minutes

---
```

## Implementation Priority

### Phase 1: Add to these categories first (highest impact)
1. technology/ - Most frequently used
2. business/ - High usage, complex topics
3. creative/ - Accessibility improvements needed
4. data-analytics/ - Complex prompts need quick starts

### Phase 2: Complete remaining categories
5. healthcare/
6. education/
7. finance/
8. professional-services/
9. industry/
10. personal/
11. nonprofit/
12. government/
13. security/

## Validation Checklist

Before committing a Quick Start section, verify:
- [ ] Minimal example is copy-paste ready
- [ ] Minimal example uses 3-5 variables (not 50+)
- [ ] "When to Use" has 3-5 specific scenarios
- [ ] Workflow has exactly 3 steps
- [ ] Time estimate is realistic
- [ ] Located immediately after Purpose/Overview
- [ ] Separated with `---` horizontal rule after
