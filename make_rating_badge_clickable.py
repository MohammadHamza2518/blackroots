import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_rating_block = """            <div class="flex items-center gap-2 mb-3">
              <div class="flex items-center text-amber-400">★★★★★</div>
              <span class="text-sm font-bold text-white">4.9 / 5.0</span>
              <span class="text-xs text-gray-400">(1,280+ Verified Indian Reviews)</span>
            </div>"""

new_rating_block = """            <a href="reviews.html" class="inline-flex items-center gap-2 mb-3 cursor-pointer group hover:opacity-90 transition-all" title="Click to view all 1,280+ Verified Customer Reviews">
              <div class="flex items-center text-amber-400 text-sm group-hover:scale-105 transition-transform">★★★★★</div>
              <span class="text-sm font-bold text-white group-hover:text-amber-300 transition-colors">4.9 / 5.0</span>
              <span class="text-xs text-gray-400 group-hover:text-amber-400 group-hover:underline transition-colors">(1,280+ Verified Indian Reviews &rarr;)</span>
            </a>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_rating_block in content:
            content = content.replace(old_rating_block, new_rating_block)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"MADE RATING BADGE CLICKABLE (AMAZON/FLIPKART STYLE) IN: {fpath}")

