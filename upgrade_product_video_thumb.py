import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_thumb_6 = """            <!-- Thumb 6: Interactive Reel Video Player (Position #6) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-gradient-to-br from-[#12151c] to-black border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer relative group flex flex-col items-center justify-center shadow-lg" onclick="changeMainProductImage(this, './assets/reel-2.mp4', true)">
              <div class="absolute inset-0 bg-cover bg-center opacity-40 group-hover:opacity-60 transition-opacity" style="background-image: url('./assets/blackroots-bottle-single.png');"></div>
              <div class="relative z-10 w-7 h-7 rounded-full bg-[#d4af37] text-black flex items-center justify-center shadow-md transform group-hover:scale-110 transition-transform">
                <svg class="w-3.5 h-3.5 fill-current translate-x-0.5" viewBox="0 0 24 24">
                  <path d="M8 5v14l11-7z"/>
                </svg>
              </div>
              <span class="relative z-10 text-[8px] sm:text-[9px] text-amber-300 font-extrabold mt-1 uppercase tracking-tight drop-shadow">Watch Reel</span>
            </button>"""

new_thumb_6 = """            <!-- Thumb 6: Professional HD Reel Video Player (Position #6) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#0e1017] border border-white/15 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer relative group flex items-center justify-center shadow-lg active:scale-95" onclick="changeMainProductImage(this, './assets/reel-2.mp4', true)" title="Watch Video Reel">
              <img src="./assets/reel-thumb-2.jpg" alt="Watch Video Reel" class="w-full h-full object-cover rounded-lg opacity-60 group-hover:opacity-85 group-hover:scale-105 transition-all duration-300">
              
              <!-- Professional Dark Gold Frosted Glass Play Badge -->
              <div class="absolute inset-0 flex flex-col items-center justify-center gap-1 z-10 pointer-events-none">
                <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-black/85 backdrop-blur-md border border-[#d4af37]/80 text-[#d4af37] flex items-center justify-center shadow-[0_4px_15px_rgba(212,175,55,0.45)] transform group-hover:scale-110 transition-transform duration-300">
                  <svg class="w-3.5 h-3.5 fill-current text-[#d4af37] translate-x-0.5" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z"/>
                  </svg>
                </div>
                <span class="text-[8px] sm:text-[9px] font-black text-amber-300 uppercase tracking-widest bg-black/80 backdrop-blur-sm px-2 py-0.5 rounded-full border border-[#d4af37]/40 shadow-md">
                  🎬 Reel
                </span>
              </div>
            </button>"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_thumb_6 in content:
            content = content.replace(old_thumb_6, new_thumb_6)
        else:
            # Fallback regex replacement
            content = re.sub(r'<!-- Thumb 6:.*?onclick="changeMainProductImage\(this,\s*\'\./assets/reel-2\.mp4\',\s*true\)".*?</button>', new_thumb_6.strip(), content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED PROFESSIONAL REEL THUMBNAIL IN: {fpath}")
