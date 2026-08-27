import os
import glob
import re

mobile_drawer_markup = """
  <!-- 📱 Ultra-Luxury Mobile Navigation Drawer Overlay & Backdrop -->
  <div id="MobileNavBackdrop" onclick="closeMobileNavDrawer()" class="fixed inset-0 bg-black/80 backdrop-blur-md z-50 opacity-0 pointer-events-none transition-opacity duration-300 ease-out"></div>

  <div id="MobileNavDrawer" class="fixed top-0 right-0 bottom-0 w-[85%] max-w-sm bg-gradient-to-b from-[#0e1017] via-[#090a0e] to-black border-l border-[#d4af37]/30 z-50 shadow-[-15px_0_40px_rgba(0,0,0,0.9)] transform translate-x-full transition-transform duration-300 ease-out flex flex-col justify-between overflow-y-auto">
    
    <!-- Drawer Header -->
    <div class="p-5 border-b border-white/10 flex items-center justify-between">
      <div class="flex items-center gap-2.5">
        <img src="./assets/blackroots-logo-circle-black.jpg" alt="BlackRoots Logo" class="w-8 h-8 rounded-full border border-[#d4af37] object-cover">
        <div class="flex flex-col">
          <span class="font-serif text-lg font-bold text-white uppercase tracking-wider">BlackRoots</span>
          <span class="text-[8px] uppercase tracking-widest text-[#d4af37] font-bold -mt-0.5">Revive Your Roots</span>
        </div>
      </div>
      <button type="button" onclick="closeMobileNavDrawer()" class="w-8 h-8 rounded-full bg-white/10 border border-[#d4af37]/40 text-[#d4af37] flex items-center justify-center text-sm font-bold hover:bg-[#d4af37] hover:text-black transition-all cursor-pointer" aria-label="Close Menu">
        ✕
      </button>
    </div>

    <!-- Special Drawer Promo Banner -->
    <div class="mx-5 mt-4 p-3 rounded-2xl bg-gradient-to-r from-emerald-950/60 to-black border border-emerald-500/30 flex items-center justify-between text-xs">
      <div class="flex items-center gap-2">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="text-emerald-300 font-bold text-[11px]">Special Launch Offer</span>
      </div>
      <span class="text-[#d4af37] font-black text-xs">&#8377;499 Only</span>
    </div>

    <!-- Navigation Links List -->
    <div class="p-5 space-y-1.5 flex-1">
      <a href="index.html" class="flex items-center gap-3 px-4 py-3 rounded-xl text-gray-200 hover:text-[#d4af37] hover:bg-white/5 font-semibold text-xs uppercase tracking-wider transition-all">
        <span>🏠</span> <span>Home</span>
      </a>
      <a href="product.html" class="flex items-center justify-between px-4 py-3 rounded-xl bg-[#d4af37]/10 border border-[#d4af37]/40 text-[#d4af37] font-bold text-xs uppercase tracking-wider transition-all">
        <div class="flex items-center gap-3">
          <span>🛍️</span> <span>Product (250ml)</span>
        </div>
        <span class="bg-[#d4af37] text-black text-[9px] font-black px-2 py-0.5 rounded-full">&#8377;499</span>
      </a>
      <a href="ingredients.html" class="flex items-center gap-3 px-4 py-3 rounded-xl text-gray-200 hover:text-[#d4af37] hover:bg-white/5 font-semibold text-xs uppercase tracking-wider transition-all">
        <span>🌿</span> <span>Herbal Ingredients</span>
      </a>
      <a href="how-to-use.html" class="flex items-center gap-3 px-4 py-3 rounded-xl text-gray-200 hover:text-[#d4af37] hover:bg-white/5 font-semibold text-xs uppercase tracking-wider transition-all">
        <span>🚿</span> <span>Application Ritual</span>
      </a>
      <a href="reviews.html" class="flex items-center gap-3 px-4 py-3 rounded-xl text-gray-200 hover:text-[#d4af37] hover:bg-white/5 font-semibold text-xs uppercase tracking-wider transition-all">
        <span>⭐</span> <span>Customer Reviews</span>
      </a>
      <a href="ai-consultant.html" class="flex items-center gap-3 px-4 py-3 rounded-xl text-amber-300 hover:bg-amber-400/10 font-bold text-xs uppercase tracking-wider transition-all">
        <span>🩺</span> <span>AI Hair Doctor</span>
      </a>
      <a href="track-order.html" class="flex items-center gap-3 px-4 py-3 rounded-xl text-gray-200 hover:text-[#d4af37] hover:bg-white/5 font-semibold text-xs uppercase tracking-wider transition-all">
        <span>📦</span> <span>Track My Order</span>
      </a>
      <a href="contact.html" class="flex items-center gap-3 px-4 py-3 rounded-xl text-gray-200 hover:text-[#d4af37] hover:bg-white/5 font-semibold text-xs uppercase tracking-wider transition-all">
        <span>📞</span> <span>Customer Support</span>
      </a>
    </div>

    <!-- Drawer Footer CTA -->
    <div class="p-5 border-t border-white/10 space-y-3 bg-black/60">
      <a href="product.html" class="group relative w-full inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs px-5 py-3.5 rounded-xl border border-[#fff3b0]/70 shadow-[0_10px_25px_rgba(212,175,55,0.3)] hover:scale-105 transition-all uppercase tracking-wider text-center">
        <span>ORDER NOW &bull; &#8377;499</span>
        <span class="w-5 h-5 rounded-md bg-black text-[#d4af37] flex items-center justify-center font-black text-xs">
          🛍️
        </span>
      </a>
      <p class="text-[10px] text-gray-400 text-center font-medium">
        ⚡ Free Express COD Delivery Across India
      </p>
    </div>

  </div>
"""

# Process all html files
all_html = glob.glob('*.html') + glob.glob('demo_lab/*.html') + glob.glob('preview/*.html')

for fpath in all_html:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any existing drawer if duplicated
    content = re.sub(r'<!-- 📱 Ultra-Luxury Mobile Navigation Drawer.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="MobileNavBackdrop".*?</div>\s*</div>', '', content, flags=re.DOTALL)

    # Inject right before </body>
    if '</body>' in content:
        content = content.replace('</body>', mobile_drawer_markup.strip() + '\n\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"INJECTED ULTRA-LUXURY MOBILE DRAWER INTO: {fpath}")
