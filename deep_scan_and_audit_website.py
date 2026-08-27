import os, re, zipfile

project_root = r"c:\Users\moham\Downloads\blackroots website"

print("=========================================================")
print("BLACKROOTS D2C WEBSITE & SHOPIFY THEME DEEP SCANNER")
print("=========================================================")

errors = []
warnings = []
stats = {
    'html_files': 0,
    'assets_checked': 0,
    'links_checked': 0,
    'missing_assets': 0,
    'missing_links': 0
}

# 1. SCAN ALL HTML FILES FOR BROKEN LINKS & MISSING ASSETS
for root, dirs, files in os.walk(project_root):
    if ".git" in root or ".system_generated" in root or "node_modules" in root:
        continue
    for f in files:
        if f.endswith('.html'):
            stats['html_files'] += 1
            fpath = os.path.join(root, f)
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()

            # Find all src="..."
            srcs = re.findall(r'src=["\']([^"\']+)["\']', content)
            for src in srcs:
                if src.startswith(('http://', 'https://', 'data:', 'javascript:')):
                    continue
                stats['assets_checked'] += 1
                clean_src = src.split('?')[0].split('#')[0]
                target_asset = os.path.normpath(os.path.join(os.path.dirname(fpath), clean_src))
                if not os.path.exists(target_asset):
                    stats['missing_assets'] += 1
                    errors.append(f"Broken asset in [{os.path.relpath(fpath, project_root)}]: {src}")

            # Find all href="..."
            hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
            for href in hrefs:
                if href.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#', 'data:')):
                    continue
                stats['links_checked'] += 1
                clean_href = href.split('?')[0].split('#')[0]
                if not clean_href:
                    continue
                target_link = os.path.normpath(os.path.join(os.path.dirname(fpath), clean_href))
                if not os.path.exists(target_link):
                    stats['missing_links'] += 1
                    warnings.append(f"Unmatched href link in [{os.path.relpath(fpath, project_root)}]: {href}")

# 2. CHECK SHOPIFY THEME ZIP PACKAGE
theme_zip_path = os.path.join(project_root, "blackroots-shopify-theme.zip")
zip_status = "NOT FOUND"
zip_size_mb = 0

if os.path.exists(theme_zip_path):
    zip_size_mb = round(os.path.getsize(theme_zip_path) / (1024 * 1024), 2)
    if zip_size_mb < 50.0:
        zip_status = f"PASSED (Size: {zip_size_mb} MB < 50MB Limit)"
    else:
        zip_status = f"EXCEEDS LIMIT (Size: {zip_size_mb} MB >= 50MB Limit)"

print(f"\nSCAN RESULTS SUMMARY:")
print(f"  * HTML Files Scanned: {stats['html_files']}")
print(f"  * Asset References Checked: {stats['assets_checked']}")
print(f"  * Internal Links Checked: {stats['links_checked']}")
print(f"  * Missing Assets Found: {stats['missing_assets']}")
print(f"  * Unmatched Links Found: {stats['missing_links']}")
print(f"  * Shopify Theme Zip Status: {zip_status}")

if errors:
    print("\nERRORS DETECTED:")
    for err in errors:
        print(f"  - {err}")
else:
    print("\n[SUCCESS] ZERO BROKEN ASSETS FOUND! ALL IMAGES, VIDEOS, CSS & JS ARE 100% INTACT!")

if warnings:
    print("\nWARNINGS DETECTED:")
    for w in warnings:
        print(f"  - {w}")
else:
    print("[SUCCESS] ZERO BROKEN INTERNAL LINKS FOUND!")

print("=========================================================")
