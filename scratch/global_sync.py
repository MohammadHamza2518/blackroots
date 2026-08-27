import os
import shutil
import glob

root_dir = r"c:\Users\moham\Downloads\blackroots website"

root_files = [
    "index.html",
    "product.html",
    "ingredients.html",
    "how-to-use.html",
    "reviews.html",
    "ai-consultant.html",
    "track-order.html",
    "contact.html",
    "influencer.html",
    "admin-influencer.html",
    "privacy-policy.html",
    "terms.html",
    "refund-policy.html",
    "shipping-policy.html",
    "mobile-preview.html",
    "product-mobile-preview.html"
]

target_folders = ["demo_lab", "preview"]

for folder in target_folders:
    target_dir = os.path.join(root_dir, folder)
    if not os.path.exists(target_dir):
        continue
    
    # Sync HTML files
    for rf in root_files:
        src = os.path.join(root_dir, rf)
        dst = os.path.join(target_dir, rf)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Synced {rf} -> {folder}/")

    # Sync assets folder
    src_assets = os.path.join(root_dir, "assets")
    dst_assets = os.path.join(target_dir, "assets")
    if os.path.exists(src_assets):
        shutil.copytree(src_assets, dst_assets, dirs_exist_ok=True)
        print(f"Synced assets/ -> {folder}/assets/")

print("\n=== GLOBAL SYNCHRONIZATION COMPLETE ===")
