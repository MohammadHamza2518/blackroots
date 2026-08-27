import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

clean_buy_section = """          <div id="MainBuyButton" class="pt-3 pb-2 space-y-3">
            <!-- ULTRA-LUXURY 3D CONVERSION BUY NOW BUTTON -->
            <button type="button" class="js-trigger-order relative overflow-hidden w-full bg-gradient-to-r from-amber-300 via-[#d4af37] to-amber-500 hover:from-amber-200 hover:via-amber-400 hover:to-amber-600 text-black font-extrabold py-3.5 px-5 rounded-2xl shadow-[0_10px_30px_rgba(212,175,55,0.4)] hover:shadow-[0_15px_40px_rgba(252,211,77,0.6)] flex items-center justify-between transition-all duration-300 transform hover:-translate-y-0.5 active:translate-y-0 cursor-pointer uppercase tracking-wider group border-2 border-amber-100/60">
              
              <!-- Sweeping Shimmer Light Sheen Effect -->
              <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/60 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-in-out pointer-events-none"></div>

              <!-- Left: Flash Express Badge -->
              <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-xl bg-black/15 flex items-center justify-center text-black text-sm font-bold shadow-inner group-hover:scale-110 transition-transform">
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
            </button>

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
                    content = content[:idx_start] + clean_buy_section + content[last_div + 6:]
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"CLEANLY REPLACED MAIN BUY BUTTON & PILL BADGES IN: {fpath}")

