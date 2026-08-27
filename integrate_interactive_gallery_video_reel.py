import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

new_gallery_container = """          <!-- Product Gallery Viewport Frame (Interactive Photo & Video Reel Engine) -->
          <div id="ProductMainImageContainer" class="relative w-full rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-[#0a0c10] transition-all duration-300">
            <img id="ProductMainImage" src="./assets/blackroots-bathroom-counter.jpg" alt="BlackRoots Product Showcase" class="w-full h-auto max-h-[550px] object-contain block transition-transform duration-300 group-hover:scale-[1.01]">
            <video id="ProductMainVideo" src="./assets/reel-1.mp4" controls loop playsinline class="hidden w-full h-auto max-h-[550px] object-contain rounded-2xl block"></video>
            
            <div id="BestsellerBadge" class="absolute top-4 left-4 bg-black/85 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase tracking-widest px-3.5 py-1.5 rounded-full border border-[#d4af37]/50 shadow-xl flex items-center gap-1.5 z-20 pointer-events-none">
              <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>BESTSELLER</span>
            </div>
          </div>

          <!-- Thumbnails Row (Mobile & Desktop Friendly Grid) -->
          <div class="grid grid-cols-6 gap-2 sm:gap-3 mt-4">
            <!-- Thumb 1: Bathroom Counter (Position #1) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border-2 border-[#d4af37] p-1 overflow-hidden focus:outline-none shadow-lg transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-bathroom-counter.jpg', false)">
              <img src="./assets/blackroots-bathroom-counter.jpg" alt="Bathroom Counter Aesthetic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 2: Flatlay Herbs Table 16:9 (Position #2) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-flatlay-herbs.jpg', false)">
              <img src="./assets/blackroots-flatlay-herbs.jpg" alt="Herbal Ingredients Flatlay 16:9" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 3: Key Ingredients Infographic (Position #3) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-key-ingredients.jpg', false)">
              <img src="./assets/blackroots-key-ingredients.jpg" alt="Key Ingredients Infographic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 4: How To Use 5 Steps (Position #4) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-how-to-use-graphic.png', false)">
              <img src="./assets/blackroots-how-to-use-graphic.png" alt="5 Steps How To Use" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 5: Shampoo Use Karne Se Pehle vs Baad Comparison (Position #5) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-[#12151c] border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer" onclick="changeMainProductImage(this, './assets/blackroots-before-after-infographic.jpg', false)">
              <img src="./assets/blackroots-before-after-infographic.jpg" alt="Before vs After Comparison Graphic" class="w-full h-full object-cover rounded-lg">
            </button>

            <!-- Thumb 6: Interactive Reel Video Player (Position #6) -->
            <button type="button" class="js-thumb-btn aspect-square rounded-xl bg-gradient-to-br from-[#12151c] to-black border border-white/10 hover:border-[#d4af37] p-1 overflow-hidden focus:outline-none transition-all cursor-pointer relative group flex flex-col items-center justify-center shadow-lg" onclick="changeMainProductImage(this, './assets/reel-1.mp4', true)">
              <div class="absolute inset-0 bg-cover bg-center opacity-40 group-hover:opacity-60 transition-opacity" style="background-image: url('./assets/blackroots-bottle-single.png');"></div>
              <div class="relative z-10 w-7 h-7 rounded-full bg-[#d4af37] text-black flex items-center justify-center shadow-md transform group-hover:scale-110 transition-transform">
                <svg class="w-3.5 h-3.5 fill-current translate-x-0.5" viewBox="0 0 24 24">
                  <path d="M8 5v14l11-7z"/>
                </svg>
              </div>
              <span class="relative z-10 text-[8px] sm:text-[9px] text-amber-300 font-extrabold mt-1 uppercase tracking-tight drop-shadow">Watch Reel</span>
            </button>
          </div>"""

perfect_video_gallery_script = """  <script>
    function changeMainProductImage(btn, src, isVideo = false) {
      const mainImg = document.getElementById('ProductMainImage');
      const mainVid = document.getElementById('ProductMainVideo');
      const imgContainer = document.getElementById('ProductMainImageContainer');
      const bestsellerBadge = document.getElementById('BestsellerBadge');
      
      if (imgContainer) {
        if (isVideo) {
          if (mainImg) mainImg.classList.add('hidden');
          if (mainVid) {
            mainVid.classList.remove('hidden');
            if (src) mainVid.src = src;
            mainVid.play().catch(() => {});
          }
          imgContainer.className = 'relative w-full rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-black transition-all duration-300';
          if (bestsellerBadge) bestsellerBadge.style.display = 'none';
        } else {
          if (mainVid) {
            mainVid.pause();
            mainVid.classList.add('hidden');
          }
          if (mainImg) {
            mainImg.classList.remove('hidden');
            mainImg.src = src;
          }
          
          if (src.includes('how-to-use')) {
            imgContainer.className = 'relative w-full rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-white p-2 sm:p-3 transition-all duration-300';
            if (mainImg) mainImg.className = 'w-full h-auto max-h-[550px] object-contain block transition-transform duration-300 group-hover:scale-[1.01]';
            if (bestsellerBadge) bestsellerBadge.style.display = 'none';
          } else if (src.includes('before-after-infographic') || src.includes('key-ingredients')) {
            imgContainer.className = 'relative w-full rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-[#0a0c10] transition-all duration-300';
            if (mainImg) mainImg.className = 'w-full h-auto max-h-[550px] object-contain block transition-transform duration-300 group-hover:scale-[1.01]';
            if (bestsellerBadge) bestsellerBadge.style.display = 'none';
          } else {
            imgContainer.className = 'relative w-full rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-[#0a0c10] transition-all duration-300';
            if (mainImg) mainImg.className = 'w-full h-auto max-h-[550px] object-contain block transition-transform duration-300 group-hover:scale-[1.01]';
            if (bestsellerBadge) bestsellerBadge.style.display = 'flex';
          }
        }
      }
      
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

        start_idx = content.find('<!-- Product Gallery Viewport Frame')
        if start_idx == -1:
            start_idx = content.find('<div id="ProductMainImageContainer"')
        if start_idx == -1:
            start_idx = content.find('<div class="relative w-full')
        end_idx = content.find('<div class="lg:col-span-5')

        if start_idx != -1 and end_idx != -1:
            container_end = content.rfind('</div>', 0, end_idx)
            container_end = content.rfind('</div>', 0, container_end)
            content = content[:start_idx] + new_gallery_container + content[container_end+6:]

        if "function changeMainProductImage" in content:
            script_idx = content.find("function changeMainProductImage")
            bg_script = content.rfind("<script>", 0, script_idx)
            if bg_script != -1:
                content = content[:bg_script] + perfect_video_gallery_script + "\n</body>\n</html>"

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"INTEGRATED INTERACTIVE REEL VIDEO PLAYER ENGINE IN: {fpath}")

