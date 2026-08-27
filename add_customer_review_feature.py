import os
import shutil

modal_html = """
  <!-- Customer Write Review Modal (Flipkart / Amazon Style) -->
  <div id="add-review-modal" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-black/80 backdrop-blur-md opacity-0 pointer-events-none transition-all duration-300">
    
    <div id="modal-card" class="bg-[#12151c] border border-[#d4af37]/40 shadow-2xl rounded-3xl p-6 sm:p-8 max-w-lg w-full max-h-[90vh] overflow-y-auto relative text-left transform scale-95 transition-all duration-300">
      
      <!-- Close Button -->
      <button type="button" id="close-review-modal" class="absolute top-5 right-5 w-9 h-9 rounded-full bg-white/5 hover:bg-white/10 border border-white/10 text-gray-400 hover:text-white flex items-center justify-center text-lg font-bold transition-colors">
        ✕
      </button>

      <!-- Modal Header -->
      <div class="mb-6 space-y-1 pr-8">
        <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-950/80 border border-emerald-500/40 text-emerald-400 text-[11px] font-bold uppercase tracking-wider mb-2">
          <span>✓ Verified Customer Review</span>
        </div>
        <h3 class="font-serif text-2xl sm:text-3xl font-bold text-white flex items-center gap-2">
          <span>✍️</span> Write Your Customer Review
        </h3>
        <p class="text-xs text-gray-300 font-light">
          Share your genuine experience with BlackRoots. Max 2 photos proof & 300 words. Published live for 1,280+ shoppers!
        </p>
      </div>

      <!-- Review Submission Form -->
      <form id="review-form" class="space-y-4">
        
        <!-- Interactive Star Rating Picker -->
        <div class="space-y-1.5 bg-white/5 p-4 rounded-2xl border border-white/10">
          <label class="block text-xs font-bold text-gray-200 uppercase tracking-wider">
            Overall Rating <span class="text-amber-400">*</span>
          </label>
          <div class="flex items-center gap-3">
            <div id="star-rating-picker" class="flex text-3xl text-gray-600 cursor-pointer select-none">
              <span data-star="1" class="hover:scale-125 transition-transform px-0.5 text-amber-400">★</span>
              <span data-star="2" class="hover:scale-125 transition-transform px-0.5 text-amber-400">★</span>
              <span data-star="3" class="hover:scale-125 transition-transform px-0.5 text-amber-400">★</span>
              <span data-star="4" class="hover:scale-125 transition-transform px-0.5 text-amber-400">★</span>
              <span data-star="5" class="hover:scale-125 transition-transform px-0.5 text-amber-400">★</span>
            </div>
            <span id="star-rating-label" class="text-xs font-bold text-amber-300 bg-amber-400/10 border border-amber-400/30 px-3 py-1 rounded-full whitespace-nowrap">
              5.0 — Outstanding!
            </span>
            <input type="hidden" id="review-rating" name="rating" value="5">
          </div>
        </div>

        <!-- Customer Name & Location Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="space-y-1">
            <label for="review-name" class="block text-xs font-bold text-gray-300">Your Full Name <span class="text-amber-400">*</span></label>
            <input type="text" id="review-name" required placeholder="e.g. Priya Sharma" class="w-full bg-[#1a1d26] border border-white/10 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-colors">
          </div>
          <div class="space-y-1">
            <label for="review-city" class="block text-xs font-bold text-gray-300">Select City / State <span class="text-amber-400">* (Compulsory)</span></label>
            <input type="text" id="review-city" list="city-list" required placeholder="e.g. Delhi NCR, Mumbai, Lucknow" class="w-full bg-[#1a1d26] border border-white/10 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-colors">
            <datalist id="city-list">
              <option value="Delhi NCR">
              <option value="Mumbai, Maharashtra">
              <option value="Bengaluru, Karnataka">
              <option value="Hyderabad, Telangana">
              <option value="Kolkata, West Bengal">
              <option value="Chennai, Tamil Nadu">
              <option value="Pune, Maharashtra">
              <option value="Ahmedabad, Gujarat">
              <option value="Jaipur, Rajasthan">
              <option value="Lucknow, Uttar Pradesh">
              <option value="Kanpur, Uttar Pradesh">
              <option value="Patna, Bihar">
              <option value="Surat, Gujarat">
              <option value="Chandigarh">
              <option value="Indore, Madhya Pradesh">
              <option value="Bhopal, Madhya Pradesh">
              <option value="Nagpur, Maharashtra">
              <option value="Dehradun, Uttarakhand">
              <option value="Kochi, Kerala">
              <option value="Guwahati, Assam">
            </datalist>
          </div>
        </div>

        <!-- Category Selection Tag -->
        <div class="space-y-1.5">
          <label class="block text-xs font-bold text-gray-300">Usage Category</label>
          <div class="grid grid-cols-2 gap-3">
            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-xl border border-white/10 bg-[#1a1d26] hover:border-[#d4af37]/50 transition-colors">
              <input type="radio" name="review-category" value="men photo" class="accent-[#d4af37]">
              <span class="text-xs text-amber-300 font-semibold">👨 Men's Scalp & Beard</span>
            </label>
            <label class="cursor-pointer flex items-center gap-2 p-2.5 rounded-xl border border-white/10 bg-[#1a1d26] hover:border-[#d4af37]/50 transition-colors">
              <input type="radio" name="review-category" value="women photo" checked class="accent-[#d4af37]">
              <span class="text-xs text-pink-300 font-semibold">👩 Women's Hair & Roots</span>
            </label>
          </div>
        </div>

        <!-- Review Title -->
        <div class="space-y-1">
          <label for="review-title" class="block text-xs font-bold text-gray-300">Review Title / Headline <span class="text-amber-400">*</span></label>
          <input type="text" id="review-title" required placeholder="e.g. Visible dark hair transition in 3 washes!" class="w-full bg-[#1a1d26] border border-white/10 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-colors">
        </div>

        <!-- Review Body Text (Max 300 Words) -->
        <div class="space-y-1">
          <div class="flex items-center justify-between">
            <label for="review-body" class="block text-xs font-bold text-gray-300">Detailed Experience <span class="text-amber-400">*</span></label>
            <span id="word-count-badge" class="text-[11px] font-bold text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-500/30">0 / 300 words</span>
          </div>
          <textarea id="review-body" rows="4" required placeholder="Describe your experience: scalp sensation, grey coverage, fragrance, how many washes it took... (Max 300 words)" class="w-full bg-[#1a1d26] border border-white/10 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-colors resize-none"></textarea>
          <p id="word-count-error" class="hidden text-[11px] text-red-400 font-bold">⚠️ Review text cannot exceed 300 words limit!</p>
        </div>

        <!-- Max 2 Photos Upload Field (Flipkart & Amazon Style) -->
        <div class="space-y-2">
          <div class="flex items-center justify-between">
            <label class="block text-xs font-bold text-gray-300">📸 Attach Photos (Max 2 Photos)</label>
            <span id="photo-count-badge" class="text-[10px] text-amber-300 font-semibold">0 / 2 photos selected</span>
          </div>
          
          <div id="photo-upload-container" class="border-2 border-dashed border-white/20 hover:border-[#d4af37]/60 rounded-2xl p-4 text-center bg-white/5 transition-colors cursor-pointer relative">
            <input type="file" id="review-photo-input" accept="image/*" multiple class="absolute inset-0 opacity-0 cursor-pointer w-full h-full z-10">
            
            <div id="photo-upload-placeholder" class="space-y-1 pointer-events-none">
              <div class="text-2xl">📸</div>
              <p class="text-xs text-gray-300 font-medium">Click or Drag photos here (Upload up to 2 photos)</p>
              <p class="text-[10px] text-gray-500">e.g., Photo 1: Hair Before/Bottle &bull; Photo 2: Hair After/Result</p>
            </div>

            <!-- Preview Grid for up to 2 Photos -->
            <div id="photo-preview-container" class="hidden flex-wrap items-center justify-center gap-3 relative z-20 pointer-events-auto pt-1">
              <!-- Dynamically populated previews -->
            </div>
          </div>
        </div>

        <!-- Verified Checkbox -->
        <div class="flex items-center gap-2 pt-1">
          <input type="checkbox" id="review-verified" checked class="w-4 h-4 accent-emerald-500 rounded cursor-pointer">
          <label for="review-verified" class="text-xs text-gray-300 cursor-pointer select-none">
            I certify this is a genuine purchase & honest experience with BlackRoots Shampoo.
          </label>
        </div>

        <!-- Form Submit Buttons -->
        <div class="pt-4 flex items-center justify-end gap-3 border-t border-white/10">
          <button type="button" id="cancel-review-btn" class="px-5 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 text-gray-300 font-bold text-xs transition-colors">
            Cancel
          </button>
          <button type="submit" id="submit-review-btn" class="bg-gradient-to-r from-[#d4af37] via-amber-300 to-[#d4af37] text-black font-extrabold text-xs py-3 px-6 rounded-xl hover:shadow-[0_0_20px_rgba(212,175,55,0.4)] transition-all transform active:scale-95 flex items-center gap-2 shadow-xl">
            <span>🚀 Publish Review Live</span>
          </button>
        </div>

      </form>
    </div>
  </div>

  <!-- Dynamic Toast Notification Container -->
  <div id="review-toast" class="fixed top-6 right-6 z-[110] bg-gradient-to-r from-[#123824] to-[#0a2014] border border-[#d4af37] text-white p-4 rounded-2xl shadow-2xl max-w-sm flex items-center gap-3 transform translate-y-[-100px] opacity-0 transition-all duration-500 pointer-events-none">
    <div class="w-10 h-10 rounded-full bg-[#d4af37] text-black text-xl flex items-center justify-center font-bold shrink-0">🎉</div>
    <div>
      <h4 id="toast-title" class="font-bold text-xs text-amber-300 uppercase tracking-wide">Review Published!</h4>
      <p id="toast-msg" class="text-xs text-gray-200">Your review has been added live to the customer ratings grid.</p>
    </div>
  </div>
"""

