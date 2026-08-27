/* ==========================================================================
   BlackRoots Official Theme JavaScript Engine
   ========================================================================== */

/* 📱 Mobile Navigation Drawer Controls */
function openMobileNavDrawer() {
  const drawer = document.getElementById('MobileNavDrawer');
  const backdrop = document.getElementById('MobileNavBackdrop');
  if (drawer) {
    drawer.classList.remove('translate-x-full');
    drawer.classList.add('translate-x-0');
  }
  if (backdrop) {
    backdrop.classList.remove('opacity-0', 'pointer-events-none');
    backdrop.classList.add('opacity-100', 'pointer-events-auto');
  }
  document.body.style.overflow = 'hidden';
}

function closeMobileNavDrawer() {
  const drawer = document.getElementById('MobileNavDrawer');
  const backdrop = document.getElementById('MobileNavBackdrop');
  if (drawer) {
    drawer.classList.remove('translate-x-0');
    drawer.classList.add('translate-x-full');
  }
  if (backdrop) {
    backdrop.classList.remove('opacity-100', 'pointer-events-auto');
    backdrop.classList.add('opacity-0', 'pointer-events-none');
  }
  document.body.style.overflow = '';
}

window.openMobileNavDrawer = openMobileNavDrawer;
window.closeMobileNavDrawer = closeMobileNavDrawer;

/* 🚚 Live India Pincode Delivery Estimator Engine */
window.executePincodeCheck = function(isExplicitClick) {
  const input = document.getElementById('HomePincodeInput');
  const box = document.getElementById('HomePincodeResult');
  const numSpan = document.getElementById('ResultPincodeNum');
  const dateSpan = document.getElementById('ResultExpectedDate');

  if (!input || !box) return;

  const raw = (input.value || '').toString().replace(/\D/g, '').slice(0, 6);
  input.value = raw;

  if (raw.length < 6) {
    if (isExplicitClick) {
      alert('Please enter a valid 6-digit Indian delivery pincode (e.g. 208001)');
      input.focus();
    }
    return;
  }

  // Calculate dynamic delivery timeline
  const today = new Date();
  let days = 3;
  // Metro / UP / Delhi / Mumbai / Kolkata / Bangalore / Hyderabad
  if (raw.startsWith('20') || raw.startsWith('11') || raw.startsWith('40') || raw.startsWith('70') || raw.startsWith('56') || raw.startsWith('50') || raw.startsWith('22') || raw.startsWith('24')) {
    days = 2;
  }
  today.setDate(today.getDate() + days);
  const dateStr = today.toLocaleDateString('en-IN', { weekday: 'long', month: 'short', day: 'numeric' });

  if (numSpan) numSpan.textContent = raw;
  if (dateSpan) dateSpan.textContent = dateStr;

  box.classList.remove('hidden');
  box.style.display = 'block';
};

/* 🕒 3-Minute Shower Scalp Massage Timer */
let showerInterval = null;
let showerSecondsLeft = 180;

function initShowerTimer() {
  const startBtn = document.getElementById('BtnStartShowerTimer');
  const resetBtn = document.getElementById('BtnResetShowerTimer');
  const display = document.getElementById('ShowerTimerDisplay');
  const progressBar = document.getElementById('ShowerTimerProgress');
  const statusText = document.getElementById('ShowerTimerStatus');

  if (!startBtn || !resetBtn || !display) return;

  function updateDisplay() {
    const mins = Math.floor(showerSecondsLeft / 60);
    const secs = showerSecondsLeft % 60;
    display.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

    if (progressBar) {
      const pct = ((180 - showerSecondsLeft) / 180) * 100;
      progressBar.style.width = `${pct}%`;
    }
  }

  startBtn.addEventListener('click', () => {
    if (showerInterval) {
      clearInterval(showerInterval);
      showerInterval = null;
      startBtn.innerHTML = '▶️ Resume Timer';
      if (statusText) statusText.textContent = '⏸️ Paused. Click resume to continue your scalp massage.';
      return;
    }

    startBtn.innerHTML = '⏸️ Pause Timer';
    if (statusText) statusText.textContent = '🌿 Nourishing roots... Gently massage in circular motions.';

    showerInterval = setInterval(() => {
      if (showerSecondsLeft > 0) {
        showerSecondsLeft--;
        updateDisplay();
      } else {
        clearInterval(showerInterval);
        showerInterval = null;
        startBtn.innerHTML = '🎉 Completed!';
        if (statusText) statusText.textContent = '✨ Time up! Rinse hair thoroughly with clean water for deep black shine.';
      }
    }, 1000);
  });

  resetBtn.addEventListener('click', () => {
    if (showerInterval) {
      clearInterval(showerInterval);
      showerInterval = null;
    }
    showerSecondsLeft = 180;
    startBtn.innerHTML = '▶️ Start 3-Min Scalp Massage Timer';
    if (statusText) statusText.textContent = 'Practice your 2-3 minute scalp massage routine during your shower!';
    updateDisplay();
  });

  updateDisplay();
}

/* 🔝 Sticky Header */
function initStickyHeader() {
  const header = document.querySelector('header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.classList.add('bg-black/95', 'backdrop-blur-md', 'shadow-2xl');
    } else {
      header.classList.remove('bg-black/95', 'backdrop-blur-md', 'shadow-2xl');
    }
  }, { passive: true });
}

