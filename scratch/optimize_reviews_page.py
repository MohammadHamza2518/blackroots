import os
import re

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

clean_filter_bar = """      <!-- Filter Controls & Category Selection Bar (Mobile Optimized & Touch Friendly) -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-4 rounded-2xl bg-white/5 border border-white/10 mb-8 max-w-5xl mx-auto">
        <!-- Horizontal Scrollable Filter Strip -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar py-1 scroll-smooth">
          <button type="button" class="js-filter-btn shrink-0 px-4 py-2 rounded-xl bg-[#d4af37] text-black font-bold text-xs shadow-md transition-all active" data-filter="all">
            🌟 All Reviews (1,280+)
          </button>
          <button type="button" class="js-filter-btn shrink-0 px-4 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 font-bold text-xs transition-all" data-filter="photo">
            📸 With Photos (420+)
          </button>
          <button type="button" class="js-filter-btn shrink-0 px-4 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-amber-300 font-bold text-xs transition-all" data-filter="men">
            👨 Men's Scalp (540+)
          </button>
          <button type="button" class="js-filter-btn shrink-0 px-4 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-pink-300 font-bold text-xs transition-all" data-filter="women">
            👩 Women's Hair (740+)
          </button>
        </div>

        <!-- Sort Dropdown -->
        <div class="flex items-center justify-between sm:justify-end gap-3 pt-2 sm:pt-0 border-t sm:border-t-0 border-white/10">
          <div class="flex items-center gap-2">
            <span class="text-xs text-gray-400 font-medium whitespace-nowrap">Sort by:</span>
            <select id="reviews-sort" class="bg-[#1a1b20] border border-[#d4af37]/30 text-amber-50 text-xs font-bold rounded-xl px-3 py-1.5 focus:outline-none focus:ring-1 focus:ring-[#d4af37] cursor-pointer hover:bg-[#d4af37]/10 transition-colors shadow-lg">
              <option value="helpful" class="font-bold bg-[#1a1b20] text-amber-50">🔥 Top Helpful</option>
              <option value="newest" class="font-bold bg-[#1a1b20] text-amber-50">✨ Newest First</option>
              <option value="oldest" class="font-bold bg-[#1a1b20] text-amber-50">⏱️ Oldest First</option>
            </select>
          </div>
          <div class="text-xs text-gray-400 font-medium whitespace-nowrap">
            Showing <strong class="js-showing-count text-white font-bold">22 Reviews</strong>
          </div>
        </div>
      </div>"""

toast_replacement = """  <!-- Dynamic Toast Notification Container -->
  <div id="review-toast" class="fixed top-6 right-6 z-50 transform translate-y-[-100px] opacity-0 pointer-events-none transition-all duration-500 max-w-sm w-full bg-[#12151c] border-2 border-[#d4af37] shadow-2xl rounded-2xl p-4 flex items-center gap-3">
    <div class="w-10 h-10 rounded-full bg-[#d4af37] text-black text-xl flex items-center justify-center font-bold shrink-0">🎉</div>
    <div>
      <h4 id="toast-title" class="font-bold text-xs text-amber-300 uppercase tracking-wide">Review Published!</h4>
      <p id="toast-msg" class="text-xs text-gray-200">Your review has been added live to the customer ratings grid.</p>
    </div>
  </div>"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Replace Filter Bar
    pattern_filter = r'<!-- Filter Controls & Category Selection Bar.*?<\/section>'
    # Match the filter div up to </section>
    new_content = re.sub(
        r'<!-- Filter Controls & Category Selection Bar.*?<div class="text-xs text-gray-400 font-medium">\s*Showing <strong class="js-showing-count">22 Reviews<\/strong>\s*<\/div>\s*<\/div>',
        clean_filter_bar,
        new_content,
        flags=re.DOTALL
    )

    # 2. Fix Toast
    new_content = re.sub(
        r'<div id="review-toast".*?<\/div>\s*<\/div>',
        toast_replacement,
        new_content,
        flags=re.DOTALL
    )

    # 3. Ensure script tag is present
    if 'src="./assets/theme.js"' not in new_content and 'src="assets/theme.js"' not in new_content:
        new_content = new_content.replace('</body>', '  <script src="./assets/theme.js"></script>\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Optimized {fpath}")

