import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Find all files with text extensions
extensions = ('*.html', '*.liquid', '*.json', '*.js', '*.css')
files_to_check = []
for ext in extensions:
    files_to_check.extend(glob.glob(os.path.join(root_dir, '**', ext), recursive=True))

updated_files = []

for filepath in files_to_check:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'SPECIAL OFFER' in content or 'Special Offer' in content or 'SPECIAL LAUNCH OFFER' in content.upper():
            # Replace SPECIAL OFFER with 50% OFFER
            new_content = content.replace('SPECIAL OFFER', '50% OFFER')
            new_content = new_content.replace('Special Offer', '50% Offer')
            new_content = new_content.replace('Special Launch Offer', '50% Launch Offer')
            new_content = new_content.replace('SPECIAL LAUNCH OFFER', '50% LAUNCH OFFER')

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_files.append(filepath)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

print(f"Updated '50% OFFER' across {len(updated_files)} files:")
for u in updated_files:
    print(" -", u)
