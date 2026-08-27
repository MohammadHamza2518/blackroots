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

    # 1. Fix the HTML badge in Sort & Count Clean Row
    new_content = re.sub(
        r'<div class="[^"]*shrink-0[^"]*bg-white/5[^"]*">\s*<strong class="js-showing-count[^"]*">.*?<\/strong>\s*Reviews\s*<\/div>',
        '''<div class="shrink-0 bg-white/5 border border-white/10 px-3 py-1.5 rounded-xl text-[11px] text-gray-300 shadow-sm flex items-center gap-1.5">
            <strong class="js-showing-count text-amber-400 font-extrabold">1,280+</strong>
            <span>Verified Reviews</span>
          </div>''',
        content
    )

    # 2. Fix JS updating showingCount
    new_content = re.sub(
        r"if\s*\(showingCount\)\s*showingCount\.textContent\s*=\s*visibleCards\s*\+\s*['\"] Reviews['\"];",
        "if (showingCount) showingCount.textContent = '1,280+';",
        new_content
    )
    new_content = re.sub(
        r"if\s*\(showingCount\)\s*showingCount\.textContent\s*=\s*totalCards\s*\+\s*['\"] Reviews['\"];",
        "if (showingCount) showingCount.textContent = '1,280+';",
        new_content
    )
    new_content = re.sub(
        r"if\s*\(showingCount\)\s*showingCount\.textContent\s*=\s*`\$\{totalItems\}\s*Reviews`;",
        "if (showingCount) showingCount.textContent = '1,280+';",
        new_content
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Fixed Review badge to '1,280+ Verified Reviews' in:", fpath)

