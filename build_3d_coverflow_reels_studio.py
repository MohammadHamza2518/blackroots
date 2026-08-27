import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

coverflow_reels_js = """/* 🚀 Ultra-Smooth 3D Cover Flow Reel Carousel (Makhan Smooth 60fps) */
function initReelsModal() {
  const cards = document.querySelectorAll('.js-3d-card');
  const stage = document.getElementById('CoverflowStage');
  const prevBtn = document.getElementById('CoverflowPrev');
  const nextBtn = document.getElementById('CoverflowNext');

  if (!cards.length || !stage) return;

  let currentIndex = 0;
  const total = cards.length;

  function updateCoverflow() {
    cards.forEach((card, i) => {
      const video = card.querySelector('video');
      const offset = (i - currentIndex + total) % total;

      // Remove existing transform classes
      card.style.transition = 'all 0.5s cubic-bezier(0.25, 1, 0.5, 1)';

      if (offset === 0) {
        // CENTER ACTIVE CARD (Large, Full Opacity, Glowing Gold Border)
        card.style.transform = 'translateX(0%) scale(1) rotateY(0deg)';
        card.style.zIndex = '30';
        card.style.opacity = '1';
        card.style.filter = 'none';
        card.classList.add('border-[#d4af37]', 'shadow-[0_25px_70px_rgba(212,175,55,0.45)]');
        card.classList.remove('border-white/10', 'shadow-lg');

        if (video) {
          const playPromise = video.play();
          if (playPromise !== undefined) playPromise.catch(() => {});
        }
      } else if (offset === 1 || offset === -(total - 1)) {
        // IMMEDIATE RIGHT CARD
        card.style.transform = 'translateX(70%) scale(0.82) rotateY(-12deg)';
        card.style.zIndex = '20';
        card.style.opacity = '0.65';
        card.style.filter = 'brightness(0.8)';
        card.classList.remove('border-[#d4af37]', 'shadow-[0_25px_70px_rgba(212,175,55,0.45)]');
        card.classList.add('border-white/10', 'shadow-lg');

        if (video) video.pause();
      } else if (offset === total - 1 || offset === -1) {
        // IMMEDIATE LEFT CARD
        card.style.transform = 'translateX(-70%) scale(0.82) rotateY(12deg)';
        card.style.zIndex = '20';
        card.style.opacity = '0.65';
        card.style.filter = 'brightness(0.8)';
        card.classList.remove('border-[#d4af37]', 'shadow-[0_25px_70px_rgba(212,175,55,0.45)]');
        card.classList.add('border-white/10', 'shadow-lg');

        if (video) video.pause();
      } else {
        // HIDDEN / FAR CARDS
        if (offset > 1 && offset < total / 2) {
          card.style.transform = 'translateX(130%) scale(0.65) rotateY(-20deg)';
        } else {
          card.style.transform = 'translateX(-130%) scale(0.65) rotateY(20deg)';
        }
        card.style.zIndex = '10';
        card.style.opacity = '0.2';
        card.style.filter = 'brightness(0.5)';
        if (video) video.pause();
      }
    });
  }

  // Card click handler
  cards.forEach((card, i) => {
    card.addEventListener('click', () => {
      if (currentIndex !== i) {
        currentIndex = i;
        updateCoverflow();
      }
    });

    // Sound toggle button setup
    const video = card.querySelector('video');
    const soundBtn = card.querySelector('.js-sound-toggle');
    const soundIcon = card.querySelector('.js-sound-icon');

    if (video && soundBtn && soundIcon) {
      soundBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        if (video.muted) {
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
        } else {
          video.muted = true;
          soundIcon.textContent = '🔇';
          soundBtn.classList.remove('bg-[#d4af37]', 'text-black');
          soundBtn.classList.add('bg-black/75', 'text-amber-300');
        }
      });
    }
  });

  // Navigation Arrows
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + total) % total;
      updateCoverflow();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % total;
      updateCoverflow();
    });
  }

  // Touch Swipe Gesture Handling for Mobile
  let touchStartX = 0;
  let touchEndX = 0;

  stage.addEventListener('touchstart', (e) => {
    if (e.touches && e.touches[0]) {
      touchStartX = e.touches[0].clientX;
    }
  }, { passive: true });

  stage.addEventListener('touchend', (e) => {
    if (e.changedTouches && e.changedTouches[0]) {
      touchEndX = e.changedTouches[0].clientX;
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) {
          // Swipe Left -> Next
          currentIndex = (currentIndex + 1) % total;
        } else {
          // Swipe Right -> Prev
          currentIndex = (currentIndex - 1 + total) % total;
        }
        updateCoverflow();
      }
    }
  });

  // Initial call
  updateCoverflow();
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
                content = content[:r_idx] + coverflow_reels_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED COVERFLOW REELS JS IN: {jspath}")

# HTML Files Update
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

coverflow_reels_section_html = """  <!-- Watch 3D Cover Flow Reels Section (Butter Smooth Apple Style 3D Carousel) -->
  <section class="py-10 sm:py-16 bg-[#07080b] border-b border-[#d4af37]/20 relative overflow-hidden">
    <!-- Ambient Gold Background Glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-96 bg-[#d4af37]/5 rounded-full filter blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Section Tagline Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/15 border border-[#d4af37]/40 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-widest mb-3 backdrop-blur-md shadow-lg">
        <span>🎬 REELS STUDIO &bull; 3D COVER FLOW</span>
      </div>

      <h2 class="font-serif text-2xl sm:text-5xl font-bold text-white mb-2 tracking-wide">
        Watch Hair Transformation <span class="gold-gradient-text">Reels</span>
      </h2>

      <p class="text-gray-300 text-xs sm:text-base max-w-xl mx-auto mb-6 font-light leading-relaxed">
        👈 <strong>Swipe or Tap Cards</strong> to rotate 3D customer transformations 👉
      </p>

      <!-- 3D Stage Wrapper with Left & Right Nav Buttons -->
      <div class="relative max-w-5xl mx-auto flex items-center justify-center">
        
        <!-- Left Nav Button -->
        <button id="CoverflowPrev" type="button" class="absolute left-2 sm:left-4 top-1/2 -translate-y-1/2 z-40 w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-black/80 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-lg shadow-2xl transition-all cursor-pointer focus:outline-none">
          &larr;
        </button>

        <!-- Right Nav Button -->
        <button id="CoverflowNext" type="button" class="absolute right-2 sm:right-4 top-1/2 -translate-y-1/2 z-40 w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-black/80 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-lg shadow-2xl transition-all cursor-pointer focus:outline-none">
          &rarr;
        </button>

        <!-- 3D Perspective Stage Container -->
        <div id="CoverflowStage" class="relative w-full h-[460px] sm:h-[560px] flex items-center justify-center select-none cursor-grab active:cursor-grabbing">
          
          <!-- Card 1 (Fix Grey Hair, Dandruff, Fall) -->
          <div class="js-3d-card absolute w-[250px] sm:w-[310px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] bg-black cursor-pointer shadow-2xl">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                🛡️ Scalp Solution
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/75 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
            </div>
            <video autoplay muted playsinline webkit-playsinline loop poster="./assets/reel-icon-4.jpg" class="w-full h-full object-cover bg-black">
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
          <div class="js-3d-card absolute w-[250px] sm:w-[310px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-white/10 bg-black cursor-pointer shadow-2xl">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ✨ Anti-Dandruff
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/75 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
            </div>
            <video muted playsinline webkit-playsinline loop poster="./assets/reel-icon-2.jpg" class="w-full h-full object-cover bg-black">
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
          <div class="js-3d-card absolute w-[250px] sm:w-[310px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-white/10 bg-black cursor-pointer shadow-2xl">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ⚡ Proven Results
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/75 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
            </div>
            <video muted playsinline webkit-playsinline loop poster="./assets/reel-icon-3.jpg" class="w-full h-full object-cover bg-black">
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
          <div class="js-3d-card absolute w-[250px] sm:w-[310px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-white/10 bg-black cursor-pointer shadow-2xl">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ❤️ Real Testimonial
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/75 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
            </div>
            <video muted playsinline webkit-playsinline loop poster="./assets/reel-icon-5.jpg" class="w-full h-full object-cover bg-black">
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
          <div class="js-3d-card absolute w-[250px] sm:w-[310px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-white/10 bg-black cursor-pointer shadow-2xl">
            <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
              <span class="bg-black/75 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-1 rounded-full border border-amber-500/30 shadow">
                ✨ Application Ritual
              </span>
              <button type="button" class="js-sound-toggle pointer-events-auto bg-black/75 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
                <span class="js-sound-icon">🔇</span> <span>Sound On</span>
              </button>
            </div>
            <video muted playsinline webkit-playsinline loop poster="./assets/reel-icon-1.jpg" class="w-full h-full object-cover bg-black">
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

        s_idx = content.find('<!-- Watch Reels')
        if s_idx == -1:
            s_idx = content.find('REELS STUDIO')
            if s_idx != -1:
                s_idx = content.rfind('<section', 0, s_idx)

        if s_idx != -1:
            e_idx = content.find('</section>', s_idx)
            if e_idx != -1:
                content = content[:s_idx] + coverflow_reels_section_html + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED 3D COVERFLOW REELS CAROUSEL IN: {fpath}")
