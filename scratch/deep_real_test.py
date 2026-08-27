import os
import glob
import re
import urllib.request

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
    "privacy-policy.html",
    "terms.html",
    "refund-policy.html",
    "shipping-policy.html",
    "mobile-preview.html",
    "product-mobile-preview.html"
]

print("================================================================================")
print("       BLACKROOTS COMPREHENSIVE DEEP INTERACTIVE & FUNCTIONALITY AUDIT")
print("================================================================================")

all_errors = []
total_checks = 0

for page in pages:
    fpath = os.path.join(root_dir, page)
    if not os.path.exists(fpath):
        all_errors.append(f"CRITICAL: Page '{page}' does not exist on disk!")
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\nScanning [{page}]...")

    # 1. Check all onclick functions
    onclicks = re.findall(r'onclick=["\']([^"\']+)["\']', content)
    for oc in onclicks:
        total_checks += 1
        # Extract function call name e.g. openMobileNavDrawer(), window.pickAge('young'), etc.
        fn_match = re.match(r'(?:window\.)?([a-zA-Z0-9_$]+)\s*\(', oc.strip())
        if fn_match:
            fn_name = fn_match.group(1)
            # Check if this function is defined in this file or in theme.js or instant-butter.js
            found = False
            # Check in content
            if re.search(rf'function\s+{fn_name}\s*\(', content) or re.search(rf'window\.{fn_name}\s*=', content) or re.search(rf'{fn_name}\s*=\s*function', content):
                found = True
            # Check in theme.js
            with open(os.path.join(root_dir, "assets", "theme.js"), "r", encoding="utf-8") as tj:
                tj_content = tj.read()
                if re.search(rf'function\s+{fn_name}\s*\(', tj_content) or re.search(rf'window\.{fn_name}\s*=', tj_content):
                    found = True
            # Check in instant-butter.js
            with open(os.path.join(root_dir, "assets", "instant-butter.js"), "r", encoding="utf-8") as ib:
                ib_content = ib.read()
                if re.search(rf'function\s+{fn_name}\s*\(', ib_content) or re.search(rf'window\.{fn_name}\s*=', ib_content):
                    found = True

            if not found:
                all_errors.append(f"[{page}] Undefined onclick handler: '{fn_name}()' from: '{oc}'")

    # 2. Check all form onsubmit handlers
    onsubmits = re.findall(r'onsubmit=["\']([^"\']+)["\']', content)
    for osb in onsubmits:
        total_checks += 1
        fn_match = re.match(r'(?:window\.)?([a-zA-Z0-9_$]+)\s*\(', osb.strip())
        if fn_match:
            fn_name = fn_match.group(1)
            found = False
            if re.search(rf'function\s+{fn_name}\s*\(', content) or re.search(rf'window\.{fn_name}\s*=', content):
                found = True
            with open(os.path.join(root_dir, "assets", "theme.js"), "r", encoding="utf-8") as tj:
                if re.search(rf'function\s+{fn_name}\s*\(', tj.read()):
                    found = True
            if not found:
                all_errors.append(f"[{page}] Undefined onsubmit handler: '{fn_name}()' from: '{osb}'")

    # 3. Check all video tags for valid posters and sources
    video_blocks = re.findall(r'<video[^>]*>.*?<\/video>', content, re.DOTALL)
    for vb in video_blocks:
        total_checks += 1
        src_match = re.search(r'src=["\']([^"\']+)["\']', vb)
        poster_match = re.search(r'poster=["\']([^"\']+)["\']', vb)
        
        if not src_match:
            all_errors.append(f"[{page}] Video missing src attribute: {vb[:60]}...")
        else:
            vsrc = src_match.group(1)
            if not vsrc.startswith('http'):
                vpath = os.path.join(root_dir, vsrc.replace('./', ''))
                if not os.path.exists(vpath):
                    all_errors.append(f"[{page}] Video file missing on disk: '{vsrc}'")

        if not poster_match:
            all_errors.append(f"[{page}] Video missing poster attribute: {vb[:60]}...")
        else:
            pimg = poster_match.group(1)
            if not pimg.startswith('http'):
                ppath = os.path.join(root_dir, pimg.replace('./', ''))
                if not os.path.exists(ppath):
                    all_errors.append(f"[{page}] Video poster image missing on disk: '{pimg}'")

    # 4. Check all local images
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for isrc in img_srcs:
        total_checks += 1
        if isrc.startswith('data:') or isrc.startswith('http:') or isrc.startswith('https:') or '${' in isrc:
            continue
        ipath = os.path.join(root_dir, isrc.replace('./', ''))
        if not os.path.exists(ipath):
            all_errors.append(f"[{page}] Image file missing on disk: '{isrc}'")

    # 5. Check all internal links
    links = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in links:
        total_checks += 1
        if href.startswith('#') or href.startswith('mailto:') or href.startswith('tel:') or href.startswith('http:') or href.startswith('https:') or href.startswith('javascript:') or '${' in href:
            continue
        clean_target = href.split('?')[0].split('#')[0]
        if clean_target:
            tpath = os.path.join(root_dir, clean_target)
            if not os.path.exists(tpath):
                all_errors.append(f"[{page}] Broken internal link: '{href}'")

    # 6. Check for unwanted .00 in currency
    if re.search(r'₹\s*\d+\.00', content) or re.search(r'&#8377;\s*\d+\.00', content) or re.search(r'Rs\.?\s*\d+\.00', content, re.I):
        all_errors.append(f"[{page}] Contains unwanted '.00' in price display")

print("\n================================================================================")
print(f"AUDIT COMPLETE: {total_checks} Total Elements, Handlers & Assets Inspected")
print(f"Total Errors Found: {len(all_errors)}")
print("================================================================================")

for i, err in enumerate(all_errors):
    print(f"  {i+1}. {err}")

if len(all_errors) == 0:
    print("\n  >>> RESULT: 100% PERFECT! ZERO BROKEN HANDLERS, ZERO BROKEN IMAGES, ZERO BROKEN LINKS! <<<")
