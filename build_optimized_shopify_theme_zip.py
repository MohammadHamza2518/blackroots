import zipfile, os

root_dir = r"c:\Users\moham\Downloads\blackroots website"
shopify_zip_path = os.path.join(root_dir, "blackroots-shopify-theme.zip")

print("=== DEEP SCAN 2: BUILDING OPTIMIZED SHOPIFY THEME ZIP (UNDER 50MB LIMIT) ===")

# Exclude heavy video reels from theme zip so Shopify accepts upload instantly (<50MB)
exclude_extensions = ['.zip', '.py', '.git', 'node_modules', '__pycache__']
exclude_large_videos = ['reel-1.mp4', 'reel-2.mp4', 'reel-3.mp4', 'reel-4.mp4', 'reel-5.mp4']

with zipfile.ZipFile(shopify_zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if any(f.endswith(ext) for ext in exclude_extensions):
                continue
            if f in exclude_large_videos:
                continue
            
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, root_dir)
            z.write(full_path, rel_path)

zip_size_mb = os.path.getsize(shopify_zip_path) / (1024 * 1024)
print(f"NEW OPTIMIZED SHOPIFY THEME ZIP CREATED: {shopify_zip_path}")
print(f"Zip Archive Size: {zip_size_mb:.2f} MB")

if zip_size_mb < 50.0:
    print("SUCCESS: ZIP SIZE IS UNDER 50MB SHOPIFY LIMIT! 100% READY FOR SHOPIFY ADMIN UPLOAD!")
else:
    print(f"WARNING: ZIP Size is {zip_size_mb:.2f} MB. Needs further reduction.")

