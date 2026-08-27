import os
import re
import shutil

# 1. Update influencer.html to remove public register form and make it strict login only
with open('influencer.html', 'r', encoding='utf-8') as f:
    inf_html = f.read()

# Replace auth section with pure clean VIP Creator Login
auth_screen_pattern = r'<!-- ========================================================================= -->\s*<!-- 1\. AUTH SCREEN.*?<!-- ========================================================================= -->\s*<!-- 2\. MAIN CREATOR DASHBOARD APP -->'

new_auth_screen = """<!-- ========================================================================= -->
  <!-- 1. AUTH SCREEN (STRICT CREATOR LOGIN ONLY - ADMIN CONTROLLED) -->
  <!-- ========================================================================= -->
  <div id="InfluencerAuthScreen" class="fixed inset-0 z-50 bg-[#0a0b0e] flex items-center justify-center p-4 overflow-y-auto">
    <div class="w-full max-w-md my-auto p-6 sm:p-8 rounded-3xl bg-[#11141b] border border-[#d4af37]/40 shadow-[0_20px_60px_rgba(0,0,0,0.95)] text-center space-y-6">
      
      <!-- Logo Header -->
      <div class="flex flex-col items-center gap-2">
        <a href="./index.html" class="flex items-center gap-2 mb-1">
          <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo" class="w-14 h-14 rounded-full border-2 border-[#d4af37] shadow-xl">
        </a>
        <h1 class="font-serif text-2xl sm:text-3xl font-bold uppercase tracking-wider gold-gradient-text">BlackRoots VIP Creator</h1>
        <p class="text-xs text-amber-300/90 font-bold uppercase tracking-widest">Official Ambassador Portal</p>
      </div>

      <div class="p-3.5 rounded-2xl bg-black/50 border border-white/10 text-left space-y-1">
        <span class="text-[10px] text-amber-300 block font-bold uppercase tracking-wider">🔒 Private Creator Access</span>
        <p class="text-[11px] text-gray-300">Creator accounts are provisioned exclusively by BlackRoots Admin. Please enter your assigned User ID and Password below.</p>
      </div>

      <!-- Pure Creator Login Form -->
      <form id="InfluencerLoginForm" onsubmit="handleInfluencerLogin(event)" class="space-y-4 text-left">
        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">User ID / Promo Code / Phone</label>
          <input type="text" id="inf-login-id" required placeholder="Enter User ID (e.g. PRIYA10)" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Password</label>
          <input type="password" id="inf-login-pass" required placeholder="Enter Your Password" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
        </div>
        
        <div class="flex items-center justify-between text-xs text-gray-400">
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" checked class="rounded accent-[#d4af37]"> Remember me
          </label>
          <a href="https://wa.me/919580835179?text=Hello%20BlackRoots%20Team%2C%20I%20need%20help%20with%20my%20VIP%20Creator%20login%20credentials." target="_blank" class="text-amber-400 hover:underline">Need Help?</a>
        </div>

        <button type="submit" id="login-submit-btn" class="w-full btn-gold-action text-sm py-4 rounded-xl shadow-xl uppercase tracking-wider cursor-pointer font-black">
          Access Creator Portal &rarr;
        </button>
        <p id="login-error-msg" class="hidden text-xs text-red-400 font-bold text-center"></p>
      </form>

      <!-- Instant Test Access Demo Info -->
      <div class="p-3.5 rounded-2xl bg-white/5 border border-[#d4af37]/20 text-left space-y-1.5">
        <div class="flex items-center justify-between">
          <span class="text-[10px] uppercase font-bold text-amber-300 tracking-wider">🌟 Demo Login (Created by Admin):</span>
          <button type="button" onclick="quickFillDemo()" class="text-[10px] text-amber-400 font-bold underline hover:text-white">1-Click Auto Fill</button>
        </div>
        <p class="text-[11px] text-gray-400">User ID: <code class="text-white font-bold bg-black px-1.5 py-0.5 rounded border border-white/10">PRIYA10</code> &bull; Password: <code class="text-white font-bold bg-black px-1.5 py-0.5 rounded border border-white/10">blackroots</code></p>
      </div>

      <div class="pt-2 border-t border-white/10">
        <a href="./index.html" class="text-xs text-gray-400 hover:text-white transition-colors">&larr; Return to Main Website</a>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 2. MAIN CREATOR DASHBOARD APP -->"""

inf_html = re.sub(auth_screen_pattern, new_auth_screen, inf_html, flags=re.DOTALL)

with open('influencer.html', 'w', encoding='utf-8') as f:
    f.write(inf_html)

