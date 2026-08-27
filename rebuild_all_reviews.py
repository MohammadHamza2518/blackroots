import random, shutil, re

random.seed(42)

# ============================================================
# ALL 22 REVIEW CARDS - Complete definitions
# ============================================================
reviews = [
    # --- Original 14 reviews ---
    {
        'id': 1, 'name': 'Aarav Sharma', 'city': 'Lucknow, UP', 'date_label': '2 days ago', 'date_ts': 20260809,
        'avatar': './assets/reviews/custom-avatar-1.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '5.0', 'cat': 'men photo', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Greys cover ho gaye, 4-5 washes lage"',
        'body': 'Thoda patience chahiye hota hai but result aata hai. Chemical dyes se scalp damage ho raha tha toh switch kiya. Smell bilkul nahi hai jo achhi baat hai.',
        'photo_src': './assets/reviews/review-photo-1.jpg', 'helpful': 42,
    },
    {
        'id': 2, 'name': 'Fatima Rizvi', 'city': 'Hyderabad, TS', 'date_label': '4 days ago', 'date_ts': 20260807,
        'avatar': './assets/reviews/custom-avatar-2.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.8', 'cat': 'women photo', 'cat_label': '👩 Women\'s Roots', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Hair didn\'t feel dry or rough"',
        'body': 'Chemical dyes always left my hair rough. After 3 washes roots blended nicely. Hair texture is better. The smell is herbal but okay.',
        'photo_src': './assets/reviews/review-photo-2.jpg', 'helpful': 37,
    },
    {
        'id': 3, 'name': 'Naincy Tiwari', 'city': 'Kanpur, UP', 'date_label': '1 week ago', 'date_ts': 20260804,
        'avatar_type': 'initial', 'initial': 'NT', 'avatar': '',
        'stars': '★★★★★', 'rating': '4.5', 'cat': 'women photo', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Scalp feels calmer after using this"',
        'body': 'Delivery was quick, came in 2 days. Packaging was sealed properly. After a few washes scalp irritation reduced noticeably. Dandruff also seems less. Decent product.',
        'photo_src': './assets/reviews/face-photo-1.jpg', 'helpful': 58,
    },
    {
        'id': 4, 'name': 'Zaid Mansuri', 'city': 'Ahmedabad, GJ', 'date_label': '5 days ago', 'date_ts': 20260806,
        'avatar': './assets/reviews/custom-avatar-7.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.9', 'cat': 'men photo', 'cat_label': '👨 Men\'s Beard & Hair', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Beard pe bhi kaam kiya, satisfied hun"',
        'body': 'Beard ke greys pe bhi lagaya dekha. 4 washes ke baad shade improve hua. Skin pe koi reaction nahi tha. Instant nahi hota lekin gradual natural aata hai.',
        'photo_src': './assets/reviews/review-photo-3.jpg', 'helpful': 28,
    },
    {
        'id': 5, 'name': 'Rakesh Gupta', 'city': 'Delhi NCR', 'date_label': '1 week ago', 'date_ts': 20260804,
        'avatar_type': 'initial', 'initial': 'RG', 'avatar': '',
        'stars': '★★★★★', 'rating': '5.0', 'cat': 'men photo', 'cat_label': '👨 Men\'s Scalp & Beard', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"3 washes ke baad farak dikh gaya"',
        'body': '3rd wash ke baad beard mein noticeable change tha. Skin pe koi reaction nahi tha. Kafi accha laga.',
        'photo_src': './assets/reviews/face-photo-2.jpg', 'helpful': 64,
    },
    {
        'id': 6, 'name': 'Imran Khan', 'city': 'Kolkata, WB', 'date_label': '6 days ago', 'date_ts': 20260805,
        'avatar': './assets/reviews/custom-avatar-5.jpg', 'avatar_type': 'img',
        'stars': '★★★★☆', 'rating': '4.2', 'cat': 'men', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Both of us use it at home now"',
        'body': 'My wife and I both started using this. She uses it for her root greys, I use it for my scalp. Both of us have seen decent results after 4-5 washes. The 250ml bottle lasts a good while.',
        'photo_src': None, 'helpful': 19,
    },
    {
        'id': 7, 'name': 'Pooja Sharma', 'city': 'Mumbai, MH', 'date_label': '1 week ago', 'date_ts': 20260804,
        'avatar': './assets/reviews/custom-avatar-6.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.9', 'cat': 'women photo', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"So easy to use, no mess at all"',
        'body': 'Works just like a normal shampoo, no mixing or gloves needed. Roots have gotten slightly darker. The herbal smell takes a bit of getting used to but it\'s fine.',
        'photo_src': './assets/reviews/review-photo-5.jpg', 'helpful': 30,
    },
    {
        'id': 8, 'name': 'Farhan Ahmed', 'city': 'Bhopal, MP', 'date_label': '2 weeks ago', 'date_ts': 20260728,
        'avatar': './assets/reviews/custom-avatar-9.jpg', 'avatar_type': 'img',
        'stars': '★★★★☆', 'rating': '3.9', 'cat': 'men photo', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Pehle wash mein kuch nahi dikh tha, gradually aaya"',
        'body': 'Pehle wash ke baad koi farak nahi tha, 3rd wash mein shade aana shuru hua. Chemical dye jaisa instant black nahi hota, gradually aata hai. Mujhe yahi pasand aaya, natural lagta hai.',
        'photo_src': './assets/reviews/farhan-bottle-photo.jpg', 'helpful': 18,
    },
    {
        'id': 9, 'name': 'Neha Joshi', 'city': 'Pune, MH', 'date_label': '3 days ago', 'date_ts': 20260808,
        'avatar': './assets/reviews/custom-avatar-8.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '5.0', 'cat': 'women', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Husband started using it too after seeing results"',
        'body': 'I started it for my greying roots and after 3 washes my husband noticed the difference and wanted to try it too. Works for both of us now. Good value for 250ml.',
        'photo_src': None, 'helpful': 25,
    },
    {
        'id': 10, 'name': 'Tariq Siddiqui', 'city': 'Patna, Bihar', 'date_label': '1 week ago', 'date_ts': 20260804,
        'avatar_type': 'initial', 'initial': 'TS', 'avatar': '',
        'stars': '★★★★★', 'rating': '4.8', 'cat': 'men photo', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"COD pe mangaya, 3 din mein aa gaya"',
        'body': 'COD option choose kiya tha, delivery 3 din mein aayi. Packing sealed thi. 4-5 washes mein result aaya. Koi chemical smell nahi hai.',
        'photo_src': './assets/reviews/face-photo-3.jpg', 'helpful': 35,
    },
    {
        'id': 11, 'name': 'Meenakshi Iyer', 'city': 'Chennai, TN', 'date_label': '4 days ago', 'date_ts': 20260807,
        'avatar': './assets/reviews/custom-avatar-10.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.9', 'cat': 'women photo', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Greys blended after a few washes"',
        'body': 'Was skeptical at first honestly. After 3 washes the greys started blending in. No scalp irritation at all. Herbal smell is fine. No side effects so far.',
        'photo_src': './assets/reviews/review-photo-7.jpg', 'helpful': 40,
    },
    {
        'id': 12, 'name': 'Sameer Sheikh', 'city': 'Surat, GJ', 'date_label': '1 week ago', 'date_ts': 20260804,
        'avatar': './assets/reviews/custom-avatar-20.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '5.0', 'cat': 'men photo', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"2 bottle mangaye the, dobara lunga"',
        'body': '2 bottles ek saath order kiye the. Pehli khatam ho gayi. Greys kafi cover hue hain. 250ml mein achhe washes milte hain. Dobara order karunga.',
        'photo_src': './assets/reviews/review-photo-8.jpg', 'helpful': 50,
    },
    {
        'id': 13, 'name': 'Priya Mehta', 'city': 'Mumbai, MH', 'date_label': '3 days ago', 'date_ts': 20260808,
        'avatar_type': 'initial', 'initial': 'PM', 'avatar': '',
        'stars': '★★★★★', 'rating': '5.0', 'cat': 'women photo', 'cat_label': '👩 Women\'s Hair & Roots', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Roots noticeably darker after 2 washes"',
        'body': 'Could see a visible difference at the roots after the 2nd wash. Easy to use, works like regular shampoo. Smell is mild and herbal. Already told a few friends about it.',
        'photo_src': './assets/reviews/girl-holding-bottle.jpg', 'helpful': 46,
    },
    {
        'id': 14, 'name': 'Vikram Pandey', 'city': 'Varanasi, UP', 'date_label': '5 days ago', 'date_ts': 20260806,
        'avatar_type': 'initial', 'initial': 'VP', 'avatar': '',
        'stars': '★★★★★', 'rating': '4.8', 'cat': 'men photo', 'cat_label': '👨 Men\'s Scalp & Beard', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Chemical dye se zyada natural lagta hai"',
        'body': 'Chemical dye ka colour kaafi obvious hota tha, logo ko pta chal jaata tha. Yahan gradual color aata hai so natural dikhta hai. COD pe mangaya tha, 4 din mein aa gaya.',
        'photo_src': './assets/reviews/table-bottle-hindu.jpg', 'helpful': 32,
    },
    # --- New 8 reviews ---
    {
        'id': 15, 'name': 'Deepak Nair', 'city': 'Kochi, KL', 'date_label': '6 days ago', 'date_ts': 20260805,
        'avatar': './assets/reviews/new-avatar-1.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.7', 'cat': 'men', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Surprisingly gentle on scalp"',
        'body': 'Was not expecting much honestly. But after 4 washes my grey patches have darkened quite a bit. No irritation at all. Will continue using.',
        'photo_src': None, 'helpful': 18,
    },
    {
        'id': 16, 'name': 'Anjali Singh', 'city': 'Jaipur, RJ', 'date_label': '1 week ago', 'date_ts': 20260804,
        'avatar': './assets/reviews/new-avatar-2.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '5.0', 'cat': 'women', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Finally something that doesn\'t damage my hair"',
        'body': 'Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone now. Smell is herbal which I personally like.',
        'photo_src': None, 'helpful': 26,
    },
    {
        'id': 17, 'name': 'Ritu Sharma', 'city': 'Indore, MP', 'date_label': '4 days ago', 'date_ts': 20260807,
        'avatar': './assets/reviews/new-avatar-7.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.5', 'cat': 'women', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Roots darken ho gayi, satisfied hun"',
        'body': 'Kuch expectations ke saath mangaya tha. 4 washes ke baad roots mein farak dikh raha hai. Scalp pe koi problem nahi. Thoda time lagta hai but worth it hai.',
        'photo_src': None, 'helpful': 13,
    },
    {
        'id': 18, 'name': 'Mohit Rastogi', 'city': 'Noida, UP', 'date_label': '3 days ago', 'date_ts': 20260808,
        'avatar': './assets/reviews/new-avatar-5.jpg', 'avatar_type': 'img',
        'stars': '★★★★☆', 'rating': '4.2', 'cat': 'men', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Takes time but works"',
        'body': 'Took about 5-6 washes to see a clear difference. Not instant like chemical dyes but the result looks more natural. No scalp burning which was my main concern. Decent product.',
        'photo_src': None, 'helpful': 21,
    },
    {
        'id': 19, 'name': 'Suresh Yadav', 'city': 'Agra, UP', 'date_label': '2 weeks ago', 'date_ts': 20260728,
        'avatar': './assets/reviews/new-avatar-6.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.8', 'cat': 'men', 'cat_label': '👨 Men\'s Scalp', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"Greys kaafi kam dikh rahe hain ab"',
        'body': 'Pehle zyada greys dikhte the, ab natural lag raha hai. Koi chemical smell nahi hai. COD milta hai jo achha laga. Delivery bhi time pe aayi thi.',
        'photo_src': None, 'helpful': 15,
    },
    {
        'id': 20, 'name': 'Kavya Reddy', 'city': 'Bengaluru, KA', 'date_label': '5 days ago', 'date_ts': 20260806,
        'avatar': './assets/reviews/new-avatar-11.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.9', 'cat': 'women', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"My grey roots blended so naturally"',
        'body': 'Using it for about 3 weeks now. The grey roots are much less visible. Hair doesn\'t feel dry. I actually look forward to wash days now. Good purchase.',
        'photo_src': None, 'helpful': 30,
    },
    {
        'id': 21, 'name': 'Ananya Dubey', 'city': 'Bhopal, MP', 'date_label': '10 days ago', 'date_ts': 20260801,
        'avatar': './assets/reviews/new-avatar-22.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '5.0', 'cat': 'women', 'cat_label': '👩 Women\'s Hair', 'cat_class': 'text-pink-300 bg-pink-400/10 border-pink-400/30',
        'title': '"Mummy ke liye liya, unhe bhi pasand aaya"',
        'body': 'Mummy ke liye order kiya tha. Wo chemical wali dye nahi lagati thi. Isse try karaya, 4-5 washes mein unke greys kaafi cover ho gaye. Ab wo khud mangwa rahi hain.',
        'photo_src': None, 'helpful': 37,
    },
    {
        'id': 22, 'name': 'Arjun Malhotra', 'city': 'Chandigarh, PB', 'date_label': '1 week ago', 'date_ts': 20260804,
        'avatar': './assets/reviews/new-avatar-14.jpg', 'avatar_type': 'img',
        'stars': '★★★★★', 'rating': '4.6', 'cat': 'men', 'cat_label': '👨 Men\'s Scalp &amp; Beard', 'cat_class': 'text-amber-300 bg-amber-400/10 border-amber-400/30',
        'title': '"No skin staining, great for beard too"',
        'body': 'Applied on beard as well. No skin staining at all. Colour comes gradually which makes it look natural. Results after about 5 washes. Happy with the purchase.',
        'photo_src': None, 'helpful': 23,
    },
]

