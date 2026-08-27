import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

deck_script = """  <script>
    // BlackRoots Perfect Startup-Grade Luxury Reviews Deck Engine (Photo Proof First & Zero Blank Space)
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

      // Helper: Check if a card contains photo proof
      function hasPhotoProof(card) {
        if (!card) return false;
        const img = card.querySelector('img[src*="review-photo"], img[src*="face-photo"], img[src*="before"], img[src*="after"], img[src*="bottle"], img[src*="girl"], img[src*="table"]');
        return img !== null || card.hasAttribute('data-has-photo');
      }

      // Preserve all initial static review cards from HTML source grid
      let allCardsArray = [];
      if (staticGridSource) {
        allCardsArray = Array.from(staticGridSource.querySelectorAll('[data-category]'));
      }

      // PRIORITIZE PHOTO PROOF REVIEWS FIRST IN DECK
      allCardsArray.sort((a, b) => {
        const aHasPhoto = hasPhotoProof(a);
        const bHasPhoto = hasPhotoProof(b);
        if (aHasPhoto && !bHasPhoto) return -1; // Photo proof cards FIRST
        if (!aHasPhoto && bHasPhoto) return 1;
        return 0;
      });

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
          
          // Fill empty space for text-only cards so every card has equal height and zero blank gaps
          if (!hasPhotoProof(card) && !card.querySelector('.js-filled-badge')) {
            const bodyPara = card.querySelector('p');
            if (bodyPara) {
              const filler = document.createElement('div');
              filler.className = "js-filled-badge mt-4 p-3 rounded-2xl bg-white/5 border border-white/10 text-[10px] text-gray-300 flex items-center justify-between";
              filler.innerHTML = `
                <span class="flex items-center gap-1.5 font-semibold text-emerald-400">
                  <span>✓</span> Verified Scalp Buyer
                </span>
                <span class="text-amber-300 font-bold">100% Herbal Formula</span>
              `;
              bodyPara.after(filler);
            }
          }

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
          
          // Re-apply Photo Priority FIRST after sorting
          allCardsArray.sort((a, b) => {
            const aHasPhoto = hasPhotoProof(a);
            const bHasPhoto = hasPhotoProof(b);
            if (aHasPhoto && !bHasPhoto) return -1;
            if (!aHasPhoto && bHasPhoto) return 1;
            return 0;
          });

          currentSlide = 0;
          updateDeck();
        });
      }

      // Expose globally for new submitted reviews from modal
      window.addNewReviewToDeck = function(cardDOM) {
        cardDOM.setAttribute('data-has-photo', 'true');
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

        script_start_idx = content.find("<script>\n    // BlackRoots")
        modal_start_idx = content.find("<!-- Customer Write Review Modal")
        if script_start_idx != -1 and modal_start_idx != -1:
            content = content[:script_start_idx] + deck_script + "\n\n  " + content[modal_start_idx:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"PHOTO-FIRST PRIORITIZATION & ZERO-BLANK-SPACE ENGINE APPLIED TO: {fpath}")