/* 🛍️ Quantity Selectors */
function initQuantitySelectors() {
  document.querySelectorAll('.js-qty-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const isPlus = btn.classList.contains('js-qty-plus');
      const input = btn.closest('.js-qty-container')?.querySelector('.js-qty-input');
      if (!input) return;

      let val = parseInt(input.value) || 1;
      if (isPlus) {
        val = Math.min(val + 1, 10);
      } else {
        val = Math.max(val - 1, 1);
      }
      input.value = val;
    });
  });
}

/* 📱 Sticky Mobile Bottom Bar */
function initStickyMobileBar() {
  const bar = document.getElementById('StickyMobileBar');
  if (!bar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      bar.classList.remove('translate-y-full');
      bar.classList.add('translate-y-0');
    } else {
      bar.classList.remove('translate-y-0');
      bar.classList.add('translate-y-full');
    }
  }, { passive: true });
}

/* ⏳ Countdown Timer */
function initCountdownTimer() {
  const timerEls = document.querySelectorAll('.js-countdown');
  if (!timerEls.length) return;

  let totalSecs = 14 * 60 + 35; // 14 mins 35 secs default

  setInterval(() => {
    if (totalSecs > 0) totalSecs--;
    const m = Math.floor(totalSecs / 60);
    const s = totalSecs % 60;
    const str = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    timerEls.forEach(el => { el.textContent = str; });
  }, 1000);
}


/* 🔄 Before / After Interactive Split Slider */
function initBeforeAfterSlider() {
  const slider = document.getElementById('BeforeAfterSlider');
  if (!slider) return;

  const overlay = slider.querySelector('.js-ba-overlay');
  const handle = slider.querySelector('.js-ba-handle');
  const innerImg = slider.querySelector('.js-ba-inner-img');

  if (!overlay || !handle) return;

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
      move(e.touches[0].clientX);
    }
  }, { passive: true });

  window.addEventListener('touchend', () => {
    isDragging = false;
  });

  // Default split 50%
  overlay.style.width = '50%';
  handle.style.left = '50%';
}

