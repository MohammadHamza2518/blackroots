"""
Complete rewrite of reviews.html for demo_lab:
1. Fix filter JS to work
2. Rewrite all 14 reviews to sound natural (mix of short/long, honest, Hinglish+English)
"""

import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ---- 1. FIX FILTER JS ----
# Find the closing </body> and inject filter JS before it
filter_js = '''
  <script>
    // Filter functionality for reviews
    const filterBtns = document.querySelectorAll('.js-filter-btn');
    const reviewCards = document.querySelectorAll('[data-category]');
    const showingCount = document.querySelector('.js-showing-count');

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.getAttribute('data-filter');

        // Update active button styles
        filterBtns.forEach(b => {
          b.classList.remove('bg-[#d4af37]', 'text-black');
          b.classList.add('bg-white/5', 'text-gray-300');
        });
        btn.classList.add('bg-[#d4af37]', 'text-black');
        btn.classList.remove('bg-white/5', 'text-gray-300');

        // Show/hide cards
        let visibleCount = 0;
        reviewCards.forEach(card => {
          const cats = card.getAttribute('data-category') || '';
          if (filter === 'all' || cats.includes(filter)) {
            card.style.display = '';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        });

        // Update count
        if (showingCount) showingCount.textContent = visibleCount + ' Reviews';
      });
    });
  </script>
'''

# Replace closing body tag with our script + closing body
content = content.replace('</body>', filter_js + '</body>')

