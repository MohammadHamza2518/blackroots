import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

pdp_ingredients_script = """
  <!-- 🌿 Interactive Botanical Ingredient Spotlight Tab Engine -->
  <script>
    (function() {
      const ingData = {
        'indigo': {
          icon: '🌿',
          target: 'Hair Cortex Pigment Layer',
          title: 'Japanese Indigo Leaf Extract',
          desc: "Centuries-old Japanese botanical secret used by ancient hair artisans. Indigo leaf naturally binds dark plant melanin to grey hair strands during shower lather without stripping hair's natural oils.",
          tag1: '✓ 100% Non-Toxic',
          tag2: '✓ Zero Ammonia Damage'
        },
        'amla': {
          icon: '🍏',
          target: 'Follicle Vitamin C & Melanin Synthesis',
          title: 'Organic Indian Gooseberry (Amla)',
          desc: "World's richest natural source of active Vitamin C and antioxidants. Boosts natural melanin production inside dormant hair follicles while strengthening root grip against shower hair fall.",
          tag1: '✓ Anti-Hair Fall',
          tag2: '✓ Melanin Booster'
        },
        'bhringraj': {
          icon: '🌱',
          target: 'Scalp Root Nourishment & Density',
          title: 'King of Herbs & Brahmi Complex',
          desc: "Celebrated in ancient Ayurveda as 'Keshraj' (Ruler of Hair). Revitalizes micro-circulation to the scalp roots, delays premature greying, and conditions rough cuticles into silky black texture.",
          tag1: '✓ 100% Ayurvedic',
          tag2: '✓ Density Revitalizer'
        },
        'camellia': {
          icon: '💧',
          target: 'Cuticle Shine & Moisture Seal',
          title: 'Tsubaki Camellia Seed Oil',
          desc: "Cold-pressed Japanese Camellia seed oil delivers deep oleic acid hydration. Seals the hair cuticle with a reflective natural black mirror shine that lasts through humidity and hard water.",
          tag1: '✓ Mirror Black Shine',
          tag2: '✓ Hard-Water Protection'
        }
      };

      const tabMap = {
        'indigo': 'TabBtnIndigo',
        'amla': 'TabBtnAmla',
        'bhringraj': 'TabBtnBhringraj',
        'camellia': 'TabBtnCamellia'
      };

      window.showIngredientTab = function(key) {
        const data = ingData[key];
        if (!data) return;

        // 1. Update button styling
        Object.keys(tabMap).forEach(function(k) {
          const btn = document.getElementById(tabMap[k]);
          if (!btn) return;
          if (k === key) {
            btn.className = 'ing-tab-btn py-2.5 px-4 rounded-full border-2 border-[#d4af37] bg-[#d4af37] text-black font-bold text-xs shadow-lg transition-all transform scale-[1.02] cursor-pointer';
          } else {
            btn.className = 'ing-tab-btn py-2.5 px-4 rounded-full border border-white/10 bg-white/5 text-gray-300 font-bold text-xs hover:border-[#d4af37] hover:text-white transition-all cursor-pointer';
          }
        });

        // 2. Update Card Display with smooth micro-fade
        const iconEl = document.getElementById('IngIconDisplay');
        const targetEl = document.getElementById('IngTargetDisplay');
        const titleEl = document.getElementById('IngTitleDisplay');
        const descEl = document.getElementById('IngDescDisplay');

        const card = document.getElementById('IngredientCardDisplay');
        if (card) {
          card.style.opacity = '0.7';
          setTimeout(function() {
            if (iconEl) iconEl.textContent = data.icon;
            if (targetEl) targetEl.textContent = data.target;
            if (titleEl) titleEl.textContent = data.title;
            if (descEl) descEl.textContent = data.desc;
            card.style.opacity = '1';
          }, 80);
        }
      };

      document.addEventListener('DOMContentLoaded', function() {
        window.showIngredientTab('indigo');
      });
    })();
  </script>
"""

files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old ingredient script if present
    content = re.sub(r'<!-- 🌿 Interactive Botanical Ingredient Spotlight Tab Engine -->.*?<\/script>', '', content, flags=re.DOTALL)

    new_content = content.replace('</body>', pdp_ingredients_script + '\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Injected Ingredient Spotlight Tab Engine into", fpath)

