import os, re

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

carousel_html = """      <!-- Startup-Grade Luxury Customer Reviews Carousel Slider Deck -->
      <div id="reviews-carousel-section" class="my-8 relative">
        
        <!-- Slider Navigation Control Bar -->
        <div class="flex items-center justify-between mb-6 pb-4 border-b border-white/10">
          <div class="flex items-center gap-3">
            <div class="w-3 h-3 rounded-full bg-[#d4af37] animate-ping"></div>
            <h3 class="text-xs sm:text-sm font-bold text-gray-200 uppercase tracking-wider">
              Verified Shopper Experience Deck
            </h3>
            <span id="slider-slide-badge" class="text-[11px] font-extrabold text-amber-300 bg-amber-400/10 border border-amber-400/30 px-3 py-1 rounded-full">
              Slide 1 of 4
            </span>
          </div>

          <!-- Slider Arrow Buttons -->
          <div class="flex items-center gap-2">
            <button type="button" id="prev-slide-btn" class="w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-white/5 border border-white/15 text-white hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37] flex items-center justify-center text-xl font-bold shadow-lg transition-all transform active:scale-95 cursor-pointer disabled:opacity-30 disabled:pointer-events-none" title="Previous Slide">
              ‹
            </button>
            <button type="button" id="next-slide-btn" class="w-10 h-10 sm:w-11 sm:h-11 rounded-full bg-white/5 border border-white/15 text-white hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37] flex items-center justify-center text-xl font-bold shadow-lg transition-all transform active:scale-95 cursor-pointer disabled:opacity-30 disabled:pointer-events-none" title="Next Slide">
              ›
            </button>
          </div>
        </div>

        <!-- Carousel Viewport & Track -->
        <div id="carousel-viewport" class="overflow-hidden relative rounded-3xl p-1">
          <div id="carousel-track" class="flex transition-transform duration-500 ease-out w-full">
            <!-- Dynamic Slide Grids rendered here -->
          </div>
        </div>

        <!-- Slider Dots & Indicator Footer -->
        <div class="mt-8 flex flex-col items-center gap-3 text-center">
          <div id="slider-dots-container" class="flex items-center justify-center gap-2">
            <!-- Dynamically populated slide dots -->
          </div>
          <p class="text-[11px] text-gray-400">
            💡 Swipe left/right or use <strong class="text-amber-300">‹ › arrows</strong> to explore verified customer reviews slides.
          </p>
        </div>

      </div>"""

