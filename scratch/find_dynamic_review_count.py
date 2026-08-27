import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

for root, dirs, files in os.walk(root_dir):
    if 'scratch' in root or '.git' in root:
        continue
    for f in files:
        if f.endswith('.html') or f.endswith('.js'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()
                for i, l in enumerate(lines):
                    if "review" in l.lower() and ("length" in l or "count" in l or "total" in l or "innerhtml" in l.lower() or "textcontent" in l.lower() or "span" in l or "pill" in l):
                        print(f"{os.path.relpath(fp, root_dir)}:L{i+1} -> {l.strip()[:100].encode('ascii', 'replace').decode()}")
