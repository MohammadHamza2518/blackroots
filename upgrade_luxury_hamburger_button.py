import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('demo_lab/*.html') + glob.glob('preview/*.html')

old_btn_pattern = r'<button[^>]*onclick="openMobileNavDrawer\(\)"[^>]*>.*?</button>'

new_luxury_hamburger = """<button type="button" onclick="openMobileNavDrawer()" class="lg:hidden p-2 sm:p-2.5 rounded-xl bg-gradient-to-br from-[#1b1e27] to-[#0c0e14] border border-[#d4af37]/60 text-amber-300 hover:border-[#d4af37] hover:text-white focus:outline-none flex items-center justify-center shadow-[0_5px_15px_rgba(0,0,0,0.6)] active:scale-90 transition-all cursor-pointer" aria-label="Open Navigation Menu">
          <svg class="w-5 h-5 text-amber-300" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
            <line x1="4" y1="6" x2="20" y2="6"></line>
            <line x1="4" y1="12" x2="20" y2="12"></line>
            <line x1="4" y1="18" x2="20" y2="18"></line>
          </svg>
        </button>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(old_btn_pattern, new_luxury_hamburger, content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED LUXURY HAMBURGER BUTTON IN: {fpath}")
