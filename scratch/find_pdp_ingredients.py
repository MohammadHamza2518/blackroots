import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"
pfile = os.path.join(root_dir, "product.html")

with open(pfile, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "Japanese Indigo" in line or "Click each active ingredient" in line or "Camellia Oil" in line:
            print(f"L{i+1}: {line.strip().encode('ascii', 'replace').decode()}")
