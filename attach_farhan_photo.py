import re

def update_farhan_card(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_block = '''        <!-- Review 8: Farhan Ahmed (Muslim Male • Bhopal MP • Text Only) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/custom-avatar-9.jpg" alt="Farhan Ahmed" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Farhan Ahmed</h3>
                  <span class="text-[10px] text-gray-400 block">Bhopal, MP &bull; 2 weeks ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                ✓ Verified
              </span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★☆ <span class="text-white font-bold ml-1">3.9</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp</span>
            </div>

            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Takes 3-4 washes to see full effect, but gentle!"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light">
              First wash me light tint aaya tha, 3rd wash me accha dark black shade mila. Chemical dye jaisa instant unnatural jet black nahi hota jo sabko pata chal jaye, ye gradual natural black dikhta hai. Good product.
            </p>
          </div>'''

    new_block = '''        <!-- Review 8: Farhan Ahmed (Muslim Male • Bhopal MP • Bottle Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men photo">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/custom-avatar-9.jpg" alt="Farhan Ahmed" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Farhan Ahmed</h3>
                  <span class="text-[10px] text-gray-400 block">Bhopal, MP &bull; 2 weeks ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                ✓ Verified
              </span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★☆ <span class="text-white font-bold ml-1">3.9</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp</span>
            </div>

            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Takes 3-4 washes to see full effect, but gentle!"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light">
              First wash me light tint aaya tha, 3rd wash me accha dark black shade mila. Chemical dye jaisa instant unnatural jet black nahi hota jo sabko pata chal jaye, ye gradual natural black dikhta hai. Good product.
            </p>

            <!-- Customer Bottle Photo Attachment -->
            <div class="rounded-2xl overflow-hidden border border-white/10 aspect-video relative bg-black/60">
              <img src="./assets/reviews/farhan-bottle-photo.jpg" alt="Farhan Customer Bottle Photo" class="w-full h-full object-cover">
              <span class="absolute bottom-2 left-2 bg-black/80 backdrop-blur-md text-amber-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-amber-400/30">📸 Customer Bottle Photo</span>
            </div>
          </div>'''

    content = content.replace(old_block, new_block)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully attached bottle photo to Farhan Ahmed card in {filepath}')

update_farhan_card('demo_lab/reviews.html')
update_farhan_card('reviews.html')
update_farhan_card('preview/reviews.html')
