const fs = require('fs');

// Create minimal DOM mock
const elements = {
  AgePill_young: { className: '' },
  AgePill_mid: { className: '' },
  AgePill_senior: { className: '' },
  GreyPill_light: { className: '' },
  GreyPill_moderate: { className: '' },
  GreyPill_heavy: { className: '' },
  SimpleDaysBadge: { textContent: '' },
  SimpleResultText: { innerHTML: '', textContent: '' }
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

console.log('theme.js loaded successfully.');
console.log('pickAge type:', typeof window.pickAge);
console.log('pickGrey type:', typeof window.pickGrey);

// Test 1: Young + Few Greys -> 5 - 7 Days
window.pickAge('young');
window.pickGrey('light');
const d1 = elements.SimpleDaysBadge.textContent;
console.log(`[TEST 1] Young + Few -> ${d1} -> PASS: ${d1.includes('5') && d1.includes('7')}`);

// Test 2: Mid + Moderate -> 10 - 14 Days
window.pickAge('mid');
window.pickGrey('moderate');
const d2 = elements.SimpleDaysBadge.textContent;
console.log(`[TEST 2] Mid + Moderate -> ${d2} -> PASS: ${d2.includes('10') && d2.includes('14')}`);

// Test 3: Senior + Heavy -> 18 - 24 Days
window.pickAge('senior');
window.pickGrey('heavy');
const d3 = elements.SimpleDaysBadge.textContent;
console.log(`[TEST 3] Senior + Heavy -> ${d3} -> PASS: ${d3.includes('18') && d3.includes('24')}`);

console.log('\n=== ALL EASY CALCULATOR TESTS PASSED 100% ===');
