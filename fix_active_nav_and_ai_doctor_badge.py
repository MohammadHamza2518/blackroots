import os, re

# Define exact navbar updates per page
# Standard nav items:
# 1. index.html -> Home
# 2. product.html -> Product (₹499)
# 3. ingredients.html -> Ingredients
# 4. how-to-use.html -> Ritual
# 5. reviews.html -> Reviews
# 6. ai-consultant.html -> AI Doctor
# 7. track-order.html -> Track Order
# 8. contact.html -> Contact

def generate_navbar(active_page):
    links = [
        ('index.html', 'Home'),
        ('product.html', 'Product (&#8377;499)'),
        ('ingredients.html', 'Ingredients'),
        ('how-to-use.html', 'Ritual'),
        ('reviews.html', 'Reviews'),
        ('ai-consultant.html', 'AI Doctor'),
        ('track-order.html', 'Track Order'),
        ('contact.html', 'Contact'),
    ]

    nav_items = []
    for href, label in links:
        is_active = (href == active_page)
        
        if href == 'ai-consultant.html':
            # Unique Pill Badge for AI Doctor
            if is_active:
                item_html = f'<a href="{href}" class="text-xs font-extrabold text-black bg-[#d4af37] px-3.5 py-1.5 rounded-full shadow-lg tracking-wider uppercase whitespace-nowrap transition-all">✨ AI Doctor</a>'
            else:
                item_html = f'<a href="{href}" class="text-xs font-bold text-amber-300 bg-amber-500/10 border border-amber-500/30 hover:bg-amber-400 hover:text-black px-3.5 py-1.5 rounded-full tracking-wider uppercase whitespace-nowrap transition-all shadow-sm">✨ AI Doctor</a>'
        else:
            if is_active:
                item_html = f'<a href="{href}" class="text-xs font-extrabold text-[#d4af37] border-b-2 border-[#d4af37] pb-1 uppercase tracking-wider transition-colors whitespace-nowrap">{label}</a>'
            else:
                item_html = f'<a href="{href}" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors whitespace-nowrap">{label}</a>'
        
        nav_items.append(item_html)

    return f'<nav class="hidden lg:flex items-center gap-4 xl:gap-6 flex-nowrap">\n        ' + '\n        '.join(nav_items) + '\n      </nav>'

# Scan all directories
target_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    if ".git" in root or ".system_generated" in root:
        continue
    for f in files:
        if f.endswith('.html'):
            target_files.append(os.path.join(root, f))

for fpath in target_files:
    fname = os.path.basename(fpath)
    # Determine active page
    active_page = fname
    if active_page not in ['index.html', 'product.html', 'ingredients.html', 'how-to-use.html', 'reviews.html', 'ai-consultant.html', 'track-order.html', 'contact.html']:
        active_page = 'other'

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <nav class="hidden lg:flex... </nav>
    idx_start = content.find('<nav class="hidden lg:flex')
    if idx_start != -1:
        idx_end = content.find('</nav>', idx_start)
        if idx_end != -1:
            new_nav = generate_navbar(active_page)
            content = content[:idx_start] + new_nav + content[idx_end + 6:]
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"UPDATED NAV WITH ACTIVE HIGHLIGHT & AI PILL BADGE IN: {fpath}")

