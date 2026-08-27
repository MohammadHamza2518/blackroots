import shutil

# New 5x5 grid layout (row x col):
# Row 0: male-sunglasses, female-pink, male-selfie-mask, female-dark, male-white-shirt
# Row 1: male-cafe, female-pink-dupatta, male-nature, female-saree-bindi, male-kurta
# Row 2: female-smile, male-dark-smart, female-mature-saree, male-beard-glasses, sunset(skip)
# Row 3: male-dark-glasses, female-earrings, male-field, male-focus-sign(skip), female-black
# Row 4: male-jacket-sunglasses, female-pink-scarf, male-forties, female-yellow-dress, male-elderly

# Map for 8 new reviewers - choosing gender-appropriate avatars:
# new-avatar-1  = row0,col0 = male sunglasses
# new-avatar-2  = row0,col1 = female pink
# new-avatar-5  = row0,col4 = male white shirt
# new-avatar-6  = row1,col0 = male cafe
# new-avatar-7  = row1,col1 = female pink dupatta
# new-avatar-9  = row1,col3 = female saree bindi
# new-avatar-11 = row2,col0 = female smile
# new-avatar-14 = row2,col3 = male beard glasses
# new-avatar-16 = row3,col0 = male dark glasses
# new-avatar-20 = row3,col4 = female black
# new-avatar-21 = row4,col0 = male jacket sunglasses
# new-avatar-22 = row4,col1 = female pink scarf

print("New avatars cropped and ready!")
print("Now adding 8 text-only reviews with new avatars...")

new_reviews_html = '''
        <!-- Review 15: Deepak Nair (Hindu Male • Kochi KL • English • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-1.jpg" alt="Deepak Nair" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Deepak Nair</h3>
                  <span class="text-[10px] text-gray-400 block">Kochi, KL &bull; 6 days ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">4.7</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Surprisingly gentle on scalp"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Was not expecting much honestly. But after 4 washes my grey patches have darkened quite a bit. No irritation at all. Will continue using.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 19 Helpful'">👍 18 Helpful</button>
          </div>
        </div>

        <!-- Review 16: Anjali Singh (Hindu Female • Jaipur RJ • English • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="women">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-2.jpg" alt="Anjali Singh" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Anjali Singh</h3>
                  <span class="text-[10px] text-gray-400 block">Jaipur, RJ &bull; 1 week ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>
              <span class="text-[10px] text-pink-300 font-semibold bg-pink-400/10 border border-pink-400/30 px-2 py-0.5 rounded-full">👩 Women's Hair</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Finally something that doesn't damage my hair"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone now. Smell is herbal which I personally like.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 27 Helpful'">👍 26 Helpful</button>
          </div>
        </div>

        <!-- Review 17: Ritu Sharma (Hindu Female • Indore MP • Hinglish • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="women">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-7.jpg" alt="Ritu Sharma" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Ritu Sharma</h3>
                  <span class="text-[10px] text-gray-400 block">Indore, MP &bull; 4 days ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">4.5</span></div>
              <span class="text-[10px] text-pink-300 font-semibold bg-pink-400/10 border border-pink-400/30 px-2 py-0.5 rounded-full">👩 Women's Hair</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Roots darken ho gayi, satisfied hun"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Kuch expectations ke saath mangaya tha. 4 washes ke baad roots mein farak dikh raha hai. Scalp pe koi problem nahi. Thoda time lagta hai but worth it hai.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 14 Helpful'">👍 13 Helpful</button>
          </div>
        </div>

        <!-- Review 18: Mohit Rastogi (Hindu Male • Noida UP • English • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-5.jpg" alt="Mohit Rastogi" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Mohit Rastogi</h3>
                  <span class="text-[10px] text-gray-400 block">Noida, UP &bull; 3 days ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★☆ <span class="text-white font-bold ml-1">4.2</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Takes time but works"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Took about 5-6 washes to see a clear difference. Not instant like chemical dyes but the result looks more natural. No scalp burning which was my main concern. Decent product.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 22 Helpful'">👍 21 Helpful</button>
          </div>
        </div>

        <!-- Review 19: Suresh Yadav (Hindu Male • Agra UP • Hinglish • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-6.jpg" alt="Suresh Yadav" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Suresh Yadav</h3>
                  <span class="text-[10px] text-gray-400 block">Agra, UP &bull; 2 weeks ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">4.8</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Greys kaafi kam dikh rahe hain ab"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Pehle zyada greys dikhte the, ab natural lag raha hai. Koi chemical smell nahi hai. COD milta hai jo achha laga. Delivery bhi time pe aayi thi.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 16 Helpful'">👍 15 Helpful</button>
          </div>
        </div>

        <!-- Review 20: Kavya Reddy (Hindu Female • Bengaluru KA • English • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="women">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-11.jpg" alt="Kavya Reddy" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Kavya Reddy</h3>
                  <span class="text-[10px] text-gray-400 block">Bengaluru, KA &bull; 5 days ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">4.9</span></div>
              <span class="text-[10px] text-pink-300 font-semibold bg-pink-400/10 border border-pink-400/30 px-2 py-0.5 rounded-full">👩 Women's Hair</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"My grey roots blended so naturally"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Using it for about 3 weeks now. The grey roots are much less visible. Hair doesn't feel dry. I actually look forward to wash days now. Good purchase.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 31 Helpful'">👍 30 Helpful</button>
          </div>
        </div>

        <!-- Review 21: Ananya Dubey (Hindu Female • Bhopal MP • Hinglish • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="women">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-22.jpg" alt="Ananya Dubey" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Ananya Dubey</h3>
                  <span class="text-[10px] text-gray-400 block">Bhopal, MP &bull; 10 days ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">5.0</span></div>
              <span class="text-[10px] text-pink-300 font-semibold bg-pink-400/10 border border-pink-400/30 px-2 py-0.5 rounded-full">👩 Women's Hair</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Mummy ke liye liya, unhe bhi pasand aaya"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Mummy ke liye order kiya tha. Wo chemical wali dye nahi lagati thi. Isse try karaya, 4-5 washes mein unke greys kaafi cover ho gaye. Ab wo khud mangwa rahi hain.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 38 Helpful'">👍 37 Helpful</button>
          </div>
        </div>

        <!-- Review 22: Arjun Malhotra (Hindu Male • Chandigarh PB • English • No Photo) -->
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="men">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-14.jpg" alt="Arjun Malhotra" class="w-full h-full rounded-full object-cover"></div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">Arjun Malhotra</h3>
                  <span class="text-[10px] text-gray-400 block">Chandigarh, PB &bull; 1 week ago</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">4.6</span></div>
              <span class="text-[10px] text-amber-300 font-semibold bg-amber-400/10 border border-amber-400/30 px-2 py-0.5 rounded-full">👨 Men's Scalp &amp; Beard</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"No skin staining, great for beard too"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Applied on beard as well. No skin staining at all. Colour comes gradually which makes it look natural. Results after about 5 washes. Happy with the purchase.</p>
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 24 Helpful'">👍 23 Helpful</button>
          </div>
        </div>

'''

# Insert new reviews before closing grid div
with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

insert_before = '      </div>\n\n      <!-- Bottom Order Callout -->'
content = content.replace(insert_before, new_reviews_html + '      </div>\n\n      <!-- Bottom Order Callout -->')

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(content)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print('8 new text-only reviews added (5 English + 3 Hinglish) with new avatars!')
