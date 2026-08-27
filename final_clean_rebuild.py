import random, shutil

random.seed(42)

# ============================================================
# 22 REVIEWS - Clean rebuild with new-avatar for ALL + proper photo sections
# Avatar assignments: new-avatar-1 to 25, unique per reviewer, gender-matched
# new-avatar grid layout (5x5):
# Row0: 1=M-sungl, 2=F-pink, 3=M-selfie, 4=F-teal, 5=M-formal
# Row1: 6=M-cafe,  7=F-dupatta, 8=M-nature, 9=F-saree-bindi, 10=M-kurta
# Row2: 11=F-back-smile, 12=M-smart, 13=F-mature-saree, 14=M-beard-sunglass, 15=SKIP(sunset)
# Row3: 16=M-older-glasses, 17=F-earrings, 18=M-farmer, 19=SKIP(sign), 20=F-black-sunglass
# Row4: 21=M-jacket, 22=F-pink-scarf, 23=M-forties, 24=F-yellow-dress, 25=M-elderly
# ============================================================

def av(n):
    return f'./assets/reviews/new-avatar-{n}.jpg'

def avatar_img(src, name):
    return f'<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="{src}" alt="{name}" class="w-full h-full rounded-full object-cover object-top"></div>'

def photo_block(src):
    return f'\n            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60" style="height:160px"><img src="{src}" alt="Customer Photo" class="w-full h-full object-cover object-center"></div>'

def no_photo_block():
    return '\n            <div class="flex-1 flex items-center justify-center py-4"><span class="text-5xl text-white/5 font-serif font-bold select-none">"</span></div>'

def card(name, city, date_label, date_ts, avatar_src, stars, rating, cat, cat_label, cat_cls, title, body, photo_src, helpful):
    avi = avatar_img(avatar_src, name)
    cat_span_cls = f'text-[10px] {cat_cls} font-semibold px-2 py-0.5 rounded-full border'
    photo_html = photo_block(photo_src) if photo_src else no_photo_block()
    return f'''
        <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col" data-category="{cat}" data-date="{date_ts}" style="min-height:340px">
          <div class="space-y-3 flex-1">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                {avi}
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">{name}</h3>
                  <span class="text-[10px] text-gray-400 block">{city} &bull; {date_label}</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">&#10003; Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">{stars} <span class="text-white font-bold ml-1">{rating}</span></div>
              <span class="{cat_span_cls}">{cat_label}</span>
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">{title}</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">{body}</p>{photo_html}
          </div>
          <div class="pt-4 mt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300" onclick="this.innerHTML='&#128077; {helpful+1} Helpful'">&#128077; {helpful} Helpful</button>
          </div>
        </div>'''

MC = 'text-amber-300 bg-amber-400/10 border-amber-400/30'
WC = 'text-pink-300 bg-pink-400/10 border-pink-400/30'

