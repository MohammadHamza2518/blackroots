import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

animated_backdrop_html = """  <!-- Hero Section (Lightweight 0% CPU Animated Luxury Gold Ambient Backdrop) -->
  <section class="relative min-h-[85vh] flex items-center justify-center overflow-hidden bg-[#08090c] py-12 sm:py-16 select-none">
    
    <!-- Pure CSS Animated Gold Ambient Glow Spheres (0% CPU Load) -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-gradient-to-tr from-[#d4af37]/15 via-[#f7e7a7]/10 to-transparent rounded-full filter blur-[100px] animate-pulse pointer-events-none"></div>
    <div class="absolute top-1/3 left-1/4 w-80 h-80 bg-[#d4af37]/10 rounded-full filter blur-[90px] animate-bounce-slow pointer-events-none"></div>
    <div class="absolute bottom-1/4 right-1/4 w-72 h-72 bg-[#aa7c11]/10 rounded-full filter blur-[80px] animate-pulse pointer-events-none"></div>

    <!-- Floating Gold Dust Particles (Pure CSS GPU Compositor) -->
    <div class="absolute inset-0 pointer-events-none overflow-hidden z-0">
      <div class="absolute top-1/4 left-1/5 w-1.5 h-1.5 rounded-full bg-[#d4af37] opacity-50 blur-[0.5px] animate-ping" style="animation-duration: 4s;"></div>
      <div class="absolute top-1/3 right-1/4 w-2 h-2 rounded-full bg-[#f7e7a7] opacity-40 blur-[0.5px] animate-pulse" style="animation-duration: 3s;"></div>
      <div class="absolute bottom-1/3 left-1/3 w-1.5 h-1.5 rounded-full bg-[#d4af37] opacity-60 blur-[0.5px] animate-ping" style="animation-duration: 5s;"></div>
      <div class="absolute top-1/2 right-1/5 w-1 h-1 rounded-full bg-amber-300 opacity-70 blur-[0.5px] animate-pulse" style="animation-duration: 3.5s;"></div>
    </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('<!-- Clean Ultra-Luxury Hero Section -->')
        if s_idx == -1:
            s_idx = content.find('<!-- Hero Section -->')

        if s_idx != -1:
            e_idx = content.find('<div class="relative z-20 max-w-5xl', s_idx)
            if e_idx != -1:
                content = content[:s_idx] + animated_backdrop_html + "\n\n    " + content[e_idx:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED LIGHTWEIGHT ANIMATED HERO BACKDROP IN: {fpath}")
