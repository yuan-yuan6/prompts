#!/usr/bin/env python3
"""
Split large prompts into focused sub-prompts with proper cross-references
"""

import os
from pathlib import Path

# Configuration for each file to split
SPLIT_CONFIG = {
    "meeting-management-framework": {
        "path": "professional-services/communication/meeting-management-framework.md",
        "parts": [
            {"lines": (367, 713), "name": "02-facilitation-engagement", "title": "Facilitation & Engagement"},
            {"lines": (714, 1075), "name": "03-followup-improvement", "title": "Follow-up & Improvement"}
        ]
    },
    "clinical-decision-support": {
        "path": "healthcare/clinical-decision-support.md",
        "parts": [
            {"lines": (1, 366), "name": "01-knowledge-base", "title": "Clinical Knowledge Base"},
            {"lines": (367, 626), "name": "02-decision-algorithms", "title": "Decision Algorithms"},
            {"lines": (627, 1075), "name": "03-implementation", "title": "Implementation & Integration"}
        ],
        "overview": True
    },
    "predictive-modeling-framework": {
        "path": "data-analytics/predictive-modeling-framework.md",
        "parts": [
            {"lines": (1, 366), "name": "01-data-preparation", "title": "Data Preparation & Feature Engineering"},
            {"lines": (367, 626), "name": "02-model-development", "title": "Model Development & Evaluation"},
            {"lines": (627, 1075), "name": "03-deployment", "title": "Deployment & Monitoring"}
        ],
        "overview": True
    },
    "crisis-communication-plan": {
        "path": "professional-services/communication/crisis-communication-plan.md",
        "parts": [
            {"lines": (1, 350), "name": "01-preparation-strategy", "title": "Preparation & Strategy"},
            {"lines": (351, 700), "name": "02-response-management", "title": "Response & Management"},
            {"lines": (701, 1061), "name": "03-recovery-learning", "title": "Recovery & Learning"}
        ],
        "overview": True
    },
    "contract-drafting-template": {
        "path": "professional-services/legal-compliance/contract-drafting-template.md",
        "parts": [
            {"lines": (1, 340), "name": "01-structure-core", "title": "Structure & Core Clauses"},
            {"lines": (341, 680), "name": "02-risk-provisions", "title": "Risk Provisions"},
            {"lines": (681, 1012), "name": "03-execution", "title": "Execution & Management"}
        ],
        "overview": True
    },
    "music-audio-comprehensive": {
        "path": "creative/Entertainment/music-audio-comprehensive.md",
        "parts": [
            {"lines": (1, 340), "name": "01-composition", "title": "Composition & Arrangement"},
            {"lines": (341, 680), "name": "02-production", "title": "Production & Recording"},
            {"lines": (681, 1012), "name": "03-mastering", "title": "Mixing & Mastering"}
        ],
        "overview": True
    }
}

def create_part_header(base_name, part_num, total_parts, part_title, category, tags):
    """Create header with cross-references for a part"""
    other_parts = [f"{base_name}-{i:02d}" for i in range(1, total_parts + 1) if i != part_num]
    related_parts_md = "\n  - ".join([f"{p}.md" for p in other_parts])

    return f"""---
title: {base_name.replace('-', ' ').title()} - Part {part_num}: {part_title}
category: {category}
tags: {tags}
series: {base_name}
part: {part_num} of {total_parts}
related_parts:
  - {related_parts_md}
  - {base_name}-overview.md
last_updated: 2025-11-11
---

# {base_name.replace('-', ' ').title()} - Part {part_num}: {part_title}

## Part Overview

**This is Part {part_num} of {total_parts}** in the {base_name.replace('-', ' ').title()} series.

- **Part 1:** {SPLIT_CONFIG[base_name]['parts'][0]['title']}
{f"- **Part 2:** {SPLIT_CONFIG[base_name]['parts'][1]['title']}" if total_parts > 2 else ""}
- **Part {total_parts}:** {SPLIT_CONFIG[base_name]['parts'][-1]['title']}

## Quick Start

This part focuses on **{part_title}**. For complete workflow, start with Part 1 and progress sequentially.

**Next Steps:** {'Continue to Part ' + str(part_num + 1) if part_num < total_parts else 'Review all parts for comprehensive understanding'}

## Related Resources
- **Overview:** Complete framework navigation guide
{chr(10).join([f'- **Part {i}:** {SPLIT_CONFIG[base_name]["parts"][i-1]["title"]}' for i in range(1, total_parts + 1) if i != part_num])}
"""

