import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

clean_live_pulse_container = """            <div class="p-3 sm:p-4 rounded-2xl glass-panel-luxury border border-[#d4af37]/35 mb-4 flex items-center justify-between gap-2.5 shadow-xl">
              <div class="flex items-center gap-2.5 min-w-0">
                <span class="relative flex h-2.5 w-2.5 shrink-0">
                  <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                  <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
                </span>
                <div class="text-xs min-w-0">
                  <span class="text-white font-bold block truncate">
                    <strong class="js-live-visitors text-emerald-400 font-extrabold transition-all duration-300">872</strong> People Viewing Right Now
                  </span>
                  <span class="text-gray-400 text-[10px] sm:text-[11px] block truncate">⚡ High Demand &bull; Ready To Dispatch in 24h</span>
                </div>
              </div>
              <span class="shrink-0 whitespace-nowrap text-[9px] sm:text-[10px] font-black uppercase tracking-wider text-amber-300 bg-amber-400/15 border border-amber-400/30 px-2.5 py-1 rounded-full shadow-sm">
                LIVE PULSE
              </span>
            </div>"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Replace the live pulse box
    pattern = r'<div class="p-4 rounded-2xl glass-panel-luxury border border-\[#d4af37\]\/30 mb-4 flex items-center justify-between shadow-xl">.*?<\/div>\s*<\/div>\s*<span class="text-\[10px\] uppercase font-bold text-amber-300 bg-amber-500\/20 px-2\.5 py-1 rounded-full border border-amber-500\/30">\s*LIVE PULSE\s*<\/span>\s*<\/div>'
    
    # Fallback simpler regex
    new_content = re.sub(
        r'<div class="p-4 rounded-2xl glass-panel-luxury.*?LIVE PULSE\s*<\/span>\s*<\/div>',
        clean_live_pulse_container,
        new_content,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed LIVE PULSE badge wrapping in", fpath)

