import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

target_old = """          <div class="relative w-full aspect-square sm:aspect-[4/3] rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center group bg-[#0d0e12]">
            <img id="ProductMainImage" src="./assets/blackroots-bathroom-counter.jpg" alt="BlackRoots Product Showcase" class="w-full h-full object-cover transition-all duration-300 group-hover:scale-105">"""

target_new = """          <div class="relative w-full aspect-square rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center group bg-[#0a0c10]">
            <img id="ProductMainImage" src="./assets/blackroots-bathroom-counter.jpg" alt="BlackRoots Product Showcase" class="w-full h-full object-contain p-2 sm:p-3 transition-all duration-300 group-hover:scale-105">"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if target_old in content:
            content = content.replace(target_old, target_new)
        else:
            # Flexible replace
            idx = content.find('id="ProductMainImage"')
            if idx != -1:
                box_start = content.rfind('<div class="relative w-full', 0, idx)
                img_end = content.find('>', idx)
                if box_start != -1 and img_end != -1:
                    content = content[:box_start] + target_new + content[img_end+1:]

        content = content.replace("</div> </div>\n\n        <div class=\"lg:col-span-5", "</div>\n        </div>\n\n        <div class=\"lg:col-span-5")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED PERFECT ZERO CROP VIEWPORT TO: {fpath}")

