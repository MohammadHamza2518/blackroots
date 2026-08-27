import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

new_js_slider_code = """function initBeforeAfterSlider() {
  const slider = document.getElementById('BeforeAfterSlider');
  const overlay = document.getElementById('BeforeAfterOverlay');
  const handle = document.getElementById('BeforeAfterHandle');
  const innerImg = document.getElementById('AfterImageInner');

  if (!slider || !overlay || !handle) return;

  function updateInnerWidth() {
    if (innerImg && slider) {
      innerImg.style.width = slider.offsetWidth + 'px';
    }
  }

  updateInnerWidth();
  window.addEventListener('resize', updateInnerWidth);

  let isDragging = false;

  function move(x) {
    const rect = slider.getBoundingClientRect();
    let pos = ((x - rect.left) / rect.width) * 100;
    if (pos < 2) pos = 2;
    if (pos > 98) pos = 98;
    overlay.style.width = pos + '%';
    handle.style.left = pos + '%';
  }

  slider.addEventListener('mousedown', (e) => {
    isDragging = true;
    move(e.clientX);
  });

  window.addEventListener('mousemove', (e) => {
    if (isDragging) move(e.clientX);
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });

  slider.addEventListener('touchstart', (e) => {
    isDragging = true;
    if (e.touches && e.touches[0]) move(e.touches[0].clientX);
  }, { passive: true });

  window.addEventListener('touchmove', (e) => {
    if (isDragging && e.touches && e.touches[0]) {
      e.preventDefault();
      move(e.touches[0].clientX);
    }
  }, { passive: false });

  window.addEventListener('touchend', () => {
    isDragging = false;
  });

  // Default initial split position: 50%
  overlay.style.width = '50%';
  handle.style.left = '50%';
}"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        s_idx = content.find('function initBeforeAfterSlider()')
        if s_idx != -1:
            e_idx = content.find('function ', s_idx + 30)
            if e_idx == -1:
                e_idx = content.find('/* ', s_idx + 30)
            if e_idx != -1:
                content = content[:s_idx] + new_js_slider_code + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED JS BEFORE/AFTER SLIDER IN: {jspath}")

# HTML files update
html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html') and f != 'mobile-preview.html':
            html_files.append(os.path.join(root, f))

new_html_slider = """      <!-- Drag Container (Touch-Optimized Before/After Comparison Slider) -->
      <div id="BeforeAfterSlider" class="relative w-full max-w-4xl h-[360px] sm:h-[520px] mx-auto rounded-3xl overflow-hidden shadow-[0_20px_60px_rgba(0,0,0,0.8)] border-2 border-[#d4af37]/50 select-none cursor-ew-resize touch-none group bg-[#090a0f]">
        
        <!-- Base Underneath Image: BEFORE (Lady with Grey Hair) -->
        <img src="./assets/blackroots-before-lady.jpg" alt="Before - Grey Hair" class="absolute inset-0 w-full h-full object-cover object-top pointer-events-none">
        
        <!-- Badge: BEFORE (Bottom-Left Corner) -->
        <div class="absolute bottom-4 left-4 z-20 bg-black/80 border border-red-500/50 text-red-300 px-3.5 py-1.5 rounded-full font-bold text-[10px] sm:text-xs uppercase tracking-widest backdrop-blur-md pointer-events-none shadow-xl flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          <span>BEFORE</span>
        </div>

        <!-- Overlay Container: AFTER (Happy Lady with Jet Black Hair - 50% initial width) -->
        <div id="BeforeAfterOverlay" class="absolute inset-y-0 left-0 w-1/2 overflow-hidden shadow-2xl">
          <!-- Inner Image: AFTER -->
          <img id="AfterImageInner" src="./assets/blackroots-after-lady.jpg" alt="After - Natural Black Hair" class="absolute top-0 left-0 h-full object-cover object-top pointer-events-none">
          
          <!-- Badge: AFTER (Bottom-Left Corner inside Overlay) -->
          <div class="absolute bottom-4 left-4 z-20 bg-[#d4af37] text-black px-3.5 py-1.5 rounded-full font-black text-[10px] sm:text-xs uppercase tracking-widest shadow-xl pointer-events-none whitespace-nowrap flex items-center gap-1.5">
            <span>✨ AFTER (10 DAYS)</span>
          </div>
        </div>

        <!-- Glowing Divider Line & Handle Knob -->
        <div id="BeforeAfterHandle" class="absolute top-0 bottom-0 left-1/2 -translate-x-1/2 z-30 flex items-center justify-center pointer-events-none">
          <!-- Vertical Glowing Gold Line -->
          <div class="w-0.5 h-full bg-gradient-to-b from-amber-300 via-[#d4af37] to-amber-500 shadow-[0_0_12px_rgba(212,175,55,0.9)]"></div>
          
          <!-- Glowing Double Arrow Circle Handle Knob -->
          <div class="absolute top-1/2 -translate-y-1/2 w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-gradient-to-br from-amber-300 via-[#d4af37] to-[#aa7c11] text-black font-black text-xs sm:text-sm flex items-center justify-center shadow-[0_0_25px_rgba(212,175,55,0.9)] border-2 border-white group-hover:scale-110 transition-transform cursor-ew-resize">
            <span>◀ ▶</span>
          </div>
        </div>

      </div>"""

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'BeforeAfterSlider' in content:
            start_s = content.find('<!-- Drag Container')
            if start_s == -1:
                start_s = content.find('<div id="BeforeAfterSlider"')

            end_s = content.find('<!-- Trust Features', start_s)
            if end_s == -1:
                end_s = content.find('</div>\n\n      <!-- Trust', start_s)
            if end_s == -1:
                end_s = content.find('</div>', content.find('BeforeAfterHandle', start_s))
                if end_s != -1:
                    end_s += 6

            if start_s != -1 and end_s != -1:
                content = content[:start_s] + new_html_slider + "\n\n      " + content[end_s:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED HTML BEFORE/AFTER SLIDER IN: {fpath}")
    except Exception as e:
        print(f"Error upgrading HTML slider in {fpath}: {e}")
