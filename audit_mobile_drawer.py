import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['index.html', 'product.html', 'how-to-use.html', 'ingredients.html', 'reviews.html', 'ai-consultant.html']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            html = f.read()
        print(f"=== {fname} ===")
        has_drawer = 'id="MobileNavDrawer"' in html
        has_backdrop = 'id="MobileNavBackdrop"' in html
        has_btn = 'openMobileNavDrawer' in html
        print(f"  Drawer markup: {has_drawer}, Backdrop markup: {has_backdrop}, Button onclick: {has_btn}")
    except Exception as e:
        print(f"Error reading {fname}: {e}")
