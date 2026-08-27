import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

uniform_trust_grid_html = """      <!-- Uniform Luxury Trust Badges Grid (100% Symmetrical & Harmonious) -->
      <div class="pt-8 border-t border-white/10 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 text-xs font-semibold text-gray-200 max-w-5xl mx-auto">
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/[0.04] border border-[#d4af37]/30 text-center text-gray-200 shadow-md backdrop-blur-md">
          <span class="text-amber-300 font-black">✓</span> <span>100% Natural</span>
        </div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/[0.04] border border-[#d4af37]/30 text-center text-gray-200 shadow-md backdrop-blur-md">
          <span class="text-amber-300 font-black">✓</span> <span>0% Ammonia</span>
        </div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/[0.04] border border-[#d4af37]/30 text-center text-gray-200 shadow-md backdrop-blur-md">
          <span>🛡️</span> <span>Derm Tested</span>
        </div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/[0.04] border border-[#d4af37]/30 text-center text-gray-200 shadow-md backdrop-blur-md">
          <span>👫</span> <span>Men & Women</span>
        </div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/[0.04] border border-[#d4af37]/30 text-center text-gray-200 shadow-md backdrop-blur-md">
          <span>🌿</span> <span>Cruelty Free</span>
        </div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/[0.04] border border-[#d4af37]/30 text-center text-gray-200 shadow-md backdrop-blur-md">
          <span>⚡</span> <span>10-Day Action</span>
        </div>
      </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        g_start = content.find('<div class="pt-8 border-t border-white/10 grid grid-cols-2')
        if g_start != -1:
            g_end = content.find('</div>\n\n    </div>', g_start)
            if g_end == -1:
                g_end = content.find('</div>\r\n\r\n    </div>', g_start)
            if g_end == -1:
                g_end = content.find('</div>\n  </section>', g_start)

            if g_end != -1:
                content = content[:g_start] + uniform_trust_grid_html + content[g_end:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UNIFIED TRUST BADGES IN: {fpath}")
