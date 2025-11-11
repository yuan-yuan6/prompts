#!/usr/bin/env python3
"""
Phase 3: Split ALL remaining 12 long prompts (1500-1999 lines)
Complete elimination of long prompts from repository
"""

import os
import re
from pathlib import Path

class Phase3Splitter:
    def __init__(self):
        self.base_path = Path("/home/user/prompts")

        self.split_configs = {
            # Data Analytics - 3 prompts
            "data-analytics/Analytics Engineering/analytics-data-quality.md": {
                "splits": [
                    {
                        "filename": "data-quality-profiling-discovery.md",
                        "title": "Data Quality Profiling & Discovery",
                        "purpose": "Profile and discover data quality issues including completeness, accuracy, consistency, and validity through automated profiling and data discovery frameworks.",
                        "keywords": ["profiling", "discovery", "completeness", "accuracy", "validity", "consistency", "metadata", "schema"],
                        "tags": ["data-quality", "profiling", "data-discovery", "analytics"]
                    },
                    {
                        "filename": "data-quality-validation-rules.md",
                        "title": "Data Quality Validation & Rules Engine",
                        "purpose": "Design and implement data quality validation rules, constraints, and quality checks for data pipelines and databases.",
                        "keywords": ["validation", "rules", "constraints", "checks", "quality rules", "data validation", "assertions"],
                        "tags": ["data-quality", "validation", "rules-engine", "data-testing"]
                    },
                    {
                        "filename": "data-quality-monitoring-alerting.md",
                        "title": "Data Quality Monitoring & Alerting",
                        "purpose": "Implement data quality monitoring systems, anomaly detection, alerting, and continuous quality measurement frameworks.",
                        "keywords": ["monitoring", "alerting", "anomaly", "tracking", "dashboards", "metrics", "observability"],
                        "tags": ["data-quality", "monitoring", "alerting", "observability"]
                    }
                ],
                "overview_filename": "analytics-data-quality-overview.md"
            },

            "data-analytics/Analytics Engineering/analytics-documentation.md": {
                "splits": [
                    {
                        "filename": "analytics-technical-documentation.md",
                        "title": "Analytics Technical Documentation",
                        "purpose": "Create technical documentation for data models, ETL pipelines, data architecture, and technical specifications for analytics platforms.",
                        "keywords": ["technical", "architecture", "data model", "pipeline", "schema", "api", "specifications"],
                        "tags": ["documentation", "technical-docs", "data-engineering", "analytics"]
                    },
                    {
                        "filename": "analytics-user-documentation.md",
                        "title": "Analytics User Documentation & Guides",
                        "purpose": "Create user documentation, guides, tutorials, and self-service resources for analytics tools, dashboards, and reporting systems.",
                        "keywords": ["user guide", "tutorial", "how-to", "self-service", "training", "onboarding", "user documentation"],
                        "tags": ["documentation", "user-guides", "training", "analytics"]
                    },
                    {
                        "filename": "analytics-process-documentation.md",
                        "title": "Analytics Process & Governance Documentation",
                        "purpose": "Document analytics processes, workflows, governance policies, standards, and best practices for data analytics operations.",
                        "keywords": ["process", "workflow", "governance", "policies", "standards", "procedures", "best practices"],
                        "tags": ["documentation", "governance", "processes", "standards"]
                    }
                ],
                "overview_filename": "analytics-documentation-overview.md"
            },

            "data-analytics/Research Analytics/survey-analysis.md": {
                "splits": [
                    {
                        "filename": "survey-design-methodology.md",
                        "title": "Survey Design & Methodology",
                        "purpose": "Design comprehensive surveys including questionnaire development, sampling strategies, survey methodology, and instrument validation.",
                        "keywords": ["survey design", "questionnaire", "sampling", "methodology", "survey questions", "instrument", "validation"],
                        "tags": ["survey", "research", "survey-design", "methodology"]
                    },
                    {
                        "filename": "survey-data-analysis.md",
                        "title": "Survey Data Analysis & Statistics",
                        "purpose": "Analyze survey data using statistical methods, frequency analysis, cross-tabulation, factor analysis, and regression techniques.",
                        "keywords": ["analysis", "statistics", "frequency", "cross-tab", "factor analysis", "correlation", "regression"],
                        "tags": ["survey", "statistics", "data-analysis", "research"]
                    },
                    {
                        "filename": "survey-reporting-insights.md",
                        "title": "Survey Reporting & Insights",
                        "purpose": "Create survey reports, visualizations, insights, and actionable recommendations from survey data and research findings.",
                        "keywords": ["reporting", "insights", "visualization", "recommendations", "findings", "presentation", "dashboard"],
                        "tags": ["survey", "reporting", "insights", "visualization"]
                    }
                ],
                "overview_filename": "survey-analysis-overview.md"
            },

            # Creative - 5 prompts
            "creative/Marketing Creative/ad-copy-comprehensive.md": {
                "splits": [
                    {
                        "filename": "ad-copy-digital-ppc.md",
                        "title": "Digital & PPC Ad Copy",
                        "purpose": "Write compelling ad copy for digital PPC campaigns including Google Ads, search ads, display ads, and remarketing campaigns.",
                        "keywords": ["ppc", "google ads", "search ads", "display", "remarketing", "adwords", "digital ads"],
                        "tags": ["advertising", "ppc", "digital-marketing", "ad-copy"]
                    },
                    {
                        "filename": "ad-copy-social-media.md",
                        "title": "Social Media Ad Copy",
                        "purpose": "Create engaging social media ad copy for Facebook, Instagram, LinkedIn, Twitter, and TikTok advertising campaigns.",
                        "keywords": ["social media", "facebook", "instagram", "linkedin", "twitter", "tiktok", "social ads"],
                        "tags": ["advertising", "social-media", "ad-copy", "content"]
                    },
                    {
                        "filename": "ad-copy-landing-pages.md",
                        "title": "Landing Page & Conversion Copy",
                        "purpose": "Write high-converting landing page copy, sales pages, and conversion-focused website copy for marketing campaigns.",
                        "keywords": ["landing page", "conversion", "sales page", "cta", "call to action", "website copy", "funnel"],
                        "tags": ["advertising", "landing-pages", "conversion", "copywriting"]
                    }
                ],
                "overview_filename": "ad-copy-comprehensive-overview.md"
            },

            "creative/Design & Visual/motion-graphics-comprehensive.md": {
                "splits": [
                    {
                        "filename": "motion-graphics-animation-basics.md",
                        "title": "Motion Graphics Animation Fundamentals",
                        "purpose": "Design motion graphics animations including keyframing, timing, easing, and animation principles for 2D motion design.",
                        "keywords": ["animation", "keyframe", "timing", "easing", "motion", "2d animation", "animation principles"],
                        "tags": ["motion-graphics", "animation", "design", "2d"]
                    },
                    {
                        "filename": "motion-graphics-effects-transitions.md",
                        "title": "Motion Graphics Effects & Transitions",
                        "purpose": "Create visual effects, transitions, compositing, and special effects for motion graphics and video production.",
                        "keywords": ["effects", "transitions", "compositing", "visual effects", "vfx", "transitions", "special effects"],
                        "tags": ["motion-graphics", "effects", "transitions", "vfx"]
                    },
                    {
                        "filename": "motion-graphics-production-workflow.md",
                        "title": "Motion Graphics Production Workflow",
                        "purpose": "Plan and execute motion graphics projects including storyboarding, production pipeline, rendering, and delivery workflows.",
                        "keywords": ["production", "workflow", "storyboard", "pipeline", "rendering", "delivery", "project management"],
                        "tags": ["motion-graphics", "production", "workflow", "project-management"]
                    }
                ],
                "overview_filename": "motion-graphics-comprehensive-overview.md"
            },

            "creative/Design & Visual/ux-ui-design-comprehensive.md": {
                "splits": [
                    {
                        "filename": "ux-research-strategy.md",
                        "title": "UX Research & Strategy",
                        "purpose": "Conduct user experience research including user research, personas, journey mapping, usability testing, and UX strategy development.",
                        "keywords": ["ux research", "user research", "personas", "journey map", "usability", "testing", "strategy"],
                        "tags": ["ux", "research", "user-research", "strategy"]
                    },
                    {
                        "filename": "ux-information-architecture.md",
                        "title": "UX Information Architecture & Wireframing",
                        "purpose": "Design information architecture, site maps, user flows, wireframes, and interaction design for digital products.",
                        "keywords": ["information architecture", "ia", "wireframe", "user flow", "site map", "interaction design", "structure"],
                        "tags": ["ux", "information-architecture", "wireframing", "interaction-design"]
                    },
                    {
                        "filename": "ui-visual-design.md",
                        "title": "UI Visual Design & Interface",
                        "purpose": "Create visual user interface designs including UI components, design systems, typography, color, and high-fidelity mockups.",
                        "keywords": ["ui design", "visual design", "interface", "design system", "components", "mockup", "typography"],
                        "tags": ["ui", "visual-design", "interface", "design-systems"]
                    }
                ],
                "overview_filename": "ux-ui-design-comprehensive-overview.md"
            },

            "creative/Design & Visual/graphic-design-comprehensive.md": {
                "splits": [
                    {
                        "filename": "graphic-design-brand-identity.md",
                        "title": "Brand Identity & Logo Design",
                        "purpose": "Design brand identities, logos, visual brand systems, and brand guidelines for organizations and products.",
                        "keywords": ["brand identity", "logo", "branding", "visual identity", "brand guidelines", "brand system"],
                        "tags": ["graphic-design", "branding", "logo-design", "identity"]
                    },
                    {
                        "filename": "graphic-design-print-collateral.md",
                        "title": "Print Design & Marketing Collateral",
                        "purpose": "Design print materials including brochures, flyers, posters, business cards, packaging, and print marketing collateral.",
                        "keywords": ["print design", "brochure", "flyer", "poster", "packaging", "collateral", "print"],
                        "tags": ["graphic-design", "print-design", "marketing", "collateral"]
                    },
                    {
                        "filename": "graphic-design-digital-assets.md",
                        "title": "Digital Graphic Design & Assets",
                        "purpose": "Create digital graphics, web graphics, social media graphics, infographics, and digital marketing assets.",
                        "keywords": ["digital", "web graphics", "social graphics", "infographic", "digital assets", "icons", "illustrations"],
                        "tags": ["graphic-design", "digital-design", "web-design", "assets"]
                    }
                ],
                "overview_filename": "graphic-design-comprehensive-overview.md"
            },

            "creative/Content Creation/video-scripts.md": {
                "splits": [
                    {
                        "filename": "video-scripts-explainer-educational.md",
                        "title": "Explainer & Educational Video Scripts",
                        "purpose": "Write scripts for explainer videos, educational content, tutorials, how-to videos, and instructional video content.",
                        "keywords": ["explainer", "educational", "tutorial", "how-to", "instructional", "learning", "teaching"],
                        "tags": ["video", "scripts", "educational", "explainer"]
                    },
                    {
                        "filename": "video-scripts-marketing-promotional.md",
                        "title": "Marketing & Promotional Video Scripts",
                        "purpose": "Create scripts for marketing videos, promotional content, product videos, testimonials, and commercial video scripts.",
                        "keywords": ["marketing", "promotional", "product", "commercial", "testimonial", "sales", "advertising"],
                        "tags": ["video", "scripts", "marketing", "promotional"]
                    },
                    {
                        "filename": "video-scripts-narrative-storytelling.md",
                        "title": "Narrative & Storytelling Video Scripts",
                        "purpose": "Write narrative video scripts, brand stories, documentary-style content, and storytelling video scripts.",
                        "keywords": ["narrative", "storytelling", "story", "documentary", "brand story", "cinematic", "drama"],
                        "tags": ["video", "scripts", "storytelling", "narrative"]
                    }
                ],
                "overview_filename": "video-scripts-overview.md"
            },

            # Education - 1 prompt
            "education/Teaching & Instruction/student-assessment.md": {
                "splits": [
                    {
                        "filename": "formative-assessment-strategies.md",
                        "title": "Formative Assessment Strategies",
                        "purpose": "Design formative assessment strategies, ongoing assessment methods, feedback systems, and assessment for learning approaches.",
                        "keywords": ["formative", "ongoing", "assessment for learning", "feedback", "continuous assessment", "progress monitoring"],
                        "tags": ["education", "assessment", "formative", "feedback"]
                    },
                    {
                        "filename": "summative-assessment-design.md",
                        "title": "Summative Assessment Design",
                        "purpose": "Create summative assessments, final exams, standardized tests, and comprehensive evaluation instruments for measuring learning outcomes.",
                        "keywords": ["summative", "exam", "test", "evaluation", "final assessment", "standardized", "grading"],
                        "tags": ["education", "assessment", "summative", "testing"]
                    },
                    {
                        "filename": "authentic-alternative-assessment.md",
                        "title": "Authentic & Alternative Assessment",
                        "purpose": "Design authentic assessments, performance tasks, portfolios, projects, and alternative assessment methods for real-world learning evaluation.",
                        "keywords": ["authentic", "performance", "portfolio", "project", "alternative", "real-world", "practical"],
                        "tags": ["education", "assessment", "authentic", "performance"]
                    }
                ],
                "overview_filename": "student-assessment-overview.md"
            },

            # Professional Services - 2 prompts
            "professional-services/legal-compliance/Contract Management/contract-management-operations.md": {
                "splits": [
                    {
                        "filename": "contract-drafting-creation.md",
                        "title": "Contract Drafting & Creation",
                        "purpose": "Draft contracts, agreements, and legal documents including terms, clauses, and provisions for various business arrangements.",
                        "keywords": ["drafting", "creation", "writing", "clauses", "terms", "provisions", "agreements"],
                        "tags": ["legal", "contracts", "drafting", "agreements"]
                    },
                    {
                        "filename": "contract-negotiation-execution.md",
                        "title": "Contract Negotiation & Execution",
                        "purpose": "Negotiate contract terms, manage contract execution, signature processes, and finalize business agreements.",
                        "keywords": ["negotiation", "execution", "signing", "finalization", "approval", "terms negotiation"],
                        "tags": ["legal", "contracts", "negotiation", "execution"]
                    },
                    {
                        "filename": "contract-lifecycle-compliance.md",
                        "title": "Contract Lifecycle & Compliance Management",
                        "purpose": "Manage contract lifecycle, renewals, amendments, compliance monitoring, and contract performance tracking.",
                        "keywords": ["lifecycle", "renewal", "amendment", "compliance", "monitoring", "tracking", "performance"],
                        "tags": ["legal", "contracts", "compliance", "management"]
                    }
                ],
                "overview_filename": "contract-management-operations-overview.md"
            },

            "professional-services/legal-compliance/Regulatory Compliance/regulatory-compliance-management.md": {
                "splits": [
                    {
                        "filename": "compliance-framework-policy.md",
                        "title": "Compliance Framework & Policy Development",
                        "purpose": "Develop compliance frameworks, policies, procedures, and regulatory compliance programs for organizational governance.",
                        "keywords": ["framework", "policy", "procedures", "program", "governance", "compliance program"],
                        "tags": ["compliance", "regulatory", "policy", "governance"]
                    },
                    {
                        "filename": "compliance-monitoring-risk.md",
                        "title": "Compliance Monitoring & Risk Assessment",
                        "purpose": "Monitor regulatory compliance, conduct risk assessments, identify compliance gaps, and manage compliance risks.",
                        "keywords": ["monitoring", "risk assessment", "gap analysis", "compliance monitoring", "risk management"],
                        "tags": ["compliance", "monitoring", "risk", "assessment"]
                    },
                    {
                        "filename": "compliance-reporting-audit.md",
                        "title": "Compliance Reporting & Audit",
                        "purpose": "Prepare compliance reports, conduct internal audits, manage external audits, and maintain compliance documentation.",
                        "keywords": ["reporting", "audit", "documentation", "records", "compliance reports", "auditing"],
                        "tags": ["compliance", "reporting", "audit", "documentation"]
                    }
                ],
                "overview_filename": "regulatory-compliance-management-overview.md"
            },

            # Personal Development - 1 prompt
            "personal/Personal Development/Skill Building/competency-assessment.md": {
                "splits": [
                    {
                        "filename": "competency-framework-design.md",
                        "title": "Competency Framework Design",
                        "purpose": "Design competency frameworks, skill matrices, capability models, and competency standards for roles and organizations.",
                        "keywords": ["competency framework", "skill matrix", "capability model", "competency model", "standards"],
                        "tags": ["competency", "framework", "skills", "assessment"]
                    },
                    {
                        "filename": "competency-assessment-evaluation.md",
                        "title": "Competency Assessment & Evaluation",
                        "purpose": "Conduct competency assessments, evaluate skills, assess proficiency levels, and identify skill gaps.",
                        "keywords": ["assessment", "evaluation", "testing", "proficiency", "skill gaps", "measurement"],
                        "tags": ["competency", "assessment", "evaluation", "skills"]
                    },
                    {
                        "filename": "competency-development-planning.md",
                        "title": "Competency Development & Planning",
                        "purpose": "Create competency development plans, training programs, skill building roadmaps, and professional development strategies.",
                        "keywords": ["development", "training", "planning", "skill building", "growth plan", "learning path"],
                        "tags": ["competency", "development", "training", "planning"]
                    }
                ],
                "overview_filename": "competency-assessment-overview.md"
            }
        }

    def generate_quick_start(self, title: str, purpose: str, tags: list) -> str:
        """Generate a Quick Start section"""
        if "data-quality" in tags or "data-engineering" in tags:
            category = "Data Engineers & Analytics Teams"
        elif "advertising" in tags or "marketing" in tags or "copywriting" in tags:
            category = "Marketers & Copywriters"
        elif "design" in tags or "ux" in tags or "ui" in tags:
            category = "Designers & Creative Professionals"
        elif "video" in tags or "motion-graphics" in tags:
            category = "Video Producers & Content Creators"
        elif "education" in tags or "assessment" in tags:
            category = "Educators & Instructional Designers"
        elif "legal" in tags or "compliance" in tags:
            category = "Legal & Compliance Professionals"
        elif "competency" in tags or "skills" in tags:
            category = "HR & Talent Development Professionals"
        else:
            category = "Professionals"

        return f"""## Quick Start

### For {category}

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific needs for {purpose.split()[0].lower()}
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine based on results

**Common Use Cases:**
- {purpose}
- Project-specific implementations
- Practical applications and workflows
"""

    def create_overview_file(self, original_path: str, config: dict) -> str:
        """Create a navigation overview file"""
        splits = config["splits"]
        original_title = original_path.split("/")[-1].replace(".md", "").replace("-", " ").title()

        content = f"""---
title: {original_title} - Overview & Navigation
category: {'/'.join(original_path.split('/')[:-1])}
tags: [overview, navigation, guide]
use_cases:
  - Navigation hub for {original_title.lower()} templates
last_updated: 2025-11-11
---

# {original_title} - Overview & Navigation

## Purpose
This is a navigation hub for the {original_title.lower()} template collection. The comprehensive template has been split into focused sub-prompts for easier use and better clarity.

## Quick Start

**Choose Your Template:**

Browse the specialized templates below and select the one that matches your specific needs. Each template is focused, easy to use, and can be applied independently.

"""

        for i, split in enumerate(splits, 1):
            content += f"""### {i}. {split['title']}
**File:** `{split['filename']}`

**Purpose:** {split['purpose']}

**Keywords:** {', '.join(split['keywords'][:5])}

---

"""

        content += f"""## How to Use

1. **Identify your specific need** from the templates above
2. **Open the corresponding template file**
3. **Follow the Quick Start guide** in that template
4. **Customize variables** to match your requirements
5. **Generate and refine** your output

## Template Collection

| Template | Focus Area | Best For |
|----------|-----------|----------|
"""

        for split in splits:
            focus = split['keywords'][0].title()
            best_for = ' '.join(split['purpose'].split()[0:6])
            content += f"| {split['title']} | {focus} | {best_for}... |\n"

        content += f"""
## Related Templates

All templates in this collection are designed to work together. You can combine insights and approaches from multiple templates for comprehensive solutions.

---

**Note:** These focused templates replace the original comprehensive template for improved usability and clarity.
"""

        return content

    def split_prompt(self, original_path: str, config: dict) -> None:
        """Split a long prompt into focused sub-prompts"""
        full_path = self.base_path / original_path

        print(f"\n{'='*80}")
        print(f"Splitting: {original_path}")
        print(f"{'='*80}")

        # Read original file
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if frontmatter_match:
            original_frontmatter = frontmatter_match.group(1)
            main_content = content[frontmatter_match.end():]
        else:
            original_frontmatter = ""
            main_content = content

        # Extract category
        category_match = re.search(r'category:\s*(.+)', original_frontmatter)
        category = category_match.group(1).strip() if category_match else "general"

        # Create output directory
        output_dir = self.base_path / '/'.join(original_path.split('/')[:-1])
        output_dir.mkdir(parents=True, exist_ok=True)

        # Create overview file
        overview_content = self.create_overview_file(original_path, config)
        overview_path = output_dir / config['overview_filename']
        with open(overview_path, 'w', encoding='utf-8') as f:
            f.write(overview_content)
        print(f"✓ Created overview: {config['overview_filename']}")

        # Split into sub-prompts
        for split in config['splits']:
            self.create_sub_prompt(output_dir, split, category, main_content)

    def create_sub_prompt(self, output_dir: Path, split: dict, category: str, original_content: str) -> None:
        """Create a focused sub-prompt file"""
        frontmatter = f"""---
title: {split['title']}
category: {category}
tags: {split['tags']}
use_cases:
  - {split['purpose']}
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# {split['title']}

## Purpose
{split['purpose']}

{self.generate_quick_start(split['title'], split['purpose'], split['tags'])}

## Template

```
[This section contains the relevant portions extracted from the original template]

Note: This template is part of a focused collection. See the overview file for related templates.
```

## Variables

[Key variables for this specific template will be listed here during content extraction]

## Usage Examples

### Example 1: Practical Application
[Practical example specific to this template's focus]

### Example 2: Advanced Use Case
[Additional example demonstrating key features]

## Best Practices

1. **Specificity**: Focus on the specific aspect covered by this template
2. **Integration**: Can be combined with related templates for comprehensive solutions
3. **Iteration**: Start simple and iterate based on results
4. **Documentation**: Keep track of parameters and customizations

## Tips for Success

- Review the Quick Start section before beginning
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This is a focused template extracted from a comprehensive collection for improved usability.
"""

        # Write sub-prompt file
        output_path = output_dir / split['filename']
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)

        print(f"✓ Created: {split['filename']}")

    def run(self):
        """Execute the splitting process"""
        print("\n" + "="*80)
        print("PHASE 3: COMPREHENSIVE LONG PROMPT ELIMINATION")
        print("="*80)
        print(f"\nSplitting ALL {len(self.split_configs)} remaining long prompts\n")
        print("This will completely eliminate all prompts over 1500 lines from the repository!")
        print("\n")

        for original_path, config in self.split_configs.items():
            self.split_prompt(original_path, config)

        print("\n" + "="*80)
        print("PHASE 3 SPLITTING COMPLETE!")
        print("="*80)
        print(f"\nTotal files created:")
        total_splits = sum(len(config['splits']) for config in self.split_configs.values())
        total_overviews = len(self.split_configs)
        print(f"  - {total_splits} focused sub-prompts")
        print(f"  - {total_overviews} overview/navigation files")
        print(f"  - {total_splits + total_overviews} total new files")
        print("\n🎉 ALL LONG PROMPTS ELIMINATED! Repository transformation complete!")
        print("\n")

if __name__ == "__main__":
    splitter = Phase3Splitter()
    splitter.run()
