import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"

for p in ["product.html", "index.html"]:
    fpath = os.path.join(root_dir, p)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f.readlines()):
                if "SAVE" in line or ("50%" in line and "OFF" in line):
                    print(f"{p}:L{i+1} -> {line.strip().encode('ascii', 'replace').decode()}")
