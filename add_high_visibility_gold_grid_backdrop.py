import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

high_visibility_backdrop_html = """  <!-- Hero Section (High-Visibility Animated Gold Grid & Luminous Ambient Aura) -->
  <section class="relative min-h-[85vh] flex items-center justify-center overflow-hidden bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-[#14161f] via-[#090a0d] to-[#040507] py-12 sm:py-16 select-none border-b border-[#d4af37]/25">
    
    <!-- Animated Subtle Gold Grid Mesh Overlay (100% Highly Visible) -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#d4af37_1px,transparent_1px),linear-gradient(to_bottom,#d4af37_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_70%_60%_at_50%_35%,#000_70%,transparent_100%)] opacity-20 animate-pulse pointer-events-none"></div>

    <!-- Vibrant Luminous Gold Floating Ambient Orbs -->
    <div class="absolute top-10 left-1/2 -translate-x-1/2 w-[650px] h-[380px] bg-gradient-to-r from-[#d4af37]/35 via-[#f7e7a7]/25 to-[#aa7c11]/30 rounded-full filter blur-[65px] animate-pulse pointer-events-none"></div>
    <div class="absolute top-1/4 left-5 w-80 h-80 bg-[#d4af37]/25 rounded-full filter blur-[60px] animate-pulse pointer-events-none"></div>
    <div class="absolute bottom-10 right-5 w-80 h-80 bg-[#aa7c11]/25 rounded-full filter blur-[60px] animate-pulse pointer-events-none"></div>

    <!-- Glowing Visible Gold Sparkles (60fps Pure CSS) -->
    <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
      <div class="absolute top-1/4 left-1/6 w-2.5 h-2.5 rounded-full bg-[#f7e7a7] shadow-[0_0_12px_#d4af37] opacity-80 animate-ping" style="animation-duration: 3s;"></div>
      <div class="absolute top-1/3 right-1/5 w-3 h-3 rounded-full bg-[#d4af37] shadow-[0_0_15px_#f7e7a7] opacity-70 animate-pulse" style="animation-duration: 2.5s;"></div>
      <div class="absolute bottom-1/3 left-1/4 w-2 h-2 rounded-full bg-[#f7e7a7] shadow-[0_0_10px_#d4af37] opacity-90 animate-ping" style="animation-duration: 4s;"></div>
      <div class="absolute top-1/2 right-1/4 w-2 h-2 rounded-full bg-[#d4af37] shadow-[0_0_10px_#d4af37] opacity-80 animate-pulse" style="animation-duration: 3.2s;"></div>
    </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('<!-- Hero Section')
        if s_idx == -1:
            s_idx = content.find('<!-- Clean Ultra-Luxury Hero Section -->')

        if s_idx != -1:
            e_idx = content.find('<div class="relative z-20 max-w-5xl', s_idx)
            if e_idx != -1:
                content = content[:s_idx] + high_visibility_backdrop_html + "\n\n    " + content[e_idx:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED HIGH-VISIBILITY GOLD GRID BACKDROP IN: {fpath}")
