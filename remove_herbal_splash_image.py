import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

new_gallery_container = """          <div class="relative w-full aspect-square sm:aspect-[4/3] rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center group bg-[#0d0e12]">
            <img id="ProductMainImage" src="./assets/blackroots-bathroom-counter.jpg" alt="BlackRoots Product Showcase" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-105">
            <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase tracking-widest px-3.5 py-1.5 rounded-full border border-[#d4af37]/50 shadow-xl flex items-center gap-1.5 z-20 pointer-events-none">
              <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>BESTSELLER</span>
            </div>
          </div>

          <div class="grid grid-cols-4 sm:grid-cols-7 gap-2 mt-4">
            <!-- Thumb 1: Bathroom Counter (Position #1) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border-2 border-[#d4af37] p-1 overflow-hidden focus:outline-none shadow-lg transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-bathroom-counter.jpg')">
              <img src="./assets/blackroots-bathroom-counter.jpg" alt="Bathroom Counter Aesthetic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 2: Flatlay Herbs Table (Position #2) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-flatlay-herbs.jpg')">
              <img src="./assets/blackroots-flatlay-herbs.jpg" alt="Herbal Ingredients Flatlay" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 3: Key Ingredients Infographic (Position #3) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-key-ingredients.jpg')">
              <img src="./assets/blackroots-key-ingredients.jpg" alt="Key Ingredients Infographic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 4: How To Use 5 Steps (Position #4) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-how-to-use-graphic.png')">
              <img src="./assets/blackroots-how-to-use-graphic.png" alt="5 Steps How To Use" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 5: Liquid Dispenser Texture (Position #5) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-liquid-texture.jpg')">
              <img src="./assets/blackroots-liquid-texture.jpg" alt="Rich Black Shampoo Liquid" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 6: Shower Hair Washing (Position #6) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-shower-washing.jpg')">
              <img src="./assets/blackroots-shower-washing.jpg" alt="Shower Hair Washing" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 7: 8-Sec Video Reel Link (Position #7) -->
            <a href="#BeforeAfterSection" class="aspect-square rounded-xl bg-gradient-to-br from-[#12151c] to-black border border-white/10 hover:border-amber-400 flex flex-col items-center justify-center text-[10px] text-amber-300 font-extrabold p-1 text-center group shadow-md no-underline">
              <span class="text-xs sm:text-base group-hover:scale-110 transition-transform">🎬</span>
              <span class="text-[8px] sm:text-[9px]">Reel Video</span>
            </a>
          </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        start_marker = '<div class="relative w-full aspect-square sm:aspect-[4/3]'
        end_marker = '</div>\n        </div>\n\n        <div class="lg:col-span-5'

        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)

        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + new_gallery_container + content[end_idx + 14:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REMOVED HERBAL SPLASH IMAGE IN: {fpath}")

