import os, shutil

src_counter = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786627172720.jpg"
src_flatlay = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786627172854.jpg"
src_shower = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786627172866.jpg"

dest_counter = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-bathroom-counter.jpg"
dest_flatlay = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-flatlay-herbs.jpg"
dest_shower = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-shower-washing.jpg"

shutil.copy2(src_counter, dest_counter)
shutil.copy2(src_flatlay, dest_flatlay)
shutil.copy2(src_shower, dest_shower)

# Mirror to demo_lab & preview
demo_assets = r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets"
prev_assets = r"c:\Users\moham\Downloads\blackroots website\preview\assets"

for da in [demo_assets, prev_assets]:
    if os.path.exists(da):
        shutil.copy2(src_counter, os.path.join(da, "blackroots-bathroom-counter.jpg"))
        shutil.copy2(src_flatlay, os.path.join(da, "blackroots-flatlay-herbs.jpg"))
        shutil.copy2(src_shower, os.path.join(da, "blackroots-shower-washing.jpg"))

print("COPIED ALL 3 LIFESTYLE IMAGES TO ASSETS!")

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_gallery_thumbs = """          <div class="grid grid-cols-6 gap-2 sm:gap-3 mt-4">
            <!-- Thumb 1: Main Single Bottle -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border-2 border-[#d4af37] p-1 overflow-hidden focus:outline-none shadow-lg transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-bottle-single.png')">
              <img src="./assets/blackroots-bottle-single.png" alt="BlackRoots Bottle Render" class="w-full h-full object-contain">
            </button>

            <!-- Thumb 2: Liquid Dispenser Texture -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-liquid-texture.jpg')">
              <img src="./assets/blackroots-liquid-texture.jpg" alt="Rich Black Shampoo Liquid" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 3: Key Ingredients Infographic -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-key-ingredients.jpg')">
              <img src="./assets/blackroots-key-ingredients.jpg" alt="Key Ingredients Infographic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 4: How To Use 5 Steps -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-how-to-use-graphic.png')">
              <img src="./assets/blackroots-how-to-use-graphic.png" alt="5 Steps How To Use" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 5: Herbal Splash Graphic -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-herbal-splash.jpg')">
              <img src="./assets/blackroots-herbal-splash.jpg" alt="Herbal Splash Render" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 6: 8-Sec Video Reel Link -->
            <a href="#BeforeAfterSection" class="aspect-square rounded-xl bg-gradient-to-br from-[#12151c] to-black border border-white/10 hover:border-amber-400 flex flex-col items-center justify-center text-[10px] text-amber-300 font-extrabold p-1 text-center group shadow-md no-underline">
              <span class="text-sm sm:text-base group-hover:scale-110 transition-transform">🎬</span>
              <span class="text-[9px] sm:text-[10px]">8-Sec Video</span>
            </a>
          </div>"""

new_gallery_thumbs = """          <div class="grid grid-cols-5 sm:grid-cols-9 gap-2 mt-4">
            <!-- Thumb 1: Main Single Bottle -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border-2 border-[#d4af37] p-1 overflow-hidden focus:outline-none shadow-lg transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-bottle-single.png')">
              <img src="./assets/blackroots-bottle-single.png" alt="BlackRoots Bottle Render" class="w-full h-full object-contain">
            </button>

            <!-- Thumb 2: Flatlay Herbs Table -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-flatlay-herbs.jpg')">
              <img src="./assets/blackroots-flatlay-herbs.jpg" alt="Herbal Ingredients Flatlay" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 3: Shower Washing Action -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-shower-washing.jpg')">
              <img src="./assets/blackroots-shower-washing.jpg" alt="Shower Hair Washing" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 4: Bathroom Counter Aesthetic -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-bathroom-counter.jpg')">
              <img src="./assets/blackroots-bathroom-counter.jpg" alt="Bathroom Counter Aesthetic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 5: Liquid Dispenser Texture -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-liquid-texture.jpg')">
              <img src="./assets/blackroots-liquid-texture.jpg" alt="Rich Black Shampoo Liquid" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 6: Key Ingredients Infographic -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-key-ingredients.jpg')">
              <img src="./assets/blackroots-key-ingredients.jpg" alt="Key Ingredients Infographic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 7: How To Use 5 Steps -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-how-to-use-graphic.png')">
              <img src="./assets/blackroots-how-to-use-graphic.png" alt="5 Steps How To Use" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 8: Herbal Splash Graphic -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-herbal-splash.jpg')">
              <img src="./assets/blackroots-herbal-splash.jpg" alt="Herbal Splash Render" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 9: 8-Sec Video Reel Link -->
            <a href="#BeforeAfterSection" class="aspect-square rounded-xl bg-gradient-to-br from-[#12151c] to-black border border-white/10 hover:border-amber-400 flex flex-col items-center justify-center text-[10px] text-amber-300 font-extrabold p-1 text-center group shadow-md no-underline">
              <span class="text-xs sm:text-base group-hover:scale-110 transition-transform">🎬</span>
              <span class="text-[8px] sm:text-[9px]">Reel Video</span>
            </a>
          </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_gallery_thumbs in content:
            content = content.replace(old_gallery_thumbs, new_gallery_thumbs)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"EXPANDED LUXURY GALLERY GRID TO 9 CARDS IN: {fpath}")

