import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

pricing_html_old = """            <div class="p-5 rounded-2xl glass-panel-luxury mb-6 flex items-center justify-between">
              <div>
                <div class="text-xs text-gray-400 mb-1">Special Introductory Offer (Incl. all taxes)</div>
                <div class="flex items-baseline gap-3">
                  <span id="PDPPriceDisplay" class="text-3xl font-bold text-amber-400">&#8377;499.00</span>
                  <span class="text-base text-gray-500 line-through">&#8377;499.00</span>
                </div>
              </div>
              <span class="px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-bold border border-amber-500/30">
                50% OFF &mdash; SAVE &#8377;500
              </span>
            </div>"""

pricing_html_new = """            <div class="p-5 rounded-2xl glass-panel-luxury mb-6 flex items-center justify-between">
              <div>
                <div class="text-xs text-gray-400 mb-1">Special Introductory Offer (Incl. all taxes)</div>
                <div class="flex items-baseline gap-3">
                  <span id="PDPPriceDisplay" class="text-3xl font-bold text-amber-400">&#8377;499.00</span>
                  <span id="PDPMRPDisplay" class="text-base text-gray-500 line-through">&#8377;999.00</span>
                </div>
              </div>
              <span id="PDPBadgeDisplay" class="px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-bold border border-amber-500/30">
                50% OFF &mdash; SAVE &#8377;500
              </span>
            </div>"""

bundle_options_old = """              <!-- Option 1: Single Bottle -->
              <div class="js-bundle-option p-4 rounded-2xl border-2 border-[#d4af37] bg-[#d4af37]/10 cursor-pointer flex items-center justify-between transition-all" data-price="&#8377;499.00">
                <div class="flex items-center gap-3">
                  <span class="w-4 h-4 rounded-full border-2 border-amber-400 flex items-center justify-center">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                  </span>
                  <div>
                    <strong class="text-white text-sm block">1 Bottle (250ml) &mdash; Starter Pack</strong>
                    <span class="text-xs text-gray-300">&#8377;499.00 &bull; FREE Express Shipping</span>
                  </div>
                </div>
                <span class="text-xs font-bold text-amber-300 uppercase">Standard</span>
              </div>

              <!-- Option 2: 2 Bottles Pack (Best Seller) -->
              <div class="js-bundle-option p-4 rounded-2xl border border-white/10 bg-white/5 hover:border-amber-400 cursor-pointer flex items-center justify-between transition-all" data-price="&#8377;799.00">
                <div class="flex items-center gap-3">
                  <span class="w-4 h-4 rounded-full border-2 border-gray-400 flex items-center justify-center"></span>
                  <div>
                    <strong class="text-white text-sm block">2 Bottles Pack (500ml) &mdash; 60-Day Value Pack</strong>
                    <span class="text-xs text-emerald-400">&#8377;799.00 (&#8377;399/bottle) &bull; Save Extra &#8377;200 + FREE Shipping</span>
                  </div>
                </div>
                <span class="text-xs font-bold text-amber-300 uppercase bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30">BEST SELLER</span>
              </div>"""

