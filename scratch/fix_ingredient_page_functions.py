import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

theme_js_path = os.path.join(root_dir, "assets", "theme.js")

with open(theme_js_path, "r", encoding="utf-8") as f:
    js = f.read()

ingredient_engine = """
/* ==========================================================================
   🌿 INGREDIENTS PAGE INTERACTIVE FILTER & DETAIL MODAL ENGINE
   ========================================================================== */
function initIngredientFilters() {
  const filterBtns = document.querySelectorAll('.js-ingredient-filter');
  const cards = document.querySelectorAll('.js-ingredient-card');

  if (filterBtns.length === 0 || cards.length === 0) return;

  filterBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      const category = btn.getAttribute('data-category');

      // Update button active styles
      filterBtns.forEach(function(b) {
        if (b === btn) {
          b.className = 'js-ingredient-filter px-5 py-2.5 rounded-full bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-xs font-black uppercase tracking-wider shadow-xl transform scale-105 transition-all cursor-pointer';
        } else {
          b.className = 'js-ingredient-filter px-5 py-2.5 rounded-full bg-white/5 text-gray-300 hover:text-white text-xs font-bold uppercase tracking-wider border border-white/10 transition-all cursor-pointer';
        }
      });

      // Filter cards with smooth fade
      cards.forEach(function(card) {
        const cardCat = card.getAttribute('data-category');
        if (category === 'all' || cardCat === category) {
          card.style.display = 'block';
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(function() {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 30);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

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
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function closeIngredientModal() {
  const modal = document.getElementById('IngredientModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

window.initIngredientFilters = initIngredientFilters;
window.openIngredientDetail = openIngredientDetail;
window.closeIngredientModal = closeIngredientModal;
"""

# Replace or insert ingredient engine in theme.js
# First remove old openIngredientDetail if present
js = re.sub(r'/\* 🌿 Ingredient Detail Modal Global Controls \*/[\s\S]*?window\.closeIngredientModal\s*=\s*closeIngredientModal;', '', js)

if 'initIngredientFilters' not in js:
    js += "\n\n" + ingredient_engine
else:
    # Update it cleanly
    js = js + "\n\n" + ingredient_engine

with open(theme_js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Updated theme.js with complete Ingredient Filter & Modal Engine!")

# Sync to demo_lab & preview
for folder in ["demo_lab", "preview"]:
    dst = os.path.join(root_dir, folder, "assets", "theme.js")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(js)
    print("Synced theme.js to", dst)

# Also in ingredients.html, let's make sure the modal has proper backdrop close click
ing_files = [
    os.path.join(root_dir, "ingredients.html"),
    os.path.join(root_dir, "demo_lab", "ingredients.html"),
    os.path.join(root_dir, "preview", "ingredients.html")
]

modal_script = """
  <!-- 🌿 Inline Active Initialization for Ingredients Page -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      if (typeof window.initIngredientFilters === 'function') {
        window.initIngredientFilters();
      }
      
      const modal = document.getElementById('IngredientModal');
      if (modal) {
        modal.addEventListener('click', function(e) {
          if (e.target === modal) window.closeIngredientModal();
        });
      }
    });
  </script>
"""

for ifp in ing_files:
    if not os.path.exists(ifp):
        continue
    with open(ifp, "r", encoding="utf-8") as f:
        icontent = f.read()

    # Clean any duplicate script if present
    icontent = re.sub(r'<!-- 🌿 Inline Active Initialization for Ingredients Page -->[\s\S]*?<\/script>', '', icontent)
    new_icontent = icontent.replace('</body>', modal_script + '\n</body>')

    with open(ifp, "w", encoding="utf-8") as f:
        f.write(new_icontent)
    print("Injected Inline Active Initialization into", ifp)

