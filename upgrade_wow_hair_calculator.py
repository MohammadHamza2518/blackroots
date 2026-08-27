import os

# 1. Update HTML files with modern WOW interactive UI for Hair Timeline Calculator
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

wow_calculator_html = """  <!-- Expected Result Timeline Calculator (Ultra-Luxury WOW Interactive D2C Experience) -->
  <section class="py-20 bg-gradient-to-b from-[#08090c] via-[#0f1118] to-[#08090c] border-b border-[#d4af37]/20 relative overflow-hidden">
    <!-- Ambient Gold Glow Backdrops -->
    <div class="absolute top-1/3 left-1/2 -translate-x-1/2 w-[600px] h-[350px] bg-[#d4af37]/10 rounded-full filter blur-[100px] pointer-events-none"></div>

    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center space-y-10">
      
      <!-- Section Header Badge -->
      <div>
        <div class="inline-flex items-center justify-center gap-2 px-4 py-1.5 rounded-full bg-[#d4af37]/10 border border-[#d4af37]/50 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-wide backdrop-blur-xl shadow-lg mb-3">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></span>
          <span>🔬 AI-POWERED RESULT PREDICTOR</span>
        </div>
        <h2 class="font-serif text-3xl sm:text-5xl font-bold text-white tracking-tight">
          Expected Hair Result <span class="gold-gradient-text italic">Timeline Calculator</span>
        </h2>
        <p class="text-gray-300 text-xs sm:text-sm max-w-xl mx-auto font-light leading-relaxed mt-2">
          Select your current age & grey hair intensity to calculate your personalized Japanese botanical melanin activation timeline.
        </p>
      </div>

      <!-- Main Interactive Calculator Panel -->
      <div class="glass-panel-luxury p-6 sm:p-10 rounded-3xl border-2 border-[#d4af37]/40 text-left space-y-8 shadow-[0_20px_50px_rgba(0,0,0,0.8)] backdrop-blur-2xl">
        
        <!-- Step 1: Age Selection -->
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <label class="text-xs font-black text-amber-300 uppercase tracking-wider flex items-center gap-2">
              <span class="w-5 h-5 rounded-full bg-amber-400/20 text-amber-300 flex items-center justify-center text-[10px] font-black border border-amber-400/40">1</span>
              SELECT YOUR AGE GROUP
            </label>
            <span id="SelectedAgeLabel" class="text-[11px] font-bold text-[#d4af37]">36 – 50 Years</span>
          </div>

          <div class="grid grid-cols-3 gap-2.5 sm:gap-4">
            <button type="button" class="js-calc-age-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer" data-age="young">
              <span class="text-lg block mb-1">🌱</span>
              <span class="text-xs font-bold text-white block">18 – 35 Yrs</span>
              <span class="text-[9px] text-gray-400 uppercase tracking-tight block mt-0.5">Early Stage</span>
            </button>

            <button type="button" class="js-calc-age-btn active-calc-btn p-3 sm:p-4 rounded-2xl bg-gradient-to-r from-[#d4af37]/20 to-[#aa7c11]/10 border-2 border-[#d4af37] text-center shadow-lg transition-all cursor-pointer" data-age="mid">
              <span class="text-lg block mb-1">🌿</span>
              <span class="text-xs font-bold text-amber-300 block">36 – 50 Yrs</span>
              <span class="text-[9px] text-amber-200 uppercase tracking-tight block mt-0.5">Moderate Stage</span>
            </button>

            <button type="button" class="js-calc-age-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer" data-age="senior">
              <span class="text-lg block mb-1">🌳</span>
              <span class="text-xs font-bold text-white block">50+ Yrs</span>
              <span class="text-[9px] text-gray-400 uppercase tracking-tight block mt-0.5">Senior Stage</span>
            </button>
          </div>
        </div>

        <!-- Step 2: Grey Hair Intensity Selection -->
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <label class="text-xs font-black text-amber-300 uppercase tracking-wider flex items-center gap-2">
              <span class="w-5 h-5 rounded-full bg-amber-400/20 text-amber-300 flex items-center justify-center text-[10px] font-black border border-amber-400/40">2</span>
              GREY HAIR PERCENTAGE
            </label>
            <span id="SelectedGreyLabel" class="text-[11px] font-bold text-[#d4af37]">35% – 65% Greys</span>
          </div>

          <div class="grid grid-cols-3 gap-2.5 sm:gap-4">
            <button type="button" class="js-calc-grey-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer" data-grey="light">
              <span class="text-xs font-black text-white block mb-0.5">10% – 35%</span>
              <span class="text-[9px] text-gray-400 uppercase tracking-tight block">Initial Roots</span>
            </button>

            <button type="button" class="js-calc-grey-btn active-calc-btn p-3 sm:p-4 rounded-2xl bg-gradient-to-r from-[#d4af37]/20 to-[#aa7c11]/10 border-2 border-[#d4af37] text-center shadow-lg transition-all cursor-pointer" data-grey="moderate">
              <span class="text-xs font-black text-amber-300 block mb-0.5">35% – 65%</span>
              <span class="text-[9px] text-amber-200 uppercase tracking-tight block">Scattered Greys</span>
            </button>

            <button type="button" class="js-calc-grey-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer" data-grey="heavy">
              <span class="text-xs font-black text-white block mb-0.5">65%+</span>
              <span class="text-[9px] text-gray-400 uppercase tracking-tight block">Full Greys</span>
            </button>
          </div>
        </div>

        <!-- Action Button -->
        <button type="button" id="BtnRunHairCalculator" onclick="window.calculateHairResultTimeline();" class="group relative w-full inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs sm:text-sm px-6 py-4 rounded-2xl border-2 border-[#fff3b0]/70 shadow-[0_15px_35px_rgba(212,175,55,0.35)] hover:shadow-[0_20px_45px_rgba(212,175,55,0.5)] transition-all transform hover:-translate-y-0.5 cursor-pointer uppercase tracking-wider overflow-hidden">
          <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/40 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-out pointer-events-none"></span>
          <span class="relative z-10 font-black">⚡ CALCULATE EXPECTED TIMELINE</span>
          <span class="w-6 h-6 rounded-lg bg-black text-[#d4af37] flex items-center justify-center font-black text-xs shadow-md shrink-0 relative z-10 group-hover:scale-110 transition-transform">
            &rarr;
          </span>
        </button>

        <!-- Dynamic WOW Result Box (Animated Timeline Protocol) -->
        <div id="CalcResultOutput" class="p-6 sm:p-8 rounded-2xl bg-gradient-to-br from-[#16130a] via-[#0d0f14] to-[#08090c] border-2 border-[#d4af37] space-y-6 shadow-2xl transition-all duration-300">
          
          <!-- Header Bar -->
          <div class="flex items-center justify-between border-b border-[#d4af37]/30 pb-4">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-ping"></span>
              <span class="text-xs font-black text-[#d4af37] uppercase tracking-wider">🎯 CLINICALLY ESTIMATED TIMELINE</span>
            </div>
            <span id="CalcResultDaysBadge" class="bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-xs sm:text-sm font-black px-3.5 py-1 rounded-full uppercase shadow-md">
              10 &ndash; 14 Days
            </span>
          </div>

          <!-- Main Result Narrative -->
          <div class="space-y-2">
            <h4 id="CalcResultHeading" class="font-serif text-lg sm:text-2xl font-bold text-white">
              First Visible Natural Darkening in 10&ndash;14 Days!
            </h4>
            <p id="CalcResultDesc" class="text-xs sm:text-sm text-gray-300 leading-relaxed font-light">
              Japanese Indigo Leaf aur Amla aapke hair follicles me natural melanin production ko nourish karenge. Regular shower washes ke sath grey roots naturally deep black shade me convert hone lagengi.
            </p>
          </div>

          <!-- 3-Phase Transformation Journey Progress Bar -->
          <div class="space-y-2 pt-2 border-t border-white/10">
            <span class="text-[10px] text-gray-400 font-bold uppercase tracking-widest block">🌿 3-Phase Melanin Activation Progression</span>
            <div class="grid grid-cols-3 gap-2 text-center text-[10px]">
              <div class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30">
                <span class="font-bold text-emerald-400 block">Phase 1 (Day 1-3)</span>
                <span class="text-gray-300 text-[9px]">Scalp Detox & Dandruff Free</span>
              </div>
              <div class="p-2.5 rounded-xl bg-amber-950/40 border border-amber-500/30">
                <span class="font-bold text-amber-300 block">Phase 2 (Day 4-8)</span>
                <span class="text-gray-300 text-[9px]">Melanin Activation & Roots Darkening</span>
              </div>
              <div class="p-2.5 rounded-xl bg-[#d4af37]/20 border border-[#d4af37]/50">
                <span class="font-bold text-[#f7e7a7] block">Phase 3 (Day 10+)</span>
                <span class="text-gray-300 text-[9px]">Deep Natural Black Shine</span>
              </div>
            </div>
          </div>

          <!-- Recommended Protocol Box & CTA -->
          <div class="pt-4 flex flex-col sm:flex-row items-center justify-between gap-4 border-t border-[#d4af37]/20">
            <div class="text-xs text-emerald-400 font-bold flex items-center gap-1.5">
              <span>🛡️ 100% Botanical Formula</span> &bull; <span>Zero Ammonia</span> &bull; <span>No Side Effects</span>
            </div>
            
            <a href="product.html" class="js-trigger-order group relative inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs sm:text-sm px-6 py-3 rounded-xl border border-[#fff3b0]/70 shadow-lg hover:scale-105 transition-all uppercase tracking-wider shrink-0">
              <span class="font-black">ORDER NOW &bull; &#8377;499</span>
              <span class="w-6 h-6 rounded-lg bg-black text-[#d4af37] flex items-center justify-center font-black text-xs shadow-md">
                <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
              </span>
            </a>
          </div>

        </div>
      </div>
    </div>
  </section>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('Expected Result Timeline')
        if s_idx != -1:
            sec_start = content.rfind('<section', 0, s_idx)
            sec_end = content.find('</section>', s_idx) + 10
            if sec_start != -1 and sec_end != -1:
                content = content[:sec_start] + wow_calculator_html.strip() + "\n\n  " + content[sec_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED WOW HAIR TIMELINE CALCULATOR HTML IN: {fpath}")
