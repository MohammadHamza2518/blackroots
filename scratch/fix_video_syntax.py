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

    # Fix the broken > poster="..." pattern
    new_content = re.sub(
        r'>\s*poster=["\']([^"\']+)["\']\s*',
        r' poster="\1">',
        content
    )

    # Double check all video tags are clean: <video autoplay muted loop playsinline webkit-playsinline preload="metadata" poster="..." class="...">
    # Let's normalize reel videos
    reels_fix = {
        'reel-6.mp4': './assets/reel-thumb-6.jpg',
        'reel-3.mp4': './assets/reel-thumb-3.jpg',
        'reel-2.mp4': './assets/reel-thumb-2.jpg',
        'reel-4.mp4': './assets/reel-thumb-4.jpg',
        'reel-1.mp4': './assets/reel-thumb-1.jpg',
        'reel-5.mp4': './assets/reel-thumb-5.jpg'
    }

    for reel, thumb in reels_fix.items():
        # Match <video ...><source src="...reel-X.mp4"...></video>
        pattern = rf'<video([^>]*)>\s*(?:poster=["\'][^"\']*["\'])?\s*<source\s+src=["\'][^"\']*{reel}["\']'
        replacement = rf'<video\1 poster="{thumb}"><source src="./assets/{reel}"'
        new_content = re.sub(pattern, replacement, new_content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed video HTML syntax in", fpath)