carousel_script = """  <script>
    // BlackRoots Startup-Grade Luxury Carousel Slider Engine
    document.addEventListener('DOMContentLoaded', function() {
      const CARDS_PER_SLIDE = 6;
      let currentSlide = 0;
      let currentFilter = 'all';

      const grid = document.querySelector('.columns-1');
      const carouselTrack = document.getElementById('carousel-track');
      const prevBtn = document.getElementById('prev-slide-btn');
      const nextBtn = document.getElementById('next-slide-btn');
      const slideBadge = document.getElementById('slider-slide-badge');
      const dotsContainer = document.getElementById('slider-dots-container');
      const filterBtns = document.querySelectorAll('.js-filter-btn');
      const showingCount = document.querySelector('.js-showing-count');
      const sortSelect = document.getElementById('reviews-sort');

      // Preserve all initial review cards from HTML
      let allCardsArray = [];
      if (grid) {
        allCardsArray = Array.from(grid.querySelectorAll('[data-category]'));
      }

      function updateSlider() {
        if (!carouselTrack) return;

        // Filter cards
        const matchingCards = allCardsArray.filter(card => {
          const cats = card.getAttribute('data-category') || '';
          return currentFilter === 'all' || cats.includes(currentFilter);
        });

        const totalItems = matchingCards.length;
        const totalSlides = Math.ceil(totalItems / CARDS_PER_SLIDE) || 1;

        if (currentSlide >= totalSlides) currentSlide = totalSlides - 1;
        if (currentSlide < 0) currentSlide = 0;

        // Render Carousel Slides Track
        carouselTrack.innerHTML = '';

        for (let s = 0; s < totalSlides; s++) {
          const slideDiv = document.createElement('div');
          slideDiv.className = "review-slide min-w-full shrink-0 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-1";
          
          const startIdx = s * CARDS_PER_SLIDE;
          const endIdx = startIdx + CARDS_PER_SLIDE;
          const slideCards = matchingCards.slice(startIdx, endIdx);

          slideCards.forEach(card => {
            card.style.display = 'block';
            slideDiv.appendChild(card);
          });

          carouselTrack.appendChild(slideDiv);
        }

        // Apply Translate Transform Slide Transition
        carouselTrack.style.transform = `translateX(-${currentSlide * 100}%)`;

        // Update Badge & Header Counts
        if (slideBadge) slideBadge.textContent = `Slide ${currentSlide + 1} of ${totalSlides}`;
        if (showingCount) showingCount.textContent = `${totalItems} Verified Reviews`;

        // Update Prev / Next Buttons State
        if (prevBtn) prevBtn.disabled = (currentSlide === 0);
        if (nextBtn) nextBtn.disabled = (currentSlide >= totalSlides - 1);

        // Render Animated Slide Dots
        if (dotsContainer) {
          dotsContainer.innerHTML = '';
          if (totalSlides <= 1) {
            dotsContainer.style.display = 'none';
          } else {
            dotsContainer.style.display = 'flex';
            for (let i = 0; i < totalSlides; i++) {
              const dot = document.createElement('button');
              dot.type = 'button';
              dot.className = `transition-all duration-300 cursor-pointer ${i === currentSlide ? 'w-8 h-2.5 bg-[#d4af37] rounded-full shadow-lg' : 'w-2.5 h-2.5 bg-white/20 hover:bg-white/40 rounded-full'}`;
              dot.setAttribute('title', `Go to Slide ${i + 1}`);
              dot.onclick = function(e) {
                e.preventDefault();
                currentSlide = i;
                updateSlider();
              };
              dotsContainer.appendChild(dot);
            }
          }
        }
      }

      // Prev / Next Button Handlers
      if (prevBtn) {
        prevBtn.onclick = function(e) {
          e.preventDefault();
          if (currentSlide > 0) {
            currentSlide--;
            updateSlider();
          }
        };
      }

      if (nextBtn) {
        nextBtn.onclick = function(e) {
          e.preventDefault();
          const totalSlides = Math.ceil(allCardsArray.filter(c => currentFilter === 'all' || (c.getAttribute('data-category')||'').includes(currentFilter)).length / CARDS_PER_SLIDE);
          if (currentSlide < totalSlides - 1) {
            currentSlide++;
            updateSlider();
          }
        };
      }

      // Touch & Swipe Support for Mobile & Touchscreens
      let touchStartX = 0;
      let touchEndX = 0;
      const viewport = document.getElementById('carousel-viewport');

      if (viewport) {
        viewport.addEventListener('touchstart', function(e) {
          touchStartX = e.changedTouches[0].screenX;
        }, { passive: true });

        viewport.addEventListener('touchend', function(e) {
          touchEndX = e.changedTouches[0].screenX;
          handleSwipe();
        }, { passive: true });
      }

      function handleSwipe() {
        const threshold = 40;
        if (touchEndX < touchStartX - threshold) {
          // Swipe Left -> Next Slide
          if (nextBtn && !nextBtn.disabled) nextBtn.click();
        } else if (touchEndX > touchStartX + threshold) {
          // Swipe Right -> Prev Slide
          if (prevBtn && !prevBtn.disabled) prevBtn.click();
        }
      }

      // Filter Button Listeners
      filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
          currentFilter = this.getAttribute('data-filter') || 'all';
          filterBtns.forEach(b => {
            b.classList.remove('bg-[#d4af37]', 'text-black', 'shadow-md', 'active');
            b.classList.add('bg-white/5', 'text-gray-300');
          });
          this.classList.remove('bg-white/5', 'text-gray-300');
          this.classList.add('bg-[#d4af37]', 'text-black', 'shadow-md', 'active');
          currentSlide = 0;
          updateSlider();
        });
      });

      // Sort Listener
      if (sortSelect) {
        sortSelect.addEventListener('change', function() {
          const order = this.value;
          allCardsArray.sort((a, b) => {
            if (order === 'helpful') {
              const aLikesMatch = a.innerHTML.match(/(?:&#128077;|👍)\s*<span[^>]*>(\d+)<\/span>/) || a.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
              const bLikesMatch = b.innerHTML.match(/(?:&#128077;|👍)\s*<span[^>]*>(\d+)<\/span>/) || b.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
              const aLikes = aLikesMatch ? parseInt(aLikesMatch[1]) : (parseInt(a.querySelector('.js-like-count')?.textContent) || 0);
              const bLikes = bLikesMatch ? parseInt(bLikesMatch[1]) : (parseInt(b.querySelector('.js-like-count')?.textContent) || 0);
              return bLikes - aLikes;
            } else {
              const da = parseInt(a.getAttribute('data-date') || '0');
              const db = parseInt(b.getAttribute('data-date') || '0');
              return order === 'newest' ? db - da : da - db;
            }
          });
          currentSlide = 0;
          updateSlider();
        });
      }

      // Expose globally for new submitted reviews
      window.addNewReviewToCarousel = function(cardDOM) {
        allCardsArray.unshift(cardDOM);
        currentSlide = 0;
        updateSlider();
      };

      // Initial run
      updateSlider();
    });
  </script>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove old pagination-wrapper
        content = re.sub(r'<!-- Luxury 8-Reviews-Per-Slide Dynamic Pagination Bar -->[\s\S]*?</div>\s*</div>', '', content)
        content = re.sub(r'<div id="pagination-wrapper"[\s\S]*?</div>\s*</div>', '', content)

        # Replace columns-1 grid container with carousel slider markup
        old_grid_start = '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">'
        if old_grid_start in content:
            # We keep the grid items inside grid for initial DOM parsing, wrapped by carousel section
            content = content.replace(old_grid_start, f'{carousel_html}\n\n      <div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6 hidden">')

        # Replace JS script engine
        script_start_idx = content.find("<script>\n    // BlackRoots")
        modal_start_idx = content.find("<!-- Customer Write Review Modal")
        if script_start_idx != -1 and modal_start_idx != -1:
            content = content[:script_start_idx] + carousel_script + "\n\n  " + content[modal_start_idx:]

        # Update Form Submit Handler to call window.addNewReviewToCarousel(card)
        content = content.replace('grid.insertBefore(card, grid.firstChild);', 'if (window.addNewReviewToCarousel) { window.addNewReviewToCarousel(card); } else if (grid) { grid.insertBefore(card, grid.firstChild); }')
        content = content.replace('if (window.refreshPagination) window.refreshPagination();', '')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CAROUSEL SLIDER ENGINE IMPLEMENTED IN: {fpath}")