os.makedirs('influencer', exist_ok=True)
with open(os.path.join('influencer', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(inf_html)

print("1. influencer.html updated (clean login only, no registration)")

# 2. Update admin.html Add Influencer Modal to explicitly have User ID & Password set by Admin
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

old_modal_form = """      <form id="AddInfluencerForm" onsubmit="handleSaveNewInfluencer(event)" class="space-y-4 text-xs">
        <div>
          <label class="block font-bold text-gray-300 uppercase mb-1">Creator Full Name</label>
          <input type="text" id="inf-name-input" required placeholder="e.g. Pooja Hegde" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Mobile / WhatsApp</label>
            <input type="tel" id="inf-phone-input" required placeholder="10-Digit Phone" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Instagram Handle</label>
            <input type="text" id="inf-handle-input" required placeholder="@handle" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Custom Promo Code</label>
            <input type="text" id="inf-code-input" required placeholder="e.g. POOJA10" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white uppercase font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Commission Rate %</label>
            <input type="number" id="inf-comm-input" required value="10" min="1" max="50" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>
        <div>
          <label class="block font-bold text-gray-300 uppercase mb-1">Login Password</label>
          <input type="text" id="inf-pass-input" required value="blackroots" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white font-mono focus:outline-none focus:border-[#d4af37]">
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-[#d4af37] to-amber-500 text-black font-black py-3.5 rounded-xl uppercase tracking-wider shadow-xl hover:brightness-110 cursor-pointer">
          Create &amp; Activate Creator
        </button>
      </form>"""

new_modal_form = """      <form id="AddInfluencerForm" onsubmit="handleSaveNewInfluencer(event)" class="space-y-3.5 text-xs">
        <div>
          <label class="block font-bold text-gray-300 uppercase mb-1">Creator Full Name</label>
          <input type="text" id="inf-name-input" required placeholder="e.g. Pooja Hegde" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">User ID / Username</label>
            <input type="text" id="inf-username-input" required placeholder="e.g. POOJA10" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-white font-mono uppercase font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Login Password</label>
            <input type="text" id="inf-pass-input" required value="pass123" placeholder="Set Password" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-white font-mono focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Promo Coupon Code</label>
            <input type="text" id="inf-code-input" required placeholder="e.g. POOJA10" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-white uppercase font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Commission Rate %</label>
            <input type="number" id="inf-comm-input" required value="10" min="1" max="50" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-white font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Mobile / WhatsApp</label>
            <input type="tel" id="inf-phone-input" required placeholder="10-Digit Mobile" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-white focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="block font-bold text-gray-300 uppercase mb-1">Instagram Handle</label>
            <input type="text" id="inf-handle-input" placeholder="@handle (optional)" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-white focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-[#d4af37] to-amber-500 text-black font-black py-3.5 rounded-xl uppercase tracking-wider shadow-xl hover:brightness-110 cursor-pointer mt-2">
          Create Influencer Account &rarr;
        </button>
      </form>"""

if old_modal_form in admin_html:
    admin_html = admin_html.replace(old_modal_form, new_modal_form)

old_save_fn = """    function handleSaveNewInfluencer(e) {
      e.preventDefault();
      const name = document.getElementById('inf-name-input').value.trim();
      const phone = document.getElementById('inf-phone-input').value.trim();
      const handle = document.getElementById('inf-handle-input').value.trim();
      const code = document.getElementById('inf-code-input').value.trim().toUpperCase().replace(/[^A-Z0-9]/g, '');
      const comm = Number(document.getElementById('inf-comm-input').value) || 10;
      const pass = document.getElementById('inf-pass-input').value.trim();"""

new_save_fn = """    function handleSaveNewInfluencer(e) {
      e.preventDefault();
      const name = document.getElementById('inf-name-input').value.trim();
      const usernameInput = document.getElementById('inf-username-input');
      const username = usernameInput ? usernameInput.value.trim().toUpperCase().replace(/[^A-Z0-9]/g, '') : '';
      const phone = document.getElementById('inf-phone-input').value.trim();
      const handle = document.getElementById('inf-handle-input').value.trim();
      const code = document.getElementById('inf-code-input').value.trim().toUpperCase().replace(/[^A-Z0-9]/g, '');
      const comm = Number(document.getElementById('inf-comm-input').value) || 10;
      const pass = document.getElementById('inf-pass-input').value.trim();
      const finalUsername = username || code;"""

if old_save_fn in admin_html:
    admin_html = admin_html.replace(old_save_fn, new_save_fn)
    admin_html = admin_html.replace("username: code,", "username: finalUsername,")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

os.makedirs('admin', exist_ok=True)
with open(os.path.join('admin', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("2. admin.html updated with explicit User ID & Password creation fields")

# 3. Sync to demo folders
for folder in ['demo_lab', 'preview']:
    if os.path.exists(folder):
        shutil.copy2('influencer.html', os.path.join(folder, 'influencer.html'))
        os.makedirs(os.path.join(folder, 'influencer'), exist_ok=True)
        shutil.copy2('influencer.html', os.path.join(folder, 'influencer', 'index.html'))
        shutil.copy2('admin.html', os.path.join(folder, 'admin.html'))
        os.makedirs(os.path.join(folder, 'admin'), exist_ok=True)
        shutil.copy2('admin.html', os.path.join(folder, 'admin', 'index.html'))
        print(f"3. Synced to {folder}")

print("=== DONE: STRICT ADMIN CREATION ONLY IMPLEMENTED ===")
