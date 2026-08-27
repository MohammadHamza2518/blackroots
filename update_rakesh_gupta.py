import re

def update_rakesh(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_block = '''        <!-- Review 5: Sunita Verma (Hindu Female • Delhi NCR • Face Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="women photo">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">SV</div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Sunita Verma</h3>
                  <span class="text-[10px] text-gray-400 block">Delhi NCR &bull; 1 week ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                ✓ Verified
              </span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>
              <span class="text-[10px] text-pink-300 font-semibold bg-pink-400/10 border border-pink-400/30 px-2 py-0.5 rounded-full">👩 Women's Hair</span>
            </div>'''

    new_block = '''        <!-- Review 5: Rakesh Gupta (Hindu Male • Delhi NCR • Face Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men photo">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">RG</div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Rakesh Gupta</h3>
                  <span class="text-[10px] text-gray-400 block">Delhi NCR &bull; 1 week ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                ✓ Verified
              </span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp & Beard</span>
            </div>'''

    content = content.replace(old_block, new_block)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated Rakesh Gupta review card in {filepath}')

update_rakesh('demo_lab/reviews.html')
update_rakesh('reviews.html')
update_rakesh('preview/reviews.html')
