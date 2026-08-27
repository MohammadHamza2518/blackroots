with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
names = re.findall(r'<h3 class="font-serif[^>]*>([^<]+)</h3>', c)
print(f'Found {len(names)} reviewer names:')
for n in names:
    print(' -', n.strip())
print()
cards = re.findall(r'data-category=', c)
print(f'Total review cards: {len(cards)}')
dates = re.findall(r'data-date=', c)
print(f'Cards with data-date: {len(dates)}')
