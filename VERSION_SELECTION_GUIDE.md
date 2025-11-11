# Version Selection Guide

## Choosing the Right Prompt Template for Your Needs

This repository contains multiple versions of many prompt templates—from quick-start versions to comprehensive frameworks. This guide helps you choose the right version for your situation.

---

## 📋 Template Version Types

### 1. **Standard Templates** (~400-800 lines)
**When to use**: Most common use cases, balanced depth

**Characteristics**:
- Complete template with all essential variables
- Quick Start section for rapid implementation
- Real-world usage examples
- Customization options
- Typical completion time: 30-60 minutes

**Best for**:
- First-time users of the template
- Standard projects with typical requirements
- When you need guidance but not exhaustive detail
- Time-sensitive projects

**Example templates**:
- `lead-generation.md`
- `market-research.md`
- `project-management.md`

---

### 2. **Comprehensive Templates** (~1000-1800 lines)
**When to use**: Complex projects requiring extensive detail

**Characteristics**:
- In-depth framework with 100+ variables
- Multiple methodology options
- Advanced customization sections
- Extensive examples across industries
- Detailed best practices
- Typical completion time: 2-4 hours

**Best for**:
- Large-scale strategic initiatives
- Enterprise-level projects
- When stakeholder buy-in requires thorough documentation
- Learning a domain in depth
- Projects with high complexity or risk

**Example templates**:
- `strategic-digital-transformation-roadmap.md`
- `ad-copy-comprehensive.md`
- `ux-ui-design-comprehensive.md`

**Recognition**: Files ending in `-comprehensive.md`

---

### 3. **Split/Modular Templates** (Multiple files, 300-500 lines each)
**When to use**: Need flexibility to use specific modules independently

**Characteristics**:
- Large topics broken into focused sub-prompts
- Overview file provides navigation
- Each module is independently usable
- Easier to digest than one massive file
- Can mix-and-match modules

**Best for**:
- Teams working on different aspects of a project
- When you only need specific components
- Phased implementation (use modules sequentially)
- Learning complex topics incrementally

**Example sets**:
- `generative-ai-implementation-01-foundation.md`
- `generative-ai-implementation-02-technical.md`
- `generative-ai-implementation-03-governance.md`
- `generative-ai-implementation-overview.md` (navigation)

**Recognition**: Files with `-01-`, `-02-`, `-03-` suffixes + `-overview.md`

---

## 🎯 Decision Framework

Use this flowchart to select the right version:

```
START: What is your project scope and experience level?

┌─────────────────────────────────────────┐
│  Are you NEW to this topic?            │
│  OR need quick results (<1 hour)?      │
└──────────┬──────────────────────────────┘
           │
           ├── YES → Use STANDARD template
           │         • Includes Quick Start
           │         • Balanced detail
           │         • Real examples included
           │
           └── NO (experienced + time available)
                     │
                     ▼
           ┌─────────────────────────────────────┐
           │  Is this a LARGE, COMPLEX project?  │
           │  (Enterprise-scale, high-stakes)    │
           └──────────┬────────────────────────────┘
                      │
                      ├── YES → Use COMPREHENSIVE template
                      │         • 100+ variables
                      │         • Extensive examples
                      │         • Advanced options
                      │
                      └── NO → Use STANDARD template
                                (Unless you need modular approach)
                                      │
                                      ▼
                      ┌─────────────────────────────────────┐
                      │  Will MULTIPLE people work on this? │
                      │  OR need to implement in PHASES?    │
                      └──────────┬────────────────────────────┘
                                 │
                                 ├── YES → Use SPLIT/MODULAR templates
                                 │         • Each person takes a module
                                 │         • Implement phase-by-phase
                                 │
                                 └── NO → Stick with STANDARD template
```

---

## 📊 Quick Comparison Table

