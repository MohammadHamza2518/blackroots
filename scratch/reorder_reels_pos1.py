import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

index_files = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html")
]

card_grey_to_black_html = """          <!-- Card 1 (HERO #1): reel-6.mp4 -> Real Testimonial (Grey To Naturally Black Hair) -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37] shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db_cLl-vUPL/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                ❤️ Real Testimonial
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-6.mp4" type="video/mp4">
            </video>

            <!-- Translucent Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                ❤️ VERIFIED REVIEW
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0" loading="lazy" decoding="async">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Grey To Naturally Black Hair</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 84.1K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>"""

card_reel3_html = """          <!-- Card 2: reel-3.mp4 -> Proven Results -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/DcA80uuvGfh/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <!-- Header Badges -->
            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                ⚡ Proven Results
              </span>
              
              <!-- Sleek Compact Circular Sound Icon Badge -->
              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>
            
            <!-- Video Tag -->
            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-3.mp4" type="video/mp4">
            </video>

            <!-- Translucent AI Rendered Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                ✨ REAL CUSTOMER REEL
              </span>
            </div>
            
            <!-- Shoppable Bottom Bar -->
            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0" loading="lazy" decoding="async">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Results Are 100% Real</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 61.2K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>"""

card_reel2_html = """          <!-- Card 3: reel-2.mp4 -> Anti-Dandruff -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db-aZhvpD_D/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                ✨ Anti-Dandruff
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-2.mp4" type="video/mp4">
            </video>

            <!-- Translucent Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                ✨ SCALP DEFENSE
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0" loading="lazy" decoding="async">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Say No To Flaky Dandruff</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 38.9K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>"""

card_reel4_html = """          <!-- Card 4: reel-4.mp4 -> Scalp Solution -->
          <div class="js-reel-card snap-center shrink-0 w-[275px] sm:w-[325px] aspect-[9/16] rounded-3xl overflow-hidden border-2 border-[#d4af37]/60 shadow-[0_20px_50px_rgba(0,0,0,0.8)] relative bg-black group transition-all duration-300 transform hover:-translate-y-1.5 cursor-pointer">
            
            <!-- 100% Full Card Transparent Overlay Anchor to Instagram -->
            <a href="https://www.instagram.com/reel/Db8ghNFJwau/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==" target="_blank" rel="noopener" class="absolute inset-0 z-20 w-full h-full" title="Click to watch on Instagram with sound"></a>

            <div class="absolute top-3.5 left-3.5 right-3.5 z-30 flex items-center justify-between pointer-events-none gap-2">
              <span class="bg-black/80 backdrop-blur-md text-amber-300 text-[9px] sm:text-[10px] font-extrabold uppercase px-3 py-1 rounded-full border border-amber-500/40 shadow-lg">
                🛡️ Scalp Solution
              </span>

              <span class="w-8 h-8 rounded-full bg-black/80 backdrop-blur-md text-amber-300 border border-amber-500/40 flex items-center justify-center text-xs shadow-xl shrink-0">
                🔊
              </span>
            </div>

            <video autoplay muted loop playsinline webkit-playsinline preload="metadata" class="w-full h-full object-cover bg-black pointer-events-none">
              <source src="./assets/reel-4.mp4" type="video/mp4">
            </video>

            <!-- Translucent Tag -->
            <div class="absolute bottom-16 left-1/2 -translate-x-1/2 z-30 pointer-events-none opacity-80 group-hover:opacity-100 transition-opacity">
              <span class="bg-black/75 backdrop-blur-md text-gray-300 text-[8px] font-medium tracking-widest uppercase px-2.5 py-0.5 rounded-full border border-white/10 shadow">
                🛡️ 3-IN-1 RECOVERY
              </span>
            </div>

            <div class="absolute bottom-3.5 left-3.5 right-3.5 z-30 p-3 rounded-2xl bg-black/85 backdrop-blur-xl border border-[#d4af37]/40 flex items-center justify-between gap-2 shadow-2xl">
              <div class="flex items-center gap-2.5 min-w-0 pointer-events-none">
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 shrink-0" loading="lazy" decoding="async">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Fix Grey Hair, Dandruff, Fall</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 29.8K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>"""

card_reel1_html = """          <!-- Card 5 (LAST): reel-1.mp4 -> 360° Studio Showcase / Application Ritual -->
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
                <img src="./assets/blackroots-bottle-single.png" alt="Product" class="w-8 h-8 object-contain rounded-lg bg-black/60 border border-[#d4af37]/40 shrink-0" loading="lazy" decoding="async">
                <div class="min-w-0 text-left">
                  <h4 class="text-[10px] font-extrabold text-white truncate">Roots Reborn Black</h4>
                  <div class="flex items-center gap-1.5">
                    <span class="text-amber-300 font-black text-xs">&#8377;499.00</span>
                    <span class="text-[8px] text-gray-400 font-semibold">&bull; 112K Views</span>
                  </div>
                </div>
              </div>
              <a href="product.html" class="js-trigger-order relative z-40 bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-[9px] font-black px-3.5 py-1.5 rounded-xl uppercase tracking-wider shrink-0 shadow-lg hover:scale-105 transition-transform pointer-events-auto">
                Buy Now &rarr;
              </a>
            </div>
          </div>"""

full_new_carousel_inner = f"\n{card_grey_to_black_html}\n\n{card_reel3_html}\n\n{card_reel2_html}\n\n{card_reel4_html}\n\n{card_reel1_html}\n"

for fpath in index_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace inner contents of ReelsCarouselContainer
        pattern = r'(<div id="ReelsCarouselContainer"[^>]*>).*?(<\/div>\s*<\/div>\s*<\/section>)'
        
        def repl(match):
            return match.group(1) + full_new_carousel_inner + "\n        </div>\n      </div>\n    </div>\n  </section>"

        # Let's check regex replacement
        new_content = re.sub(
            r'(<div id="ReelsCarouselContainer"[^>]*>).*?(<\/div>\s*<!-- Carousel Container Wrapper|\n\s*<\/div>\s*<\/div>\s*<\/section>)',
            r'\1' + full_new_carousel_inner + '\n        </div>',
            content,
            flags=re.DOTALL
        )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"REORDERED CAROUSEL CARDS TO PUT EDITED 6 AT 1ST IN: {fpath}")
