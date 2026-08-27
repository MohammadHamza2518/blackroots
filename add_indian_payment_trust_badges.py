import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

payment_badges_html = """
            <!-- High-Converting Indian Payment Trust Badges Box -->
            <div class="p-4 rounded-2xl bg-[#12151c]/90 border border-[#d4af37]/40 shadow-xl space-y-3">
              <div class="flex items-center justify-between text-[11px] font-bold text-gray-300 uppercase tracking-wider">
                <span class="flex items-center gap-1.5 text-amber-300">
                  <svg class="w-4 h-4 text-emerald-400" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M2.166 4.999A2.396 2.396 0 014.563 2.6h10.874a2.396 2.396 0 012.397 2.399v10.002a2.396 2.396 0 01-2.397 2.399H4.563a2.396 2.396 0 01-2.397-2.399V4.999zm2.397-.799a.799.799 0 00-.799.799v10.002c0 .441.358.799.799.799h10.874c.441 0 .799-.358.799-.799V4.999a.799.799 0 00-.799-.799H4.563z" clip-rule="evenodd"/>
                  </svg>
                  Guaranteed Safe & Secure Checkout
                </span>
                <span class="text-[10px] text-emerald-400 font-extrabold bg-emerald-500/20 px-2 py-0.5 rounded-full border border-emerald-500/30">256-BIT SSL</span>
              </div>

              <!-- Sleek Indian Payment Badges Grid -->
              <div class="grid grid-cols-5 gap-2 items-center text-center pt-1">
                <!-- Badge 1: UPI -->
                <div class="bg-[#0a0b0e] border border-white/10 rounded-xl p-2 flex flex-col items-center justify-center hover:border-amber-400/50 transition-all group shadow-inner">
                  <span class="text-xs font-black text-emerald-400 tracking-tighter group-hover:scale-105 transition-transform">UPI</span>
                  <span class="text-[8px] sm:text-[9px] font-bold text-gray-400 mt-0.5">GPay/PhonePe</span>
                </div>

                <!-- Badge 2: Cash on Delivery -->
                <div class="bg-[#0a0b0e] border border-white/10 rounded-xl p-2 flex flex-col items-center justify-center hover:border-amber-400/50 transition-all group shadow-inner">
                  <span class="text-xs font-black text-amber-300 tracking-tighter group-hover:scale-105 transition-transform">COD</span>
                  <span class="text-[8px] sm:text-[9px] font-bold text-gray-400 mt-0.5">Pay On Delivery</span>
                </div>

                <!-- Badge 3: RuPay & Cards -->
                <div class="bg-[#0a0b0e] border border-white/10 rounded-xl p-2 flex flex-col items-center justify-center hover:border-amber-400/50 transition-all group shadow-inner">
                  <span class="text-xs font-black text-blue-400 tracking-tighter group-hover:scale-105 transition-transform">RuPay</span>
                  <span class="text-[8px] sm:text-[9px] font-bold text-gray-400 mt-0.5">Debit/Credit</span>
                </div>

                <!-- Badge 4: Paytm / Wallet -->
                <div class="bg-[#0a0b0e] border border-white/10 rounded-xl p-2 flex flex-col items-center justify-center hover:border-amber-400/50 transition-all group shadow-inner">
                  <span class="text-xs font-black text-cyan-400 tracking-tighter group-hover:scale-105 transition-transform">Paytm</span>
                  <span class="text-[8px] sm:text-[9px] font-bold text-gray-400 mt-0.5">All Wallets</span>
                </div>

                <!-- Badge 5: NetBanking -->
                <div class="bg-[#0a0b0e] border border-white/10 rounded-xl p-2 flex flex-col items-center justify-center hover:border-amber-400/50 transition-all group shadow-inner">
                  <span class="text-xs font-black text-purple-400 tracking-tighter group-hover:scale-105 transition-transform">BANK</span>
                  <span class="text-[8px] sm:text-[9px] font-bold text-gray-400 mt-0.5">NetBanking</span>
                </div>
              </div>
            </div>"""

target_snippet = """              <div class="flex items-center gap-2.5 text-amber-300 font-medium border-t border-white/10 pt-2">
                <span>🛡️ 100% Quality Guaranteed &bull; Secure COD Dispatch</span>
              </div>
            </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if target_snippet in content and "Guaranteed Safe & Secure Checkout" not in content:
            content = content.replace(target_snippet, f"{target_snippet}\n{payment_badges_html}")
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"ADDED INDIAN PAYMENT TRUST BADGES TO: {fpath}")

