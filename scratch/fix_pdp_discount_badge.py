import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Update PDPBadgeDisplay markup
    new_content = re.sub(
        r'<span id="PDPBadgeDisplay"[^>]*>.*?<\/span>',
        '<span id="PDPBadgeDisplay" class="px-3 py-1.5 rounded-full bg-amber-500/20 text-amber-300 text-[11px] sm:text-xs font-extrabold border border-amber-500/40 shadow-sm shrink-0 whitespace-nowrap text-center">🔥 50% OFF &bull; Save &#8377;500</span>',
        new_content,
        flags=re.DOTALL
    )

    # 2. Update data-badge attributes
    new_content = new_content.replace(
        'data-badge="50% OFF &mdash; SAVE &#8377;500"',
        'data-badge="🔥 50% OFF &bull; Save &#8377;500"'
    )
    new_content = new_content.replace(
        'data-badge="60% OFF &mdash; SAVE &#8377;1,199"',
        'data-badge="🔥 60% OFF &bull; Save &#8377;1,199"'
    )

    # 3. Update JS fallback string
    new_content = new_content.replace(
        "const badge = this.getAttribute('data-badge') || '50% OFF — SAVE ₹500';",
        "const badge = this.getAttribute('data-badge') || '🔥 50% OFF • Save ₹500';"
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated discount badge in", fpath)

