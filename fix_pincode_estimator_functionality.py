import os

# 1. Update HTML files to fix button ID, remove js-trigger-order from pincode button, and add result container
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

old_pincode_box = """        <div class="flex flex-col sm:flex-row gap-3">
          <input type="text" id="HomePincodeInput" maxlength="6" placeholder="Enter 6-Digit Pincode" class="flex-1 px-5 py-3.5 rounded-2xl bg-black/90 border border-white/20 text-sm text-white font-bold text-center tracking-widest focus:border-[#d4af37] focus:outline-none">
          <button type="button" class="js-trigger-order group relative inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs sm:text-sm px-6 py-3 rounded-xl border border-[#fff3b0]/70 shadow-[0_10px_25px_rgba(212,175,55,0.25)] hover:shadow-[0_15px_35px_rgba(212,175,55,0.4)] transition-all transform hover:-translate-y-0.5 cursor-pointer uppercase tracking-wider overflow-hidden w-full sm:w-auto">
              <span class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/40 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000 ease-out pointer-events-none"></span>
              <span class="flex items-center gap-2 relative z-10">
                <span class="font-black tracking-wider">ORDER NOW</span>
                <span class="text-black/40 font-normal">&bull;</span>
                <span class="font-black text-sm text-black">&#8377;499</span>
              </span>
              <span class="w-6 h-6 rounded-lg bg-black text-[#d4af37] flex items-center justify-center shadow-md shrink-0 relative z-10 group-hover:scale-110 transition-transform">
                <svg class="w-3.5 h-3.5 text-[#d4af37]" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
              </span>
            </button>
        </div>"""

new_pincode_box = """        <div class="flex flex-col sm:flex-row gap-3">
          <input type="text" id="HomePincodeInput" maxlength="6" value="208001" placeholder="Enter 6-Digit Pincode" class="flex-1 px-5 py-3.5 rounded-2xl bg-black/90 border border-white/20 text-sm text-white font-bold text-center tracking-widest focus:border-[#d4af37] focus:outline-none">
          <button type="button" id="HomeCheckPincodeBtn" class="group relative inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs sm:text-sm px-6 py-3.5 rounded-2xl border border-[#fff3b0]/70 shadow-lg hover:scale-105 transition-transform cursor-pointer uppercase tracking-wider shrink-0">
            <span>CHECK PINCODE</span>
            <span class="text-black font-black">&rarr;</span>
          </button>
        </div>

        <!-- Live Pincode Result Banner Container -->
        <div id="HomePincodeResult" class="hidden mt-4 p-4 rounded-2xl bg-emerald-950/90 border border-emerald-500/60 text-center shadow-xl backdrop-blur-md">
          <div class="flex items-center justify-center gap-2 text-emerald-300 font-extrabold text-xs sm:text-sm uppercase tracking-wider mb-1">
            <span>⚡ PINCODE <span id="ResultPincodeNum" class="text-white">208001</span> IS 100% SERVICEABLE!</span>
          </div>
          <p id="ResultDeliveryTimeline" class="text-xs text-gray-200 font-medium">
            🚚 <strong>FREE Express Shipping</strong> &bull; Expected Doorstep Delivery By <strong id="ResultExpectedDate" class="text-amber-300 font-bold">Monday, Aug 17</strong>
          </p>
          <div class="flex items-center justify-center gap-3 text-[10px] text-emerald-400 font-bold uppercase tracking-widest mt-2 pt-2 border-t border-emerald-500/20">
            <span>✓ Cash On Delivery</span> &bull; <span>✓ 24hr Dispatch</span> &bull; <span>✓ Discreet Box</span>
          </div>
        </div>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('HomePincodeInput')
        if s_idx != -1:
            b_start = content.rfind('<div class="flex flex-col', 0, s_idx)
            b_end = content.find('</div>', s_idx) + 6
            if b_start != -1 and b_end != -1:
                content = content[:b_start] + new_pincode_box.strip() + content[b_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED PINCODE ESTIMATOR HTML IN: {fpath}")

# 2. Add Live Pincode Calculator JS engine to theme.js
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

pincode_calculator_js = """/* 🚚 Live Pincode Delivery Timeline Calculator Engine */
function initPincodeChecker() {
  const pincodeInput = document.getElementById('HomePincodeInput');
  const checkBtn = document.getElementById('HomeCheckPincodeBtn');
  const resultBox = document.getElementById('HomePincodeResult');
  const resultPincodeNum = document.getElementById('ResultPincodeNum');
  const resultExpectedDate = document.getElementById('ResultExpectedDate');

  if (!pincodeInput || !checkBtn || !resultBox) return;

  function calculateDeliveryDate(pin) {
    const today = new Date();
    let daysToAdd = 3;

    // Fast 1-2 days for UP / Delhi NCR / Metro pincodes
    if (pin.startsWith('20') || pin.startsWith('11') || pin.startsWith('40') || pin.startsWith('70') || pin.startsWith('56') || pin.startsWith('50')) {
      daysToAdd = 2;
    }

    const deliveryDate = new Date(today);
    deliveryDate.setDate(today.getDate() + daysToAdd);

    const options = { weekday: 'long', month: 'short', day: 'numeric' };
    return deliveryDate.toLocaleDateString('en-IN', options);
  }

  function runCheck() {
    const pin = pincodeInput.value.trim();

    if (!pin || pin.length < 6 || isNaN(pin)) {
      alert('Please enter a valid 6-digit Indian delivery pincode (e.g. 208001)');
      pincodeInput.focus();
      return;
    }

    const dateStr = calculateDeliveryDate(pin);

    if (resultPincodeNum) resultPincodeNum.textContent = pin;
    if (resultExpectedDate) resultExpectedDate.textContent = dateStr;

    resultBox.classList.remove('hidden');
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  checkBtn.addEventListener('click', runCheck);

  pincodeInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      runCheck();
    }
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPincodeChecker);
} else {
  initPincodeChecker();
}"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'initPincodeChecker' not in content:
            content += "\n\n" + pincode_calculator_js
            with open(jspath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"ADDED LIVE PINCODE CALCULATOR JS TO: {jspath}")
