import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

new_buynow_html = """            <!-- ULTRA-LUXURY 3D CONVERSION BUY NOW BUTTON -->
            <button type="button" class="js-trigger-order relative overflow-hidden w-full bg-gradient-to-r from-amber-300 via-[#d4af37] to-amber-500 hover:from-amber-200 hover:via-amber-400 hover:to-amber-600 text-black font-extrabold py-3.5 px-5 rounded-2xl shadow-[0_8px_30px_rgba(212,175,55,0.4)] hover:shadow-[0_12px_40px_rgba(252,211,77,0.6)] flex items-center justify-between transition-all duration-300 transform hover:-translate-y-0.5 active:translate-y-0 cursor-pointer uppercase tracking-wider group border-2 border-amber-200/60">
              
              <!-- Sweeping Shimmer Light Effect -->
              <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/50 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-in-out pointer-events-none"></div>

              <!-- Left: Flash Express Icon -->
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-black/15 flex items-center justify-center text-black text-sm shadow-inner group-hover:scale-110 transition-transform">
                  ⚡
                </span>
              </div>

              <!-- Center: CTA Text & Sub-trust -->
              <div class="text-center flex flex-col items-center">
                <span class="text-base sm:text-lg font-black tracking-widest text-black flex items-center gap-2">
                  BUY NOW &mdash; <span id="BuyButtonPriceDisplay">&#8377;499.00</span>
                </span>
                <span class="text-[10px] font-extrabold text-black/80 tracking-wider uppercase -mt-0.5">
                  Instant Order &bull; Free Express COD
                </span>
              </div>

              <!-- Right: Animated Arrow Icon -->
              <div class="w-8 h-8 rounded-xl bg-black/15 flex items-center justify-center text-black font-black text-base shadow-inner group-hover:translate-x-1 transition-transform">
                &rarr;
              </div>
            </button>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find button in MainBuyButton container
        idx_start = content.find('<button type="button" class="js-trigger-order')
        if idx_start != -1:
            idx_end = content.find('</button>', idx_start)
            if idx_end != -1:
                content = content[:idx_start] + new_buynow_html + content[idx_end + 9:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"REDESIGNED ULTRA-LUXURY BUY NOW BUTTON IN: {fpath}")

