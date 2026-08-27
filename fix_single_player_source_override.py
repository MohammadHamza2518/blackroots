import os

# 1. HTML Update: Set src attribute DIRECTLY on <video id="MainReelPlayer"> tag and remove child <source> tag
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        old_video_markup = """<video id="MainReelPlayer" autoplay muted playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">
            <source src="./assets/reel-4.mp4" type="video/mp4">
          </video>"""

        new_video_markup = """<video id="MainReelPlayer" src="./assets/reel-4.mp4" autoplay muted playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black"></video>"""

        content = content.replace(old_video_markup, new_video_markup)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED MAIN REEL PLAYER HTML TAG IN: {fpath}")

# 2. Update theme.js to handle direct src update + child source fallback + sound toggle + arrow click
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

fixed_single_player_js = """/* 🎬 Single-Player Masterpiece Reel Engine (Fixed Direct Source Switching) */
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

    // Update Player Source directly on video element + child source
    player.src = data.video;
    const childSource = player.querySelector('source');
    if (childSource) childSource.src = data.video;

    player.muted = true;
    player.playsInline = true;
    player.load();
    const playPromise = player.play();
    if (playPromise !== undefined) playPromise.catch(() => {});

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

  if (player.parentElement) {
    player.parentElement.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches[0]) {
        touchStartX = e.touches[0].clientX;
      }
    }, { passive: true });

    player.parentElement.addEventListener('touchend', (e) => {
      if (e.changedTouches && e.changedTouches[0]) {
        touchEndX = e.changedTouches[0].clientX;
        const diff = touchStartX - touchEndX;
        if (Math.abs(diff) > 35) {
          if (diff > 0) {
            loadReel(currentIndex + 1);
          } else {
            loadReel(currentIndex - 1);
          }
        }
      }
    });
  }

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
                content = content[:r_idx] + fixed_single_player_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED REELS JS IN: {jspath}")
