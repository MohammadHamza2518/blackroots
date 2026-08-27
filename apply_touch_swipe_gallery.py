import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

swipe_gallery_html = """          <!-- Product Gallery Viewport Frame (Touch Swipe + Arrow + Thumbnail Engine) -->
          <div id="ProductGallerySlider" class="relative w-full aspect-square rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl bg-[#0a0c10] group">
            
            <!-- Scrollable Snap Track (Swipe Left/Right on Mobile & Drag on PC) -->
            <div id="ProductSlidesTrack" class="flex w-full h-full overflow-x-auto no-scrollbar snap-x snap-mandatory scroll-smooth touch-pan-x select-none" style="scrollbar-width: none; -ms-overflow-style: none;">
              
              <!-- Slide 1: Botanical Stone Pedestal 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-botanical-pedestal-1x1.jpg" alt="Botanical 1:1 Showcase" class="w-full h-full object-cover select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 2: Flatlay Herbs Table 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-flatlay-herbs-1x1.jpg" alt="Herbal Ingredients Flatlay 1:1" class="w-full h-full object-cover select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 3: Key Ingredients Infographic 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-key-ingredients-1x1.jpg" alt="Key Ingredients Infographic 1:1" class="w-full h-full object-cover select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 4: How To Use 5 Steps 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-how-to-use-1x1.jpg" alt="How To Use 1:1" class="w-full h-full object-cover select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 5: Before vs After Comparison 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-before-after-1x1.jpg" alt="Before vs After Comparison 1:1" class="w-full h-full object-cover select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 6: Luxury Video Reel Player -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-black">
                <video id="ProductSlideVideo" src="./assets/reel-2.mp4" controls loop playsinline webkit-playsinline class="w-full h-full object-cover rounded-2xl"></video>
              </div>

            </div>

            <!-- Left / Right Floating Luxury Navigation Arrows -->
            <button type="button" onclick="window.slideProductGallery(-1)" class="absolute left-2.5 top-1/2 -translate-y-1/2 w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-black/80 backdrop-blur-md border border-[#d4af37]/70 text-amber-300 flex items-center justify-center text-xs font-black shadow-xl active:scale-90 hover:scale-110 hover:bg-[#d4af37] hover:text-black transition-all z-20 cursor-pointer" aria-label="Previous Slide">
              &larr;
            </button>
            <button type="button" onclick="window.slideProductGallery(1)" class="absolute right-2.5 top-1/2 -translate-y-1/2 w-8 h-8 sm:w-9 sm:h-9 rounded-full bg-black/80 backdrop-blur-md border border-[#d4af37]/70 text-amber-300 flex items-center justify-center text-xs font-black shadow-xl active:scale-90 hover:scale-110 hover:bg-[#d4af37] hover:text-black transition-all z-20 cursor-pointer" aria-label="Next Slide">
              &rarr;
            </button>

            <!-- Floating Slide Counter Badge (e.g. 1 / 6) -->
            <div class="absolute bottom-3 right-3 bg-black/85 backdrop-blur-md text-amber-300 border border-[#d4af37]/60 text-[10px] font-black px-2.5 py-1 rounded-full shadow-xl z-20 pointer-events-none">
              <span id="CurrentSlideNum">1</span> / 6
            </div>

            <!-- Bestseller Badge -->
            <div id="BestsellerBadge" class="absolute top-3.5 left-3.5 bg-black/85 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase tracking-widest px-3 py-1 rounded-full border border-[#d4af37]/50 shadow-xl flex items-center gap-1.5 z-20 pointer-events-none">
              <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              <span>BESTSELLER</span>
            </div>

          </div>

          <!-- Thumbnails Row (100% Symmetrical 1:1 Square Grid) -->
          <div class="grid grid-cols-6 gap-2 sm:gap-3 mt-4">
            <!-- Thumb 1: Botanical Stone Pedestal 1:1 (Position #1) -->
            <button type="button" id="ProductThumb_0" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border-2 border-[#d4af37] p-1 overflow-hidden focus:outline-none shadow-lg transition-all cursor-pointer active:scale-95" onclick="window.goToProductSlide(0)">
              <img src="./assets/blackroots-botanical-pedestal-1x1.jpg" alt="Botanical 1:1 Showcase" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 2: Flatlay Herbs Table 1:1 (Position #2) -->
            <button type="button" id="ProductThumb_1" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer active:scale-95" onclick="window.goToProductSlide(1)">
              <img src="./assets/blackroots-flatlay-herbs-1x1.jpg" alt="Herbal Ingredients Flatlay 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 3: Key Ingredients Infographic 1:1 (Position #3) -->
            <button type="button" id="ProductThumb_2" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer active:scale-95" onclick="window.goToProductSlide(2)">
              <img src="./assets/blackroots-key-ingredients-1x1.jpg" alt="Key Ingredients Infographic 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 4: How To Use 5 Steps 1:1 (Position #4) -->
            <button type="button" id="ProductThumb_3" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer active:scale-95" onclick="window.goToProductSlide(3)">
              <img src="./assets/blackroots-how-to-use-1x1.jpg" alt="5 Steps How To Use 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 5: Before vs After Comparison 1:1 (Position #5) -->
            <button type="button" id="ProductThumb_4" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer active:scale-95" onclick="window.goToProductSlide(4)">
              <img src="./assets/blackroots-before-after-1x1.jpg" alt="Before vs After Comparison 1:1" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 6: Luxury Video Reel Player (Position #6) -->
            <button type="button" id="ProductThumb_5" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer relative group flex items-center justify-center shadow-lg active:scale-95" onclick="window.goToProductSlide(5)" title="Watch Product Video">
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

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'<!-- Product Gallery Viewport Frame.*?<!-- Thumb 6:.*?<\/button>\s*<\/div>'
        content = re.sub(pattern, swipe_gallery_html.strip(), content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED TOUCH-SWIPE GALLERY IN: {fpath}")
