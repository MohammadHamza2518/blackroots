import re

def fix_dps(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tariq Siddiqui
    ts_old = '<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/custom-avatar-11.jpg" alt="Tariq Siddiqui" class="w-full h-full rounded-full object-cover"></div>'
    ts_new = '<div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">TS</div>'
    content = content.replace(ts_old, ts_new)

    # Sunita Verma
    sv_old = '<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/custom-avatar-12.jpg" alt="Sunita Verma" class="w-full h-full rounded-full object-cover"></div>'
    sv_new = '<div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">SV</div>'
    content = content.replace(sv_old, sv_new)

    # Rajesh K. Verma
    rk_old = '<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="./assets/reviews/custom-avatar-3.jpg" alt="Rajesh K. Verma" class="w-full h-full rounded-full object-cover"></div>'
    rk_new = '<div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">RK</div>'
    content = content.replace(rk_old, rk_new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated DPs in {filepath}')

fix_dps('demo_lab/reviews.html')
fix_dps('reviews.html')
fix_dps('preview/reviews.html')
