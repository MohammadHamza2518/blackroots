import os
import glob

html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML files to optimize for mobile.")

mobile_head_css = """
  <!-- Mobile & Touch Optimization (Android & iOS) -->
  <style>
    @media (max-width: 768px) {
      input[type="text"],
      input[type="email"],
      input[type="number"],
      input[type="password"],
      input[type="search"],
      select,
      textarea {
        font-size: 16px !important; /* Prevents auto-zoom on iOS Safari */
      }
    }
    html {
      scroll-behavior: smooth;
      -webkit-tap-highlight-color: transparent;
    }
    body {
      padding-bottom: env(safe-area-inset-bottom);
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100% !important;
    }
    /* Touch scrollbar refinement for mobile */
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
  </style>
"""

sticky_buy_bar_html = """
<!-- Mobile Floating Sticky Buy Bar (Android & iOS Optimized) -->
<div id="MobileStickyBuyBar" class="fixed bottom-0 left-0 right-0 z-50 bg-black/90 backdrop-blur-xl border-t border-[#d4af37]/40 p-2.5 sm:hidden shadow-[0_-10px_25px_rgba(0,0,0,0.8)] transition-all duration-300 transform translate-y-0">
  <div class="flex items-center justify-between gap-2.5 max-w-md mx-auto px-1">
    <div class="flex items-center gap-2.5 min-w-0">
      <img src="./assets/blackroots-bottle-single.png" alt="BlackRoots Shampoo" class="w-10 h-10 object-contain rounded-lg bg-black/60 border border-[#d4af37]/30 p-0.5 shrink-0">
      <div class="truncate">
        <h4 class="text-xs font-bold text-white truncate tracking-tight">BlackRoots Hair Shampoo</h4>
        <div class="flex items-center gap-1.5 mt-0.5">
          <span class="text-xs font-extrabold text-[#d4af37]">₹799</span>
          <span class="text-[10px] text-gray-400 line-through">₹1,499</span>
          <span class="text-[9px] bg-amber-400/20 text-amber-300 font-bold px-1.5 py-0.5 rounded uppercase">47% OFF</span>
        </div>
      </div>
    </div>
    
    <a href="./product.html" class="shrink-0 bg-gradient-to-r from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-xs px-4 py-2.5 rounded-full shadow-lg flex items-center gap-1.5 transform active:scale-95 transition-transform uppercase tracking-wider">
      <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
        <path d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"/>
      </svg>
      <span>Buy Now</span>
    </a>
  </div>
</div>
"""

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified = False

        # 1. Update Viewport Meta Tag for Notch & iOS Safari Safe Area
        old_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        new_viewport = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
        if old_viewport in content:
            content = content.replace(old_viewport, new_viewport)
            modified = True
        elif 'viewport-fit=cover' not in content and '<meta name="viewport"' in content:
            # find meta viewport line and replace
            vp_idx = content.find('<meta name="viewport"')
            vp_end = content.find('>', vp_idx)
            content = content[:vp_idx] + new_viewport + content[vp_end+1:]
            modified = True

        # 2. Add Mobile CSS Fixes in Head
        if '/* Mobile & Touch Optimization (Android & iOS) */' not in content:
            head_end = content.find('</head>')
            if head_end != -1:
                content = content[:head_end] + mobile_head_css + '\n' + content[head_end:]
                modified = True

        # 3. Add overflow-x-hidden to body
        if '<body' in content and 'overflow-x-hidden' not in content:
            body_idx = content.find('<body')
            body_close = content.find('>', body_idx)
            body_tag = content[body_idx:body_close+1]
            if 'class="' in body_tag:
                new_body_tag = body_tag.replace('class="', 'class="overflow-x-hidden w-full max-w-full ')
            else:
                new_body_tag = body_tag.replace('<body', '<body class="overflow-x-hidden w-full max-w-full"')
            content = content[:body_idx] + new_body_tag + content[body_close+1:]
            modified = True

        # 4. Add playsinline and webkit-playsinline to all video tags
        if '<video' in content:
            lines = content.splitlines()
            new_lines = []
            for line in lines:
                if '<video' in line and 'playsinline' not in line:
                    line = line.replace('<video', '<video playsinline webkit-playsinline')
                    modified = True
                elif '<video' in line and 'webkit-playsinline' not in line:
                    line = line.replace('playsinline', 'playsinline webkit-playsinline')
                    modified = True
                new_lines.append(line)
            content = '\n'.join(new_lines)

        # 5. Add Sticky Mobile Buy Bar to index.html and product.html
        fname = os.path.basename(fpath)
        if fname in ['index.html', 'product.html'] and 'MobileStickyBuyBar' not in content:
            body_end = content.rfind('</body>')
            if body_end != -1:
                content = content[:body_end] + sticky_buy_bar_html + '\n' + content[body_end:]
                modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"OPTIMIZED FOR MOBILE: {fpath}")
    except Exception as e:
        print(f"Error processing {fpath}: {e}")
