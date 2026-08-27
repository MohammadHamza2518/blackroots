import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

theme_js_path = os.path.join(root_dir, "assets", "theme.js")

with open(theme_js_path, 'r', encoding='utf-8') as f:
    js = f.read()

helpers_code = """
/* 📦 Quick Order Modal Global Controls */
function openQuickOrderModal() {
  const modal = document.getElementById('QuickOrderModal');
  if (modal) {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  } else {
    window.location.href = 'product.html';
  }
}

function closeQuickOrderModal() {
  const modal = document.getElementById('QuickOrderModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }
}

window.openQuickOrderModal = openQuickOrderModal;
window.closeQuickOrderModal = closeQuickOrderModal;

/* 🌿 Ingredient Detail Modal Global Controls */
function openIngredientDetail(title, desc, benefit) {
  const modal = document.getElementById('IngredientModal');
  const titleEl = document.getElementById('IngredientModalTitle');
  const descEl = document.getElementById('IngredientModalDesc');
  const benefitEl = document.getElementById('IngredientModalBenefit');

  if (titleEl) titleEl.textContent = title;
  if (descEl) descEl.textContent = desc;
  if (benefitEl) benefitEl.textContent = benefit;

  if (modal) {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }
}

function closeIngredientModal() {
  const modal = document.getElementById('IngredientModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }
}

window.openIngredientDetail = openIngredientDetail;
window.closeIngredientModal = closeIngredientModal;

/* 📱 Mobile Simulator Page Switcher Helper */
function switchToSimPage(page) {
  const iframe = document.getElementById('SimulatedIframe');
  const selector = document.getElementById('PageSelector');
  if (iframe) {
    iframe.src = page + '?v=' + Date.now();
  }
  if (selector) {
    selector.value = page;
  }
  const tabHome = document.getElementById('TabHome');
  const tabProd = document.getElementById('TabProduct');
  if (tabHome && tabProd) {
    if (page === 'index.html') {
      tabHome.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-[#d4af37] text-black shadow';
      tabProd.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
    } else if (page === 'product.html') {
      tabProd.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-[#d4af37] text-black shadow';
      tabHome.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
    }
  }
}

window.switchToSimPage = switchToSimPage;
"""

# Append helpers to theme.js if not present
if 'function openQuickOrderModal()' not in js:
    js = js.strip() + "\n\n" + helpers_code.strip() + "\n"

with open(theme_js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated theme.js with all modal and simulator helper functions!")

# Sync theme.js to demo_lab & preview
for folder in ["demo_lab", "preview"]:
    dst = os.path.join(root_dir, folder, "assets", "theme.js")
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(js)
    print("Synced theme.js to", dst)

# Clean corrupted characters in all HTML files
html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
for hf in html_files:
    fp = os.path.join(root_dir, hf)
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('œ•', '✕').replace('œ“', '✓')
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(c)

print("Cleaned corrupted characters across HTML files!")
