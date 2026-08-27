import os
import glob

root_dir = r"c:\Users\moham\Downloads\blackroots website\assets"
files = glob.glob(os.path.join(root_dir, "*reel*"))
for f in files:
    print(os.path.basename(f))