modal_js = r"""
  <script>
    // Write a Customer Review Modal & Real-Time Grid Prepend Logic (Compulsory City & Relative Time Display)
    document.addEventListener('DOMContentLoaded', function() {
      const modal = document.getElementById('add-review-modal');
      const modalCard = document.getElementById('modal-card');
      const openModalBtns = document.querySelectorAll('.js-open-review-modal');
      const closeModalBtn = document.getElementById('close-review-modal');
      const cancelModalBtn = document.getElementById('cancel-review-btn');
      const reviewForm = document.getElementById('review-form');
      
      const starPicker = document.getElementById('star-rating-picker');
      const starRatingInput = document.getElementById('review-rating');
      const starRatingLabel = document.getElementById('star-rating-label');
      
      const reviewBodyInput = document.getElementById('review-body');
      const wordCountBadge = document.getElementById('word-count-badge');
      const wordCountError = document.getElementById('word-count-error');
      
      const photoInput = document.getElementById('review-photo-input');
      const photoPlaceholder = document.getElementById('photo-upload-placeholder');
      const photoPreviewContainer = document.getElementById('photo-preview-container');
      const photoCountBadge = document.getElementById('photo-count-badge');
      
      let uploadedPhotosDataUrls = [];

      const starLabels = {
        1: '1.0 — Poor',
        2: '2.0 — Fair',
        3: '3.0 — Good',
        4: '4.0 — Very Good',
        5: '5.0 — Outstanding!'
      };

      // Open Modal Function
      function openModal() {
        if (!modal) return;
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modalCard.classList.remove('scale-95');
        modalCard.classList.add('scale-100');
        document.body.style.overflow = 'hidden';
      }

      // Close Modal Function
      function closeModal() {
        if (!modal) return;
        modal.classList.add('opacity-0', 'pointer-events-none');
        modalCard.classList.remove('scale-100');
        modalCard.classList.add('scale-95');
        document.body.style.overflow = '';
      }

      openModalBtns.forEach(btn => btn.addEventListener('click', openModal));
      if (closeModalBtn) closeModalBtn.addEventListener('click', closeModal);
      if (cancelModalBtn) cancelModalBtn.addEventListener('click', closeModal);

      if (modal) {
        modal.addEventListener('click', function(e) {
          if (e.target === modal) closeModal();
        });
      }

      // Star Rating Hover & Select Handler
      if (starPicker) {
        const stars = starPicker.querySelectorAll('[data-star]');
        
        function updateStars(rating) {
          starRatingInput.value = rating;
          starRatingLabel.textContent = starLabels[rating] || (rating + '.0');
          
          stars.forEach(star => {
            const sVal = parseInt(star.getAttribute('data-star'));
            if (sVal <= rating) {
              star.classList.add('text-amber-400');
              star.classList.remove('text-gray-600');
            } else {
              star.classList.remove('text-amber-400');
              star.classList.add('text-gray-600');
            }
          });
        }

        stars.forEach(star => {
          star.addEventListener('click', function() {
            const val = parseInt(this.getAttribute('data-star'));
            updateStars(val);
          });

          star.addEventListener('mouseenter', function() {
            const val = parseInt(this.getAttribute('data-star'));
            stars.forEach(s => {
              const sVal = parseInt(s.getAttribute('data-star'));
              if (sVal <= val) {
                s.classList.add('text-amber-400');
                s.classList.remove('text-gray-600');
              } else {
                s.classList.remove('text-amber-400');
                s.classList.add('text-gray-600');
              }
            });
          });
        });

        starPicker.addEventListener('mouseleave', function() {
          const currentVal = parseInt(starRatingInput.value) || 5;
          updateStars(currentVal);
        });
      }

      // Live 300 Word Counter Handler
      function getWordCount(text) {
        const words = text.trim().split(/\s+/).filter(w => w.length > 0);
        return words.length;
      }

      if (reviewBodyInput && wordCountBadge) {
        reviewBodyInput.addEventListener('input', function() {
          const count = getWordCount(this.value);
          wordCountBadge.textContent = `${count} / 300 words`;

          if (count > 300) {
            wordCountBadge.classList.remove('text-emerald-400', 'bg-emerald-950/60', 'border-emerald-500/30');
            wordCountBadge.classList.add('text-red-400', 'bg-red-950/80', 'border-red-500/50');
            if (wordCountError) wordCountError.classList.remove('hidden');
          } else {
            wordCountBadge.classList.remove('text-red-400', 'bg-red-950/80', 'border-red-500/50');
            wordCountBadge.classList.add('text-emerald-400', 'bg-emerald-950/60', 'border-emerald-500/30');
            if (wordCountError) wordCountError.classList.add('hidden');
          }
        });
      }

      // Dynamic Relative Time Formatter ("Itne Din Purana")
      function getRelativeTime(timestamp) {
        if (!timestamp) return 'Just Now';
        const now = Date.now();
        const elapsedMs = now - timestamp;
        const elapsedSec = Math.floor(elapsedMs / 1000);
        const elapsedMin = Math.floor(elapsedSec / 60);
        const elapsedHours = Math.floor(elapsedMin / 60);
        const elapsedDays = Math.floor(elapsedHours / 24);
        const elapsedWeeks = Math.floor(elapsedDays / 7);

        if (elapsedSec < 45) return 'Just Now';
        if (elapsedMin < 60) return `${elapsedMin} ${elapsedMin === 1 ? 'min' : 'mins'} ago`;
        if (elapsedHours < 24) return `${elapsedHours} ${elapsedHours === 1 ? 'hour' : 'hours'} ago`;
        if (elapsedDays < 7) return `${elapsedDays} ${elapsedDays === 1 ? 'day' : 'days'} ago`;
        return `${elapsedWeeks} ${elapsedWeeks === 1 ? 'week' : 'weeks'} ago`;
      }

      // Max 2 Photos Upload Handler
      function renderPhotoPreviews() {
        if (!photoPreviewContainer) return;
        photoPreviewContainer.innerHTML = '';

        if (uploadedPhotosDataUrls.length === 0) {
          photoPreviewContainer.classList.add('hidden');
          photoPreviewContainer.classList.remove('flex');
          if (photoPlaceholder) photoPlaceholder.classList.remove('hidden');
          if (photoCountBadge) photoCountBadge.textContent = '0 / 2 photos selected';
          return;
        }

        if (photoPlaceholder) photoPlaceholder.classList.add('hidden');
        photoPreviewContainer.classList.remove('hidden');
        photoPreviewContainer.classList.add('flex');
        if (photoCountBadge) photoCountBadge.textContent = `${uploadedPhotosDataUrls.length} / 2 photos selected`;

        uploadedPhotosDataUrls.forEach((url, idx) => {
          const wrapper = document.createElement('div');
          wrapper.className = "relative flex flex-col items-center gap-1";
          wrapper.innerHTML = `
            <div class="w-20 h-20 rounded-xl overflow-hidden border border-[#d4af37] shadow-lg relative bg-black">
              <img src="${url}" alt="Preview ${idx + 1}" class="w-full h-full object-cover">
              <span class="absolute top-1 left-1 bg-black/70 text-amber-300 font-bold text-[9px] px-1.5 py-0.5 rounded">#${idx + 1}</span>
            </div>
            <button type="button" class="js-remove-photo-item text-[10px] text-red-400 hover:text-red-300 font-bold bg-red-950/80 px-2 py-0.5 rounded-full border border-red-500/30" data-index="${idx}">
              ✕ Remove
            </button>
          `;
          photoPreviewContainer.appendChild(wrapper);
        });

        // Remove item click listeners
        const removeBtns = photoPreviewContainer.querySelectorAll('.js-remove-photo-item');
        removeBtns.forEach(btn => {
          btn.addEventListener('click', function(e) {
            e.stopPropagation();
            const index = parseInt(this.getAttribute('data-index'));
            uploadedPhotosDataUrls.splice(index, 1);
            renderPhotoPreviews();
          });
        });
      }

      if (photoInput) {
        photoInput.addEventListener('change', function(e) {
          const files = Array.from(e.target.files);
          if (!files.length) return;

          const availableSlots = 2 - uploadedPhotosDataUrls.length;
          if (availableSlots <= 0) {
            alert('Maximum 2 photos allowed per review!');
            photoInput.value = '';
            return;
          }

          const filesToProcess = files.slice(0, availableSlots);
          if (files.length > availableSlots) {
            alert(`You can only upload up to 2 photos. Processing first ${availableSlots} photo(s).`);
          }

          let processed = 0;
          filesToProcess.forEach(file => {
            if (file.size > 5 * 1024 * 1024) {
              alert(`File "${file.name}" exceeds 5MB limit and was skipped.`);
              return;
            }
            const reader = new FileReader();
            reader.onload = function(evt) {
              uploadedPhotosDataUrls.push(evt.target.result);
              processed++;
              if (processed === filesToProcess.length) {
                renderPhotoPreviews();
                photoInput.value = '';
              }
            };
            reader.readAsDataURL(file);
          });
        });
      }

      // Toast Notification Function
      function showToast(name) {
        const toast = document.getElementById('review-toast');
        const toastMsg = document.getElementById('toast-msg');
        if (!toast) return;

        if (toastMsg) {
          toastMsg.textContent = `Thank you ${name}! Your review has been added live to the page.`;
        }

        toast.classList.remove('translate-y-[-100px]', 'opacity-0', 'pointer-events-none');
        toast.classList.add('translate-y-0', 'opacity-100');

        setTimeout(() => {
          toast.classList.remove('translate-y-0', 'opacity-100');
          toast.classList.add('translate-y-[-100px]', 'opacity-0', 'pointer-events-none');
        }, 5000);
      }

      // User Initials Creator
      function getInitials(name) {
        const parts = name.trim().split(' ');
        if (parts.length >= 2) {
          return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
        }
        return name.slice(0, 2).toUpperCase();
      }

      // Create Review Card DOM Element (With Dynamic Relative Time & Compulsory City Display)
      function createCardElement(data) {
        const div = document.createElement('div');
        div.className = "p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/40 shadow-xl flex flex-col break-inside-avoid mb-6 animate-fadeIn relative overflow-hidden";
        div.style.cssText = "height: max-content; break-inside: avoid-column !important; -webkit-column-break-inside: avoid !important; display: inline-block !important; width: 100% !important; margin-bottom: 1.5rem !important;";
        div.setAttribute('data-category', data.category);
        div.setAttribute('data-date', data.date);

        const initials = getInitials(data.name);
        const categoryBadge = data.category.includes('men') 
          ? '<span class="text-[10px] text-amber-300 bg-amber-400/10 border-amber-400/30 font-semibold px-2 py-0.5 rounded-full border">👨 Men\'s Scalp</span>'
          : '<span class="text-[10px] text-pink-300 bg-pink-400/10 border-pink-400/30 font-semibold px-2 py-0.5 rounded-full border">👩 Women\'s Hair</span>';

        const starCount = parseInt(data.rating) || 5;
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
            <div class="rounded-2xl overflow-hidden border border-white/10 relative bg-black/60 mt-3" style="aspect-ratio: 1/1; max-height: 300px;">
              <img src="${photosArray[0]}" alt="Customer Photo Proof" class="w-full h-full object-cover object-center">
            </div>
          `;
        } else if (photosArray.length >= 2) {
          photoMarkup = `
            <div class="grid grid-cols-2 gap-2 mt-3">
              <div class="rounded-xl overflow-hidden border border-white/10 relative bg-black/60" style="aspect-ratio: 1/1; max-height: 220px;">
                <img src="${photosArray[0]}" alt="Customer Photo Proof 1" class="w-full h-full object-cover object-center">
                <span class="absolute bottom-1.5 left-1.5 bg-black/70 text-amber-300 text-[9px] font-bold px-1.5 py-0.5 rounded">Photo 1</span>
              </div>
              <div class="rounded-xl overflow-hidden border border-white/10 relative bg-black/60" style="aspect-ratio: 1/1; max-height: 220px;">
                <img src="${photosArray[1]}" alt="Customer Photo Proof 2" class="w-full h-full object-cover object-center">
                <span class="absolute bottom-1.5 left-1.5 bg-black/70 text-amber-300 text-[9px] font-bold px-1.5 py-0.5 rounded">Photo 2</span>
              </div>
            </div>
          `;
        }

        div.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="${data.name}">
                  ${initials}
                </div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug flex items-center gap-1.5">
                    ${data.name}
                    <span class="text-[9px] bg-amber-400/20 text-amber-300 px-1.5 py-0.2 rounded border border-amber-400/40 font-mono uppercase">NEW</span>
                  </h3>
                  <span class="text-[10px] text-gray-400 block">${data.city} &bull; ${relativeTimeText}</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">${starsHtml} <span class="text-white font-bold ml-1">${parseFloat(data.rating).toFixed(1)}</span></div>
              ${categoryBadge}
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"${data.title}"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light whitespace-pre-line">${data.body}</p>
            ${photoMarkup}
          </div>
          <div class="pt-4 mt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="js-like-btn hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300 transition-colors" data-likes="${data.likes || 0}">
              👍 <span class="js-like-count">${data.likes || 0}</span> Helpful
            </button>
          </div>
        `;

        // Add Like click functionality
        const likeBtn = div.querySelector('.js-like-btn');
        if (likeBtn) {
          likeBtn.addEventListener('click', function() {
            let likes = parseInt(this.getAttribute('data-likes')) || 0;
            likes++;
            this.setAttribute('data-likes', likes);
            this.querySelector('.js-like-count').textContent = likes;
            this.classList.add('text-amber-400');
          });
        }

        return div;
      }

      // Load Saved User Reviews from LocalStorage
      const grid = document.querySelector('.columns-1');
      function loadUserReviews() {
        if (!grid) return;
        const stored = localStorage.getItem('blackroots_user_reviews');
        if (stored) {
          try {
            const userReviews = JSON.parse(stored);
            userReviews.reverse().forEach(data => {
              const card = createCardElement(data);
              grid.insertBefore(card, grid.firstChild);
            });
            // Update counts
            const showingCount = document.querySelector('.js-showing-count');
            const visibleCards = document.querySelectorAll('[data-category]').length;
            if (showingCount) showingCount.textContent = visibleCards + ' Reviews';
          } catch(e) {
            console.error('Error loading saved reviews', e);
          }
        }
      }

      loadUserReviews();

      // Form Submit Handler
      if (reviewForm) {
        reviewForm.addEventListener('submit', function(e) {
          e.preventDefault();
          
          const name = document.getElementById('review-name').value.trim();
          const city = document.getElementById('review-city').value.trim();
          const title = document.getElementById('review-title').value.trim();
          const body = reviewBodyInput.value.trim();
          const rating = starRatingInput.value || '5';
          const catRadio = document.querySelector('input[name="review-category"]:checked');
          let category = catRadio ? catRadio.value : 'women photo';

          // Compulsory City Check
          if (!city) {
            alert('Please enter or select your City/Location (Compulsory field)!');
            document.getElementById('review-city').focus();
            return;
          }

          // Word Count Check (Max 300 Words)
          const wordCount = getWordCount(body);
          if (wordCount > 300) {
            alert(`Your review text contains ${wordCount} words. Please shorten your review to 300 words or less!`);
            reviewBodyInput.focus();
            return;
          }

          if (uploadedPhotosDataUrls.length > 0 && !category.includes('photo')) {
            category += ' photo';
          }

          const now = new Date();
          const timestamp = now.getTime();
          const dateStr = now.getFullYear().toString() +
                          (now.getMonth() + 1).toString().padStart(2, '0') +
                          now.getDate().toString().padStart(2, '0');

          const reviewObj = {
            id: timestamp,
            name: name,
            city: city,
            title: title,
            body: body,
            rating: rating,
            category: category,
            photos: [...uploadedPhotosDataUrls],
            timestamp: timestamp,
            date: dateStr,
            likes: 1
          };

          // Save to LocalStorage
          let existing = [];
          try {
            existing = JSON.parse(localStorage.getItem('blackroots_user_reviews') || '[]');
          } catch(err) {
            existing = [];
          }
          existing.push(reviewObj);
          localStorage.setItem('blackroots_user_reviews', JSON.stringify(existing));

          // Prepend to Grid
          const cardEl = createCardElement(reviewObj);
          if (grid) {
            grid.insertBefore(cardEl, grid.firstChild);
            cardEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }

          // Reset Form & Close Modal
          reviewForm.reset();
          uploadedPhotosDataUrls = [];
          renderPhotoPreviews();
          if (wordCountBadge) {
            wordCountBadge.textContent = '0 / 300 words';
            wordCountBadge.className = "text-[11px] font-bold text-emerald-400 bg-emerald-950/60 px-2 py-0.5 rounded border border-emerald-500/30";
          }
          closeModal();

          // Show Toast Notification
          showToast(name);

          // Update visible review count
          const showingCount = document.querySelector('.js-showing-count');
          const totalCards = document.querySelectorAll('[data-category]').length;
          if (showingCount) showingCount.textContent = totalCards + ' Reviews';
        });
      }
    });
  </script>
"""

