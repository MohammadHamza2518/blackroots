import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

ai_files = [
    os.path.join(root_dir, "ai-consultant.html"),
    os.path.join(root_dir, "demo_lab", "ai-consultant.html"),
    os.path.join(root_dir, "preview", "ai-consultant.html")
]

modern_chat_ui = """      <!-- Ultra-Luxury Apple-Grade Clinical AI Chat UI Window -->
      <div class="rounded-3xl bg-[#11141b] border border-[#d4af37]/60 shadow-[0_15px_50px_rgba(0,0,0,0.8)] overflow-hidden flex flex-col max-w-3xl mx-auto w-full">
        
        <!-- Chat Header -->
        <div class="bg-[#151922] px-4 py-3 sm:px-6 sm:py-3.5 border-b border-white/10 flex items-center justify-between gap-2 shrink-0">
          <div class="flex items-center gap-3 min-w-0">
            <div class="relative shrink-0">
              <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-[#123824] via-[#1a4a30] to-[#d4af37] border border-[#d4af37] flex items-center justify-center text-lg shadow-md">
                🩺
              </div>
              <span class="absolute bottom-0 right-0 w-2.5 h-2.5 bg-emerald-400 border-2 border-black rounded-full animate-pulse"></span>
            </div>
            <div class="min-w-0">
              <div class="flex items-center gap-1.5">
                <h3 class="font-serif font-bold text-white text-sm sm:text-base truncate">Dr. Kuroki</h3>
                <span class="text-[9px] bg-amber-400/15 text-amber-300 px-1.5 py-0.5 rounded border border-amber-400/30 font-bold uppercase shrink-0">AI Trichologist</span>
              </div>
              <span class="text-[10px] text-emerald-400 font-medium block truncate">● Online • Japanese Herbal Specialist</span>
            </div>
          </div>
          
          <a href="product.html" class="shrink-0 bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-[11px] px-3.5 py-2 rounded-xl shadow-lg hover:scale-105 transition-all flex items-center gap-1 uppercase tracking-tight">
            <span>Buy &#8377;499</span>
            <span>&rarr;</span>
          </a>
        </div>

        <!-- Chat Message History Window (Auto-Scroll, Mobile Perfect) -->
        <div id="AIChatMessages" class="p-3.5 sm:p-5 overflow-y-auto space-y-3.5 bg-[#0c0e14] h-[360px] sm:h-[440px] scroll-smooth">
          
          <!-- AI Initial Welcome Message Bubble -->
          <div class="flex gap-2.5 sm:gap-3 justify-start items-start">
            <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-[#123824] to-[#d4af37] border border-[#d4af37]/60 flex items-center justify-center text-xs shrink-0 shadow-md">
              🩺
            </div>
            <div class="max-w-[85%] sm:max-w-[80%] bg-[#151922] border border-[#d4af37]/40 text-gray-200 text-xs sm:text-sm p-4 rounded-2xl rounded-tl-none shadow-xl space-y-2.5">
              <div class="flex items-center justify-between border-b border-white/10 pb-1.5">
                <span class="font-serif font-bold text-amber-300 text-xs sm:text-sm">Dr. Kuroki</span>
                <span class="text-[10px] text-gray-400">Clinical Trichologist</span>
              </div>
              <p class="leading-relaxed font-light">
                Konnichiwa! I am <strong>Dr. Kuroki</strong>, BlackRoots Chief AI Trichologist. How can I assist your hair or beard journey today?
              </p>
              <p class="text-[11px] text-gray-300 bg-white/5 p-2 rounded-xl border border-white/10">
                💡 Ask me about <strong>Grey Hair Reversal</strong>, <strong>3-Min Shower Routine</strong>, <strong>Beard Care</strong>, or <strong>Hair Fall Reduction</strong>.
              </p>
            </div>
          </div>

        </div>

        <!-- Quick Prompt Pills (Horizontal Scrollable Strip) -->
        <div class="px-3 py-2 bg-[#12151c] border-t border-white/10 flex items-center gap-2 overflow-x-auto no-scrollbar scroll-smooth shrink-0">
          <span class="text-[10px] font-bold text-amber-400 uppercase tracking-wider shrink-0 flex items-center gap-1">
            ⚡ Quick:
          </span>
          <button type="button" class="js-ai-prompt-pill shrink-0 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-[#d4af37] hover:text-black border border-white/10 text-gray-200 text-[11px] font-medium transition-all cursor-pointer">
            🌿 How to stop grey hair?
          </button>
          <button type="button" class="js-ai-prompt-pill shrink-0 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-[#d4af37] hover:text-black border border-white/10 text-gray-200 text-[11px] font-medium transition-all cursor-pointer">
            ⏱️ How to use in 3 mins?
          </button>
          <button type="button" class="js-ai-prompt-pill shrink-0 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-[#d4af37] hover:text-black border border-white/10 text-gray-200 text-[11px] font-medium transition-all cursor-pointer">
            🧔 Is it safe for beard?
          </button>
          <button type="button" class="js-ai-prompt-pill shrink-0 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-[#d4af37] hover:text-black border border-white/10 text-gray-200 text-[11px] font-medium transition-all cursor-pointer">
            🛡️ Any Ammonia or PPD?
          </button>
          <button type="button" class="js-ai-prompt-pill shrink-0 px-3 py-1.5 rounded-xl bg-white/5 hover:bg-[#d4af37] hover:text-black border border-white/10 text-gray-200 text-[11px] font-medium transition-all cursor-pointer">
            🚚 Price & COD Delivery?
          </button>
        </div>

        <!-- Chat Input Form -->
        <form id="AIChatForm" class="p-3 sm:p-3.5 bg-[#151922] border-t border-white/10 flex items-center gap-2 shrink-0">
          <input id="AIChatInput" type="text" placeholder="Ask Dr. Kuroki anything about hair..." required autocomplete="off" class="flex-1 px-4 py-3 rounded-xl bg-black border border-white/15 text-xs sm:text-sm text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-all">
          <button type="submit" id="AIChatSubmitBtn" class="bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-extrabold text-xs sm:text-sm px-4 sm:px-6 py-3 rounded-xl shadow-lg hover:brightness-110 active:scale-95 transition-all flex items-center gap-1.5 shrink-0 uppercase tracking-wider cursor-pointer">
            <span>Send</span>
            <span>&rarr;</span>
          </button>
        </form>

      </div>"""

for fpath in ai_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Replace the chat container section
    pattern = r'<!-- Ultra-Luxury Apple-Grade Chat UI Window -->.*?<\/div>\s*<\/div>\s*<\/div>\s*<\/section>'
    new_content = re.sub(
        r'<!-- Ultra-Luxury Apple-Grade Chat UI Window -->.*?<\/form>\s*<\/div>',
        modern_chat_ui,
        new_content,
        flags=re.DOTALL
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated Chat UI in", fpath)

