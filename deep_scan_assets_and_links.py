import os, re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]

print("=== DEEP SCAN 1: IMAGE AND ASSET INTEGRITY AUDIT ===")
missing_assets = []
broken_links = []

for html_file in html_files:
    fpath = os.path.join(root_dir, html_file)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all src="..."
    src_matches = re.findall(r'src=["\']([^"\']+)["\']', content)
    for src in src_matches:
        if src.startswith('http://') or src.startswith('https://') or src.startswith('data:'):
            continue
        
        rel_path = src.lstrip('./').replace('/', os.sep)
        full_asset_path = os.path.join(root_dir, rel_path)
        if not os.path.exists(full_asset_path):
            missing_assets.append((html_file, src, full_asset_path))

    # Find all href="..."
    href_matches = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in href_matches:
        if href.startswith('http://') or href.startswith('https://') or href.startswith('mailto:') or href.startswith('https://wa.me') or href.startswith('#') or href.startswith('javascript:'):
            continue
        
        rel_path = href.lstrip('./').replace('/', os.sep)
        full_link_path = os.path.join(root_dir, rel_path)
        if not os.path.exists(full_link_path):
            broken_links.append((html_file, href, full_link_path))

print(f"Total HTML files scanned: {len(html_files)}")
print(f"Missing Assets Found: {len(missing_assets)}")
for page, src, target in missing_assets:
    print(f"  [MISSING ASSET] in [{page}]: '{src}' -> Target: {target}")

print(f"Broken Local Links Found: {len(broken_links)}")
for page, href, target in broken_links:
    print(f"  [BROKEN LINK] in [{page}]: '{href}' -> Target: {target}")

if len(missing_assets) == 0 and len(broken_links) == 0:
    print("SUCCESS: ALL ASSETS AND LOCAL LINKS EXIST 100% ON DISK!")

