import shutil
import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# The current avatar block for Naincy Tiwari is:
# <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-13.jpg" alt="Naincy Tiwari" class="w-full h-full rounded-full object-cover object-top"></div>
avatar_old = '<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/new-avatar-13.jpg" alt="Naincy Tiwari" class="w-full h-full rounded-full object-cover object-top"></div>'
avatar_new = '<div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">NT</div>'

c = c.replace(avatar_old, avatar_new)

# Hindi Title
title_old = '"&#2326;&#2369;&#2332;&#2354;&#2368; &#2325;&#2350; &#2361;&#2369;&#2312;, &#2336;&#2368;&#2325; &#2346;&#2381;&#2352;&#2379;&#2337;&#2325;&#2381;&#2335; &#2361;&#2376;"'
# Just in case it's literal or html entities
title_literal = '"खुजली कम हुई, ठीक प्रोडक्ट है"'

c = c.replace(title_old, '"Scalp feels calmer after using this"')
c = c.replace(title_literal, '"Scalp feels calmer after using this"')
c = c.replace('"&#2326;&#2369;&#2332;&#2354;&#2368; &#2325;&#2350; &#2361;&#2369;&#2312;, &#2336;&#2368;&#2325; &#2346;&#2381;&#2352;&#2379;&#2337;&#2325;&#2381;&#2335; &#2361;&#2376;"', '"Scalp feels calmer after using this"')

# Hindi Body
body_old = '2 &#2342;&#2367;&#2344; &#2350;&#2375;&#2306; &#2337;&#2367;&#2354;&#2368;&#2357;&#2352;&#2368; &#2310; &#2327;&#2312;&#2404; &#2346;&#2376;&#2325;&#2375;&#2332;&#2367;&#2306;&#2327; &#2348;&#2306;&#2342; &#2341;&#2368;&#2404; &#2325;&#2369;&#2331; &#2348;&#2366;&#2352; &#2311;&#2360;&#2381;&#2340;&#2375;&#2350;&#2366;&#2354; &#2325;&#2352;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2326;&#2379;&#2346;&#2337;&#2368; &#2346;&#2352; &#2326;&#2369;&#2332;&#2354;&#2368; &#2325;&#2350; &#2361;&#2369;&#2312;&#2404; &#2352;&#2370;&#2360;&#2368; &#2349;&#2368; &#2341;&#2379;&#2337;&#2368; &#2325;&#2350; &#2354;&#2327;&#2368;&#2404; &#2325;&#2369;&#2354; &#2350;&#2367;&#2354;&#2366;&#2325;&#2352; &#2336;&#2368;&#2325; &#2361;&#2376;&#2404;'
body_literal = '2 दिन में डिलीवरी आ गई। पैकेजिंग बंद थी। कुछ बार इस्तेमाल करने के बाद खोपड़ी पर खुजली कम हुई। रूसी भी थोड़ी कम लगी। कुल मिलाकर ठीक है।'

c = c.replace(body_old, 'Delivery was quick, came in 2 days. Packaging was sealed properly. After a few washes scalp irritation reduced noticeably. Dandruff also seems less. Decent product.')
c = c.replace(body_literal, 'Delivery was quick, came in 2 days. Packaging was sealed properly. After a few washes scalp irritation reduced noticeably. Dandruff also seems less. Decent product.')

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Naincy Tiwari review updated: English text and DP removed!")
