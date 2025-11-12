#!/usr/bin/env python3
"""
Fix broken related_templates links in markdown files.

This script:
1. Scans all template files for related_templates in YAML frontmatter
2. Identifies broken links (files that don't exist)
3. Attempts to find the correct path for each broken link
4. Updates the YAML frontmatter with corrected paths
5. Creates a backup before making changes
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

class RelatedTemplatesFixer:
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.template_files = []
        self.all_files = set()
        self.file_basenames = {}  # basename -> [full_paths]
        self.fixes_made = []
        self.unfixable = []

    def scan_repository(self):
        """Scan repository for all template files"""
        exclude_patterns = [
            'README.md', 'INDEX.md', 'CHANGELOG.md', 'LICENSE',
            '_VIEW.md', 'GUIDE.md', 'SUMMARY.md', 'PLAN.md',
            'STATUS.md', 'COMPLETE.md', 'ANALYSIS.md', 'TRACKER.md',
            'RECOMMENDATIONS.md', 'TAXONOMY.md', 'FEASIBILITY.md'
        ]

        for root, dirs, files in os.walk('.'):
            if '.git' in root or 'scripts' in root:
                continue

            for file in files:
                if not file.endswith('.md'):
                    continue

                filepath = os.path.join(root, file)

                # Skip documentation files
                if any(p in file for p in exclude_patterns):
                    continue

                self.template_files.append(filepath)
                self.all_files.add(filepath)

                # Index by basename
                basename = os.path.basename(filepath)
                if basename not in self.file_basenames:
                    self.file_basenames[basename] = []
                self.file_basenames[basename].append(filepath)

        print(f"Found {len(self.template_files)} template files")

    def find_correct_path(self, broken_link, source_file):
        """Try to find the correct path for a broken link"""
        # Extract basename
        basename = os.path.basename(broken_link)

        # Method 1: Direct basename match
        if basename in self.file_basenames:
            candidates = self.file_basenames[basename]

            # If only one match, use it
            if len(candidates) == 1:
                return candidates[0].lstrip('./')

            # Multiple matches - try to find best match based on directory
            source_dir = os.path.dirname(source_file)

            # Prefer files in same category
            source_category = source_dir.split('/')[1] if '/' in source_dir else None

            for candidate in candidates:
                candidate_category = candidate.split('/')[1] if '/' in candidate else None
                if candidate_category == source_category:
                    return candidate.lstrip('./')

            # Return first match if no category match
            return candidates[0].lstrip('./')

        # Method 2: Try common path variations
        variations = [
            broken_link,
            './' + broken_link,
            broken_link.replace(' ', '-'),
            './' + broken_link.replace(' ', '-'),
            os.path.join(os.path.dirname(source_file), broken_link).replace(' ', '-'),
        ]

        for variation in variations:
            if os.path.exists(variation):
                return variation.lstrip('./')
            # Check in all_files
            for filepath in self.all_files:
                if filepath.endswith(variation) or filepath.lstrip('./') == variation:
                    return filepath.lstrip('./')

        return None

    def process_file(self, filepath):
        """Process a single file and fix broken links"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return False

        # Extract YAML frontmatter
        match = re.match(r'^---\s*\n(.*?\n)---\s*\n', content, re.DOTALL)
        if not match:
            return False

        yaml_block = match.group(1)

        # Find related_templates section
        related_match = re.search(r'related_templates:\s*\n((?:- .*\n)*)', yaml_block)
        if not related_match:
            return False

        related_section = related_match.group(0)
        original_related_section = related_section

        # Extract individual links
        links = re.findall(r'- (.+)', related_section)

        fixes_in_file = []
        for link in links:
            link_clean = link.strip()

            # Check if link exists
            link_path = link_clean if link_clean.startswith('./') else './' + link_clean

            if not os.path.exists(link_path):
                # Try to fix it
                correct_path = self.find_correct_path(link_clean, filepath)

                if correct_path:
                    # Replace in related_section
                    related_section = related_section.replace(f"- {link_clean}", f"- {correct_path}")
                    fixes_in_file.append({
                        'broken': link_clean,
                        'fixed': correct_path
                    })
                else:
                    self.unfixable.append({
                        'file': filepath,
                        'link': link_clean
                    })

        if fixes_in_file:
            # Update content
            new_content = content.replace(original_related_section, related_section)

            if not self.dry_run:
                # Create backup
                backup_path = filepath + '.backup'
                shutil.copy2(filepath, backup_path)

                # Write updated content
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

            self.fixes_made.append({
                'file': filepath,
                'fixes': fixes_in_file
            })

            return True

        return False

    def run(self):
        """Run the fixer"""
        print("=" * 70)
        print("RELATED_TEMPLATES LINK FIXER")
        print("=" * 70)
        print(f"Mode: {'DRY RUN (no changes)' if self.dry_run else 'LIVE (making changes)'}")
        print()

        # Scan repository
        self.scan_repository()

        # Process each file
        print("\nProcessing files...")
        for filepath in self.template_files:
            self.process_file(filepath)

        # Report results
        print("\n" + "=" * 70)
        print("RESULTS")
        print("=" * 70)
        print(f"\nFiles processed: {len(self.template_files)}")
        print(f"Files with fixes: {len(self.fixes_made)}")
        print(f"Total fixes made: {sum(len(f['fixes']) for f in self.fixes_made)}")
        print(f"Unfixable links: {len(self.unfixable)}")

        if self.fixes_made:
            print("\n" + "=" * 70)
            print("FIXES APPLIED (Sample - First 20)")
            print("=" * 70)
            for i, fix_record in enumerate(self.fixes_made[:20]):
                print(f"\n{i+1}. {fix_record['file']}")
                for fix in fix_record['fixes'][:3]:  # Show first 3 fixes per file
                    print(f"   ✓ {fix['broken']}")
                    print(f"   → {fix['fixed']}")
                if len(fix_record['fixes']) > 3:
                    print(f"   ... and {len(fix_record['fixes']) - 3} more fixes")

        if self.unfixable:
            print("\n" + "=" * 70)
            print("UNFIXABLE LINKS (Sample - First 20)")
            print("=" * 70)
            for i, unfixable in enumerate(self.unfixable[:20]):
                print(f"\n{i+1}. File: {unfixable['file']}")
                print(f"   Link: {unfixable['link']}")

        if self.dry_run:
            print("\n" + "=" * 70)
            print("DRY RUN COMPLETE")
            print("=" * 70)
            print("Run with --live to apply changes")
        else:
            print("\n" + "=" * 70)
            print("CHANGES APPLIED")
            print("=" * 70)
            print("Backups created with .backup extension")

if __name__ == "__main__":
    import sys

    dry_run = '--live' not in sys.argv

    fixer = RelatedTemplatesFixer(dry_run=dry_run)
    fixer.run()
