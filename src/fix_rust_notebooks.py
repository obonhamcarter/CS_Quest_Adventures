#!/usr/bin/env python3
"""
Remove invalid notebook references from Rust lesson files.
Rust uses the Rust Playground, not Jupyter notebooks.
"""

import re
from pathlib import Path

def fix_rust_lesson(file_path):
    """Remove notebook references from a Rust lesson file."""
    content = file_path.read_text()
    
    # Pattern to match the tip-box with notebook references
    old_pattern = r'::: \{\.tip-box\}\n\*\*💻 Practice Options:\*\*\n- 🦀 \[Open Rust Playground\]\(https://play\.rust-lang\.org/\)\n- 📓 \[View Notebook\]\(\.\./files/lessons/.*?\.ipynb\)\n- 📥 \[Download Notebook\]\(\.\./files/lessons/.*?\.ipynb\)\n:::'
    
    new_content = '::: {.tip-box}\n**💻 Practice Options:**\n- 🦀 [Open Rust Playground](https://play.rust-lang.org/)\n:::'
    
    updated_content = re.sub(old_pattern, new_content, content)
    
    if updated_content != content:
        file_path.write_text(updated_content)
        return True
    return False

def main():
    rust_lessons_dir = Path(__file__).parent.parent / "tracks" / "rust" / "lessons"
    
    if not rust_lessons_dir.exists():
        print(f"❌ Directory not found: {rust_lessons_dir}")
        return
    
    fixed_count = 0
    for lesson_file in sorted(rust_lessons_dir.glob("*.qmd")):
        if fix_rust_lesson(lesson_file):
            print(f"✓ Fixed: {lesson_file.name}")
            fixed_count += 1
        else:
            print(f"  Skipped: {lesson_file.name} (no changes needed)")
    
    print(f"\n✅ Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
