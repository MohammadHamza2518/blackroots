import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

strict_8_engine = """  <script>
    // BlackRoots Strict 8-Reviews-Per-Slide Engine (Hero + Grid = Exactly 8 Per Page)
    document.addEventListener('DOMContentLoaded', function() {
      const REVIEWS_PER_PAGE = 8;
      let currentPage = 1;
      let currentFilter = 'all';

      const grid = document.querySelector('.columns-1');
      const heroRow = document.getElementById('hero-reviews-row');
      const filterBtns = document.querySelectorAll('.js-filter-btn');
      const showingCount = document.querySelector('.js-showing-count');
      const sortSelect = document.getElementById('reviews-sort');
      const paginationControls = document.getElementById('pagination-controls');
      const paginatedStartIdx = document.getElementById('paginated-start-idx');
      const paginatedEndIdx = document.getElementById('paginated-end-idx');
      const totalReviewsCount = document.getElementById('total-reviews-count');

      function getGridCards() {
        if (!grid) return [];
        return Array.from(grid.querySelectorAll('[data-category]'));
      }

      function getHeroCards() {
        if (!heroRow) return [];
        return Array.from(heroRow.querySelectorAll('[data-category]'));
      }

      function scrollToReviews() {
        const target = heroRow || grid;
        if (target) {
          const yOffset = -100;
          const y = target.getBoundingClientRect().top + window.pageYOffset + yOffset;
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      }

      function updatePagination() {
        const heroCards = getHeroCards();
        const gridCards = getGridCards();

        // 1. Filter Hero Cards
        const matchingHeroCards = heroCards.filter(card => {
          const cats = card.getAttribute('data-category') || '';
          return currentFilter === 'all' || cats.includes(currentFilter);
        });

        # 2. Filter Grid Cards
        const matchingGridCards = gridCards.filter(card => {
          const cats = card.getAttribute('data-category') || '';
          return currentFilter === 'all' || cats.includes(currentFilter);
        });

        const totalHeroCount = matchingHeroCards.length;
        const totalGridCount = matchingGridCards.length;
        const grandTotal = totalHeroCount + totalGridCount;

        // Capacity for grid cards on Page 1 so total on Page 1 = 8
        const page1GridCapacity = Math.max(0, REVIEWS_PER_PAGE - totalHeroCount);

        // Calculate Total Pages
        let totalPages = 1;
        if (totalGridCount > page1GridCapacity) {
          totalPages = 1 + Math.ceil((totalGridCount - page1GridCapacity) / REVIEWS_PER_PAGE);
        }

        if (currentPage > totalPages) currentPage = totalPages;
        if (currentPage < 1) currentPage = 1;

        // Display/Hide Hero Cards (Shown on Page 1 if matching filter, hidden on Page 2+)
        heroCards.forEach(card => {
          const cats = card.getAttribute('data-category') || '';
          const matches = currentFilter === 'all' || cats.includes(currentFilter);
          if (currentPage === 1 && matches) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });

        // Hide/Show Hero Row Container if all cards inside it are hidden
        if (heroRow) {
          const visibleHeroes = heroCards.filter(c => c.style.display !== 'none');
          heroRow.style.display = (currentPage === 1 && visibleHeroes.length > 0) ? 'grid' : 'none';
        }

        // Determine range of grid cards for current page
        let gridStart = 0;
        let gridEnd = 0;

        if (currentPage === 1) {
          gridStart = 0;
          gridEnd = page1GridCapacity;
        } else {
          gridStart = page1GridCapacity + (currentPage - 2) * REVIEWS_PER_PAGE;
          gridEnd = gridStart + REVIEWS_PER_PAGE;
        }

        // Display/Hide Grid Cards
        gridCards.forEach(card => {
          const cats = card.getAttribute('data-category') || '';
          const matches = currentFilter === 'all' || cats.includes(currentFilter);
          if (!matches) {
            card.style.display = 'none';
          } else {
            const idx = matchingGridCards.indexOf(card);
            if (idx >= gridStart && idx < gridEnd) {
              card.style.display = 'inline-block';
            } else {
              card.style.display = 'none';
            }
          }
        });

        // Update counts display
        let currentScreenCount = 0;
        if (currentPage === 1) {
          currentScreenCount = Math.min(grandTotal, REVIEWS_PER_PAGE);
          if (paginatedStartIdx) paginatedStartIdx.textContent = grandTotal === 0 ? '0' : '1';
          if (paginatedEndIdx) paginatedEndIdx.textContent = currentScreenCount;
        } else {
          const startNum = REVIEWS_PER_PAGE + (currentPage - 2) * REVIEWS_PER_PAGE + 1;
          const endNum = Math.min(startNum + REVIEWS_PER_PAGE - 1, grandTotal);
          if (paginatedStartIdx) paginatedStartIdx.textContent = startNum;
          if (paginatedEndIdx) paginatedEndIdx.textContent = endNum;
        }

        if (totalReviewsCount) totalReviewsCount.textContent = grandTotal;
        if (showingCount) showingCount.textContent = grandTotal + ' Reviews';

        // Render Pagination Control Buttons
        if (paginationControls) {
          paginationControls.innerHTML = '';

          if (totalPages <= 1) {
            paginationControls.style.display = 'none';
            return;
          }
          paginationControls.style.display = 'flex';

          // Previous Button
          const prevBtn = document.createElement('button');
          prevBtn.type = 'button';
          prevBtn.className = `px-4 py-2 rounded-xl border text-xs font-bold transition-all cursor-pointer select-none ${currentPage === 1 ? 'opacity-40 pointer-events-none bg-white/5 border-white/10 text-gray-500' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37]'}`;
          prevBtn.innerHTML = '‹ Prev';
          prevBtn.onclick = function(e) {
            e.preventDefault();
            if (currentPage > 1) {
              currentPage--;
              updatePagination();
              scrollToReviews();
            }
          };
          paginationControls.appendChild(prevBtn);

          // Page Number Buttons
          for (let p = 1; p <= totalPages; p++) {
            const pBtn = document.createElement('button');
            pBtn.type = 'button';
            pBtn.className = `w-10 h-10 rounded-xl border font-bold text-xs transition-all cursor-pointer select-none ${p === currentPage ? 'bg-[#d4af37] text-black border-[#d4af37] shadow-lg scale-105' : 'bg-white/5 text-gray-300 border-white/10 hover:border-[#d4af37] hover:text-white'}`;
            pBtn.textContent = p;
            pBtn.onclick = function(e) {
              e.preventDefault();
              currentPage = p;
              updatePagination();
              scrollToReviews();
            };
            paginationControls.appendChild(pBtn);
          }

          // Next Button
          const nextBtn = document.createElement('button');
          nextBtn.type = 'button';
          nextBtn.className = `px-4 py-2 rounded-xl border text-xs font-bold transition-all cursor-pointer select-none ${currentPage === totalPages ? 'opacity-40 pointer-events-none bg-white/5 border-white/10 text-gray-500' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37]'}`;
          nextBtn.innerHTML = 'Next ›';
          nextBtn.onclick = function(e) {
            e.preventDefault();
            if (currentPage < totalPages) {
              currentPage++;
              updatePagination();
              scrollToReviews();
            }
          };
          paginationControls.appendChild(nextBtn);
        }
      }

      function applySort(order) {
        if (!grid) return;
        const cards = getGridCards();
        const sorted = cards.sort((a, b) => {
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
        sorted.forEach(card => grid.appendChild(card));
        updatePagination();
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
          currentPage = 1;
          applySort(sortSelect ? sortSelect.value : 'helpful');
        });
      });

      if (sortSelect) {
        sortSelect.addEventListener('change', function() {
          currentPage = 1;
          applySort(this.value);
        });
      }

      // Expose refreshPagination function for review form submit
      window.refreshPagination = function() {
        currentPage = 1;
        updatePagination();
      };

      // Initial run
      updatePagination();
    });
  </script>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        script_start_idx = content.find("<script>\n    // BlackRoots Unified Reviews")
        modal_start_idx = content.find("<!-- Customer Write Review Modal")
        if script_start_idx != -1 and modal_start_idx != -1:
            content = content[:script_start_idx] + strict_8_engine + "\n\n  " + content[modal_start_idx:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"STRICT 8 REVIEWS PER PAGE IMPLEMENTED IN: {fpath}")

