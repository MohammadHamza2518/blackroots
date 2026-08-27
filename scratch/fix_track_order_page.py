import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

track_files = [
    os.path.join(root_dir, "track-order.html"),
    os.path.join(root_dir, "demo_lab", "track-order.html"),
    os.path.join(root_dir, "preview", "track-order.html")
]

modern_tracker_markup = """      <div class="p-5 sm:p-8 rounded-3xl bg-[#11141b] border border-[#d4af37]/60 shadow-[0_15px_50px_rgba(0,0,0,0.8)] text-left space-y-6 max-w-2xl mx-auto">
        
        <form id="OrderTrackerForm" class="space-y-4">
          <div>
            <label class="block text-xs font-bold text-amber-300 uppercase tracking-wider mb-1.5">
              Order ID / Tracking Number <span class="text-amber-400">*</span>
            </label>
            <input type="text" id="track-order-id" placeholder="e.g. #BR-1024 or 10-digit mobile" required class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-xs sm:text-sm text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-all">
          </div>

          <div>
            <label class="block text-xs font-bold text-amber-300 uppercase tracking-wider mb-1.5">
              Mobile Number or Email
            </label>
            <input type="text" id="track-contact" placeholder="e.g. 9876543210 or your email" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-xs sm:text-sm text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-all">
          </div>

          <button type="submit" id="track-submit-btn" class="w-full bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-xs sm:text-sm py-4 rounded-xl shadow-xl hover:brightness-110 active:scale-95 transition-all uppercase tracking-wider flex items-center justify-center gap-2 cursor-pointer">
            <span>🔥 Track Order Live Status</span>
            <span>&rarr;</span>
          </button>
        </form>

        <!-- Live Dynamic Tracking Result Container -->
        <div id="OrderTrackerResult" class="hidden pt-6 border-t border-white/10 space-y-6 animate-fadeIn">
          
          <!-- Status Banner -->
          <div class="p-4 rounded-2xl bg-gradient-to-r from-emerald-950/80 to-[#123824] border border-emerald-500/40 shadow-lg flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-emerald-400 text-lg font-bold shrink-0">
                🚚
              </div>
              <div>
                <div class="flex items-center gap-2">
                  <h4 class="text-sm font-bold text-white">Dispatched & In Transit</h4>
                  <span id="tracker-display-id" class="text-[10px] font-mono bg-amber-400/20 text-amber-300 px-1.5 py-0.5 rounded border border-amber-400/30">#BR-1024</span>
                </div>
                <p class="text-[11px] text-gray-300">Courier: <strong>Delhivery Express Air</strong> &bull; AWB: <span class="font-mono text-amber-300">8839201492</span></p>
              </div>
            </div>
            <div class="text-right sm:text-right shrink-0 bg-black/40 px-3 py-1.5 rounded-xl border border-white/10">
              <span class="text-[10px] text-gray-400 block uppercase">Est. Delivery</span>
              <span class="text-xs font-bold text-emerald-400">Within 48 Hours</span>
            </div>
          </div>

          <!-- Product Details Summary -->
          <div class="p-3.5 rounded-xl bg-white/5 border border-white/10 flex items-center justify-between text-xs">
            <div class="flex items-center gap-2.5">
              <img src="./assets/blackroots-bottles-trio.jpg" alt="Product" class="w-10 h-10 object-contain rounded-lg bg-black border border-white/10">
              <div>
                <span class="font-semibold text-white block">BlackRoots Herbal Shampoo (250ml)</span>
                <span class="text-[10px] text-gray-400">Qty: 1 &bull; Cash on Delivery (COD)</span>
              </div>
            </div>
            <span class="font-bold text-[#d4af37] text-sm">&#8377;499</span>
          </div>

          <!-- Vertical Timeline Steps -->
          <div class="space-y-5 relative pl-6 before:absolute before:left-2.5 before:top-2 before:bottom-2 before:w-0.5 before:bg-gradient-to-b before:from-emerald-500 before:via-[#d4af37] before:to-gray-700">
            
            <!-- Step 1: Confirmed -->
            <div class="relative flex items-start gap-3">
              <div class="absolute -left-6 top-0.5 w-5 h-5 rounded-full bg-emerald-500 text-black flex items-center justify-center font-bold text-[10px] shadow-md">
                ✓
              </div>
              <div class="space-y-0.5">
                <h5 class="text-xs font-bold text-white">Order Verified & Confirmed</h5>
                <p class="text-[11px] text-gray-400">Payment method: Cash on Delivery &bull; Order logged at Shuklaganj UP central server.</p>
              </div>
            </div>

            <!-- Step 2: Packed -->
            <div class="relative flex items-start gap-3">
              <div class="absolute -left-6 top-0.5 w-5 h-5 rounded-full bg-emerald-500 text-black flex items-center justify-center font-bold text-[10px] shadow-md">
                ✓
              </div>
              <div class="space-y-0.5">
                <h5 class="text-xs font-bold text-white">Packed & Quality Passed</h5>
                <p class="text-[11px] text-gray-400">Shuklaganj UP Central Warehouse &bull; Double tamper-proof bubble seal verified.</p>
              </div>
            </div>

            <!-- Step 3: In Transit (Active) -->
            <div class="relative flex items-start gap-3">
              <div class="absolute -left-6 top-0.5 w-5 h-5 rounded-full bg-[#d4af37] text-black flex items-center justify-center font-bold text-[10px] shadow-[0_0_12px_rgba(212,175,55,0.8)] animate-pulse">
                🚚
              </div>
              <div class="space-y-0.5">
                <h5 class="text-xs font-bold text-amber-300 flex items-center gap-1.5">
                  <span>In Transit to Your Nearest City Hub</span>
                  <span class="text-[9px] bg-amber-400/20 text-amber-300 px-1 py-0.2 rounded border border-amber-400/30 uppercase">LIVE</span>
                </h5>
                <p class="text-[11px] text-gray-300">Fast Air Cargo Express &bull; Package moving smoothly towards destination delivery center.</p>
              </div>
            </div>

            <!-- Step 4: Out for Delivery (Pending) -->
            <div class="relative flex items-start gap-3 opacity-60">
              <div class="absolute -left-6 top-0.5 w-5 h-5 rounded-full bg-black border-2 border-gray-600 flex items-center justify-center font-bold text-[8px] text-gray-400">
                📍
              </div>
              <div class="space-y-0.5">
                <h5 class="text-xs font-medium text-gray-400">Out for Doorstep Delivery</h5>
                <p class="text-[11px] text-gray-500">Delivery executive will call your mobile before arriving with your parcel.</p>
              </div>
            </div>

          </div>

          <!-- WhatsApp Support Bar -->
          <div class="pt-4 border-t border-white/10 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
            <span class="text-gray-400 text-[11px]">Need urgent delivery help?</span>
            <a href="https://wa.me/919580835179?text=Hello%20BlackRoots%20Team%2C%20I%20want%20to%20check%20my%20Order%20Status" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/30 text-emerald-400 px-4 py-2 rounded-xl font-bold transition-all">
              <span>💬 WhatsApp Support: +91 9580835179</span>
            </a>
          </div>

        </div>

      </div>"""