# ---- 2. UPDATE SHOWING COUNT to have js class ----
content = content.replace(
    'Showing <strong>12 Featured Buyer Reviews</strong>',
    'Showing <strong class="js-showing-count">14 Reviews</strong>'
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Filter JS injected successfully!")

# ---- 3. Now rewrite review texts (natural, mixed short/long) ----
reviews_replacements = [
    # Review 1: Aarav Sharma - short and natural
    (
        '"Grey hair turned naturally black after 4 washes!"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Main 3 years se chemical dye use kar raha tha jisse mera scalp damage hone laga tha. BlackRoots herbal shampoo shift kiya aur sach me 4th wash tak saare greys cover ho gaye. Koi chemical smell nahi hai. Highly recommended for men!\n            </p>',
        '"Greys cover ho gaye, 4-5 washes lage"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Thoda time lagta hai result aane me but aata zaroor hai. Chemical wali dyes se scalp damage ho raha tha, isliye try kiya. Ab greys kaafi cover hain. Smell bhi koi nahi hai.\n            </p>'
    ),
    # Review 2: Fatima Rizvi - medium natural
    (
        '"Soft silk hair feel, zero ammonia smell!"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              As a woman, chemical dyes always made my hair dry like straw. BlackRoots is so gentle! My front root greys blended into shiny natural black after 3 washes. My hair feels nourished &amp; silky soft.\n            </p>',
        '"Hair dry nahi hua is baar, accha laga"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Pehle wali dye se hair bahut dry ho jaate the. Yahan se kharida dekh ke, 3 washes mein roots kaafi darken ho gayi. Smell bhi tolerable hai.\n            </p>'
    ),
    # Review 3: Naincy Tiwari - short
    (
        '"Scalp irritation &amp; dandruff completely gone"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Shuklaganj UP warehouse se dispatch fast hua tha 2 din me Kanpur mil gaya. Scalp itchiness complete band ho gayi aur flakes khatam ho gaye. 100% genuine herbal shampoo!\n            </p>',
        '"Scalp itching kaafi kam hui"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Delivery 2 din mein aayi, packaging theek thi. Use karne ke baad scalp pe itching band hui. Dandruff bhi thodi kam hua. Overall theek hai product.\n            </p>'
    ),
    # Review 4: Zaid Mansuri - medium
    (
        '"Great for men\'s hair &amp; beard greys"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Bhai beard greys par bhi use karke dekha &amp; natural dark black tone aaya without any skin staining. Simple 3 minute shower massage method works effortlessly.\n            </p>',
        '"Beard pe bhi try kiya, accha result"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Bhai beard ke greys pe bhi laga ke dekha. 3-4 washes mein shade kaafi improve hua. Skin staining nahi hua jo main sochta tha. Thoda patience chahiye bas.\n            </p>'
    ),
    # Review 5: Rakesh Gupta - short
    (
        '"Beard greys completely gone in 3 washes!"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Bhai beard &amp; patch greys par try kiya tha and 3rd wash tak natural dark shade aa gaya! Zero skin staining, zero itching and hair fall also reduced significantly. 100% recommended for men!\n            </p>',
        '"3 washes mein farak dikh gaya"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              3rd wash ke baad noticeable change tha. Skin pe koi reaction nahi hua. Hair fall bhi thoda kam laga. Theek product hai.\n            </p>'
    ),
    # Review 6: Imran Khan - long and natural
    (
        '"My husband and I both use it! Perfect unisex shampoo"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              We bought the 250ml bott',
        '"Ghar mein dono use karte hain"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              We bought the 250ml bott'
    ),
    # Review 7: Pooja Sharma - natural medium
    (
        '"No gloves or mixing needed, love natural shine"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              I love how easy this fits into my weekly routine. The botanical aroma is herbal and clean. My root greys disappear naturally without artificial harsh tones.\n            </p>',
        '"Simple use, koi jhanjhat nahi"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Normal shampoo ki tarah hi use hota hai, gloves ya mixing ka koi chakar nahi. Roots thodi dark huin hai. Smell herbal type hai, adjust ho jaata hai.\n            </p>'
    ),
    # Review 8: Farhan Ahmed - keep existing
    (
        '"Takes 3-4 washes to see full effect, but gentle!"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              First wash me light tint aaya tha, 3rd wash me accha dark black shade mila. Chemical dye jaisa instant unnatural jet black nahi hota jo sabko pata chal jaye, ye gradual natural black dikhta hai. Good product.\n            </p>',
        '"Pehle wash mein zyada nahi dikh, baad mein acha hua"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Pehle wash mein toh kuch nahi dikh tha, 3rd ke baad shade aa gaya. Chemical wali instant jet black nahi hai, gradually aata hai jo natural lagta hai.\n            </p>'
    ),
    # Review 9: Neha Joshi - short and casual
    (
        '"My husband and I both use it! Perfect unisex shampoo"</h4>',
        '"Husband ne bhi use karna shuru kiya"</h4>'
    ),
    # Review 10: Tariq Siddiqui - short
    (
        '"Fast BlueDart express delivery to Patna"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              COD option ke saath order kiya tha, 3 days me delivery mil gayi. Bottle 100% sealed packing me aayi. Result is authentic black tone without any harsh chemicals.\n            </p>',
        '"COD mein aaya, packaging sahi thi"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              COD select kiya tha, 3 din mein aa gaya. Box sealed tha. Use kiya toh result aaya but 4-5 washes lagte hain. Chemical smell nahi hai jo achhi baat hai.\n            </p>'
    ),
    # Review 11: Meenakshi Iyer - medium
    (
        '"Herbal aroma, grey roots vanished seamlessly"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              I was skeptical at first, but after 3 washes my greys blended naturally into black. Scalp feels clean and refreshed without any itchiness.\n            </p>',
        '"Roots thodi dark huin, overall okay"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Pehle mujhe doubt tha honestly. 3 washes ke baad greys thodi blend hin. Scalp irritation nahi hua. Smell herbal type hai. Koi side effect nahi mila abhi tak.\n            </p>'
    ),
    # Review 12: Sameer Sheikh - long natural
    (
        '"Bought 2-bottle combo pack. Best decision ever."</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Quality is top tier. 250ml size is very generous. Hair fall control is 100% real. Will definitely continue ordering from BlackRoots.\n            </p>',
        '"2 bottle mangaye the, use ho gaye"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              2 bottle order kiye the ek saath. Pehli khatam ho gayi. Result aaya hai, greys cover hue hain kuch had tak. 250ml mein kaafi washes milte hain. Dobara le lunga.\n            </p>'
    ),
    # Review 13: Priya Mehta
    (
        '"My roots are visibly darker after just 2 washes!"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Maine bahut products try kiye hai par ye genuinely alag hai. No ammonia smell, no mess, just simple shampoo karke chhod do. 2nd wash ke baad hi meri roots darken hone lagi. Packaging bhi ekdum premium hai! Highly recommend krungi apni saheli ko bhi.\n            </p>',
        '"2-3 washes mein roots thodi dark lagi"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              2nd wash ke baad thoda farak dikh raha tha roots mein. Simple use hai, normal shampoo ki tarah. Smell strong nahi hai. Saheli ko bhi bata diya.\n            </p>'
    ),
    # Review 14: Vikram Pandey
    (
        '"Bilkul natural result, koi artificial shine nahi!"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Pehle chemical dyes use karta tha jo 2-3 din baad pakka artificial lagta tha. BlackRoots se jo black aata hai wo genuinely natural dikhta hai. Scalp bhi healthy feel ho rahi hai. COD pe mangaya tha, delivery fast aayi. Product is 100% worth it!\n            </p>',
        '"Chemical dye se better laga mujhe"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Chemical dye se jo colour aata tha wo kaafi obvious lagta tha. Yahan gradual aata hai toh natural dikhai deta hai. COD tha delivery 4 din mein aayi. Theek experience raha.\n            </p>'
    ),
]

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

for old, new in reviews_replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:50]}...")
    else:
        print(f"NOT FOUND: {old[:50]}...")

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nAll review texts updated to natural style!")
