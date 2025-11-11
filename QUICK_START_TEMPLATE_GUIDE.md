# Quick Start Template Guide

**Purpose**: Standardized template for adding Quick Start sections to all prompts
**Target**: Every prompt should have a Quick Start section that enables 5-10 minute first use
**Last Updated**: November 10, 2025

---

## Why Quick Start Sections Matter

### The Problem Without Quick Start
- Users see 500+ line prompt
- Don't know where to begin
- Get overwhelmed and abandon
- Time-to-first-use: 30-60 minutes
- Completion rate: ~20%

### The Solution With Quick Start
- Users see clear 5-step process
- Get working result in 5-10 minutes
- Return for advanced features later
- Time-to-first-use: 5-10 minutes
- Completion rate: ~80%

---

## Quick Start Template

Copy and paste this template immediately after the "## Purpose" section in any prompt:

```markdown
## Quick Start

**Want to [achieve primary outcome] quickly?** Here's the minimal approach:

### When to Use This
- [Use case 1 - most common]
- [Use case 2 - second most common]
- [Use case 3 - third most common]

### Minimal Example
```
[Paste a real, working example with actual values filled in - not just [VARIABLE_NAME]]

Example for customer sentiment analysis:
- Data: 1,000 product reviews from e-commerce site
- Goal: Understand overall sentiment and top complaints
- Time period: Last 30 days
- Expected output: Sentiment distribution chart + top 10 issues
```

### Basic 3-5 Step Workflow
1. **[Action Verb] [What]** - [One sentence describing the step]
2. **[Action Verb] [What]** - [One sentence describing the step]
3. **[Action Verb] [What]** - [One sentence describing the step]
4. **[Action Verb] [What]** - [Optional: One sentence]
5. **[Action Verb] [What]** - [Optional: One sentence]

**Time to complete**: [X] minutes for basic use, [Y] minutes for advanced

**Pro tip**: [One actionable tip for best results]

---

[Rest of full template follows...]
```

---

## Examples by Prompt Type

### Example 1: Data Analytics Prompt (Text Analytics)

```markdown
## Quick Start

**Want to analyze customer sentiment quickly?** Here's the minimal approach:

### When to Use This
- You have customer reviews, feedback, or survey responses
- Need to understand overall sentiment (positive/negative/neutral)
- Want to identify key themes and topics
- Time-sensitive analysis required

### Minimal Example
```
Analyze 500 product reviews for our smartphone model X1000:
- Data source: CSV file with review_text and rating columns
- Goal: Understand why 2-star reviews are increasing
- Focus: Find specific product issues mentioned in negative reviews
- Output: Top 10 complaints with example quotes
```

### Basic 5-Step Workflow
1. **Load your data** - Import text data from CSV, database, or API
2. **Clean the text** - Remove HTML, URLs, special characters, normalize text
3. **Analyze sentiment** - Use VADER or transformer models for sentiment scoring
4. **Extract topics** - Apply LDA or BERTopic to find main themes (5-10 topics)
5. **Generate report** - Create visualizations showing sentiment distribution and top topics

**Time to complete**: 10 minutes for 1,000 reviews, 30 minutes for 100,000 reviews

**Pro tip**: Start with VADER for quick sentiment scoring, then use transformer models for nuanced analysis if needed.

---
```

### Example 2: Business Strategy Prompt (Strategic Planning)

```markdown
## Quick Start

**Want to create a strategic plan quickly?** Here's the minimal approach:

### When to Use This
- Starting annual or quarterly planning process
- Need to align team on strategic direction
- Preparing for board meeting or stakeholder presentation
- Responding to market changes or competitive threats

### Minimal Example
```
Create Q2 2025 strategic plan for mid-sized SaaS company:
- Current situation: 40% revenue growth but losing market share to competitors
- Key challenge: Feature parity with competitors while maintaining innovation
- Timeline: 90-day plan
- Stakeholders: Executive team, board of directors
- Desired outcome: Clear priorities, resource allocation, success metrics
```

### Basic 4-Step Workflow
1. **Assess current state** - Conduct SWOT analysis of current position (15 min)
2. **Define strategic objectives** - Set 3-5 key objectives for the period (20 min)
3. **Develop action plans** - Create specific initiatives with owners and timelines (30 min)
4. **Establish metrics** - Define KPIs to measure progress on each objective (15 min)

**Time to complete**: 90 minutes for basic plan, 4-6 hours for comprehensive plan

**Pro tip**: Focus on 3-5 strategic objectives maximum. More than 5 dilutes focus and reduces execution effectiveness.

---
```

