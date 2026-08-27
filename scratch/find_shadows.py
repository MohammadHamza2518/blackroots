import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Search in theme.css and html files
for fpath in glob.glob(os.path.join(root_dir, "*.html")) + glob.glob(os.path.join(root_dir, "assets", "*.css")):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Search for any elements with radial-gradient or gradients in top area
    for m in re.finditer(r'([^\n;{}]*(?:radial-gradient|linear-gradient|box-shadow|backdrop-filter|fixed|sticky)[^\n;{}]*)', content):
        line = m.group(1).strip()
        if any(w in line for w in ['radial', 'bg-', 'shadow', 'header', 'announcement', 'gradient', 'inset']):
            # Filter relevant
            if 'button' not in line.lower() and 'font' not in line.lower() and len(line) < 150:
                print(f"[{fname}] {line}")
