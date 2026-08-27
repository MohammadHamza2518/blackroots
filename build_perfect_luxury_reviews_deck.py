import os, re

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

deck_html = """      <!-- Real Customer Reviews Deck Section Header -->
      <div class="mt-12 mb-8 text-center space-y-2">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-amber-400/10 border border-amber-400/30 text-amber-300 text-[11px] font-bold uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-[#d4af37] animate-pulse"></span>
          Verified Customer Experiences Deck
        </div>
        <h3 class="font-serif text-2xl sm:text-3xl font-bold text-white">
          Real Results From Genuine Shoppers
        </h3>
        <p class="text-xs text-gray-400 font-light max-w-xl mx-auto">
          Explore genuine BlackRoots shower wash reviews from verified Indian buyers.
        </p>
      </div>

      <!-- Symmetrical 3-Column Customer Reviews Grid Deck -->
      <div id="customer-reviews-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- 6 Symmetrical Customer Review Cards rendered per slide deck -->
      </div>

      <!-- Startup-Grade Luxury Slide Controls Container -->
      <div id="deck-pagination-bar" class="mt-10 p-4 sm:p-5 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-4">
        
        <!-- Left: Slide Info & Status -->
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-full bg-[#d4af37]/20 border border-[#d4af37]/40 text-[#d4af37] font-extrabold text-xs flex items-center justify-center">
            ❖
          </div>
          <div>
            <div id="deck-slide-badge" class="text-xs font-bold text-amber-300">
              Slide 1 of 5
            </div>
            <div id="deck-showing-text" class="text-[10px] text-gray-400">
              Showing 6 Verified Reviews per slide deck
            </div>
          </div>
        </div>

        <!-- Center: Interactive Gold Slide Dots -->
        <div id="deck-dots-container" class="flex items-center justify-center gap-2">
          <!-- Animated Gold Dots -->
        </div>

        <!-- Right: Slide Prev / Next Buttons -->
        <div class="flex items-center gap-2.5">
          <button type="button" id="deck-prev-btn" class="px-4 py-2.5 rounded-xl bg-white/5 border border-white/15 text-white hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37] text-xs font-extrabold flex items-center gap-1.5 shadow-lg transition-all transform active:scale-95 cursor-pointer disabled:opacity-30 disabled:pointer-events-none">
            ‹ Previous Slide
          </button>
          <button type="button" id="deck-next-btn" class="px-4 py-2.5 rounded-xl bg-[#d4af37] text-black border border-[#d4af37] hover:bg-amber-300 text-xs font-extrabold flex items-center gap-1.5 shadow-lg transition-all transform active:scale-95 cursor-pointer disabled:opacity-30 disabled:pointer-events-none">
            Next Slide ›
          </button>
        </div>

      </div>"""

