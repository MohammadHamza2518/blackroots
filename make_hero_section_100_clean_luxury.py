import os

# Clean theme.js to remove particle canvas errors
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

clean_particles_js = """function initParticleCanvas() {
  const canvas = document.getElementById('ParticleCanvas');
  if (!canvas) return;
  canvas.style.display = 'none';
}"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        p_idx = content.find('function initParticleCanvas()')
        if p_idx != -1:
            e_idx = content.find('function ', p_idx + 30)
            if e_idx == -1:
                e_idx = content.find('/* ', p_idx + 30)
            if e_idx != -1:
                content = content[:p_idx] + clean_particles_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"CLEANED PARTICLES JS IN: {jspath}")

# Update HTML files to render 100% clean luxury Hero section matching screenshot
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

clean_hero_section_html = """  <!-- Clean Ultra-Luxury Hero Section -->
  <section class="relative min-h-[85vh] flex items-center justify-center overflow-hidden bg-[#0a0b0e] py-12 sm:py-16">
    <!-- Ambient Gold Glow Backdrop -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-4xl h-96 bg-[#d4af37]/10 rounded-full filter blur-3xl pointer-events-none"></div>

    <div class="relative z-20 max-w-5xl mx-auto px-4 text-center space-y-6">
      
      <!-- Top Tagline Pill -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-black/60 border border-[#d4af37]/40 text-[#f5e4ab] text-[11px] sm:text-xs font-bold uppercase tracking-widest backdrop-blur-xl">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span>👫 100% Unisex Formula &bull; Japanese Botanical Hair Ritual</span>
      </div>

      <!-- Main Headline -->
      <h1 class="font-serif text-3xl sm:text-6xl lg:text-7xl font-bold tracking-tight text-white leading-tight">
        Say Goodbye to Grey Hair <br>
        <span class="gold-gradient-text italic">Naturally & Gently.</span>
      </h1>

      <!-- Subtitle -->
      <p class="text-sm sm:text-lg text-gray-300 max-w-3xl mx-auto font-light leading-relaxed">
        Turns grey & white hair naturally black for both <strong class="text-amber-300 font-semibold">Men & Women</strong> over regular shower washes &mdash; while eliminating scalp dandruff and stopping hair fall with 100% botanical active ingredients.
      </p>

      <!-- CTA Action Buttons -->
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 pt-2">
        <button type="button" class="js-trigger-order btn-gold-luxury btn-shimmer text-sm sm:text-base px-8 py-3.5 sm:px-10 sm:py-4 shadow-2xl cursor-pointer">
          <span>Buy Now (250ml Bottle) &mdash; &#8377; 499.00</span> <svg class="w-4 h-4 sm:w-5 sm:h-5 text-black shrink-0 inline-block -mt-0.5 ml-1.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
        </button>

        <a href="ai-consultant.html" class="px-6 py-3 rounded-full border border-amber-400/50 text-amber-300 font-bold text-xs uppercase tracking-widest hover:bg-white/10 transition-all backdrop-blur-md">
          🩺 Consult AI Hair Doctor
        </a>
      </div>

      <!-- Stock Scarcity Bar -->
      <p class="text-xs text-amber-300/90 font-medium pt-1">
        ⚡ <strong>14 Bottles Left In Stock</strong> &bull; Free Express Shipping Across India
      </p>

      <!-- Symmetrical 6-Card Trust Badges Grid -->
      <div class="pt-8 border-t border-white/10 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 text-xs font-semibold text-gray-300 max-w-5xl mx-auto">
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">✓ 100% Natural</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">✓ 0% Ammonia</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">🛡️ Derm Tested</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-amber-400/10 border border-amber-400/30 text-amber-300 font-bold text-center">👫 Men & Women</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-white/5 border border-white/10 text-center">🌿 Cruelty Free</div>
        <div class="flex items-center justify-center gap-1.5 p-2.5 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold text-center">⚡ 10-Day Action</div>
      </div>

    </div>
  </section>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('<!-- Clean')
        if s_idx == -1:
            s_idx = content.find('<!-- Tagline')
            if s_idx == -1:
                s_idx = content.find('Say Goodbye to Grey Hair')
                if s_idx != -1:
                    s_idx = content.rfind('<section', 0, s_idx)

        if s_idx != -1:
            e_idx = content.find('</section>', s_idx)
            if e_idx != -1:
                content = content[:s_idx] + clean_hero_section_html + "\n\n  " + content[e_idx+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"APPLIED CLEAN LUXURY HERO SECTION IN: {fpath}")