def make_avatar_html(r):
    if r['avatar_type'] == 'img':
        return f'<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="{r["avatar"]}" alt="{r["name"]}" class="w-full h-full rounded-full object-cover"></div>'
    else:
        return f'<div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">{r["initial"]}</div>'

def make_photo_html(r):
    if r['photo_src']:
        return f'''
            <div class="rounded-2xl overflow-hidden border border-white/10 aspect-video relative bg-black/60">
              <img src="{r['photo_src']}" alt="Review Photo" class="w-full h-full object-cover">
            </div>'''
    return ''

def make_card(r):
    return f'''
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 space-y-4 shadow-xl flex flex-col justify-between" data-category="{r['cat']}" data-date="{r['date_ts']}">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                {make_avatar_html(r)}
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">{r['name']}</h3>
                  <span class="text-[10px] text-gray-400 block">{r['city']} &bull; {r['date_label']}</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">{r['stars']} <span class="text-white font-bold ml-1">{r['rating']}</span></div>
              <span class="text-[10px] {r['cat_class']} font-semibold px-2 py-0.5 rounded-full">{r['cat_label']}</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">{r['title']}</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">{r['body']}</p>{make_photo_html(r)}
          </div>
          <div class="pt-4 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='👍 {r['helpful']+1} Helpful'">👍 {r['helpful']} Helpful</button>
          </div>
        </div>'''

# Shuffle all 22 reviews randomly
random.shuffle(reviews)

# Build the grid HTML
grid_html = '\n' + ''.join([make_card(r) for r in reviews]) + '\n      '

# Now inject into the reviews.html
with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the entire grid inner content
grid_open = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
grid_close = '      </div>\n\n      <!-- Bottom Order Callout -->'

start = content.index(grid_open) + len(grid_open)
end = content.index(grid_close)

new_content = content[:start] + grid_html + content[end:]

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print('SUCCESS! All 22 reviews rebuilt + randomly shuffled + data-date set!')
