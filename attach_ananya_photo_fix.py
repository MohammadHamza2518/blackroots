import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

target_text = '<p class="text-xs text-gray-300 leading-relaxed font-light">Mummy ke liye order kiya tha. Wo chemical wali dye nahi lagati thi. Isse try karaya, 4-5 washes mein unke greys kaafi cover ho gaye. Ab wo khud mangwa rahi hain.</p>'

replacement_text = """<p class="text-xs text-gray-300 leading-relaxed font-light">Mummy ke liye order kiya tha. Wo chemical wali dye nahi lagati thi. Isse try karaya, 4-5 washes mein unke greys kaafi cover ho gaye. Ab wo khud mangwa rahi hain.</p>
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;"><img src="./assets/reviews/ananya-dubey-result.jpg" alt="Ananya Dubey Hair Result Photo" class="w-full h-full object-cover object-center"></div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if "ananya-dubey-result.jpg" not in content:
            content = content.replace(target_text, replacement_text)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"ATTACHED ANANYA PHOTO IN: {fpath}")

