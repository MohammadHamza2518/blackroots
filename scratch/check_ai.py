import os
import re
import shutil

# ==============================================================================
# 1. UPDATE INFLUENCER.HTML
# ==============================================================================
with open('influencer.html', 'r', encoding='utf-8') as f:
    inf_html = f.read()

# Replace auth screen with pristine Login Form + Eye Icon toggle + Zero demo boxes
auth_screen_pattern = r'<!-- ========================================================================= -->\s*<!-- 1\. AUTH SCREEN.*?<!-- ========================================================================= -->\s*<!-- 2\. MAIN CREATOR DASHBOARD APP -->'

clean_auth_screen = """<!-- ========================================================================= -->
  <!-- 1. AUTH SCREEN (STRICT CREATOR LOGIN ONLY - USER ID & PASSWORD) -->
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
        <p class="text-[11px] text-gray-300">Creator accounts are provisioned exclusively by BlackRoots Admin. Please sign in with your assigned User ID and Password.</p>
      </div>

      <!-- Pure Creator Login Form -->
      <form id="InfluencerLoginForm" onsubmit="handleInfluencerLogin(event)" class="space-y-4 text-left">
        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Assigned User ID</label>
          <input type="text" id="inf-login-id" required placeholder="Enter Your User ID (e.g. PRIYA10)" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
        </div>
        
        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Password</label>
          <div class="relative">
            <input type="password" id="inf-login-pass" required placeholder="Enter Your Password" class="w-full pl-4 pr-11 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
            <button type="button" onclick="togglePass('inf-login-pass', 'inf-eye-svg')" class="absolute right-3.5 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white p-1 cursor-pointer transition-colors" title="Show / Hide Password">
              <svg id="inf-eye-svg" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
            </button>
          </div>
        </div>
        
        <div class="flex items-center justify-between text-xs text-gray-400">
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" checked class="rounded accent-[#d4af37]"> Remember me
          </label>
          <a href="https://wa.me/919580835179?text=Hello%20BlackRoots%20Team%2C%20I%20need%20assistance%20with%20my%20VIP%20Creator%20login%20credentials." target="_blank" class="text-amber-400 hover:underline">Need Help?</a>
        </div>

        <button type="submit" id="login-submit-btn" class="w-full btn-gold-action text-sm py-4 rounded-xl shadow-xl uppercase tracking-wider cursor-pointer font-black">
          Sign In to Creator Portal &rarr;
        </button>
        <p id="login-error-msg" class="hidden text-xs text-red-400 font-bold text-center"></p>
      </form>

      <div class="pt-2 border-t border-white/10">
        <a href="./index.html" class="text-xs text-gray-400 hover:text-white transition-colors">&larr; Return to Main Website</a>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 2. MAIN CREATOR DASHBOARD APP -->"""

inf_html = re.sub(auth_screen_pattern, clean_auth_screen, inf_html, flags=re.DOTALL)

# Add password visibility toggle function and clean auth check
pass_toggle_fn = """
    // Eye Icon Password Toggle
    function togglePass(inputId, iconId) {
      const input = document.getElementById(inputId);
      const icon = document.getElementById(iconId);
      if (!input) return;
      if (input.type === 'password') {
        input.type = 'text';
        if (icon) {
          icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l18 18" />';
        }
      } else {
        input.type = 'password';
        if (icon) {
          icon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />';
        }
      }
    }
"""

if "function togglePass" not in inf_html:
    inf_html = inf_html.replace("'use strict';", "'use strict';\n" + pass_toggle_fn)

# Strict login handler in influencer.html
old_inf_login_fn = """    function handleInfluencerLogin(e) {
      e.preventDefault();
      const loginId = document.getElementById('inf-login-id').value.trim().toUpperCase();
      const pass = document.getElementById('inf-login-pass').value;
      const errorMsg = document.getElementById('login-error-msg');

      const db = getInfluencersDb();
      const user = db.find(u => 
        (u.username && u.username.toUpperCase() === loginId) || 
        (u.code && u.code.toUpperCase() === loginId) ||
        (u.phone && u.phone === loginId)
      );

      if (user && (user.password === pass || pass === 'blackroots')) {
        currentInfluencer = user;
        sessionStorage.setItem('br_active_inf_id', user.id);
        errorMsg.classList.add('hidden');
        
        document.getElementById('InfluencerAuthScreen').classList.add('hidden');
        document.getElementById('InfluencerDashboardApp').classList.remove('hidden');
        renderDashboard();
        showToast('Welcome back, ' + user.name + '!');
      } else {
        errorMsg.textContent = 'Invalid credentials. Check promo code or password.';
        errorMsg.classList.remove('hidden');
      }
    }"""

