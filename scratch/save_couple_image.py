import os
from PIL import Image

src_img = r"C:\Users\moham\.gemini\antigravity\brain\f7203594-97f5-4091-912c-258b263457b4\.user_uploaded\media_1786801918612.jpg"
dest_asset = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-lifestyle-couple-1x1.jpg"

if os.path.exists(src_img):
    img = Image.open(src_img)
    print(f"Source size: {img.size}, mode: {img.mode}")
    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    # Save optimized 1024x1024 square JPEG
    img_resized = img.resize((1024, 1024), Image.Resampling.LANCZOS)
    img_resized.save(dest_asset, 'JPEG', quality=95, optimize=True)
    print(f"Saved optimized image to: {dest_asset}")
else:
    print(f"ERROR: Source image not found at {src_img}")
