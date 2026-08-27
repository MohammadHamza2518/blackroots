import os
import re

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content

    # 1. Fix single photo container in static and dynamic cards
    new_content = re.sub(
        r'<div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60[^"]*"\s*style="aspect-ratio:\s*1/1;\s*max-height:\s*300px;">',
        '<div class="w-full rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mx-auto mt-2" style="aspect-ratio: 1/1; width: 100%; max-width: 100%;">',
        new_content
    )

    # 2. In createCardElement (JavaScript dynamic generator)
    new_content = new_content.replace(
        '<div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;">',
        '<div class="w-full rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mx-auto mt-3" style="aspect-ratio: 1/1; width: 100%; max-width: 100%;">'
    )

    # 3. In Hero reviews (Sunita, Alok, Anita)
    new_content = re.sub(
        r'<div class="relative rounded-xl overflow-hidden border border-white/10 bg-black/60 shadow-md"\s*style="aspect-ratio:\s*1/1;">',
        '<div class="w-full relative rounded-xl overflow-hidden border border-white/10 bg-black/60 shadow-md" style="aspect-ratio: 1/1; width: 100%; max-width: 100%;">',
        new_content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Centered photos in {fpath}")