### Example 3: Technology Prompt (API Design)

```markdown
## Quick Start

**Want to design a RESTful API quickly?** Here's the minimal approach:

### When to Use This
- Building new web service or microservice
- Exposing functionality to external developers
- Creating internal service-to-service communication
- Modernizing legacy system interfaces

### Minimal Example
```
Design REST API for e-commerce order management:
- Resources: Orders, Products, Customers
- Key operations: Create order, Get order status, Update order, Cancel order
- Authentication: OAuth 2.0 with JWT tokens
- Rate limiting: 1000 requests per hour per API key
- Response format: JSON
```

### Basic 5-Step Workflow
1. **Identify resources** - List main nouns/entities your API will expose (5 min)
2. **Define endpoints** - Map HTTP methods to operations (GET, POST, PUT, DELETE) (10 min)
3. **Design data models** - Specify request/response JSON schemas (15 min)
4. **Plan authentication** - Choose auth method and implement security (10 min)
5. **Document API** - Create OpenAPI/Swagger spec with examples (20 min)

**Time to complete**: 60 minutes for basic API, 3-4 hours for production-ready design

**Pro tip**: Use plural nouns for collections (e.g., /orders not /order) and HTTP status codes correctly (200, 201, 400, 404, 500).

---
```

### Example 4: Creative Prompt (Content Writing)

```markdown
## Quick Start

**Want to write engaging blog content quickly?** Here's the minimal approach:

### When to Use This
- Creating blog posts for company website
- Writing thought leadership articles
- Developing SEO-optimized content
- Producing regular content for content calendar

### Minimal Example
```
Write blog post about AI adoption in small businesses:
- Target audience: Small business owners (10-50 employees)
- Goal: Educate and inspire action on AI tools
- Tone: Friendly, practical, non-technical
- Length: 1,200 words
- SEO keywords: "AI for small business", "business automation", "AI tools 2025"
- Call-to-action: Download our AI readiness checklist
```

### Basic 4-Step Workflow
1. **Research topic** - Gather key points, statistics, examples (15 min)
2. **Create outline** - Structure with intro, 3-5 main sections, conclusion (10 min)
3. **Write first draft** - Focus on getting ideas down, don't self-edit yet (30 min)
4. **Edit and optimize** - Refine clarity, add SEO keywords, proofread (15 min)

**Time to complete**: 70 minutes for 1,200-word post, 2 hours for 2,500-word post

**Pro tip**: Start with a compelling hook in the first 2 sentences. If you don't grab attention immediately, readers won't continue.

---
```

### Example 5: Education Prompt (Course Design)

```markdown
## Quick Start

**Want to design an online course quickly?** Here's the minimal approach:

### When to Use This
- Creating new online course or training program
- Updating existing curriculum for online delivery
- Designing professional development workshops
- Building employee training modules

### Minimal Example
```
Design 4-week online course on "Data Analytics Fundamentals":
- Target audience: Business analysts with Excel experience, no coding background
- Learning objectives: Students can perform basic data analysis with Python and create visualizations
- Format: 2 hours of video + 3 hours of hands-on exercises per week
- Assessment: Weekly quizzes + final project analyzing real business data
- Platform: Learning Management System (LMS) with video hosting
```

### Basic 5-Step Workflow
1. **Define learning objectives** - What should students be able to DO after the course? (15 min)
2. **Outline content modules** - Break course into 4-8 logical modules (20 min)
3. **Design assessments** - Create quizzes, assignments, projects that test objectives (20 min)
4. **Plan delivery format** - Decide on videos, readings, exercises, discussions (15 min)
5. **Create course schedule** - Map modules to timeline with reasonable pacing (10 min)

**Time to complete**: 80 minutes for basic structure, 8-12 hours for detailed course design

**Pro tip**: Start with assessments and learning objectives, then work backwards to content. This ensures everything you teach directly supports what students need to achieve.

---
```

---

## Quick Start Checklist

When adding a Quick Start section, ensure it includes:

- [ ] **Clear headline** - "Want to [achieve outcome] quickly?"
- [ ] **When to Use This** - 3-4 common use cases (helps users identify relevance)
- [ ] **Minimal Example** - Real example with actual values (not [VARIABLE])
- [ ] **3-5 Step Workflow** - Action verbs, one sentence per step
- [ ] **Time estimate** - Realistic time for basic use + advanced use
- [ ] **Pro tip** - One actionable insight for better results
- [ ] **Separator** - Horizontal rule (---) before full template

