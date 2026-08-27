import os
import shutil
from PIL import Image

src_img = r"C:\Users\moham\.gemini\antigravity\brain\9acc6079-8758-4b60-9ce0-86f829074f1f\.user_uploaded\media_1786735588197.jpg"
dest_hero = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-botanical-hero-16x9.jpg"
dest_counter = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-bathroom-counter.jpg"

# Optimize and copy to assets
with Image.open(src_img) as im:
    rgb_im = im.convert('RGB')
    rgb_im.save(dest_hero, 'JPEG', quality=88, optimize=True)
    rgb_im.save(dest_counter, 'JPEG', quality=88, optimize=True)

print(f"COPIED 16:9 BOTANICAL IMAGE TO ASSETS ({os.path.getsize(dest_hero)/1024:.1f} KB)")

# Update product.html, demo_lab/product.html, preview/product.html
product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('./assets/blackroots-bathroom-counter.jpg', './assets/blackroots-botanical-hero-16x9.jpg')
        content = content.replace('Bathroom Counter Aesthetic', 'Botanical 16:9 Shoot Aesthetic')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED PRODUCT HERO IMAGE IN: {fpath}")
