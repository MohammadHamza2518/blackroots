import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Sync instant-butter.js to demo_lab/assets and preview/assets
for folder in ["demo_lab", "preview"]:
    dst_assets = os.path.join(root_dir, folder, "assets")
    os.makedirs(dst_assets, exist_ok=True)
    with open(os.path.join(root_dir, "assets", "instant-butter.js"), "r", encoding="utf-8") as sf:
        content = sf.read()
    with open(os.path.join(dst_assets, "instant-butter.js"), "w", encoding="utf-8") as df:
        df.write(content)
    print(f"Synced instant-butter.js to {folder}/assets/")

html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

butter_tag = '  <script src="./assets/instant-butter.js" defer></script>'

for hf in html_files:
    if 'scratch' in hf or '.git' in hf or 'node_modules' in hf:
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    if 'instant-butter.js' not in new_content:
        # Insert right after theme.js
        if 'theme.js' in new_content:
            new_content = re.sub(r'(<script src="[^"]*theme\.js[^"]*"[^>]*><\/script>)', r'\1\n' + butter_tag, new_content)
        else:
            new_content = new_content.replace('</head>', butter_tag + '\n</head>')

    if new_content != content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected instant-butter.js into: {os.path.relpath(hf, root_dir)}")

# Also inject in layout/theme.liquid
theme_liquid = os.path.join(root_dir, "layout", "theme.liquid")
if os.path.exists(theme_liquid):
    with open(theme_liquid, "r", encoding="utf-8") as f:
        l_content = f.read()
    if 'instant-butter.js' not in l_content:
        l_content = l_content.replace('</head>', '  {{ "instant-butter.js" | asset_url | script_tag }}\n</head>')
        with open(theme_liquid, "w", encoding="utf-8") as f:
            f.write(l_content)
        print("Injected instant-butter.js into layout/theme.liquid")

print("\n=== INSTANT BUTTER ACCELERATION ENGINE ACTIVATED GLOBALLY ===")
