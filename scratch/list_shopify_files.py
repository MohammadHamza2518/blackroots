import os
import glob

root_dir = r"c:\Users\moham\Downloads\blackroots website"

folders = ['templates', 'sections', 'snippets', 'layout', 'config', 'locales']

for fld in folders:
    fld_path = os.path.join(root_dir, fld)
    if os.path.exists(fld_path):
        files = os.listdir(fld_path)
        print(f"\n[{fld}/] ({len(files)} files):")
        for f in files:
            print(f"  - {f}")
    else:
        print(f"\n[{fld}/]: DOES NOT EXIST")
