import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Find all html and liquid files
files_to_check = []
for ext in ('*.html', '*.liquid', '*.json', '*.js'):
    files_to_check.extend(glob.glob(os.path.join(root_dir, '**', ext), recursive=True))

updated_files = []

for filepath in files_to_check:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'blackroots-flatlay-herbs-1x1.jpg' in content:
            new_content = content.replace('blackroots-flatlay-herbs-1x1.jpg', 'blackroots-lifestyle-couple-1x1.jpg')
            # Also update alt tag if present
            new_content = new_content.replace('Herbal Ingredients Flatlay 1:1', 'Real Indian Couple with BlackRoots Shampoo 1:1')
            new_content = new_content.replace('Flatlay Herbs Table 1:1', 'Real Indian Couple Showcase 1:1')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.append(filepath)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print("Updated the following files:")
for u in updated_files:
    print(" -", u)
