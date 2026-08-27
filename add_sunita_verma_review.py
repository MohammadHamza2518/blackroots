import os
import re

sunita_card_html = """
        <!-- Sunita Verma Verified Customer Review Card (With Real Before & After Photos) -->
        <div id="sunita-verma" class="p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/60 shadow-2xl flex flex-col break-inside-avoid mb-6 relative overflow-hidden transition-all duration-500 hover:border-[#d4af37]" style="height: max-content;" data-category="women photo" data-date="20260805">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="Sunita Verma">
                  SV
                </div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug flex items-center gap-1.5">
                    Sunita Verma
                    <span class="text-[9px] bg-amber-400/20 text-amber-300 px-1.5 py-0.2 rounded border border-amber-400/40 font-mono uppercase">VERIFIED BUYER</span>
                  </h3>
                  <span class="text-[10px] text-gray-400 block">Kanpur, UP &bull; 1 week ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>
              <span class="text-[10px] text-pink-300 bg-pink-400/10 border-pink-400/30 font-semibold px-2 py-0.5 rounded-full border">👩 Women's Hair</span>
            </div>

            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Grey roots turned naturally black in 5 washes"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light italic">
              "I had grey hair and scalp itching from chemical dyes. After just 5 shower washes with BlackRoots, my grey roots turned naturally black and my scalp dandruff completely stopped!"
            </p>

            <!-- Real Side-by-Side Before & After Photo Grid -->
            <div class="grid grid-cols-2 gap-2.5 mt-3">
              <div class="relative rounded-2xl overflow-hidden border border-white/10 bg-black/60 shadow-md" style="aspect-ratio: 1/1;">
                <img src="./assets/reviews/sunita-verma-before.jpg" alt="Sunita Verma Before" class="w-full h-full object-cover object-center">
                <span class="absolute top-2 left-2 bg-red-950/90 text-red-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-red-500/40 uppercase tracking-wider">BEFORE</span>
              </div>
              <div class="relative rounded-2xl overflow-hidden border border-white/10 bg-black/60 shadow-md" style="aspect-ratio: 1/1;">
                <img src="./assets/reviews/sunita-verma-after.jpg" alt="Sunita Verma After 5 Washes" class="w-full h-full object-cover object-center">
                <span class="absolute top-2 left-2 bg-emerald-950/90 text-emerald-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40 uppercase tracking-wider">AFTER 5 WASHES</span>
              </div>
            </div>

            <div class="p-2.5 rounded-xl bg-[#123824] border border-[#d4af37]/30 text-[11px] text-emerald-300 font-bold text-center mt-2">
              ✓ Result: Natural Black Hair + Zero Dandruff
            </div>
          </div>

          <div class="pt-4 mt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="js-like-btn hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300 transition-colors" data-likes="142">
              👍 <span class="js-like-count">142</span> Helpful
            </button>
          </div>
        </div>
"""

hash_scroll_js = """
  <script>
    // Auto Scroll & Gold Glow Highlight for Linked Reviews (e.g. #sunita-verma)
    document.addEventListener('DOMContentLoaded', function() {
      if (window.location.hash) {
        const hash = window.location.hash;
        const targetEl = document.querySelector(hash);
        if (targetEl) {
          setTimeout(function() {
            targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
            targetEl.classList.add('ring-4', 'ring-[#d4af37]', 'scale-[1.02]', 'shadow-[0_0_35px_rgba(212,175,55,0.7)]');
            setTimeout(function() {
              targetEl.classList.remove('scale-[1.02]');
            }, 2500);
          }, 400);
        }
      }
    });
  </script>
"""

# 1. Update Reviews Files
def update_reviews_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert Sunita Verma card at top of review grid if not present
    if 'id="sunita-verma"' not in content:
        grid_marker = '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">'
        if grid_marker in content:
            content = content.replace(grid_marker, grid_marker + '\n' + sunita_card_html)

    # Insert Hash scroll JS
    if 'Auto Scroll & Gold Glow Highlight' not in content:
        content = content.replace('</body>', hash_scroll_js + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} with Sunita Verma card!")

update_reviews_file('reviews.html')
update_reviews_file('demo_lab/reviews.html')
if os.path.exists('preview/reviews.html'):
    update_reviews_file('preview/reviews.html')

