import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

clean_options_html = """            <div class="space-y-3 mb-6">
              <label class="block text-xs font-bold uppercase tracking-wider text-amber-300">Select Package Option:</label>
              
              <!-- Option 1: Single Bottle -->
              <div class="js-bundle-option p-4 rounded-2xl border-2 border-[#d4af37] bg-[#d4af37]/10 cursor-pointer flex items-center justify-between transition-all" data-price="&#8377;499.00" data-mrp="&#8377;999.00" data-badge="50% OFF &mdash; SAVE &#8377;500">
                <div class="flex items-center gap-3">
                  <span class="w-4 h-4 rounded-full border-2 border-amber-400 flex items-center justify-center shrink-0">
                    <span class="w-2 h-2 rounded-full bg-amber-400"></span>
                  </span>
                  <div>
                    <strong class="text-white text-sm font-bold block">1 Bottle (250ml)</strong>
                    <span class="text-xs text-gray-300">&#8377;499 &bull; FREE Delivery</span>
                  </div>
                </div>
                <span class="text-[11px] font-extrabold text-amber-300 uppercase tracking-wider shrink-0">STANDARD</span>
              </div>

              <!-- Option 2: 2 Bottles Pack (Best Seller) -->
              <div class="js-bundle-option p-4 rounded-2xl border border-white/10 bg-white/5 hover:border-amber-400 cursor-pointer flex items-center justify-between transition-all" data-price="&#8377;799.00" data-mrp="&#8377;1,998.00" data-badge="60% OFF &mdash; SAVE &#8377;1,199">
                <div class="flex items-center gap-3">
                  <span class="w-4 h-4 rounded-full border-2 border-gray-400 flex items-center justify-center shrink-0"></span>
                  <div>
                    <strong class="text-white text-sm font-bold block">2 Bottles Pack (500ml)</strong>
                    <span class="text-xs text-emerald-400 font-semibold">&#8377;799 (&#8377;399/ea) &bull; Save &#8377;200 Extra</span>
                  </div>
                </div>
                <span class="text-[11px] font-extrabold text-amber-300 uppercase bg-amber-500/10 px-3 py-1 rounded-full border border-amber-500/30 shrink-0">BEST SELLER</span>
              </div>
            </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        start_marker = '<div class="space-y-3 mb-6">'
        end_marker = '</div>\n\n          <div id="MainBuyButton"'
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)

        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + clean_options_html + content[end_idx + 6:]
        else:
            start_idx = content.find('<label class="block text-xs font-bold uppercase tracking-wider text-amber-300">Select Package Option:</label>')
            if start_idx != -1:
                container_start = content.rfind('<div class="space-y-3 mb-6">', 0, start_idx)
                container_end = content.find('<div id="MainBuyButton"', start_idx)
                if container_start != -1 and container_end != -1:
                    content = content[:container_start] + clean_options_html + "\n\n          " + content[container_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEAN PUNCHY OPTIONS APPLIED TO: {fpath}")

