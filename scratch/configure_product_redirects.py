import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# 1. Update assets/theme.js
theme_js = os.path.join(root_dir, "assets", "theme.js")
with open(theme_js, "r", encoding="utf-8") as f:
    js_content = f.read()

# Replace openQuickOrderModal logic
updated_theme_js = re.sub(
    r'window\.openQuickOrderModal\s*=\s*function\s*\([^)]*\)\s*\{[\s\S]*?\n\s*\};',
    '''window.openQuickOrderModal = function(customPrice, customTitle) {
    const isProductPage = window.location.pathname.endsWith('product.html') || window.location.pathname.endsWith('product');
    
    // If not on product.html, direct straight to product page!
    if (!isProductPage) {
      window.location.href = 'product.html';
      return;
    }

    // If on product page, open 1-Click Instant Checkout Modal
    let price = customPrice || (window.selectedPack ? window.selectedPack.price : 499);
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
    }
  };''',
    js_content
)

# Also update global click delegator
updated_theme_js = re.sub(
    r'document\.addEventListener\(\'click\',\s*function\(e\)\s*\{[\s\S]*?if\s*\(modal[\s\S]*?\}\s*\}\s*\);\s*\}\s*\);',
    '''document.addEventListener('click', function(e) {
    const target = e.target.closest('.js-trigger-order, button, a');
    if (target) {
      const text = (target.textContent || '').toLowerCase().trim();
      const isOrderBtn = target.classList.contains('js-trigger-order') || text.includes('order now') || text.includes('buy now') || text.includes('claim offer') || text.includes('buy ₹');
      
      if (isOrderBtn && target.getAttribute('type') !== 'submit') {
        const isProductPage = window.location.pathname.endsWith('product.html') || window.location.pathname.endsWith('product');
        if (!isProductPage) {
          e.preventDefault();
          window.location.href = 'product.html';
        }
      }
    }
  });''',
    updated_theme_js
)

with open(theme_js, "w", encoding="utf-8") as f:
    f.write(updated_theme_js)

print("Updated theme.js: All external order buttons redirect to product.html!")

# Sync to demo_lab & preview
for folder in ["demo_lab", "preview"]:
    dst = os.path.join(root_dir, folder, "assets", "theme.js")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(updated_theme_js)
    print("Synced theme.js to", dst)

# 2. Update all HTML files except product.html:
# Change any onclick="openQuickOrderModal();" to onclick="window.location.href='product.html';" and ensure href="product.html"
pages_to_redirect = [
    "index.html",
    "ingredients.html",
    "how-to-use.html",
    "reviews.html",
    "ai-consultant.html",
    "track-order.html",
    "contact.html",
    "demo_lab/index.html",
    "demo_lab/ingredients.html",
    "demo_lab/how-to-use.html",
    "demo_lab/reviews.html",
    "demo_lab/ai-consultant.html",
    "demo_lab/track-order.html",
    "demo_lab/contact.html",
    "preview/index.html",
    "preview/ingredients.html",
    "preview/how-to-use.html",
    "preview/reviews.html",
    "preview/ai-consultant.html",
    "preview/track-order.html",
    "preview/contact.html"
]

for p in pages_to_redirect:
    fp = os.path.join(root_dir, p)
    if not os.path.exists(fp):
        continue

    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    # In non-product pages, replace onclick="openQuickOrderModal();" with href="product.html" / onclick="window.location.href='product.html';"
    new_content = content.replace('onclick="openQuickOrderModal();"', 'onclick="window.location.href=\'product.html\';"')
    new_content = new_content.replace('onclick="openQuickOrderModal()"', 'onclick="window.location.href=\'product.html\';"')

    if new_content != content:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated all order buttons to direct to product.html in:", p)

