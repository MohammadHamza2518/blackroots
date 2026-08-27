import os
import glob

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

old_btn_block = """          <div class="pt-2 flex flex-col sm:flex-row items-center justify-between gap-3 border-t border-white/10">
            <span class="text-[11px] text-gray-300">
              🌿 100% Botanical &bull; Zero Ammonia &bull; No Side Effects
            </span>
            <a href="product.html" class="js-trigger-order group relative inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs px-5 py-2.5 rounded-xl border border-[#fff3b0]/70 shadow-md hover:scale-105 transition-all uppercase tracking-wider shrink-0 w-full sm:w-auto text-center">
              <span>ORDER NOW &bull; &#8377;499</span>
              <span class="w-5 h-5 rounded-lg bg-black text-[#d4af37] flex items-center justify-center font-bold text-xs">
                &rarr;
              </span>
            </a>
          </div>"""

new_btn_block = """          <div class="pt-3 flex flex-col sm:flex-row items-center justify-between gap-3 border-t border-white/10">
            <span class="text-[11px] text-gray-300">
              🌿 100% Botanical &bull; Zero Ammonia &bull; No Side Effects
            </span>
            <a href="product.html" class="js-trigger-order group relative inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs sm:text-sm px-6 py-3 rounded-xl border border-[#fff3b0]/70 shadow-[0_10px_25px_rgba(212,175,55,0.25)] hover:shadow-[0_15px_35px_rgba(212,175,55,0.4)] transition-all transform hover:-translate-y-0.5 uppercase tracking-wider overflow-hidden w-full sm:w-auto text-center">
              <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/40 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-out pointer-events-none"></span>
              <span class="flex items-center gap-2 relative z-10">
                <span class="font-black tracking-wider">ORDER NOW</span>
                <span class="text-black/40 font-normal">&bull;</span>
                <span class="font-black text-sm text-black">&#8377;499</span>
              </span>
              <span class="w-6 h-6 rounded-lg bg-black text-[#d4af37] flex items-center justify-center shadow-md shrink-0 relative z-10 group-hover:scale-110 transition-transform">
                <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
              </span>
            </a>
          </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_btn_block in content:
            content = content.replace(old_btn_block, new_btn_block)
        else:
            # Fallback replacement
            s_idx = content.find('SimpleResultText')
            if s_idx != -1:
                b_start = content.find('<div class="pt-2 flex flex-col', s_idx)
                b_end = content.find('</a>', b_start) + 10
                div_close = content.find('</div>', b_end) + 6
                if b_start != -1 and div_close != -1:
                    content = content[:b_start] + new_btn_block.strip() + content[div_close:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED CALCULATOR ORDER BUTTON IN: {fpath}")
