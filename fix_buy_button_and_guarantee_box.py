import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_buy_stack = """          <div id="MainBuyButton" class="space-y-3 pt-2">
            <button type="button" class="js-trigger-order btn-gold-luxury btn-shimmer w-full text-base py-4 shadow-2xl flex items-center justify-center gap-2">
              <span>Buy Now &mdash; &#8377;499.00</span>
              &rarr;
            </button>
          </div>

          <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2 text-xs text-gray-300">
            <div class="flex items-center gap-2 text-emerald-400">⚡ Free Express Shipping Across India (3-5 Days)</div>
            <div class="flex items-center gap-2 text-amber-300">🛡️ 100% Quality Guaranteed &bull; Secure Dispatch</div>
          </div>"""

new_buy_stack = """          <div id="MainBuyButton" class="pt-3 pb-2 space-y-3">
            <button type="button" class="js-trigger-order btn-gold-luxury btn-shimmer w-full text-base sm:text-lg font-extrabold py-4 px-6 rounded-2xl shadow-[0_10px_25px_rgba(212,175,55,0.3)] flex items-center justify-center gap-3 transform transition-all hover:scale-[1.02] active:scale-95 cursor-pointer uppercase tracking-wider">
              <span>Buy Now &mdash; &#8377;499.00</span>
              <span class="text-xl font-bold">&rarr;</span>
            </button>

            <!-- Harmonious Luxury Callout Box -->
            <div class="p-4 rounded-2xl bg-white/5 border border-white/10 flex flex-col gap-2 text-xs text-gray-300 shadow-md">
              <div class="flex items-center gap-2.5 text-emerald-400 font-semibold">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>⚡ Free Express Shipping Across India (3-5 Days)</span>
              </div>
              <div class="flex items-center gap-2.5 text-amber-300 font-medium border-t border-white/10 pt-2">
                <span>🛡️ 100% Quality Guaranteed &bull; Secure COD Dispatch</span>
              </div>
            </div>
          </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_buy_stack in content:
            content = content.replace(old_buy_stack, new_buy_stack)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED BUY BUTTON & GUARANTEE BOX STACK IN: {fpath}")

