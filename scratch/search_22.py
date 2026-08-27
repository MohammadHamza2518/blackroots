import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

for root, dirs, files in os.walk(root_dir):
    if 'scratch' in root or '.git' in root:
        continue
    for f in files:
        if f.endswith('.html') or f.endswith('.liquid') or f.endswith('.js'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                matches = re.finditer(r'([^\n]*?22[^\n]*?)', content, re.IGNORECASE)
                for m in matches:
                    line = m.group(1).strip()
                    if "review" in line.lower() or "rating" in line.lower() or "tab" in line.lower() or "pill" in line.lower():
                        print(f"{os.path.relpath(fp, root_dir)} -> {line}")
