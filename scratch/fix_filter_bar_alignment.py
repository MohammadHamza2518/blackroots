import os
import re

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

clean_filter_bar_v2 = """      <!-- Filter Controls & Category Selection Bar (Mobile Optimized & 100% Contained) -->
      <div class="p-3.5 sm:p-4 rounded-2xl bg-[#12151c]/90 border border-white/10 mb-8 max-w-5xl mx-auto space-y-3 shadow-xl">
        <!-- Horizontal Scrollable Filter Strip -->
        <div class="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1 scroll-smooth">
          <button type="button" class="js-filter-btn shrink-0 px-3.5 py-2 rounded-xl bg-[#d4af37] text-black font-bold text-xs shadow-md transition-all active cursor-pointer" data-filter="all">
            🌟 All Reviews (1,280+)
          </button>
          <button type="button" class="js-filter-btn shrink-0 px-3.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 font-bold text-xs transition-all cursor-pointer" data-filter="photo">
            📸 Photos (420+)
          </button>
          <button type="button" class="js-filter-btn shrink-0 px-3.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-amber-300 font-bold text-xs transition-all cursor-pointer" data-filter="men">
            👨 Men (540+)
          </button>
          <button type="button" class="js-filter-btn shrink-0 px-3.5 py-2 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-pink-300 font-bold text-xs transition-all cursor-pointer" data-filter="women">
            👩 Women (740+)
          </button>
        </div>

        <!-- Sort & Count Clean Row -->
        <div class="flex items-center justify-between gap-2 pt-2.5 border-t border-white/10 text-xs">
          <div class="flex items-center gap-1.5 min-w-0">
            <span class="text-[11px] text-gray-400 font-medium shrink-0">Sort:</span>
            <select id="reviews-sort" class="bg-[#1a1b20] border border-[#d4af37]/40 text-amber-300 text-[11px] font-bold rounded-lg px-2.5 py-1 focus:outline-none focus:border-[#d4af37] cursor-pointer shadow-sm">
              <option value="helpful">🔥 Top Helpful</option>
              <option value="newest">✨ Newest First</option>
              <option value="oldest">⏱️ Oldest First</option>
            </select>
          </div>
          
          <div class="shrink-0 bg-white/5 border border-white/10 px-2.5 py-1 rounded-lg text-[11px] text-gray-300">
            <strong class="js-showing-count text-amber-400 font-bold">22</strong> Reviews
          </div>
        </div>
      </div>"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the filter bar section
    pattern = r'<!-- Filter Controls & Category Selection Bar.*?<\/div>\s*<\/div>\s*<\/div>'
    new_content = re.sub(pattern, clean_filter_bar_v2, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated filter bar in {fpath}")
