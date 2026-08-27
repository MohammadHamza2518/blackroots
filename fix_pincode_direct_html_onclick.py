import os

# 1. Update HTML files: remove value="208001" attribute, add direct onclick & onkeyup attributes
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove hardcoded value="208001" from input tag
        content = content.replace('value="208001"', '')

        # Add direct inline onclick/onkeyup handlers for 1000% bulletproof execution
        old_input = '<input type="text" id="HomePincodeInput" maxlength="6"  placeholder="Enter 6-Digit Pincode" class="flex-1 px-5 py-3.5 rounded-2xl bg-black/90 border border-white/20 text-sm text-white font-bold text-center tracking-widest focus:border-[#d4af37] focus:outline-none">'
        new_input = '<input type="text" id="HomePincodeInput" maxlength="6" placeholder="Enter 6-Digit Pincode" onkeyup="executePincodeCheck()" oninput="executePincodeCheck()" class="flex-1 px-5 py-3.5 rounded-2xl bg-black/90 border border-white/20 text-sm text-white font-bold text-center tracking-widest focus:border-[#d4af37] focus:outline-none">'

        old_btn = '<button type="button" id="HomeCheckPincodeBtn" class="group relative inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs sm:text-sm px-6 py-3.5 rounded-2xl border border-[#fff3b0]/70 shadow-lg hover:scale-105 transition-transform cursor-pointer uppercase tracking-wider shrink-0">'
        new_btn = '<button type="button" id="HomeCheckPincodeBtn" onclick="executePincodeCheck()" class="group relative inline-flex items-center justify-center gap-2 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs sm:text-sm px-6 py-3.5 rounded-2xl border border-[#fff3b0]/70 shadow-lg hover:scale-105 transition-transform cursor-pointer uppercase tracking-wider shrink-0">'

        content = content.replace(old_input, new_input)
        content = content.replace(old_btn, new_btn)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED DIRECT HTML ONCLICK & REMOVED HARDCODED VALUE IN: {fpath}")

# 2. Update theme.js to make executePincodeCheck global (window.executePincodeCheck)
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

global_pincode_js = """/* 🚚 Global Bulletproof Window-Bound Pincode Checker Engine */
window.calculateDeliveryDateStr = function(pin) {
  const today = new Date();
  let daysToAdd = 3;

  if (pin.startsWith('20') || pin.startsWith('11') || pin.startsWith('40') || pin.startsWith('70') || pin.startsWith('56') || pin.startsWith('50')) {
    daysToAdd = 2;
  }

  const deliveryDate = new Date(today);
  deliveryDate.setDate(today.getDate() + daysToAdd);

  const options = { weekday: 'long', month: 'short', day: 'numeric' };
  return deliveryDate.toLocaleDateString('en-IN', options);
};

window.executePincodeCheck = function() {
  const pincodeInput = document.getElementById('HomePincodeInput');
  const resultBox = document.getElementById('HomePincodeResult');
  const resultPincodeNum = document.getElementById('ResultPincodeNum');
  const resultExpectedDate = document.getElementById('ResultExpectedDate');

  if (!pincodeInput || !resultBox) return;

  const pin = (pincodeInput.value || '').trim();

  if (!pin || pin.length < 6 || isNaN(pin)) {
    return;
  }

  const dateStr = window.calculateDeliveryDateStr(pin);

  if (resultPincodeNum) {
    resultPincodeNum.textContent = pin;
    resultPincodeNum.innerText = pin;
  }

  if (resultExpectedDate) {
    resultExpectedDate.textContent = dateStr;
    resultExpectedDate.innerText = dateStr;
  }

  resultBox.classList.remove('hidden');
  resultBox.style.display = 'block';
};"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        p_idx = content.find('/* 🚚 Global Bulletproof')
        if p_idx == -1:
            p_idx = content.find('function calculateDeliveryDateStr')

        if p_idx != -1:
            content = content[:p_idx] + global_pincode_js
        else:
            content += "\n\n" + global_pincode_js

        with open(jspath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED GLOBAL WINDOW PINCODE ENGINE IN: {jspath}")
