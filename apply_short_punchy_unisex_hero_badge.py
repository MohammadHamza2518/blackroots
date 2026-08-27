import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

short_punchy_badge = """      <!-- Top Tagline Pill (Compact 1-Line Responsive D2C Luxury Badge) -->
      <div class="inline-flex items-center justify-center gap-1.5 px-3.5 py-1.5 rounded-full bg-[#d4af37]/10 border border-[#d4af37]/50 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-wide backdrop-blur-xl shadow-[0_10px_25px_rgba(212,175,55,0.15)] mx-auto text-center max-w-full">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></span>
        <span class="whitespace-nowrap">👫 100% UNISEX &bull; JAPANESE BOTANICAL FORMULA</span>
      </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('UNISEX')
        if s_idx != -1:
            b_start = content.rfind('<div class="inline-flex', 0, s_idx)
            b_end = content.find('</div>', s_idx) + 6
            if b_start != -1 and b_end != -1:
                content = content[:b_start] + short_punchy_badge.strip() + content[b_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED SHORT PUNCHY HERO BADGE IN: {fpath}")
