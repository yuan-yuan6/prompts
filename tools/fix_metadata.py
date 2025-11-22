#!/usr/bin/env python3
"""Fill in missing front-matter metadata fields for prompt templates.

- Adds default `type`, `difficulty`, and `slug` for files that already
  have valid YAML front-matter with `title` and `category`.
- Skips documentation files (no `category`) and hidden/utility folders.
"""

import sys
from pathlib import Path

try:
    import yaml
except Exception:
    print("PyYAML is required in the current environment.")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".github", ".venv", ".templates", ".claude"}

UPDATED = 0

for md in ROOT.glob("**/*.md"):
    if not md.is_file():
        continue
    if any(part in SKIP_DIRS for part in md.parts):
        continue

    text = md.read_text(encoding="utf-8")
    stripped = text.lstrip()
    if not stripped.startswith("---"):
        # No front-matter; treat as documentation, not a template
        continue

    parts = text.split("---", 2)
    if len(parts) < 3:
        # Malformed front-matter delimiters; skip rather than guessing
        continue

    _prefix, fm_raw, body = parts
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except Exception as e:
        # YAML parse error; do not attempt automatic repair
        print(f"Skipping due to YAML parse error in {md}: {e}")
        continue

    # Only treat files with both title and category as real templates
    if not (fm.get("title") and fm.get("category")):
        continue

    changed = False

    if not fm.get("type"):
        fm["type"] = "template"
        changed = True

    if not fm.get("difficulty"):
        fm["difficulty"] = "intermediate"
        changed = True

    if not fm.get("slug"):
        # Use file stem as a simple, stable slug
        rel = md.relative_to(ROOT)
        fm["slug"] = rel.with_suffix("").name
        changed = True

    if not changed:
        continue

    new_fm = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    new_text = f"---\n{new_fm}\n---" + body
    md.write_text(new_text, encoding="utf-8")
    UPDATED += 1

print(f"Updated {UPDATED} files with missing metadata fields.")
