import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

clean_swipe_gallery_html = """          <!-- Product Gallery Viewport Frame (Clean Touch Swipe + Thumbnail Engine • No Arrows • Zero Cropping) -->
          <div id="ProductGallerySlider" class="relative w-full aspect-square rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl bg-[#0a0c10]">
            
            <!-- Scrollable Snap Track (Swipe Left/Right on Mobile & Drag on PC) -->
            <div id="ProductSlidesTrack" class="flex w-full h-full overflow-x-auto no-scrollbar snap-x snap-mandatory scroll-smooth touch-pan-x select-none" style="scrollbar-width: none; -ms-overflow-style: none;">
              
              <!-- Slide 1: Botanical Stone Pedestal 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-botanical-pedestal-1x1.jpg" alt="Botanical 1:1 Showcase" class="w-full h-full object-contain block select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 2: Flatlay Herbs Table 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-flatlay-herbs-1x1.jpg" alt="Herbal Ingredients Flatlay 1:1" class="w-full h-full object-contain block select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 3: Key Ingredients Infographic 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-key-ingredients-1x1.jpg" alt="Key Ingredients Infographic 1:1" class="w-full h-full object-contain block select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 4: How To Use 5 Steps 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-how-to-use-1x1.jpg" alt="How To Use 1:1" class="w-full h-full object-contain block select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 5: Before vs After Comparison 1:1 -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-[#0a0c10]">
                <img src="./assets/blackroots-before-after-1x1.jpg" alt="Before vs After Comparison 1:1" class="w-full h-full object-contain block select-none pointer-events-none" draggable="false">
              </div>

              <!-- Slide 6: Luxury Video Reel Player (Full Uncropped HD Playback) -->
              <div class="w-full h-full shrink-0 snap-center relative flex items-center justify-center bg-black">
                <video id="ProductSlideVideo" src="./assets/reel-2.mp4" controls loop playsinline webkit-playsinline class="w-full h-full object-contain rounded-2xl block bg-black"></video>
              </div>

            </div>

            <!-- Floating Slide Counter Badge (e.g. 1 / 6) -->
            <div class="absolute bottom-3.5 right-3.5 bg-black/85 backdrop-blur-md text-amber-300 border border-[#d4af37]/60 text-[10px] font-black px-2.5 py-1 rounded-full shadow-xl z-20 pointer-events-none">
              <span id="CurrentSlideNum">1</span> / 6
            </div>

            <!-- Bestseller Badge -->
            <div id="BestsellerBadge" class="absolute top-3.5 left-3.5 bg-black/85 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase tracking-widest px-3 py-1 rounded-full border border-[#d4af37]/50 shadow-xl flex items-center gap-1.5 z-20 pointer-events-none">
              <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
              <span>BESTSELLER</span>
            </div>

          </div>"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'<!-- Product Gallery Viewport Frame.*?<!-- Thumbnails Row'
        content = re.sub(pattern, clean_swipe_gallery_html.strip() + '\n\n          <!-- Thumbnails Row', content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REMOVED ARROWS & APPLIED UNCLUTTERED UNRECROP GALLERY IN: {fpath}")
