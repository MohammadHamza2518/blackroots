import re
from collections import Counter

with open('reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'src=["\'](\./assets/reviews/[^"\']+)["\']', content)
counts = Counter(matches)
print("--- ALL DUPLICATE REVIEW IMAGES ---")
for path, count in counts.items():
    if count > 1:
        print(f"{count}x -> {path}")
