import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

simulator_files = [
    os.path.join(root_dir, "product-mobile-preview.html"),
    os.path.join(root_dir, "mobile-preview.html")
]

quick_tabs_html = """      <!-- Quick Page Tabs (Instant 1-Click Switch) -->
      <div class="flex items-center gap-1 bg-[#141722] p-1 border border-[#d4af37]/40 rounded-xl shadow-inner">
        <button id="TabHome" type="button" onclick="switchToSimPage('index.html')" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white">
          🏠 Home (Reels)
        </button>
        <button id="TabProduct" type="button" onclick="switchToSimPage('product.html')" class="px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-[#d4af37] text-black shadow">
          🛍️ Product
        </button>
      </div>"""

helper_script = """
    function switchToSimPage(page) {
      const pageSelector = document.getElementById('PageSelector');
      if (pageSelector) pageSelector.value = page;
      changeSimulatedPage(page);
      
      const tabHome = document.getElementById('TabHome');
      const tabProduct = document.getElementById('TabProduct');
      if (tabHome && tabProduct) {
        if (page === 'index.html') {
          tabHome.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-[#d4af37] text-black shadow';
          tabProduct.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
        } else if (page === 'product.html') {
          tabProduct.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-[#d4af37] text-black shadow';
          tabHome.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
        } else {
          tabHome.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
          tabProduct.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
        }
      }
    }
"""

for sf in simulator_files:
    if os.path.exists(sf):
        with open(sf, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add quick tabs before page selector if not present
        if 'id="TabHome"' not in content:
            content = content.replace('<!-- Page Selector -->', quick_tabs_html + '\n\n      <!-- Page Selector -->')
        
        # Add helper script
        if 'switchToSimPage' not in content:
            content = content.replace('function changeSimulatedPage', helper_script + '\n    function changeSimulatedPage')

        with open(sf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"ENHANCED SIMULATOR NAVIGATION: {sf}")
