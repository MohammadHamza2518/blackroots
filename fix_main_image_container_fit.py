import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_viewport_container = """          <div class="relative aspect-square sm:aspect-[4/3] rounded-3xl overflow-hidden glass-panel-luxury p-6 flex items-center justify-center group">
            <img id="ProductMainImage" src="./assets/blackroots-bottle-single.png" alt="BlackRoots 250ml Bottles Render" class="max-h-full max-w-full object-contain filter drop-shadow-2xl transition-all duration-300 group-hover:scale-105">
            <div class="absolute top-4 left-4 bg-[#0a0f0d]/90 backdrop-blur-md text-amber-300 text-[10px] font-bold uppercase tracking-widest px-3 py-1 rounded-full border border-[#d4af37]/40 shadow-lg flex items-center gap-1.5 z-10">
              <svg class="w-3 h-3 text-[#d4af37]" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>BESTSELLER</span>
            </div>
          </div>"""

new_viewport_container = """          <div class="relative w-full aspect-square sm:aspect-[4/3] rounded-3xl overflow-hidden glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl flex items-center justify-center group bg-[#0d0e12]">
            <img id="ProductMainImage" src="./assets/blackroots-bottle-single.png" alt="BlackRoots Product Showcase" class="w-full h-full object-contain p-4 transition-all duration-300 group-hover:scale-105">
            <div class="absolute top-4 left-4 bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold uppercase tracking-widest px-3.5 py-1.5 rounded-full border border-[#d4af37]/50 shadow-xl flex items-center gap-1.5 z-20 pointer-events-none">
              <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
              </svg>
              <span>BESTSELLER</span>
            </div>
          </div>"""

smart_script = """  <script>
    function changeMainProductImage(btn, src) {
      const mainImg = document.getElementById('ProductMainImage');
      if (mainImg) {
        mainImg.src = src;
        if (src.includes('single') || src.includes('bottle-single')) {
          mainImg.className = 'w-full h-full object-contain p-4 transition-all duration-300 group-hover:scale-105';
        } else {
          mainImg.className = 'w-full h-full object-cover transition-all duration-300 group-hover:scale-105';
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

        if old_viewport_container in content:
            content = content.replace(old_viewport_container, new_viewport_container)

        if "function changeMainProductImage" in content:
            # Replace old helper script with smart script
            old_script_start = content.find("function changeMainProductImage")
            old_script_end = content.find("</script>", old_script_start)
            if old_script_start != -1 and old_script_end != -1:
                content = content[:old_script_start-12] + smart_script + content[old_script_end+9:]
        elif "</body>" in content:
            content = content.replace("</body>", f"{smart_script}\n</body>")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED MAIN IMAGE CONTAINER ASPECT RATIO & FIT IN: {fpath}")