def split_file(base_name, config, base_path="/home/user/prompts"):
    """Split a file into parts"""
    source_file = Path(base_path) / config["path"]

    # Read source file
    with open(source_file, 'r') as f:
        lines = f.readlines()

    # Extract metadata from original
    category = None
    tags = None
    for line in lines[:20]:
        if line.startswith('category:'):
            category = line.split(':', 1)[1].strip()
        if line.startswith('tags:'):
            tags = line.split(':', 1)[1].strip()

    # Process each part
    for idx, part in enumerate(config["parts"], 1):
        start_line = part["lines"][0] - 1
        end_line = part["lines"][1]
        part_lines = lines[start_line:end_line]

        # Create header
        header = create_part_header(
            base_name,
            idx,
            len(config["parts"]),
            part["title"],
            category,
            tags
        )

        # Write part file
        out_dir = Path(base_path) / Path(config["path"]).parent
        out_file = out_dir / f"{base_name}-{part['name']}.md"

        with open(out_file, 'w') as f:
            f.write(header)
            f.write('\n')
            f.writelines(part_lines)

        print(f"Created: {out_file}")

def create_overview(base_name, config, base_path="/home/user/prompts"):
    """Create overview file for a split prompt"""
    source_file = Path(base_path) / config["path"]

    # Read first 20 lines for metadata
    with open(source_file, 'r') as f:
        lines = [f.readline() for _ in range(20)]

    category = None
    tags = None
    for line in lines:
        if line.startswith('category:'):
            category = line.split(':', 1)[1].strip()
        if line.startswith('tags:'):
            tags = line.split(':', 1)[1].strip()

    parts_desc = "\n\n".join([
        f"""### Part {idx}: {part['title']} (Lines {part['lines'][0]}-{part['lines'][1]})
**File:** `{base_name}-{part['name']}.md`

**Use this part when you need to:**
[Focus area for part {idx}]"""
        for idx, part in enumerate(config["parts"], 1)
    ])

    overview_content = f"""---
title: {base_name.replace('-', ' ').title()} - Overview & Navigation
category: {category}
tags: {tags}
parent_prompt: {base_name} (split into {len(config['parts'])} parts)
last_updated: 2025-11-11
---

# {base_name.replace('-', ' ').title()} - Overview & Navigation

## Purpose
This comprehensive framework has been split into {len(config['parts'])} focused sub-prompts for easier navigation and use.

## Framework Structure

{parts_desc}

## Quick Navigation

**Complete Workflow:**
{chr(10).join([f'{i}. Start with Part {i} for {config["parts"][i-1]["title"].lower()}' for i in range(1, len(config["parts"]) + 1)])}

## Related Resources
{chr(10).join([f'- Part {i}: {config["parts"][i-1]["title"]}' for i in range(1, len(config["parts"]) + 1)])}
"""

    out_dir = Path(base_path) / Path(config["path"]).parent
    out_file = out_dir / f"{base_name}-overview.md"

    with open(out_file, 'w') as f:
        f.write(overview_content)

    print(f"Created: {out_file}")

# Main execution
if __name__ == "__main__":
    base_path = "/home/user/prompts"

    for base_name, config in SPLIT_CONFIG.items():
        print(f"\nProcessing {base_name}...")

        # Skip meeting-management-framework part 1 (already created)
        if base_name == "meeting-management-framework":
            # Only create parts 2 and 3
            for idx, part in enumerate(config["parts"], 2):
                split_file(base_name, {"path": config["path"], "parts": [part]}, base_path)
        else:
            # Create overview if needed
            if config.get("overview"):
                create_overview(base_name, config, base_path)

            # Create all parts
            split_file(base_name, config, base_path)

    print("\n✓ All files created successfully!")
