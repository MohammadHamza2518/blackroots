import shutil

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace h-fit with inline styles because the precompiled Tailwind CSS might not have h-fit or items-start
c = c.replace(
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col h-fit"',
    'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col" style="height: max-content; align-self: flex-start;"'
)

# Also ensure no min-height inline styles remain (just in case)
c = c.replace(' style="min-height:340px"', '')

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Inline styles applied!")
