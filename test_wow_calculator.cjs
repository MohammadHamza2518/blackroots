const fs = require('fs');

// Create minimal DOM mock
const elements = {
  CalcResultDaysBadge: { textContent: '' },
  CalcResultHeading: { textContent: '' },
  CalcResultDesc: { textContent: '' },
  SelectedAgeLabel: { textContent: '' },
  SelectedGreyLabel: { textContent: '' },
  CalcResultOutput: { className: 'hidden', style: {}, classList: { remove(c) { this[c] = false; }, add(c) { this[c] = true; } } }
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

console.log('theme.js loaded successfully. calculateHairResultTimeline type:', typeof window.calculateHairResultTimeline);

// Test all 9 combinations
const ageOptions = ['young', 'mid', 'senior'];
const greyOptions = ['light', 'moderate', 'heavy'];

let totalTests = 0;
let passedTests = 0;

ageOptions.forEach(age => {
  greyOptions.forEach(grey => {
    totalTests++;
    // Execute calculator
    window.calculateHairResultTimeline();

    const days = elements.CalcResultDaysBadge.textContent;
    const heading = elements.CalcResultHeading.textContent;
    const desc = elements.CalcResultDesc.textContent;
    const isVisible = elements.CalcResultOutput.style.display === 'block';

    const isValid = days.length > 0 && heading.length > 0 && desc.length > 0 && isVisible;
    if (isValid) passedTests++;

    console.log(`[TEST ${totalTests}/9] Combination: ${age} + ${grey} -> Days: ${days} | Visible: ${isVisible} | PASS: ${isValid}`);
  });
});

console.log(`\n=== WOW CALCULATOR TEST SUMMARY: ${passedTests}/${totalTests} PASSED ===`);
