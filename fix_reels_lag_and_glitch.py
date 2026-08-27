import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

ultra_smooth_reels_js = """/* 🚀 Ultra-Performance Promise-Safe Reels Studio (Zero Lag, Zero Glitch) */
function initReelsModal() {
  const pills = document.querySelectorAll('.js-select-reel');
  const stageVideo = document.getElementById('StageReelVideo');
  const stageTag = document.getElementById('ReelStageTag');
  const stageTitle = document.getElementById('ReelStageTitle');
  const soundBtn = document.getElementById('StageSoundToggle');
  const soundIcon = document.getElementById('StageSoundIcon');
  const soundText = document.getElementById('StageSoundText');

  if (!pills.length || !stageVideo) return;

  let currentIndex = 0;
  let isSwitching = false;

  // Safe error fallback
  stageVideo.addEventListener('error', () => {
    isSwitching = false;
  });

  // End event -> Auto Next
  stageVideo.addEventListener('ended', () => {
    switchReel(currentIndex + 1);
  });

  function switchReel(index) {
    if (isSwitching) return;
    if (index < 0) index = pills.length - 1;
    if (index >= pills.length) index = 0;
    
    isSwitching = true;
    currentIndex = index;

    const activePill = pills[currentIndex];
    const videoSrc = activePill.getAttribute('data-video');
    const posterSrc = activePill.getAttribute('data-poster');
    const title = activePill.getAttribute('data-title');
    const tag = activePill.getAttribute('data-tag');

    if (posterSrc) {
      stageVideo.setAttribute('poster', posterSrc);
    }

    if (title && stageTitle) stageTitle.textContent = title;
    if (tag && stageTag) stageTag.textContent = tag;

    // Update Story Thumbnails Active Styling
    pills.forEach((pill, idx) => {
      if (idx === currentIndex) {
        pill.className = 'js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-[#d4af37]/20 border-2 border-[#d4af37] shadow-xl transition-all cursor-pointer focus:outline-none group w-24 sm:w-28';
        const ring = pill.querySelector('.js-ring');
        if (ring) ring.className = 'js-ring w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-amber-200 to-amber-500 shadow-md relative';
        const txt = pill.querySelector('.js-title');
        if (txt) txt.className = 'js-title text-[9px] font-extrabold text-amber-300 uppercase tracking-tight line-clamp-1 text-center';
      } else {
        pill.className = 'js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28';
        const ring = pill.querySelector('.js-ring');
        if (ring) ring.className = 'js-ring w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400';
        const txt = pill.querySelector('.js-title');
        if (txt) txt.className = 'js-title text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300';
      }
    });

    // Safely pause current playing video before switching
    try {
      stageVideo.pause();
    } catch(e) {}

    if (videoSrc) {
      stageVideo.src = videoSrc;
      const playPromise = stageVideo.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          isSwitching = false;
        }).catch(() => {
          isSwitching = false;
        });
      } else {
        isSwitching = false;
      }
    } else {
      isSwitching = false;
    }
  }

  pills.forEach((pill) => {
    pill.addEventListener('click', () => {
      const idx = parseInt(pill.getAttribute('data-reel-index')) || 0;
      switchReel(idx);
    });
  });

  if (soundBtn && soundIcon && soundText) {
    soundBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (stageVideo.muted) {
        stageVideo.muted = false;
        soundIcon.textContent = '🔊';
        soundText.textContent = 'Playing Sound';
        soundBtn.classList.remove('bg-black/70');
        soundBtn.classList.add('bg-[#d4af37]', 'text-black');
      } else {
        stageVideo.muted = true;
        soundIcon.textContent = '🔇';
        soundText.textContent = 'Sound On';
        soundBtn.classList.remove('bg-[#d4af37]', 'text-black');
        soundBtn.classList.add('bg-black/70', 'text-amber-300');
      }
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
                content = content[:r_idx] + ultra_smooth_reels_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED ULTRA-PERFORMANCE REELS JS IN: {jspath}")

# Update HTML Structure to add js-ring and js-title classes and remove yellow line overflow
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

ultra_smooth_reels_section_html = """  <!-- Watch Reels Section (Instagram / D2C Pro Mobile Experience) -->
  <section class="py-10 sm:py-16 bg-[#07080b] border-b border-[#d4af37]/20 relative overflow-hidden">
    <!-- Background Glow -->
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
        Experience real customer stories & doctor reviews in 9:16 vertical HD video.
      </p>

      <!-- Horizontal Stories Reel Selector Bar (Instagram Style - Touch Smooth) -->
      <div class="flex items-center justify-start sm:justify-center gap-3 overflow-x-auto no-scrollbar pb-3 mb-5 px-1 snap-x w-full">
        
        <!-- Story 1 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-[#d4af37]/20 border-2 border-[#d4af37] shadow-xl transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="0" data-title="Fix Grey Hair, Dandruff, Fall" data-views="29.8K Views" data-tag="🛡️ Scalp Solution" data-video="./assets/reel-4.mp4" data-poster="./assets/reel-icon-4.jpg">
          <div class="js-ring w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-amber-200 to-amber-500 shadow-md relative">
            <img src="./assets/reel-icon-4.jpg" alt="Reel 1" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="js-title text-[9px] font-extrabold text-amber-300 uppercase tracking-tight line-clamp-1 text-center">Fix Grey Hair</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">29.8K Views</span>
        </button>

        <!-- Story 2 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="1" data-title="Say No To Flaky Dandruff" data-views="38.9K Views" data-tag="✨ Dandruff Shield" data-video="./assets/reel-2.mp4" data-poster="./assets/reel-icon-2.jpg">
          <div class="js-ring w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-2.jpg" alt="Reel 2" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="js-title text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">No Dandruff</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">38.9K Views</span>
        </button>

        <!-- Story 3 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="2" data-title="Results Are 100% Real" data-views="61.2K Views" data-tag="⚡ Proven Results" data-video="./assets/reel-3.mp4" data-poster="./assets/reel-icon-3.jpg">
          <div class="js-ring w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-3.jpg" alt="Reel 3" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="js-title text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">100% Real</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">61.2K Views</span>
        </button>

        <!-- Story 4 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="3" data-title="Stop Premature Greying, Feel Confident" data-views="84.1K Views" data-tag="❤️ Real Testimonial" data-video="./assets/reel-5.mp4" data-poster="./assets/reel-icon-5.jpg">
          <div class="js-ring w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-5.jpg" alt="Reel 4" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="js-title text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">Stop Greying</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">84.1K Views</span>
        </button>

        <!-- Story 5 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="4" data-title="Your Roots, Naturally Reborn Black" data-views="52.4K Views" data-tag="✨ Product Application" data-video="./assets/reel-1.mp4" data-poster="./assets/reel-icon-1.jpg">
          <div class="js-ring w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-1.jpg" alt="Reel 5" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="js-title text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">Roots Reborn</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">52.4K Views</span>
        </button>

      </div>

      <!-- Center Stage: Royal 9:16 Video Player -->
      <div class="flex justify-center w-full">
        <div class="relative w-full max-w-[310px] sm:max-w-[360px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_60px_rgba(0,0,0,0.9)] bg-black group">
          
          <!-- Top Header Overlay Controls -->
          <div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
            <span id="ReelStageTag" class="bg-black/70 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-2.5 py-0.5 rounded-full border border-amber-500/30 shadow">
              🛡️ Scalp Solution
            </span>
            
            <button id="StageSoundToggle" type="button" class="pointer-events-auto bg-black/70 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer">
              <span id="StageSoundIcon">🔇</span>
              <span id="StageSoundText">Sound On</span>
            </button>
          </div>

          <!-- 9:16 Vertical HD Video Player (Seamless Poster, Promise-Safe Zero Glitch) -->
          <video id="StageReelVideo" autoplay muted playsinline webkit-playsinline poster="./assets/reel-icon-4.jpg" class="w-full h-full object-cover bg-black">
            <source src="./assets/reel-4.mp4" type="video/mp4">
          </video>

          <!-- Bottom Floating Shoppable Bar inside Player -->
          <div class="absolute bottom-3 left-3 right-3 z-30 p-2.5 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
            <div class="flex items-center gap-2 min-w-0">
              <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
              <div class="min-w-0 text-left">
                <h4 id="ReelStageTitle" class="text-[10px] font-extrabold text-white truncate">Fix Grey Hair, Dandruff, Fall</h4>
                <div class="flex items-center gap-1">
                  <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                  <span class="text-[8px] text-emerald-400 font-bold">FREE Shipping</span>
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
  </section>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('<!-- Watch Reels Section')
        if s_idx == -1:
            s_idx = content.find('REELS STUDIO')
            if s_idx != -1:
                s_idx = content.rfind('<section', 0, s_idx)

        if s_idx != -1:
            e_idx = content.find('</section>', s_idx)
            if e_idx != -1:
                content = content[:s_idx] + ultra_smooth_reels_section_html + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPDATED ULTRA-SMOOTH REELS SECTION HTML IN: {fpath}")
