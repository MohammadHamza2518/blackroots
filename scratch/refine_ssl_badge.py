import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html"),
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html")
]

refined_subhead = """              <!-- Security Subhead -->
              <div class="flex items-center justify-between text-[10px] font-bold uppercase tracking-wider px-1 gap-2">
                <span class="flex items-center gap-1.5 text-gray-300 truncate">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0 animate-pulse"></span>
                  <span>100% Secure Checkout</span>
                </span>
                <span class="text-amber-300/90 font-semibold flex items-center gap-1 shrink-0 bg-white/5 px-2 py-0.5 rounded-md border border-white/10">
                  🔒 256-Bit SSL
                </span>
              </div>"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the security subhead
    pattern = r'<!-- Security Subhead -->.*?<div class="flex items-center justify-between text-\[10px\].*?<\/div>\s*<\/div>'
    
    new_content = re.sub(
        r'<!-- Security Subhead -->\s*<div class="flex items-center justify-between text-\[10px\].*?🔒 256-Bit SSL\s*<\/span>\s*<\/div>',
        refined_subhead,
        content,
        flags=re.DOTALL
    )

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Refined security subhead in", fpath)

