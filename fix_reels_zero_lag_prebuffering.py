import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

zero_lag_reels_js = """/* 🎬 Zero-Lag Pre-Buffered Mobile Reel Engine (Instant 0.00s Video Play on Swipe) */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const cards = container.querySelectorAll('.js-reel-card');
  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  if (!cards.length) return;

  let activeIndex = -1;
  let isAutoScrolling = false;

  // PRE-BUFFER ALL VIDEOS FOR INSTANT 0.00s PLAYBACK
  cards.forEach((card) => {
    const video = card.querySelector('video');
    if (video) {
      video.muted = true;
      video.playsInline = true;
      video.setAttribute('playsinline', '');
      video.setAttribute('webkit-playsinline', '');
      video.preload = 'auto';
      video.load(); // Warm up buffer in RAM
    }
  });

  // Exact container-only smooth scroll helper
  function scrollToCardIndex(index) {
    if (index < 0) index = cards.length - 1;
    if (index >= cards.length) index = 0;

    const card = cards[index];
    if (!card) return;

    isAutoScrolling = true;
    const containerWidth = container.clientWidth;
    const cardLeft = card.offsetLeft;
    const cardWidth = card.clientWidth;
    const targetScroll = cardLeft - (containerWidth / 2) + (cardWidth / 2);

    container.scrollTo({ left: targetScroll, behavior: 'smooth' });

    // Trigger video playback immediately during scroll
    setActiveCard(index);

    setTimeout(() => {
      isAutoScrolling = false;
    }, 400);
  }

  // Calculate centered card index
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

  function setActiveCard(index) {
    if (activeIndex === index) return;
    activeIndex = index;

    cards.forEach((card, idx) => {
      const video = card.querySelector('video');

      if (idx === activeIndex) {
        // Active centered card
        card.classList.add('border-[#d4af37]', 'shadow-[0_25px_65px_rgba(212,175,55,0.45)]', 'opacity-100');
        card.classList.remove('border-white/10', 'opacity-50');

        if (video) {
          video.muted = true;
          video.playsInline = true;
          video.currentTime = 0;

          const playPromise = video.play();
          if (playPromise !== undefined) {
            playPromise.catch(() => {});
          }
        }
      } else {
        // Inactive side card
        card.classList.remove('border-[#d4af37]', 'shadow-[0_25px_65px_rgba(212,175,55,0.45)]', 'opacity-100');
        card.classList.add('border-white/10', 'opacity-50');

        if (video) {
          video.pause();
        }
      }
    });
  }

  // Instant Touch End Listener for Mobile Gestures
  container.addEventListener('touchend', () => {
    setTimeout(() => {
      const idx = getCenteredCardIndex();
      scrollToCardIndex(idx);
    }, 50);
  }, { passive: true });

  // Scroll Event Listener
  let scrollTimeout = null;
  container.addEventListener('scroll', () => {
    if (isAutoScrolling) return;
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
      const idx = getCenteredCardIndex();
      setActiveCard(idx);
    }, 60);
  }, { passive: true });

  // Setup video ended & sound toggle handlers
  cards.forEach((card, cardIdx) => {
    const video = card.querySelector('video');

    if (video) {
      // AUTO-NEXT: When current video finishes, automatically slide to next card & play!
      video.addEventListener('ended', () => {
        const nextIndex = (cardIdx + 1) % cards.length;
        scrollToCardIndex(nextIndex);
      });
    }

    // Click card to center & play
    card.addEventListener('click', () => {
      scrollToCardIndex(cardIdx);
    });

    // Sound toggle
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

  // Initial center & play Reel 01
  setTimeout(() => {
    scrollToCardIndex(0);
  }, 150);
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
                content = content[:r_idx] + zero_lag_reels_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED ZERO-LAG REELS JS IN: {jspath}")
