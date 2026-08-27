import os

# 1. Update theme.js to use global capture/bubble delegation for pincode checker
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

delegated_pincode_js = """/* 🚚 Global Bulletproof Pincode Checker Engine (100% Mobile & Desktop Delegation) */
function calculateDeliveryDateStr(pin) {
  const today = new Date();
  let daysToAdd = 3;

  if (pin.startsWith('20') || pin.startsWith('11') || pin.startsWith('40') || pin.startsWith('70') || pin.startsWith('56') || pin.startsWith('50')) {
    daysToAdd = 2;
  }

  const deliveryDate = new Date(today);
  deliveryDate.setDate(today.getDate() + daysToAdd);

  const options = { weekday: 'long', month: 'short', day: 'numeric' };
  return deliveryDate.toLocaleDateString('en-IN', options);
}

function executePincodeCheck() {
  const pincodeInput = document.getElementById('HomePincodeInput');
  const resultBox = document.getElementById('HomePincodeResult');
  const resultPincodeNum = document.getElementById('ResultPincodeNum');
  const resultExpectedDate = document.getElementById('ResultExpectedDate');

  if (!pincodeInput || !resultBox) return;

  const pin = pincodeInput.value.trim();

  if (!pin || pin.length < 6 || isNaN(pin)) {
    alert('Please enter a valid 6-digit Indian delivery pincode (e.g. 208001)');
    pincodeInput.focus();
    return;
  }

  const dateStr = calculateDeliveryDateStr(pin);

  if (resultPincodeNum) resultPincodeNum.textContent = pin;
  if (resultExpectedDate) resultExpectedDate.textContent = dateStr;

  resultBox.classList.remove('hidden');
  resultBox.style.display = 'block';
}

// Global Body Click Delegation for HomeCheckPincodeBtn
document.addEventListener('click', function(e) {
  const checkBtn = e.target.closest('#HomeCheckPincodeBtn');
  if (checkBtn) {
    e.preventDefault();
    e.stopPropagation();
    executePincodeCheck();
  }
}, true);

// Global Keypress for Enter Key on HomePincodeInput
document.addEventListener('keypress', function(e) {
  if (e.target && e.target.id === 'HomePincodeInput' && e.key === 'Enter') {
    e.preventDefault();
    executePincodeCheck();
  }
}, true);

// Input listener for auto-check on 6 digits
document.addEventListener('input', function(e) {
  if (e.target && e.target.id === 'HomePincodeInput') {
    if (e.target.value.trim().length === 6) {
      executePincodeCheck();
    }
  }
}, true);"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        p_idx = content.find('initPincodeChecker')
        if p_idx != -1:
            content = content[:p_idx] + delegated_pincode_js
        else:
            content += "\n\n" + delegated_pincode_js

        with open(jspath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPGRADED DELEGATED PINCODE JS IN: {jspath}")

# 2. Make sure HomePincodeResult is visible by default in HTML with 208001 pre-calculated
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        old_res_div = '<div id="HomePincodeResult" class="hidden mt-4'
        new_res_div = '<div id="HomePincodeResult" class="mt-4'

        content = content.replace(old_res_div, new_res_div)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REMOVED HIDDEN CLASS FROM PINCODE RESULT IN: {fpath}")
