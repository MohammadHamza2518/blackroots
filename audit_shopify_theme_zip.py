import zipfile, os, sys

sys.stdout.reconfigure(encoding='utf-8')
zip_path = r"c:\Users\moham\Downloads\blackroots website\blackroots-shopify-theme.zip"

print("=== DEEP SCAN 2: SHOPIFY THEME ZIP INTEGRITY AUDIT (OS 2.0) ===")

if not os.path.exists(zip_path):
    print("[ERROR] blackroots-shopify-theme.zip does not exist!")
else:
    z = zipfile.ZipFile(zip_path, 'r')
    file_list = [f.replace('\\', '/') for f in z.namelist()]
    
    required_files = [
        'layout/theme.liquid',
        'templates/index.json',
        'templates/product.json',
        'templates/page.reviews.json',
        'config/settings_schema.json',
        'config/settings_data.json',
        'locales/en.default.json',
        'assets/theme.css',
        'assets/theme.js'
    ]

    print(f"Total files in Zip Archive: {len(file_list)}")
    print(f"Zip Archive Size: {os.path.getsize(zip_path) / (1024*1024):.2f} MB")

    missing = []
    for req in required_files:
        if req not in file_list:
            missing.append(req)

    if missing:
        print("[ERROR] MISSING REQUIRED SHOPIFY THEME FILES:")
        for m in missing:
            print(f"   - {m}")
    else:
        print("[SUCCESS] ALL REQUIRED SHOPIFY LIQUID & OS 2.0 JSON THEME STRUCTURE FILES ARE PRESENT!")

    print("\nTop 15 Files in Zip Archive:")
    for f in sorted(file_list)[:15]:
        print(f"  • {f}")


