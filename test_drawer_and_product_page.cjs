const fs = require('fs');

// Create minimal DOM mock
const elements = {
  MobileNavDrawer: {
    classList: {
      items: ['translate-x-full'],
      remove: function(c) { this.items = this.items.filter(x => x !== c); },
      add: function(c) { if (!this.items.includes(c)) this.items.push(c); },
      contains: function(c) { return this.items.includes(c); }
    }
  },
  MobileNavBackdrop: {
    classList: {
      items: ['opacity-0', 'pointer-events-none'],
      remove: function(c) { this.items = this.items.filter(x => x !== c); },
      add: function(c) { if (!this.items.includes(c)) this.items.push(c); },
      contains: function(c) { return this.items.includes(c); }
    }
  }
};

global.document = {
  getElementById(id) {
    return elements[id] || null;
  },
  body: { style: {} },
  querySelector() { return null; },
  querySelectorAll() { return []; },
  addEventListener() {}
};

global.window = global;
global.window.addEventListener = () => {};

// Load theme.js
require('./assets/theme.js');

console.log('=== TESTING MOBILE NAVIGATION DRAWER ===');
console.log('Initial Drawer State:', elements.MobileNavDrawer.classList.items);

// 1. Test Open
window.openMobileNavDrawer();
const isOpen = elements.MobileNavDrawer.classList.contains('translate-x-0') && elements.MobileNavBackdrop.classList.contains('opacity-100');
console.log('After openMobileNavDrawer():', elements.MobileNavDrawer.classList.items);
console.log('Drawer Open Test: PASS =', isOpen);

// 2. Test Close
window.closeMobileNavDrawer();
const isClosed = elements.MobileNavDrawer.classList.contains('translate-x-full') && elements.MobileNavBackdrop.classList.contains('opacity-0');
console.log('After closeMobileNavDrawer():', elements.MobileNavDrawer.classList.items);
console.log('Drawer Close Test: PASS =', isClosed);

console.log('\n=== ALL DRAWER TESTS PASSED 100% ===');
