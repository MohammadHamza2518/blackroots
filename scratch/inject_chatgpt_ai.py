import os
import re

chatgpt_ai_script = """  <script>
    // 🩺 Ultra-Intelligent ChatGPT-Grade Dr. Kuroki AI Trichologist Engine
    document.addEventListener('DOMContentLoaded', function() {
      const chatForm = document.getElementById('AIChatForm');
      const chatInput = document.getElementById('AIChatInput');
      const chatBox = document.getElementById('AIChatMessages');
      const promptPills = document.querySelectorAll('.js-ai-prompt-pill');

      if (!chatForm || !chatInput || !chatBox) {
        console.warn('AI Chat elements not found');
        return;
      }

      // Quick Prompt Pills Click Handler
      promptPills.forEach(pill => {
        pill.addEventListener('click', function(e) {
          e.preventDefault();
          const cleanText = this.textContent.replace(/^[^\w\u0900-\u097F]+/, '').trim();
          chatInput.value = cleanText;
          sendMessage(cleanText);
        });
      });

      // Comprehensive Clinical Trichology Knowledge Base (ChatGPT Style)
      function getDoctorResponse(query) {
        const q = query.toLowerCase();

        if (q.includes('grey') || q.includes('gray') || q.includes('safed') || q.includes('white') || q.includes('revers') || q.includes('black') || q.includes('kala')) {
          return {
            title: "Melanin Reactivation & Botanical Color Locking",
            points: [
              "<strong>Root Cause:</strong> Hair turns grey when hair bulb melanocytes stop producing melanin due to oxidative stress and toxic chemical dyes.",
              "<strong>BlackRoots Mechanism:</strong> Uses <em>Polygonum Multiflorum (He Shou Wu)</em> and <em>Black Sesame Extract</em> to deposit rich botanical dark pigments directly into the hair cuticle within 3 minutes.",
              "<strong>Long-Term Benefit:</strong> 100% Ammonia & PPD free. Does not damage natural hair texture and keeps roots nourished."
            ],
            tip: "💡 Visible darkening starts from the 2nd to 3rd wash. Use 2-3 times weekly for full coverage.",
            ctaText: "🛍️ Order BlackRoots 250ml — ₹499 (Free COD)",
            ctaLink: "product.html"
          };
        }

        if (q.includes('3 min') || q.includes('time') || q.includes('how to use') || q.includes('routine') || q.includes('ritual') || q.includes('kaise use') || q.includes('tarika') || q.includes('lagaye')) {
          return {
            title: "Dr. Kuroki's 3-Minute Shower Ritual Guide",
            points: [
              "<strong>Step 1 (Wet Hair):</strong> Rinse your scalp or beard thoroughly with lukewarm water in the morning shower.",
              "<strong>Step 2 (3-Min Massage):</strong> Pump 2-3 coin-sized pumps onto wet palms and massage gently into scalp roots and grey hair for 3 full minutes.",
              "<strong>Step 3 (Rinse Clean):</strong> Rinse completely with fresh water. No extra conditioner or harsh chemical shampoo needed!"
            ],
            tip: "⏱️ Just 3 minutes in your regular morning bath — no gloves, no mess, no waiting around!",
            ctaText: "🚿 View Live 3-Min Scalp Timer",
            ctaLink: "how-to-use.html"
          };
        }

        if (q.includes('beard') || q.includes('darhi') || q.includes('face') || q.includes('skin') || q.includes('chehra') || q.includes('mustache') || q.includes('mooch')) {
          return {
            title: "Dermatological Safety for Beard & Mustache",
            points: [
              "<strong>100% Skin Safe:</strong> Formulated without ammonia, resorcinol, or hydrogen peroxide, making it completely non-irritating for facial skin.",
              "<strong>No Skin Stains:</strong> Unlike chemical dye pastes that leave dark stubborn stains on the jawline, BlackRoots washes off clean from skin.",
              "<strong>Beard Softening:</strong> Infused with Argan Oil & Ginseng to soften coarse beard bristles and prevent beard dandruff."
            ],
            tip: "🧔 Apply on damp beard, massage for 3 minutes during shower, and rinse clean.",
            ctaText: "🧔 Get Beard & Scalp Care — ₹499",
            ctaLink: "product.html"
          };
        }

        if (q.includes('ammonia') || q.includes('ppd') || q.includes('safe') || q.includes('side effect') || q.includes('chemical') || q.includes('nuksan') || q.includes('allergy') || q.includes('harm')) {
          return {
            title: "Zero-Chemical Safety & Purity Certification",
            points: [
              "<strong>Certified Free Of:</strong> Ammonia, PPD, Resorcinol, Sulfates, and Parabens.",
              "<strong>Scalp Gentle:</strong> Zero burning, zero tingling, and zero scalp irritation.",
              "<strong>Active Herbs:</strong> Enriched with Reishi Mushroom, Biotin, Ginger Root, and Black Sesame."
            ],
            tip: "🛡️ 100% safe for long-term weekly maintenance for both men and women.",
            ctaText: "🌿 View Herbal Ingredients Details",
            ctaLink: "ingredients.html"
          };
        }

        if (q.includes('price') || q.includes('cost') || q.includes('cod') || q.includes('delivery') || q.includes('order') || q.includes('buy') || q.includes('kitna') || q.includes('paisa') || q.includes('rupaye') || q.includes('offer')) {
          return {
            title: "Official Pricing & Express Delivery Information",
            points: [
              "<strong>Special Special:</strong> <strong class='text-amber-300 font-bold'>₹499 Only</strong> (Flat 50% Off Verified Deal).",
              "<strong>Bottle Size:</strong> 250ml Luxury Pump Bottle — provides 25 to 30 shower washes (lasts 2 to 3 months).",
              "<strong>Free Express Delivery:</strong> Dispatched in 24h via Delhivery/BlueDart across 19,000+ Indian Pincodes with Cash on Delivery (COD) available."
            ],
            tip: "⚡ Free Express COD Delivery across India with zero hidden shipping charges.",
            ctaText: "🛍️ Buy BlackRoots Now — ₹499 Only",
            ctaLink: "product.html"
          };
        }

        if (q.includes('fall') || q.includes('jharna') || q.includes('dandruff') || q.includes('rusi') || q.includes('growth') || q.includes('loss') || q.includes('patle')) {
          return {
            title: "Follicle Strengthening & Anti-Dandruff Protocol",
            points: [
              "<strong>Pure Ginger Root:</strong> Boosts micro-circulation in scalp capillaries, waking up dormant hair follicles.",
              "<strong>Biotin & Reishi Mushroom:</strong> Fortifies hair cortex from within, reducing shower hair fall by up to 85%.",
              "<strong>Herbal Saponins:</strong> Cleanses microbial scalp buildup and clears dandruff without drying hair."
            ],
            tip: "✨ Stronger, thicker roots with zero flaky scalp from the first week of use.",
            ctaText: "✨ Stop Hair Fall — Order ₹499",
            ctaLink: "product.html"
          };
        }

        // Default Intelligent Conversational Trichology Response
        return {
          title: `Clinical Trichology Analysis for "${query}"`,
          points: [
            "<strong>Herbal Approach:</strong> BlackRoots combines ancient Japanese botanical alchemy with modern trichology to restore natural hair vitality.",
            "<strong>Multi-Action Formula:</strong> Simultaneously targets grey hair reduction, root strengthening, and gentle cleansing in just 3 minutes.",
            "<strong>Zero Chemical Rebound:</strong> Free of ammonia and harsh salts, keeping your hair silky, soft, and naturally dark."
          ],
          tip: "💡 Regular 2-3 weekly washes keep roots nourished and dark hair rich and vibrant.",
          ctaText: "🛍️ Order BlackRoots 250ml — ₹499",
          ctaLink: "product.html"
        };
      }

      function appendUserMessage(text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'flex gap-2.5 sm:gap-3 justify-end items-start animate-fadeIn';
        msgDiv.innerHTML = `
          <div class="max-w-[85%] sm:max-w-[75%] bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#d4af37] text-black font-semibold text-xs sm:text-sm p-3.5 rounded-2xl rounded-tr-none shadow-lg leading-relaxed break-words">
            ${text}
          </div>
          <div class="w-8 h-8 rounded-full bg-white/20 border border-white/30 flex items-center justify-center text-xs text-white shrink-0 shadow-md font-bold">
            👤
          </div>
        `;
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
          <div class="bg-[#151922] border border-white/15 text-amber-300 text-xs px-4 py-3 rounded-2xl rounded-tl-none flex items-center gap-2 shadow-lg">
            <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-bounce"></span>
            <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-bounce [animation-delay:0.2s]"></span>
            <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-bounce [animation-delay:0.4s]"></span>
            <span class="text-[11px] text-gray-300 ml-1.5 font-mono">Dr. Kuroki is formulating clinical advice...</span>
          </div>
        `;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
        return id;
      }

      // ChatGPT Streaming Typewriter Response Renderer
      function streamDoctorResponse(resData) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'flex gap-2.5 sm:gap-3 justify-start items-start animate-fadeIn';
        
        const contentId = 'doc_content_' + Date.now();
        msgDiv.innerHTML = `
          <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-[#123824] to-[#d4af37] border border-[#d4af37]/60 flex items-center justify-center text-xs shrink-0 shadow-md">
            🩺
          </div>
          <div class="max-w-[88%] sm:max-w-[80%] bg-[#151922] border border-[#d4af37]/45 text-gray-200 text-xs sm:text-sm p-4 rounded-2xl rounded-tl-none shadow-2xl space-y-2.5 leading-relaxed">
            <div class="flex items-center justify-between border-b border-white/10 pb-1.5">
              <div class="flex items-center gap-1.5">
                <span class="font-serif font-bold text-amber-300 text-xs sm:text-sm">Dr. Kuroki</span>
                <span class="text-[9px] bg-emerald-400/20 text-emerald-400 px-1 py-0.2 rounded border border-emerald-500/30 uppercase font-mono">Verified</span>
              </div>
              <span class="text-[10px] text-gray-400 font-mono">Just Now</span>
            </div>
            
            <div id="${contentId}" class="space-y-2">
              <h4 class="font-serif font-bold text-amber-200 text-sm sm:text-base">${resData.title}</h4>
              <ul class="list-disc pl-4 space-y-1.5 text-xs text-gray-300">
                ${resData.points.map(p => `<li>${p}</li>`).join('')}
              </ul>
              <p class="text-[11px] text-emerald-300 bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-500/30 font-medium">
                ${resData.tip}
              </p>
              <div class="pt-2">
                <a href="${resData.ctaLink}" class="inline-flex items-center gap-1.5 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs px-4 py-2.5 rounded-xl shadow-lg hover:scale-105 transition-all uppercase tracking-tight">
                  <span>${resData.ctaText}</span>
                  <span>&rarr;</span>
                </a>
              </div>
            </div>
          </div>
        `;

        chatBox.appendChild(msgDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
      }

      function sendMessage(query) {
        if (!query) return;

        appendUserMessage(query);
        chatInput.value = '';

        const typingId = appendTypingIndicator();

        // Realistic AI Response Delay (700ms) like ChatGPT
        setTimeout(() => {
          const typingEl = document.getElementById(typingId);
          if (typingEl) typingEl.remove();

          const resData = getDoctorResponse(query);
          streamDoctorResponse(resData);
        }, 700);
      }

      // Form Submit Handler
      chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const query = chatInput.value.trim();
        if (query) {
          sendMessage(query);
        }
      });
    });
  </script>
"""

root_dir = r"c:\Users\moham\Downloads\blackroots website"
ai_pages = [
    os.path.join(root_dir, "ai-consultant.html"),
    os.path.join(root_dir, "demo_lab", "ai-consultant.html"),
    os.path.join(root_dir, "preview", "ai-consultant.html")
]

for p in ai_pages:
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any existing AI script before body
    content = re.sub(r'<script>\s*\/\/\s*🩺 Ultra-Intelligent.*?<\/script>', '', content, flags=re.DOTALL)
    
    # Inject directly before </body>
    content = content.replace('</body>', chatgpt_ai_script + '\n</body>')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected ChatGPT-Grade AI Engine in", p)

