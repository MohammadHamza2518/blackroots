import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

theme_js_path = os.path.join(root_dir, "assets", "theme.js")

with open(theme_js_path, 'r', encoding='utf-8') as f:
    js_code = f.read()

# Dynamic Natural Live Pulse Engine
natural_counter_code = """
/* 👥 Ultra-Realistic Live Shopper Counter & Traffic Pulse Engine */
function initLiveShopperCounter() {
  const counterEls = document.querySelectorAll('.js-live-counter, .js-live-visitors');
  if (!counterEls.length) return;

  let count = Math.floor(Math.random() * (885 - 865 + 1)) + 865;
  counterEls.forEach(el => { el.textContent = count; });

  function tick() {
    // Natural human traffic variation
    const change = (Math.random() > 0.45 ? 1 : -1) * (Math.floor(Math.random() * 3) + 1);
    count = Math.max(835, Math.min(925, count + change));

    counterEls.forEach(el => {
      el.style.opacity = '0.5';
      el.style.transform = 'scale(1.1)';
      setTimeout(() => {
        el.textContent = count;
        el.style.opacity = '1';
        el.style.transform = 'scale(1)';
      }, 150);
    });

    // Random natural interval between 2.5s and 5s
    const nextInterval = Math.floor(Math.random() * 2500) + 2500;
    setTimeout(tick, nextInterval);
  }

  setTimeout(tick, 3000);
}

// Master DOM Ready Initializer
document.addEventListener('DOMContentLoaded', function() {
  try { initLiveShopperCounter(); } catch(e) {}
  try { initShowerTimer(); } catch(e) {}
  try { initStickyHeader(); } catch(e) {}
  try { initCartDrawer(); } catch(e) {}
  try { initBeforeAfterSlider(); } catch(e) {}
  try { initIngredientFilters(); } catch(e) {}
  try { initAIConsultantChat(); } catch(e) {}
});
"""

# Replace existing initLiveShopperCounter if exists or append
if 'function initLiveShopperCounter()' in js_code:
    js_code = re.sub(r'function initLiveShopperCounter\(\)\s*\{[^}]*setInterval[^}]*\}\s*\}', '', js_code, flags=re.DOTALL)

js_code = js_code.strip() + "\n\n" + natural_counter_code.strip() + "\n"

with open(theme_js_path, 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Updated theme.js with Master DOM Initializer & Dynamic Traffic Pulse!")

# Also sync to demo_lab & preview
for folder in ["demo_lab", "preview"]:
    dst = os.path.join(root_dir, folder, "assets", "theme.js")
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(js_code)
    print("Synced to", dst)

# Add inline fallback to product.html
inline_product_script = """
  <script>
    // Live Pulse Natural Traffic Fluctuation Simulator
    document.addEventListener('DOMContentLoaded', function() {
      const liveEls = document.querySelectorAll('.js-live-visitors');
      if (!liveEls.length) return;

      let currentViewers = 872;
      function updateLiveViewers() {
        const delta = (Math.random() > 0.44 ? 1 : -1) * (Math.floor(Math.random() * 3) + 1);
        currentViewers = Math.max(842, Math.min(918, currentViewers + delta));
        
        liveEls.forEach(el => {
          el.style.transition = 'all 0.2s ease';
          el.style.opacity = '0.4';
          el.style.transform = 'scale(1.12)';
          setTimeout(() => {
            el.textContent = currentViewers;
            el.style.opacity = '1';
            el.style.transform = 'scale(1)';
          }, 150);
        });

        const nextTick = Math.floor(Math.random() * 2500) + 2500;
        setTimeout(updateLiveViewers, nextTick);
      }

      setTimeout(updateLiveViewers, 2500);
    });
  </script>
"""

product_files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

for pf in product_files:
    if not os.path.exists(pf):
        continue
    with open(pf, 'r', encoding='utf-8') as f:
        pcontent = f.read()

    # Clean old inline live script if any
    pcontent = re.sub(r'<script>\s*\/\/\s*Live Pulse Natural.*?<\/script>', '', pcontent, flags=re.DOTALL)
    pcontent = pcontent.replace('</body>', inline_product_script + '\n</body>')

    with open(pf, 'w', encoding='utf-8') as f:
        f.write(pcontent)
    print("Injected Live Pulse script into", pf)

