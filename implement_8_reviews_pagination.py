import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

pagination_html = """      <!-- Luxury 8-Reviews-Per-Slide Dynamic Pagination Bar -->
      <div id="pagination-wrapper" class="mt-10 pt-8 border-t border-white/10 flex flex-col items-center gap-4 text-center">
        <!-- Page Indicator / Counter badge -->
        <div class="text-xs font-bold text-gray-400 bg-white/5 border border-white/10 px-4 py-2 rounded-full shadow-md">
          Showing <span id="paginated-start-idx" class="text-amber-300 font-extrabold">1</span> &minus; <span id="paginated-end-idx" class="text-amber-300 font-extrabold">8</span> of <span id="total-reviews-count" class="text-white font-extrabold">33+</span> Verified Customer Reviews
        </div>

        <!-- Pagination Control Buttons -->
        <div id="pagination-controls" class="flex flex-wrap items-center justify-center gap-2">
          <!-- Dynamically populated page buttons: [Prev] [1] [2] [3] ... [Next] -->
        </div>
      </div>"""

target_grid_end = """      </div>
    </div>
  </section>

  <!-- Footer -->"""

replacement_grid_end = f"""{pagination_html}
      </div>
    </div>
  </section>

  <!-- Footer -->"""

old_scripts_block = """  <script>
    // Client-side Category Filter for Reviews
    document.addEventListener('DOMContentLoaded', function() {
      const filterBtns = document.querySelectorAll('.js-filter-btn');
      const reviewCards = document.querySelectorAll('[data-category]');

      filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
          filterBtns.forEach(b => {
            b.classList.remove('bg-[#d4af37]', 'text-black', 'shadow-md', 'active');
            b.classList.add('bg-white/5', 'text-gray-300');
          });

          this.classList.remove('bg-white/5', 'text-gray-300');
          this.classList.add('bg-[#d4af37]', 'text-black', 'shadow-md', 'active');

          const filter = this.getAttribute('data-filter');

          reviewCards.forEach(card => {
            const cat = card.getAttribute('data-category') || '';
            if (filter === 'all' || cat.includes(filter)) {
              card.style.display = card.classList.contains('grid') ? 'grid' : 'flex';
            } else {
              card.style.display = 'none';
            }
          });
        });
      });
    });
  </script>


  
  <script>
    // Filter functionality
    const filterBtns = document.querySelectorAll('.js-filter-btn');
    const grid = document.querySelector('.columns-1');
    const showingCount = document.querySelector('.js-[#showing-count]');
    const sortSelect = document.getElementById('reviews-sort');

    function getVisibleCards() {
      return Array.from(document.querySelectorAll('[data-category]'));
    }

    function applyFilter(filter) {
      let count = 0;
      getVisibleCards().forEach(card => {
        const cats = card.getAttribute('data-category') || '';
        if (filter === 'all' || cats.includes(filter)) {
          card.style.display = '';
          count++;
        } else {
          card.style.display = 'none';
        }
      });
      if (showingCount) showingCount.textContent = count + ' Reviews';
    }

    function applySort(order) {
      // Only sort non-pinned cards inside main grid container so Top 3 Hero Row remains untouched
      const cards = Array.from(grid.querySelectorAll('[data-category]'));
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
    }

    let currentFilter = 'all';

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        currentFilter = btn.getAttribute('data-filter');
        filterBtns.forEach(b => {
          b.classList.remove('bg-[#d4af37]', 'text-black');
          b.classList.add('bg-white/5', 'text-gray-300');
        });
        btn.classList.add('bg-[#d4af37]', 'text-black');
        btn.classList.remove('bg-white/5', 'text-gray-300');
        applyFilter(currentFilter);
        applySort(sortSelect ? sortSelect.value : 'helpful');
      });
    });

    if (sortSelect) {
      sortSelect.addEventListener('change', () => {
        applySort(sortSelect.value);
      });
    }

    applyFilter('all');
  </script>"""