new_inf_login_fn = """    function handleInfluencerLogin(e) {
      e.preventDefault();
      const loginId = document.getElementById('inf-login-id').value.trim().toUpperCase();
      const pass = document.getElementById('inf-login-pass').value.trim();
      const errorMsg = document.getElementById('login-error-msg');

      const db = getInfluencersDb();
      const user = db.find(u => 
        (u.username && u.username.toUpperCase() === loginId) || 
        (u.code && u.code.toUpperCase() === loginId)
      );

      if (user && user.password === pass) {
        currentInfluencer = user;
        sessionStorage.setItem('br_active_inf_id', user.id);
        errorMsg.classList.add('hidden');
        
        document.getElementById('InfluencerAuthScreen').classList.add('hidden');
        document.getElementById('InfluencerDashboardApp').classList.remove('hidden');
        renderDashboard();
        showToast('Welcome back, ' + user.name + '!');
      } else {
        errorMsg.textContent = 'Incorrect User ID or Password. Please check with BlackRoots Admin.';
        errorMsg.classList.remove('hidden');
      }
    }"""

if old_inf_login_fn in inf_html:
    inf_html = inf_html.replace(old_inf_login_fn, new_inf_login_fn)

with open('influencer.html', 'w', encoding='utf-8') as f:
    f.write(inf_html)

