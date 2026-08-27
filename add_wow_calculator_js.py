import os
import subprocess
import glob

wow_calculator_js = """/* 🔬 Ultra-Luxury Interactive Hair Result Timeline Calculator Engine */
(function() {
  let currentAge = 'mid';
  let currentGrey = 'moderate';

  const ageLabels = {
    young: '18 – 35 Years',
    mid: '36 – 50 Years',
    senior: '50+ Years'
  };

  const greyLabels = {
    light: '10% – 35% Greys',
    moderate: '35% – 65% Greys',
    heavy: '65%+ Full Greys'
  };

  const timelineData = {
    'young_light': {
      days: '5 – 7 Days',
      heading: 'Superfast Natural Melanin Activation in 5–7 Days!',
      desc: 'Younger hair follicles with initial roots react rapidly to Japanese Indigo & Amla. First 2-3 regular washes me hi grey roots completely naturally dark ho jayengi.'
    },
    'young_moderate': {
      days: '7 – 10 Days',
      heading: 'Visible Deep Dark Blackening in 7–10 Days!',
      desc: 'Aapki age aur moderate grey intensity ke liye BlackRoots ka botanical melanin stimulator 1 week ke regular shower washes me roots ko natural deep black shade provide karega.'
    },
    'young_heavy': {
      days: '10 – 14 Days',
      heading: 'Root Rejuvenation in 10–14 Days!',
      desc: 'Japanese Indigo aur Bhringraj extract pure hair shaft ko nourish karke heavy grey strands ko 10-14 days me rich black color me restore karenge.'
    },
    'mid_light': {
      days: '7 – 10 Days',
      heading: 'First Visible Dark Shade in 7–10 Days!',
      desc: 'Mid-stage roots ke liye Japanese Indigo Leaf aur Amla natural melanin production boost karte hain. Hafte me 2-3 washes ke sath roots natural black ho jati hain.'
    },
    'mid_moderate': {
      days: '10 – 14 Days',
      heading: 'Natural Deep Dark Transformation in 10–14 Days!',
      desc: 'Moderate scattered greys ke liye BlackRoots 250ml Bottle perfect hai. Regular shower washes ke sath 10-14 days me grey hair naturally black shine me convert honge.'
    },
    'mid_heavy': {
      days: '14 – 18 Days',
      heading: 'Complete Melanin Restoration in 14–18 Days!',
      desc: 'Deeper greys ke liye Japanese Indigo aur Brahmi deep cortex tak penetrate karte hain. 2 weeks ke regular use se natural uniform dark black shade achieve hota hai.'
    },
    'senior_light': {
      days: '10 – 14 Days',
      heading: 'Healthy Dark Roots in 10–14 Days!',
      desc: 'Mature hair roots ko Amla aur Camellia Oil se deep moisture aur Indigo se natural dark pigment milta hai. 10-14 days me noticeable blackening milti hai.'
    },
    'senior_moderate': {
      days: '14 – 18 Days',
      heading: 'Natural Rejuvenation in 14–18 Days!',
      desc: '50+ age me mature grey hair ko without ammonia safe blackening milti hai. 2-3 weeks me grey hair completely soft, shiny aur dark black ho jate hain.'
    },
    'senior_heavy': {
      days: '18 – 24 Days',
      heading: 'Full Ayurvedic Dark Transformation in 18–24 Days!',
      desc: 'Senior stage me full coverage ke liye 100% botanical nourishment zaroori hoti hai. Consistent 3-4 weeks regular shower washes se deep natural black color establish hota hai.'
    }
  };

  function updateCalculatorDisplay() {
    const key = `${currentAge}_${currentGrey}`;
    const data = timelineData[key] || timelineData['mid_moderate'];

    const daysBadge = document.getElementById('CalcResultDaysBadge');
    const heading = document.getElementById('CalcResultHeading');
    const desc = document.getElementById('CalcResultDesc');
    const ageLabel = document.getElementById('SelectedAgeLabel');
    const greyLabel = document.getElementById('SelectedGreyLabel');
    const outputBox = document.getElementById('CalcResultOutput');

    if (daysBadge) daysBadge.textContent = data.days;
    if (heading) heading.textContent = data.heading;
    if (desc) desc.textContent = data.desc;
    if (ageLabel) ageLabel.textContent = ageLabels[currentAge] || '';
    if (greyLabel) greyLabel.textContent = greyLabels[currentGrey] || '';

    if (outputBox) {
      outputBox.classList.remove('hidden');
      outputBox.style.display = 'block';
    }
  }

  function setupCalculatorEventListeners() {
    // Age button clicks
    document.querySelectorAll('.js-calc-age-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.js-calc-age-btn').forEach(b => {
          b.className = 'js-calc-age-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer';
          const title = b.querySelector('.text-xs');
          const sub = b.querySelector('.text-\\[9px\\]');
          if (title) title.className = 'text-xs font-bold text-white block';
          if (sub) sub.className = 'text-[9px] text-gray-400 uppercase tracking-tight block mt-0.5';
        });

        btn.className = 'js-calc-age-btn active-calc-btn p-3 sm:p-4 rounded-2xl bg-gradient-to-r from-[#d4af37]/20 to-[#aa7c11]/10 border-2 border-[#d4af37] text-center shadow-lg transition-all cursor-pointer';
        const title = btn.querySelector('.text-xs');
        const sub = btn.querySelector('.text-\\[9px\\]');
        if (title) title.className = 'text-xs font-bold text-amber-300 block';
        if (sub) sub.className = 'text-[9px] text-amber-200 uppercase tracking-tight block mt-0.5';

        currentAge = btn.getAttribute('data-age') || 'mid';
        updateCalculatorDisplay();
      });
    });

    // Grey intensity button clicks
    document.querySelectorAll('.js-calc-grey-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.js-calc-grey-btn').forEach(b => {
          b.className = 'js-calc-grey-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer';
          const title = b.querySelector('.text-xs');
          const sub = b.querySelector('.text-\\[9px\\]');
          if (title) title.className = 'text-xs font-black text-white block mb-0.5';
          if (sub) sub.className = 'text-[9px] text-gray-400 uppercase tracking-tight block';
        });

        btn.className = 'js-calc-grey-btn active-calc-btn p-3 sm:p-4 rounded-2xl bg-gradient-to-r from-[#d4af37]/20 to-[#aa7c11]/10 border-2 border-[#d4af37] text-center shadow-lg transition-all cursor-pointer';
        const title = btn.querySelector('.text-xs');
        const sub = btn.querySelector('.text-\\[9px\\]');
        if (title) title.className = 'text-xs font-black text-amber-300 block mb-0.5';
        if (sub) sub.className = 'text-[9px] text-amber-200 uppercase tracking-tight block';

        currentGrey = btn.getAttribute('data-grey') || 'moderate';
        updateCalculatorDisplay();
      });
    });

    // Calculate CTA button click
    const calcBtn = document.getElementById('BtnRunHairCalculator');
    if (calcBtn) {
      calcBtn.addEventListener('click', (e) => {
        e.preventDefault();
        updateCalculatorDisplay();
        const outputBox = document.getElementById('CalcResultOutput');
        if (outputBox) {
          outputBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      });
    }
  }

  window.calculateHairResultTimeline = function() {
    updateCalculatorDisplay();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupCalculatorEventListeners);
  } else {
    setupCalculatorEventListeners();
  }
})();"""

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

for f in theme_js_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content + "\n\n" + wow_calculator_js
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Added WOW Hair Calculator JS engine to {f}")

for f in theme_js_files:
    res = subprocess.run(['node', '-c', f], capture_output=True, text=True)
    print(f, "Syntax check return code:", res.returncode)
    if res.returncode != 0:
        print("  Error:", res.stderr)
