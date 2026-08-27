import os
import shutil
import subprocess

# 1. Run apply_touch_swipe_gallery.py
os.system("python apply_touch_swipe_gallery.py")

# 2. Add full swipe & thumbnail synchronization logic to assets/theme.js
js_code_to_add = """
/* ==========================================================================
   📸 BLACKROOTS 1:1 SQUARE PRODUCT GALLERY TOUCH-SWIPE ENGINE
   ========================================================================== */
let currentProductSlideIndex = 0;
const totalProductSlides = 6;

window.goToProductSlide = function(index) {
  const track = document.getElementById('ProductSlidesTrack');
  const counterEl = document.getElementById('CurrentSlideNum');
  const bestsellerBadge = document.getElementById('BestsellerBadge');
  const videoEl = document.getElementById('ProductSlideVideo');

  if (!track) return;

  index = Math.max(0, Math.min(totalProductSlides - 1, index));
  currentProductSlideIndex = index;

  const slideWidth = track.clientWidth;
  track.scrollTo({
    left: index * slideWidth,
    behavior: 'smooth'
  });

  if (counterEl) counterEl.textContent = (index + 1);

  if (bestsellerBadge) {
    bestsellerBadge.style.display = index === 0 ? 'flex' : 'none';
  }

  if (videoEl) {
    if (index === 5) {
      videoEl.play().catch(() => {});
    } else {
      videoEl.pause();
    }
  }

  // Update Thumbnail Borders
  document.querySelectorAll('.js-thumb-btn').forEach((btn, i) => {
    if (i === index) {
      btn.classList.remove('border-white/10');
      btn.classList.add('border-2', 'border-[#d4af37]');
    } else {
      btn.classList.remove('border-2', 'border-[#d4af37]');
      btn.classList.add('border-white/10');
    }
  });
};

window.slideProductGallery = function(direction) {
  let nextIndex = currentProductSlideIndex + direction;
  if (nextIndex < 0) nextIndex = totalProductSlides - 1;
  if (nextIndex >= totalProductSlides) nextIndex = 0;
  window.goToProductSlide(nextIndex);
};

function initProductGalleryTouchSwipe() {
  const track = document.getElementById('ProductSlidesTrack');
  if (!track) return;

  let scrollTimeout;
  track.addEventListener('scroll', () => {
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
      const slideWidth = track.clientWidth;
      if (slideWidth <= 0) return;
      const detectedIndex = Math.round(track.scrollLeft / slideWidth);
      if (detectedIndex !== currentProductSlideIndex && detectedIndex >= 0 && detectedIndex < totalProductSlides) {
        currentProductSlideIndex = detectedIndex;
        const counterEl = document.getElementById('CurrentSlideNum');
        if (counterEl) counterEl.textContent = (detectedIndex + 1);

        const bestsellerBadge = document.getElementById('BestsellerBadge');
        if (bestsellerBadge) bestsellerBadge.style.display = detectedIndex === 0 ? 'flex' : 'none';

        const videoEl = document.getElementById('ProductSlideVideo');
        if (videoEl) {
          if (detectedIndex === 5) videoEl.play().catch(() => {});
          else videoEl.pause();
        }

        document.querySelectorAll('.js-thumb-btn').forEach((btn, i) => {
          if (i === detectedIndex) {
            btn.classList.remove('border-white/10');
            btn.classList.add('border-2', 'border-[#d4af37]');
          } else {
            btn.classList.remove('border-2', 'border-[#d4af37]');
            btn.classList.add('border-white/10');
          }
        });
      }
    }, 50);
  }, { passive: true });

  // Touch Swipe Gesture Detection for Ultra-Smooth Mobile Experience
  let touchStartX = 0;
  let touchEndX = 0;

  track.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  track.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diffX = touchStartX - touchEndX;
    if (Math.abs(diffX) > 40) {
      if (diffX > 0) {
        window.slideProductGallery(1); // Swipe Left -> Next
      } else {
        window.slideProductGallery(-1); // Swipe Right -> Prev
      }
    }
  }, { passive: true });
}
"""

with open('assets/theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Append or replace
if 'BLACKROOTS 1:1 SQUARE PRODUCT GALLERY TOUCH-SWIPE ENGINE' not in js:
    js += "\n" + js_code_to_add

# Ensure initProductGalleryTouchSwipe is called inside DOMContentLoaded
if 'initProductGalleryTouchSwipe()' not in js:
    js = js.replace('document.addEventListener("DOMContentLoaded", () => {', 'document.addEventListener("DOMContentLoaded", () => {\n  initProductGalleryTouchSwipe();')

with open('assets/theme.js', 'w', encoding='utf-8') as f:
    f.write(js)

shutil.copy('assets/theme.js', 'demo_lab/assets/theme.js')
shutil.copy('assets/theme.js', 'preview/assets/theme.js')

for f in ['assets/theme.js', 'demo_lab/assets/theme.js', 'preview/assets/theme.js']:
    res = subprocess.run(['node', '-c', f], capture_output=True, text=True)
    print(f, "Syntax return code:", res.returncode)
