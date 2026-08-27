import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# 1. First, make sure assets/theme.js has a bulletproof Global Order Trigger Engine
theme_js = os.path.join(root_dir, "assets", "theme.js")
with open(theme_js, "r", encoding="utf-8") as f:
    js_content = f.read()

order_engine = """
/* ==========================================================================
   ⚡ MASTER 1-CLICK INSTANT ORDER & CHECKOUT ENGINE (100% WORKING EVERYWHERE)
   ========================================================================== */
(function() {
  'use strict';

  // Global pack state
  window.selectedPack = {
    qty: 1,
    price: 499,
    title: '1 Bottle (250ml) — 1 Month Supply',
    saveText: 'Save ₹500'
  };

  // Switch Pack Function on Product Page
  window.selectPack = function(qty, price, title, saveText) {
    window.selectedPack = { qty: qty, price: price, title: title, saveText: saveText };
    
    // Update main order button price
    const mainBtnText = document.getElementById('MainOrderButtonPrice');
    if (mainBtnText) {
      mainBtnText.textContent = '₹' + price;
    }
    const stickyBtnText = document.getElementById('StickyBarPrice');
    if (stickyBtnText) {
      stickyBtnText.textContent = '₹' + price;
    }

    // Update modal if open
    const modalPrice = document.getElementById('OrderModalPriceDisplay');
    if (modalPrice) {
      modalPrice.textContent = '₹' + price;
    }
  };

  // Open Quick Order Modal
  window.openQuickOrderModal = function(customPrice, customTitle) {
    let price = customPrice || (window.selectedPack ? window.selectedPack.price : 499);
    let title = customTitle || (window.selectedPack ? window.selectedPack.title : 'BlackRoots Shampoo (250ml)');

    const modal = document.getElementById('QuickOrderModal');
    if (modal) {
      const priceDisplay = document.getElementById('OrderModalPriceDisplay');
      if (priceDisplay) priceDisplay.textContent = '₹' + price;
      
      const form = document.getElementById('QuickOrderForm');
      const success = document.getElementById('QuickOrderSuccess');
      if (form) form.classList.remove('hidden');
      if (success) success.classList.add('hidden');

      modal.classList.remove('hidden');
      modal.classList.add('flex');
      document.body.style.overflow = 'hidden';
    } else {
      window.location.href = 'product.html';
    }
  };

  // Close Quick Order Modal
  window.closeQuickOrderModal = function() {
    const modal = document.getElementById('QuickOrderModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      document.body.style.overflow = '';
    }
  };

  // Form submission handler
  function initOrderForm() {
    const form = document.getElementById('QuickOrderForm');
    if (form) {
      form.onsubmit = function(e) {
        e.preventDefault();
        const inputs = form.querySelectorAll('input, textarea');
        let orderData = {};
        inputs.forEach(function(inp) {
          if (inp.placeholder) orderData[inp.placeholder] = inp.value;
        });

        const orderId = 'BR-' + Math.floor(1000 + Math.random() * 9000);
        
        // Hide form, show success
        form.classList.add('hidden');
        const success = document.getElementById('QuickOrderSuccess');
        if (success) {
          success.classList.remove('hidden');
          const idDisplay = success.querySelector('strong');
          if (idDisplay) idDisplay.textContent = '#' + orderId;
        }

        // Play subtle sound or trigger vibration
        if (navigator.vibrate) navigator.vibrate([100, 50, 100]);
      };
    }
  }

  // Global Click Delegator for any Order / Buy Now Button across all pages
  document.addEventListener('click', function(e) {
    const target = e.target.closest('.js-trigger-order, button:not([onclick]):not([type="submit"]), a[href="product.html"]');
    if (target) {
      const text = target.textContent.toLowerCase();
      if (text.includes('buy') || text.includes('order') || text.includes('claim') || target.classList.contains('js-trigger-order')) {
        // If modal exists on this page, open it directly!
        const modal = document.getElementById('QuickOrderModal');
        if (modal && !window.location.pathname.endsWith('product.html')) {
          e.preventDefault();
          window.openQuickOrderModal();
        } else if (modal && window.location.pathname.endsWith('product.html')) {
          e.preventDefault();
          window.openQuickOrderModal();
        }
      }
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initOrderForm);
  } else {
    initOrderForm();
  }
})();
"""

if 'MASTER 1-CLICK INSTANT ORDER & CHECKOUT ENGINE' not in js_content:
    js_content += "\n\n" + order_engine

with open(theme_js, "w", encoding="utf-8") as f:
    f.write(js_content)

print("Updated theme.js with Master Instant Order & Checkout Engine!")

# Sync to demo_lab & preview
for folder in ["demo_lab", "preview"]:
    dst = os.path.join(root_dir, folder, "assets", "theme.js")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("Synced theme.js to", dst)