bundle_options_new = """              <!-- Option 1: Single Bottle -->
              <div class="js-bundle-option p-4 rounded-2xl border-2 border-[#d4af37] bg-[#d4af37]/10 cursor-pointer flex items-center justify-between transition-all" data-price="&#8377;499.00" data-mrp="&#8377;999.00" data-badge="50% OFF &mdash; SAVE &#8377;500">
                <div class="flex items-center gap-3">
                  <span class="w-4 h-4 rounded-full border-2 border-amber-400 flex items-center justify-center">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                  </span>
                  <div>
                    <strong class="text-white text-sm block">1 Bottle (250ml) &mdash; Starter Pack</strong>
                    <span class="text-xs text-gray-300">&#8377;499.00 &bull; FREE Express Shipping</span>
                  </div>
                </div>
                <span class="text-xs font-bold text-amber-300 uppercase">Standard</span>
              </div>

              <!-- Option 2: 2 Bottles Pack (Best Seller) -->
              <div class="js-bundle-option p-4 rounded-2xl border border-white/10 bg-white/5 hover:border-amber-400 cursor-pointer flex items-center justify-between transition-all" data-price="&#8377;899.00" data-mrp="&#8377;1,998.00" data-badge="55% OFF &mdash; SAVE &#8377;1,099">
                <div class="flex items-center gap-3">
                  <span class="w-4 h-4 rounded-full border-2 border-gray-400 flex items-center justify-center"></span>
                  <div>
                    <strong class="text-white text-sm block">2 Bottles Pack (500ml) &mdash; 60-Day Value Pack</strong>
                    <span class="text-xs text-emerald-400">&#8377;899.00 (&#8377;449/bottle) &bull; Save Extra &#8377;100 + FREE Shipping</span>
                  </div>
                </div>
                <span class="text-xs font-bold text-amber-300 uppercase bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30">BEST SELLER</span>
              </div>

              <!-- Option 3: 3 Bottles Family Pack (Max Savings) -->
              <div class="js-bundle-option p-4 rounded-2xl border border-white/10 bg-white/5 hover:border-amber-400 cursor-pointer flex items-center justify-between transition-all" data-price="&#8377;1,199.00" data-mrp="&#8377;2,997.00" data-badge="60% OFF &mdash; SAVE &#8377;1,798">
                <div class="flex items-center gap-3">
                  <span class="w-4 h-4 rounded-full border-2 border-gray-400 flex items-center justify-center"></span>
                  <div>
                    <strong class="text-white text-sm block">3 Bottles Family Pack (750ml) &mdash; Max Value Pack</strong>
                    <span class="text-xs text-emerald-400">&#8377;1,199.00 (&#8377;399/bottle) &bull; Save Extra &#8377;300 + FREE Shipping</span>
                  </div>
                </div>
                <span class="text-xs font-bold text-emerald-400 uppercase bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/30">MAX VALUE</span>
              </div>"""

bundle_script = """  <script>
    // BlackRoots Interactive Bundle Selector Engine
    document.addEventListener('DOMContentLoaded', function() {
      const bundleOptions = document.querySelectorAll('.js-bundle-option');
      const pdpPrice = document.getElementById('PDPPriceDisplay');
      const pdpMrp = document.getElementById('PDPMRPDisplay');
      const pdpBadge = document.getElementById('PDPBadgeDisplay');

      bundleOptions.forEach(option => {
        option.addEventListener('click', function() {
          bundleOptions.forEach(opt => {
            opt.classList.remove('border-2', 'border-[#d4af37]', 'bg-[#d4af37]/10');
            opt.classList.add('border-white/10', 'bg-white/5');
            const dot = opt.querySelector('span.w-4');
            if (dot) dot.innerHTML = '';
          });

          this.classList.remove('border-white/10', 'bg-white/5');
          this.classList.add('border-2', 'border-[#d4af37]', 'bg-[#d4af37]/10');
          const dot = this.querySelector('span.w-4');
          if (dot) dot.innerHTML = '<span class="w-2 h-2 rounded-full bg-amber-400"></span>';

          const price = this.getAttribute('data-price') || '₹499.00';
          const mrp = this.getAttribute('data-mrp') || '₹999.00';
          const badge = this.getAttribute('data-badge') || '50% OFF — SAVE ₹500';

          if (pdpPrice) pdpPrice.innerHTML = price;
          if (pdpMrp) pdpMrp.innerHTML = mrp;
          if (pdpBadge) pdpBadge.innerHTML = badge;

          const buyBtnSpan = document.querySelector('#MainBuyButton span');
          if (buyBtnSpan) buyBtnSpan.innerHTML = `Buy Now &mdash; ${price}`;
        });
      });
    });
  </script>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if pricing_html_old in content:
            content = content.replace(pricing_html_old, pricing_html_new)
        if bundle_options_old in content:
            content = content.replace(bundle_options_old, bundle_options_new)

        if "BlackRoots Interactive Bundle Selector Engine" not in content and "</body>" in content:
            content = content.replace("</body>", f"{bundle_script}\n</body>")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED PRICING & BUNDLE ENGINE IN: {fpath}")

