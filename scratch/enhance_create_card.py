import os
import re

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

enhanced_create_card = """      // Create Review Card DOM Element (Bulletproof Layout, Responsive & Symmetric)
      function createCardElement(data) {
        const div = document.createElement('div');
        div.className = "p-4 sm:p-6 rounded-2xl sm:rounded-3xl glass-panel-luxury border border-[#d4af37]/45 shadow-xl flex flex-col justify-between h-full transition-all duration-300 hover:border-[#d4af37] w-full box-border break-words overflow-hidden animate-fadeIn relative";
        div.style.cssText = "display: flex !important; width: 100% !important; max-width: 100% !important; margin-bottom: 0 !important; box-sizing: border-box !important;";
        div.setAttribute('data-category', data.category || 'all');
        div.setAttribute('data-date', data.date || Date.now());

        const initials = getInitials(data.name || 'Customer');
        let avatarMarkup = '';
        if (data.dp) {
          avatarMarkup = `
            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden border border-white/20" title="${data.name}">
              <img src="${data.dp}" alt="${data.name}" class="w-full h-full rounded-full object-cover object-center">
            </div>
          `;
        } else {
          avatarMarkup = `
            <div class="w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-xs sm:text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="${data.name}">
              ${initials}
            </div>
          `;
        }
        
        const catStr = (data.category || '').toLowerCase();
        const categoryBadge = catStr.includes('men') 
          ? '<span class="text-[9px] sm:text-[10px] text-amber-300 bg-amber-400/10 border-amber-400/30 font-semibold px-2 py-0.5 rounded-full border shrink-0">👨 Men\'s Scalp</span>'
          : '<span class="text-[9px] sm:text-[10px] text-pink-300 bg-pink-400/10 border-pink-400/30 font-semibold px-2 py-0.5 rounded-full border shrink-0">👩 Women\'s Hair</span>';

        const starCount = Math.min(5, Math.max(1, parseInt(data.rating) || 5));
        const starsHtml = '★'.repeat(starCount) + '☆'.repeat(5 - starCount);
        const relativeTimeText = getRelativeTime(data.timestamp || Date.now());

        let photosArray = [];
        if (Array.isArray(data.photos)) {
          photosArray = data.photos;
        } else if (data.photo) {
          photosArray = [data.photo];
        }

        let photoMarkup = '';
        if (photosArray.length === 1) {
          photoMarkup = `
            <div class="w-full rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mx-auto mt-2.5" style="aspect-ratio: 1/1; width: 100%; max-width: 100%;">
              <img src="${photosArray[0]}" alt="Customer Photo Proof" class="w-full h-full object-cover object-center">
            </div>
          `;
        } else if (photosArray.length >= 2) {
          photoMarkup = `
            <div class="grid grid-cols-2 gap-2 mt-2.5">
              <div class="w-full rounded-xl overflow-hidden border border-white/10 relative bg-black/60" style="aspect-ratio: 1/1;">
                <img src="${photosArray[0]}" alt="Customer Photo Proof 1" class="w-full h-full object-cover object-center">
                <span class="absolute bottom-1.5 left-1.5 bg-black/75 text-amber-300 text-[8px] font-bold px-1.5 py-0.2 rounded">Photo 1</span>
              </div>
              <div class="w-full rounded-xl overflow-hidden border border-white/10 relative bg-black/60" style="aspect-ratio: 1/1;">
                <img src="${photosArray[1]}" alt="Customer Photo Proof 2" class="w-full h-full object-cover object-center">
                <span class="absolute bottom-1.5 left-1.5 bg-black/75 text-amber-300 text-[8px] font-bold px-1.5 py-0.2 rounded">Photo 2</span>
              </div>
            </div>
          `;
        } else {
          // Filler badge for equal symmetrical heights
          photoMarkup = `
            <div class="mt-3 p-3 rounded-2xl bg-white/5 border border-white/10 text-[10px] text-gray-300 flex items-center justify-between">
              <span class="flex items-center gap-1.5 font-semibold text-emerald-400">
                <span>✓</span> Verified Scalp Buyer
              </span>
              <span class="text-amber-300 font-bold">100% Herbal Formula</span>
            </div>
          `;
        }

        // Sanitization helper
        function escapeHtml(str) {
          return (str || '').replace(/[&<>"']/g, function(m) {
            return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;'}[m];
          });
        }

        const safeName = escapeHtml(data.name || 'Customer');
        const safeCity = escapeHtml(data.city || 'India');
        const safeTitle = escapeHtml(data.title || 'Genuine Experience');
        const safeBody = escapeHtml(data.body || '');

        div.innerHTML = `
          <div class="space-y-2.5">
            <div class="flex items-center justify-between gap-2">
              <div class="flex items-center gap-2.5 min-w-0">
                ${avatarMarkup}
                <div class="min-w-0">
                  <h3 class="font-serif text-sm sm:text-base font-bold text-white leading-snug flex items-center gap-1.5 truncate">
                    <span>${safeName}</span>
                    <span class="text-[8px] bg-amber-400/20 text-amber-300 px-1 py-0.2 rounded border border-amber-400/40 font-mono uppercase shrink-0">NEW</span>
                  </h3>
                  <span class="text-[10px] text-gray-400 block truncate">${safeCity} &bull; ${relativeTimeText}</span>
                </div>
              </div>
              <span class="text-[9px] sm:text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2 py-0.5 rounded-full flex items-center gap-1 shrink-0">✓ Verified</span>
            </div>
            
            <div class="flex items-center justify-between pt-0.5">
              <div class="text-amber-400 text-xs tracking-wider">${starsHtml} <span class="text-white font-bold ml-1">${parseFloat(data.rating || 5).toFixed(1)}</span></div>
              ${categoryBadge}
            </div>
            
            <h4 class="font-serif text-base sm:text-lg font-bold text-white leading-snug break-words">"${safeTitle}"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light whitespace-pre-line break-words">${safeBody}</p>
            ${photoMarkup}
          </div>
          
          <div class="pt-3 mt-3 border-t border-white/10 flex items-center justify-between text-[10px] sm:text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="js-like-btn hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300 transition-colors cursor-pointer" data-likes="${data.likes || 1}">
              👍 <span class="js-like-count">${data.likes || 1}</span> Helpful
            </button>
          </div>
        `;

        // Add Like click functionality
        const likeBtn = div.querySelector('.js-like-btn');
        if (likeBtn) {
          likeBtn.addEventListener('click', function() {
            let likes = parseInt(this.getAttribute('data-likes')) || 1;
            likes++;
            this.setAttribute('data-likes', likes);
            this.querySelector('.js-like-count').textContent = likes;
            this.classList.add('text-amber-400');
          });
        }

        return div;
      }"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace createCardElement function
    pattern = r'\/\/ Create Review Card DOM Element.*?return div;\s*\}'
    new_content = re.sub(pattern, enhanced_create_card, content, flags=re.DOTALL)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Enhanced createCardElement in", fpath)