/* 🩺 Dr. Kuroki — Chief AI Trichologist Clinical Response Engine */
function initAIConsultantChat() {
  const chatForm = document.getElementById('AIChatForm');
  const chatInput = document.getElementById('AIChatInput');
  const chatBox = document.getElementById('AIChatMessages');
  const promptPills = document.querySelectorAll('.js-ai-prompt-pill');

  if (!chatForm || !chatInput || !chatBox) return;

  // Quick Prompt Pills Click Handler
  promptPills.forEach(pill => {
    pill.addEventListener('click', () => {
      chatInput.value = pill.textContent.replace(/^[^a-zA-Z0-9]+/, '').trim();
      chatForm.dispatchEvent(new Event('submit'));
    });
  });

  // Clinical Response Knowledge Base
  function getDoctorResponse(query) {
    const q = query.toLowerCase();

    if (q.includes('grey') || q.includes('gray') || q.includes('safed') || q.includes('white hair') || q.includes('revers')) {
      return `
        <div class="space-y-2">
          <p><strong>Clinical Assessment: Melanin & Follicle Revival</strong></p>
          <p>Traditional chemical dyes simply coat the hair shaft with toxic ammonia and peroxide, which oxidizes your melanin stem cells and makes hair turn white faster.</p>
          <p><strong>How BlackRoots Works:</strong></p>
          <ul class="list-disc pl-4 space-y-1 text-[11px] text-gray-300">
            <li><strong>Polygonum Multiflorum (He Shou Wu):</strong> Clinically proven Japanese herb that activates tyrosinase enzyme for natural melanin deposit.</li>
            <li><strong>Black Sesame Bio-Pigments:</strong> Delivers natural botanical dark brown/black color pigments that lock onto keratin within 3 minutes of shower massage.</li>
            <li><strong>No Chemical Rebound:</strong> 100% Ammonia-free, PPD-free formula ensures your natural hair texture stays soft and roots remain nourished.</li>
          </ul>
          <div class="pt-2">
            <a href="product.html" class="inline-flex items-center gap-1.5 bg-[#d4af37] text-black font-extrabold text-[11px] px-3.5 py-1.5 rounded-lg shadow hover:bg-amber-300 transition-all">
              🛍️ Order BlackRoots 250ml (₹499) &rarr;
            </a>
          </div>
        </div>
      `;
    }

    if (q.includes('3 min') || q.includes('time') || q.includes('how to use') || q.includes('routine') || q.includes('ritual') || q.includes('kaise use')) {
      return `
        <div class="space-y-2">
          <p><strong>Dr. Kuroki's 3-Minute Shower Ritual Guide</strong></p>
          <ol class="list-decimal pl-4 space-y-1.5 text-[11px] text-gray-300">
            <li><strong>Wet Hair:</strong> Rinse hair or beard thoroughly with lukewarm water in the morning shower.</li>
            <li><strong>Pump & Massage (3 Mins):</strong> Pump BlackRoots Herbal Shampoo onto wet palms and massage into scalp, roots, and beard for 3 full minutes.</li>
            <li><strong>Rinse Clean:</strong> Rinse thoroughly with normal water. No extra conditioner or chemical post-wash needed!</li>
          </ol>
          <p class="text-[11px] text-emerald-400 font-medium">💡 Noticeable rich dark results from the first 2-3 washes!</p>
          <div class="pt-2">
            <a href="how-to-use.html" class="inline-flex items-center gap-1.5 bg-white/10 text-amber-300 border border-amber-400/40 font-bold text-[11px] px-3 py-1 rounded-lg hover:bg-amber-400 hover:text-black transition-all">
              🚿 3-Min Scalp Timer Ritual &rarr;
            </a>
          </div>
        </div>
      `;
    }

    if (q.includes('beard') || q.includes('darhi') || q.includes('face') || q.includes('skin')) {
      return `
        <div class="space-y-2">
          <p><strong>Dermatological Safety for Beard & Facial Hair</strong></p>
          <p>Yes, absolutely! BlackRoots is formulated with zero harsh parabens, zero ammonia, and zero peroxide, making it <strong>100% skin-safe for beard and mustache application</strong>.</p>
          <ul class="list-disc pl-4 space-y-1 text-[11px] text-gray-300">
            <li>Does NOT leave stubborn chemical black stains on facial skin.</li>
            <li>Enriched with Argan Oil & Ginseng to soften coarse beard hair and eliminate beard dandruff.</li>
            <li>Application: Apply on damp beard, leave for 3 minutes while showering, then rinse.</li>
          </ul>
          <div class="pt-2">
            <a href="product.html" class="inline-flex items-center gap-1.5 bg-[#d4af37] text-black font-extrabold text-[11px] px-3.5 py-1.5 rounded-lg shadow hover:bg-amber-300 transition-all">
              🧔 Order Beard & Hair Care • ₹499 &rarr;
            </a>
          </div>
        </div>
      `;
    }

    if (q.includes('ammonia') || q.includes('ppd') || q.includes('safe') || q.includes('side effect') || q.includes('chemical') || q.includes('nuksan')) {
      return `
        <div class="space-y-2">
          <p><strong>Safety & Toxicology Certificate</strong></p>
          <p>BlackRoots is certified <strong>100% Free of Ammonia, PPD, Resorcinol, Sulfates, and Parabens</strong>.</p>
          <ul class="list-disc pl-4 space-y-1 text-[11px] text-gray-300">
            <li>No burning sensation or itchy scalp irritation.</li>
            <li>Infused with Ayurvedic & Japanese botanical extracts: Reishi Mushroom, Biotin, Ginger Root, and Black Sesame.</li>
            <li>Safe for long-term weekly maintenance for both men and women.</li>
          </ul>
          <div class="pt-2">
            <a href="ingredients.html" class="inline-flex items-center gap-1.5 bg-white/10 text-amber-300 border border-amber-400/40 font-bold text-[11px] px-3 py-1 rounded-lg hover:bg-amber-400 hover:text-black transition-all">
              🌿 View Botanical Ingredients &rarr;
            </a>
          </div>
        </div>
      `;
    }

    if (q.includes('price') || q.includes('cost') || q.includes('cod') || q.includes('delivery') || q.includes('order') || q.includes('buy') || q.includes('kitna')) {
      return `
        <div class="space-y-2">
          <p><strong>Official Pricing & Express Delivery Status</strong></p>
          <p>A single 250ml bottle of BlackRoots Herbal Shampoo provides <strong>25 to 30 shower washes</strong> (lasts 2 to 3 months of usage).</p>
          <ul class="list-disc pl-4 space-y-1 text-[11px] text-gray-300">
            <li><strong>Price:</strong> <strong class="text-amber-400 font-bold">₹499 Only</strong> (Flat 50% Off Verified Special).</li>
            <li><strong>Delivery:</strong> Free Express COD Delivery across 19,000+ Indian Pincodes (Dispatched in 24h via Delhivery/BlueDart).</li>
            <li><strong>Payment:</strong> Cash on Delivery (COD) or UPI / Cards supported.</li>
          </ul>
          <div class="pt-2">
            <a href="product.html" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs px-4 py-2 rounded-xl shadow-xl hover:scale-105 transition-all">
              🛍️ Order Now • ₹499 &rarr;
            </a>
          </div>
        </div>
      `;
    }

    if (q.includes('fall') || q.includes('jharna') || q.includes('dandruff') || q.includes('rusi') || q.includes('growth')) {
      return `
        <div class="space-y-2">
          <p><strong>Scalp Follicle Strengthening Protocol</strong></p>
          <p>Hair fall and dandruff are typically caused by synthetic sulfates blocking hair follicle pores. BlackRoots treats this with root-nourishing actives:</p>
          <ul class="list-disc pl-4 space-y-1 text-[11px] text-gray-300">
            <li><strong>Pure Ginger Root Extract:</strong> Stimulates micro-circulation in the scalp capillaries to stop follicle shrinking.</li>
            <li><strong>Reishi Mushroom & Biotin:</strong> Strengthens hair keratin roots from within, reducing shower hair fall by up to 85%.</li>
            <li><strong>Scalp Cleanser:</strong> Natural saponins eliminate dry flakes and dandruff without stripping scalp moisture.</li>
          </ul>
          <div class="pt-2">
            <a href="product.html" class="inline-flex items-center gap-1.5 bg-[#d4af37] text-black font-extrabold text-[11px] px-3.5 py-1.5 rounded-lg shadow hover:bg-amber-300 transition-all">
              ✨ Stop Hair Fall • Order ₹499 &rarr;
            </a>
          </div>
        </div>
      `;
    }

    // Default Conversational Trichology Response
    return `
      <div class="space-y-2">
        <p>Thank you for consulting Dr. Kuroki. Based on clinical trichology principles for your inquiry ("<em>${query}</em>"):</p>
        <p>BlackRoots Herbal Shampoo is specially formulated to tackle <strong>grey hair, follicle weakness, and scalp damage</strong> using 100% botanical actives with zero ammonia.</p>
        <ul class="list-disc pl-4 space-y-1 text-[11px] text-gray-300">
          <li><strong>3-Minute Shower Wash:</strong> Works like normal shampoo while depositing natural bio-pigments.</li>
          <li><strong>Deep Nourishment:</strong> Restores natural shine, softness, and scalp health.</li>
        </ul>
        <div class="pt-2 flex flex-wrap gap-2">
          <a href="product.html" class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[11px] px-3.5 py-1.5 rounded-lg shadow hover:bg-amber-300 transition-all">
            🛍️ Buy BlackRoots • ₹499 &rarr;
          </a>
          <a href="reviews.html" class="inline-flex items-center gap-1 bg-white/10 text-amber-300 border border-amber-400/30 text-[11px] font-bold px-3 py-1.5 rounded-lg hover:bg-white/20 transition-all">
            ⭐ Read 1,280+ Reviews &rarr;
          </a>
        </div>
      </div>
    `;
  }

  function appendMessage(sender, htmlContent) {
    const isUser = sender === 'user';
    const msgDiv = document.createElement('div');
    msgDiv.className = `flex gap-2.5 sm:gap-3 ${isUser ? 'justify-end' : 'justify-start items-start'}`;

    if (isUser) {
      msgDiv.innerHTML = `
        <div class="max-w-[85%] sm:max-w-[75%] bg-gradient-to-r from-[#d4af37] to-[#e6c265] text-black font-semibold text-xs sm:text-sm p-3.5 rounded-2xl rounded-tr-none shadow-lg leading-relaxed">
          ${htmlContent}
        </div>
        <div class="w-8 h-8 rounded-full bg-white/20 border border-white/30 flex items-center justify-center text-xs text-white shrink-0 shadow-md font-bold">
          👤
        </div>
      `;
    } else {
      msgDiv.innerHTML = `
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-[#123824] to-[#d4af37] border border-[#d4af37]/60 flex items-center justify-center text-xs shrink-0 shadow-md">
          🩺
        </div>
        <div class="max-w-[88%] sm:max-w-[80%] bg-[#151922] border border-[#d4af37]/40 text-gray-200 text-xs sm:text-sm p-4 rounded-2xl rounded-tl-none shadow-xl space-y-2 leading-relaxed">
          <div class="flex items-center justify-between border-b border-white/10 pb-1.5">
            <span class="font-serif font-bold text-amber-300 text-xs sm:text-sm">Dr. Kuroki</span>
            <span class="text-[10px] text-gray-400 font-mono">Just Now</span>
          </div>
          ${htmlContent}
        </div>
      `;
    }

    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  function appendTypingIndicator() {
    const id = 'typing_' + Date.now();
    const div = document.createElement('div');
    div.id = id;
    div.className = 'flex gap-2.5 sm:gap-3 justify-start items-start animate-pulse';
    div.innerHTML = `
      <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-[#123824] to-[#d4af37] border border-[#d4af37]/60 flex items-center justify-center text-xs shrink-0 shadow-md">
        🩺
      </div>
      <div class="bg-[#151922] border border-white/10 text-amber-300 text-xs px-4 py-3 rounded-2xl rounded-tl-none flex items-center gap-2">
        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-bounce"></span>
        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-bounce [animation-delay:0.2s]"></span>
        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-bounce [animation-delay:0.4s]"></span>
        <span class="text-[11px] text-gray-300 ml-1">Dr. Kuroki is formulating trichology advice...</span>
      </div>
    `;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
    return id;
  }

  function removeTypingIndicator(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
  }

  // Form Submit Listener
  chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const query = chatInput.value.trim();
    if (!query) return;

    appendMessage('user', query);
    chatInput.value = '';

    const typingId = appendTypingIndicator();

    setTimeout(() => {
      removeTypingIndicator(typingId);
      const responseHtml = getDoctorResponse(query);
      appendMessage('bot', responseHtml);
    }, 900);
  });
}

