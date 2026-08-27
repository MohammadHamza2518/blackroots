import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\how-to-use.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\how-to-use.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\how-to-use.html"
]

timer_ui_replacement = """      <div class="max-w-xl mx-auto mb-16 p-8 rounded-3xl glass-panel-luxury border-2 border-[#d4af37] shadow-2xl space-y-5 text-center">
        <div class="flex items-center justify-center gap-2 text-amber-300 text-xs font-bold uppercase tracking-widest">
          <span>⏱️ Interactive Shower Scalp Massage Timer</span>
        </div>

        <div class="relative flex items-center justify-center">
          <div id="ShowerTimerDisplay" class="font-mono text-6xl sm:text-7xl font-extrabold text-amber-400 tracking-wider py-1 select-none">
            03:00
          </div>
        </div>

        <!-- Progress Bar -->
        <div class="w-full bg-white/10 h-2.5 rounded-full overflow-hidden border border-white/10">
          <div id="ShowerTimerProgress" class="bg-gradient-to-r from-amber-400 to-[#d4af37] h-full w-full transition-all duration-1000 ease-linear rounded-full"></div>
        </div>

        <p id="ShowerTimerStatus" class="text-xs text-gray-300 font-medium">
          Practice your 2-3 minute scalp massage routine during your shower!
        </p>

        <div class="flex flex-wrap items-center justify-center gap-3 pt-2">
          <button type="button" id="BtnStartShowerTimer" class="btn-gold-luxury btn-shimmer text-xs py-3.5 px-8 uppercase font-extrabold shadow-lg cursor-pointer transition-transform active:scale-95">
            ▶️ Start 3-Min Scalp Massage Timer
          </button>
          <button type="button" id="BtnResetShowerTimer" class="px-6 py-3.5 rounded-full bg-white/10 hover:bg-white/20 border border-white/20 text-gray-200 text-xs font-bold uppercase tracking-wider cursor-pointer transition-all active:scale-95">
            ↺ Reset
          </button>
        </div>
      </div>"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Fix broken symbols
    new_content = new_content.replace('œ•', '✕')
    new_content = new_content.replace('œ“', '✓')
    
    # Replace the shower timer section
    import re
    pattern = r'<div class="max-w-xl mx-auto mb-16.*?<\/div>\s*<\/div>'
    new_content = re.sub(pattern, timer_ui_replacement, new_content, flags=re.DOTALL)

    # Ensure script tag is present before </body>
    if 'src="./assets/theme.js"' not in new_content and 'src="assets/theme.js"' not in new_content:
        new_content = new_content.replace('</body>', '  <script src="./assets/theme.js"></script>\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {fpath}")