# 2. Update Product Pages
def update_product_file(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Sunita Verma photos & add clickable link to reviews.html#sunita-verma
    old_sunita_card = '''        <!-- Card 1 -->
        <div class="p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/40 space-y-4 shadow-2xl hover:-translate-y-1.5 transition-all">
          
          <div class="grid grid-cols-2 gap-2 rounded-2xl overflow-hidden relative">
            <div class="relative">
              <img src="./assets/blackroots-before-lady.jpg" alt="Before Sunita" class="w-full h-44 object-cover rounded-xl">
              <span class="absolute top-2 left-2 bg-red-950/90 text-red-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-red-500/40">BEFORE</span>
            </div>
            <div class="relative">
              <img src="./assets/blackroots-after-lady.jpg" alt="After Sunita" class="w-full h-44 object-cover rounded-xl">
              <span class="absolute top-2 left-2 bg-emerald-950/90 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40">AFTER 5 WASHES</span>
            </div>
          </div>

          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <h3 class="font-serif text-lg font-bold text-white">Sunita Verma</h3>
              <span class="text-[11px] text-gray-400">Kanpur, UP &bull; Verified Buyer</span>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>

          <p class="text-xs text-gray-300 font-light leading-relaxed italic">
            "I had grey hair and scalp itching from chemical dyes. After just 5 shower washes with BlackRoots, my grey roots turned naturally black and my scalp dandruff completely stopped!"
          </p>

          <div class="p-2.5 rounded-xl bg-[#123824] border border-[#d4af37]/30 text-[11px] text-emerald-300 font-bold text-center">
            ✓ Result: Natural Black Hair + Zero Dandruff
          </div>

        </div>'''

    new_sunita_card = '''        <!-- Card 1: Sunita Verma (Clickable -> Opens reviews.html#sunita-verma) -->
        <a href="reviews.html#sunita-verma" class="block p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/40 space-y-4 shadow-2xl hover:-translate-y-1.5 hover:border-[#d4af37] transition-all group no-underline text-left cursor-pointer">
          
          <div class="grid grid-cols-2 gap-2 rounded-2xl overflow-hidden relative">
            <div class="relative">
              <img src="./assets/reviews/sunita-verma-before.jpg" alt="Before Sunita Verma" class="w-full h-44 object-cover rounded-xl group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-red-950/90 text-red-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-red-500/40">BEFORE</span>
            </div>
            <div class="relative">
              <img src="./assets/reviews/sunita-verma-after.jpg" alt="After Sunita Verma" class="w-full h-44 object-cover rounded-xl group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-2 left-2 bg-emerald-950/90 text-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40">AFTER 5 WASHES</span>
            </div>
          </div>

          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <div>
              <h3 class="font-serif text-lg font-bold text-white group-hover:text-[#d4af37] transition-colors">Sunita Verma</h3>
              <span class="text-[11px] text-gray-400">Kanpur, UP &bull; Verified Buyer</span>
            </div>
            <div class="text-amber-400 text-xs">★★★★★</div>
          </div>

          <p class="text-xs text-gray-300 font-light leading-relaxed italic">
            "I had grey hair and scalp itching from chemical dyes. After just 5 shower washes with BlackRoots, my grey roots turned naturally black and my scalp dandruff completely stopped!"
          </p>

          <div class="p-2.5 rounded-xl bg-[#123824] border border-[#d4af37]/30 text-[11px] text-emerald-300 font-bold text-center flex items-center justify-center gap-1">
            <span>✓ Result: Natural Black Hair + Zero Dandruff</span>
          </div>

          <div class="pt-2 text-center">
            <span class="text-[11px] font-bold text-amber-300 group-hover:underline flex items-center justify-center gap-1">
              💬 View Verified Review on Reviews Page &rarr;
            </span>
          </div>

        </a>'''

    if old_sunita_card in content:
        content = content.replace(old_sunita_card, new_sunita_card)
    elif 'Sunita Verma' in content and 'sunita-verma-before.jpg' not in content:
        # Generic regex replace if formatting slightly differed
        content = content.replace('./assets/blackroots-before-lady.jpg', './assets/reviews/sunita-verma-before.jpg')
        content = content.replace('./assets/blackroots-after-lady.jpg', './assets/reviews/sunita-verma-after.jpg')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path} product card for Sunita Verma!")

update_product_file('product.html')
update_product_file('demo_lab/product.html')
if os.path.exists('preview/product.html'):
    update_product_file('preview/product.html')

print("SUNITA VERMA BEFORE & AFTER PHOTOS AND REVIEWS LINKING COMPLETE!")