/* 👥 Ultra-Realistic Live Shopper Counter & Traffic Pulse Engine */
function initLiveShopperCounter() {
  const counterEls = document.querySelectorAll('.js-live-counter, .js-live-visitors');
  if (!counterEls.length) return;

  let count = Math.floor(Math.random() * (885 - 865 + 1)) + 865;
  counterEls.forEach(el => { el.textContent = count; });

  function tick() {
    // Natural human traffic variation
    const change = (Math.random() > 0.45 ? 1 : -1) * (Math.floor(Math.random() * 3) + 1);
    count = Math.max(835, Math.min(925, count + change));

    counterEls.forEach(el => {
      el.style.opacity = '0.5';
      el.style.transform = 'scale(1.1)';
      setTimeout(() => {
        el.textContent = count;
        el.style.opacity = '1';
        el.style.transform = 'scale(1)';
      }, 150);
    });

    // Random natural interval between 2.5s and 5s
    const nextInterval = Math.floor(Math.random() * 2500) + 2500;
    setTimeout(tick, nextInterval);
  }

  setTimeout(tick, 3000);
}

// Master DOM Ready Initializer
document.addEventListener('DOMContentLoaded', function() {
  try { initLiveShopperCounter(); } catch(e) {}
  try { initShowerTimer(); } catch(e) {}
  try { initStickyHeader(); } catch(e) {}
  try { initCartDrawer(); } catch(e) {}
  try { initBeforeAfterSlider(); } catch(e) {}
  try { initIngredientFilters(); } catch(e) {}
  try { initAIConsultantChat(); } catch(e) {}
});

