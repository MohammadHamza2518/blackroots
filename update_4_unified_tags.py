import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

new_4_tags_html = """            <!-- Badges Pill Row (4 Symmetrical Tags • 100% Unified Minimalist Style) -->
            <div class="flex flex-wrap items-center gap-2 mb-5">
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-[11px] font-bold uppercase tracking-wide">
                <span>🇯🇵</span> <span>Japanese Inspired</span>
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-[11px] font-bold uppercase tracking-wide">
                <span>🌿</span> <span>250ml Net Vol</span>
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-[11px] font-bold uppercase tracking-wide">
                <span>👫</span> <span>100% Unisex</span>
              </span>
              <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-[11px] font-bold uppercase tracking-wide">
                <span>🛡️</span> <span>Zero Ammonia</span>
              </span>
            </div>"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'<!-- Badges Pill Row.*?<\/div>'
        content = re.sub(pattern, new_4_tags_html.strip(), content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED 4 UNIFIED TAGS IN: {fpath}")
