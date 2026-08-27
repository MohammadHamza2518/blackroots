import os
import glob
import re
import subprocess

all_html = glob.glob('*.html') + glob.glob('demo_lab/*.html') + glob.glob('preview/*.html')

for fpath in all_html:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace 14 Bottles with 31 Bottles
    content = content.replace('14 Bottles Left In Stock', '31 Bottles Left In Stock')
    content = content.replace('14 Bottles Left', '31 Bottles Left')
    content = content.replace('14 bottles left', '31 bottles left')
    content = content.replace('14 Bottles', '31 Bottles')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"UPDATED 31 BOTTLES IN: {fpath}")

# Update theme.js files
js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

for jpath in js_files:
    with open(jpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update initLiveShopperCounter function
    old_counter_fn = r'function initLiveShopperCounter\(\) \{.*?\}'
    new_counter_fn = """function initLiveShopperCounter() {
  const counterEls = document.querySelectorAll('.js-live-counter, .js-live-visitors');
  if (!counterEls.length) return;

  let count = 872;
  setInterval(() => {
    // Realistic visitor fluctuation (+1, -1, +2, -2)
    const delta = (Math.random() > 0.48 ? 1 : -1) * (Math.floor(Math.random() * 3) + 1);
    count += delta;
    count = Math.max(846, Math.min(896, count));
    
    counterEls.forEach(el => {
      el.textContent = count;
      el.classList.add('text-emerald-300', 'scale-105');
      setTimeout(() => {
        el.classList.remove('scale-105');
      }, 400);
    });
  }, 3000);
}"""

    content = re.sub(old_counter_fn, new_counter_fn, content, flags=re.DOTALL)

    with open(jpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"UPDATED LIVE VISITOR ENGINE IN: {jpath}")

for jpath in js_files:
    res = subprocess.run(['node', '-c', jpath], capture_output=True, text=True)
    print(jpath, "Syntax check return code:", res.returncode)
