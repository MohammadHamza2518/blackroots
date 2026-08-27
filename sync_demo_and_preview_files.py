import os, shutil

root_dir = r"c:\Users\moham\Downloads\blackroots website"
demo_dir = os.path.join(root_dir, "demo_lab")
preview_dir = os.path.join(root_dir, "preview")

# Root HTML files to sync
html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]

print("Syncing HTML files and assets to demo_lab and preview...")

# 1. Sync assets directory
root_assets = os.path.join(root_dir, "assets")

for target in [demo_dir, preview_dir]:
    if not os.path.exists(target):
        os.makedirs(target)
    
    target_assets = os.path.join(target, "assets")
    if os.path.exists(root_assets):
        if os.path.exists(target_assets):
            shutil.rmtree(target_assets)
        shutil.copytree(root_assets, target_assets)
        print(f"Synced assets to {target_assets}")

    # Copy HTML files
    for hf in html_files:
        src_path = os.path.join(root_dir, hf)
        dst_path = os.path.join(target, hf)
        shutil.copy2(src_path, dst_path)
        print(f"Synced {hf} to {target}")

print("Synchronization complete!")

