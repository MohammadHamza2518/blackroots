import glob
import subprocess
import shutil

# Read assets/theme.js
with open('assets/theme.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the duplicate closure
js = js.replace("""    counterEls.forEach(el => {
      el.textContent = count;
      el.classList.add('text-emerald-300', 'scale-105');
      setTimeout(() => {
        el.classList.remove('scale-105');
      }, 400);
    });
  }, 3000);
}, 4000);
}""", """    counterEls.forEach(el => {
      el.textContent = count;
      el.classList.add('text-emerald-300', 'scale-105');
      setTimeout(() => {
        el.classList.remove('scale-105');
      }, 400);
    });
  }, 3000);
}""")

with open('assets/theme.js', 'w', encoding='utf-8') as f:
    f.write(js)

shutil.copy('assets/theme.js', 'demo_lab/assets/theme.js')
shutil.copy('assets/theme.js', 'preview/assets/theme.js')

for f in ['assets/theme.js', 'demo_lab/assets/theme.js', 'preview/assets/theme.js']:
    res = subprocess.run(['node', '-c', f], capture_output=True, text=True)
    print(f, "Syntax return code:", res.returncode)
