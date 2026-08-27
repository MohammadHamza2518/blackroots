import shutil, re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove all the photo label badges (the span overlays on photos)
c = re.sub(
    r'\s*<span class="absolute bottom-2 left-2 bg-black/80 backdrop-blur-md text-amber-300 text-\[9px\] font-bold px-2 py-0\.5 rounded-full border border-amber-400/30">📸[^<]*</span>',
    '',
    c
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print('Removed all photo label badges!')
