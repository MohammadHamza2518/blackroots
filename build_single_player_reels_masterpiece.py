import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

single_player_reels_js = """/* 🎬 Single-Player Masterpiece Reel Engine (0% Memory Lag & 100% Instant Play) */
function initReelsModal() {
  const player = document.getElementById('MainReelPlayer');
  const cards = document.querySelectorAll('.js-reel-card');
  const tagBadge = document.getElementById('ReelTagBadge');
  const titleText = document.getElementById('ReelTitleText');
  const soundBtn = document.getElementById('ReelSoundToggle');
  const prevBtn = document.getElementById('ReelPrevBtn');
  const nextBtn = document.getElementById('ReelNextBtn');

  if (!player || !cards.length) return;

  let currentIndex = 0;

  const reelData = [
    { video: './assets/reel-4.mp4', title: 'Fix Grey Hair, Dandruff, Fall', views: '29.8K Views', tag: '🛡️ Scalp Solution' },
    { video: './assets/reel-2.mp4', title: 'Say No To Flaky Dandruff', views: '38.9K Views', tag: '✨ Anti-Dandruff' },
    { video: './assets/reel-3.mp4', title: 'Results Are 100% Real', views: '61.2K Views', tag: '⚡ Proven Results' },
    { video: './assets/reel-5.mp4', title: 'Stop Premature Greying', views: '84.1K Views', tag: '❤️ Real Testimonial' },
    { video: './assets/reel-1.mp4', title: 'Roots Reborn Black', views: '52.4K Views', tag: '✨ Application Ritual' }
  ];

  function loadReel(index) {
    if (index < 0) index = reelData.length - 1;
    if (index >= reelData.length) index = 0;
    currentIndex = index;

    const data = reelData[currentIndex];
    if (!data) return;

    // Update Player Source
    player.src = data.video;
    player.muted = true;
    player.playsInline = true;
    player.load();
    player.play().catch(() => {});

    // Update Overlay Labels
    if (tagBadge) tagBadge.textContent = data.tag;
    if (titleText) titleText.textContent = data.title;

    // Reset Sound Button
    if (soundBtn) {
      soundBtn.innerHTML = '<span>🔇</span> <span>Sound On</span>';
      soundBtn.className = 'pointer-events-auto bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-3 py-1.5 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1.5 shadow-xl cursor-pointer';
    }

    // Highlight active card
    cards.forEach((card, idx) => {
      if (idx === currentIndex) {
        card.className = 'js-reel-card snap-center shrink-0 w-[130px] sm:w-[150px] p-2.5 rounded-2xl bg-[#d4af37]/20 border-2 border-[#d4af37] text-left transition-all shadow-xl cursor-pointer opacity-100';
      } else {
        card.className = 'js-reel-card snap-center shrink-0 w-[130px] sm:w-[150px] p-2.5 rounded-2xl bg-white/5 border border-white/10 text-left transition-all hover:border-[#d4af37]/40 cursor-pointer opacity-60';
      }
    });
  }

  // AUTO-NEXT: When current reel finishes, automatically load next reel & play!
  player.addEventListener('ended', () => {
    loadReel(currentIndex + 1);
  });

  // Card click handlers
  cards.forEach((card, idx) => {
    card.addEventListener('click', () => {
      loadReel(idx);
    });
  });

  // Sound Toggle Handler
  if (soundBtn) {
    soundBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (player.muted) {
        player.muted = false;
        player.volume = 1.0;
        soundBtn.innerHTML = '<span>🔊</span> <span>Mute Sound</span>';
        soundBtn.className = 'pointer-events-auto bg-[#d4af37] text-black text-[10px] font-black px-3 py-1.5 rounded-full border border-[#d4af37] hover:scale-105 transition-transform flex items-center gap-1.5 shadow-xl cursor-pointer';
        player.play().catch(() => {});
      } else {
        player.muted = true;
        soundBtn.innerHTML = '<span>🔇</span> <span>Sound On</span>';
        soundBtn.className = 'pointer-events-auto bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-3 py-1.5 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1.5 shadow-xl cursor-pointer';
      }
    });
  }

  // Prev / Next Navigation Arrows
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      loadReel(currentIndex - 1);
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      loadReel(currentIndex + 1);
    });
  }

  // Touch Swipe Gesture on Player Stage
  let touchStartX = 0;
  let touchEndX = 0;

  player.parentElement.addEventListener('touchstart', (e) => {
    if (e.touches && e.touches[0]) {
      touchStartX = e.touches[0].clientX;
    }
  }, { passive: true });

  player.parentElement.addEventListener('touchend', (e) => {
    if (e.changedTouches && e.changedTouches[0]) {
      touchEndX = e.changedTouches[0].clientX;
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) {
          loadReel(currentIndex + 1); // Swipe Left -> Next
        } else {
          loadReel(currentIndex - 1); // Swipe Right -> Prev
        }
      }
    }
  });

  // Initial Reel Load
  loadReel(0);
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
                content = content[:r_idx] + single_player_reels_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED SINGLE-PLAYER REELS JS IN: {jspath}")

# HTML Files Update - Render 1 Single Player Stage + 5 Story Cards
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

single_player_html = """  <!-- Watch Reels Section (Single Player Masterpiece Engine - 0% Memory Lag) -->
  <section class="py-10 sm:py-16 bg-[#07080b] border-b border-[#d4af37]/20 relative overflow-hidden">
    <!-- Ambient Gold Glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-96 bg-[#d4af37]/5 rounded-full filter blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Section Tagline Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/15 border border-[#d4af37]/40 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-widest mb-3 backdrop-blur-md shadow-lg">
        <span>🎬 REELS STUDIO &bull; REAL RESULTS</span>
      </div>

      <h2 class="font-serif text-2xl sm:text-5xl font-bold text-white mb-2 tracking-wide">
        Watch Hair Transformation <span class="gold-gradient-text">Reels</span>
      </h2>

      <p class="text-gray-300 text-xs sm:text-base max-w-xl mx-auto mb-6 font-light leading-relaxed">
        👈 <strong>Swipe Player or Tap Cards</strong> to watch real 9:16 customer transformations 👉
      </p>

      <!-- Main Stage: Central 9:16 Video Player with Navigation Arrows -->
      <div class="relative max-w-sm sm:max-w-md mx-auto mb-6">
        
        <!-- Left Arrow Button -->
        <button id="ReelPrevBtn" type="button" class="absolute -left-3 sm:-left-6 top-1/2 -translate-y-1/2 z-40 w-11 h-11 rounded-full bg-black/80 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-lg shadow-2xl transition-all cursor-pointer focus:outline-none">
          &larr;
        </button>

        <!-- Right Arrow Button -->
        <button id="ReelNextBtn" type="button" class="absolute -right-3 sm:-right-6 top-1/2 -translate-y-1/2 z-40 w-11 h-11 rounded-full bg-black/80 border-2 border-[#d4af37] text-[#d4af37] hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-black text-lg shadow-2xl transition-all cursor-pointer focus:outline-none">
          &rarr;
        </button>

        <!-- Single Native Video Player Card -->
        <div class="relative w-full aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-[0_25px_65px_rgba(212,175,55,0.45)] bg-black group select-none">
          
          <!-- Top Overlay Controls -->
          <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none">
            <span id="ReelTagBadge" class="bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/30 shadow">
              🛡️ Scalp Solution
            </span>
            <button id="ReelSoundToggle" type="button" class="pointer-events-auto bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-3 py-1.5 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1.5 shadow-xl cursor-pointer">
              <span>🔇</span> <span>Sound On</span>
            </button>
          </div>

          <!-- THE SINGLE NATIVE HD VIDEO ELEMENT (0% Memory Overhead) -->
          <video id="MainReelPlayer" autoplay muted playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">
            <source src="./assets/reel-4.mp4" type="video/mp4">
          </video>

          <!-- Bottom Floating Shoppable Bar inside Player -->
          <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
            <div class="flex items-center gap-2.5 min-w-0">
              <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-9 h-9 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
              <div class="min-w-0 text-left">
                <h4 id="ReelTitleText" class="text-[11px] font-extrabold text-white truncate">Fix Grey Hair, Dandruff, Fall</h4>
                <div class="flex items-center gap-1.5">
                  <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                  <span class="text-[9px] text-emerald-400 font-bold">FREE Express Delivery</span>
                </div>
              </div>
            </div>

            <a href="product.html" class="js-trigger-order bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[10px] font-black px-3.5 py-2 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform">
              Buy Now &rarr;
            </a>
          </div>

        </div>

      </div>

      <!-- Bottom Horizontal Story Selector Cards -->
      <div class="flex items-center gap-3 overflow-x-auto no-scrollbar py-2 px-2 max-w-3xl mx-auto snap-x justify-start sm:justify-center">
        
        <!-- Story 1 -->
        <div class="js-reel-card snap-center shrink-0 w-[130px] sm:w-[150px] p-2.5 rounded-2xl bg-[#d4af37]/20 border-2 border-[#d4af37] text-left transition-all shadow-xl cursor-pointer opacity-100">
          <div class="flex items-center gap-2 mb-1">
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
            <span class="text-[9px] text-amber-300 font-extrabold uppercase">Reel 01</span>
          </div>
          <strong class="text-[10px] text-white font-bold block truncate">Fix Grey Hair</strong>
          <span class="text-[8px] text-gray-400 block font-light">29.8K Views</span>
        </div>

        <!-- Story 2 -->
        <div class="js-reel-card snap-center shrink-0 w-[130px] sm:w-[150px] p-2.5 rounded-2xl bg-white/5 border border-white/10 text-left transition-all hover:border-[#d4af37]/40 cursor-pointer opacity-60">
          <div class="flex items-center gap-2 mb-1">
            <span class="w-2 h-2 rounded-full bg-gray-500"></span>
            <span class="text-[9px] text-gray-400 font-bold uppercase">Reel 02</span>
          </div>
          <strong class="text-[10px] text-white font-bold block truncate">Anti-Dandruff</strong>
          <span class="text-[8px] text-gray-400 block font-light">38.9K Views</span>
        </div>

        <!-- Story 3 -->
        <div class="js-reel-card snap-center shrink-0 w-[130px] sm:w-[150px] p-2.5 rounded-2xl bg-white/5 border border-white/10 text-left transition-all hover:border-[#d4af37]/40 cursor-pointer opacity-60">
          <div class="flex items-center gap-2 mb-1">
            <span class="w-2 h-2 rounded-full bg-gray-500"></span>
            <span class="text-[9px] text-gray-400 font-bold uppercase">Reel 03</span>
          </div>
          <strong class="text-[10px] text-white font-bold block truncate">Proven Results</strong>
          <span class="text-[8px] text-gray-400 block font-light">61.2K Views</span>
        </div>

        <!-- Story 4 -->
        <div class="js-reel-card snap-center shrink-0 w-[130px] sm:w-[150px] p-2.5 rounded-2xl bg-white/5 border border-white/10 text-left transition-all hover:border-[#d4af37]/40 cursor-pointer opacity-60">
          <div class="flex items-center gap-2 mb-1">
            <span class="w-2 h-2 rounded-full bg-gray-500"></span>
            <span class="text-[9px] text-gray-400 font-bold uppercase">Reel 04</span>
          </div>
          <strong class="text-[10px] text-white font-bold block truncate">Stop Greying</strong>
          <span class="text-[8px] text-gray-400 block font-light">84.1K Views</span>
        </div>

        <!-- Story 5 -->
        <div class="js-reel-card snap-center shrink-0 w-[130px] sm:w-[150px] p-2.5 rounded-2xl bg-white/5 border border-white/10 text-left transition-all hover:border-[#d4af37]/40 cursor-pointer opacity-60">
          <div class="flex items-center gap-2 mb-1">
            <span class="w-2 h-2 rounded-full bg-gray-500"></span>
            <span class="text-[9px] text-gray-400 font-bold uppercase">Reel 05</span>
          </div>
          <strong class="text-[10px] text-white font-bold block truncate">Roots Reborn</strong>
          <span class="text-[8px] text-gray-400 block font-light">52.4K Views</span>
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
                content = content[:s_idx] + single_player_html + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"APPLIED SINGLE PLAYER REELS SECTION IN: {fpath}")
