import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"
html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

solid_announcement_tag = '<div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important; background-color: #133e28 !important; background-image: none !important;">'

count = 0
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match announcement bar opening div
    pattern = r'<div class="[^"]*(?:bg-\[#133e28\]|from-\[#123824\]|announcement-bar-solid)[^"]*"(?:\s*style="[^"]*")?>'
    
    new_content = re.sub(pattern, solid_announcement_tag, content)

    if new_content != content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Applied 100% Solid Emerald Announcement Bar to {count} HTML files!")
