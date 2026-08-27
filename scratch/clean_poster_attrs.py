import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html"),
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean any duplicate poster="..." poster="..." attributes
    new_content = re.sub(r'poster=["\']([^"\']+)["\']\s+poster=["\']\1["\']', r'poster="\1"', content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Cleaned poster attributes in", fpath)

