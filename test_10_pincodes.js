const fs = require('fs');

// Create minimal DOM mock
const elements = {
  HomePincodeInput: { value: '' },
  HomePincodeResult: { className: 'hidden', style: {}, classList: { remove(c) { this[c] = false; }, add(c) { this[c] = true; } } },
  ResultPincodeNum: { textContent: '' },
  ResultExpectedDate: { textContent: '' }
};

global.document = {
  getElementById(id) {
    return elements[id] || null;
  },
  querySelector() { return null; },
  querySelectorAll() { return []; },
  addEventListener() {}
};

global.window = global;
global.window.addEventListener = () => {};

// Load theme.js
require('./assets/theme.js');

console.log('theme.js loaded successfully. executePincodeCheck type:', typeof window.executePincodeCheck);

const testPincodes = [
  '208001', // Kanpur Central
  '110001', // New Delhi Connaught Place
  '400001', // Mumbai Fort
  '560001', // Bengaluru GPO
  '700001', // Kolkata GPO
  '500001', // Hyderabad GPO
  '208902', // Kanpur Dehat / Chakeri
  '302001', // Jaipur GPO
  '600001', // Chennai GPO
  '380001'  // Ahmedabad GPO
];

let allPassed = true;

testPincodes.forEach((pin, i) => {
  elements.HomePincodeInput.value = pin;
  window.executePincodeCheck(true);

  const shownPin = elements.ResultPincodeNum.textContent;
  const shownDate = elements.ResultExpectedDate.textContent;
  const isVisible = elements.HomePincodeResult.style.display === 'block';

  const passed = (shownPin === pin) && shownDate.length > 5 && isVisible;
  console.log(`[TEST ${(i+1).toString().padStart(2, '0')}/10] Input: ${pin} -> Shown: ${shownPin} | Delivery: ${shownDate} | Visible: ${isVisible} | PASS: ${passed}`);
  if (!passed) allPassed = false;
});

console.log('\n=== FINAL VERIFICATION RESULT ===');
console.log('ALL 10 RANDOM PINCODES PASSED 100%:', allPassed);
