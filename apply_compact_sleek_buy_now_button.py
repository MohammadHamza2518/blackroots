import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

compact_sleek_button_html = """        <button type="button" class="js-trigger-order group relative inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs sm:text-sm px-6 py-3 rounded-xl border border-[#fff3b0]/70 shadow-[0_10px_25px_rgba(212,175,55,0.25)] hover:shadow-[0_15px_35px_rgba(212,175,55,0.4)] transition-all transform hover:-translate-y-0.5 cursor-pointer uppercase tracking-wider overflow-hidden">
          <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/40 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-out pointer-events-none"></span>
          <span class="flex items-center gap-2 relative z-10">
            <span class="font-black tracking-wider">ORDER NOW</span>
            <span class="text-black/40 font-normal">&bull;</span>
            <span class="font-black text-sm text-black">&#8377;499</span>
          </span>
          <span class="w-6 h-6 rounded-lg bg-black text-[#d4af37] flex items-center justify-center font-black text-xs shadow-md shrink-0 relative z-10 group-hover:scale-110 transition-transform">
            &rarr;
          </span>
        </button>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('Buy Now (250ml')
        if s_idx == -1:
            s_idx = content.find('js-trigger-order group relative')
            if s_idx == -1:
                s_idx = content.find('ORDER NOW')

        if s_idx != -1:
            b_start = content.rfind('<button', 0, s_idx)
            b_end = content.find('</button>', s_idx) + 9
            if b_start != -1 and b_end != -1:
                content = content[:b_start] + compact_sleek_button_html.strip() + content[b_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED COMPACT SLEEK BUTTON IN: {fpath}")
