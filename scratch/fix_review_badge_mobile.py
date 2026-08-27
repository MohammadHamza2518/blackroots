import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "reviews.html"),
    os.path.join(root_dir, "demo_lab", "reviews.html"),
    os.path.join(root_dir, "preview", "reviews.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Sort & Count Clean Row with mobile-first balanced spacing
    old_row_pattern = r'<!-- Sort & Count Clean Row -->[\s\S]*?<\/div>\s*<\/div>\s*<\/div>'
    
    new_row = """<!-- Sort & Count Clean Row (100% Mobile Contained & Balanced) -->
        <div class="flex items-center justify-between gap-2 pt-2.5 border-t border-white/10 text-xs w-full">
          <div class="flex items-center gap-1 sm:gap-1.5 shrink-0">
            <span class="text-[10px] sm:text-[11px] text-gray-400 font-medium shrink-0">Sort:</span>
            <select id="reviews-sort" class="bg-[#1a1b20] border border-[#d4af37]/40 text-amber-300 text-[10px] sm:text-[11px] font-bold rounded-lg px-2 sm:px-2.5 py-1 focus:outline-none focus:border-[#d4af37] cursor-pointer shadow-sm">
              <option value="helpful">🔥 Top Helpful</option>
              <option value="newest">✨ Newest First</option>
              <option value="oldest">⏱️ Oldest First</option>
            </select>
          </div>
          
          <div class="shrink-0 bg-white/5 border border-white/10 px-2.5 sm:px-3 py-1 sm:py-1.5 rounded-xl text-[10px] sm:text-[11px] text-gray-300 shadow-sm flex items-center gap-1">
            <strong class="js-showing-count text-amber-400 font-black">1,280+</strong>
            <span class="hidden xs:inline sm:inline">Verified</span>
            <span>Reviews</span>
          </div>
        </div>
      </div>"""

    new_content = re.sub(r'<!-- Sort & Count Clean Row -->[\s\S]*?<\/div>\s*<\/div>', new_row, content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed responsive review sort & count badge in:", fpath)

