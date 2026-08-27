import os
import zipfile
import re

zip_path = r"c:\Users\moham\Downloads\blackroots website\blackroots-shopify-theme.zip"

print("=== INSPECTING SHOPIFY THEME ZIP ===")
if not os.path.exists(zip_path):
    print("Zip file not found!")
    exit(1)

size_mb = os.path.getsize(zip_path) / (1024 * 1024)
print(f"Zip File Size: {size_mb:.2f} MB (Shopify Limit: 50.00 MB) -> {'PASS' if size_mb < 50 else 'FAIL'}")

with zipfile.ZipFile(zip_path, 'r') as z:
    file_list = z.namelist()
    print(f"Total files in zip: {len(file_list)}")
    
    # Check essential Shopify directories
    required_dirs = ['layout', 'templates', 'sections', 'snippets', 'assets', 'config', 'locales']
    found_dirs = set()
    for f in file_list:
        parts = f.replace('\\', '/').split('/')
        if len(parts) > 1:
            found_dirs.add(parts[0])
            
    print("Detected Top-Level Directories in Zip:", sorted(list(found_dirs)))
    for req in required_dirs:
        status = "EXISTS" if req in found_dirs else "MISSING"
        print(f"  - {req}/ : {status}")

    # Check key Shopify files
    key_files = [
        'layout/theme.liquid',
        'config/settings_schema.json',
        'config/settings_data.json',
        'locales/en.default.json',
        'templates/index.liquid',
        'templates/product.liquid',
        'templates/page.ingredients.liquid',
        'templates/page.how-to-use.liquid',
        'templates/page.reviews.liquid',
        'templates/page.ai-doctor.liquid',
        'templates/page.track-order.liquid',
        'templates/page.contact.liquid'
    ]
    
    print("\nKey Shopify Theme Files Check:")
    for kf in key_files:
        present = any(f.replace('\\', '/') == kf for f in file_list)
        print(f"  - {kf}: {'OK' if present else 'MISSING'}")

