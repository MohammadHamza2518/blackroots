import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

glow_border_reels_js = """/* 🎬 Real-Time Swipe Gold Glow Border Engine (Instant Highlight on Centered Reel Card) */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const cards = container.querySelectorAll('.js-reel-card');
  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  if (!cards.length) return;

  let activeIndex = -1;

  // Force play & preload all 5 videos natively
  cards.forEach((card, idx) => {
    const video = card.querySelector('video');
    if (video) {
      video.muted = true;
      video.playsInline = true;
      video.setAttribute('playsinline', '');
      video.setAttribute('webkit-playsinline', '');
      video.setAttribute('autoplay', '');
      video.setAttribute('loop', '');
      video.preload = 'auto';
      
      const p = video.play();
      if (p !== undefined) p.catch(() => {});
    }

    // Click card to center
    card.addEventListener('click', () => {
      scrollToCardIndex(idx);
    });

    // Sound toggle handling
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

  function updateActiveHighlight(index) {
    if (activeIndex === index) return;
    activeIndex = index;

    cards.forEach((c, i) => {
      const v = c.querySelector('video');
      if (i === activeIndex) {
        // Active Centered Card -> Glowing Gold Border & High Opacity
        c.className = 'js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-[0_25px_65px_rgba(212,175,55,0.45)] relative bg-black group transition-all duration-300 cursor-pointer opacity-100';
        if (v) v.play().catch(() => {});
      } else {
        // Inactive Side Card -> Subtle Border & Dimmed Opacity
        c.className = 'js-reel-card snap-center shrink-0 w-[270px] sm:w-[320px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-white/10 shadow-xl relative bg-black group transition-all duration-300 cursor-pointer opacity-50';
      }
    });
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
    updateActiveHighlight(index);
  }

  // Real-Time Scroll Listener for Finger Swipe
  let scrollTimer = null;
  container.addEventListener('scroll', () => {
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(() => {
      const closest = getCenteredCardIndex();
      updateActiveHighlight(closest);
    }, 40);
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

  // Initial call
  setTimeout(() => {
    updateActiveHighlight(0);
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
                content = content[:r_idx] + glow_border_reels_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED GLOW BORDER SWIPE REELS JS IN: {jspath}")