reviews = [
    card('Aarav Sharma',    'Lucknow, UP',     '2 days ago',   20260809, av(1),  '&#9733;&#9733;&#9733;&#9733;&#9733;','5.0','men photo',   '&#128104; Men\'s Scalp', MC, '"Greys cover ho gaye, 4-5 washes lage"',          'Thoda patience chahiye hota hai but result aata hai. Chemical dyes se scalp damage ho raha tha toh switch kiya. Smell bilkul nahi hai jo achhi baat hai.',                                              './assets/reviews/review-photo-1.jpg', 42),
    card('Fatima Rizvi',    'Hyderabad, TS',   '4 days ago',   20260807, av(2),  '&#9733;&#9733;&#9733;&#9733;&#9733;','4.8','women photo', '&#128105; Women\'s Hair', WC, '"Hair didn\'t feel dry or rough"',                 'Chemical dyes always left my hair rough. After 3 washes roots blended nicely. Hair texture is better. The smell is herbal but okay.',                                                                     './assets/reviews/review-photo-2.jpg', 37),
    card('Naincy Tiwari',   'Kanpur, UP',      '1 week ago',   20260804, av(13), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.5','women photo', '&#128105; Women\'s Hair', WC, '"&#2326;&#2369;&#2332;&#2354;&#2368; &#2325;&#2350; &#2361;&#2369;&#2312;, &#2336;&#2368;&#2325; &#2346;&#2381;&#2352;&#2379;&#2337;&#2325;&#2381;&#2335; &#2361;&#2376;"',  '2 &#2342;&#2367;&#2344; &#2350;&#2375;&#2306; &#2337;&#2367;&#2354;&#2368;&#2357;&#2352;&#2368; &#2310; &#2327;&#2312;&#2404; &#2346;&#2376;&#2325;&#2375;&#2332;&#2367;&#2306;&#2327; &#2348;&#2306;&#2342; &#2341;&#2368;&#2404; &#2325;&#2369;&#2331; &#2348;&#2366;&#2352; &#2311;&#2360;&#2381;&#2340;&#2375;&#2350;&#2366;&#2354; &#2325;&#2352;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2326;&#2379;&#2346;&#2337;&#2368; &#2346;&#2352; &#2326;&#2369;&#2332;&#2354;&#2368; &#2325;&#2350; &#2361;&#2369;&#2312;&#2404; &#2352;&#2370;&#2360;&#2368; &#2349;&#2368; &#2341;&#2379;&#2337;&#2368; &#2325;&#2350; &#2354;&#2327;&#2368;&#2404; &#2325;&#2369;&#2354; &#2350;&#2367;&#2354;&#2366;&#2325;&#2352; &#2336;&#2368;&#2325; &#2361;&#2376;&#2404;',
                './assets/reviews/face-photo-1.jpg', 58),
    card('Zaid Mansuri',    'Ahmedabad, GJ',   '5 days ago',   20260806, av(3),  '&#9733;&#9733;&#9733;&#9733;&#9733;','4.9','men photo',   '&#128104; Men\'s Beard', MC, '"Beard pe bhi kaam kiya, satisfied hun"',          'Beard ke greys pe bhi lagaya dekha. 4 washes ke baad shade improve hua. Skin pe koi reaction nahi tha. Instant nahi hota lekin gradual natural aata hai.',                                              './assets/reviews/review-photo-3.jpg', 28),
    card('Rakesh Gupta',    'Delhi NCR',       '1 week ago',   20260804, av(23), '&#9733;&#9733;&#9733;&#9733;&#9733;','5.0','men photo',   '&#128104; Men\'s Scalp', MC, '"3 washes ke baad farak dikh gaya"',               '3rd wash ke baad beard mein noticeable change tha. Skin pe koi reaction nahi tha. Kafi accha laga.',                                                                                                     './assets/reviews/face-photo-2.jpg', 64),
    card('Imran Khan',      'Kolkata, WB',     '6 days ago',   20260805, av(6),  '&#9733;&#9733;&#9733;&#9734;&#9734;','4.2','men',         '&#128104; Men\'s Scalp', MC, '"Both of us use it at home now"',                  'My wife and I both started using this. She uses it for her root greys, I use it for my scalp. Both of us have seen decent results after 4-5 washes. The 250ml bottle lasts a good while.',               None, 19),
    card('Pooja Sharma',    'Mumbai, MH',      '1 week ago',   20260804, av(7),  '&#9733;&#9733;&#9733;&#9733;&#9733;','4.9','women photo', '&#128105; Women\'s Hair', WC, '"So easy to use, no mess at all"',                 'Works just like a normal shampoo, no mixing or gloves needed. Roots have gotten slightly darker. The herbal smell takes a bit of getting used to but it\'s fine.',                                       './assets/reviews/review-photo-5.jpg', 30),
    card('Farhan Ahmed',    'Bhopal, MP',      '2 weeks ago',  20260728, av(8),  '&#9733;&#9733;&#9733;&#9734;&#9734;','3.9','men photo',   '&#128104; Men\'s Scalp', MC, '"Pehle wash mein kuch nahi dikh tha, gradually aaya"', 'Pehle wash ke baad koi farak nahi tha, 3rd wash mein shade aana shuru hua. Chemical dye jaisa instant black nahi hota, gradually aata hai. Mujhe yahi pasand aaya, natural lagta hai.',              './assets/reviews/farhan-bottle-photo.jpg', 18),
    card('Neha Joshi',      'Pune, MH',        '3 days ago',   20260808, av(4),  '&#9733;&#9733;&#9733;&#9733;&#9733;','5.0','women',       '&#128105; Women\'s Hair', WC, '"Husband started using it too"',                   'I started it for my greying roots and after 3 washes my husband noticed the difference and wanted to try it too. Works for both of us now. Good value for 250ml.',                                       None, 25),
    card('Tariq Siddiqui',  'Patna, Bihar',    '1 week ago',   20260804, av(10), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.8','men photo',   '&#128104; Men\'s Scalp', MC, '"COD pe mangaya, 3 din mein aa gaya"',             'COD option choose kiya tha, delivery 3 din mein aayi. Packing sealed thi. 4-5 washes mein result aaya. Koi chemical smell nahi hai.',                                                                    './assets/reviews/face-photo-3.jpg', 35),
    card('Meenakshi Iyer',  'Chennai, TN',     '4 days ago',   20260807, av(9),  '&#9733;&#9733;&#9733;&#9733;&#9733;','4.9','women photo', '&#128105; Women\'s Hair', WC, '"3 &#3118;&#3123;&#3128;&#3143; &#3056;&#3095;&#3137;&#3125;&#3135;&#3092; &#3015;&#3093;&#2986;&#3021; &#3125;&#3135;&#3096;&#3021;&#3116;&#3122;&#3021; &#3056;&#3095;&#3137;&#3121;&#3016;&#3092;&#3007;&#3009;"', '&#3007;&#3014;&#3021; &#3078;&#3092;&#3016;&#3021;&#3074;&#3021;&#3015;&#3128;&#3021; &#3050;&#3009;&#3019;&#3016;&#3021; &#3057;&#3020;&#3021;&#3071;&#3128;&#3021; &#3046;&#3074;&#3078;&#3021;&#3056;&#3019;&#3019;&#3021;. &#3006;&#3009;&#3016;&#3021; 3 &#3118;&#3123;&#3128;&#3143; &#3056;&#3095;&#3137;&#3125;&#3135;&#3092; &#3015;&#3093;&#2986;&#3021; &#3046;&#3006;&#3018;&#3021;&#3015;&#3122;&#3021; &#3046;&#3017;&#3021; &#3053;&#3092;&#3009;&#3016;&#3021; &#3051;&#3021;&#3018;&#3019;&#3021; &#3005;&#3092;&#3021;&#3038;&#3021;&#3015;&#3017;&#3006;&#3056;&#3021; &#3020;&#3006;&#3021;&#3038;&#3021;&#3016;&#3019;&#3021;. &#3010;&#3122;&#3016;&#3021; &#3046;&#3017;&#3021; &#3053;&#3092;&#3021; &#3046;&#3006;&#3016;&#3021;&#3038;&#3021; &#3007;&#3021;&#3009;&#3016;&#3021;.',   './assets/reviews/review-photo-7.jpg', 40),
    card('Sameer Sheikh',   'Surat, GJ',       '1 week ago',   20260804, av(12), '&#9733;&#9733;&#9733;&#9733;&#9733;','5.0','men photo',   '&#128104; Men\'s Scalp', MC, '"2 bottle mangaye the, dobara lunga"',             '2 bottles ek saath order kiye the. Pehli khatam ho gayi. Greys kafi cover hue hain. 250ml mein achhe washes milte hain. Dobara order karunga.',                                                         './assets/reviews/review-photo-8.jpg', 50),
    card('Priya Mehta',     'Mumbai, MH',      '3 days ago',   20260808, av(17), '&#9733;&#9733;&#9733;&#9733;&#9733;','5.0','women photo', '&#128105; Women\'s Hair', WC, '"Roots noticeably darker after 2 washes"',         'Could see a visible difference at the roots after the 2nd wash. Easy to use, works like regular shampoo. Smell is mild and herbal. Already told a few friends about it.',                                './assets/reviews/girl-holding-bottle.jpg', 46),
    card('Vikram Pandey',   'Varanasi, UP',    '5 days ago',   20260806, av(16), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.8','men photo',   '&#128104; Men\'s Scalp', MC, '"Chemical dye se zyada natural lagta hai"',        'Chemical dye ka colour kaafi obvious hota tha, logo ko pta chal jaata tha. Yahan gradual color aata hai so natural dikhta hai. COD pe mangaya tha, 4 din mein aa gaya.',                               './assets/reviews/table-bottle-hindu.jpg', 32),
    card('Selvam Krishnan', 'Coimbatore, TN',  '6 days ago',   20260805, av(18), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.7','men',         '&#128104; Men\'s Scalp', MC, '"&#3018;&#3086;&#3021;&#3021;&#3006;&#3056;&#3021; &#3050;&#3006;&#3056;&#3021;&#3021;&#3021;&#3021;, &#3015;&#3095;&#3021; &#3039;&#3007;&#3122;&#3016;&#3021;&#3038;&#3021; &#3007;&#3021;&#3021;&#3009;"', '4 &#3118;&#3123;&#3128;&#3143; &#3078;&#3016;&#3021;&#3071;&#3128;&#3021; &#3046;&#3006;&#3018;&#3021;&#3015;&#3122;&#3021; &#3015;&#3093;&#2986;&#3021;&#3074;&#3021;&#3021; &#3056;&#3095;&#3137;&#3091;&#3006;&#3056;&#3021;&#3006;&#3009;. &#3010;&#3122;&#3016;&#3021; &#3046;&#3017;&#3021; &#3046;&#3014;&#3021;&#3021;&#3021;&#3006;&#3056;&#3021; &#3007;&#3021;&#3021;&#3009;. &#3018;&#3109;&#3021;&#3071;&#3056;&#3016;&#3021; &#3042;&#3021;&#3009;&#3038;&#3021;&#3015;&#3016;&#3021;.',  None, 18),
    card('Anjali Singh',    'Jaipur, RJ',      '1 week ago',   20260804, av(20), '&#9733;&#9733;&#9733;&#9733;&#9733;','5.0','women',       '&#128105; Women\'s Hair', WC, '"Finally something that doesn\'t damage hair"',    'Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone now. Smell is herbal which I personally like.',                                 None, 26),
    card('Ritu Sharma',     'Indore, MP',      '4 days ago',   20260807, av(11), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.5','women',       '&#128105; Women\'s Hair', WC, '"4 &#2348;&#2366;&#2352; &#2343;&#2379;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2332;&#2921;&#2368;&#2306; &#2325;&#2366;&#2354;&#2368; &#2361;&#2379; &#2327;&#2312;&#2306;"',  '&#2341;&#2379;&#2322;&#2368; &#2313;&#2350;&#2381;&#2350;&#2368;&#2342; &#2325;&#2375; &#2360;&#2366;&#2341; &#2350;&#2306;&#2327;&#2366;&#2351;&#2366; &#2341;&#2366;&#2404; 4 &#2348;&#2366;&#2352; &#2343;&#2379;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2332;&#2921;&#2379;&#2306; &#2350;&#2375;&#2306; &#2347;&#2364;&#2352;&#2381;&#2325;&#2364; &#2342;&#2367;&#2326;&#2344;&#2375; &#2354;&#2327;&#2366;&#2404; &#2326;&#2379;&#2346;&#2322;&#2368; &#2346;&#2352; &#2325;&#2379;&#2312; &#2332;&#2354;&#2344; &#2344;&#2361;&#2368;&#2306; &#2361;&#2369;&#2312;&#2404; &#2341;&#2379;&#2322;&#2366; &#2360;&#2350;&#2351; &#2354;&#2327;&#2340;&#2366; &#2361;&#2376; &#2346;&#2352; &#2325;&#2366;&#2350; &#2325;&#2352;&#2340;&#2366; &#2361;&#2376;&#2404;',  None, 13),
    card('Mohit Rastogi',   'Noida, UP',       '3 days ago',   20260808, av(5),  '&#9733;&#9733;&#9733;&#9734;&#9734;','4.2','men',         '&#128104; Men\'s Scalp', MC, '"Takes time but works"',                           'Took about 5-6 washes to see a clear difference. Not instant like chemical dyes but the result looks more natural. No scalp burning which was my main concern. Decent product.',                        None, 21),
    card('Suresh Yadav',    'Agra, UP',        '2 weeks ago',  20260728, av(21), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.8','men',         '&#128104; Men\'s Scalp', MC, '"&#2360;&#2347;&#2364;&#2375;&#2342; &#2348;&#2366;&#2354; &#2309;&#2348; &#2348;&#2361;&#2369;&#2340; &#2325;&#2350; &#2342;&#2367;&#2326;&#2340;&#2375; &#2361;&#2376;&#2306;"',  '&#2346;&#2361;&#2354;&#2375; &#2347;&#2364;&#2381;&#2351;&#2366;&#2342;&#2366; &#2360;&#2347;&#2364;&#2375;&#2342; &#2348;&#2366;&#2354; &#2342;&#2367;&#2326;&#2340;&#2375; &#2341;&#2375;, &#2309;&#2348; &#2325;&#2366;&#2347;&#2364;&#2368; &#2325;&#2350; &#2361;&#2379; &#2327;&#2319; &#2361;&#2376;&#2306;&#2404; &#2325;&#2379;&#2312; &#2325;&#2375;&#2350;&#2367;&#2325;&#2354; &#2327;&#2306;&#2343; &#2344;&#2361;&#2368;&#2306; &#2361;&#2376;&#2404; COD &#2346;&#2352; &#2350;&#2306;&#2327;&#2366;&#2351;&#2366;, &#2337;&#2367;&#2354;&#2368;&#2357;&#2352;&#2368; &#2349;&#2368; &#2360;&#2350;&#2351; &#2346;&#2352; &#2310;&#2312;&#2404;',  None, 15),
    card('Kavya Reddy',     'Bengaluru, KA',   '5 days ago',   20260806, av(24), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.9','women',       '&#128105; Women\'s Hair', WC, '"My grey roots blended so naturally"',             'Using it for about 3 weeks now. The grey roots are much less visible. Hair doesn\'t feel dry. I actually look forward to wash days now. Good purchase.',                                                   None, 30),
    card('Ananya Dubey',    'Bhopal, MP',      '10 days ago',  20260801, av(22), '&#9733;&#9733;&#9733;&#9733;&#9733;','5.0','women',       '&#128105; Women\'s Hair', WC, '"Mummy ke liye liya, unhe bhi pasand aaya"',       'Mummy ke liye order kiya tha. Wo chemical wali dye nahi lagati thi. Isse try karaya, 4-5 washes mein unke greys kaafi cover ho gaye. Ab wo khud mangwa rahi hain.',                                     None, 37),
    card('Arjun Malhotra',  'Chandigarh, PB',  '1 week ago',   20260804, av(14), '&#9733;&#9733;&#9733;&#9733;&#9733;','4.6','men',         '&#128104; Scalp &amp; Beard', MC, '"No skin staining, great for beard too"',      'Applied on beard as well. No skin staining at all. Colour comes gradually which makes it look natural. Results after about 5 washes. Happy with the purchase.',                                          None, 23),
]

random.shuffle(reviews)
grid_html = '\n' + ''.join(reviews) + '\n      '

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

grid_open = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
grid_close = '      </div>\n\n      <!-- Bottom Order Callout -->'

start = content.index(grid_open) + len(grid_open)
end = content.index(grid_close)

new_content = content[:start] + grid_html + content[end:]

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print('DONE! All 22 reviews rebuilt clean — proper avatars, photos, consistent height!')