masonry_css = """
  <style>
    /* Absolute Masonry Stability Fix - Prevents Layout Shifting & Empty Black Gaps */
    .columns-1 > div, .columns-2 > div, .columns-3 > div {
      break-inside: avoid-column !important;
      -webkit-column-break-inside: avoid !important;
      page-break-inside: avoid !important;
      display: inline-block !important;
      width: 100% !important;
      margin-bottom: 1.5rem !important;
    }

    /* Custom Luxury Dark Gold Scrollbar for Modal Card */
    #modal-card::-webkit-scrollbar {
      width: 6px !important;
    }
    #modal-card::-webkit-scrollbar-track {
      background: rgba(18, 21, 28, 0.95) !important;
      border-radius: 9999px !important;
    }
    #modal-card::-webkit-scrollbar-thumb {
      background: linear-gradient(to bottom, #d4af37, #b38f28) !important;
      border-radius: 9999px !important;
      border: 1px solid rgba(212, 175, 55, 0.4) !important;
    }
    #modal-card::-webkit-scrollbar-thumb:hover {
      background: #f5e4ab !important;
    }
    #modal-card {
      scrollbar-width: thin !important;
      scrollbar-color: #d4af37 rgba(18, 21, 28, 0.95) !important;
    }
  </style>
"""

