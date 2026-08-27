import os

# 1. Update mobile-preview.html to add allow="autoplay; encrypted-media; fullscreen" to iframe
preview_file = r"c:\Users\moham\Downloads\blackroots website\mobile-preview.html"

if os.path.exists(preview_file):
    with open(preview_file, 'r', encoding='utf-8') as f:
        content = f.read()

    old_iframe = '<iframe id="SimulatedIframe" src="index.html" title="Live Mobile Website Preview"></iframe>'
    new_iframe = '<iframe id="SimulatedIframe" src="index.html" title="Live Mobile Website Preview" allow="autoplay; encrypted-media; fullscreen"></iframe>'

    content = content.replace(old_iframe, new_iframe)

    with open(preview_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("ADDED ALLOW AUTOPLAY TO IFRAME IN mobile-preview.html")

# 2. Update theme.js to use Capture Phase Event Delegation for Sound Toggle Button
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

capture_sound_js = """/* 🔊 Bulletproof Capture-Phase Sound On / Mute Toggle Engine */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

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
}

// Global Capture Phase Listener for Sound Toggle Buttons (Fires BEFORE any DOM layer)
document.addEventListener('click', function(e) {
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
    if (p !== undefined) {
      p.catch(() => {
        video.muted = false;
      });
    }
  } else {
    video.muted = true;
    soundBtn.innerHTML = '<span>🔇</span> <span>Sound On</span>';
    soundBtn.className = 'js-sound-toggle bg-black/80 backdrop-blur-md text-amber-300 text-[10px] font-extrabold px-2.5 py-1 rounded-full border border-amber-500/30 hover:scale-105 transition-transform flex items-center gap-1 shadow-xl cursor-pointer';
  }
}, true);"""

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
                content = content[:r_idx] + capture_sound_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED CAPTURE-PHASE SOUND REELS JS IN: {jspath}")
