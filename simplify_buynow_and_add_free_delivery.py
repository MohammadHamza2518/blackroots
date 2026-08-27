import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

clean_buynow_with_free_delivery_html = """          <div id="MainBuyButton" class="pt-3 pb-2 space-y-3">
            <!-- CLEAN HIGH-CONVERTING BUY NOW BUTTON -->
            <button type="button" class="js-trigger-order btn-gold-luxury btn-shimmer w-full text-base sm:text-lg font-extrabold py-4 px-6 rounded-2xl shadow-[0_10px_25px_rgba(212,175,55,0.35)] flex items-center justify-center gap-3 transform transition-all hover:scale-[1.02] active:scale-95 cursor-pointer uppercase tracking-wider">
              <span>BUY NOW &mdash; <span id="BuyButtonPriceDisplay">&#8377;499.00</span></span>
              <span class="text-xl font-bold">&rarr;</span>
            </button>

            <!-- SLEEK FREE DELIVERY TRUST BADGE (DIRECTLY BELOW BUY NOW BUTTON) -->
            <div class="flex items-center justify-center gap-2 text-center text-xs font-extrabold text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 rounded-xl py-2.5 px-4 shadow-md">
              <span class="text-sm">🚚</span>
              <span>FREE Express Delivery Across India &bull; Cash On Delivery Available</span>
            </div>

            <!-- ULTRA-CLEAN CODE-RENDERED INDIAN PAYMENT PILL BADGES (COMPACT & LUXURIOUS) -->
            <div class="p-3 rounded-2xl bg-[#12151c]/90 border border-[#d4af37]/40 shadow-xl space-y-2">
              
              <!-- Security Subhead -->
              <div class="flex items-center justify-between text-[10px] font-extrabold uppercase tracking-wider px-1">
                <span class="flex items-center gap-1.5 text-amber-300">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span>Guaranteed Safe & Secure Checkout</span>
                </span>
                <span class="text-emerald-400 font-extrabold flex items-center gap-1">
                  🔒 256-Bit SSL
                </span>
              </div>

              <!-- Sleek Compact 5-Pill Payment Strip -->
              <div class="grid grid-cols-5 gap-1.5 items-center text-center">
                
                <!-- 1. GPay Pill -->
                <div class="bg-white border border-gray-200 rounded-lg py-1.5 px-1 shadow-sm flex items-center justify-center hover:scale-105 transition-transform cursor-default">
                  <span class="font-extrabold text-[11px] tracking-tight bg-gradient-to-r from-blue-600 via-red-500 to-amber-500 bg-clip-text text-transparent">GPay</span>
                </div>

                <!-- 2. PhonePe Pill -->
                <div class="bg-[#5f259f] rounded-lg py-1.5 px-1 shadow-sm flex items-center justify-center hover:scale-105 transition-transform cursor-default">
                  <span class="font-extrabold text-[11px] text-white tracking-tight">PhonePe</span>
                </div>

                <!-- 3. Paytm Pill -->
                <div class="bg-[#00baf2] rounded-lg py-1.5 px-1 shadow-sm flex items-center justify-center hover:scale-105 transition-transform cursor-default">
                  <span class="font-extrabold text-[11px] text-white tracking-tight">Paytm</span>
                </div>

                <!-- 4. UPI Pill -->
                <div class="bg-white border border-gray-300 rounded-lg py-1.5 px-1 shadow-sm flex items-center justify-center gap-1 hover:scale-105 transition-transform cursor-default">
                  <span class="font-black text-[11px] text-gray-800 tracking-tighter">UPI</span>
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                </div>

                <!-- 5. COD Pill -->
                <div class="bg-gradient-to-r from-amber-500 to-amber-600 rounded-lg py-1.5 px-1 shadow-sm flex items-center justify-center hover:scale-105 transition-transform cursor-default">
                  <span class="font-black text-[11px] text-black tracking-wider uppercase">🚚 COD</span>
                </div>

              </div>
            </div>

            <!-- Harmonious Quality Guarantee Box -->
            <div class="p-3 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center gap-2 text-xs text-amber-300 font-medium shadow-sm">
              <span>🛡️ 100% Herbal Quality Guaranteed &bull; Fast 3–5 Days Dispatch</span>
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
                    content = content[:idx_start] + clean_buynow_with_free_delivery_html + content[last_div + 6:]
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"SIMPLIFIED BUY NOW AND ADDED FREE DELIVERY STRIP IN: {fpath}")

