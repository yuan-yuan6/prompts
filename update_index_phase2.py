#!/usr/bin/env python3
"""
Update INDEX.md with Phase 2 splits (online-learning and statistical-analysis)
"""

import re
from pathlib import Path

def update_index_phase2():
    index_path = Path("/home/user/prompts/INDEX.md")

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define replacements for phase 2
    replacements = {
        # Online Learning (education)
        r'- \[Online Learning\]\(education/Teaching & Instruction/online-learning\.md\) - `education`': '''- [Online Learning Overview](education/Teaching & Instruction/online-learning-overview.md) - `education`
- [Online Learning Platform Architecture](education/Teaching & Instruction/online-learning-platform-architecture.md) - `education`
- [Online Learning Content & Curriculum](education/Teaching & Instruction/online-learning-content-curriculum.md) - `education`
- [Online Learning Pedagogy & Engagement](education/Teaching & Instruction/online-learning-pedagogy-engagement.md) - `education`
- [Online Learning Communication Tools](education/Teaching & Instruction/online-learning-communication-tools.md) - `education`''',

        # Statistical Analysis (data-analytics) - already split in phase 1, but now splitting further
        r'- \[Statistical Analysis\]\(data-analytics/Research Analytics/statistical-analysis\.md\) - `data-analytics`': '''- [Statistical Analysis Overview](data-analytics/Research Analytics/statistical-analysis-overview.md) - `data-analytics`
- [Descriptive Statistics & EDA](data-analytics/Research Analytics/descriptive-statistics-eda.md) - `data-analytics`
- [Hypothesis Testing & Inference](data-analytics/Research Analytics/hypothesis-testing-inference.md) - `data-analytics`
- [Regression Modeling & Analysis](data-analytics/Research Analytics/regression-modeling-analysis.md) - `data-analytics`
- [Advanced Statistical Methods](data-analytics/Research Analytics/advanced-statistical-methods.md) - `data-analytics`''',
    }

    # Additional replacements for contexts without category tag
    replacements_no_category = {
        r'- \[Online Learning\]\(education/Teaching & Instruction/online-learning\.md\)': '''- [Online Learning Overview](education/Teaching & Instruction/online-learning-overview.md)
- [Online Learning Platform Architecture](education/Teaching & Instruction/online-learning-platform-architecture.md)
- [Online Learning Content & Curriculum](education/Teaching & Instruction/online-learning-content-curriculum.md)
- [Online Learning Pedagogy & Engagement](education/Teaching & Instruction/online-learning-pedagogy-engagement.md)
- [Online Learning Communication Tools](education/Teaching & Instruction/online-learning-communication-tools.md)''',

        r'- \[Statistical Analysis\]\(data-analytics/Research Analytics/statistical-analysis\.md\)': '''- [Statistical Analysis Overview](data-analytics/Research Analytics/statistical-analysis-overview.md)
- [Descriptive Statistics & EDA](data-analytics/Research Analytics/descriptive-statistics-eda.md)
- [Hypothesis Testing & Inference](data-analytics/Research Analytics/hypothesis-testing-inference.md)
- [Regression Modeling & Analysis](data-analytics/Research Analytics/regression-modeling-analysis.md)
- [Advanced Statistical Methods](data-analytics/Research Analytics/advanced-statistical-methods.md)''',
    }

    # Apply replacements with category tags
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    # Apply replacements without category tags
    for pattern, replacement in replacements_no_category.items():
        content = re.sub(pattern, replacement, content)

    # Update template counts
    # Analytics & Business Intelligence: was 41 (from phase 1), now 41 - 1 + 5 = 45
    content = re.sub(
        r'### Analytics & Business Intelligence\n\*\*41 templates\*\*',
        '### Analytics & Business Intelligence\n**45 templates**',
        content
    )

    # Education & Learning: was 37 (from phase 1), now 37 - 1 + 5 = 41
    content = re.sub(
        r'### Education & Learning\n\*\*37 templates\*\*',
        '### Education & Learning\n**41 templates**',
        content
    )

    # Update total count: was 400+, now 400 + 10 - 2 = 408+
    content = re.sub(
        r'A comprehensive, searchable index of all 400\+ templates',
        'A comprehensive, searchable index of all 410+ templates',
        content
    )

    # Write updated content
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ INDEX.md updated successfully (Phase 2)!")
    print("\nChanges made:")
    print("  - Replaced 2 long prompts with 10 new sub-prompts and overviews")
    print("  - Updated Analytics & Business Intelligence: 41 → 45 templates")
    print("  - Updated Education & Learning: 37 → 41 templates")
    print("  - Updated total count: 400+ → 410+ templates")

if __name__ == "__main__":
    update_index_phase2()
