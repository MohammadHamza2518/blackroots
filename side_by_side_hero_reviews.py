import os
import re

hero_section_html = """
      <!-- Top Featured Hero Reviews (Side-by-Side Row: Sunita Verma #1 & Alok Mishra #2) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        
        <!-- #1 Hero Review: Sunita Verma -->
        <div id="sunita-verma" class="p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37] shadow-2xl flex flex-col justify-between relative overflow-hidden transition-all duration-500 hover:border-[#d4af37]" data-category="women photo" data-date="20260812" data-pinned="true">
          <div class="space-y-3">
            
            <div class="flex items-center justify-between">
              <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-[#d4af37] to-amber-300 text-black text-[10px] font-extrabold uppercase tracking-wider shadow-md">
                👑 #1 TOP FEATURED HERO REVIEW
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="Sunita Verma">
                  SV
                </div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug flex items-center gap-1.5">
                    Sunita Verma
                    <span class="text-[9px] bg-amber-400/20 text-amber-300 px-1.5 py-0.2 rounded border border-amber-400/40 font-mono uppercase">FEATURED</span>
                  </h3>
                  <span class="text-[10px] text-gray-400 block">Kanpur, UP &bull; Verified Buyer</span>
                </div>
              </div>
              <span class="text-[10px] text-pink-300 bg-pink-400/10 border-pink-400/30 font-semibold px-2 py-0.5 rounded-full border">👩 Women's Hair</span>
            </div>
            
            <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>

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
            <button type="button" class="js-like-btn hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300 transition-colors" data-likes="990">
              👍 <span class="js-like-count">990</span> Helpful
            </button>
          </div>
        </div>

        <!-- #2 Hero Review: Alok Mishra -->
        <div id="alok-mishra" class="p-6 rounded-3xl glass-panel-luxury border-2 border-[#d4af37] shadow-2xl flex flex-col justify-between relative overflow-hidden transition-all duration-500 hover:border-[#d4af37]" data-category="men photo" data-date="20260811" data-pinned="true">
          <div class="space-y-3">
            
            <div class="flex items-center justify-between">
              <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-gradient-to-r from-[#d4af37] to-amber-300 text-black text-[10px] font-extrabold uppercase tracking-wider shadow-md">
                🌟 #2 TOP FEATURED HERO REVIEW
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="Alok Mishra">
                  AM
                </div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug flex items-center gap-1.5">
                    Alok Mishra
                    <span class="text-[9px] bg-amber-400/20 text-amber-300 px-1.5 py-0.2 rounded border border-amber-400/40 font-mono uppercase">FEATURED</span>
                  </h3>
                  <span class="text-[10px] text-gray-400 block">Delhi NCR &bull; Verified Buyer</span>
                </div>
              </div>
              <span class="text-[10px] text-amber-300 bg-amber-400/10 border-amber-400/30 font-semibold px-2 py-0.5 rounded-full border">👨 Men's Scalp</span>
            </div>
            
            <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>

            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Thoda time laga par kaam kiya! Hair fall bhi ruk gaya"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light italic">
              "Chemical dyes ki wajah se heavy hair fall ho raha tha. BlackRoots use kiya, thoda time laga par kaam kiya! 8 washes ke baad grey hair dark ho gaye aur hair fall bhi ruk gaya."
            </p>

            <!-- Real Side-by-Side Before & After Photo Grid -->
            <div class="grid grid-cols-2 gap-2.5 mt-3">
              <div class="relative rounded-2xl overflow-hidden border border-white/10 bg-black/60 shadow-md" style="aspect-ratio: 1/1;">
                <img src="./assets/reviews/alok-mishra-before.jpg" alt="Alok Mishra Before" class="w-full h-full object-cover object-center">
                <span class="absolute top-2 left-2 bg-red-950/90 text-red-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-red-500/40 uppercase tracking-wider">BEFORE</span>
              </div>
              <div class="relative rounded-2xl overflow-hidden border border-white/10 bg-black/60 shadow-md" style="aspect-ratio: 1/1;">
                <img src="./assets/reviews/alok-mishra-after.jpg" alt="Alok Mishra After 8 Washes" class="w-full h-full object-cover object-center">
                <span class="absolute top-2 left-2 bg-emerald-950/90 text-emerald-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-emerald-500/40 uppercase tracking-wider">AFTER 8 WASHES</span>
              </div>
            </div>

            <div class="p-2.5 rounded-xl bg-[#123824] border border-[#d4af37]/30 text-[11px] text-emerald-300 font-bold text-center mt-2">
              ✓ Result: Grey Hair Darkened + Hair Fall Stopped
            </div>
          </div>

          <div class="pt-4 mt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="js-like-btn hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300 transition-colors" data-likes="885">
              👍 <span class="js-like-count">885</span> Helpful
            </button>
          </div>
        </div>

      </div>
"""

def update_file(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip Sunita and Alok cards from inside masonry columns if present
    content = re.sub(r'<!--\s*#1 Hero Review: Sunita Verma.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!--\s*#2 Hero Review: Alok Mishra.*?</div>\s*</div>', '', content, flags=re.DOTALL)

    # Insert hero_section_html right before masonry columns grid
    grid_marker = '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">'
    if 'Top Featured Hero Reviews (Side-by-Side Row' not in content and grid_marker in content:
        content = content.replace(grid_marker, hero_section_html + '\n      ' + grid_marker)

    # Update filter JS to handle hero cards visibility when filters change
    old_filter_js = """          reviewCards.forEach(card => {
            const cat = card.getAttribute('data-category');
            if (filter === 'all' || cat.includes(filter)) {
              card.style.display = 'flex';
            } else {
              card.style.display = 'none';
            }
          });"""

    new_filter_js = """          reviewCards.forEach(card => {
            const cat = card.getAttribute('data-category') || '';
            if (filter === 'all' || cat.includes(filter)) {
              card.style.display = card.classList.contains('grid') ? 'grid' : 'flex';
            } else {
              card.style.display = 'none';
            }
          });"""

    if old_filter_js in content:
        content = content.replace(old_filter_js, new_filter_js)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {file_path} with side-by-side hero reviews!")

update_file('demo_lab/reviews.html')
update_file('reviews.html')
if os.path.exists('preview/reviews.html'):
    update_file('preview/reviews.html')

print("SIDE BY SIDE HERO REVIEWS UPDATE COMPLETE!")
