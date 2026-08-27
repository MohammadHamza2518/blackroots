import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"
index_files = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html")
]

for fpath in index_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove "360° 3D BOTTLE SHOWCASE" pill block
        content = re.sub(
            r'<!-- Center Interactive Hint Pill -->\s*<div class="absolute bottom-20[^>]*>.*?<\/div>',
            '',
            content,
            flags=re.DOTALL
        )

        # Remove all middle "Translucent Tag / AI Rendered Tag" floating blocks above bottom bar
        content = re.sub(
            r'<!-- (?:Translucent Tag|Translucent AI Rendered Tag) -->\s*<div class="absolute bottom-16[^>]*>.*?<\/div>',
            '',
            content,
            flags=re.DOTALL
        )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEANED ALL OVERLAY PILLS IN: {fpath}")

