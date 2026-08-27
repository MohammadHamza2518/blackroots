import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

target_old_btn = '<button type="button" class="js-trigger-order btn-gold-luxury btn-shimmer w-full text-center">Buy Now (250ml Bottle &mdash; &#8377;499.00) &rarr;</button>'

compact_formulation_button = """<button type="button" class="js-trigger-order group relative inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs sm:text-sm px-6 py-3 rounded-xl border border-[#fff3b0]/70 shadow-[0_10px_25px_rgba(212,175,55,0.25)] hover:shadow-[0_15px_35px_rgba(212,175,55,0.4)] transition-all transform hover:-translate-y-0.5 cursor-pointer uppercase tracking-wider overflow-hidden w-full sm:w-auto">
              <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/40 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-out pointer-events-none"></span>
              <span class="flex items-center gap-2 relative z-10">
                <span class="font-black tracking-wider">ORDER NOW</span>
                <span class="text-black/40 font-normal">&bull;</span>
                <span class="font-black text-sm text-black">&#8377;499</span>
              </span>
              <span class="w-6 h-6 rounded-lg bg-black text-[#d4af37] flex items-center justify-center shadow-md shrink-0 relative z-10 group-hover:scale-110 transition-transform">
                <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
              </span>
            </button>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if target_old_btn in content:
            content = content.replace(target_old_btn, compact_formulation_button)
        else:
            s_idx = content.find('Restores Hair Melanin')
            if s_idx != -1:
                b_start = content.find('<button', s_idx)
                b_end = content.find('</button>', s_idx) + 9
                if b_start != -1 and b_end != -1:
                    content = content[:b_start] + compact_formulation_button + content[b_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REPLACED FORMULATION BUTTON IN: {fpath}")
