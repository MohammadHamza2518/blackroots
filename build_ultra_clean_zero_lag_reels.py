import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

ultra_clean_reels_js = """/* ⚡ Ultra-Clean Zero-Lag 60fps Reel Carousel (Native Pure Video Engine) */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const cards = container.querySelectorAll('.js-reel-card');
  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  if (!cards.length) return;

  // Sound toggle handling
  cards.forEach(card => {
    const video = card.querySelector('video');
    const soundBtn = card.querySelector('.js-sound-toggle');
    const soundIcon = card.querySelector('.js-sound-icon');

    if (video && soundBtn && soundIcon) {
      soundBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (video.muted) {
          // Mute all other videos
          cards.forEach(c => {
            const v = c.querySelector('video');
            const btn = c.querySelector('.js-sound-toggle');
            const ico = c.querySelector('.js-sound-icon');
            if (v) v.muted = true;
            if (btn && ico) {
              ico.textContent = '🔇';
              btn.classList.remove('bg-[#d4af37]', 'text-black');
              btn.classList.add('bg-black/75', 'text-amber-300');
            }
          });
          video.muted = false;
          soundIcon.textContent = '🔊';
          soundBtn.classList.remove('bg-black/75', 'text-amber-300');
          soundBtn.classList.add('bg-[#d4af37]', 'text-black');
          video.play().catch(() => {});
        } else {
          video.muted = true;
          soundIcon.textContent = '🔇';
          soundBtn.classList.remove('bg-[#d4af37]', 'text-black');
          soundBtn.classList.add('bg-black/75', 'text-amber-300');
        }
      });
    }
  });

  // Simple, instant arrow navigation
  if (leftArrow) {
    leftArrow.addEventListener('click', () => {
      container.scrollBy({ left: -310, behavior: 'smooth' });
    });
  }

  if (rightArrow) {
    rightArrow.addEventListener('click', () => {
      container.scrollBy({ left: 310, behavior: 'smooth' });
    });
  }
}"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        r_idx = content.find('function initReelsModal()')
        if r_idx != -1:
            e_idx = content.find('function ', r_idx + 30)
            if e_idx == -1:
                e_idx = content.find('/* ', r_idx + 30)
            if e_idx != -1:
                content = content[:r_idx] + ultra_clean_reels_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"APPLIED ULTRA-CLEAN ZERO-LAG REELS JS IN: {jspath}")

# Update HTML files to render 100% clean video cards with zero heavy glow shadows
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

ultra_clean_reels_section_html = """  <!-- Watch Reels Section (Ultra-Clean 60fps Native Video Carousel) -->
  <section class="py-10 sm:py-16 bg-[#07080b] border-b border-[#d4af37]/20 relative overflow-hidden">
    <!-- Subtle Background Glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-96 bg-[#d4af37]/5 rounded-full filter blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Section Tagline Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/15 border border-[#d4af37]/40 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-widest mb-3 backdrop-blur-md shadow-lg">
        <span>🎬 REELS STUDIO &bull; SWIPE TO WATCH</span>
      </div>

      <h2 class="font-serif text-2xl sm:text-5xl font-bold text-white mb-2 tracking-wide">
        Watch Hair Transformation <span class="gold-gradient-text">Reels</span>
      </h2>

      <p class="text-gray-300 text-xs sm:text-base max-w-xl mx-auto mb-6 font-light leading-relaxed">
        👈 <strong>Swipe Left & Right</strong> to watch real 9:16 customer transformations & doctor reviews 👉
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

        <!-- Ultra-Clean Native Swipeable Reel Cards Carousel -->
        <div id="ReelsCarouselContainer" class="flex items-center gap-4 sm:gap-6 overflow-x-auto no-scrollbar snap-x snap-mandatory py-4 px-2 sm:px-6 scroll-smooth w-full">
          
          <!-- Card 1 (Fix Grey Hair, Dandruff, Fall) -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-2xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                🛡️ Scalp Solution
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/70 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
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

          <!-- Card 2 (Say No To Flaky Dandruff) -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ✨ Anti-Dandruff
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/70 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
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

          <!-- Card 3 (Results Are 100% Real) -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ⚡ Proven Results
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/70 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
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

          <!-- Card 4 (Stop Premature Greying) -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ❤️ Real Testimonial
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/70 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
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

          <!-- Card 5 (Your Roots, Reborn Black) -->
          <div class="js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-xl relative bg-black group transition-all duration-300">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ✨ Application Ritual
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/70 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
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
                content = content[:s_idx] + ultra_clean_reels_section_html + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"APPLIED ULTRA-CLEAN REELS SECTION IN: {fpath}")
