import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

reels_html_last_pos = """  <!-- Watch Reels Section (Native Smooth Horizontal Swipe & User Ordered Instagram Links) -->
  <section class="py-10 sm:py-16 bg-[#07080b] border-b border-[#d4af37]/20 relative overflow-hidden">
    <!-- Ambient Gold Glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-96 bg-[#d4af37]/5 rounded-full filter blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Section Tagline Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/15 border border-[#d4af37]/40 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-widest mb-3 backdrop-blur-md shadow-lg">
        <span>🎬 REELS STUDIO &bull; OFFICIAL INSTAGRAM @BLACKROOTS.IN</span>
      </div>

      <h2 class="font-serif text-2xl sm:text-5xl font-bold text-white mb-2 tracking-wide">
        Watch Hair Transformation <span class="gold-gradient-text">Reels</span>
      </h2>

      <p class="text-gray-300 text-xs sm:text-base max-w-xl mx-auto mb-6 font-light leading-relaxed">
        👈 <strong>Swipe Left & Right</strong> to watch preview &bull; Click button to watch with full audio on Instagram 👉
      </p>

      <!-- Carousel Container Wrapper with Left & Right Arrows -->
      <div class="relative max-w-6xl mx-auto">
        
        <!-- Left Arrow Button -->
        <button id="ReelsSlideLeft" type="button" class="hidden sm:flex absolute left-0 top-1/2 -translate-y-1/2 -translate-x-4 z-40 w-11 h-11 rounded-full bg-black/80 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-lg shadow-2xl transition-all cursor-pointer focus:outline-none">
          &larr;
        </button>

        <!-- Right Arrow Button -->
        <button id="ReelsSlideRight" type="button" class="hidden sm:flex absolute right-0 top-1/2 -translate-y-1/2 translate-x-4 z-40 w-11 h-11 rounded-full bg-black/80 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-lg shadow-2xl transition-all cursor-pointer focus:outline-none">
          &rarr;
        </button>

        <!-- Native Smooth Horizontal Swipe Reel Cards Carousel -->
        <div id="ReelsCarouselContainer" class="flex items-center gap-4 sm:gap-6 overflow-x-auto no-scrollbar snap-x snap-mandatory py-4 px-2 sm:px-6 scroll-smooth w-full">
          
          <!-- Position 1: reel-3.mp4 -> Link: DcA80uuvGfh -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-2xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-auto gap-2">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow shrink-0">
                ⚡ Proven Results
              </span>
              
              <!-- IG Link -->
              <a href="https://www.instagram.com/reel/DcA80uuvGfh/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 text-white font-extrabold text-[9px] sm:text-[10px] tracking-wide shadow-xl hover:scale-105 transition-transform border border-white/30 text-decoration-none shrink-0" title="Watch on Instagram with Sound">
                <span>📸 Sound on IG 🔊</span>
              </a>
            </div>
            
            <video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">
              <source src="./assets/reel-3.mp4" type="video/mp4">
            </video>
            
            <div class="absolute bottom-3 left-3 right-3 z-30 p-2.5 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2 min-w-0">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Results Are 100% Real</h4>
                  <div class="flex items-center gap-1">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 61.2K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Position 2: reel-2.mp4 -> Link: Db-aZhvpD_D -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-auto gap-2">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow shrink-0">
                ✨ Anti-Dandruff
              </span>

              <!-- IG Link -->
              <a href="https://www.instagram.com/reel/Db-aZhvpD_D/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 text-white font-extrabold text-[9px] sm:text-[10px] tracking-wide shadow-xl hover:scale-105 transition-transform border border-white/30 text-decoration-none shrink-0" title="Watch on Instagram with Sound">
                <span>📸 Sound on IG 🔊</span>
              </a>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">
              <source src="./assets/reel-2.mp4" type="video/mp4">
            </video>

            <div class="absolute bottom-3 left-3 right-3 z-30 p-2.5 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2 min-w-0">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Say No To Flaky Dandruff</h4>
                  <div class="flex items-center gap-1">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 38.9K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Position 3: reel-4.mp4 -> Link: Db8ghNFJwau -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-auto gap-2">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow shrink-0">
                🛡️ Scalp Solution
              </span>

              <!-- IG Link -->
              <a href="https://www.instagram.com/reel/Db8ghNFJwau/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 text-white font-extrabold text-[9px] sm:text-[10px] tracking-wide shadow-xl hover:scale-105 transition-transform border border-white/30 text-decoration-none shrink-0" title="Watch on Instagram with Sound">
                <span>📸 Sound on IG 🔊</span>
              </a>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">
              <source src="./assets/reel-4.mp4" type="video/mp4">
            </video>

            <div class="absolute bottom-3 left-3 right-3 z-30 p-2.5 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2 min-w-0">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Fix Grey Hair, Dandruff, Fall</h4>
                  <div class="flex items-center gap-1">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 29.8K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Position 4: reel-5.mp4 -> Link: Db_cLl-vUPL -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-auto gap-2">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow shrink-0">
                ❤️ Real Testimonial
              </span>

              <!-- IG Link -->
              <a href="https://www.instagram.com/reel/Db_cLl-vUPL/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 text-white font-extrabold text-[9px] sm:text-[10px] tracking-wide shadow-xl hover:scale-105 transition-transform border border-white/30 text-decoration-none shrink-0" title="Watch on Instagram with Sound">
                <span>📸 Sound on IG 🔊</span>
              </a>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">
              <source src="./assets/reel-5.mp4" type="video/mp4">
            </video>

            <div class="absolute bottom-3 left-3 right-3 z-30 p-2.5 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2 min-w-0">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Stop Premature Greying</h4>
                  <div class="flex items-center gap-1">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 84.1K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Position 5 (LAST): reel-1.mp4 -> Link: Db-axwZpQGN (Roots Reborn Black / Application Ritual) -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-auto gap-2">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow shrink-0">
                ✨ Application Ritual
              </span>

              <!-- IG Link -->
              <a href="https://www.instagram.com/reel/Db-axwZpQGN/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 text-white font-extrabold text-[9px] sm:text-[10px] tracking-wide shadow-xl hover:scale-105 transition-transform border border-white/30 text-decoration-none shrink-0" title="Watch on Instagram with Sound">
                <span>📸 Sound on IG 🔊</span>
              </a>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">
              <source src="./assets/reel-1.mp4" type="video/mp4">
            </video>

            <div class="absolute bottom-3 left-3 right-3 z-30 p-2.5 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2 min-w-0">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Roots Reborn Black</h4>
                  <div class="flex items-center gap-1">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 52.4K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform">
                Buy Now &rarr;
              </a>
            </div>
          </div>

        </div>

      </div>

    </div>
  </section>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('<!-- Watch')
        if s_idx == -1:
            s_idx = content.find('REELS STUDIO')
            if s_idx != -1:
                s_idx = content.rfind('<section', 0, s_idx)

        if s_idx != -1:
            e_idx = content.find('</section>', s_idx)
            if e_idx != -1:
                content = content[:s_idx] + reels_html_last_pos + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"MOVED APPLICATION RITUAL TO LAST POSITION IN: {fpath}")
