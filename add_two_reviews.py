def add_two_reviews(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_reviews = '''
        <!-- Review 13: Priya Mehta (Hindu Female • Mumbai MH • Girl Holding Bottle Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="women photo">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">PM</div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Priya Mehta</h3>
                  <span class="text-[10px] text-gray-400 block">Mumbai, MH &bull; 3 days ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                ✓ Verified
              </span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>
              <span class="text-[10px] text-pink-300 font-semibold bg-pink-400/10 border border-pink-400/30 px-2 py-0.5 rounded-full">👩 Women's Hair & Roots</span>
            </div>

            <h4 class="font-serif text-lg font-bold text-white leading-snug">"My roots are visibly darker after just 2 washes!"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light">
              Maine bahut products try kiye hai par ye genuinely alag hai. No ammonia smell, no mess, just simple shampoo karke chhod do. 2nd wash ke baad hi meri roots darken hone lagi. Packaging bhi ekdum premium hai! Highly recommend krungi apni saheli ko bhi.
            </p>

            <!-- Girl Holding Bottle Photo -->
            <div class="rounded-2xl overflow-hidden border border-white/10 aspect-video relative bg-black/60">
              <img src="./assets/reviews/girl-holding-bottle.jpg" alt="Customer Holding BlackRoots Bottle" class="w-full h-full object-cover">
              <span class="absolute bottom-2 left-2 bg-black/80 backdrop-blur-md text-amber-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-amber-400/30">📸 Customer Bottle Photo</span>
            </div>
          </div>

          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 47 Helpful'">
              👍 46 Helpful
            </button>
          </div>
        </div>

        <!-- Review 14: Vikram Pandey (Hindu Male • Varanasi UP • Bottle on Table Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men photo">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">VP</div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Vikram Pandey</h3>
                  <span class="text-[10px] text-gray-400 block">Varanasi, UP &bull; 5 days ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">
                ✓ Verified
              </span>
            </div>

            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">4.8</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp & Beard</span>
            </div>

            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Bilkul natural result, koi artificial shine nahi!"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light">
              Pehle chemical dyes use karta tha jo 2-3 din baad pakka artificial lagta tha. BlackRoots se jo black aata hai wo genuinely natural dikhta hai. Scalp bhi healthy feel ho rahi hai. COD pe mangaya tha, delivery fast aayi. Product is 100% worth it!
            </p>

            <!-- Bottle on Table Photo -->
            <div class="rounded-2xl overflow-hidden border border-white/10 aspect-video relative bg-black/60">
              <img src="./assets/reviews/table-bottle-hindu.jpg" alt="BlackRoots Bottle on Table" class="w-full h-full object-cover">
              <span class="absolute bottom-2 left-2 bg-black/80 backdrop-blur-md text-amber-300 text-[9px] font-bold px-2 py-0.5 rounded-full border border-amber-400/30">📸 Customer Bottle Photo</span>
            </div>
          </div>

          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 33 Helpful'">
              👍 32 Helpful
            </button>
          </div>
        </div>

'''

    insert_before = '      </div>\n\n      <!-- Bottom Order Callout -->'
    content = content.replace(insert_before, new_reviews + '      </div>\n\n      <!-- Bottom Order Callout -->')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Added 2 new reviews in {filepath}')

add_two_reviews('demo_lab/reviews.html')
add_two_reviews('reviews.html')
add_two_reviews('preview/reviews.html')
