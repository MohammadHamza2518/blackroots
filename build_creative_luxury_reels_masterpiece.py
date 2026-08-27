import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

luxury_reels_masterpiece_html = """  <!-- Watch Reels & 360° Showcase Section (Creative Ultra-Luxury D2C Design - Butter Smooth 60fps) -->
  <section class="py-12 sm:py-20 bg-gradient-to-b from-[#050608] via-[#0b0c10] to-[#050608] border-b border-[#d4af37]/25 relative overflow-hidden">
    
    <!-- Ambient Gold Radial Glow Backgrounds -->
    <div class="absolute top-1/2 left-1/4 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#d4af37]/8 rounded-full filter blur-[120px] pointer-events-none"></div>
    <div class="absolute top-1/2 right-1/4 translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#d4af37]/5 rounded-full filter blur-[120px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Section Tagline Pill -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/10 border border-[#d4af37]/40 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-widest mb-3 backdrop-blur-xl shadow-[0_10px_25px_rgba(212,175,55,0.15)]">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span>🎬 360° STUDIO SHOWCASE &bull; OFFICIAL REELS</span>
      </div>

      <h2 class="font-serif text-3xl sm:text-5xl font-extrabold text-white mb-3 tracking-wide leading-tight">
        Watch Hair Transformation <span class="gold-gradient-text">Reels</span>
      </h2>

      <p class="text-gray-300 text-xs sm:text-base max-w-xl mx-auto mb-8 font-light leading-relaxed">
        👈 <strong>Swipe Left & Right</strong> &bull; Tap video to watch with full audio on Instagram 👉
      </p>

      <!-- Carousel Container Wrapper with Left & Right Floating Arrows -->
      <div class="relative max-w-6xl mx-auto">
        
        <!-- Left Floating Arrow Button -->
        <button id="ReelsSlideLeft" type="button" class="hidden sm:flex absolute left-0 top-1/2 -translate-y-1/2 -translate-x-5 z-40 w-12 h-12 rounded-full bg-black/90 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-xl shadow-[0_15px_35px_rgba(0,0,0,0.8)] transition-all transform hover:scale-110 cursor-pointer focus:outline-none">
          &larr;
        </button>

        <!-- Right Floating Arrow Button -->
        <button id="ReelsSlideRight" type="button" class="hidden sm:flex absolute right-0 top-1/2 -translate-y-1/2 translate-x-5 z-40 w-12 h-12 rounded-full bg-black/90 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-xl shadow-[0_15px_35px_rgba(0,0,0,0.8)] transition-all transform hover:scale-110 cursor-pointer focus:outline-none">
          &rarr;
        </button>

        <!-- Butter-Smooth Horizontal Swipe Reel Cards Carousel -->
        <div id="ReelsCarouselContainer" class="flex items-center gap-5 sm:gap-7 overflow-x-auto no-scrollbar snap-x snap-mandatory py-6 px-2 sm:px-6 scroll-smooth w-full select-none">
          
          <!-- Card 1: reel-3.mp4 -> Proven Results -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/DcA80uuvGfh/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <!-- Header Badges -->
            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                ⚡ Proven Results
              </span>
              
              <!-- Sleek Compact Circular Sound Icon Badge -->
              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>
            
            <!-- Video Tag -->
            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-3.mp4" type="video/mp4">
            </video>

            <!-- Translucent AI Rendered Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                ✨ REAL CUSTOMER REEL
              </span>
            </div>
            
            <!-- Shoppable Bottom Bar -->
            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Results Are 100% Real</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 61.2K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Card 2: reel-2.mp4 -> Anti-Dandruff -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db-aZhvpD_D/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                ✨ Anti-Dandruff
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-2.mp4" type="video/mp4">
            </video>

            <!-- Translucent Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                ✨ SCALP DEFENSE
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Say No To Flaky Dandruff</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 38.9K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Card 3: reel-4.mp4 -> Scalp Solution -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db8ghNFJwau/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                🛡️ Scalp Solution
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-4.mp4" type="video/mp4">
            </video>

            <!-- Translucent Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                🛡️ 3-IN-1 RECOVERY
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Fix Grey Hair, Dandruff, Fall</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 29.8K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Card 4: reel-5.mp4 -> Real Testimonial -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db_cLl-vUPL/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                ❤️ Real Testimonial
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-5.mp4" type="video/mp4">
            </video>

            <!-- Translucent Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                ❤️ VERIFIED REVIEW
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Stop Premature Greying</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 84.1K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>

          <!-- Card 5 (LAST): reel-1.mp4 -> 360° Studio Showcase / Application Ritual -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-[0_25px_60px_rgba(212,175,55,0.25)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db-axwZpQGN/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] sm:text-[10px] font-black uppercase px-3 py-1 rounded-full shadow-lg">
                ✨ 360° STUDIO SHOWCASE
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-1.mp4" type="video/mp4">
            </video>

            <!-- Ultra-Clean Studio Watermark Pill -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[8px] font-extrabold tracking-widest uppercase px-3 py-1 rounded-full border border-amber-500/30 shadow-xl">
                ⚡ 360° AI Studio Rendered
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Roots Reborn Black</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 52.4K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
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
                content = content[:s_idx] + luxury_reels_masterpiece_html + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"APPLIED CREATIVE LUXURY REELS SECTION IN: {fpath}")
