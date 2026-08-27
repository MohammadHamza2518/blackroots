import os

# 1. Update HTML files across index.html, demo_lab/index.html, preview/index.html
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

new_pincode_checker_html = """        <div class="flex flex-col sm:flex-row gap-3">
          <input type="text" id="HomePincodeInput" maxlength="6" placeholder="Enter 6-Digit Pincode" class="flex-1 px-5 py-3.5 rounded-2xl bg-black/90 border border-white/20 text-sm text-white font-bold text-center tracking-widest focus:border-[#d4af37] focus:outline-none">
          <button type="button" id="HomeCheckPincodeBtn" class="group relative inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs sm:text-sm px-6 py-3.5 rounded-2xl border border-[#fff3b0]/70 shadow-lg hover:scale-105 transition-transform cursor-pointer uppercase tracking-wider shrink-0">
            <span>CHECK PINCODE</span>
            <span class="text-black font-black">&rarr;</span>
          </button>
        </div>

        <!-- Live Pincode Result Banner Container (Hidden By Default, Appears Dynamic) -->
        <div id="HomePincodeResult" class="hidden mt-4 p-4 rounded-2xl bg-emerald-950/90 border border-emerald-500/60 text-center shadow-xl backdrop-blur-md transition-all duration-300">
          <div class="flex items-center justify-center gap-2 text-emerald-300 font-extrabold text-xs sm:text-sm uppercase tracking-wider mb-1">
            <span>⚡ PINCODE <span id="ResultPincodeNum" class="text-white font-black text-base underline decoration-amber-400"></span> IS 100% SERVICEABLE!</span>
          </div>
          <p id="ResultDeliveryTimeline" class="text-xs text-gray-200 font-medium">
            🚚 <strong>FREE Express Shipping</strong> &bull; Expected Doorstep Delivery By <strong id="ResultExpectedDate" class="text-amber-300 font-bold"></strong>
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
            b_end = content.find('<!-- 4 Express Delivery Pillars -->', s_idx)
            if b_start != -1 and b_end != -1:
                # Find the div closing before 4 pillars
                div_end = content.rfind('</div>', b_start, b_end)
                if div_end != -1:
                    content = content[:b_start] + new_pincode_checker_html.strip() + "\n\n        " + content[div_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REBUILT PINCODE CHECKER HTML IN: {fpath}")

# 2. Rebuild theme.js Pincode engine with 100% Bulletproof Event Handlers
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

bulletproof_pincode_js = """/* 🚚 100% Bulletproof Mobile & Desktop India Pincode Calculator Engine */
(function() {
  let trackedPincode = '';

  function getDeliveryDateString(pin) {
    const today = new Date();
    let daysToAdd = 3;
    const clean = (pin || '').toString().replace(/\\D/g, '');

    if (clean.startsWith('20') || clean.startsWith('11') || clean.startsWith('40') || clean.startsWith('70') || clean.startsWith('56') || clean.startsWith('50')) {
      daysToAdd = 2;
    }

    const deliveryDate = new Date(today);
    deliveryDate.setDate(today.getDate() + daysToAdd);

    const options = { weekday: 'long', month: 'short', day: 'numeric' };
    return deliveryDate.toLocaleDateString('en-IN', options);
  }

  function processPincodeCheck(isUserClick = false) {
    const inputEl = document.getElementById('HomePincodeInput');
    const resultBox = document.getElementById('HomePincodeResult');
    const numSpan = document.getElementById('ResultPincodeNum');
    const dateSpan = document.getElementById('ResultExpectedDate');

    if (!inputEl || !resultBox) return;

    let currentVal = (inputEl.value || trackedPincode || '').toString().replace(/\\D/g, '').slice(0, 6);

    if (currentVal.length < 6) {
      if (isUserClick) {
        alert('Please enter a valid 6-digit Indian delivery pincode (e.g. 208001)');
        inputEl.focus();
      }
      return;
    }

    trackedPincode = currentVal;
    inputEl.value = currentVal;

    const deliveryTimeline = getDeliveryDateString(currentVal);

    if (numSpan) numSpan.textContent = currentVal;
    if (dateSpan) dateSpan.textContent = deliveryTimeline;

    resultBox.classList.remove('hidden');
    resultBox.style.display = 'block';
  }

  function attachPincodeListeners() {
    const inputEl = document.getElementById('HomePincodeInput');
    const btnEl = document.getElementById('HomeCheckPincodeBtn');

    if (!inputEl || !btnEl) return;

    ['input', 'keyup', 'change', 'blur'].forEach(evt => {
      inputEl.addEventListener(evt, function(e) {
        const sanitized = (e.target.value || '').replace(/\\D/g, '').slice(0, 6);
        trackedPincode = sanitized;
        if (sanitized.length === 6) {
          processPincodeCheck(false);
        }
      });
    });

    ['click', 'touchstart'].forEach(evt => {
      btnEl.addEventListener(evt, function(e) {
        e.preventDefault();
        processPincodeCheck(true);
      });
    });

    inputEl.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        processPincodeCheck(true);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachPincodeListeners);
  } else {
    attachPincodeListeners();
  }

  // Also bind to window for emergency fallback calls
  window.executePincodeCheck = function(isClick) {
    processPincodeCheck(isClick);
  };
})();"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        p_idx = content.find('/* 🚚 100% Bulletproof')
        if p_idx == -1:
            p_idx = content.find('/* 🚚 Professional India Pincode')
        if p_idx == -1:
            p_idx = content.find('/* 🚚 Global Bulletproof')
        if p_idx == -1:
            p_idx = content.find('window.calculateDeliveryDateStr')

        if p_idx != -1:
            content = content[:p_idx] + bulletproof_pincode_js
        else:
            content += "\n\n" + bulletproof_pincode_js

        with open(jspath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REBUILT BULLETPROOF PINCODE JS ENGINE IN: {jspath}")
