import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

clean_thumb_6 = """            <!-- Thumb 6: Luxury Video Reel Player (Position #6) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer relative group flex items-center justify-center shadow-lg active:scale-95" onclick="changeMainProductImage(this, './assets/reel-2.mp4', true)" title="Watch Product Video">
              <!-- Video Poster Image -->
              <img src="./assets/reel-thumb-2.jpg" alt="Watch Product Video" class="w-full h-full object-cover rounded-lg group-hover:scale-105 transition-transform duration-300">
              
              <!-- Subtle Dark Vignette Overlay -->
              <div class="absolute inset-0 bg-black/40 group-hover:bg-black/20 transition-colors rounded-lg"></div>

              <!-- Single Clean Centered Gold Play Button -->
              <div class="absolute inset-0 flex items-center justify-center pointer-events-none">
                <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-[#d4af37] text-black flex items-center justify-center shadow-[0_4px_15px_rgba(212,175,55,0.6)] transform group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-3.5 h-3.5 fill-current translate-x-0.5" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z"/>
                  </svg>
                </div>
              </div>
            </button>"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(r'<!-- Thumb 6:.*?onclick="changeMainProductImage\(this,\s*\'\./assets/reel-2\.mp4\',\s*true\)".*?</button>', clean_thumb_6.strip(), content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEANED VIDEO THUMBNAIL IN: {fpath}")
