import os
import re

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

clean_change_fn = """    function changeMainProductImage(btn, src, isVideo = false) {
      const mainImg = document.getElementById('ProductMainImage');
      const mainVid = document.getElementById('ProductMainVideo');
      const imgContainer = document.getElementById('ProductMainImageContainer');
      const bestsellerBadge = document.getElementById('BestsellerBadge');
      
      if (imgContainer) {
        if (isVideo) {
          if (mainImg) mainImg.classList.add('hidden');
          if (mainVid) {
            mainVid.classList.remove('hidden');
            if (src) mainVid.src = src;
            mainVid.play().catch(() => {});
          }
          imgContainer.className = 'relative w-full aspect-square rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-black transition-all duration-300';
          if (bestsellerBadge) bestsellerBadge.style.display = 'none';
        } else {
          if (mainVid) {
            mainVid.pause();
            mainVid.classList.add('hidden');
          }
          if (mainImg) {
            mainImg.classList.remove('hidden');
            mainImg.src = src;
            mainImg.className = 'w-full h-full object-cover block transition-transform duration-300 group-hover:scale-[1.01]';
          }
          imgContainer.className = 'relative w-full aspect-square rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center bg-[#0a0c10] transition-all duration-300';
          if (bestsellerBadge) {
            bestsellerBadge.style.display = src.includes('botanical-pedestal') ? 'flex' : 'none';
          }
        }
      }
      
      document.querySelectorAll('.js-thumb-btn').forEach(b => {
        b.classList.remove('border-2', 'border-[#d4af37]');
        b.classList.add('border-white/10');
      });
      if (btn) {
        btn.classList.remove('border-white/10');
        btn.classList.add('border-2', 'border-[#d4af37]');
      }
    }"""

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(r'function changeMainProductImage\(btn,\s*src,\s*isVideo\s*=\s*false\)\s*\{.*?\}\s*\}', clean_change_fn, content, flags=re.DOTALL)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED changeMainProductImage IN: {fpath}")