def update_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old modal & script if present
    if '<div id="add-review-modal"' in content:
        start_idx = content.find('<!-- Customer Write Review Modal')
        end_idx = content.find('</body>')
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + '</body>\n</html>'

    # Inject Masonry CSS fix into <head> if not present
    if 'break-inside: avoid-column !important' not in content:
        content = content.replace('</head>', masonry_css + '\n</head>')

    # 1. Inject Primary CTA button in Stat Box
    cta_html = '''
          <!-- Write Review Primary CTA Row -->
          <div class="md:col-span-12 pt-6 mt-2 border-t border-white/10 flex flex-wrap items-center justify-between gap-4">
            <div class="flex items-center gap-2 text-xs text-gray-300">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
              <span>Bought BlackRoots Herbal Shampoo? Help 1,280+ shoppers with your honest rating!</span>
            </div>
            <button type="button" class="js-open-review-modal bg-gradient-to-r from-[#d4af37] via-amber-300 to-[#d4af37] text-black font-extrabold text-xs py-3 px-6 rounded-xl hover:shadow-[0_0_20px_rgba(212,175,55,0.4)] transition-all transform hover:-translate-y-0.5 active:translate-y-0 flex items-center gap-2 shadow-lg cursor-pointer">
              <span>✍️</span> Write a Customer Review
            </button>
          </div>
'''
    if 'js-open-review-modal' not in content:
        stat_close = '</div>\n      </div>\n\n      <!-- Filter Controls'
        if stat_close in content:
            content = content.replace(stat_close, cta_html + '\n        </div>\n      </div>\n\n      <!-- Filter Controls')

    # 2. Inject Secondary CTA button in Filter Bar
    filter_bar_alt = '👩 Women\'s Hair & Roots (740+)\n          </button>'
    
    sec_cta = '''
          <button type="button" class="js-open-review-modal px-4 py-2 rounded-xl bg-gradient-to-r from-[#123824] to-[#1a4a30] hover:from-[#1a4a30] hover:to-[#123824] border border-[#d4af37]/50 text-[#f5e4ab] font-bold text-xs shadow-md transition-all flex items-center gap-1.5 hover:scale-105 active:scale-95 cursor-pointer ml-auto sm:ml-0">
            <span>✍️</span> Write Review
          </button>'''

    if sec_cta.strip() not in content and filter_bar_alt in content:
        content = content.replace(filter_bar_alt, filter_bar_alt + '\n' + sec_cta)

    # 3. Inject Modal & Toast HTML before </body>
    content = content.replace('</body>', modal_html + '\n' + modal_js + '\n</body>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {file_path} successfully!")

update_file('demo_lab/reviews.html')
update_file('reviews.html')
if os.path.exists('preview/reviews.html'):
    update_file('preview/reviews.html')

print("ALL REVIEWS FILES UPDATED WITH COMPULSORY CITY & RELATIVE TIME DISPLAY!")
