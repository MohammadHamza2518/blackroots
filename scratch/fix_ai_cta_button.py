import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

ai_files = [
    os.path.join(root_dir, "ai-consultant.html"),
    os.path.join(root_dir, "demo_lab", "ai-consultant.html"),
    os.path.join(root_dir, "preview", "ai-consultant.html"),
    os.path.join(root_dir, "assets", "theme.js"),
    os.path.join(root_dir, "demo_lab", "assets", "theme.js"),
    os.path.join(root_dir, "preview", "assets", "theme.js")
]

# Clean CTA texts and button markup
replacements = [
    ('🛍️ Order BlackRoots 250ml — ₹499 (Free COD)', '🛍️ Order BlackRoots • ₹499'),
    ('🛍️ Order BlackRoots 250ml — ₹499', '🛍️ Order BlackRoots • ₹499'),
    ('🛍️ Buy BlackRoots Now — ₹499 Only', '🛍️ Buy BlackRoots • ₹499'),
    ('🛍️ Buy BlackRoots (₹499)', '🛍️ Buy BlackRoots • ₹499'),
    ('🛍️ Order Now — ₹499 (Free COD)', '🛍️ Order Now • ₹499'),
    ('🧔 Get Beard & Scalp Care — ₹499', '🧔 Order Beard & Hair Care • ₹499'),
    ('🧔 Get Beard & Scalp Care (₹499)', '🧔 Order Beard & Hair Care • ₹499'),
    ('✨ Stop Hair Fall — Order ₹499', '✨ Stop Hair Fall • Order ₹499'),
    ('🚿 View Live 3-Min Scalp Timer', '🚿 3-Min Scalp Timer Ritual'),
    ('🌿 View Herbal Ingredients Details', '🌿 View Botanical Ingredients'),
    ('🌿 Explore Herbal Ingredients', '🌿 View Botanical Ingredients')
]

for fpath in ai_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    for old_txt, new_txt in replacements:
        new_content = new_content.replace(old_txt, new_txt)

    # Clean CTA button container markup in streamDoctorResponse
    new_content = re.sub(
        r'<div class="pt-2">\s*<a href="\$\{resData\.ctaLink\}" class="inline-flex items-center gap-1\.5 bg-gradient-to-r from-\[#d4af37\] via-\[#f7e7a7\] to-\[#aa7c11\] text-black font-black text-xs px-4 py-2\.5 rounded-xl shadow-lg hover:scale-105 transition-all uppercase tracking-tight">\s*<span>\$\{resData\.ctaText\}<\/span>\s*<span>&rarr;<\/span>\s*<\/a>\s*<\/div>',
        r'<div class="pt-2"><a href="${resData.ctaLink}" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs px-4 py-3 rounded-xl shadow-md hover:brightness-110 active:scale-95 transition-all text-center tracking-normal"><span>${resData.ctaText}</span> <span class="font-black">&rarr;</span></a></div>',
        new_content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated button in", fpath)

