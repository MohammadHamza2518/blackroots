import zipfile, os

root_dir = r"c:\Users\moham\Downloads\blackroots website"
shopify_zip_path = os.path.join(root_dir, "blackroots-shopify-theme.zip")

print("=== BUILDING CLEAN OFFICIAL SHOPIFY THEME ZIP (< 50MB LIMIT) ===")

# Standard Shopify Theme Directory Structure
shopify_dirs = ['assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates']
exclude_exts = ['.zip', '.py', '.mp4'] # Videos are hosted on Shopify CDN Files / external

count = 0
with zipfile.ZipFile(shopify_zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for s_dir in shopify_dirs:
        dir_path = os.path.join(root_dir, s_dir)
        if not os.path.exists(dir_path):
            continue
        for root, dirs, files in os.walk(dir_path):
            for f in files:
                if any(f.endswith(ext) for ext in exclude_exts):
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, root_dir)
                z.write(full_path, rel_path)
                count += 1

zip_size_mb = os.path.getsize(shopify_zip_path) / (1024 * 1024)
print(f"Total files packaged in theme zip: {count}")
print(f"OFFICIAL SHOPIFY THEME ZIP PATH: {shopify_zip_path}")
print(f"Zip Archive Size: {zip_size_mb:.2f} MB")

if zip_size_mb < 50.0:
    print("SUCCESS: THEME ZIP IS 100% CLEAN & UNDER 50MB SHOPIFY LIMIT! READY FOR 1-CLICK SHOPIFY ADMIN UPLOAD!")
else:
    print(f"WARNING: Zip Size is {zip_size_mb:.2f} MB.")


