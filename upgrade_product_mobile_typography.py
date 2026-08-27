import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_header_block = """            <a href="reviews.html" class="inline-flex items-center gap-2 mb-3 cursor-pointer group hover:opacity-90 transition-all" title="Click to view all 1,280+ Verified Customer Reviews">
              <div class="flex items-center text-amber-400 text-sm group-hover:scale-105 transition-transform">★★★★★</div>
              <span class="text-sm font-bold text-white group-hover:text-amber-300 transition-colors">4.9 / 5.0</span>
              <span class="text-xs text-gray-400 group-hover:text-amber-400 group-hover:underline transition-colors">(1,280+ Verified Indian Reviews &rarr;)</span>
            </a>

            <h1 class="font-serif text-3xl sm:text-4xl font-bold text-white mb-2 leading-tight">
              BlackRoots Herbal Hair Dye Shampoo
            </h1>
            <div class="flex flex-wrap items-center gap-2.5 mb-5">
              <span class="text-xs tracking-widest text-amber-400 font-bold uppercase">
                Japanese Inspired Formulation &bull; Net Vol: 250 ml
              </span>
              <span class="text-gray-500 hidden sm:inline">&bull;</span>
              <span class="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-amber-400/10 border border-amber-400/30 text-amber-300 text-xs font-bold uppercase tracking-wider">
                👫 100% Unisex (Men & Women)
              </span>
            </div>"""

new_header_block = """            <!-- Reviews Rating Bar -->
            <a href="reviews.html" class="inline-flex items-center gap-2 mb-3 cursor-pointer group hover:opacity-90 transition-all" title="Click to view all 1,280+ Verified Customer Reviews">
              <div class="flex items-center text-amber-400 text-xs sm:text-sm tracking-tighter">★★★★★</div>
              <span class="text-xs sm:text-sm font-black text-white group-hover:text-amber-300 transition-colors">4.9/5.0</span>
              <span class="text-[11px] sm:text-xs text-gray-400 group-hover:text-amber-400 transition-colors">(1,280+ Verified Reviews &rarr;)</span>
            </a>

            <!-- Modern Luxury Product Title -->
            <h1 class="text-2xl sm:text-3xl lg:text-4xl font-black text-white tracking-tight leading-tight mb-3">
              BlackRoots Herbal Hair Dye Shampoo
            </h1>

            <!-- Badges Pill Row (Mobile Optimized • No Awkward Line Breaks) -->
            <div class="flex flex-wrap items-center gap-2 mb-5">
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-[#d4af37]/15 border border-[#d4af37]/40 text-[#f5d77f] text-[11px] font-extrabold uppercase tracking-wide">
                <span>🇯🇵</span> <span>Japanese Inspired</span>
              </span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-[11px] font-bold uppercase tracking-wide">
                <span>🌿</span> <span>250ml Net Vol</span>
              </span>
              <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-white/5 border border-white/10 text-gray-300 text-[11px] font-bold uppercase tracking-wide">
                <span>👫</span> <span>100% Unisex</span>
              </span>
            </div>"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_header_block in content:
            content = content.replace(old_header_block, new_header_block)
        else:
            pattern = r'<a href="reviews\.html".*?<!-- Price Display'
            # fallback
            content = re.sub(r'<a href="reviews\.html".*?👫 100% Unisex \(Men & Women\)\s*<\/span>\s*<\/div>', new_header_block.strip(), content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED MOBILE TYPOGRAPHY IN: {fpath}")
