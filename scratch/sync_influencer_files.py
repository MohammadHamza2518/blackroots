import os
import shutil

src_root = r"c:\Users\moham\Downloads\blackroots website"

for p in ["influencer.html", "admin-influencer.html"]:
    src = os.path.join(src_root, p)
    for folder in ["demo_lab", "preview"]:
        dst = os.path.join(src_root, folder, p)
        shutil.copy2(src, dst)
        print(f"Synced {p} to {folder}/")