| Criteria | Standard | Comprehensive | Split/Modular |
|----------|----------|---------------|---------------|
| **Length** | 400-800 lines | 1000-1800 lines | 300-500 per module |
| **Time to complete** | 30-60 min | 2-4 hours | 30-60 min per module |
| **Variables** | 30-60 | 100-150+ | 20-40 per module |
| **Examples** | 2-3 scenarios | 5-8 scenarios | 2-3 per module |
| **Best for** | Most projects | Enterprise/Complex | Team/Phased work |
| **Learning curve** | Easy | Moderate | Easy (per module) |
| **Flexibility** | Moderate | High | Highest |
| **Detail level** | Balanced | Exhaustive | Focused |

---

## 💡 Practical Examples

### Scenario 1: Small Business Marketing Campaign

**Situation**: Local bakery wants to create social media ads for holiday season

**Recommended version**: **Standard** - `ad-copy.md`

**Why**:
- Small-scale project
- Limited time and budget
- Needs practical examples quickly
- Comprehensive version would be overwhelming

**Alternative**: If bakery is launching a full rebrand with multiple campaigns, use `ad-copy-comprehensive.md`

---

### Scenario 2: Fortune 500 Digital Transformation

**Situation**: Large manufacturing company (5,000 employees) planning 3-year digital transformation

**Recommended version**: **Comprehensive** - `strategic-digital-transformation-roadmap.md`

**Why**:
- Enterprise-scale project ($50M+ budget)
- Multiple stakeholders need buy-in
- High complexity (legacy systems, change management, etc.)
- Board-level visibility requires thorough documentation
- 2-4 hour investment justified by project scale

---

### Scenario 3: Healthcare System Implementing AI

**Situation**: 12-hospital system implementing generative AI across departments

**Recommended version**: **Split/Modular** - `generative-ai-implementation-XX-` series

**Why**:
- Multiple teams involved:
  - IT team: Technical infrastructure module
  - Legal/Compliance: Governance module
  - Clinical leaders: Foundation/strategy module
- Phased rollout (pilot → expansion → full deployment)
- Each team can work independently
- Overview file keeps everyone aligned

**How to use**:
1. Leadership reads `generative-ai-implementation-overview.md`
2. Each team uses their specific module
3. Monthly meetings to integrate work
4. Sequential implementation over 18 months

---

## 🔄 When to Switch Versions

### Start with Standard, Upgrade to Comprehensive if:
- ✓ Project scope expands significantly
- ✓ Stakeholders request more detail
- ✓ Standard version feels too shallow
- ✓ You're hitting edge cases not covered in standard

### Start with Comprehensive, Simplify to Standard if:
- ✓ Feeling overwhelmed by variables
- ✓ Time-constrained (deadline moved up)
- ✓ Project scope reduced
- ✓ Just need "good enough," not perfect

### Switch to Split/Modular if:
- ✓ Team grows (assign modules to members)
- ✓ Timeline extends (phased approach better)
- ✓ Only need specific components
- ✓ Want to learn topic incrementally

---

## 🎓 Learning Path Recommendation

**If you're NEW to a domain** (e.g., first time doing market research):

**Week 1**: Use **Standard** template
- Get familiar with core concepts
- Complete a small project
- Understand the basics

**Month 2-3**: Try **Comprehensive** template
- Deepen your understanding
- Tackle a larger project
- Explore advanced options

**Quarter 2+**: Use **Split/Modular** as needed
- Pick modules relevant to specific needs
- Mix-and-match for custom workflows
- Become an expert

---

## 📝 Template Naming Conventions

Understanding filenames helps you quickly identify versions:

| Filename Pattern | Version Type | Example |
|-----------------|--------------|---------|
| `topic-name.md` | Standard | `market-research.md` |
| `topic-name-comprehensive.md` | Comprehensive | `ad-copy-comprehensive.md` |
| `topic-name-overview.md` | Navigation (for split set) | `network-analysis-overview.md` |
| `topic-name-01-section.md` | Split module | `generative-ai-implementation-01-foundation.md` |
| `topic-name-simple.md` | Simplified (rare) | N/A (not commonly used) |

