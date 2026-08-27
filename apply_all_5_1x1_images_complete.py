import os
import shutil
from PIL import Image

# 1. Optimize and copy all 5 1:1 images to assets/
image_mappings = [
    (r"C:\Users\moham\.gemini\antigravity\brain\9acc6079-8758-4b60-9ce0-86f829074f1f\.user_uploaded\media_1786737103465.jpg", 
     r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-botanical-pedestal-1x1.jpg", "1. Hero Pedestal 1:1"),
    (r"C:\Users\moham\.gemini\antigravity\brain\9acc6079-8758-4b60-9ce0-86f829074f1f\.user_uploaded\media_1786737103460.jpg", 
     r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-flatlay-herbs-1x1.jpg", "2. Flatlay Herbs 1:1"),
    (r"C:\Users\moham\.gemini\antigravity\brain\9acc6079-8758-4b60-9ce0-86f829074f1f\.user_uploaded\media_1786737103383.jpg", 
     r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-key-ingredients-1x1.jpg", "3. Key Ingredients 1:1"),
    (r"C:\Users\moham\.gemini\antigravity\brain\9acc6079-8758-4b60-9ce0-86f829074f1f\.user_uploaded\media_1786737153741.jpg", 
     r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-how-to-use-1x1.jpg", "4. How To Use 1:1"),
    (r"C:\Users\moham\.gemini\antigravity\brain\9acc6079-8758-4b60-9ce0-86f829074f1f\.user_uploaded\media_1786737153845.jpg", 
     r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-before-after-1x1.jpg", "5. Before After 1:1")
]

for src, dest, name in image_mappings:
    with Image.open(src) as im:
        rgb_im = im.convert('RGB')
        rgb_im.save(dest, 'JPEG', quality=88, optimize=True)
    print(f"SAVED {name} -> {dest} ({os.path.getsize(dest)/1024:.1f} KB)")

# 2. Perfect 1:1 Square Gallery HTML
perfect_1x1_gallery_html = """          <!-- Product Gallery Viewport Frame (Ultra-Crisp 100% 1:1 Square Mobile & Desktop Engine) -->
          <div id="ProductMainImageContainer" class="relative w-full aspect-square rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-[#0a0c10] transition-all duration-300">
            <img id="ProductMainImage" src="./assets/blackroots-botanical-pedestal-1x1.jpg" alt="BlackRoots Botanical 1:1 Showcase" class="w-full h-full object-cover block transition-transform duration-300 group-hover:scale-[1.01]">
            <video id="ProductMainVideo" src="./assets/reel-2.mp4" controls loop playsinline webkit-playsinline class="hidden w-full h-full object-cover rounded-2xl block"></video>
            
            <div id="BestsellerBadge" class="absolute top-4 left-4 bg-black/85 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase tracking-widest px-3.5 py-1.5 rounded-full border border-[#d4af37]/50 shadow-xl flex items-center gap-1.5 z-20 pointer-events-none">
              <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>BESTSELLER</span>
            </div>
          </div>

          <!-- Thumbnails Row (100% Symmetrical 1:1 Square Grid) -->
          <div class="grid grid-cols-6 gap-2 sm:gap-3 mt-4">
            <!-- Thumb 1: Botanical Stone Pedestal 1:1 (Position #1) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border-2 border-[#d4af37] p-1 overflow-hidden focus:outline-none shadow-lg transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-botanical-pedestal-1x1.jpg', false)">
              <img src="./assets/blackroots-botanical-pedestal-1x1.jpg" alt="Botanical 1:1 Showcase" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 2: Flatlay Herbs Table 1:1 (Position #2) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-flatlay-herbs-1x1.jpg', false)">
              <img src="./assets/blackroots-flatlay-herbs-1x1.jpg" alt="Herbal Ingredients Flatlay 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 3: Key Ingredients Infographic 1:1 (Position #3) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-key-ingredients-1x1.jpg', false)">
              <img src="./assets/blackroots-key-ingredients-1x1.jpg" alt="Key Ingredients Infographic 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 4: How To Use 5 Steps 1:1 (Position #4) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-how-to-use-1x1.jpg', false)">
              <img src="./assets/blackroots-how-to-use-1x1.jpg" alt="5 Steps How To Use 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 5: Before vs After Comparison 1:1 (Position #5) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-before-after-1x1.jpg', false)">
              <img src="./assets/blackroots-before-after-1x1.jpg" alt="Before vs After Comparison 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 6: Luxury Video Reel Player (Position #6) -->
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
            </button>
          </div>"""

import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'<!-- Product Gallery Viewport Frame.*?<!-- Thumb 6:.*?<\/button>\s*<\/div>'
        content = re.sub(pattern, perfect_1x1_gallery_html.strip(), content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED COMPLETE 1:1 GALLERY IN: {fpath}")
