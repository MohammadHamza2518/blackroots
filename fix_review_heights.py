import shutil

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove the forced min-height on review cards
c = c.replace(' style="min-height:340px"', '')

# 2. Remove the flex-1 from space-y-3 so it doesn't try to fill the stretched height
c = c.replace('class="space-y-3 flex-1"', 'class="space-y-3"')

# 3. Remove the dummy quote block that was taking up the empty space
dummy_quote = '<div class="flex-1 flex items-center justify-center py-4"><span class="text-5xl text-white/5 font-serif font-bold select-none">"</span></div>'
c = c.replace(dummy_quote, '')
c = c.replace('\n            ' + dummy_quote, '')

# 4. Make the grid align-items: start so cards are only as tall as their content, rather than stretching to match the tallest card in the row
c = c.replace(
    '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">',
    '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">'
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Fixed review card heights and removed dummy blocks!")
