import os

target_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

new_trust_grid_html = """      <div class="pt-8 border-t border-white/10 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 text-xs font-semibold text-gray-300 max-w-5xl mx-auto">
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">✓ 100% Natural</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">✓ 0% Ammonia</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">🛡️ Derm Tested</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-amber-400/10 border border-amber-400/30 text-amber-300 font-bold text-center">👫 Men & Women</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">🌿 Cruelty Free</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold text-center">⚡ 10-Day Action</div>
      </div>"""

new_tagline_badge_html = """      <!-- Tagline Badges & Headings -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/15 border border-[#d4af37]/40 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-widest mb-4 backdrop-blur-md shadow-lg">
        <span>✨ REAL 10-DAY NATURAL TRANSFORMATION &bull; 100% ORGANIC</span>
      </div>"""

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Trust Grid
        g_start = content.find('<div class="pt-8 border-t border-white/10 grid grid-cols-2')
        if g_start != -1:
            g_end = content.find('</div>\n\n    </div>', g_start)
            if g_end == -1:
                g_end = content.find('</div>\r\n\r\n    </div>', g_start)
            if g_end != -1:
                content = content[:g_start] + new_trust_grid_html + content[g_end+6:]

        # Update Tagline Badge
        b_start = content.find('<!-- Tagline Badges & Headings -->')
        if b_start != -1:
            b_end = content.find('<h2 class="font-serif', b_start)
            if b_end != -1:
                content = content[:b_start] + new_tagline_badge_html + "\n\n      " + content[b_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED TRUST BADGES AND TAGLINE BADGE IN: {fpath}")
