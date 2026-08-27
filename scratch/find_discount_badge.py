import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

for p in ["product.html", "index.html"]:
    fpath = os.path.join(root_dir, p)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f.readlines()):
                if "SAVE" in line or "50% OFF" in line or "500" in line:
                    if "50%" in line or "SAVE" in line:
                        print(f"{p}:L{i+1} -> {line.strip()}")