---

## Common Mistakes to Avoid

### ❌ Don't: Use placeholders in minimal example
```
Bad: Analyze [NUMBER_OF_REVIEWS] reviews for [PRODUCT_NAME]
```

### ✅ Do: Use actual values
```
Good: Analyze 500 reviews for iPhone 15 Pro
```

### ❌ Don't: Make steps too vague
```
Bad: 1. Prepare your data
```

### ✅ Do: Be specific about the action
```
Good: 1. **Import your data** - Load CSV file with pandas or read from database
```

### ❌ Don't: Overload with options
```
Bad: Choose between VADER, TextBlob, BERT, RoBERTa, DistilBERT, or custom models
```

### ✅ Do: Recommend one best option
```
Good: Use VADER for quick results (good for social media, reviews)
```

### ❌ Don't: Set unrealistic time estimates
```
Bad: Time to complete: 5 minutes for comprehensive strategic plan
```

### ✅ Do: Be honest about time requirements
```
Good: Time to complete: 90 minutes for basic plan, 4-6 hours for comprehensive
```

---

## Testing Your Quick Start

### The 5-Minute Test
Ask someone unfamiliar with the prompt to:
1. Read only the Quick Start section (not the full prompt)
2. Try to complete the task using just the Quick Start guidance
3. Time how long it takes

**Success criteria:**
- ✅ They understand what the prompt does
- ✅ They know when to use it
- ✅ They can start using it without reading the full prompt
- ✅ They complete a basic version in 5-15 minutes

### The Clarity Test
Review your Quick Start and ask:
- Could a beginner understand this?
- Are the steps actionable (not just descriptive)?
- Is the example realistic and specific?
- Does the time estimate match reality?

---

## Implementation Strategy

### Priority Order for Adding Quick Starts:

**Phase 1 (Highest Impact)** - Week 1
1. All newly split prompts from mega-prompts (33 prompts)
2. Top 20 business/strategy prompts
3. Top 20 technology/development prompts

**Phase 2 (High Impact)** - Weeks 2-3
4. All data-analytics prompts (63 prompts)
5. All education prompts (49 prompts)
6. All creative prompts (46 prompts)

**Phase 3 (Completion)** - Month 2
7. Healthcare prompts (40 prompts)
8. Professional services (43 prompts)
9. Remaining categories (110 prompts)

### Tracking Progress
Use the IMPLEMENTATION_PROGRESS_TRACKER.md to track:
- Number of prompts with Quick Starts added
- Category completion percentages
- Quality check results
- User feedback (if available)

---

## Quick Start Variations by Prompt Complexity

### For Simple Prompts (< 300 lines)
- 3-step workflow
- 5-10 minute time estimate
- Minimal example only

### For Standard Prompts (300-600 lines)
- 4-5 step workflow
- 10-20 minute time estimate
- Minimal example + pro tip

### For Complex Prompts (600+ lines)
- 5-step workflow
- 20-30 minute time estimate
- Minimal example + pro tip + link to related simpler prompts

### For Technical/Code-Heavy Prompts
- Include code snippet in minimal example
- Reference specific libraries/tools to use
- Mention common pitfalls
- Link to documentation

---

## Measuring Success

### Before Quick Starts
- Average time-to-first-use: 30-60 minutes
- Completion rate: ~20%
- User feedback: "Don't know where to start"

### After Quick Starts (Target)
- Average time-to-first-use: 5-10 minutes
- Completion rate: ~80%
- User feedback: "Easy to get started, came back for more"

### Key Metrics to Track
1. **Time-to-First-Use** - How long from opening prompt to getting first result
2. **Completion Rate** - % of users who successfully use the prompt
3. **Return Rate** - % of users who use the prompt multiple times
4. **Advanced Feature Adoption** - % who explore beyond Quick Start
5. **User Satisfaction** - NPS or satisfaction scores

---

## Support and Questions

**For implementation questions:**
- Reference examples in this guide
- Check existing prompts with good Quick Starts (email-writing.md, prompt-engineering.md)
- Review FEASIBILITY_SUMMARY_ACTION_PLAN.md

**For quality review:**
- Use the 5-Minute Test
- Get peer review from colleague
- Test with user unfamiliar with the prompt

---

**Remember**: The goal is not to replace the comprehensive prompt, but to provide an onramp. Quick Start gets users their first win in 5-10 minutes, then they naturally explore advanced features.

Good luck adding Quick Starts! 🚀
