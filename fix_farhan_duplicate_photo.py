import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

farhan_old_photo = 'src="./assets/reviews/farhan-bottle-photo.jpg"'
farhan_new_photo = 'src="./assets/reviews/review-photo-4.jpg"'

# We also assign unique photos to text-only cards so every card in the deck has its own distinct photo proof
kavya_old_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"My grey roots blended so naturally"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Using it for about 3 weeks now. The grey roots are much less visible. Hair doesn't feel dry. I actually look forward to wash days now. Good purchase.</p>"""

kavya_new_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"My grey roots blended so naturally"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Using it for about 3 weeks now. The grey roots are much less visible. Hair doesn't feel dry. I actually look forward to wash days now. Good purchase.</p>
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;"><img src="./assets/reviews/review-photo-6.jpg" alt="Customer Photo" class="w-full h-full object-cover object-center"></div>"""

anjali_old_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Finally something that doesn't damage hair"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone. Very satisfied.</p>"""

anjali_new_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Finally something that doesn't damage hair"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone. Very satisfied.</p>
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;"><img src="./assets/reviews/review-photo-10.jpg" alt="Customer Photo" class="w-full h-full object-cover object-center"></div>"""

ameena_old_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Sweekar ke liye, ache bhagwan!"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Hair dye use karke pareshan ho chuki thi. Ab ye use kar rahi hu 4 washes me grey cover ho gaya. Sickness worry khataam ho gayi.</p>"""

ameena_new_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Sweekar ke liye, ache bhagwan!"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Hair dye use karke pareshan ho chuki thi. Ab ye use kar rahi hu 4 washes me grey cover ho gaya. Sickness worry khataam ho gayi.</p>
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;"><img src="./assets/reviews/face-photo-4.jpg" alt="Customer Photo" class="w-full h-full object-cover object-center"></div>"""

ritu_old_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"4 &#2348;&#2366;&#2352; &#2343;&#2379;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2332;&#2921;&#2368;&#2306; &#2325;&#2366;&#2354;&#2368; &#2361;&#2379; &#2327;&#2312;&#2306;"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">&#2341;&#2379;&#2322;&#2368; &#2313;&#2350;&#2381;&#2350;&#2368;&#2342; &#2325;&#2375; &#2360;&#2366;&#2341; &#2350;&#2306;&#2327;&#2364;&#2366;&#2351;&#2366; &#2341;&#2366;&#2404; 4 &#2348;&#2366;&#2352; &#2343;&#2379;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2332;&#2921;&#2379;&#2306; &#2350;&#2375;&#2306; &#2347;&#2364;&#2352;&#2381;&#2325;&#2364; &#2342;&#2367;&#2326;&#2344;&#2375; &#2354;&#2327;&#2366;&#2404; &#2326;&#2379;&#2346;&#2322;&#2368; &#2346;&#2352; &#2325;&#2379;&#2312; &#2332;&#2354;&#2344; &#2344;&#2361;&#2368;&#2306; &#2361;&#2369;&#2312;&#2404; &#2341;&#2379;&#2322;&#2366; &#2360;&#2350;&#2351; &#2354;&#2327;&#2340;&#2366; &#2361;&#2376; &#2346;&#2352; &#2325;&#2366;&#2350; &#2325;&#2352;&#2340;&#2366; &#2361;&#2376;&#2404;</p>"""

ritu_new_card = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"4 &#2348;&#2366;&#2352; &#2343;&#2379;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2332;&#2921;&#2368;&#2306; &#2325;&#2366;&#2354;&#2368; &#2361;&#2379; &#2327;&#2312;&#2306;"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">&#2341;&#2379;&#2322;&#2368; &#2313;&#2350;&#2381;&#2350;&#2368;&#2342; &#2325;&#2375; &#2360;&#2366;&#2341; &#2350;&#2306;&#2327;&#2364;&#2366;&#2351;&#2366; &#2341;&#2366;&#2404; 4 &#2348;&#2366;&#2352; &#2343;&#2379;&#2344;&#2375; &#2325;&#2375; &#2348;&#2366;&#2342; &#2332;&#2921;&#2379;&#2306; &#2350;&#2375;&#2306; &#2347;&#2364;&#2352;&#2381;&#2325;&#2364; &#2342;&#2367;&#2326;&#2344;&#2375; &#2354;&#2327;&#2366;&#2404; &#2326;&#2379;&#2346;&#2322;&#2368; &#2346;&#2352; &#2325;&#2379;&#2312; &#2332;&#2354;&#2344; &#2344;&#2361;&#2368;&#2306; &#2361;&#2369;&#2312;&#2404; &#2341;&#2379;&#2322;&#2366; &#2360;&#2350;&#2351; &#2354;&#2327;&#2340;&#2366; &#2361;&#2376; &#2346;&#2352; &#2325;&#2366;&#2350; &#2325;&#2352;&#2340;&#2366; &#2361;&#2376;&#2404;</p>
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;"><img src="./assets/reviews/review-photo-9.jpg" alt="Customer Photo" class="w-full h-full object-cover object-center"></div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace(farhan_old_photo, farhan_new_photo)
        content = content.replace(kavya_old_card, kavya_new_card)
        content = content.replace(anjali_old_card, anjali_new_card)
        content = content.replace(ameena_old_card, ameena_new_card)
        content = content.replace(ritu_old_card, ritu_new_card)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REPLACED DUPLICATE FARHAN PHOTO & ASSIGNED UNIQUE PHOTOS IN: {fpath}")

