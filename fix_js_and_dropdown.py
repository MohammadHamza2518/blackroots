import shutil
import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update the Select HTML
new_select = r'''<select id="reviews-sort" class="bg-[#1a1b20] border border-[#d4af37]/30 text-amber-50 text-xs font-bold rounded-full px-4 py-2 focus:outline-none focus:ring-1 focus:ring-[#d4af37] cursor-pointer hover:bg-[#d4af37]/10 transition-colors shadow-lg">
            <option value="helpful" class="font-bold bg-[#1a1b20] text-amber-50">&#128293; Top Helpful</option>
            <option value="newest" class="font-bold bg-[#1a1b20] text-amber-50">&#10024; Newest First</option>
            <option value="oldest" class="font-bold bg-[#1a1b20] text-amber-50">&#8986; Oldest First</option>
          </select>'''

c = re.sub(r'<select id="reviews-sort"[\s\S]*?</select>', lambda _: new_select, c)

# 2. Update the JavaScript
old_js_pattern = r'<script>\s*// Filter functionality[\s\S]*?</script>'

new_js = r'''<script>
    // Filter functionality
    const filterBtns = document.querySelectorAll('.js-filter-btn');
    const grid = document.querySelector('.grid.grid-cols-1.md\\:grid-cols-2') || document.querySelector('.grid');
    const showingCount = document.querySelector('.js-showing-count');
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
      const cards = getVisibleCards();
      const sorted = cards.sort((a, b) => {
        if (order === 'helpful') {
           const aLikesMatch = a.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
           const bLikesMatch = b.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
           const aLikes = aLikesMatch ? parseInt(aLikesMatch[1]) : 0;
           const bLikes = bLikesMatch ? parseInt(bLikesMatch[1]) : 0;
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
  </script>'''

c = re.sub(old_js_pattern, lambda _: new_js, c)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Dropdown and JS fixed!")
