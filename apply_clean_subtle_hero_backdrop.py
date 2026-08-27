import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

clean_subtle_backdrop_html = """  <!-- Clean Ultra-Luxury Hero Section (Minimalist Soft Gold Ambient Glow - 0% Lag) -->
  <section class="relative min-h-[85vh] flex items-center justify-center overflow-hidden bg-[#090a0d] py-12 sm:py-16 select-none border-b border-[#d4af37]/20">
    
    <!-- Single Soft Ambient Gold Glow (Ultra-Lightweight & Clean) -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-3xl h-80 bg-[#d4af37]/10 rounded-full filter blur-3xl pointer-events-none"></div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('<!-- Hero Section')
        if s_idx == -1:
            s_idx = content.find('<!-- Clean Ultra-Luxury Hero Section')

        if s_idx != -1:
            e_idx = content.find('<div class="relative z-20 max-w-5xl', s_idx)
            if e_idx != -1:
                content = content[:s_idx] + clean_subtle_backdrop_html + "\n\n    " + content[e_idx:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED CLEAN SUBTLE HERO BACKDROP IN: {fpath}")