---

## ❓ FAQ

### Q: Can I use multiple versions for one project?
**A**: Yes! Common pattern:
1. Start with **Standard** for initial planning
2. Switch to **Comprehensive** for detailed execution
3. Use **Split modules** to delegate to team members

### Q: Do comprehensive templates include everything from standard versions?
**A**: Yes, comprehensive versions are supersets. They include all standard content plus additional depth.

### Q: Which version should consultants/agencies use?
**A**: Usually **Comprehensive**:
- Clients expect thorough deliverables
- Demonstrates expertise
- Justifies premium pricing
- Reduces revision cycles

### Q: Which version for academic/research projects?
**A**: **Comprehensive** or **Split/Modular**:
- Research requires rigor and documentation
- Comprehensive versions include methodology details
- Split versions work well for thesis chapters

### Q: I'm overwhelmed by the comprehensive version. What do I do?
**A**: Three options:
1. **Switch to Standard** - Totally fine! Use what works.
2. **Use only relevant sections** - Skip sections that don't apply
3. **Split approach** - Tackle one section per day

### Q: How do I know if examples are included?
**A**: Check the table of contents or search for "## Usage Examples" or "## Examples" section. As of 2025, 100% of prompts have Quick Start sections, and high-priority prompts (12+) have detailed usage examples.

---

## 🚀 Quick Start by User Type

### **Startup Founder** (moving fast, limited resources)
👉 Use **Standard** templates
- Quick implementation
- Good enough for early stage
- Iterate as you grow

### **Enterprise Manager** (established company, governance-focused)
👉 Use **Comprehensive** templates
- Thoroughness expected
- Multiple stakeholder alignment
- Compliance and risk management

### **Consultant/Agency** (delivering to clients)
👉 Use **Comprehensive** templates
- Professional deliverables
- Demonstrates value
- Reduces client questions

### **Academic Researcher** (rigorous methodology required)
👉 Use **Comprehensive** or **Split/Modular**
- Meet publication standards
- Detailed documentation
- Reproducible methods

### **Student** (learning + assignments)
👉 Use **Standard** templates
- Learn fundamentals
- Complete assignments efficiently
- Upgrade to comprehensive for thesis/capstone

### **Team Lead** (coordinating multiple people)
👉 Use **Split/Modular** templates
- Assign modules to team members
- Parallel workstreams
- Easier integration

---

## 📈 When to Create Your Own Hybrid Version

Sometimes the best approach is customizing:

**How to create a hybrid**:
1. Start with **Standard** template as base
2. Pull specific advanced sections from **Comprehensive** version
3. Add your own examples and customizations
4. Save as `project-name-custom.md`

**Good candidates for customization**:
- Recurring projects (create a template for your specific workflow)
- Industry-specific adaptations (add your domain jargon/standards)
- Team templates (incorporate your company's processes)

---

## 📞 Still Not Sure?

**Decision paralysis?** → Start with **Standard**. You can always upgrade.

**Want maximum thoroughness?** → Choose **Comprehensive**.

**Working with a team?** → Try **Split/Modular**.

**Time-constrained?** → Definitely **Standard** (or just use Quick Start section!).

---

## 📚 Related Resources

- **README.md** - Repository overview and how to use templates
- **INDEX.md** - Searchable catalog of all 375+ templates
- **QUICK_START_TEMPLATE_GUIDE.md** - Guide to Quick Start sections (all templates have these)
- Category README files (each of 13 categories has a guide)

---

## 🔄 Version History

- **2025-11-11**: Initial version selection guide created
- Covers 375+ templates across 13 categories
- Reflects recent improvements: 100% Quick Start coverage, split templates, comprehensive versions

---

**Need help?** File an issue on GitHub or reference this guide when selecting templates.

**Pro tip**: When in doubt, start simple. You can always add complexity later.
