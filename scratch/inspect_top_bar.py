import glob

for f in ["index.html", "product.html", "mobile-preview.html", "product-mobile-preview.html"]:
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if '50% OFFER' in line or 'Introductory Price' in line or 'android-status-bar' in line:
            print(f"{f} Line {i+1}: {line.strip()}")
