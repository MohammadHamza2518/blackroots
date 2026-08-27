import os

html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Fixing headers across {len(html_files)} HTML files...")

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        # 1. Fix product.html header Buy Now button
        if 'product.html' in fpath:
            old_p_btn = 'class="js-trigger-order relative overflow-hidden w-full bg-gradient-to-r'
            new_p_btn = 'class="hidden sm:flex js-trigger-order relative overflow-hidden bg-gradient-to-r'
            if old_p_btn in content:
                content = content.replace(old_p_btn, new_p_btn)
                modified = True

        # 2. Fix header CTA buttons across all pages (ensure hidden sm:flex on mobile header)
        h_start = content.find('<header')
        h_end = content.find('</header>')
        if h_start != -1 and h_end != -1:
            header_block = content[h_start:h_end+9]
            if 'btn-gold-luxury' in header_block and 'hidden sm:flex' not in header_block and 'hidden md:flex' not in header_block and 'hidden lg:flex' not in header_block:
                new_header_block = header_block.replace('class="js-trigger-order btn-gold-luxury', 'class="hidden sm:flex js-trigger-order btn-gold-luxury')
                content = content[:h_start] + new_header_block + content[h_end+9:]
                modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"FIXED HEADER IN: {fpath}")
    except Exception as e:
        print(f"Error fixing {fpath}: {e}")
