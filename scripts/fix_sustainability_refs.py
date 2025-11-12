#!/usr/bin/env python3
"""
Fix sustainability template references to include subdirectory paths.
"""

import os
import re

def fix_sustainability_refs():
    """Fix sustainability references in all templates."""

    # Mapping of old references to new ones
    replacements = {
        'sustainability/esg-strategy-framework.md': 'sustainability/ESG-Strategy/esg-strategy-framework.md',
        'sustainability/esg-reporting-disclosure.md': 'sustainability/ESG-Strategy/esg-reporting-disclosure.md',
        'sustainability/stakeholder-engagement.md': 'sustainability/ESG-Strategy/stakeholder-engagement.md',
        'sustainability/esg-risk-assessment.md': 'sustainability/ESG-Strategy/esg-risk-assessment.md',
        'sustainability/esg-performance-metrics.md': 'sustainability/ESG-Strategy/esg-performance-metrics.md',
        'sustainability/circular-economy-strategy.md': 'sustainability/Circular-Economy/circular-economy-strategy.md',
        'sustainability/waste-reduction-programs.md': 'sustainability/Circular-Economy/waste-reduction-programs.md',
        'sustainability/sustainable-supply-chain.md': 'sustainability/Circular-Economy/sustainable-supply-chain.md',
        'sustainability/climate-strategy-net-zero.md': 'sustainability/Climate-Environment/climate-strategy-net-zero.md',
        'sustainability/environmental-impact-assessment.md': 'sustainability/Climate-Environment/environmental-impact-assessment.md',
        'sustainability/carbon-footprint-accounting.md': 'sustainability/Climate-Environment/carbon-footprint-accounting.md',
        'sustainability/renewable-energy-transition.md': 'sustainability/Climate-Environment/renewable-energy-transition.md',
        'sustainability/dei-programs.md': 'sustainability/Social-Impact/dei-programs.md',
    }

    fixed_count = 0

    # Walk through all markdown files
    for root, dirs, files in os.walk('/home/user/prompts'):
        # Skip hidden directories and scripts
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scripts']

        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    original_content = content

                    # Apply all replacements
                    for old_ref, new_ref in replacements.items():
                        if old_ref in content:
                            content = content.replace(old_ref, new_ref)

                    # Write back if changed
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixed_count += 1
                        rel_path = os.path.relpath(filepath, '/home/user/prompts')
                        print(f"✅ Fixed: {rel_path}")

                except Exception as e:
                    print(f"❌ Error processing {filepath}: {e}")

    print(f"\n{'='*80}")
    print(f"✅ Fixed {fixed_count} files")
    return fixed_count

if __name__ == '__main__':
    fix_sustainability_refs()
