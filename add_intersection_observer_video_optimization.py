import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

intersection_observer_js = """/* 🚀 Ultra-Fast Mobile IntersectionObserver Video Renderer (0% Lag, 100% Instant Play) */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const cards = container.querySelectorAll('.js-reel-card');
  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  // IntersectionObserver: Play ONLY visible centered video, pause off-screen videos for 0% mobile GPU lag
  if ('IntersectionObserver' in window) {
    const reelObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const video = entry.target.querySelector('video');
        if (!video) return;

        if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
          video.muted = true;
          video.playsInline = true;
          const p = video.play();
          if (p !== undefined) p.catch(() => {});
        } else {
          video.pause();
        }
      });
    }, {
      root: container,
      threshold: 0.5
    });

    cards.forEach(card => reelObserver.observe(card));
  }

  // Full Card Click -> Open Instagram Reel (Except Buy Now button)
  cards.forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', (e) => {
      if (e.target.closest('.js-trigger-order')) return;

      const igLinkEl = card.querySelector('a[href*="instagram.com"]');
      if (igLinkEl && igLinkEl.href) {
        window.open(igLinkEl.href, '_blank', 'noopener,noreferrer');
      }
    });
  });

  // Arrow controls
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
                content = content[:r_idx] + intersection_observer_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED INTERSECTION OBSERVER VIDEO JS IN: {jspath}")
