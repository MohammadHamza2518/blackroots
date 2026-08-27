import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

dp_html_block = """        <!-- Customer Profile Photo / DP Upload Field (Optional) -->
        <div class="space-y-1.5 bg-white/5 p-3.5 rounded-2xl border border-white/10">
          <label class="block text-xs font-bold text-gray-200 uppercase tracking-wider">
            Customer Profile Photo / DP <span class="text-gray-400 font-normal lowercase">(optional avatar photo)</span>
          </label>
          <div class="flex items-center gap-3.5">
            <div id="dp-preview-circle" class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden relative cursor-pointer border border-white/20 hover:scale-105 transition-transform group">
              <input type="file" id="review-dp-input" accept="image/*" class="absolute inset-0 opacity-0 cursor-pointer w-full h-full z-10" title="Click to select DP photo">
              <div id="dp-placeholder" class="w-full h-full rounded-full bg-[#1a1d26] text-amber-300 font-bold text-base flex items-center justify-center group-hover:bg-[#252a38] transition-colors">
                👤
              </div>
              <img id="dp-preview-img" src="" alt="DP Preview" class="hidden w-full h-full rounded-full object-cover object-center">
            </div>
            <div class="space-y-1">
              <label for="review-dp-input" class="inline-block text-xs font-bold text-amber-300 hover:text-amber-200 cursor-pointer underline">
                📷 Choose Customer Profile Photo (DP)
              </label>
              <p class="text-[10px] text-gray-400">Attach your profile picture to display verified DP avatar on your review card. Max 5MB.</p>
              <button type="button" id="remove-dp-btn" class="hidden text-[10px] text-red-400 hover:text-red-300 font-bold">
                ✕ Remove DP Photo
              </button>
            </div>
          </div>
        </div>

        <!-- Customer Name & Location Grid -->"""

old_name_grid = """        <!-- Customer Name & Location Grid -->"""

dp_js_vars = """      const photoInput = document.getElementById('review-photo-input');
      const photoPlaceholder = document.getElementById('photo-upload-placeholder');
      const photoPreviewContainer = document.getElementById('photo-preview-container');
      const photoCountBadge = document.getElementById('photo-count-badge');
      
      const dpInput = document.getElementById('review-dp-input');
      const dpPreviewImg = document.getElementById('dp-preview-img');
      const dpPlaceholder = document.getElementById('dp-placeholder');
      const removeDpBtn = document.getElementById('remove-dp-btn');
      let uploadedDpDataUrl = '';"""

old_js_vars = """      const photoInput = document.getElementById('review-photo-input');
      const photoPlaceholder = document.getElementById('photo-upload-placeholder');
      const photoPreviewContainer = document.getElementById('photo-preview-container');
      const photoCountBadge = document.getElementById('photo-count-badge');"""

dp_js_handlers = """      // DP Avatar Upload Handler
      if (dpInput) {
        dpInput.addEventListener('change', function(e) {
          const file = e.target.files[0];
          if (!file) return;
          if (file.size > 5 * 1024 * 1024) {
            alert('Profile photo size exceeds 5MB limit!');
            dpInput.value = '';
            return;
          }
          const reader = new FileReader();
          reader.onload = function(evt) {
            uploadedDpDataUrl = evt.target.result;
            if (dpPreviewImg) {
              dpPreviewImg.src = uploadedDpDataUrl;
              dpPreviewImg.classList.remove('hidden');
            }
            if (dpPlaceholder) dpPlaceholder.classList.add('hidden');
            if (removeDpBtn) removeDpBtn.classList.remove('hidden');
          };
          reader.readAsDataURL(file);
        });
      }

      if (removeDpBtn) {
        removeDpBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          uploadedDpDataUrl = '';
          if (dpInput) dpInput.value = '';
          if (dpPreviewImg) {
            dpPreviewImg.src = '';
            dpPreviewImg.classList.add('hidden');
          }
          if (dpPlaceholder) dpPlaceholder.classList.remove('hidden');
          removeDpBtn.classList.add('hidden');
        });
      }

      // Max 2 Photos Upload Handler"""

old_js_photo_handler = """      // Max 2 Photos Upload Handler"""

old_card_avatar = """                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="${data.name}">
                  ${initials}
                </div>"""

new_card_avatar = """${avatarMarkup}"""

old_card_func_start = """        const initials = getInitials(data.name);"""

new_card_func_start = """        const initials = getInitials(data.name);
        let avatarMarkup = '';
        if (data.dp) {
          avatarMarkup = `
            <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden border border-white/20" title="${data.name}">
              <img src="${data.dp}" alt="${data.name}" class="w-full h-full rounded-full object-cover object-center">
            </div>
          `;
        } else {
          avatarMarkup = `
            <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="${data.name}">
              ${initials}
            </div>
          `;
        }"""

old_new_review_obj = """          const newReview = {
            id: 'user-review-' + Date.now(),
            name: name,
            city: city,
            title: title,
            body: body,
            rating: rating,
            category: category,
            timestamp: Date.now(),
            date: new Date().toISOString().slice(0,10).replace(/-/g, ''),
            photos: uploadedPhotosDataUrls,
            likes: 0
          };"""

new_new_review_obj = """          const newReview = {
            id: 'user-review-' + Date.now(),
            name: name,
            city: city,
            title: title,
            body: body,
            rating: rating,
            category: category,
            timestamp: Date.now(),
            date: new Date().toISOString().slice(0,10).replace(/-/g, ''),
            photos: uploadedPhotosDataUrls,
            dp: uploadedDpDataUrl,
            likes: 0
          };"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_name_grid, dp_html_block)
        content = content.replace(old_js_vars, dp_js_vars)
        content = content.replace(old_js_photo_handler, dp_js_handlers)
        content = content.replace(old_card_func_start, new_card_func_start)
        content = content.replace(old_card_avatar, new_card_avatar)
        content = content.replace(old_new_review_obj, new_new_review_obj)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SUCCESSFULLY ADDED DP UPLOAD FEATURE TO: {fpath}")

