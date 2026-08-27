import os
import glob

html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html') and f != 'mobile-preview.html':
            html_files.append(os.path.join(root, f))

print(f"Upgrading mobile header & navigation across {len(html_files)} HTML files...")

mobile_drawer_html = """
<!-- Mobile Slide-In Navigation Drawer (Android & iOS) -->
<div id="MobileNavDrawerBackdrop" class="fixed inset-0 bg-black/80 backdrop-blur-md z-[90] hidden transition-opacity duration-300" onclick="closeMobileNavDrawer()"></div>

<div id="MobileNavDrawer" class="fixed top-0 right-0 bottom-0 w-[280px] sm:w-[320px] bg-[#0c0e14] border-l border-[#d4af37]/30 z-[100] transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col justify-between shadow-2xl p-5">
  
  <div>
    <!-- Drawer Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-4 mb-5">
      <div class="flex items-center gap-2.5">
        <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo" class="w-8 h-8 rounded-full border border-[#d4af37]">
        <span class="font-serif font-bold text-white text-lg tracking-wider">BlackRoots</span>
      </div>
      <button type="button" onclick="closeMobileNavDrawer()" class="w-8 h-8 rounded-full bg-white/10 text-amber-300 hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-bold text-sm transition-all focus:outline-none">
        ✕
      </button>
    </div>

    <!-- Navigation Links -->
    <nav class="space-y-2">
      <a href="index.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>🏠</span> <span>Home Page</span>
      </a>
      <a href="product.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-amber-300 bg-amber-500/10 border border-amber-500/30 transition-all">
        <span>🛍️</span> <span>Product Detail (₹499)</span>
      </a>
      <a href="reviews.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>⭐</span> <span>1,300+ Verified Reviews</span>
      </a>
      <a href="ai-consultant.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 transition-all">
        <span>🤖</span> <span>AI Doctor (Dr. Kuroki)</span>
      </a>
      <a href="ingredients.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>🌿</span> <span>Botanical Ingredients</span>
      </a>
      <a href="how-to-use.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>📖</span> <span>How To Use & Timer</span>
      </a>
      <a href="track-order.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>🚚</span> <span>Track Your Order</span>
      </a>
      <a href="contact.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>📞</span> <span>Contact Support</span>
      </a>
      <a href="influencer.html" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>👥</span> <span>Creator Portal</span>
      </a>
    </nav>
  </div>

  <!-- Drawer Footer CTA -->
  <div class="pt-4 border-t border-white/10 space-y-3">
    <a href="product.html" class="w-full bg-gradient-to-r from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-black text-xs py-3 px-4 rounded-xl flex items-center justify-center gap-2 shadow-lg uppercase tracking-wider">
      <span>BUY NOW &bull; ₹499.00</span>
    </a>
    <p class="text-[10px] text-gray-400 text-center font-light">
      Free Express Delivery Across India &bull; COD Available
    </p>
  </div>

</div>

<script>
  function openMobileNavDrawer() {
    const backdrop = document.getElementById('MobileNavDrawerBackdrop');
    const drawer = document.getElementById('MobileNavDrawer');
    if (backdrop && drawer) {
      backdrop.classList.remove('hidden');
      setTimeout(() => {
        backdrop.classList.remove('opacity-0');
        drawer.classList.remove('translate-x-full');
      }, 10);
    }
  }

  function closeMobileNavDrawer() {
    const backdrop = document.getElementById('MobileNavDrawerBackdrop');
    const drawer = document.getElementById('MobileNavDrawer');
    if (backdrop && drawer) {
      drawer.classList.add('translate-x-full');
      backdrop.classList.add('opacity-0');
      setTimeout(() => {
        backdrop.classList.add('hidden');
      }, 300);
    }
  }
</script>
"""

