import os
import glob

root_dir = r"c:\Users\moham\Downloads\blackroots website"
html_files = [os.path.basename(f) for f in glob.glob(os.path.join(root_dir, "*.html"))]
print("All root HTML files:", sorted(html_files))
