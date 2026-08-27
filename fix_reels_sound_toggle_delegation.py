import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

delegated_sound_js = """/* 🔊 Bulletproof Delegated Sound On / Mute Toggle Engine */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  // Global Event Delegation for Sound Toggle Buttons
  document.body.addEventListener('click', (e) => {
    const soundBtn = e.target.closest('.js-sound-toggle');
    if (!soundBtn) return;

    e.preventDefault();
    e.stopPropagation();

    const card = soundBtn.closest('.js-reel-card');
    if (!card) return;

    const video = card.querySelector('video');
    if (!video) return;

    const allCards = document.querySelectorAll('.js-reel-card');

    if (video.muted) {
      // Mute all other videos first
      allCards.forEach(c => {
        const v = c.querySelector('video');
        const btn = c.querySelector('.js-sound-toggle');
        if (v) v.muted = true;
        if (btn) {
          btn.innerHTML = '<span>🔇</span> <span>Sound On</span>';
          btn.className = 'js-sound-toggle bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer';
        }
      });

      // Unmute active video
      video.muted = false;
      video.volume = 1.0;
      soundBtn.innerHTML = '<span>🔊</span> <span>Mute Sound</span>';
      soundBtn.className = 'js-sound-toggle bg-[#d4af37] text-black text-[10px] font-black px-2.5 py-1 rounded-full border border-[#d4af37] hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer';
      
      const p = video.play();
      if (p !== undefined) p.catch(() => {});
    } else {
      video.muted = true;
      soundBtn.innerHTML = '<span>🔇</span> <span>Sound On</span>';
      soundBtn.className = 'js-sound-toggle bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer';
    }
  });

  // Arrow controls
  if (leftArrow) {
    leftArrow.addEventListener('click', () => {
      container.scrollBy({ left: -310, behavior: 'smooth' });
    });
  }

  if (rightArrow) {
    rightArrow.addEventListener('click', () => {
      container.scrollBy({ left: 310, behavior: 'smooth' });
    });
  }
}"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        r_idx = content.find('function initReelsModal()')
        if r_idx != -1:
            e_idx = content.find('function ', r_idx + 30)
            if e_idx == -1:
                e_idx = content.find('/* ', r_idx + 30)
            if e_idx != -1:
                content = content[:r_idx] + delegated_sound_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED DELEGATED SOUND REELS JS IN: {jspath}")

# Update HTML files to fix top overlay container pointer-events
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        old_overlay = '<div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-none">'
        new_overlay = '<div class="absolute top-3 left-3 right-3 z-30 flex items-center justify-between pointer-events-auto">'
        content = content.replace(old_overlay, new_overlay)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED OVERLAY POINTER EVENTS IN: {fpath}")
