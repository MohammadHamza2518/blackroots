import os, shutil

src_liquid = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786627035623.jpg"
src_ingredients = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786627035762.jpg"
src_how_to_use = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786627035705.png"
src_splash = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786627035706.jpg"

dest_liquid = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-liquid-texture.jpg"
dest_ingredients = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-key-ingredients.jpg"
dest_how_to_use = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-how-to-use-graphic.png"
dest_splash = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-herbal-splash.jpg"

shutil.copy2(src_liquid, dest_liquid)
shutil.copy2(src_ingredients, dest_ingredients)
shutil.copy2(src_how_to_use, dest_how_to_use)
shutil.copy2(src_splash, dest_splash)

# Mirror to demo_lab & preview
demo_assets = r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets"
prev_assets = r"c:\Users\moham\Downloads\blackroots website\preview\assets"

for da in [demo_assets, prev_assets]:
    if os.path.exists(da):
        shutil.copy2(src_liquid, os.path.join(da, "blackroots-liquid-texture.jpg"))
        shutil.copy2(src_ingredients, os.path.join(da, "blackroots-key-ingredients.jpg"))
        shutil.copy2(src_how_to_use, os.path.join(da, "blackroots-how-to-use-graphic.png"))
        shutil.copy2(src_splash, os.path.join(da, "blackroots-herbal-splash.jpg"))

print("COPIED ALL 4 NEW GALLERY IMAGES TO ASSETS!")

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_gallery_thumbs = """          <div class="grid grid-cols-4 gap-4">
            <button type="button" class="aspect-square rounded-2xl bg-[#12151c] border-2 border-[#d4af37] p-1.5 overflow-hidden focus:outline-none shadow-lg" onclick="document.getElementById('ProductMainImage').src='./assets/blackroots-bottle-single.png'">
              <img src="./assets/blackroots-bottle-single.png" alt="Bottles Render" class="w-full h-full object-contain">
            </button>
            <button type="button" class="aspect-square rounded-2xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1.5 overflow-hidden focus:outline-none" onclick="document.getElementById('ProductMainImage').src='./assets/blackroots-back-label-full.png'">
              <img src="./assets/blackroots-back-label-full.png" alt="Back Label Artwork" class="w-full h-full object-contain">
            </button>
            <button type="button" class="aspect-square rounded-2xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1.5 overflow-hidden focus:outline-none" onclick="document.getElementById('ProductMainImage').src='./assets/blackroots-logo-circle-black.jpg'">
              <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo Emblem" class="w-full h-full object-contain rounded-lg">
            </button>
            <div class="aspect-square rounded-2xl bg-[#12151c] border border-white/10 flex flex-col items-center justify-center text-xs text-amber-300 font-bold p-1 text-center">
              <span>🎬 8-Sec Video</span>
            </div>
          </div>"""

new_gallery_thumbs = """          <div class="grid grid-cols-6 gap-2 sm:gap-3 mt-4">
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

helper_script = """  <script>
    function changeMainProductImage(btn, src) {
      const mainImg = document.getElementById('ProductMainImage');
      if (mainImg) mainImg.src = src;
      document.querySelectorAll('.js-thumb-btn').forEach(b => {
        b.classList.remove('border-2', 'border-[#d4af37]');
        b.classList.add('border-white/10');
      });
      if (btn) {
        btn.classList.remove('border-white/10');
        btn.classList.add('border-2', 'border-[#d4af37]');
      }
    }
  </script>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_gallery_thumbs in content:
            content = content.replace(old_gallery_thumbs, new_gallery_thumbs)

        if "function changeMainProductImage" not in content and "</body>" in content:
            content = content.replace("</body>", f"{helper_script}\n</body>")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"ENHANCED PRODUCT MEDIA GALLERY IN: {fpath}")

