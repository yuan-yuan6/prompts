#!/usr/bin/env python3
"""
Update related_templates references after repository reorganization
"""
import os
import re
from pathlib import Path

# Path mappings (old directory → new directory)
PATH_MAPPINGS = {
    'business/Finance & Accounting': 'finance/Corporate-Finance',
    'business/Strategic Management': 'strategy',
    'business/Operations & Processes': 'operations',
    'business/Sales & Marketing': 'sales-marketing',
    'business/Human Resources': 'human-resources',
    'professional-services/communication': 'communication',
    'professional-services/legal-compliance': 'legal-compliance',
    'professional-services/human-resources': 'human-resources',
    'creative/Design & Visual': 'design',
    'creative/Content Creation': 'content-creation',
    'creative/Entertainment': 'content-creation/Entertainment',
    'creative/arts-culture': 'content-creation/Arts-Culture',
    'creative/journalism': 'media-journalism',
    'creative/Marketing Creative': 'sales-marketing/Marketing-Creative',
    'creative/social-media': 'sales-marketing/Social-Media',
    'industry/manufacturing': 'operations/Manufacturing',
    'industry/transportation-logistics': 'operations/Transportation-Logistics',
    'industry/energy-utilities': 'operations/Energy-Utilities',
    'industry/construction': 'operations/Construction',
    'industry/hospitality': 'operations/Hospitality',
    'industry/agriculture': 'operations/Agriculture',
    'industry/retail-ecommerce': 'sales-marketing/Retail-Ecommerce',
    'industry/real-estate': 'sales-marketing/Real-Estate',
    'industry/fashion-beauty': 'design/Fashion',
    'industry/telecommunications': 'technology/Telecommunications',
    'industry/entertainment-gaming': 'content-creation/Gaming',
    'technology/Cybersecurity': 'security/Cybersecurity',
}

# Build a file location index
def build_file_index(base_dir):
    """Build an index of all markdown files and their locations"""
    file_index = {}
    for root, dirs, files in os.walk(base_dir):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith('.md') and file != 'README.md':
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                filename = file
                if filename not in file_index:
                    file_index[filename] = []
                file_index[filename].append(rel_path)
    return file_index

def find_new_path(old_ref, file_index):
    """Find the new path for a moved file reference"""
    # Extract just the filename
    filename = os.path.basename(old_ref)

    if filename in file_index:
        # If there's only one match, use it
        if len(file_index[filename]) == 1:
            return file_index[filename][0]
        # If multiple matches, try to find best match
        for new_path in file_index[filename]:
            # Prefer paths that match the mapping
            for old_dir, new_dir in PATH_MAPPINGS.items():
                if old_dir in old_ref and new_dir in new_path:
                    return new_path
        # If no good match, return first one
        return file_index[filename][0]

    return None

def update_file_links(filepath, file_index, base_dir):
    """Update related_templates links in a single file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not yaml_match:
        return False

    yaml_content = yaml_match.group(1)

    # Find related_templates section
    related_match = re.search(r'related_templates:\s*\n((?:  ?- [^\n]+\n)+)', yaml_content)
    if not related_match:
        return False

    related_section = related_match.group(1)
    updated_section = related_section
    updates_made = False

    # Find all template references
    for line_match in re.finditer(r'  ?- (.+\.md)', related_section):
        old_ref = line_match.group(1).strip()

        # Check if file still exists at old location
        old_full_path = os.path.join(base_dir, old_ref)
        if os.path.exists(old_full_path):
            continue  # File wasn't moved

        # Try to find new location
        new_ref = find_new_path(old_ref, file_index)
        if new_ref and new_ref != old_ref:
            updated_section = updated_section.replace(f'- {old_ref}', f'- {new_ref}')
            updates_made = True
            print(f"  Updated: {old_ref} → {new_ref}")

    if updates_made:
        # Replace in original content
        new_content = content.replace(related_section, updated_section)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True

    return False

def main():
    base_dir = '/home/user/prompts'

    print("Building file index...")
    file_index = build_file_index(base_dir)
    print(f"Found {len(file_index)} unique filenames")

    print("\nUpdating related_templates references...")
    total_files = 0
    updated_files = 0

    for root, dirs, files in os.walk(base_dir):
        # Skip hidden directories and old directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['business', 'professional-services', 'creative', 'industry']]

        for file in files:
            if file.endswith('.md') and file != 'README.md':
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, base_dir)
                total_files += 1

                if update_file_links(filepath, file_index, base_dir):
                    updated_files += 1
                    print(f"✓ Updated {rel_path}")

    print(f"\nProcessed {total_files} files, updated {updated_files} files")

if __name__ == '__main__':
    main()
