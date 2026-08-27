import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

liquid_files = glob.glob(os.path.join(root_dir, "**", "*.liquid"), recursive=True)
json_files = glob.glob(os.path.join(root_dir, "**", "*.json"), recursive=True)

all_theme_files = liquid_files + json_files

print(f"=== SCANNING {len(all_theme_files)} SHOPIFY THEME FILES FOR COPY & FORMATTING ACCURACY ===")

issues = []

for tf in all_theme_files:
    if 'scratch' in tf or '.git' in tf or 'node_modules' in tf:
        continue
    rel_path = os.path.relpath(tf, root_dir)
    with open(tf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Check for 10 minutes
    if re.search(r'10[\s-]*(?:min|minute)', content, re.I):
        # check if it's not a color code or something
        matches = re.findall(r'.{0,30}10[\s-]*(?:min|minute).{0,30}', content, re.I)
        issues.append(f"[{rel_path}] Contains '10 minutes' reference: {matches}")

    # 2. Check for launch offer / 31 bottles
    if re.search(r'31\s*bottle', content, re.I):
        issues.append(f"[{rel_path}] Contains '31 bottles left' reference")
    if re.search(r'launch\s*offer', content, re.I):
        issues.append(f"[{rel_path}] Contains 'launch offer' reference")

    # 3. Check for .00 in currency
    if re.search(r'₹\s*\d+\.00', content) or re.search(r'&#8377;\s*\d+\.00', content):
        matches = re.findall(r'.{0,20}(?:₹|&#8377;)\s*\d+\.00.{0,20}', content)
        issues.append(f"[{rel_path}] Contains '.00' in price: {matches}")

    # 4. Check for corrupted characters
    corruptions = ["œ•", "œ“", "â€¢", "â€”", "â˜", "Ã—", "âœ"]
    for c in corruptions:
        if c in content:
            issues.append(f"[{rel_path}] Contains corrupted string '{c}'")

print(f"\nTotal Issues Found in Shopify Theme Files: {len(issues)}")
for i, issue in enumerate(issues):
    print(f"  {i+1}. {issue}")

if len(issues) == 0:
    print("  ✅ 100% PERFECT: NO '10 MIN', NO '31 BOTTLES', NO 'LAUNCH OFFER', NO '.00', NO CORRUPTIONS!")

