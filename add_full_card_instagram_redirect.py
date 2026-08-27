import os

# 1. Update theme.js to handle full video card click redirect to Instagram
theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

full_card_redirect_js = """/* 📸 Full Video Card Direct Instagram Redirect Engine */
function initReelsModal() {
  const container = document.getElementById('ReelsCarouselContainer');
  if (!container) return;

  const cards = container.querySelectorAll('.js-reel-card');
  const leftArrow = document.getElementById('ReelsSlideLeft');
  const rightArrow = document.getElementById('ReelsSlideRight');

  // Full Card Click -> Open Instagram Reel (Except Buy Now button)
  cards.forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', (e) => {
      // If user clicked Buy Now button, let it navigate to product.html
      if (e.target.closest('.js-trigger-order')) {
        return;
      }

      // Find Instagram link inside the card
      const igLinkEl = card.querySelector('a[href*="instagram.com"]');
      if (igLinkEl && igLinkEl.href) {
        window.open(igLinkEl.href, '_blank', 'noopener,noreferrer');
      }
    });
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
                content = content[:r_idx] + full_card_redirect_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED FULL CARD INSTAGRAM REDIRECT JS IN: {jspath}")