deck_script = """  <script>
    // BlackRoots Perfect Startup-Grade Luxury Reviews Deck Engine
    document.addEventListener('DOMContentLoaded', function() {
      const CARDS_PER_SLIDE = 6;
      let currentSlide = 0;
      let currentFilter = 'all';

      const customerGrid = document.getElementById('customer-reviews-grid');
      const staticGridSource = document.querySelector('.columns-1');
      const prevBtn = document.getElementById('deck-prev-btn');
      const nextBtn = document.getElementById('deck-next-btn');
      const slideBadge = document.getElementById('deck-slide-badge');
      const showingText = document.getElementById('deck-showing-text');
      const dotsContainer = document.getElementById('deck-dots-container');
      const filterBtns = document.querySelectorAll('.js-filter-btn');
      const showingCount = document.querySelector('.js-showing-count');
      const sortSelect = document.getElementById('reviews-sort');

      // Preserve all initial static review cards from HTML source grid
      let allCardsArray = [];
      if (staticGridSource) {
        allCardsArray = Array.from(staticGridSource.querySelectorAll('[data-category]'));
      }

      function scrollToDeckTop() {
        const header = document.getElementById('customer-reviews-grid') || customerGrid;
        if (header) {
          const yOffset = -110;
          const y = header.getBoundingClientRect().top + window.pageYOffset + yOffset;
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      }

      function updateDeck() {
        if (!customerGrid) return;

        // Filter cards
        const matchingCards = allCardsArray.filter(card => {
          const cats = card.getAttribute('data-category') || '';
          return currentFilter === 'all' || cats.includes(currentFilter);
        });

        const totalItems = matchingCards.length;
        const totalSlides = Math.ceil(totalItems / CARDS_PER_SLIDE) || 1;

        if (currentSlide >= totalSlides) currentSlide = totalSlides - 1;
        if (currentSlide < 0) currentSlide = 0;

        const startIdx = currentSlide * CARDS_PER_SLIDE;
        const endIdx = startIdx + CARDS_PER_SLIDE;
        const visibleCardsForSlide = matchingCards.slice(startIdx, endIdx);

        // Render Exactly 6 Cards into 3-Column Symmetrical Grid
        customerGrid.innerHTML = '';
        visibleCardsForSlide.forEach(card => {
          // Normalize card styles for 3-column grid layout
          card.className = "p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col justify-between h-full transition-all duration-300 hover:border-[#d4af37]";
          card.style.cssText = "display: flex !important; width: 100% !important; margin-bottom: 0 !important;";
          customerGrid.appendChild(card);
        });

        // Update Slide Badge & Status Text
        if (slideBadge) slideBadge.textContent = `Slide ${currentSlide + 1} of ${totalSlides}`;
        if (showingText) showingText.textContent = `Showing ${visibleCardsForSlide.length} of ${totalItems} Verified Reviews`;
        if (showingCount) showingCount.textContent = `${totalItems} Reviews`;

        // Update Prev / Next Buttons State
        if (prevBtn) prevBtn.disabled = (currentSlide === 0);
        if (nextBtn) nextBtn.disabled = (currentSlide >= totalSlides - 1);

        // Render Interactive Dots
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
                updateDeck();
                scrollToDeckTop();
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
            updateDeck();
            scrollToDeckTop();
          }
        };
      }

      if (nextBtn) {
        nextBtn.onclick = function(e) {
          e.preventDefault();
          const totalSlides = Math.ceil(allCardsArray.filter(c => currentFilter === 'all' || (c.getAttribute('data-category')||'').includes(currentFilter)).length / CARDS_PER_SLIDE);
          if (currentSlide < totalSlides - 1) {
            currentSlide++;
            updateDeck();
            scrollToDeckTop();
          }
        };
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
          updateDeck();
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
          updateDeck();
        });
      }

      // Expose globally for new submitted reviews from modal
      window.addNewReviewToDeck = function(cardDOM) {
        allCardsArray.unshift(cardDOM);
        currentSlide = 0;
        updateDeck();
        scrollToDeckTop();
      };

      // Initial run
      updateDeck();
    });
  </script>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean old carousel section or columns-1 grid
        content = re.sub(r'<!-- Startup-Grade Luxury Customer Reviews Carousel Slider Deck -->[\s\S]*?</div>\s*</div>', '', content)
        content = re.sub(r'<div id="reviews-carousel-section"[\s\S]*?</div>\s*</div>', '', content)

        # Replace columns-1 container with new deck HTML
        old_grid_pattern = '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6 hidden">'
        if old_grid_pattern in content:
            content = content.replace(old_grid_pattern, f'{deck_html}\n\n      <div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6 hidden">')
        elif '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">' in content:
            content = content.replace('<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">', f'{deck_html}\n\n      <div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6 hidden">')

        # Replace script
        script_start_idx = content.find("<script>\n    // BlackRoots")
        modal_start_idx = content.find("<!-- Customer Write Review Modal")
        if script_start_idx != -1 and modal_start_idx != -1:
            content = content[:script_start_idx] + deck_script + "\n\n  " + content[modal_start_idx:]

        # Update Form Submit Handler
        content = content.replace('window.addNewReviewToCarousel', 'window.addNewReviewToDeck')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"PERFECT LUXURY REVIEWS DECK IMPLEMENTED IN: {fpath}")

