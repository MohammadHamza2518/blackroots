import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"
index_files = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html")
]

for fpath in index_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update Card 5 Top Badge to clean uniform style (remove green dot and 360 text)
        old_card5_badge = r'<div class="absolute top-3\.5 left-3\.5 right-3\.5 z-30 flex items-center justify-between pointer-events-none gap-2">\s*<span class="bg-black/90 backdrop-blur-md text-amber-300 border border-\[#d4af37\]/70 text-\[9px\] sm:text-\[10px\] font-black uppercase px-3 py-1 rounded-full shadow-xl flex items-center gap-1\.5">\s*<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"><\/span>\s*<span>✨ 360° STUDIO VIEW<\/span>\s*<\/span>'
        
        new_card5_badge = """<div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                🌿 100% Herbal Active
              </span>"""

        content = re.sub(old_card5_badge, new_card5_badge, content)

        # In case regex doesn't catch exact whitespace:
        content = content.replace(
            '<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>\n                <span>✨ 360° STUDIO VIEW</span>',
            '<span>🌿 100% Herbal Active</span>'
        )
        content = content.replace(
            '<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>\n                <span>✨ 360 STUDIO VIEW</span>',
            '<span>🌿 100% Herbal Active</span>'
        )
        content = content.replace('✨ 360° STUDIO VIEW', '🌿 100% Herbal Active')
        content = content.replace('✨ 360 STUDIO VIEW', '🌿 100% Herbal Active')

        # 2. Update Card 5 bottom title to sensible natural text
        content = content.replace(
            '<h4 class="text-[10px] font-extrabold text-white truncate">Roots Reborn Black</h4>',
            '<h4 class="text-[10px] font-extrabold text-white truncate">Easy 10-Min Application</h4>'
        )

        # 3. Update Section Tagline Pill from "360° STUDIO SHOWCASE" to clean "OFFICIAL CUSTOMER REELS"
        content = content.replace('🎬 360° STUDIO SHOWCASE &bull; OFFICIAL REELS', '🎬 REAL CUSTOMER REELS &bull; VERIFIED RESULTS')
        content = content.replace('🎬 360 STUDIO SHOWCASE &bull; OFFICIAL REELS', '🎬 REAL CUSTOMER REELS &bull; VERIFIED RESULTS')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEANED AND STANDARDIZED BADGES IN: {fpath}")
