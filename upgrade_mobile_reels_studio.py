import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

new_js_reels_code = """function initReelsModal() {
  const pills = document.querySelectorAll('.js-select-reel');
  const stageVideo = document.getElementById('StageReelVideo');
  const stageTag = document.getElementById('ReelStageTag');
  const stageTitle = document.getElementById('ReelStageTitle');
  const soundBtn = document.getElementById('StageSoundToggle');
  const soundIcon = document.getElementById('StageSoundIcon');
  const soundText = document.getElementById('StageSoundText');
  const progressBar = document.getElementById('ReelProgressBar');

  if (!pills.length || !stageVideo) return;

  let currentIndex = 0;

  stageVideo.addEventListener('error', () => {
    if (!stageVideo.src.includes('360%20shampoo.mp4') && !stageVideo.src.includes('360 shampoo.mp4')) {
      stageVideo.src = './assets/360 shampoo.mp4';
      stageVideo.load();
      stageVideo.play().catch(() => {});
    }
  });

  stageVideo.addEventListener('timeupdate', () => {
    if (progressBar && stageVideo.duration) {
      const percentage = (stageVideo.currentTime / stageVideo.duration) * 100;
      progressBar.style.width = percentage + '%';
    }
  });

  stageVideo.addEventListener('ended', () => {
    switchReel(currentIndex + 1);
  });

  function switchReel(index) {
    if (index < 0) index = pills.length - 1;
    if (index >= pills.length) index = 0;
    currentIndex = index;

    const activePill = pills[currentIndex];
    const videoSrc = activePill.getAttribute('data-video');
    const posterSrc = activePill.getAttribute('data-poster');
    const title = activePill.getAttribute('data-title');
    const tag = activePill.getAttribute('data-tag');

    // Set poster thumbnail before loading to eliminate white flash
    if (posterSrc) {
      stageVideo.setAttribute('poster', posterSrc);
    }

    if (videoSrc) {
      stageVideo.src = videoSrc;
      stageVideo.load();
      stageVideo.play().catch(() => {
        stageVideo.src = './assets/360 shampoo.mp4';
        stageVideo.load();
        stageVideo.play().catch(() => {});
      });
    }

    if (title && stageTitle) stageTitle.textContent = title;
    if (tag && stageTag) stageTag.textContent = tag;

    // Update Story Thumbnail Active Styling
    pills.forEach((pill, idx) => {
      if (idx === currentIndex) {
        pill.className = 'js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-[#d4af37]/15 border-2 border-[#d4af37] shadow-xl transition-all cursor-pointer focus:outline-none group w-24 sm:w-28';
        const ring = pill.querySelector('div');
        if (ring) ring.className = 'w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-amber-200 to-amber-500 shadow-md relative';
        const txt = pill.querySelector('span');
        if (txt) txt.className = 'text-[9px] font-extrabold text-amber-300 uppercase tracking-tight line-clamp-1 text-center';
      } else {
        pill.className = 'js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28';
        const ring = pill.querySelector('div');
        if (ring) ring.className = 'w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400';
        const txt = pill.querySelector('span');
        if (txt) txt.className = 'text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300';
      }
    });
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
        soundBtn.classList.remove('bg-black/80');
        soundBtn.classList.add('bg-[#d4af37]', 'text-black');
      } else {
        stageVideo.muted = true;
        soundIcon.textContent = '🔇';
        soundText.textContent = 'Sound On';
        soundBtn.classList.remove('bg-[#d4af37]', 'text-black');
        soundBtn.classList.add('bg-black/80', 'text-amber-300');
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
                content = content[:r_idx] + new_js_reels_code + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED REELS JS IN: {jspath}")

# HTML Files Update
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

new_reels_section_html = """  <!-- Watch Reels Section (Instagram / D2C Pro Mobile Experience) -->
  <section class="py-12 sm:py-20 bg-[#07080b] border-b border-[#d4af37]/20 relative overflow-hidden">
    <!-- Background Glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-96 bg-[#d4af37]/5 rounded-full filter blur-3xl pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <!-- Section Tagline Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/15 border border-[#d4af37]/40 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-widest mb-3 backdrop-blur-md shadow-lg">
        <span>🎬 REELS STUDIO &bull; REAL RESULTS</span>
      </div>

      <h2 class="font-serif text-2xl sm:text-5xl font-bold text-white mb-3 tracking-wide">
        Watch Hair Transformation <span class="gold-gradient-text">Reels</span>
      </h2>

      <p class="text-gray-300 text-xs sm:text-base max-w-xl mx-auto mb-8 font-light leading-relaxed">
        Experience real customer stories, 5-minute shower routines & doctor reviews in 9:16 vertical HD video.
      </p>

      <!-- Horizontal Stories Reel Selector Bar (Instagram Style) -->
      <div class="flex items-center justify-start sm:justify-center gap-3 overflow-x-auto no-scrollbar pb-4 mb-6 px-2 snap-x">
        
        <!-- Story 1 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-[#d4af37]/15 border-2 border-[#d4af37] shadow-xl transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="0" data-title="Fix Grey Hair, Dandruff, Fall" data-views="29.8K Views" data-tag="🛡️ Scalp Solution" data-video="./assets/reel-4.mp4" data-poster="./assets/reel-icon-4.jpg">
          <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-amber-200 to-amber-500 shadow-md relative">
            <img src="./assets/reel-icon-4.jpg" alt="Reel 1" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="text-[9px] font-extrabold text-amber-300 uppercase tracking-tight line-clamp-1 text-center">Fix Grey Hair</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">29.8K Views</span>
        </button>

        <!-- Story 2 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="1" data-title="Say No To Flaky Dandruff" data-views="38.9K Views" data-tag="✨ Dandruff Shield" data-video="./assets/reel-2.mp4" data-poster="./assets/reel-icon-2.jpg">
          <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-2.jpg" alt="Reel 2" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">No Dandruff</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">38.9K Views</span>
        </button>

        <!-- Story 3 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="2" data-title="Results Are 100% Real" data-views="61.2K Views" data-tag="⚡ Proven Results" data-video="./assets/reel-3.mp4" data-poster="./assets/reel-icon-3.jpg">
          <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-3.jpg" alt="Reel 3" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">100% Real</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">61.2K Views</span>
        </button>

        <!-- Story 4 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="3" data-title="Stop Premature Greying, Feel Confident" data-views="84.1K Views" data-tag="❤️ Real Testimonial" data-video="./assets/reel-5.mp4" data-poster="./assets/reel-icon-5.jpg">
          <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-5.jpg" alt="Reel 4" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">Stop Greying</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">84.1K Views</span>
        </button>

        <!-- Story 5 Thumbnail -->
        <button type="button" class="js-select-reel snap-center shrink-0 flex flex-col items-center gap-1.5 p-2 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 shadow-md transition-all cursor-pointer focus:outline-none group w-24 sm:w-28" data-reel-index="4" data-title="Your Roots, Naturally Reborn Black" data-views="52.4K Views" data-tag="✨ Product Application" data-video="./assets/reel-1.mp4" data-poster="./assets/reel-icon-1.jpg">
          <div class="w-12 h-12 sm:w-14 sm:h-14 rounded-full p-0.5 bg-gradient-to-tr from-gray-700 to-gray-400 shadow-md relative group-hover:from-[#d4af37] group-hover:to-amber-400">
            <img src="./assets/reel-icon-1.jpg" alt="Reel 5" class="w-full h-full object-cover rounded-full">
            <div class="absolute inset-0 bg-black/30 rounded-full flex items-center justify-center">
              <span class="text-amber-300 text-xs">▶</span>
            </div>
          </div>
          <span class="text-[9px] font-extrabold text-gray-200 uppercase tracking-tight line-clamp-1 text-center group-hover:text-amber-300">Roots Reborn</span>
          <span class="text-[8px] text-gray-400 font-semibold -mt-1">52.4K Views</span>
        </button>

      </div>

      <!-- Center Stage: Royal 9:16 Video Player -->
      <div class="flex justify-center w-full">
        <div class="relative w-full max-w-[320px] sm:max-w-[360px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_60px_rgba(0,0,0,0.9)] bg-black group">
          
          <!-- Story Progress Line -->
          <div class="absolute top-3 left-3 right-3 z-30 flex gap-1.5">
            <div class="h-1 flex-1 bg-white/30 rounded-full overflow-hidden">
              <div id="ReelProgressBar" class="h-full bg-[#d4af37] w-0 transition-all duration-300"></div>
            </div>
          </div>

          <!-- Top Header Overlay Controls -->
          <div class="absolute top-6 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">
            <span id="ReelStageTag" class="bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow">
              🛡️ Scalp Solution
            </span>
            
            <button id="StageSoundToggle" type="button" class="pointer-events-auto bg-black/80 backdrop-blur-md text-amber-300 text-[10px] sm:text-xs font-extrabold px-3 py-1 rounded-full border border-amber-500/40 hover:scale-105 transition-transform flex items-center gap-1.5 shadow-xl cursor-pointer">
              <span id="StageSoundIcon">🔇</span>
              <span id="StageSoundText">Sound On</span>
            </button>
          </div>

          <!-- 9:16 Vertical HD Video Player (Seamless Poster, Zero White Flash) -->
          <video id="StageReelVideo" autoplay muted playsinline webkit-playsinline poster="./assets/reel-icon-4.jpg" class="w-full h-full object-cover bg-black">
            <source src="./assets/reel-4.mp4" type="video/mp4">
          </video>

          <!-- Bottom Floating Shoppable Bar inside Player -->
          <div class="absolute bottom-3 left-3 right-3 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
            <div class="flex items-center gap-2.5 min-w-0">
              <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-9 h-9 object-contain rounded-lg bg-black/60 border border-white/10 shrink-0">
              <div class="min-w-0 text-left">
                <h4 id="ReelStageTitle" class="text-[11px] font-extrabold text-white truncate">Fix Grey Hair, Dandruff, Fall</h4>
                <div class="flex items-center gap-1.5">
                  <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                  <span class="text-[9px] text-emerald-400 font-bold">FREE Shipping</span>
                </div>
              </div>
            </div>

            <a href="product.html" class="js-trigger-order bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[10px] font-black px-3.5 py-2 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform">
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
                content = content[:s_idx] + new_reels_section_html + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED REELS SECTION HTML IN: {fpath}")
