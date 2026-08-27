import os
import re

anita_card_html = """        <!-- Anita Patel Verified Customer Review Card (With Real Scalp Before & After Photos) -->
        <div id="anita-patel" class="p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/60 shadow-2xl flex flex-col break-inside-avoid mb-6 relative overflow-hidden transition-all duration-500 hover:border-[#d4af37]" style="height: max-content;" data-category="women photo" data-date="20260810">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="Anita Patel">
                  AP
                </div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug flex items-center gap-1.5">
                    Anita Patel
                    <span class="text-[9px] bg-amber-400/20 text-amber-300 px-1.5 py-0.2 rounded border border-amber-400/40 font-mono uppercase">VERIFIED BUYER</span>
                  </h3>
                  <span class="text-[10px] text-gray-400 block">Ahmedabad, Gujarat &bull; Verified Buyer</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>
              <span class="text-[10px] text-pink-300 bg-pink-400/10 border-pink-400/30 font-semibold px-2 py-0.5 rounded-full border">👩 Women's Hair</span>
            </div>

            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Extremely easy to use! Grey hair is soft & dark black now"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light italic">
              "Extremely easy to use in morning shower! No messy gloves needed, no chemical smell. My grey hair is soft, shiny, and 100% dark black now!"
            </p>

            <!-- Real Side-by-Side Before & After Photo Grid -->
            <div class="grid grid-cols-2 gap-2.5 mt-3">
              <div class="relative rounded-2xl overflow-hidden border border-white/10 bg-black/60 shadow-md" style="aspect-ratio: 1/1;">
                <img src="./assets/reviews/anita-patel-before.jpg" alt="Anita Patel Before" class="w-full h-full object-cover object-center">
                <span class="absolute top-2 left-2 bg-red-950/90 text-red-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-red-500/40 uppercase tracking-wider">BEFORE</span>
              </div>
              <div class="relative rounded-2xl overflow-hidden border border-white/10 bg-black/60 shadow-md" style="aspect-ratio: 1/1;">
                <img src="./assets/reviews/anita-patel-after.jpg" alt="Anita Patel After 10 Washes" class="w-full h-full object-cover object-center">
                <span class="absolute top-2 left-2 bg-emerald-950/90 text-emerald-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40 uppercase tracking-wider">AFTER 10 WASHES</span>
              </div>
            </div>

            <div class="p-2.5 rounded-xl bg-[#123824] border border-[#d4af37]/30 text-[11px] text-emerald-300 font-bold text-center mt-2">
              ✓ Result: Soft Shiny Dark Black Hair
            </div>
          </div>

          <div class="pt-4 mt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="js-like-btn hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300 transition-colors" data-likes="760">
              👍 <span class="js-like-count">760</span> Helpful
            </button>
          </div>
        </div>
"""

# 1. Update Reviews Files
def update_reviews_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert Anita Patel card at the top of the columns-1 masonry grid if not present
    if 'id="anita-patel"' not in content:
        grid_marker = '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">'
        if grid_marker in content:
            content = content.replace(grid_marker, grid_marker + '\n' + anita_card_html)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} with Anita Patel card!")

update_reviews_file('reviews.html')
update_reviews_file('demo_lab/reviews.html')
if os.path.exists('preview/reviews.html'):
    update_reviews_file('preview/reviews.html')

# 2. Update Product Pages (Card 3 for Anita Patel)
def update_product_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    old_anita_card = '''        <!-- Card 3 -->
        <div class="p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/40 space-y-4 shadow-2xl hover:-translate-y-1.5 transition-all">
          
          <div class="grid grid-cols-2 gap-2 rounded-2xl overflow-hidden relative">
            <div class="relative">
              <img src="./assets/blackroots-before-lady.jpg" alt="Before Anita" class="w-full h-44 object-cover rounded-xl">
              <span class="absolute top-2 left-2 bg-red-950/90 text-red-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-red-500/40">BEFORE</span>
            </div>
            <div class="relative">
              <img src="./assets/blackroots-after-lady.jpg" alt="After Anita" class="w-full h-44 object-cover rounded-xl">
              <span class="absolute top-2 left-2 bg-emerald-950/90 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40">AFTER 10 WASHES</span>
            </div>
          </div>

          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <h3 class="font-serif text-lg font-bold text-white">Anita Patel</h3>
              <span class="text-[11px] text-gray-400">Ahmedabad &bull; Verified Buyer</span>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>

          <p class="text-xs text-gray-300 font-light leading-relaxed italic">
            "Extremely easy to use in morning shower! No messy gloves needed, no chemical smell. My grey hair is soft, shiny, and 100% dark black now!"
          </p>

          <div class="p-2.5 rounded-xl bg-[#123824] border border-[#d4af37]/30 text-[11px] text-emerald-300 font-bold text-center">
            ✓ Result: Soft Shiny Dark Black Hair
          </div>

        </div>'''

    new_anita_card = '''        <!-- Card 3: Anita Patel (Clickable -> Opens reviews.html#anita-patel) -->
        <a href="reviews.html#anita-patel" class="block p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/40 space-y-4 shadow-2xl hover:-translate-y-1.5 hover:border-[#d4af37] transition-all group no-underline text-left cursor-pointer">
          
          <div class="grid grid-cols-2 gap-2 rounded-2xl overflow-hidden relative">
            <div class="relative">
              <img src="./assets/reviews/anita-patel-before.jpg" alt="Before Anita Patel" class="w-full h-44 object-cover rounded-xl group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-red-950/90 text-red-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-red-500/40">BEFORE</span>
            </div>
            <div class="relative">
              <img src="./assets/reviews/anita-patel-after.jpg" alt="After Anita Patel" class="w-full h-44 object-cover rounded-xl group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-emerald-950/90 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40">AFTER 10 WASHES</span>
            </div>
          </div>

          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Anita Patel</h3>
              <span class="text-[11px] text-gray-400">Ahmedabad, Gujarat &bull; Verified Buyer</span>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>

          <p class="text-xs text-gray-300 font-light leading-relaxed italic">
            "Extremely easy to use in morning shower! No messy gloves needed, no chemical smell. My grey hair is soft, shiny, and 100% dark black now!"
          </p>

          <div class="p-2.5 rounded-xl bg-[#123824] border border-[#d4af37]/30 text-[11px] text-emerald-300 font-bold text-center flex items-center justify-center gap-1">
            <span>✓ Result: Soft Shiny Dark Black Hair</span>
          </div>

          <div class="pt-2 text-center">
            <span class="text-[11px] font-bold text-amber-300 group-hover:underline flex items-center justify-center gap-1">
              💬 View Verified Review on Reviews Page &rarr;
            </span>
          </div>

        </a>'''

    if old_anita_card in content:
        content = content.replace(old_anita_card, new_anita_card)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} product card for Anita Patel!")

update_product_file('product.html')
update_product_file('demo_lab/product.html')
if os.path.exists('preview/product.html'):
    update_product_file('preview/product.html')

print("ANITA PATEL BEFORE & AFTER PHOTOS AND REVIEWS LINKING COMPLETE!")
