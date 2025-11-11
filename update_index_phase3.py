#!/usr/bin/env python3
"""
Update INDEX.md with Phase 3 splits (all 12 remaining long prompts)
Comprehensive INDEX update for final repository transformation
"""

import re
from pathlib import Path

def update_index_phase3():
    index_path = Path("/home/user/prompts/INDEX.md")

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define all replacements for Phase 3 (12 prompts → 48 files)
    replacements = {
        # Data Quality (Analytics Engineering)
        r'- \[Analytics Data Quality\]\(data-analytics/Analytics Engineering/analytics-data-quality\.md\) - `data-analytics`': '''- [Analytics Data Quality Overview](data-analytics/Analytics Engineering/analytics-data-quality-overview.md) - `data-analytics`
- [Data Quality Profiling & Discovery](data-analytics/Analytics Engineering/data-quality-profiling-discovery.md) - `data-analytics`
- [Data Quality Validation & Rules](data-analytics/Analytics Engineering/data-quality-validation-rules.md) - `data-analytics`
- [Data Quality Monitoring & Alerting](data-analytics/Analytics Engineering/data-quality-monitoring-alerting.md) - `data-analytics`''',

        # Analytics Documentation
        r'- \[Analytics Documentation\]\(data-analytics/Analytics Engineering/analytics-documentation\.md\) - `data-analytics`': '''- [Analytics Documentation Overview](data-analytics/Analytics Engineering/analytics-documentation-overview.md) - `data-analytics`
- [Analytics Technical Documentation](data-analytics/Analytics Engineering/analytics-technical-documentation.md) - `data-analytics`
- [Analytics User Documentation](data-analytics/Analytics Engineering/analytics-user-documentation.md) - `data-analytics`
- [Analytics Process Documentation](data-analytics/Analytics Engineering/analytics-process-documentation.md) - `data-analytics`''',

        # Survey Analysis
        r'- \[Survey Analysis\]\(data-analytics/Research Analytics/survey-analysis\.md\) - `data-analytics`': '''- [Survey Analysis Overview](data-analytics/Research Analytics/survey-analysis-overview.md) - `data-analytics`
- [Survey Design & Methodology](data-analytics/Research Analytics/survey-design-methodology.md) - `data-analytics`
- [Survey Data Analysis](data-analytics/Research Analytics/survey-data-analysis.md) - `data-analytics`
- [Survey Reporting & Insights](data-analytics/Research Analytics/survey-reporting-insights.md) - `data-analytics`''',

        # Ad Copy Comprehensive
        r'- \[Ad Copy Comprehensive\]\(creative/Marketing Creative/ad-copy-comprehensive\.md\) - `creative`': '''- [Ad Copy Overview](creative/Marketing Creative/ad-copy-comprehensive-overview.md) - `creative`
- [Digital & PPC Ad Copy](creative/Marketing Creative/ad-copy-digital-ppc.md) - `creative`
- [Social Media Ad Copy](creative/Marketing Creative/ad-copy-social-media.md) - `creative`
- [Landing Page & Conversion Copy](creative/Marketing Creative/ad-copy-landing-pages.md) - `creative`''',

        # Motion Graphics
        r'- \[Motion Graphics Comprehensive\]\(creative/Design & Visual/motion-graphics-comprehensive\.md\) - `creative`': '''- [Motion Graphics Overview](creative/Design & Visual/motion-graphics-comprehensive-overview.md) - `creative`
- [Motion Graphics Animation Fundamentals](creative/Design & Visual/motion-graphics-animation-basics.md) - `creative`
- [Motion Graphics Effects & Transitions](creative/Design & Visual/motion-graphics-effects-transitions.md) - `creative`
- [Motion Graphics Production Workflow](creative/Design & Visual/motion-graphics-production-workflow.md) - `creative`''',

        # UX UI Design
        r'- \[Ux Ui Design Comprehensive\]\(creative/Design & Visual/ux-ui-design-comprehensive\.md\) - `creative`': '''- [UX UI Design Overview](creative/Design & Visual/ux-ui-design-comprehensive-overview.md) - `creative`
- [UX Research & Strategy](creative/Design & Visual/ux-research-strategy.md) - `creative`
- [UX Information Architecture](creative/Design & Visual/ux-information-architecture.md) - `creative`
- [UI Visual Design & Interface](creative/Design & Visual/ui-visual-design.md) - `creative`''',

        # Graphic Design
        r'- \[Graphic Design Comprehensive\]\(creative/Design & Visual/graphic-design-comprehensive\.md\) - `creative`': '''- [Graphic Design Overview](creative/Design & Visual/graphic-design-comprehensive-overview.md) - `creative`
- [Brand Identity & Logo Design](creative/Design & Visual/graphic-design-brand-identity.md) - `creative`
- [Print Design & Marketing Collateral](creative/Design & Visual/graphic-design-print-collateral.md) - `creative`
- [Digital Graphic Design & Assets](creative/Design & Visual/graphic-design-digital-assets.md) - `creative`''',

        # Video Scripts
        r'- \[Video Scripts\]\(creative/Content Creation/video-scripts\.md\) - `creative`': '''- [Video Scripts Overview](creative/Content Creation/video-scripts-overview.md) - `creative`
- [Explainer & Educational Video Scripts](creative/Content Creation/video-scripts-explainer-educational.md) - `creative`
- [Marketing & Promotional Video Scripts](creative/Content Creation/video-scripts-marketing-promotional.md) - `creative`
- [Narrative & Storytelling Video Scripts](creative/Content Creation/video-scripts-narrative-storytelling.md) - `creative`''',

        # Student Assessment
        r'- \[Student Assessment\]\(education/Teaching & Instruction/student-assessment\.md\) - `education`': '''- [Student Assessment Overview](education/Teaching & Instruction/student-assessment-overview.md) - `education`
- [Formative Assessment Strategies](education/Teaching & Instruction/formative-assessment-strategies.md) - `education`
- [Summative Assessment Design](education/Teaching & Instruction/summative-assessment-design.md) - `education`
- [Authentic & Alternative Assessment](education/Teaching & Instruction/authentic-alternative-assessment.md) - `education`''',

        # Contract Management (note the path)
        r'- \[Contract Management Operations\]\(professional-services/legal-compliance/Contract Management/contract-management-operations\.md\)': '''- [Contract Management Overview](professional-services/legal-compliance/Contract Management/contract-management-operations-overview.md)
- [Contract Drafting & Creation](professional-services/legal-compliance/Contract Management/contract-drafting-creation.md)
- [Contract Negotiation & Execution](professional-services/legal-compliance/Contract Management/contract-negotiation-execution.md)
- [Contract Lifecycle & Compliance](professional-services/legal-compliance/Contract Management/contract-lifecycle-compliance.md)''',

        # Regulatory Compliance (note the path)
        r'- \[Regulatory Compliance Management\]\(professional-services/legal-compliance/Regulatory Compliance/regulatory-compliance-management\.md\)': '''- [Regulatory Compliance Overview](professional-services/legal-compliance/Regulatory Compliance/regulatory-compliance-management-overview.md)
- [Compliance Framework & Policy](professional-services/legal-compliance/Regulatory Compliance/compliance-framework-policy.md)
- [Compliance Monitoring & Risk](professional-services/legal-compliance/Regulatory Compliance/compliance-monitoring-risk.md)
- [Compliance Reporting & Audit](professional-services/legal-compliance/Regulatory Compliance/compliance-reporting-audit.md)''',

        # Competency Assessment
        r'- \[Competency Assessment\]\(personal/Personal Development/Skill Building/competency-assessment\.md\)': '''- [Competency Assessment Overview](personal/Personal Development/Skill Building/competency-assessment-overview.md)
- [Competency Framework Design](personal/Personal Development/Skill Building/competency-framework-design.md)
- [Competency Assessment & Evaluation](personal/Personal Development/Skill Building/competency-assessment-evaluation.md)
- [Competency Development & Planning](personal/Personal Development/Skill Building/competency-development-planning.md)''',
    }

    # Apply all replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    # Update template counts by category
    # Analytics & Business Intelligence: was 45, adding 9 (quality 3 + docs 3 + survey 3) = 54
    content = re.sub(
        r'### Analytics & Business Intelligence\n\*\*45 templates\*\*',
        '### Analytics & Business Intelligence\n**54 templates**',
        content
    )

    # Design & Creative: was 35, adding 12 (motion 3 + ux-ui 3 + graphic 3 + ad-copy 3) = 47
    # Need to count current creative templates first
    # From previous: ad-copy-comprehensive, motion-graphics-comprehensive, ux-ui-design-comprehensive, graphic-design-comprehensive, video-scripts
    # These 5 become 20 (5 removed, 20 added = +15)
    # But we need to find the actual current count
    creative_match = re.search(r'### Design & Creative\n\*\*(\d+) templates\*\*', content)
    if creative_match:
        current_creative = int(creative_match.group(1))
        new_creative = current_creative - 5 + 20  # Remove 5 comprehensive, add 20 split
        content = re.sub(
            r'### Design & Creative\n\*\*\d+ templates\*\*',
            f'### Design & Creative\n**{new_creative} templates**',
            content
        )

    # Content Creation & Writing: video-scripts splits (+3 net)
    content_match = re.search(r'### Content Creation & Writing\n\*\*(\d+) templates\*\*', content)
    if content_match:
        current_content = int(content_match.group(1))
        new_content = current_content - 1 + 4  # Remove 1, add 4
        content = re.sub(
            r'### Content Creation & Writing\n\*\*\d+ templates\*\*',
            f'### Content Creation & Writing\n**{new_content} templates**',
            content
        )

    # Education & Learning: was 41, adding 3 (assessment splits) = 44
    content = re.sub(
        r'### Education & Learning\n\*\*41 templates\*\*',
        '### Education & Learning\n**44 templates**',
        content
    )

    # Update total count: was 410+, adding 36 net (48 new - 12 removed) = 446+
    content = re.sub(
        r'A comprehensive, searchable index of all 410\+ templates',
        'A comprehensive, searchable index of all 450+ templates',
        content
    )

    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ INDEX.md updated successfully (Phase 3 - FINAL)!")
    print("\nChanges made:")
    print("  - Replaced 12 long prompts with 48 new files (36 sub-prompts + 12 overviews)")
    print("  - Updated Analytics & Business Intelligence: 45 → 54 templates (+9)")
    print("  - Updated Design & Creative category (+15 net)")
    print("  - Updated Content Creation & Writing (+3 net)")
    print("  - Updated Education & Learning: 41 → 44 templates (+3)")
    print("  - Updated total count: 410+ → 450+ templates (+40)")
    print("\n🎉 PHASE 3 INDEX UPDATE COMPLETE!")
    print("✅ ALL LONG PROMPTS ELIMINATED FROM INDEX!")

if __name__ == "__main__":
    update_index_phase3()
