import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

old_card_5 = """          <!-- Card 5 (LAST): reel-1.mp4 -> 360° Studio Showcase / Application Ritual -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-[0_25px_60px_rgba(212,175,55,0.25)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db-axwZpQGN/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] sm:text-[10px] font-black uppercase px-3 py-1 rounded-full shadow-lg">
                ✨ 360° STUDIO SHOWCASE
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-1.mp4" type="video/mp4">
            </video>

            <!-- Ultra-Clean Studio Watermark Pill -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[8px] font-extrabold tracking-widest uppercase px-3 py-1 rounded-full border border-amber-500/30 shadow-xl">
                ⚡ 360° AI Studio Rendered
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Roots Reborn Black</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 52.4K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>"""

new_card_5 = """          <!-- Card 5 (LAST): reel-1.mp4 -> 360° Studio Showcase / Application Ritual -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-[0_25px_60px_rgba(212,175,55,0.35)] relative bg-black group transition-all duration-300 transform hover:-translate-y-2 hover:shadow-[0_30px_70px_rgba(212,175,55,0.45)] cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db-axwZpQGN/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <!-- Top Floating Header Badges -->
            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/90 backdrop-blur-md text-amber-300 border border-[#d4af37]/70 text-[9px] sm:text-[10px] font-black uppercase px-3 py-1 rounded-full shadow-xl flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span>✨ 360° STUDIO VIEW</span>
              </span>

              <span class="w-8 h-8 rounded-full bg-black/90 backdrop-blur-md text-amber-300 border border-[#d4af37]/60 flex items-center justify-center text-xs shadow-xl shrink-0 group-hover:scale-110 transition-transform">
                🔊
              </span>
            </div>

            <!-- Video Player -->
            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none group-hover:scale-105 transition-transform duration-700 ease-out">
              <source src="./assets/reel-1.mp4" type="video/mp4">
            </video>

            <!-- Center Interactive Hint Pill -->
            <div class="absolute bottom-20 left-1/2 -translate-x-1/2 z-30 pointer-events-none">
              <span class="bg-black/90 backdrop-blur-md text-amber-300 text-[8px] sm:text-[9px] font-black tracking-widest uppercase px-3.5 py-1.5 rounded-full border border-amber-500/50 shadow-2xl flex items-center gap-1.5 animate-pulse">
                <span>🔄 360° 3D BOTTLE SHOWCASE</span>
              </span>
            </div>

            <!-- Bottom Floating Action Bar -->
            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/90 backdrop-blur-xl border border-[#d4af37]/50 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/40 shrink-0">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Roots Reborn Black</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-emerald-400 font-semibold">&bull; 52.4K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_card_5 in content:
            content = content.replace(old_card_5, new_card_5)
        else:
            # Fallback replacement
            s_idx = content.find('360° STUDIO SHOWCASE')
            if s_idx != -1:
                b_start = content.rfind('<div class="js-reel-card', 0, s_idx)
                b_end = content.find('<!-- Card 5', 0, s_idx)
                # Find the closing tag
                div_close = content.find('</div>', content.find('Buy Now &rarr;', s_idx)) + 12
                if b_start != -1 and div_close != -1:
                    content = content[:b_start] + new_card_5.strip() + content[div_close:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED 360 SHOWCASE CARD IN: {fpath}")
