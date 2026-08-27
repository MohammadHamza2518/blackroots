import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_nav_block = """      <nav class="text-xs text-gray-400 mb-8 flex items-center gap-2">
        <a href="index.html" class="hover:text-amber-400">Home</a>
        <span>/</span>
        <a href="ingredients.html" class="hover:text-amber-400">Hair Care</a>
        <span>/</span>
        <span class="text-amber-400 font-bold">BlackRoots Herbal Hair Dye Shampoo (250ml)</span>
      </nav>"""

new_nav_block = """      <!-- Desktop Clean Breadcrumb -->
      <nav class="hidden sm:flex items-center gap-2 text-xs text-gray-400 mb-8">
        <a href="index.html" class="hover:text-amber-400 transition-colors">Home</a>
        <span>/</span>
        <a href="ingredients.html" class="hover:text-amber-400 transition-colors">Hair Care</a>
        <span>/</span>
        <span class="text-amber-400 font-bold">BlackRoots Herbal Hair Dye Shampoo (250ml)</span>
      </nav>

      <!-- Mobile Clean Native Header Bar (Replaces Clunky Desktop Breadcrumbs) -->
      <div class="flex sm:hidden items-center justify-between mb-4">
        <a href="index.html" class="inline-flex items-center gap-1.5 text-xs text-gray-300 hover:text-amber-300 font-medium bg-white/5 border border-white/10 px-3 py-1.5 rounded-full backdrop-blur-md transition-all active:scale-95">
          <span class="text-amber-400 font-bold">&larr;</span> <span>Back</span>
        </a>
        <span class="text-[10px] text-amber-300 font-extrabold uppercase tracking-widest bg-amber-400/10 border border-amber-400/30 px-3 py-1 rounded-full">
          🌿 250ml Official Edition
        </span>
      </div>"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_nav_block in content:
            content = content.replace(old_nav_block, new_nav_block)
        else:
            # Fallback regex replacement
            content = re.sub(r'<nav class="text-xs text-gray-400 mb-8 flex items-center gap-2">.*?</nav>', new_nav_block, content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED PRODUCT BREADCRUMB IN: {fpath}")
