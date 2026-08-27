import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

drawer_js_code = """
/* 📱 Mobile Navigation Drawer Global Controls */
function openMobileNavDrawer() {
  const backdrop = document.getElementById('MobileNavDrawerBackdrop');
  const drawer = document.getElementById('MobileNavDrawer');
  if (backdrop && drawer) {
    backdrop.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
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
    document.body.style.overflow = '';
    setTimeout(() => {
      backdrop.classList.add('hidden');
    }, 300);
  }
}

window.openMobileNavDrawer = openMobileNavDrawer;
window.closeMobileNavDrawer = closeMobileNavDrawer;
"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'openMobileNavDrawer' not in content:
            content += "\n" + drawer_js_code
            with open(jspath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"ADDED MOBILE DRAWER JS TO: {jspath}")

# Now update all HTML files to ensure MobileNavDrawer has z-[9999] and ultra-fast click response
html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html') and f != 'mobile-preview.html':
            html_files.append(os.path.join(root, f))

new_drawer_html = """<!-- Mobile Slide-In Navigation Drawer (Android & iOS) -->
<div id="MobileNavDrawerBackdrop" class="fixed inset-0 bg-black/80 backdrop-blur-md z-[9990] hidden opacity-0 transition-opacity duration-300" onclick="closeMobileNavDrawer()"></div>

<div id="MobileNavDrawer" class="fixed top-0 right-0 bottom-0 w-[280px] sm:w-[320px] bg-[#0c0e14] border-l border-[#d4af37]/40 z-[9999] transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col justify-between shadow-2xl p-5 overflow-y-auto">
  
  <div>
    <!-- Drawer Header -->
    <div class="flex items-center justify-between border-b border-white/10 pb-4 mb-5">
      <div class="flex items-center gap-2.5">
        <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo" class="w-8 h-8 rounded-full border border-[#d4af37]">
        <div class="flex flex-col">
          <span class="font-serif font-bold text-white text-lg tracking-wider">BlackRoots</span>
          <span class="text-[8px] text-amber-300 font-bold tracking-widest uppercase -mt-1">Revive Your Roots</span>
        </div>
      </div>
      <button type="button" onclick="closeMobileNavDrawer()" class="w-8 h-8 rounded-full bg-white/10 text-amber-300 hover:bg-[#d4af37] hover:text-black flex items-center justify-center font-bold text-sm transition-all focus:outline-none cursor-pointer">
        ✕
      </button>
    </div>

    <!-- Navigation Links -->
    <nav class="space-y-1.5">
      <a href="index.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>🏠</span> <span>Home Page</span>
      </a>
      <a href="product.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-amber-300 bg-amber-500/10 border border-amber-500/30 transition-all">
        <span>🛍️</span> <span>Product Detail (₹499)</span>
      </a>
      <a href="reviews.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>⭐</span> <span>1,300+ Verified Reviews</span>
      </a>
      <a href="ai-consultant.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 transition-all">
        <span>🤖</span> <span>AI Doctor (Dr. Kuroki)</span>
      </a>
      <a href="ingredients.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>🌿</span> <span>Botanical Ingredients</span>
      </a>
      <a href="how-to-use.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>📖</span> <span>How To Use & Timer</span>
      </a>
      <a href="track-order.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>🚚</span> <span>Track Your Order</span>
      </a>
      <a href="contact.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>📞</span> <span>Contact Support</span>
      </a>
      <a href="influencer.html" class="flex items-center gap-3 px-3.5 py-3 rounded-xl text-xs font-bold text-gray-200 hover:text-amber-300 hover:bg-white/5 transition-all">
        <span>👥</span> <span>Creator Affiliate Portal</span>
      </a>
    </nav>
  </div>

  <!-- Drawer Footer CTA -->
  <div class="pt-4 border-t border-white/10 space-y-3 mt-6">
    <a href="product.html" class="w-full bg-gradient-to-r from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-black text-xs py-3.5 px-4 rounded-xl flex items-center justify-center gap-2 shadow-lg uppercase tracking-wider">
      <span>BUY NOW &bull; ₹499.00</span>
    </a>
    <p class="text-[10px] text-gray-400 text-center font-light">
      Free Express Delivery Across India &bull; COD Available
    </p>
  </div>

</div>"""

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'MobileNavDrawer' in content:
            start_d = content.find('<!-- Mobile Slide-In Navigation Drawer')
            if start_d == -1:
                start_d = content.find('<div id="MobileNavDrawerBackdrop"')
            end_d = content.find('</div>\n\n<script>', start_d)
            if end_d == -1:
                end_d = content.find('</div>\r\n\r\n<script>', start_d)
            if end_d == -1:
                end_d = content.find('</script>', start_d)
                if end_d != -1:
                    end_d += 9

            if start_d != -1 and end_d != -1:
                content = content[:start_d] + new_drawer_html + content[end_d:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPDATED DRAWER HTML IN: {fpath}")
    except Exception as e:
        print(f"Error updating drawer in {fpath}: {e}")
