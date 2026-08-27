import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# 1. Delete influencer & admin HTML files
files_to_delete = [
    os.path.join(root_dir, "influencer.html"),
    os.path.join(root_dir, "admin-influencer.html"),
    os.path.join(root_dir, "demo_lab", "influencer.html"),
    os.path.join(root_dir, "demo_lab", "admin-influencer.html"),
    os.path.join(root_dir, "preview", "influencer.html"),
    os.path.join(root_dir, "preview", "admin-influencer.html"),
    os.path.join(root_dir, "templates", "page.influencer.json")
]

for f in files_to_delete:
    if os.path.exists(f):
        os.remove(f)
        print(f"Deleted: {f}")

# 2. Clean up links pointing to influencer.html or admin-influencer.html in all remaining HTML files
html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

for hf in html_files:
    if 'scratch' in hf or '.git' in hf or 'node_modules' in hf:
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Remove link tags to influencer.html or admin-influencer.html
    new_content = re.sub(r'<a[^>]*href=["\'](?:admin-)?influencer\.html["\'][^>]*>.*?<\/a>', '', new_content, flags=re.DOTALL)
    
    # In mobile-preview.html, remove selector options
    new_content = re.sub(r'<option[^>]*value=["\'](?:admin-)?influencer\.html["\'][^>]*>.*?<\/option>', '', new_content)

    if new_content != content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned influencer links from: {os.path.relpath(hf, root_dir)}")

print("\n=== INFLUENCER & ADMIN CODE PURGED CLEANLY FOR MAXIMUM PERFORMANCE ===")
