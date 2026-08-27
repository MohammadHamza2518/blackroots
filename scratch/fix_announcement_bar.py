import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# 1. Update announcement bar across all HTML files to uniform, clean, vibrant emerald green
html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

old_announcement_pattern = r'class="[^"]*bg-gradient-to-r from-\[#123824\] via-\[#0d2a1c\] to-\[#123824\][^"]*"'
new_announcement_class = 'class="bg-[#133e28] text-[#fef3c7] border-b border-[#d4af37]/35 py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide"'

updated = []
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(
        r'class="[^"]*from-\[#123824\][^"]*"',
        'class="bg-[#133e28] text-[#fef3c7] border-b border-[#d4af37]/35 py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide"',
        content
    )
    
    if new_content != content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated.append(hf)

print(f"Updated announcement bar in {len(updated)} files:")
for u in updated:
    print(" -", u)
