import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

extensions = ('*.html', '*.liquid', '*.json', '*.js')
matches = []

for ext in extensions:
    for fpath in glob.glob(os.path.join(root_dir, '**', ext), recursive=True):
        if 'scratch' in fpath or '.git' in fpath:
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f.readlines()):
                if re.search(r'\d+\.00', line):
                    matches.append(f"{os.path.basename(fpath)} L{i+1}: {line.strip()[:100]}")

print(f"Total remaining .00 found: {len(matches)}")
for m in matches[:20]:
    print(m)
