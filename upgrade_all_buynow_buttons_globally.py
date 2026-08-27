import os, re

# Pattern 1: Header nav Buy Now buttons e.g.:
# <a href="product.html" ...>Buy Now &mdash; &#8377;499.00 &rarr;</a>
# Replace &rarr; or → with Shopping Bag SVG Icon

shopping_bag_svg_small = '<svg class="w-4 h-4 text-black shrink-0 inline-block -mt-0.5 ml-1" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>'
shopping_bag_svg_medium = '<svg class="w-5 h-5 text-black shrink-0 inline-block -mt-0.5 ml-1.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>'

target_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    if ".git" in root or ".system_generated" in root:
        continue
    for f in files:
        if f.endswith('.html'):
            target_files.append(os.path.join(root, f))

print(f"Scanning {len(target_files)} HTML files...")

shopping_bag_icon_svg = '<svg class="w-5 h-5 text-black shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>'

for fpath in target_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Header Buy Now button replacement
    # Buy Now &mdash; &#8377;499.00 &rarr; OR Buy Now &mdash; &#8377;499.00 &rarr;
    content = re.sub(
        r'Buy Now &mdash; (&#8377;|₹)499\.00\s*(&rarr;|→)?',
        f'<span>Buy Now &mdash; \\1 499.00</span> {shopping_bag_svg_small}',
        content
    )

    # 2. Hero & Section Buy Now Buttons replacement (e.g., Buy Now (250ml Bottle) — ₹499.00 →)
    content = re.sub(
        r'Buy Now \((250ml Bottle|500ml Pack)\) &mdash; (&#8377;|₹)499\.00\s*(&rarr;|→)?',
        f'<span>Buy Now (\\1) &mdash; \\2 499.00</span> {shopping_bag_svg_medium}',
        content
    )

    # Clean any double svgs or extra spaces if any
    content = content.replace('</span> </span>', '</span>')
    
    if content != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED BUY NOW BUTTONS IN: {fpath}")

