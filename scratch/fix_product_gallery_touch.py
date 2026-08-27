import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

gallery_engine_script = """
  <!-- 📸 High-Performance Touch & Thumbnail Gallery Engine -->
  <script>
    (function() {
      function initProductGallery() {
        const track = document.getElementById('ProductSlidesTrack');
        const counter = document.getElementById('CurrentSlideNum');
        const bestseller = document.getElementById('BestsellerBadge');
        const video = document.getElementById('ProductSlideVideo');
        const thumbBtns = document.querySelectorAll('.js-thumb-btn');

        if (!track) return;

        function updateActiveSlide(index) {
          // 1. Update active thumbnail styling
          thumbBtns.forEach((btn, idx) => {
            if (idx === index) {
              btn.classList.remove('border-white/10');
              btn.classList.add('border-2', 'border-[#d4af37]', 'shadow-lg');
            } else {
              btn.classList.remove('border-2', 'border-[#d4af37]', 'shadow-lg');
              btn.classList.add('border-white/10');
            }
          });

          // 2. Update slide counter (e.g. 1 / 6)
          if (counter) counter.textContent = index + 1;

          // 3. Update Bestseller badge
          if (bestseller) {
            bestseller.style.display = (index === 0) ? 'flex' : 'none';
          }

          // 4. Handle video playback
          if (video) {
            if (index === 5) {
              video.play().catch(() => {});
            } else {
              video.pause();
            }
          }
        }

        // Global function for onclick on thumbnails
        window.goToProductSlide = function(index) {
          if (!track) return;
          const slideWidth = track.clientWidth || track.offsetWidth;
          track.scrollTo({
            left: index * slideWidth,
            behavior: 'smooth'
          });
          updateActiveSlide(index);
        };

        // Touch & swipe listener to sync thumbnails as user swipes
        let isScrolling;
        track.addEventListener('scroll', function() {
          window.clearTimeout(isScrolling);
          isScrolling = setTimeout(function() {
            const slideWidth = track.clientWidth || track.offsetWidth;
            if (slideWidth > 0) {
              const activeIndex = Math.round(track.scrollLeft / slideWidth);
              if (activeIndex >= 0 && activeIndex < 6) {
                updateActiveSlide(activeIndex);
              }
            }
          }, 60);
        }, { passive: true });

        // Add explicit touch/click listeners to thumb buttons
        thumbBtns.forEach((btn, idx) => {
          btn.addEventListener('click', function(e) {
            e.preventDefault();
            window.goToProductSlide(idx);
          });
        });
      }

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initProductGallery);
      } else {
        initProductGallery();
      }
    })();
  </script>
"""

files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old broken changeMainProductImage script if present
    content = re.sub(r'<script>\s*function changeMainProductImage.*?<\/script>', '', content, flags=re.DOTALL)
    
    # Remove any duplicate old gallery script
    content = re.sub(r'<!-- 📸 High-Performance Touch & Thumbnail Gallery Engine -->.*?<\/script>', '', content, flags=re.DOTALL)

    # Insert clean gallery engine before closing body
    new_content = content.replace('</body>', gallery_engine_script + '\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Injected High-Performance Gallery Engine into", fpath)

