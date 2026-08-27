import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"
tfile = os.path.join(root_dir, "assets", "theme.js")

with open(tfile, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        if "js-ingredient-filter" in l or "data-category" in l or "filter" in l.lower():
            print(f"L{i+1}: {l.strip()}")
