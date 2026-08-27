import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Find all HTML files
html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update theme.css cachebuster
    new_content = re.sub(r'theme\.css(\?v=\d+)?', 'theme.css?v=1786802001', content)
    # Also update theme.js cachebuster
    new_content = re.sub(r'theme\.js(\?v=\d+)?', 'theme.js?v=1786802001', new_content)

    if new_content != content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Updated theme.css and theme.js cachebusters across all HTML files!")