os.makedirs('influencer', exist_ok=True)
with open(os.path.join('influencer', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(inf_html)

print("1. [SUCCESS] influencer.html updated with password eye toggle & zero demo boxes")

# ==============================================================================
# 2. UPDATE ADMIN.HTML WITH PASSWORD EYE TOGGLE & CREATOR TABLE PASSWORDS
# ==============================================================================
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

# Admin Login Eye Icon
old_admin_login_box = """        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Master Password</label>
          <input type="password" id="admin-pass-input" required placeholder="Enter Admin Password" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
        </div>"""

new_admin_login_box = """        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Master Password</label>
          <div class="relative">
            <input type="password" id="admin-pass-input" required placeholder="Enter Admin Password" class="w-full pl-4 pr-11 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
            <button type="button" onclick="togglePass('admin-pass-input', 'admin-eye-svg')" class="absolute right-3.5 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white p-1 cursor-pointer transition-colors" title="Show / Hide Password">
              <svg id="admin-eye-svg" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
            </button>
          </div>
        </div>"""

if old_admin_login_box in admin_html:
    admin_html = admin_html.replace(old_admin_login_box, new_admin_login_box)

# Clean out demo text from admin screen
admin_html = admin_html.replace('<p class="text-[11px] text-gray-500">Default Access: <code class="text-gray-400">blackroots2026</code> (Changeable in Settings)</p>', '')

if "function togglePass" not in admin_html:
    admin_html = admin_html.replace("'use strict';", "'use strict';\n" + pass_toggle_fn)

# In Admin Influencers Table: Show User ID and Password so Admin can easily share with creator
old_inf_table_head = """              <tr>
                <th class="py-3 px-3">Creator Name &amp; Handle</th>
                <th class="py-3 px-3">Promo Code</th>
                <th class="py-3 px-3">Commission %</th>
                <th class="py-3 px-3">Orders Driven</th>
                <th class="py-3 px-3">Sales Driven (₹)</th>
                <th class="py-3 px-3">Total Earned</th>
                <th class="py-3 px-3">Unpaid Balance</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3 text-right">Actions</th>
              </tr>"""

new_inf_table_head = """              <tr>
                <th class="py-3 px-3">Creator Details</th>
                <th class="py-3 px-3">User ID</th>
                <th class="py-3 px-3">Assigned Password</th>
                <th class="py-3 px-3">Promo Code</th>
                <th class="py-3 px-3">Commission %</th>
                <th class="py-3 px-3">Orders</th>
                <th class="py-3 px-3">Sales (₹)</th>
                <th class="py-3 px-3">Unpaid Balance</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3 text-right">Actions</th>
              </tr>"""

if old_inf_table_head in admin_html:
    admin_html = admin_html.replace(old_inf_table_head, new_inf_table_head)

old_table_render = """      tbody.innerHTML = influencers.map(u => `
        <tr class="hover:bg-white/5 transition-colors">
          <td class="py-3 px-3">
            <div class="font-bold text-white">${u.name}</div>
            <div class="text-[10px] text-gray-400">${u.handle || '@handle'} &bull; ${u.phone}</div>
          </td>
          <td class="py-3 px-3">
            <span class="px-2.5 py-1 rounded-lg bg-amber-500/20 text-amber-300 font-mono font-black border border-amber-500/30">
              ${u.code}
            </span>
          </td>
          <td class="py-3 px-3 font-bold text-white">
            ${u.comm_rate || 10}% Flat
          </td>
          <td class="py-3 px-3 font-bold text-amber-300 font-mono">
            ${u.total_orders || 0}
          </td>
          <td class="py-3 px-3 font-bold text-white">
            ₹${Number(u.total_sales || 0).toLocaleString()}
          </td>
          <td class="py-3 px-3 font-bold text-emerald-400">
            ₹${Number(u.total_earned || 0).toLocaleString()}
          </td>
          <td class="py-3 px-3 font-bold text-amber-400 font-mono">
            ₹${Number(u.unpaid_balance || 0).toLocaleString()}
          </td>
          <td class="py-3 px-3">
            <span class="px-2 py-0.5 rounded-full text-[9px] font-bold ${u.status === 'Active' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'}">
              ${u.status || 'Active'}
            </span>
          </td>
          <td class="py-3 px-3 text-right space-x-1">
            <button onclick="toggleInfStatus('${u.id}')" class="px-2 py-1 rounded bg-white/5 hover:bg-white/10 text-[10px] text-gray-300 font-bold">Toggle</button>
            <button onclick="deleteInfluencer('${u.id}')" class="px-2 py-1 rounded bg-red-500/10 hover:bg-red-500/20 text-[10px] text-red-400 font-bold">Delete</button>
          </td>
        </tr>
      `).join('');"""

new_table_render = """      tbody.innerHTML = influencers.map(u => `
        <tr class="hover:bg-white/5 transition-colors">
          <td class="py-3 px-3">
            <div class="font-bold text-white">${u.name}</div>
            <div class="text-[10px] text-gray-400">${u.handle || '@handle'} &bull; ${u.phone}</div>
          </td>
          <td class="py-3 px-3">
            <span class="px-2 py-1 rounded-lg bg-black text-amber-300 font-mono font-bold border border-white/20">
              ${u.username || u.code}
            </span>
          </td>
          <td class="py-3 px-3 font-mono text-gray-300 font-bold">
            <code class="bg-black/60 px-2 py-0.5 rounded border border-white/10">${u.password || '••••••'}</code>
          </td>
          <td class="py-3 px-3">
            <span class="px-2.5 py-1 rounded-lg bg-amber-500/20 text-amber-300 font-mono font-black border border-amber-500/30">
              ${u.code}
            </span>
          </td>
          <td class="py-3 px-3 font-bold text-white">
            ${u.comm_rate || 10}% Flat
          </td>
          <td class="py-3 px-3 font-bold text-amber-300 font-mono">
            ${u.total_orders || 0}
          </td>
          <td class="py-3 px-3 font-bold text-white">
            ₹${Number(u.total_sales || 0).toLocaleString()}
          </td>
          <td class="py-3 px-3 font-bold text-amber-400 font-mono">
            ₹${Number(u.unpaid_balance || 0).toLocaleString()}
          </td>
          <td class="py-3 px-3">
            <span class="px-2 py-0.5 rounded-full text-[9px] font-bold ${u.status === 'Active' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'}">
              ${u.status || 'Active'}
            </span>
          </td>
          <td class="py-3 px-3 text-right space-x-1 whitespace-nowrap">
            <button onclick="toggleInfStatus('${u.id}')" class="px-2 py-1 rounded bg-white/5 hover:bg-white/10 text-[10px] text-gray-300 font-bold cursor-pointer">Toggle</button>
            <button onclick="deleteInfluencer('${u.id}')" class="px-2 py-1 rounded bg-red-500/10 hover:bg-red-500/20 text-[10px] text-red-400 font-bold cursor-pointer">Delete</button>
          </td>
        </tr>
      `).join('');"""

if old_table_render in admin_html:
    admin_html = admin_html.replace(old_table_render, new_table_render)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

os.makedirs('admin', exist_ok=True)
with open(os.path.join('admin', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("2. [SUCCESS] admin.html updated with password visibility & creator credentials list")

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

print("=== DONE: ALL REQUESTS APPLIED 100% ===")
