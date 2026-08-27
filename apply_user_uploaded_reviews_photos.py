import os, shutil

src_ananya = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786623839369.jpg"
src_anjali = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786623863927.jpg"

dest_ananya = r"c:\Users\moham\Downloads\blackroots website\assets\reviews\ananya-dubey-result.jpg"
dest_anjali = r"c:\Users\moham\Downloads\blackroots website\assets\reviews\anjali-singh-result.jpg"

shutil.copy2(src_ananya, dest_ananya)
shutil.copy2(src_anjali, dest_anjali)
print(f"COPIED ANANYA PHOTO TO: {dest_ananya}")
print(f"COPIED ANJALI PHOTO TO: {dest_anjali}")

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Ananya Dubey Card
        ananya_old = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Mummy ke liye liya, unhe bhi pasand aaya"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Mummy ke liye order kiya tha. Wo chemical wali dye nahi lagati thi. Isse try karaya, 4&ndash;5 washes mein unke greys kaafi cover ho gaye. Ab wo khud mangwa rahi hain.</p>"""

        ananya_new = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Mummy ke liye liya, unhe bhi pasand aaya"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Mummy ke liye order kiya tha. Wo chemical wali dye nahi lagati thi. Isse try karaya, 4&ndash;5 washes mein unke greys kaafi cover ho gaye. Ab wo khud mangwa rahi hain.</p>
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;"><img src="./assets/reviews/ananya-dubey-result.jpg" alt="Ananya Dubey Hair Result Photo" class="w-full h-full object-cover object-center"></div>"""

        if "Mummy ke liye liya, unhe bhi pasand aaya" in content and "ananya-dubey-result.jpg" not in content:
            content = content.replace(ananya_old, ananya_new)

        # Update Anjali Singh Card
        anjali_old = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Finally something that doesn't damage hair"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone. Very satisfied.</p>"""
        
        anjali_old_2 = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Finally something that doesn't damage hair"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone now. Smell is herbal which I personally like.</p>"""

        anjali_new = """            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Finally something that doesn't damage hair"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone now. Smell is herbal which I personally like.</p>
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;"><img src="./assets/reviews/anjali-singh-result.jpg" alt="Anjali Singh Hair Result Photo" class="w-full h-full object-cover object-center"></div>"""

        if "Finally something that doesn't damage hair" in content:
            if "review-photo-10.jpg" in content:
                content = content.replace("./assets/reviews/review-photo-10.jpg", "./assets/reviews/anjali-singh-result.jpg")
            else:
                content = content.replace(anjali_old, anjali_new)
                content = content.replace(anjali_old_2, anjali_new)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED UPLOADED PHOTOS TO: {fpath}")

