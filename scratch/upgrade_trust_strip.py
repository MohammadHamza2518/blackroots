import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

clean_guarantee_strip = """            <!-- High-Trust Brand Guarantee Strip -->
            <div class="p-3.5 rounded-2xl bg-[#12151c] border border-[#d4af37]/40 flex flex-wrap items-center justify-center gap-2.5 sm:gap-4 text-center text-xs shadow-lg">
              <div class="inline-flex items-center gap-1.5 text-amber-300 font-bold">
                <span>🛡️</span> <span>100% Herbal Guaranteed</span>
              </div>
              <span class="text-white/20 hidden sm:inline">&bull;</span>
              <div class="inline-flex items-center gap-1.5 text-emerald-400 font-bold">
                <span>⚡</span> <span>Dispatched in 24h</span>
              </div>
              <span class="text-white/20 hidden sm:inline">&bull;</span>
              <div class="inline-flex items-center gap-1.5 text-gray-300 font-medium">
                <span>🚚</span> <span>Free Express Delivery</span>
              </div>
            </div>"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Replace the Harmonious Quality Guarantee Box
    pattern = r'<!-- Harmonious Quality Guarantee Box -->.*?<span>.*?100% Herbal Quality Guaranteed.*?<\/span>\s*<\/div>'
    new_content = re.sub(pattern, clean_guarantee_strip, new_content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Upgraded trust guarantee strip in", fpath)

