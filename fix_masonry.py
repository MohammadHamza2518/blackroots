import shutil
import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Replace the grid container with CSS columns
c = c.replace(
    '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">',
    '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">'
)

# 2. Add break-inside-avoid to all cards so they don't break across columns
# The cards currently have this class string:
# class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col" style="height: max-content; align-self: flex-start;"
c = c.replace(
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col" style="height: max-content; align-self: flex-start;"',
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col break-inside-avoid mb-6" style="height: max-content;"'
)

# Also replace the old version if it didn't match exactly
c = c.replace(
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col h-fit"',
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col break-inside-avoid mb-6"'
)
c = c.replace(
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col"',
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col break-inside-avoid mb-6"'
)
# Wait, multiple replaces might add `break-inside-avoid mb-6` multiple times if not careful.
# Let's just use regex to ensure it's added cleanly.

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Applied Masonry layout!")
