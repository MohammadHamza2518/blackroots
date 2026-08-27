import os

review_files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

sunita_old = """                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-xs flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="Sunita Verma">
                  SV
                </div>"""

sunita_new = """                <div class="w-10 h-10 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden border border-white/20" title="Sunita Verma">
                  <img src="./assets/reviews/sunita-verma-dp.jpg" alt="Sunita Verma" class="w-full h-full rounded-full object-cover object-top">
                </div>"""

alok_old = """                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-xs flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="Alok Mishra">
                  AM
                </div>"""

alok_new = """                <div class="w-10 h-10 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden border border-white/20" title="Alok Mishra">
                  <img src="./assets/reviews/alok-mishra-dp.jpg" alt="Alok Mishra" class="w-full h-full rounded-full object-cover object-top">
                </div>"""

anita_old = """                <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-xs flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="Anita Patel">
                  AP
                </div>"""

anita_new = """                <div class="w-10 h-10 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden border border-white/20" title="Anita Patel">
                  <img src="./assets/reviews/anita-patel-dp.jpg" alt="Anita Patel" class="w-full h-full rounded-full object-cover object-top">
                </div>"""

for fpath in review_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(sunita_old, sunita_new)
        content = content.replace(alok_old, alok_new)
        content = content.replace(anita_old, anita_new)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED REVIEWS DP IN: {fpath}")

# Product files update
product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

prod_sunita_old = """          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Sunita Verma</h3>
              <span class="text-[11px] text-gray-400">Kanpur, UP &bull; Verified Buyer</span>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>"""

prod_sunita_new = """          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-md shrink-0 overflow-hidden border border-white/20">
                <img src="./assets/reviews/sunita-verma-dp.jpg" alt="Sunita Verma" class="w-full h-full rounded-full object-cover object-top">
              </div>
              <div>
                <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Sunita Verma</h3>
                <span class="text-[11px] text-gray-400 block">Kanpur, UP &bull; Verified Buyer</span>
              </div>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>"""

prod_alok_old = """          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Alok Mishra</h3>
              <span class="text-[11px] text-gray-400">Delhi NCR &bull; Verified Buyer</span>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>"""

prod_alok_new = """          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-md shrink-0 overflow-hidden border border-white/20">
                <img src="./assets/reviews/alok-mishra-dp.jpg" alt="Alok Mishra" class="w-full h-full rounded-full object-cover object-top">
              </div>
              <div>
                <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Alok Mishra</h3>
                <span class="text-[11px] text-gray-400 block">Delhi NCR &bull; Verified Buyer</span>
              </div>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>"""

prod_anita_old = """          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Anita Patel</h3>
              <span class="text-[11px] text-gray-400">Ahmedabad, Gujarat &bull; Verified Buyer</span>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>"""

prod_anita_new = """          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-md shrink-0 overflow-hidden border border-white/20">
                <img src="./assets/reviews/anita-patel-dp.jpg" alt="Anita Patel" class="w-full h-full rounded-full object-cover object-top">
              </div>
              <div>
                <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Anita Patel</h3>
                <span class="text-[11px] text-gray-400 block">Ahmedabad, Gujarat &bull; Verified Buyer</span>
              </div>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(prod_sunita_old, prod_sunita_new)
        content = content.replace(prod_alok_old, prod_alok_new)
        content = content.replace(prod_anita_old, prod_anita_new)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED PRODUCT DP IN: {fpath}")

