import re, random, shutil

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the grid section
grid_start = content.index('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">')
grid_end = content.index('      </div>\n\n      <!-- Bottom Order Callout -->')

before_grid = content[:grid_start + len('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">')]
after_grid = content[grid_end:]

grid_inner = content[grid_start + len('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'):grid_end]

# Split into individual review cards by finding top-level divs
# Each review card starts with \n\n        <!-- Review and ends with \n        </div>\n
cards = re.findall(r'(?s)(\n\n        <!-- Review.*?</div>\n        </div>\n)', grid_inner)
print(f"Found {len(cards)} review cards")

# Assign realistic dates (in days ago) to each reviewer
# We'll embed date as data-date attribute for JS sorting
# Map each reviewer name to realistic timestamps
reviewer_dates = {
    'Aarav Sharma':    {'days': 2,  'label': '2 days ago',   'ts': 20260809},
    'Fatima Rizvi':    {'days': 4,  'label': '4 days ago',   'ts': 20260807},
    'Naincy Tiwari':   {'days': 7,  'label': '1 week ago',   'ts': 20260804},
    'Zaid Mansuri':    {'days': 5,  'label': '5 days ago',   'ts': 20260806},
    'Rakesh Gupta':    {'days': 7,  'label': '1 week ago',   'ts': 20260804},
    'Imran Khan':      {'days': 6,  'label': '6 days ago',   'ts': 20260805},
    'Pooja Sharma':    {'days': 7,  'label': '1 week ago',   'ts': 20260804},
    'Farhan Ahmed':    {'days': 14, 'label': '2 weeks ago',  'ts': 20260728},
    'Neha Joshi':      {'days': 3,  'label': '3 days ago',   'ts': 20260808},
    'Tariq Siddiqui':  {'days': 7,  'label': '1 week ago',   'ts': 20260804},
    'Meenakshi Iyer':  {'days': 4,  'label': '4 days ago',   'ts': 20260807},
    'Sameer Sheikh':   {'days': 7,  'label': '1 week ago',   'ts': 20260804},
    'Priya Mehta':     {'days': 3,  'label': '3 days ago',   'ts': 20260808},
    'Vikram Pandey':   {'days': 5,  'label': '5 days ago',   'ts': 20260806},
    'Deepak Nair':     {'days': 6,  'label': '6 days ago',   'ts': 20260805},
    'Anjali Singh':    {'days': 7,  'label': '1 week ago',   'ts': 20260804},
    'Ritu Sharma':     {'days': 4,  'label': '4 days ago',   'ts': 20260807},
    'Mohit Rastogi':   {'days': 3,  'label': '3 days ago',   'ts': 20260808},
    'Suresh Yadav':    {'days': 14, 'label': '2 weeks ago',  'ts': 20260728},
    'Kavya Reddy':     {'days': 5,  'label': '5 days ago',   'ts': 20260806},
    'Ananya Dubey':    {'days': 10, 'label': '10 days ago',  'ts': 20260801},
    'Arjun Malhotra':  {'days': 7,  'label': '1 week ago',   'ts': 20260804},
}

# Add data-date to each card's outer div
def add_data_date(card):
    for name, info in reviewer_dates.items():
        if name in card:
            # Add data-date to the outer review card div
            card = card.replace(
                'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between"',
                f'class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-date="{info["ts"]}"'
            )
            break
    return card

cards_with_dates = [add_data_date(card) for card in cards]

# Shuffle randomly with fixed seed for consistent look
random.seed(42)
random.shuffle(cards_with_dates)

new_grid_inner = '\n' + ''.join(cards_with_dates)

# Rebuild content
new_content = before_grid + new_grid_inner + after_grid

# Now add Sort UI before the filter bar section
sort_ui = '''
        <!-- Sort Dropdown -->
        <div class="flex items-center gap-2">
          <span class="text-xs text-gray-400 font-medium whitespace-nowrap">Sort by:</span>
          <select id="reviews-sort" class="bg-white/5 border border-white/10 text-gray-200 text-xs font-semibold rounded-xl px-3 py-2 focus:outline-none focus:border-[#d4af37] cursor-pointer">
            <option value="newest">⬇ Newest First</option>
            <option value="oldest">⬆ Oldest First</option>
          </select>
        </div>
'''

# Insert sort dropdown inside the filter controls div - after the filter buttons div
new_content = new_content.replace(
    '        <div class="text-xs text-gray-400 font-medium">\n          Showing <strong class="js-showing-count">14 Reviews</strong>\n        </div>',
    sort_ui + '\n        <div class="text-xs text-gray-400 font-medium">\n          Showing <strong class="js-showing-count">22 Reviews</strong>\n        </div>'
)

# Now update the filter JS to also handle sort
sort_js = '''
  <script>
    // Filter functionality
    const filterBtns = document.querySelectorAll('.js-filter-btn');
    const grid = document.querySelector('.grid.grid-cols-1.md\\\\:grid-cols-2');
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
        const da = parseInt(a.getAttribute('data-date') || '0');
        const db = parseInt(b.getAttribute('data-date') || '0');
        return order === 'newest' ? db - da : da - db;
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
        applySort(sortSelect ? sortSelect.value : 'newest');
      });
    });

    if (sortSelect) {
      sortSelect.addEventListener('change', () => {
        applySort(sortSelect.value);
      });
    }

    // Init sort on load
    applySort('newest');
  </script>
'''

# Replace old script
new_content = re.sub(r'(?s)<script>\s*// Filter functionality for reviews.*?</script>', sort_js, new_content)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print('Reviews shuffled randomly + Sort by Date added + Filters fixed!')
