import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

old_button_snippet = 'Buy Now (250ml Bottle)'

new_button_html = """        <button type="button" class="js-trigger-order group relative inline-flex items-center justify-between gap-3.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs sm:text-sm px-6 py-3.5 sm:px-8 sm:py-4 rounded-2xl border-2 border-[#fff3b0]/60 shadow-[0_15px_35px_rgba(212,175,55,0.35)] hover:shadow-[0_20px_45px_rgba(212,175,55,0.5)] transition-all transform hover:-translate-y-0.5 cursor-pointer uppercase tracking-wider overflow-hidden">
          <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/40 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-out pointer-events-none"></span>
          <span class="flex items-center gap-2 relative z-10">
            <span>Buy Now (250ml Bottle)</span>
            <span class="text-black/40 font-normal">&bull;</span>
            <span class="font-black text-sm text-black">&#8377;499.00</span>
          </span>
          <span class="w-7 h-7 sm:w-8 sm:h-8 rounded-xl bg-black text-[#d4af37] flex items-center justify-center font-black text-xs sm:text-sm shadow-md shrink-0 relative z-10 group-hover:scale-110 transition-transform">
            &rarr;
          </span>
        </button>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('Buy Now (250ml Bottle) &mdash;')
        if s_idx != -1:
            b_start = content.rfind('<button', 0, s_idx)
            b_end = content.find('</button>', s_idx) + 9
            if b_start != -1 and b_end != -1:
                content = content[:b_start] + new_button_html.strip() + content[b_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED HERO BUY NOW CTA BUTTON IN: {fpath}")