tracking_script = """  <script>
    // 🚚 Live Order Tracker Interactive Logic
    document.addEventListener('DOMContentLoaded', function() {
      const trackForm = document.getElementById('OrderTrackerForm');
      const orderInput = document.getElementById('track-order-id');
      const contactInput = document.getElementById('track-contact');
      const submitBtn = document.getElementById('track-submit-btn');
      const resultBox = document.getElementById('OrderTrackerResult');
      const displayId = document.getElementById('tracker-display-id');

      if (!trackForm || !orderInput || !resultBox) return;

      // Check URL parameters (e.g. ?order_id=BR-1025)
      const urlParams = new URLSearchParams(window.location.search);
      const paramOrderId = urlParams.get('order_id') || urlParams.get('id');
      if (paramOrderId) {
        orderInput.value = paramOrderId;
        setTimeout(() => {
          trackForm.dispatchEvent(new Event('submit'));
        }, 300);
      }

      trackForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const enteredId = orderInput.value.trim();
        if (!enteredId) return;

        // Button Loading State
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>⏳ Fetching Live Logistics Status...</span>';

        setTimeout(() => {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<span>🔥 Track Order Live Status</span> <span>&rarr;</span>';
          
          let formattedId = enteredId.toUpperCase();
          if (!formattedId.startsWith('#') && !formattedId.startsWith('BR')) {
            formattedId = '#' + formattedId;
          }
          if (displayId) displayId.textContent = formattedId;

          resultBox.classList.remove('hidden');
          resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 500);
      });
    });
  </script>
"""

for fpath in track_files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Replace tracker card section
    pattern = r'<div class="p-8 rounded-3xl glass-panel-luxury.*?<\/div>\s*<\/div>\s*<\/div>\s*<\/section>'
    new_content = re.sub(
        r'<div class="p-8 rounded-3xl glass-panel-luxury.*?<\/div>\s*<\/div>\s*<\/div>',
        modern_tracker_markup,
        new_content,
        flags=re.DOTALL
    )

    # Clean UTF-8 artifacts in modal if any
    new_content = new_content.replace('œ•', '✕').replace('œ“', '✓')

    # Remove any old tracker script before body
    new_content = re.sub(r'<script>\s*\/\/\s*🚚 Live Order Tracker.*?<\/script>', '', new_content, flags=re.DOTALL)
    new_content = new_content.replace('</body>', tracking_script + '\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated Track Order page in", fpath)

