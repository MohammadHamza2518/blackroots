import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

official_payment_badges_html = """          <div id="MainBuyButton" class="pt-3 pb-2 space-y-3">
            <button type="button" class="js-trigger-order btn-gold-luxury btn-shimmer w-full text-base sm:text-lg font-extrabold py-4 px-6 rounded-2xl shadow-[0_10px_25px_rgba(212,175,55,0.3)] flex items-center justify-center gap-3 transform transition-all hover:scale-[1.02] active:scale-95 cursor-pointer uppercase tracking-wider">
              <span>Buy Now &mdash; &#8377;499.00</span>
              <span class="text-xl font-bold">&rarr;</span>
            </button>

            <!-- ULTRA-PROFESSIONAL OFFICIAL INDIAN PAYMENT BADGES FRAME (DIRECTLY BELOW BUY NOW) -->
            <div class="p-3.5 sm:p-4 rounded-2xl bg-gradient-to-r from-[#12151c] via-[#1a1f2c] to-[#12151c] border-2 border-[#d4af37]/40 shadow-2xl space-y-3">
              <!-- Security Header Bar -->
              <div class="flex items-center justify-between text-[10px] sm:text-[11px] font-extrabold text-gray-300 uppercase tracking-wider px-1">
                <span class="flex items-center gap-1.5 text-amber-300">
                  <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                  <span>Guaranteed Express Checkout</span>
                </span>
                <span class="text-emerald-400 font-extrabold flex items-center gap-1 bg-emerald-500/10 px-2.5 py-0.5 rounded-full border border-emerald-500/30">
                  🔒 256-Bit SSL Secured
                </span>
              </div>

              <!-- Official Indian Payment Badges Graphic -->
              <div class="bg-white/95 rounded-xl p-2.5 shadow-inner border border-white/20 hover:brightness-105 transition-all">
                <img src="./assets/blackroots-payment-badges.png" alt="Accepted Indian Payment Methods: GPay, UPI, PhonePe, COD Cash On Delivery, Paytm" class="w-full h-auto object-contain block mx-auto rounded-lg">
              </div>
            </div>

            <!-- Harmonious Shipping Callout Box -->
            <div class="p-3.5 rounded-2xl bg-white/5 border border-white/10 flex flex-col gap-1.5 text-xs text-gray-300 shadow-sm">
              <div class="flex items-center gap-2.5 text-emerald-400 font-semibold text-[11px]">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                <span>⚡ Free Express Shipping Across India (3-5 Days)</span>
              </div>
              <div class="flex items-center gap-2.5 text-amber-300 font-medium text-[11px] border-t border-white/10 pt-1.5">
                <span>🛡️ 100% Quality Guaranteed &bull; Secure COD Dispatch</span>
              </div>
            </div>
          </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        idx_start = content.find('<div id="MainBuyButton"')
        if idx_start != -1:
            idx_end = content.find('<!-- REAL HUMAN REVIEWS SECTION', idx_start)
            if idx_end != -1:
                last_div = content.rfind('</div>', idx_start, idx_end)
                if last_div != -1:
                    content = content[:idx_start] + official_payment_badges_html + content[last_div + 6:]
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"INTEGRATED OFFICIAL PAYMENT BADGES GRAPHIC IN: {fpath}")

