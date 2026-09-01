import os
import shutil

src_root = r"c:\Users\moham\Downloads\blackroots website"

def convert_to_subdir(html_text):
    text = html_text
    replacements = [
        ('href="./assets/', 'href="../assets/'),
        ('src="./assets/', 'src="../assets/'),
        ('href="./favicon.ico"', 'href="../favicon.ico"'),
        ('href="./site.webmanifest"', 'href="../site.webmanifest"'),
        ('href="./index.html"', 'href="../index.html"'),
        ('href="./product.html"', 'href="../product.html"'),
        ('href="./checkout.html"', 'href="../checkout.html"'),
        ('href="./track-order.html"', 'href="../track-order.html"'),
        ('href="./admin.html"', 'href="../admin.html"'),
        ('href="./influencer.html"', 'href="../influencer.html"'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

admin_path = os.path.join(src_root, 'admin.html')
with open(admin_path, 'r', encoding='utf-8') as f:
    admin_src = f.read()

admin_idx_path = os.path.join(src_root, 'admin', 'index.html')
with open(admin_idx_path, 'w', encoding='utf-8') as f:
    f.write(convert_to_subdir(admin_src))

inf_path = os.path.join(src_root, 'influencer.html')
with open(inf_path, 'r', encoding='utf-8') as f:
    inf_src = f.read()

inf_idx_path = os.path.join(src_root, 'influencer', 'index.html')
with open(inf_idx_path, 'w', encoding='utf-8') as f:
    f.write(convert_to_subdir(inf_src))

for folder in ['preview', 'demo_lab']:
    folder_path = os.path.join(src_root, folder)
    if os.path.exists(folder_path):
        shutil.copy2(admin_path, os.path.join(folder_path, 'admin.html'))
        shutil.copy2(inf_path, os.path.join(folder_path, 'influencer.html'))
        shutil.copy2(os.path.join(src_root, 'checkout.html'), os.path.join(folder_path, 'checkout.html'))
        
        os.makedirs(os.path.join(folder_path, 'admin'), exist_ok=True)
        os.makedirs(os.path.join(folder_path, 'influencer'), exist_ok=True)
        shutil.copy2(admin_idx_path, os.path.join(folder_path, 'admin', 'index.html'))
        shutil.copy2(inf_idx_path, os.path.join(folder_path, 'influencer', 'index.html'))
        print(f"Synced files to {folder}/")

print("All files synchronized successfully!")


