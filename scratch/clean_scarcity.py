import os
import glob

root_dir = r"c:\Users\moham\Downloads\blackroots website"

extensions = ('*.html', '*.liquid', '*.json', '*.js')
all_files = []
for ext in extensions:
    all_files.extend(glob.glob(os.path.join(root_dir, '**', ext), recursive=True))

count = 0
for fpath in all_files:
    if 'scratch' in fpath or '.git' in fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Replace 31 bottles left with fast dispatch and verified stock
    new_content = new_content.replace('⚡ 31 Bottles Left In Stock • High Demand', '⚡ High Demand • Ready To Dispatch in 24 Hours')
    new_content = new_content.replace('31 Bottles Left In Stock &bull; High Demand', 'High Demand &bull; Ready To Dispatch in 24 Hours')
    new_content = new_content.replace('31 Bottles Left In Stock • High Demand', 'High Demand • Ready To Dispatch in 24 Hours')
    new_content = new_content.replace('⚡ 31 Bottles Left In Stock', '⚡ In Stock • Ready To Dispatch')
    new_content = new_content.replace('31 Bottles Left', 'In Stock • Ready To Dispatch')
    
    # Replace Introductory Offer
    new_content = new_content.replace('Special Introductory Offer', 'Special Brand Offer')
    new_content = new_content.replace('special introductory offer', 'special brand offer')

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Cleaned stock/introductory scarcity from {count} files!")
