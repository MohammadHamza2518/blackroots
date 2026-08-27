import os
import re

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content

    # 1. Update dynamic deck card classes in JavaScript
    new_content = new_content.replace(
        'card.className = "p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col justify-between h-full transition-all duration-300 hover:border-[#d4af37]";',
        'card.className = "p-4 sm:p-6 rounded-2xl sm:rounded-3xl glass-panel-luxury border border-[#d4af37]/35 shadow-xl flex flex-col justify-between h-full transition-all duration-300 hover:border-[#d4af37] w-full box-border";'
    )
    
    new_content = new_content.replace(
        'card.style.cssText = "display: flex !important; width: 100% !important; margin-bottom: 0 !important;";',
        'card.style.cssText = "display: flex !important; width: 100% !important; max-width: 100% !important; margin-bottom: 0 !important; box-sizing: border-box !important;";'
    )

    # 2. Update static hero cards padding
    new_content = re.sub(
        r'class="p-5 sm:p-6 rounded-3xl glass-panel-luxury border-2 border-\[#d4af37\] shadow-xl flex flex-col justify-between relative overflow-hidden',
        r'class="p-4 sm:p-6 rounded-2xl sm:rounded-3xl glass-panel-luxury border border-[#d4af37]/40 shadow-xl flex flex-col justify-between relative overflow-hidden w-full box-border',
        new_content
    )

    # 3. Ensure section container has solid safe margins
    new_content = new_content.replace(
        '<section class="py-12 bg-[#0a0b0e]">',
        '<section class="py-10 sm:py-12 bg-[#0a0b0e] overflow-hidden">'
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Refined card margins in {fpath}")

