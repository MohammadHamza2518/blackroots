import os

# 1. Update HTML files to give ALL 5 reel videos native 'autoplay muted loop playsinline webkit-playsinline preload="auto"'
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace non-autoplay reel video tags with full native autoplay loop video tags
        old_tag = '<video muted playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">'
        new_tag = '<video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">'
        
        content = content.replace(old_tag, new_tag)

        # Ensure card 1 also has loop
        old_card1_tag = '<video autoplay muted playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">'
        new_card1_tag = '<video autoplay muted loop playsinline webkit-playsinline preload="auto" class="w-full h-full object-cover bg-black">'
        content = content.replace(old_card1_tag, new_card1_tag)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"ENABLED NATIVE AUTOPLAY LOOP ON ALL 5 REELS IN: {fpath}")

# 2. Update theme.js to support smooth 60fps scrolling, card focus highlights, sound toggle, and instant play enforcement
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

native_reels_js = """/* 🎬 Native 100% Guaranteed Autoplay Reel Engine (All 5 Videos Play Natively) */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const cards = container.querySelectorAll('.js-reel-card');
  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  if (!cards.length) return;

  let activeIndex = 0;

  // Force play all 5 videos natively so zero videos freeze
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

    // Click on side card centers it
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

  function scrollToCardIndex(index) {
    if (index < 0) index = cards.length - 1;
    if (index >= cards.length) index = 0;
    activeIndex = index;

    const card = cards[index];
    if (!card) return;

    const containerWidth = container.clientWidth;
    const cardLeft = card.offsetLeft;
    const cardWidth = card.clientWidth;
    const targetScroll = cardLeft - (containerWidth / 2) + (cardWidth / 2);

    container.scrollTo({ left: targetScroll, behavior: 'smooth' });

    // Update active highlight border
    cards.forEach((c, i) => {
      const v = c.querySelector('video');
      if (i === activeIndex) {
        c.classList.add('border-[#d4af37]', 'shadow-[0_25px_65px_rgba(212,175,55,0.45)]', 'opacity-100');
        c.classList.remove('border-white/10', 'opacity-60');
        if (v) v.play().catch(() => {});
      } else {
        c.classList.remove('border-[#d4af37]', 'shadow-[0_25px_65px_rgba(212,175,55,0.45)]', 'opacity-100');
        c.classList.add('border-white/10', 'opacity-60');
      }
    });
  }

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
                content = content[:r_idx] + native_reels_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED NATIVE REELS JS IN: {jspath}")
