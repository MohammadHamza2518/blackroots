import os
import re

theme_js_path = r"c:\Users\moham\Downloads\blackroots website\assets\theme.js"

ai_engine_code = """/* 🩺 Dr. Kuroki — Chief AI Trichologist Clinical Response Engine */
function initAIConsultantChat() {
  const chatForm = document.getElementById('AIChatForm');
  const chatInput = document.getElementById('AIChatInput');
  const chatBox = document.getElementById('AIChatMessages');
  const promptPills = document.querySelectorAll('.js-ai-prompt-pill');

  if (!chatForm || !chatInput || !chatBox) return;

  // Quick Prompt Pills Click Handler
  promptPills.forEach(pill => {
    pill.addEventListener('click', () => {
      chatInput.value = pill.textContent.replace(/^[^\w]+/, '').trim();
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
              🚿 View Live 3-Min Scalp Timer &rarr;
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
              🧔 Get Beard & Scalp Care (₹499) &rarr;
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
              🌿 Explore Herbal Ingredients &rarr;
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
              🛍️ Order Now — ₹499 (Free COD) &rarr;
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
              ✨ Stop Hair Fall — Order ₹499 &rarr;
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
            🛍️ Buy BlackRoots (₹499) &rarr;
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
"""

with open(theme_js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Replace the existing initAIConsultantChat or append it
if 'function initAIConsultantChat()' in js_content:
    # Replace from function initAIConsultantChat() to the next top level function or end
    pattern = r'function initAIConsultantChat\(\)\s*\{.*?(?=\n\/\*|\nfunction |\Z)'
    js_content = re.sub(pattern, ai_engine_code + "\n", js_content, flags=re.DOTALL)
else:
    js_content += "\n" + ai_engine_code

with open(theme_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Upgraded initAIConsultantChat in assets/theme.js successfully!")
