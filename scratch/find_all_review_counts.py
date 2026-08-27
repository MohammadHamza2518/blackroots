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
                    if "Review" in line and ("<button" in line or "<span" in line or "<div" in line or "<a" in line):
                        # print if contains a number like 22 or similar
                        if re.search(r'\d+\s*Review', line) or "Reviews" in line:
                            print(f"{os.path.relpath(fp, root_dir)}:L{i+1} -> {line.strip().encode('ascii', 'replace').decode()}")