/* 📦 Quick Order Modal Global Controls */
function openQuickOrderModal() {
  const modal = document.getElementById('QuickOrderModal');
  if (modal) {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  } else {
    window.location.href = 'product.html';
  }
}

function closeQuickOrderModal() {
  const modal = document.getElementById('QuickOrderModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }
}

window.openQuickOrderModal = openQuickOrderModal;
window.closeQuickOrderModal = closeQuickOrderModal;



/* 📱 Mobile Simulator Page Switcher Helper */
function switchToSimPage(page) {
  const iframe = document.getElementById('SimulatedIframe');
  const selector = document.getElementById('PageSelector');
  if (iframe) {
    iframe.src = page + '?v=' + Date.now();
  }
  if (selector) {
    selector.value = page;
  }
  const tabHome = document.getElementById('TabHome');
  const tabProd = document.getElementById('TabProduct');
  if (tabHome && tabProd) {
    if (page === 'index.html') {
      tabHome.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-[#d4af37] text-black shadow';
      tabProd.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
    } else if (page === 'product.html') {
      tabProd.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all bg-[#d4af37] text-black shadow';
      tabHome.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition-all text-gray-300 hover:text-white';
    }
  }
}

window.switchToSimPage = switchToSimPage;



/* ==========================================================================
   ⚡ MASTER 1-CLICK INSTANT ORDER & CHECKOUT ENGINE (100% WORKING EVERYWHERE)
   ========================================================================== */
(function() {
  'use strict';

  // Global pack state
  window.selectedPack = {
    qty: 1,
    price: 499,
    title: '1 Bottle (250ml) — 1 Month Supply',
    saveText: 'Save ₹500'
  };

  // Switch Pack Function on Product Page
  window.selectPack = function(qty, price, title, saveText) {
    window.selectedPack = { qty: qty, price: price, title: title, saveText: saveText };
    
    // Update main order button price
    const mainBtnText = document.getElementById('MainOrderButtonPrice');
    if (mainBtnText) {
      mainBtnText.textContent = '₹' + price;
    }
    const stickyBtnText = document.getElementById('StickyBarPrice');
    if (stickyBtnText) {
      stickyBtnText.textContent = '₹' + price;
    }

    // Update modal if open
    const modalPrice = document.getElementById('OrderModalPriceDisplay');
    if (modalPrice) {
      modalPrice.textContent = '₹' + price;
    }
  };

  // Open Quick Order Modal
  window.openQuickOrderModal = function(customPrice, customTitle) {
    const isProductPage = window.location.pathname.endsWith('product.html') || window.location.pathname.endsWith('product');
    
    // If not on product.html, direct straight to product page!
    if (!isProductPage) {
      window.location.href = 'product.html';
      return;
    }

    // If on product page, open 1-Click Instant Checkout Modal
    let price = customPrice || (window.selectedPack ? window.selectedPack.price : 499);
    const modal = document.getElementById('QuickOrderModal');
    if (modal) {
      const priceDisplay = document.getElementById('OrderModalPriceDisplay');
      if (priceDisplay) priceDisplay.textContent = '₹' + price;
      
      const form = document.getElementById('QuickOrderForm');
      const success = document.getElementById('QuickOrderSuccess');
      if (form) form.classList.remove('hidden');
      if (success) success.classList.add('hidden');

      modal.classList.remove('hidden');
      modal.classList.add('flex');
      document.body.style.overflow = 'hidden';
    }
  };

  // Close Quick Order Modal
  window.closeQuickOrderModal = function() {
    const modal = document.getElementById('QuickOrderModal');
    if (modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      document.body.style.overflow = '';
    }
  };

  // Form submission handler & Abandoned Checkout Capture
  function initOrderForm() {
    const form = document.getElementById('QuickOrderForm');
    if (form) {
      // 1. Abandoned Checkout Lead Capture on Phone Input
      const phoneInput = form.querySelector('input[type="tel"]') || form.querySelectorAll('input')[1];
      const nameInput = form.querySelector('input[type="text"]') || form.querySelectorAll('input')[0];

      if (phoneInput) {
        let lastCapturedPhone = '';
        function checkAndCaptureLead() {
          const rawPhone = phoneInput.value.replace(/[^0-9]/g, '');
          if (rawPhone.length >= 10 && rawPhone !== lastCapturedPhone) {
            lastCapturedPhone = rawPhone;
            const price = window.selectedPack ? window.selectedPack.price : 499;
            const bundleName = window.selectedPack ? window.selectedPack.name : '1 Bottle (250ml)';
            
            const abPayload = {
              name: nameInput ? nameInput.value.trim() : 'Visitor',
              phone: rawPhone,
              bundle: bundleName,
              price: price
            };
            // Try Vercel Serverless then Hostinger
            fetch('api/abandoned', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(abPayload)
            }).catch(function() {
              fetch('api/abandoned.php', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(abPayload)
              }).catch(function() {});
            });

            // Local cache for immediate admin view
            try {
              let cur = JSON.parse(localStorage.getItem('br_abandoned_leads') || '[]');
              cur.unshift(abPayload);
              localStorage.setItem('br_abandoned_leads', JSON.stringify(cur.slice(0, 50)));
            } catch(e) {}
          }
        }

        phoneInput.addEventListener('blur', checkAndCaptureLead);
        phoneInput.addEventListener('input', function() {
          if (phoneInput.value.replace(/[^0-9]/g, '').length === 10) {
            checkAndCaptureLead();
          }
        });
      }

      // 2. Full Order Submission Handler
      form.onsubmit = async function(e) {
        e.preventDefault();
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Confirm Order';

        const allInputs = form.querySelectorAll('input, textarea');
        let orderPayload = {
          name: allInputs[0] ? allInputs[0].value.trim() : '',
          phone: allInputs[1] ? allInputs[1].value.trim() : '',
          pincode: allInputs[2] ? allInputs[2].value.trim() : '',
          city: allInputs[3] ? allInputs[3].value.trim() : '',
          address: allInputs[4] ? allInputs[4].value.trim() : '',
          bundle: window.selectedPack ? window.selectedPack.name : '1 Bottle (250ml)',
          price: window.selectedPack ? window.selectedPack.price : 499,
          payment_method: 'COD'
        };

        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.innerHTML = '<span>⏳ Confirming Logistics Order...</span>';
        }

        let orderData = null;
        const endpoints = ['api/order', 'api/order.js', 'api/order.php'];
        for (let ep of endpoints) {
          try {
            let res = await fetch(ep, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(orderPayload)
            });
            if (res.ok) {
              orderData = await res.json();
              if (orderData && orderData.success) break;
            }
          } catch(err) {}
        }

        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnText;
        }

        const orderId = (orderData && orderData.order_id) ? orderData.order_id : ('#BR-' + Math.floor(1000 + Math.random() * 9000));
        orderPayload.order_id = orderId;
        orderPayload.status = 'New';
        orderPayload.created_at = new Date().toLocaleString();

        // Local cache for immediate admin view
        try {
          let curOrders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
          curOrders.unshift(orderPayload);
          localStorage.setItem('br_local_orders', JSON.stringify(curOrders.slice(0, 100)));
        } catch(e) {}

          // Hide form, show success screen
          form.classList.add('hidden');
          const success = document.getElementById('QuickOrderSuccess');
          if (success) {
            success.classList.remove('hidden');
            const idDisplay = success.querySelector('strong');
            if (idDisplay) idDisplay.textContent = orderId;

            // Track Meta Pixel & GA4 Purchase Event
            if (window.trackD2CEvent) {
              window.trackD2CEvent('Purchase', {
                value: orderPayload.price,
                currency: 'INR',
                order_id: orderId,
                items: [{ item_name: 'BlackRoots Herbal Hair Dye Shampoo', price: orderPayload.price, quantity: 1 }]
              });
            }

            // Update Track Order link in success box if present
            const trackBtn = success.querySelector('a.js-track-live') || success.querySelector('button');
            if (trackBtn) {
              trackBtn.onclick = function() {
                window.location.href = 'track-order.html?id=' + encodeURIComponent(orderId);
              };
            }
          }

          if (navigator.vibrate) navigator.vibrate([100, 50, 100]);
        })
        .catch(function() {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
          }

          const orderId = '#BR-' + Math.floor(1000 + Math.random() * 9000);
          form.classList.add('hidden');
          const success = document.getElementById('QuickOrderSuccess');
          if (success) {
            success.classList.remove('hidden');
            const idDisplay = success.querySelector('strong');
            if (idDisplay) idDisplay.textContent = orderId;
          }
        });
      };
    }
  }

  // Global Click Delegator for any Order / Buy Now Button across all pages
  document.addEventListener('click', function(e) {
    const target = e.target.closest('.js-trigger-order, button:not([onclick]):not([type="submit"]), a[href="product.html"]');
    if (target) {
      const text = target.textContent.toLowerCase();
      if (text.includes('buy') || text.includes('order') || text.includes('claim') || target.classList.contains('js-trigger-order')) {
        // If modal exists on this page, open it directly!
        const modal = document.getElementById('QuickOrderModal');
        if (modal && !window.location.pathname.endsWith('product.html')) {
          e.preventDefault();
          window.openQuickOrderModal();
        } else if (modal && window.location.pathname.endsWith('product.html')) {
          e.preventDefault();
          window.openQuickOrderModal();
        }
      }
    }
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initOrderForm);
  } else {
    initOrderForm();
  }
})();



