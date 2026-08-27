import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

for root, dirs, files in os.walk(root_dir):
    if 'scratch' in root or '.git' in root:
        continue
    for f in files:
        if f.endswith('.html') or f.endswith('.liquid') or f.endswith('.js'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
                for i, line in enumerate(file.readlines()):
                    if "22 Review" in line or "Reviews Reviews" in line or "22 reviews" in line.lower():
                        print(f"{os.path.relpath(fp, root_dir)}:L{i+1} -> {line.strip().encode('ascii', 'replace').decode()}")
