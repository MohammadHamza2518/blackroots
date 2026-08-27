import os
import glob
import re

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Remove unused heavy Three.js scripts
        content = re.sub(r'<script\s+src="https://cdnjs\.cloudflare\.com/ajax/libs/three\.js/[^"]*"></script>', '', content)
        content = re.sub(r'<script\s+src="https://cdn\.jsdelivr\.net/npm/three[^"]*"></script>', '', content)

        # 2. Add loading="lazy" and decoding="async" to all <img> tags that don't already have it
        def optimize_img(match):
            tag = match.group(0)
            if 'loading=' not in tag and 'blackroots-logo' not in tag:
                tag = tag[:-1] + ' loading="lazy" decoding="async">'
            return tag
        content = re.sub(r'<img\s+[^>]*>', optimize_img, content)

        # 3. Optimize Product360Video preload to none
        content = content.replace('id="Product360Video" autoplay loop muted playsinline webkit-playsinline', 'id="Product360Video" loop muted playsinline webkit-playsinline preload="none"')

        # 4. Replace GPU-heavy blur filters on ambient glow backgrounds with ultra-light radial gradients
        content = re.sub(r'class="([^"]*)filter\s+blur-\[\d+px\]([^"]*)"', r'class="\1\2" style="background: radial-gradient(circle, rgba(212,175,55,0.08) 0%, transparent 70%);"', content)
        content = re.sub(r'class="([^"]*)filter\s+blur-3xl([^"]*)"', r'class="\1\2" style="background: radial-gradient(circle, rgba(212,175,55,0.06) 0%, transparent 70%);"', content)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"OPTIMIZED PERFORMANCE & ZERO-LAG IN: {fpath}")

# 5. Update assets/theme.js with high-performance 60fps video intersection observer
js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

smooth_scroll_engine = """/* 🚀 Ultra-High Performance 60FPS Video & Scroll Memory Optimizer */
(function() {
  if (typeof window === 'undefined') return;

  function initPerformanceOptimizer() {
    // 1. Smart Video Intersection Observer (Zero GPU Lag)
    const videos = document.querySelectorAll('video');
    if ('IntersectionObserver' in window && videos.length > 0) {
      const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          const vid = entry.target;
          if (entry.isIntersecting && entry.intersectionRatio >= 0.3) {
            vid.play().catch(() => {});
          } else {
            if (!vid.paused) {
              vid.pause();
            }
          }
        });
      }, { threshold: [0.0, 0.3, 0.7] });

      videos.forEach(v => videoObserver.observe(v));
    }

    // 2. Hardware Acceleration on Carousel
    const carousel = document.getElementById('ReelsCarouselContainer');
    if (carousel) {
      carousel.style.willChange = 'scroll-position';
      carousel.style.transform = 'translateZ(0)';
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPerformanceOptimizer);
  } else {
    initPerformanceOptimizer();
  }
})();"""

for jpath in js_files:
    if os.path.exists(jpath):
        with open(jpath, 'r', encoding='utf-8') as f:
            content = f.read()

        idx = content.find('/* 🚀 Ultra-High Performance')
        if idx != -1:
            content = content[:idx] + smooth_scroll_engine
        else:
            content += "\n\n" + smooth_scroll_engine

        with open(jpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"OPTIMIZED SMOOTH JS ENGINE IN: {jpath}")
