import shutil
import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the fixed height of 160px with aspect-square to show the full photo without cropping it too much horizontally
c = c.replace(
    'class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60" style="height:160px"',
    'class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60" style="aspect-ratio: 1/1; max-height: 300px;"'
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Fixed review photos aspect ratio!")