new_unified_script = """  <script>
    // BlackRoots Unified Reviews 8-Per-Slide Pagination & Filter Engine
    document.addEventListener('DOMContentLoaded', function() {
      const REVIEWS_PER_PAGE = 8;
      let currentPage = 1;
      let currentFilter = 'all';

      const grid = document.querySelector('.columns-1');
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

      function updatePagination() {
        const gridCards = getGridCards();
        
        // Filter matching cards
        const matchingCards = gridCards.filter(card => {
          const cats = card.getAttribute('data-category') || '';
          return currentFilter === 'all' || cats.includes(currentFilter);
        });

        const totalItems = matchingCards.length;
        const totalPages = Math.ceil(totalItems / REVIEWS_PER_PAGE) || 1;

        if (currentPage > totalPages) currentPage = totalPages;
        if (currentPage < 1) currentPage = 1;

        const startIndex = (currentPage - 1) * REVIEWS_PER_PAGE;
        const endIndex = startIndex + REVIEWS_PER_PAGE;

        // Display only 8 cards for current slide page
        gridCards.forEach(card => {
          const cats = card.getAttribute('data-category') || '';
          const matches = currentFilter === 'all' || cats.includes(currentFilter);
          
          if (!matches) {
            card.style.display = 'none';
          } else {
            const cardIdx = matchingCards.indexOf(card);
            if (cardIdx >= startIndex && cardIdx < endIndex) {
              card.style.display = '';
            } else {
              card.style.display = 'none';
            }
          }
        });

        // Update counts
        const startNum = totalItems === 0 ? 0 : startIndex + 1;
        const endNum = Math.min(endIndex, totalItems);
        
        if (paginatedStartIdx) paginatedStartIdx.textContent = startNum;
        if (paginatedEndIdx) paginatedEndIdx.textContent = endNum;
        if (totalReviewsCount) totalReviewsCount.textContent = totalItems;
        if (showingCount) showingCount.textContent = totalItems + ' Reviews';

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
          prevBtn.className = `px-3.5 py-2 rounded-xl border text-xs font-bold transition-all ${currentPage === 1 ? 'opacity-40 pointer-events-none bg-white/5 border-white/10 text-gray-500' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37]'}`;
          prevBtn.innerHTML = '‹ Prev';
          prevBtn.addEventListener('click', function() {
            if (currentPage > 1) {
              currentPage--;
              updatePagination();
              scrollToGrid();
            }
          });
          paginationControls.appendChild(prevBtn);

          // Page Number Buttons
          for (let p = 1; p <= totalPages; p++) {
            const pBtn = document.createElement('button');
            pBtn.type = 'button';
            pBtn.className = `w-9 h-9 rounded-xl border font-bold text-xs transition-all ${p === currentPage ? 'bg-[#d4af37] text-black border-[#d4af37] shadow-lg scale-105' : 'bg-white/5 text-gray-300 border-white/10 hover:border-[#d4af37] hover:text-white'}`;
            pBtn.textContent = p;
            pBtn.addEventListener('click', function() {
              currentPage = p;
              updatePagination();
              scrollToGrid();
            });
            paginationControls.appendChild(pBtn);
          }

          // Next Button
          const nextBtn = document.createElement('button');
          nextBtn.type = 'button';
          nextBtn.className = `px-3.5 py-2 rounded-xl border text-xs font-bold transition-all ${currentPage === totalPages ? 'opacity-40 pointer-events-none bg-white/5 border-white/10 text-gray-500' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37]'}`;
          nextBtn.innerHTML = 'Next ›';
          nextBtn.addEventListener('click', function() {
            if (currentPage < totalPages) {
              currentPage++;
              updatePagination();
              scrollToGrid();
            }
          });
          paginationControls.appendChild(nextBtn);
        }
      }

      function scrollToGrid() {
        const heroRow = document.getElementById('hero-reviews-row') || grid;
        if (heroRow) {
          heroRow.scrollIntoView({ behavior: 'smooth', block: 'start' });
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

load_reviews_old = """      loadUserReviews();"""

load_reviews_new = """      loadUserReviews();
      if (window.refreshPagination) window.refreshPagination();"""

form_submit_end_old = """          showToast(name);
          closeModal();
          reviewForm.reset();"""

form_submit_end_new = """          showToast(name);
          closeModal();
          reviewForm.reset();
          if (window.refreshPagination) window.refreshPagination();"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if target_grid_end in content:
            content = content.replace(target_grid_end, replacement_grid_end)

        # Replace script blocks using regex or string match
        if "Client-side Category Filter for Reviews" in content:
            # cut out old script blocks up to modal
            modal_start_idx = content.find("<!-- Customer Write Review Modal")
            client_filter_idx = content.find("<script>\n    // Client-side Category Filter for Reviews")
            if client_filter_idx != -1 and modal_start_idx != -1:
                content = content[:client_filter_idx] + new_unified_script + "\n\n  " + content[modal_start_idx:]

        content = content.replace(load_reviews_old, load_reviews_new)
        content = content.replace(form_submit_end_old, form_submit_end_new)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"PAGINATION IMPLEMENTED SUCCESSFULLY IN: {fpath}")

