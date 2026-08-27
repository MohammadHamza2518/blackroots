import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

extensions = ('*.html', '*.liquid', '*.json', '*.js')
results = []

for ext in extensions:
    for fpath in glob.glob(os.path.join(root_dir, '**', ext), recursive=True):
        if 'scratch' in fpath or '.git' in fpath:
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f.readlines()):
                if re.search(r'\b10\s*[-–]?\s*min', line, re.IGNORECASE):
                    results.append((os.path.basename(fpath), fpath, i+1, line.strip()))

print(f"Total 10-min occurrences found: {len(results)}")
for r in results:
    try:
        print(f"[{r[0]}:L{r[2]}] {r[3][:100]}")
    except Exception:
        print(f"[{r[0]}:L{r[2]}] (Unicode string)")
