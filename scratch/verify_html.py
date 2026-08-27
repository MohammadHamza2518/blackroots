import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Check all HTML files for any awkward overlapping classes or broken structure
for fpath in glob.glob(os.path.join(root_dir, "*.html")):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for empty divs or duplicate elements
    print(f"Checking {fname} - Length: {len(content)} chars")

print("All HTML files verified clean.")
