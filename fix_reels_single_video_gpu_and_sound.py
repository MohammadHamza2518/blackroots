import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

single_gpu_sound_js = """/* 🎬 Single-Video GPU Decoder Engine (0% Lag) + Bulletproof Sound On/Off Toggle */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const cards = container.querySelectorAll('.js-reel-card');
  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  if (!cards.length) return;

  let activeIndex = -1;

  // Single Video Playback Management (Pauses 4 off-screen videos to free 100% GPU memory)
  function setActiveReel(index) {
    if (index < 0) index = cards.length - 1;
    if (index >= cards.length) index = 0;

    activeIndex = index;

    cards.forEach((card, idx) => {
      const video = card.querySelector('video');

      if (idx === activeIndex) {
        // Highlight active centered card
        card.classList.add('border-[#d4af37]', 'opacity-100');
        card.classList.remove('border-white/10', 'opacity-60');

        if (video) {
          video.muted = true;
          video.playsInline = true;
          video.setAttribute('playsinline', '');
          video.setAttribute('webkit-playsinline', '');
          
          const p = video.play();
          if (p !== undefined) p.catch(() => {});
        }
      } else {
        // Pause off-screen video to prevent GPU lag & stuttering
        card.classList.remove('border-[#d4af37]', 'opacity-100');
        card.classList.add('border-white/10', 'opacity-60');

        if (video) {
          video.pause();
        }
      }
    });
  }

  // Calculate centered card index in real-time
  function getCenteredCardIndex() {
    const containerCenter = container.scrollLeft + (container.clientWidth / 2);
    let minDiff = Infinity;
    let closestIndex = 0;

    cards.forEach((card, idx) => {
      const cardCenter = card.offsetLeft + (card.clientWidth / 2);
      const diff = Math.abs(containerCenter - cardCenter);
      if (diff < minDiff) {
        minDiff = diff;
        closestIndex = idx;
      }
    });

    return closestIndex;
  }

  function scrollToCardIndex(index) {
    if (index < 0) index = cards.length - 1;
    if (index >= cards.length) index = 0;

    const card = cards[index];
    if (!card) return;

    const containerWidth = container.clientWidth;
    const cardLeft = card.offsetLeft;
    const cardWidth = card.clientWidth;
    const targetScroll = cardLeft - (containerWidth / 2) + (cardWidth / 2);

    container.scrollTo({ left: targetScroll, behavior: 'smooth' });
    setActiveReel(index);
  }

  // Setup Sound Toggle & Touch Handlers
  cards.forEach((card, cardIdx) => {
    const video = card.querySelector('video');
    const soundBtn = card.querySelector('.js-sound-toggle');

    if (video) {
      // When video ends, smoothly scroll to next card
      video.addEventListener('ended', () => {
        scrollToCardIndex(cardIdx + 1);
      });
    }

    // Sound Toggle Handler (Bulletproof click on button or inner spans)
    if (soundBtn && video) {
      soundBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        if (video.muted) {
          // Mute all other videos first
          cards.forEach(c => {
            const v = c.querySelector('video');
            const btn = c.querySelector('.js-sound-toggle');
            if (v) v.muted = true;
            if (btn) {
              btn.innerHTML = '<span>🔇</span> <span>Sound On</span>';
              btn.className = 'js-sound-toggle pointer-events-auto bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer';
            }
          });

          // Unmute active video
          video.muted = false;
          video.volume = 1.0;
          soundBtn.innerHTML = '<span>🔊</span> <span>Mute Sound</span>';
          soundBtn.className = 'js-sound-toggle pointer-events-auto bg-[#d4af37] text-black text-[10px] font-black px-2.5 py-1 rounded-full border border-[#d4af37] hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer';
          
          const p = video.play();
          if (p !== undefined) p.catch(() => {});
        } else {
          video.muted = true;
          soundBtn.innerHTML = '<span>🔇</span> <span>Sound On</span>';
          soundBtn.className = 'js-sound-toggle pointer-events-auto bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer';
        }
      });
    }

    // Card click to center
    card.addEventListener('click', () => {
      scrollToCardIndex(cardIdx);
    });
  });

  // Real-Time Scroll Listener for Finger Swipe
  let scrollTimer = null;
  container.addEventListener('scroll', () => {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(() => {
      const closest = getCenteredCardIndex();
      setActiveReel(closest);
    }, 50);
  }, { passive: true });

  // Navigation Arrows
  if (leftArrow) {
    leftArrow.addEventListener('click', () => {
      scrollToCardIndex(activeIndex - 1);
    });
  }

  if (rightArrow) {
    rightArrow.addEventListener('click', () => {
      scrollToCardIndex(activeIndex + 1);
    });
  }

  // Initial setup: Center Card 0 & play
  setTimeout(() => {
    setActiveReel(0);
  }, 100);
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
                content = content[:r_idx] + single_gpu_sound_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED SINGLE-GPU SOUND REELS JS IN: {jspath}")

# Remove 'autoplay' from HTML video tags so videos don't all decode simultaneously!
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        old_tag = '<video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">'
        new_tag = '<video muted playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">'
        content = content.replace(old_tag, new_tag)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REMOVED ALL-AUTOPLAY PARALLEL LOAD FROM: {fpath}")
