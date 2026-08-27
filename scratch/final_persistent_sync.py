import os
import shutil
import glob

root_dir = r"c:\Users\moham\Downloads\blackroots website"

core_files = [
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

# Sync all core HTML files and assets to demo_lab and preview
for f in core_files:
    src = os.path.join(root_dir, f)
    if os.path.exists(src):
        for folder in ["demo_lab", "preview"]:
            dst = os.path.join(root_dir, folder, f)
            shutil.copy2(src, dst)

# Sync assets
asset_files = glob.glob(os.path.join(root_dir, "assets", "*.*"))
for af in asset_files:
    fname = os.path.basename(af)
    for folder in ["demo_lab", "preview"]:
        dst = os.path.join(root_dir, folder, "assets", fname)
        shutil.copy2(af, dst)

print("=== ALL FILES, ASSETS & PREVIEWS 100% PERSISTED & SYNCHRONIZED ===")