new_top_announcement_bar = """  <!-- Top Announcement Bar (Mobile & Desktop Optimized) -->
  <div class="bg-gradient-to-r from-[#123824] via-[#0d2a1c] to-[#123824] text-[#f5e4ab] border-b border-[#d4af37]/30 py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap">
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        SPECIAL OFFER
      </span>
      <span>FREE Express Delivery Across India &bull; Introductory Price ₹499.00</span>
    </div>
  </div>"""

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        # 1. Update Top Announcement Bar
        ann_start = content.find('<div class="bg-gradient-to-r from-[#123824]')
        if ann_start != -1:
            ann_end = content.find('</div>\n', ann_start)
            if ann_end == -1:
                ann_end = content.find('</div>\r\n', ann_start)
            if ann_end != -1:
                # check if it contains Special Offer
                content = content[:ann_start] + new_top_announcement_bar + content[ann_end+6:]
                modified = True

        # 2. Update Header for Mobile Cleanliness & Hamburger Icon
        h_start = content.find('<header')
        h_end = content.find('</header>')
        if h_start != -1 and h_end != -1:
            header_content = content[h_start:h_end+9]
            
            # Check if hamburger icon is missing
            if 'openMobileNavDrawer()' not in header_content:
                # Build header with logo, desktop nav, mobile buy pill, and hamburger icon
                clean_header = """<header class="sticky-header bg-[#0a0b0e]/95 backdrop-blur-xl border-b border-[#d4af37]/20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between gap-3">
      
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center gap-2.5 sm:gap-3 group text-decoration-none shrink-0">
        <img src="./assets/blackroots-logo-circle-black.jpg" alt="BlackRoots Logo" class="w-9 h-9 sm:w-11 sm:h-11 rounded-full border border-[#d4af37] object-cover shadow-lg group-hover:scale-105 transition-transform">
        <div class="flex flex-col">
          <span class="font-serif text-lg sm:text-2xl font-bold tracking-wider text-white group-hover:text-[#d4af37] transition-colors uppercase whitespace-nowrap">BlackRoots</span>
          <span class="text-[8px] sm:text-[9px] uppercase tracking-[0.2em] text-[#d4af37] font-bold -mt-1 whitespace-nowrap">Revive Your Roots</span>
        </div>
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="hidden lg:flex items-center gap-4 xl:gap-6 flex-nowrap">
        <a href="index.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors whitespace-nowrap">Home</a>
        <a href="product.html" class="text-xs font-extrabold text-[#d4af37] border-b-2 border-[#d4af37] pb-1 uppercase tracking-wider transition-colors whitespace-nowrap">Product (&#8377;499)</a>
        <a href="ingredients.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors whitespace-nowrap">Ingredients</a>
        <a href="how-to-use.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors whitespace-nowrap">Ritual</a>
        <a href="reviews.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors whitespace-nowrap">Reviews</a>
        <a href="ai-consultant.html" class="text-xs font-bold text-amber-300 bg-amber-500/10 border border-amber-500/30 hover:bg-amber-400 hover:text-black px-3.5 py-1.5 rounded-full tracking-wider uppercase whitespace-nowrap transition-all shadow-sm">✨ AI Doctor</a>
        <a href="track-order.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors whitespace-nowrap">Track Order</a>
        <a href="contact.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors whitespace-nowrap">Contact</a>
      </nav>

      <!-- Right Header Actions (Desktop CTA + Mobile Pill & Hamburger) -->
      <div class="flex items-center gap-2">
        <!-- Desktop Buy Button -->
        <a href="product.html" class="hidden lg:inline-flex js-trigger-order btn-gold-luxury py-2.5 px-5 text-xs font-bold shadow-xl shrink-0 whitespace-nowrap">
          <span>Buy Now &mdash; &#8377; 499.00</span>
        </a>

        <!-- Mobile Quick Buy Pill -->
        <a href="product.html" class="inline-flex lg:hidden bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black font-extrabold text-[10px] px-3 py-1.5 rounded-full shadow-md items-center gap-1 shrink-0 uppercase tracking-tight">
          <span>Buy &#8377;499</span>
        </a>

        <!-- Mobile Drawer Hamburger Toggle Button -->
        <button type="button" onclick="openMobileNavDrawer()" class="lg:hidden p-2 rounded-xl bg-white/10 border border-white/15 text-amber-300 hover:text-white hover:bg-white/20 focus:outline-none flex items-center justify-center shadow transition-all cursor-pointer" aria-label="Open Navigation Menu">
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
            <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>
          </svg>
        </button>
      </div>

    </div>
  </header>"""
                content = content[:h_start] + clean_header + content[h_end+9:]
                modified = True

        # 3. Insert Mobile Navigation Drawer before </body>
        if 'MobileNavDrawer' not in content:
            b_end = content.rfind('</body>')
            if b_end != -1:
                content = content[:b_end] + mobile_drawer_html + '\n' + content[b_end:]
                modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"UPGRADED MOBILE HEADER & DRAWER IN: {fpath}")
    except Exception as e:
        print(f"Error upgrading {fpath}: {e}")
