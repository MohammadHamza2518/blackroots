import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

new_unisex_badge = """      <!-- Top Tagline Pill (Ultra-Luxury D2C Single-Line Responsive Badge with Unisex Icon) -->
      <div class="inline-flex items-center justify-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/10 border border-[#d4af37]/50 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-wide backdrop-blur-xl shadow-[0_10px_25px_rgba(212,175,55,0.15)] mx-auto">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></span>
        <span>👫 100% UNISEX FORMULA &bull; JAPANESE BOTANICAL HAIR RITUAL</span>
      </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('UNISEX FORMULA')
        if s_idx != -1:
            b_start = content.rfind('<div class="inline-flex', 0, s_idx)
            b_end = content.find('</div>', s_idx) + 6
            if b_start != -1 and b_end != -1:
                content = content[:b_start] + new_unisex_badge.strip() + content[b_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"RESTORED UNISEX ICON IN HERO BADGE IN: {fpath}")
