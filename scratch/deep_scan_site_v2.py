import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

pages = [
    "index.html",
    "product.html",
    "ingredients.html",
    "how-to-use.html",
    "reviews.html",
    "ai-consultant.html",
    "track-order.html",
    "contact.html",
    "influencer-affiliate.html",
    "privacy-policy.html",
    "terms.html",
    "refund-policy.html",
    "shipping-policy.html"
]

print("=== DEEP SCANNING BLACKROOTS WEBSITE FOR MOBILE & INTERACTIVE READINESS ===")
issues = []
stats = {
    "total_pages_scanned": 0,
    "links_checked": 0,
    "images_checked": 0,
    "forms_checked": 0
}

for page in pages:
    fpath = os.path.join(root_dir, page)
    if not os.path.exists(fpath):
        issues.append(f"Missing page file: {page}")
        continue

    stats["total_pages_scanned"] += 1
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Check Mobile Navigation Drawer
    if 'id="MobileNavDrawer"' not in content:
        issues.append(f"[{page}] Missing #MobileNavDrawer element")
    if 'id="MobileNavBackdrop"' not in content:
        issues.append(f"[{page}] Missing #MobileNavBackdrop element")
    if 'openMobileNavDrawer()' not in content:
        issues.append(f"[{page}] Missing Hamburger Menu open button")

    # 2. Check Theme Assets Linked
    if 'theme.css' not in content:
        issues.append(f"[{page}] Missing theme.css link")
    if 'theme.js' not in content:
        issues.append(f"[{page}] Missing theme.js script link")

    # 3. Check All Links
    for m in re.finditer(r'href=["\']([^"\']+)["\']', content):
        href = m.group(1)
        stats["links_checked"] += 1
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("https://") or href.startswith("http://") or href.startswith("javascript:"):
            continue
        target = href.split("?")[0].split("#")[0]
        if target:
            target_path = os.path.join(root_dir, target)
            if not os.path.exists(target_path):
                issues.append(f"[{page}] Broken link to '{href}'")

    # 4. Check All Images
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content):
        src = m.group(1)
        stats["images_checked"] += 1
        if src.startswith("data:") or src.startswith("http://") or src.startswith("https://"):
            continue
        img_target = src.replace("./", "")
        img_path = os.path.join(root_dir, img_target)
        if not os.path.exists(img_path):
            issues.append(f"[{page}] Missing image: '{src}'")

    # 5. Check All Forms
    forms = re.findall(r'<form[^>]*>', content)
    stats["forms_checked"] += len(forms)

    # 6. Check Character Encoding & Corrupted Characters
    corruptions = ["œ•", "œ“", "â€¢", "â€”", "â˜", "Ã—", "âœ"]
    for c in corruptions:
        if c in content:
            issues.append(f"[{page}] Found corrupted UTF-8 string: '{c}'")

    # 7. Check Price Formatting (No .00)
    if re.search(r'₹\s*\d+\.00', content) or re.search(r'&#8377;\s*\d+\.00', content) or re.search(r'Rs\.?\s*\d+\.00', content, re.I):
        issues.append(f"[{page}] Contains unwanted '.00' in price display")

print("\n--- SCAN SUMMARY ---")
print(f"Total Pages Checked: {stats['total_pages_scanned']}")
print(f"Total Links Checked: {stats['links_checked']}")
print(f"Total Images Checked: {stats['images_checked']}")
print(f"Total Forms Checked: {stats['forms_checked']}")
print(f"Total Issues Found: {len(issues)}")

for issue in issues:
    print(f"  ❌ {issue}")

if len(issues) == 0:
    print("  ✅ ZERO BROKEN LINKS, ZERO BROKEN IMAGES, ZERO CORRUPTIONS FOUND!")
