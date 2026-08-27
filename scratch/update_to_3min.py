import os
import glob
import re

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
    
    # 1. Update announcement bar pill from 10 MINUTES to 3 MINUTES
    new_content = new_content.replace('⏱️ 10 MINUTES', '⏱️ 3 MINUTES')
    new_content = new_content.replace('⏱️ 10-MIN RITUAL', '⏱️ 3-MIN RITUAL')
    new_content = new_content.replace('10-MIN RITUAL', '3-MIN RITUAL')
    new_content = new_content.replace('10 MINUTES', '3 MINUTES')
    new_content = new_content.replace('10 Minutes', '3 Minutes')
    new_content = new_content.replace('10-minute', '3-minute')
    new_content = new_content.replace('10-Minute', '3-Minute')
    new_content = new_content.replace('10-Min', '3-Min')
    new_content = new_content.replace('10 min', '3 min')
    new_content = new_content.replace('10 Min', '3 Min')
    new_content = new_content.replace('Easy 10-Min Application', 'Easy 3-Min Application')
    new_content = new_content.replace('Just 10 minutes in your daily shower', 'Just 3 minutes in your daily shower')

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {fpath}")

print(f"Total files updated: {count}")
