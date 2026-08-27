import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check top hero badge
import re
hero_badges = re.findall(r'<div class="inline-flex items-center[^>]*>.*?</div>', html[:3000], re.DOTALL)
print("=== HERO BADGE FOUND ===")
for b in hero_badges:
    print(b.strip())

print("\n=== AI CONSULTANT LINK / SECTION ===")
print("ai-consultant.html link in nav:", "ai-consultant.html" in html)

print("\n=== HOW TO USE / SHOWER RITUAL ===")
print("how-to-use.html link in nav:", "how-to-use.html" in html)
