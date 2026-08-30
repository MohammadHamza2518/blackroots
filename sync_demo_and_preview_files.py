import os, shutil

root_dir = r"c:\Users\moham\Downloads\blackroots website"
demo_dir = os.path.join(root_dir, "demo_lab")
preview_dir = os.path.join(root_dir, "preview")

# 1. Update admin/index.html and influencer/index.html from admin.html and influencer.html
with open(os.path.join(root_dir, 'admin.html'), 'r', encoding='utf-8') as f:
    admin_content = f.read()

with open(os.path.join(root_dir, 'influencer.html'), 'r', encoding='utf-8') as f:
    inf_content = f.read()

# admin/index.html uses ../assets/ and ../index.html
admin_sub = admin_content.replace('href="./assets/', 'href="../assets/').replace('src="./assets/', 'src="../assets/')
with open(os.path.join(root_dir, 'admin', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(admin_sub)
print("Updated admin/index.html")

# influencer/index.html uses ../assets/ and ../index.html
inf_sub = inf_content.replace('href="./assets/', 'href="../assets/').replace('src="./assets/', 'src="../assets/').replace('href="./index.html"', 'href="../index.html"')
with open(os.path.join(root_dir, 'influencer', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(inf_sub)
print("Updated influencer/index.html")

# 2. Sync to demo_lab and preview
html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]

for target in [demo_dir, preview_dir]:
    os.makedirs(target, exist_ok=True)

    # Sync assets directory
    root_assets = os.path.join(root_dir, "assets")
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

    # Copy admin folder
    src_admin = os.path.join(root_dir, "admin")
    dst_admin = os.path.join(target, "admin")
    if os.path.exists(src_admin):
        if os.path.exists(dst_admin):
            shutil.rmtree(dst_admin)
        shutil.copytree(src_admin, dst_admin)
        print(f"Synced admin folder to {dst_admin}")

    # Copy influencer folder
    src_inf = os.path.join(root_dir, "influencer")
    dst_inf = os.path.join(target, "influencer")
    if os.path.exists(src_inf):
        if os.path.exists(dst_inf):
            shutil.rmtree(dst_inf)
        shutil.copytree(src_inf, dst_inf)
        print(f"Synced influencer folder to {dst_inf}")

print("All files synchronized successfully!")


