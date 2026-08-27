with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
names = re.findall(r'class="font-serif text-base font-bold text-white leading-snug">([^<]+)</h3>', c)
print(f'All reviewer names ({len(names)}):')
for n in names:
    print(' -', n.strip())

# Count data-category
cats = re.findall(r'data-category=', c)
print(f'\nTotal review cards with data-category: {len(cats)}')