/* ==========================================================================
   🌿 INGREDIENTS PAGE INTERACTIVE FILTER & DETAIL MODAL ENGINE
   ========================================================================== */
function initIngredientFilters() {
  const filterBtns = document.querySelectorAll('.js-ingredient-filter');
  const cards = document.querySelectorAll('.js-ingredient-card');

  if (filterBtns.length === 0 || cards.length === 0) return;

  filterBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      const category = btn.getAttribute('data-category');

      // Update button active styles
      filterBtns.forEach(function(b) {
        if (b === btn) {
          b.className = 'js-ingredient-filter px-5 py-2.5 rounded-full bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black text-xs font-black uppercase tracking-wider shadow-xl transform scale-105 transition-all cursor-pointer';
        } else {
          b.className = 'js-ingredient-filter px-5 py-2.5 rounded-full bg-white/5 text-gray-300 hover:text-white text-xs font-bold uppercase tracking-wider border border-white/10 transition-all cursor-pointer';
        }
      });

      // Filter cards with smooth fade
      cards.forEach(function(card) {
        const cardCat = card.getAttribute('data-category');
        if (category === 'all' || cardCat === category) {
          card.style.display = 'block';
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(function() {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 30);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

function openIngredientDetail(title, desc, benefit) {
  const modal = document.getElementById('IngredientModal');
  const titleEl = document.getElementById('IngredientModalTitle');
  const descEl = document.getElementById('IngredientModalDesc');
  const benefitEl = document.getElementById('IngredientModalBenefit');

  if (titleEl) titleEl.textContent = title;
  if (descEl) descEl.textContent = desc;
  if (benefitEl) benefitEl.textContent = benefit;

  if (modal) {
    modal.classList.remove('hidden');
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

function closeIngredientModal() {
  const modal = document.getElementById('IngredientModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.style.display = 'none';
    document.body.style.overflow = '';
  }
}

window.initIngredientFilters = initIngredientFilters;
window.openIngredientDetail = openIngredientDetail;
window.closeIngredientModal = closeIngredientModal;

/* ==========================================================================
   🔬 ULTRA-LUXURY INTERACTIVE HAIR RESULT TIMELINE CALCULATOR ENGINE
   ========================================================================== */
(function() {
  let currentAge = 'mid';
  let currentGrey = 'moderate';

  const ageLabels = {
    young: '18 – 35 Years',
    mid: '36 – 50 Years',
    senior: '50+ Years'
  };

  const greyLabels = {
    light: '10% – 35% Greys',
    moderate: '35% – 65% Greys',
    heavy: '65%+ Full Greys'
  };

  const timelineData = {
    'young_light': {
      days: '5 – 7 Days',
      heading: 'Superfast Natural Melanin Activation in 5–7 Days!',
      desc: 'Younger hair follicles with initial roots react rapidly to Japanese Indigo & Amla. First 2-3 regular washes me hi grey roots completely naturally dark ho jayengi.'
    },
    'young_moderate': {
      days: '7 – 10 Days',
      heading: 'Visible Deep Dark Blackening in 7–10 Days!',
      desc: 'Aapki age aur moderate grey intensity ke liye BlackRoots ka botanical melanin stimulator 1 week ke regular shower washes me roots ko natural deep black shade provide karega.'
    },
    'young_heavy': {
      days: '10 – 14 Days',
      heading: 'Root Rejuvenation in 10–14 Days!',
      desc: 'Japanese Indigo aur Bhringraj extract pure hair shaft ko nourish karke heavy grey strands ko 10-14 days me rich black color me restore karenge.'
    },
    'mid_light': {
      days: '7 – 10 Days',
      heading: 'First Visible Dark Shade in 7–10 Days!',
      desc: 'Mid-stage roots ke liye Japanese Indigo Leaf aur Amla natural melanin production boost karte hain. Hafte me 2-3 washes ke sath roots natural black ho jati hain.'
    },
    'mid_moderate': {
      days: '10 – 14 Days',
      heading: 'Natural Deep Dark Transformation in 10–14 Days!',
      desc: 'Moderate scattered greys ke liye BlackRoots 250ml Bottle perfect hai. Regular shower washes ke sath 10-14 days me grey hair naturally black shine me convert honge.'
    },
    'mid_heavy': {
      days: '14 – 18 Days',
      heading: 'Complete Melanin Restoration in 14–18 Days!',
      desc: 'Deeper greys ke liye Japanese Indigo aur Brahmi deep cortex tak penetrate karte hain. 2 weeks ke regular use se natural uniform dark black shade achieve hota hai.'
    },
    'senior_light': {
      days: '10 – 14 Days',
      heading: 'Healthy Dark Roots in 10–14 Days!',
      desc: 'Mature hair roots ko Amla aur Camellia Oil se deep moisture aur Indigo se natural dark pigment milta hai. 10-14 days me noticeable blackening milti hai.'
    },
    'senior_moderate': {
      days: '14 – 18 Days',
      heading: 'Natural Rejuvenation in 14–18 Days!',
      desc: '50+ age me mature grey hair ko without ammonia safe blackening milti hai. 2-3 weeks me grey hair completely soft, shiny aur dark black ho jate hain.'
    },
    'senior_heavy': {
      days: '18 – 24 Days',
      heading: 'Full Ayurvedic Dark Transformation in 18–24 Days!',
      desc: 'Senior stage me full coverage ke liye 100% botanical nourishment zaroori hoti hai. Consistent 3-4 weeks regular shower washes se deep natural black color establish hota hai.'
    }
  };

  function updateCalculatorDisplay() {
    const key = `${currentAge}_${currentGrey}`;
    const data = timelineData[key] || timelineData['mid_moderate'];

    const daysBadge = document.getElementById('CalcResultDaysBadge');
    const heading = document.getElementById('CalcResultHeading');
    const desc = document.getElementById('CalcResultDesc');
    const ageLabel = document.getElementById('SelectedAgeLabel');
    const greyLabel = document.getElementById('SelectedGreyLabel');
    const outputBox = document.getElementById('CalcResultOutput');
    const simpleBadge = document.getElementById('SimpleDaysBadge');
    const simpleText = document.getElementById('SimpleResultText');

    if (daysBadge) daysBadge.textContent = data.days;
    if (heading) heading.textContent = data.heading;
    if (desc) desc.textContent = data.desc;
    if (ageLabel) ageLabel.textContent = ageLabels[currentAge] || '';
    if (greyLabel) greyLabel.textContent = greyLabels[currentGrey] || '';
    if (simpleBadge) simpleBadge.textContent = data.days;
    if (simpleText) simpleText.textContent = data.heading;

    if (outputBox) {
      if (outputBox.classList && outputBox.classList.remove) outputBox.classList.remove('hidden');
      outputBox.style.display = 'block';
    }
  }

  window.selectAgeGroup = function(age) {
    currentAge = age;
    updateCalculatorDisplay();
  };

  window.selectGreyPercentage = function(grey) {
    currentGrey = grey;
    updateCalculatorDisplay();
  };

  window.pickAge = window.selectAgeGroup;
  window.pickGrey = window.selectGreyPercentage;

  window.calculateHairResultTimeline = function(isExplicit) {
    updateCalculatorDisplay();
    const outputBox = document.getElementById('CalcResultOutput');
    if (outputBox && outputBox.scrollIntoView && isExplicit) {
      outputBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  };

  function setupCalculatorEventListeners() {
    // Age button clicks
    document.querySelectorAll('.js-calc-age-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.js-calc-age-btn').forEach(b => {
          b.className = 'js-calc-age-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer';
          const title = b.querySelector('.text-xs');
          const sub = b.querySelector('.text-\\[9px\\]');
          if (title) title.className = 'text-xs font-bold text-white block';
          if (sub) sub.className = 'text-[9px] text-gray-400 uppercase tracking-tight block mt-0.5';
        });

        btn.className = 'js-calc-age-btn active-calc-btn p-3 sm:p-4 rounded-2xl bg-gradient-to-r from-[#d4af37]/20 to-[#aa7c11]/10 border-2 border-[#d4af37] text-center shadow-lg transition-all cursor-pointer';
        const title = btn.querySelector('.text-xs');
        const sub = btn.querySelector('.text-\\[9px\\]');
        if (title) title.className = 'text-xs font-bold text-amber-300 block';
        if (sub) sub.className = 'text-[9px] text-amber-200 uppercase tracking-tight block mt-0.5';

        currentAge = btn.getAttribute('data-age') || 'mid';
        updateCalculatorDisplay();
      });
    });

    // Grey intensity button clicks
    document.querySelectorAll('.js-calc-grey-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.js-calc-grey-btn').forEach(b => {
          b.className = 'js-calc-grey-btn p-3 sm:p-4 rounded-2xl bg-white/5 border border-white/10 text-center hover:border-[#d4af37]/60 transition-all cursor-pointer';
          const title = b.querySelector('.text-xs');
          const sub = b.querySelector('.text-\\[9px\\]');
          if (title) title.className = 'text-xs font-black text-white block mb-0.5';
          if (sub) sub.className = 'text-[9px] text-gray-400 uppercase tracking-tight block';
        });

        btn.className = 'js-calc-grey-btn active-calc-btn p-3 sm:p-4 rounded-2xl bg-gradient-to-r from-[#d4af37]/20 to-[#aa7c11]/10 border-2 border-[#d4af37] text-center shadow-lg transition-all cursor-pointer';
        const title = btn.querySelector('.text-xs');
        const sub = btn.querySelector('.text-\\[9px\\]');
        if (title) title.className = 'text-xs font-black text-amber-300 block mb-0.5';
        if (sub) sub.className = 'text-[9px] text-amber-200 uppercase tracking-tight block';

        currentGrey = btn.getAttribute('data-grey') || 'moderate';
        updateCalculatorDisplay();
      });
    });

    // Calculate CTA button click
    const calcBtn = document.getElementById('BtnRunHairCalculator');
    if (calcBtn) {
      calcBtn.addEventListener('click', (e) => {
        e.preventDefault();
        window.calculateHairResultTimeline(true);
      });
    }
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', setupCalculatorEventListeners);
    } else {
      setupCalculatorEventListeners();
    }
  }
})();

