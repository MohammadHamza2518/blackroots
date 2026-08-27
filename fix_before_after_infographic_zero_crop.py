import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

smart_zero_crop_script = """  <script>
    function changeMainProductImage(btn, src) {
      const mainImg = document.getElementById('ProductMainImage');
      const imgContainer = document.getElementById('ProductMainImageContainer');
      const bestsellerBadge = document.getElementById('BestsellerBadge');
      
      if (mainImg && imgContainer) {
        mainImg.src = src;
        
        if (src.includes('before-after-infographic') || src.includes('key-ingredients')) {
          // Infographic Banners: Must use object-contain p-1 so NO top/bottom text is sliced off!
          imgContainer.className = 'relative w-full aspect-[16/9] rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center group bg-[#0a0c10] p-1 sm:p-2 transition-all duration-300';
          mainImg.className = 'w-full h-full object-contain rounded-xl transition-transform duration-300 group-hover:scale-[1.01]';
          if (bestsellerBadge) bestsellerBadge.style.display = 'none';
        } else if (src.includes('how-to-use')) {
          // White Graphic Canvas Fits Perfectly
          imgContainer.className = 'relative w-full aspect-[16/9] sm:aspect-[16/10] rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center group bg-white p-2 sm:p-4 transition-all duration-300';
          mainImg.className = 'w-full h-full object-contain rounded-xl transition-transform duration-300 group-hover:scale-[1.01]';
          if (bestsellerBadge) bestsellerBadge.style.display = 'none';
        } else {
          // Bathroom Counter & Flatlay Photos
          imgContainer.className = 'relative w-full aspect-[16/9] sm:aspect-[4/3] rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center group bg-[#0a0c10] p-1 transition-all duration-300';
          mainImg.className = 'w-full h-full object-contain sm:object-cover rounded-xl transition-transform duration-300 group-hover:scale-[1.01]';
          if (bestsellerBadge) bestsellerBadge.style.display = 'flex';
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
    }
  </script>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if "function changeMainProductImage" in content:
            script_idx = content.find("function changeMainProductImage")
            bg_script = content.rfind("<script>", 0, script_idx)
            if bg_script != -1:
                content = content[:bg_script] + smart_zero_crop_script + "\n</body>\n</html>"

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED BEFORE-AFTER INFOGRAPHIC ZERO CROP DISPLAY IN: {fpath}")

