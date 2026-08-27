import os
import glob
import subprocess

# 1. Update HTML files with simple, clean, customer-friendly UI
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

easy_clean_calculator_html = """  <!-- Expected Result Timeline Calculator (Customer-Friendly Clean Interactive Experience) -->
  <section class="py-16 sm:py-20 bg-gradient-to-b from-[#08090c] via-[#0e1017] to-[#08090c] border-b border-[#d4af37]/20 relative overflow-hidden" id="HairTimelineCalculatorSection">
    <!-- Ambient Soft Glow -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#d4af37]/10 rounded-full filter blur-3xl pointer-events-none"></div>

    <div class="max-w-3xl mx-auto px-4 sm:px-6 relative z-10 text-center space-y-6">
      
      <!-- Clean Header -->
      <div>
        <div class="inline-flex items-center justify-center gap-1.5 px-3.5 py-1.5 rounded-full bg-[#d4af37]/10 border border-[#d4af37]/50 text-[#d4af37] text-[10px] sm:text-xs font-extrabold uppercase tracking-wide backdrop-blur-xl shadow-md mb-3">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse shrink-0"></span>
          <span>⚡ LIVE RESULT ESTIMATOR</span>
        </div>
        <h2 class="font-serif text-2xl sm:text-4xl font-bold text-white tracking-tight">
          When Will You See <span class="gold-gradient-text italic">Black Hair Results?</span>
        </h2>
        <p class="text-gray-300 text-xs sm:text-sm font-light mt-1">
          Select your age & grey hair level to see your estimated natural timeline.
        </p>
      </div>

      <!-- Main Clean Card -->
      <div class="glass-panel-luxury p-5 sm:p-8 rounded-3xl border border-[#d4af37]/40 text-left space-y-6 shadow-2xl backdrop-blur-xl">
        
        <!-- Step 1: Age Group -->
        <div class="space-y-2">
          <label class="block text-xs font-bold text-amber-300 uppercase tracking-wider">
            1. Select Your Age:
          </label>
          <div class="grid grid-cols-3 gap-2">
            <button type="button" id="AgePill_young" onclick="window.pickAge('young')" class="js-age-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer">
              18 – 35 Yrs
            </button>
            <button type="button" id="AgePill_mid" onclick="window.pickAge('mid')" class="js-age-pill py-2.5 px-2 rounded-xl bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black border border-[#fff3b0] text-center text-xs font-black shadow-lg transition-all cursor-pointer">
              36 – 50 Yrs
            </button>
            <button type="button" id="AgePill_senior" onclick="window.pickAge('senior')" class="js-age-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer">
              50+ Yrs
            </button>
          </div>
        </div>

        <!-- Step 2: Grey Level -->
        <div class="space-y-2">
          <label class="block text-xs font-bold text-amber-300 uppercase tracking-wider">
            2. Grey Hair Amount:
          </label>
          <div class="grid grid-cols-3 gap-2">
            <button type="button" id="GreyPill_light" onclick="window.pickGrey('light')" class="js-grey-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer">
              Few Greys (10-35%)
            </button>
            <button type="button" id="GreyPill_moderate" onclick="window.pickGrey('moderate')" class="js-grey-pill py-2.5 px-2 rounded-xl bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black border border-[#fff3b0] text-center text-xs font-black shadow-lg transition-all cursor-pointer">
              Moderate (35-65%)
            </button>
            <button type="button" id="GreyPill_heavy" onclick="window.pickGrey('heavy')" class="js-grey-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer">
              Heavy (65%+)
            </button>
          </div>
        </div>

        <!-- Dynamic Live Result Box -->
        <div class="p-5 sm:p-6 rounded-2xl bg-gradient-to-br from-[#16130a] via-[#0d0f14] to-[#08090c] border border-[#d4af37]/70 space-y-4 shadow-xl">
          
          <div class="flex items-center justify-between border-b border-white/10 pb-3">
            <span class="text-xs font-extrabold text-emerald-400 uppercase tracking-wide flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
              Estimated Natural Timeline:
            </span>
            <span id="SimpleDaysBadge" class="bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-xs sm:text-sm font-black px-3 py-1 rounded-full uppercase shadow-md">
              10 &ndash; 14 Days
            </span>
          </div>

          <p id="SimpleResultText" class="text-xs sm:text-sm text-gray-200 leading-relaxed">
            Japanese Indigo Leaf &amp; Amla melanin boost karenge. Regular shower washes ke sath <strong>10–14 days</strong> me roots naturally dark black shade me convert ho jayengi.
          </p>

          <div class="pt-2 flex flex-col sm:flex-row items-center justify-between gap-3 border-t border-white/10">
            <span class="text-[11px] text-gray-300">
              🌿 100% Botanical &bull; Zero Ammonia &bull; No Side Effects
            </span>
            <a href="product.html" class="js-trigger-order group relative inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs px-5 py-2.5 rounded-xl border border-[#fff3b0]/70 shadow-md hover:scale-105 transition-all uppercase tracking-wider shrink-0 w-full sm:w-auto text-center">
              <span>ORDER NOW &bull; &#8377;499</span>
              <span class="w-5 h-5 rounded-lg bg-black text-[#d4af37] flex items-center justify-center font-bold text-xs">
                &rarr;
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

        s_idx = content.find('Expected Hair Result')
        if s_idx == -1:
            s_idx = content.find('Expected Result Timeline')
        if s_idx == -1:
            s_idx = content.find('When Will You See')

        if s_idx != -1:
            sec_start = content.rfind('<section', 0, s_idx)
            sec_end = content.find('</section>', s_idx) + 10
            if sec_start != -1 and sec_end != -1:
                content = content[:sec_start] + easy_clean_calculator_html.strip() + "\n\n  " + content[sec_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"APPLIED EASY CLEAN CALCULATOR HTML IN: {fpath}")

# 2. Update theme.js files with instant pickAge & pickGrey logic
easy_calc_js = """/* 🌿 Simple & Customer-Friendly Hair Timeline Calculator Engine */
(function() {
  window.simpleAge = 'mid';
  window.simpleGrey = 'moderate';

  const simpleData = {
    'young_light': {
      days: '5 – 7 Days',
      text: 'Younger hair follicles initial roots par fast react karte hain. First 2-3 regular washes (5–7 days) me hi roots naturally dark black ho jayengi.'
    },
    'young_moderate': {
      days: '7 – 10 Days',
      text: 'BlackRoots ka botanical melanin formula regular shower washes ke sath 7–10 days me roots ko uniform deep dark shade provide karega.'
    },
    'young_heavy': {
      days: '10 – 14 Days',
      text: 'Heavy grey strands ko Japanese Indigo aur Bhringraj 10–14 days me naturally rich black color me restore karte hain.'
    },
    'mid_light': {
      days: '7 – 10 Days',
      text: 'Japanese Indigo Leaf aur Amla natural melanin boost karte hain. Regular 2-3 washes (7–10 days) me roots natural dark black ho jati hain.'
    },
    'mid_moderate': {
      days: '10 – 14 Days',
      text: 'Moderate scattered greys ke liye BlackRoots 250ml perfect hai. Regular washes ke sath 10–14 days me grey hair naturally deep black shine me convert honge.'
    },
    'mid_heavy': {
      days: '14 – 18 Days',
      text: 'Japanese Indigo aur Brahmi deep cortex tak nourish karte hain. 2 weeks ke regular use se uniform dark black shade achieve hota hai.'
    },
    'senior_light': {
      days: '10 – 14 Days',
      text: 'Mature hair roots ko Amla aur Indigo se safe botanical nourishment milti hai. 10–14 days me noticeable natural blackening dikhti hai.'
    },
    'senior_moderate': {
      days: '14 – 18 Days',
      text: '50+ age me mature grey hair ko without ammonia safe blackening milti hai. 2-3 weeks me grey hair completely shiny aur dark black ho jate hain.'
    },
    'senior_heavy': {
      days: '18 – 24 Days',
      text: 'Senior stage me full coverage ke liye regular shower washes zaroori hote hain. 3-4 weeks me deep natural black color establish hota hai.'
    }
  };

  function updateSimpleCalculator() {
    const key = `${window.simpleAge}_${window.simpleGrey}`;
    const item = simpleData[key] || simpleData['mid_moderate'];

    const badge = document.getElementById('SimpleDaysBadge');
    const textEl = document.getElementById('SimpleResultText');

    if (badge) badge.textContent = item.days;
    if (textEl) textEl.innerHTML = item.text;
  }

  window.pickAge = function(age) {
    window.simpleAge = age;
    ['young', 'mid', 'senior'].forEach(a => {
      const btn = document.getElementById('AgePill_' + a);
      if (!btn) return;
      if (a === age) {
        btn.className = 'js-age-pill py-2.5 px-2 rounded-xl bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black border border-[#fff3b0] text-center text-xs font-black shadow-lg transition-all cursor-pointer';
      } else {
        btn.className = 'js-age-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer';
      }
    });
    updateSimpleCalculator();
  };

  window.pickGrey = function(grey) {
    window.simpleGrey = grey;
    ['light', 'moderate', 'heavy'].forEach(g => {
      const btn = document.getElementById('GreyPill_' + g);
      if (!btn) return;
      if (g === grey) {
        btn.className = 'js-grey-pill py-2.5 px-2 rounded-xl bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black border border-[#fff3b0] text-center text-xs font-black shadow-lg transition-all cursor-pointer';
      } else {
        btn.className = 'js-grey-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer';
      }
    });
    updateSimpleCalculator();
  };
})();"""

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

for f in theme_js_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    idx = content.find('/* 🔬 Ultra-Luxury Interactive')
    if idx == -1:
        idx = content.find('/* 🌿 Simple & Customer-Friendly')
    
    if idx != -1:
        content = content[:idx] + easy_calc_js
    else:
        content += "\n\n" + easy_calc_js

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"APPLIED EASY CALCULATOR JS IN: {f}")

for f in theme_js_files:
    res = subprocess.run(['node', '-c', f], capture_output=True, text=True)
    print(f, "Syntax check return code:", res.returncode)
