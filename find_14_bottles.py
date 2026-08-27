import glob
import re

print("=== FINDING 14 BOTTLES & LIVE VISITORS ===")

for f in glob.glob('*.html') + glob.glob('demo_lab/*.html') + glob.glob('preview/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Find 14 Bottles
    found_14 = re.findall(r'\b14\s+Bottles?\b', content, flags=re.IGNORECASE)
    if found_14:
        print(f"{f}: Found {len(found_14)} matches of '14 Bottles'")
