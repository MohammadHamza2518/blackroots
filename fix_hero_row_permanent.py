import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

target_old = """    function applySort(order) {
      const cards = getVisibleCards();
      const sorted = cards.sort((a, b) => {
        const heroIds = ['sunita-verma', 'alok-mishra', 'anita-patel'];
        const aPinned = heroIds.includes(a.id);
        const bPinned = heroIds.includes(b.id);
        if (aPinned && bPinned) {
          return heroIds.indexOf(a.id) - heroIds.indexOf(b.id);
        }

        if (aPinned && !bPinned) return -1;
        if (!aPinned && bPinned) return 1;
        if (aPinned && bPinned) {
          return a.id === 'sunita-verma' ? -1 : 1;
        }

        if (order === 'helpful') {
           const aLikesMatch = a.innerHTML.match(/(?:&#128077;|👍)\s*<span[^>]*>(\d+)<\/span>/) || a.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
           const bLikesMatch = b.innerHTML.match(/(?:&#128077;|👍)\s*<span[^>]*>(\d+)<\/span>/) || b.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
           const aLikes = aLikesMatch ? parseInt(aLikesMatch[1]) : (parseInt(a.querySelector('.js-like-count')?.textContent) || 0);
           const bLikes = bLikesMatch ? parseInt(bLikesMatch[1]) : (parseInt(b.querySelector('.js-like-count')?.textContent) || 0);
           return bLikes - aLikes;
        } else {
           const da = parseInt(a.getAttribute('data-date') || '0');
           const db = parseInt(b.getAttribute('data-date') || '0');
           return order === 'newest' ? db - da : da - db;
        }
      });
      sorted.forEach(card => grid.appendChild(card));
    }"""

replacement_new = """    function applySort(order) {
      // Only sort non-pinned cards inside main grid container so Top 3 Hero Row remains untouched
      const cards = Array.from(grid.querySelectorAll('[data-category]'));
      const sorted = cards.sort((a, b) => {
        if (order === 'helpful') {
           const aLikesMatch = a.innerHTML.match(/(?:&#128077;|👍)\s*<span[^>]*>(\d+)<\/span>/) || a.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
           const bLikesMatch = b.innerHTML.match(/(?:&#128077;|👍)\s*<span[^>]*>(\d+)<\/span>/) || b.innerHTML.match(/&#128077;\s*(\d+)\s*Helpful/);
           const aLikes = aLikesMatch ? parseInt(aLikesMatch[1]) : (parseInt(a.querySelector('.js-like-count')?.textContent) || 0);
           const bLikes = bLikesMatch ? parseInt(bLikesMatch[1]) : (parseInt(b.querySelector('.js-like-count')?.textContent) || 0);
           return bLikes - aLikes;
        } else {
           const da = parseInt(a.getAttribute('data-date') || '0');
           const db = parseInt(b.getAttribute('data-date') || '0');
           return order === 'newest' ? db - da : da - db;
        }
      });
      sorted.forEach(card => grid.appendChild(card));
    }"""

for filePath in files:
    if os.path.exists(filePath):
        with open(filePath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_old in content:
            new_content = content.replace(target_old, replacement_new)
            with open(filePath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"SUCCESSFULLY UPDATED: {filePath}")
        else:
            print(f"TARGET NOT FOUND IN: {filePath}")
