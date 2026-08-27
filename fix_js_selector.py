import shutil
import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update the JS grid selector
c = c.replace(
    "const grid = document.querySelector('.grid.grid-cols-1.md\\\\:grid-cols-2') || document.querySelector('.grid');",
    "const grid = document.querySelector('.columns-1');"
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Fixed JS grid selector!")
