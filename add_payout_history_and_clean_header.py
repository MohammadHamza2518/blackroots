import os

# 1. REWRITE INFLUENCER PORTAL WITH CLEAN HEADER & LIVE PAYOUT HISTORY TABLE (influencer.html)
influencer_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Influencer Login & Portal &mdash; BlackRoots Herbal Hair Dye Shampoo</title>
  <meta name="description" content="BlackRoots Official VIP Creator Login Portal. Access your assigned promo code, track live commission earnings, view payout history, and request payouts.">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brandDark: '#0a0b0e',
            brandCard: '#12151c',
            brandEmerald: '#123824',
            brandGold: '#d4af37',
          },
          fontFamily: {
            sans: ['Plus Jakarta Sans', 'system-ui', '-apple-system', 'sans-serif'],
          }
        }
      }
    }
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./assets/theme.css">
  <script src="./assets/theme.js" defer></script>
</head>
<body class="bg-[#0a0b0e] text-white font-sans antialiased selection:bg-[#d4af37] selection:text-black min-h-screen flex flex-col justify-between">

  <!-- Top Announcement Bar -->
  <div class="bg-gradient-to-r from-[#123824] via-[#0d2a1c] to-[#123824] text-[#f5e4ab] border-b border-[#d4af37]/30 py-2.5 px-4 text-center text-xs md:text-sm font-semibold tracking-wide">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-3 flex-wrap">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-bold text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
          VIP CREATOR PORTAL
        </span>
        <span>Secured Login &bull; Minimum Payout Threshold: ₹1,000.00</span>
      </div>
      <a href="./index.html" class="text-xs text-amber-300 underline hover:text-white transition-colors">Main Store &rarr;</a>
    </div>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-50 bg-[#0a0b0e]/90 backdrop-blur-xl border-b border-[#d4af37]/20 py-4 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <a href="./index.html" class="flex items-center gap-2.5 no-underline">
        <span class="text-2xl sm:text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-[#d4af37] to-amber-500 tracking-tight">BlackRoots</span>
        <span class="text-[10px] uppercase font-extrabold text-amber-300 bg-amber-500/20 px-2.5 py-0.5 rounded-full border border-amber-500/30 tracking-wider">VIP CREATOR</span>
      </a>

      <div class="flex items-center gap-3">
        <!-- Logged Out State Button -->
        <button id="HeaderLoginBtn" type="button" onclick="showAuthSection()" class="bg-[#d4af37] hover:bg-amber-400 text-black font-extrabold text-xs px-5 py-2.5 rounded-full shadow-lg transition-all transform hover:scale-105 cursor-pointer">
          Login / Portal Access
        </button>

        <!-- Logged In State Clean Logout Only (Header badge removed as requested) -->
        <div id="HeaderProfileGroup" class="hidden items-center gap-3">
          <button type="button" onclick="handleLogout()" class="bg-red-500/20 hover:bg-red-500/30 text-red-300 border border-red-500/40 font-bold text-xs px-4 py-1.5 rounded-full transition-all cursor-pointer">
            Logout
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- ================= STATE 1: LOGIN GATE ================= -->
  <section id="LoginGateSection" class="max-w-md mx-auto px-4 py-14 w-full my-auto space-y-6">
    <div class="p-6 sm:p-8 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/50 shadow-2xl bg-gradient-to-b from-[#12151c] to-[#0a0b0e] space-y-6 relative overflow-hidden">
      <div class="absolute -right-12 -top-12 w-40 h-40 bg-[#d4af37]/10 rounded-full blur-2xl pointer-events-none"></div>

      <div class="text-center space-y-2 relative z-10">
        <div class="w-12 h-12 rounded-2xl bg-[#d4af37]/20 border border-[#d4af37]/40 flex items-center justify-center mx-auto text-amber-300 text-xl font-bold">
          🔑
        </div>
        <h1 class="text-2xl font-extrabold text-white tracking-tight">Creator Portal Login</h1>
        <p class="text-xs text-gray-400 font-medium">Enter your Admin-Assigned User ID & Password to access your dashboard.</p>
      </div>

      <!-- Login Form -->
      <form onsubmit="handleLoginSubmit(event)" class="space-y-4 text-xs relative z-10">
        <div id="LoginErrorBanner" class="p-3.5 rounded-xl bg-red-500/20 border border-red-500/40 text-red-300 text-xs font-semibold hidden">
          ⚠️ Invalid User ID or Password! Access denied. Contact Store Admin for credentials.
        </div>

        <div class="space-y-1.5">
          <label class="font-bold text-gray-300 uppercase tracking-wider block text-[11px]">Assigned User ID</label>
          <input id="LoginUserID" type="text" required placeholder="Enter assigned User ID..." class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3.5 text-white font-mono text-sm focus:outline-none focus:border-[#d4af37] transition-all">
        </div>

        <div class="space-y-1.5">
          <label class="font-bold text-gray-300 uppercase tracking-wider block text-[11px]">Password</label>
          <div class="relative flex items-center">
            <input id="LoginPassword" type="password" required placeholder="Enter assigned password..." class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3.5 pr-10 text-white font-mono text-sm focus:outline-none focus:border-[#d4af37] transition-all">
            <button type="button" onclick="togglePasswordVisibility()" class="absolute right-3 text-gray-400 hover:text-amber-300 text-sm cursor-pointer" title="Show/Hide Password">
              👁️
            </button>
          </div>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-amber-400 via-[#d4af37] to-amber-500 text-black font-extrabold text-sm py-4 rounded-2xl shadow-xl hover:brightness-110 transition-all cursor-pointer tracking-wide uppercase mt-2">
          Unlock Creator Dashboard &rarr;
        </button>
      </form>

      <div class="text-center pt-3 border-t border-white/10">
        <p class="text-[11px] text-gray-400 font-medium">Don't have login details? <span class="text-amber-300 font-bold">Contact BlackRoots Store Owner for your credentials.</span></p>
      </div>
    </div>
  </section>

  <!-- ================= STATE 2: AUTHENTICATED DASHBOARD ================= -->
  <main id="DashboardSection" class="hidden max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">

    <!-- Influencer Welcome Hero Banner -->
    <div class="p-6 sm:p-8 rounded-3xl glass-panel-luxury border-2 border-[#d4af37]/40 shadow-2xl relative overflow-hidden bg-gradient-to-br from-[#12151c] via-[#0d0e12] to-black">
      <div class="absolute -right-16 -top-16 w-64 h-64 bg-[#d4af37]/10 rounded-full blur-3xl pointer-events-none"></div>
      
      <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div class="flex items-center gap-4">
          <div class="relative">
            <img src="./assets/blackroots-bottle-single.png" alt="Creator Avatar" class="w-16 h-16 sm:w-20 sm:h-20 rounded-2xl object-cover border-2 border-[#d4af37] shadow-xl bg-[#12151c] p-1">
            <span class="absolute -bottom-1 -right-1 w-5 h-5 rounded-full bg-emerald-500 border-2 border-black flex items-center justify-center text-[10px]" title="Active Influencer">✓</span>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h1 id="DashCreatorName" class="text-xl sm:text-3xl font-extrabold text-white tracking-tight">Creator Name</h1>
              <span class="text-[10px] font-extrabold uppercase bg-amber-500/20 text-amber-300 border border-amber-500/40 px-2.5 py-0.5 rounded-full tracking-wider">ACTIVE CREATOR</span>
            </div>
            <p class="text-xs sm:text-sm text-gray-400 mt-1 font-medium">User ID: <strong id="DashUserID" class="text-amber-300 font-mono">userid</strong> &bull; <span class="text-emerald-400 font-semibold"><span id="DashCommissionRate">15%</span> Commission Rate</span></p>
          </div>
        </div>

        <div class="flex flex-col items-end gap-1.5">
          <button type="button" onclick="openPayoutModal()" class="w-full md:w-auto bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-xs sm:text-sm px-6 py-3.5 rounded-2xl shadow-xl hover:brightness-110 transition-all flex items-center justify-center gap-2 cursor-pointer">
            <span>💸 Request Payout</span>
          </button>
          <span class="text-[11px] text-amber-300 font-medium">⚠️ Minimum Payout Limit: ₹1,000.00</span>
        </div>
      </div>
    </div>

    <!-- Key Performance Indicators (KPI Cards Grid) -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      
      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-1.5">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Total Sales Brought</span>
          <span class="text-amber-400 text-base">🛍️</span>
        </div>
        <div id="DashTotalSalesVal" class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">₹0.00</div>
        <p class="text-[11px] text-emerald-400 font-semibold">Ready for new sales</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-1.5">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Orders Brought</span>
          <span class="text-amber-400 text-base">📦</span>
        </div>
        <div id="DashOrdersCountVal" class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">0 Orders</div>
        <p class="text-[11px] text-gray-400 font-medium">Tracking live</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-1.5">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Total Earnings</span>
          <span class="text-amber-400 text-base">💰</span>
        </div>
        <div id="DashTotalEarningsVal" class="text-2xl sm:text-3xl font-extrabold text-amber-300 tracking-tight">₹0.00</div>
        <p id="DashSettledVal" class="text-[11px] text-gray-400 font-medium">₹0.00 Settled</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border-2 border-emerald-500/40 bg-[#123824]/30 shadow-xl space-y-1.5 relative overflow-hidden">
        <div class="flex items-center justify-between text-emerald-300 text-xs font-bold uppercase tracking-wider">
          <span>Unpaid Balance</span>
          <span class="text-emerald-400 text-base">💳</span>
        </div>
        <div id="DashUnpaidVal" class="text-2xl sm:text-3xl font-extrabold text-emerald-400 tracking-tight">₹0.00</div>
        <p class="text-[11px] text-emerald-300 font-semibold">Min Payout: ₹1,000</p>
      </div>

    </div>

    <!-- Referral Code & Share Link Box -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
        <div>
          <h2 class="text-lg font-bold text-white tracking-tight">Your Assigned Promo Code & Referral Link</h2>
          <p class="text-xs text-gray-400 font-medium">Assigned by Store Owner. Share this code with followers to earn commission!</p>
        </div>
        <span class="text-xs bg-amber-500/20 text-amber-300 font-bold px-3 py-1 rounded-full border border-amber-500/30 self-start sm:self-auto">
          🔒 Code Verified by Admin
        </span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        
        <!-- Code Box -->
        <div class="space-y-2">
          <label class="text-xs font-bold text-gray-300 uppercase tracking-wider block">Assigned Promo Code (10% OFF for Followers)</label>
          <div class="flex items-center gap-2 bg-[#0a0b0e] border-2 border-[#d4af37]/60 rounded-2xl p-2 shadow-inner">
            <span id="DashCodeDisplay" class="font-mono text-lg font-extrabold text-amber-300 px-3 tracking-widest uppercase">CODE</span>
            <button id="CopyCodeBtn" type="button" class="ml-auto bg-[#d4af37] hover:bg-amber-400 text-black font-extrabold text-xs px-4 py-2.5 rounded-xl transition-all shadow-md cursor-pointer">
              Copy Code
            </button>
          </div>
        </div>

        <!-- Direct Link Box -->
        <div class="space-y-2">
          <label class="text-xs font-bold text-gray-300 uppercase tracking-wider block">Direct Shopping Referral Link</label>
          <div class="flex items-center gap-2 bg-[#0a0b0e] border border-white/10 rounded-2xl p-2 shadow-inner">
            <input id="RefLinkInput" type="text" readonly value="https://blackroots.in/?ref=CODE" class="bg-transparent text-xs text-gray-300 font-mono px-3 w-full focus:outline-none">
            <button id="CopyLinkBtn" type="button" class="ml-auto bg-white/10 hover:bg-white/20 text-white font-bold text-xs px-4 py-2.5 rounded-xl transition-all cursor-pointer">
              Copy Link
            </button>
          </div>
        </div>

      </div>
    </div>

    <!-- SECTION: MY PAYOUT WITHDRAWAL HISTORY -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-lg font-bold text-white tracking-tight">📜 My Payout Withdrawal History</h2>
          <p class="text-xs text-gray-400 font-medium">Track your requested payout status and settlements by Store Owner</p>
        </div>
        <span class="text-xs bg-amber-500/20 text-amber-300 font-bold px-3 py-1 rounded-full border border-amber-500/30">
          Live Transaction Ledger
        </span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3.5 px-4">Request ID</th>
              <th class="py-3.5 px-4">Requested Amount</th>
              <th class="py-3.5 px-4">UPI ID</th>
              <th class="py-3.5 px-4">Date Requested</th>
              <th class="py-3.5 px-4 text-right">Status</th>
            </tr>
          </thead>
          <tbody id="MyPayoutHistoryBody" class="divide-y divide-white/5 font-medium text-gray-300">
            <tr>
              <td colspan="5" class="py-6 text-center text-gray-400 text-xs font-medium">
                No payout requests submitted yet. Click "Request Payout" above when your balance reaches ₹1,000!
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Live Sales Ledger Table -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-5">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 class="text-lg font-bold text-white tracking-tight">Sales Brought By Your Code (<span id="DashTableCode">CODE</span>)</h2>
          <p class="text-xs text-gray-400 font-medium">Live automatic breakdown of orders using your assigned code</p>
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3.5 px-4 rounded-l-xl">Order ID</th>
              <th class="py-3.5 px-4">Date</th>
              <th class="py-3.5 px-4">Customer Name</th>
              <th class="py-3.5 px-4">Sale Amount</th>
              <th class="py-3.5 px-4">Follower Discount</th>
              <th class="py-3.5 px-4">Your Commission</th>
              <th class="py-3.5 px-4 rounded-r-xl">Status</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5 font-medium text-gray-300">
            <tr>
              <td colspan="7" class="py-8 text-center text-gray-400">
                ✨ No orders recorded yet for your code. Share your code with followers to earn your first commission!
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- Payout Request Modal -->
  <div id="PayoutModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-md w-full p-6 shadow-2xl relative space-y-5">
      <button type="button" onclick="closePayoutModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 class="text-xl font-bold text-amber-300 tracking-tight">Request Commission Payout</h3>
        <p class="text-xs text-gray-400 font-medium">Current Unpaid Balance: <strong id="ModalUnpaidBalance" class="text-emerald-400 font-extrabold">₹0.00</strong></p>
        <p class="text-[11px] text-amber-300 font-semibold">⚠️ Minimum Payout Limit is ₹1,000.00</p>
      </div>

      <form onsubmit="handlePayoutSubmit(event)" class="space-y-4 text-xs">
        <div class="space-y-1.5">
          <label class="font-bold text-gray-300 uppercase tracking-wider block">Requested Amount (₹)</label>
          <input id="PayoutAmountInput" type="number" value="1000" min="1000" required class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono text-base font-extrabold focus:outline-none focus:border-[#d4af37]">
        </div>

        <div class="space-y-1.5">
          <label class="font-bold text-gray-300 uppercase tracking-wider block">Enter Your UPI ID (GPay / PhonePe / Paytm)</label>
          <input id="PayoutUPIInput" type="text" placeholder="e.g. 9876543210@paytm or name@okicici" required class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono focus:outline-none focus:border-[#d4af37]">
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-sm py-3.5 rounded-2xl shadow-xl hover:brightness-110 transition-all cursor-pointer uppercase font-bold">
          Submit Payout Request To Store Owner
        </button>
      </form>
    </div>
  </div>

  <!-- Toast Container -->
  <div id="Toast" class="fixed bottom-6 right-6 z-50 bg-[#d4af37] text-black font-extrabold text-xs px-5 py-3 rounded-2xl shadow-2xl transform translate-y-20 opacity-0 transition-all duration-300 flex items-center gap-2 pointer-events-none">
    <span id="ToastMsg">Copied to Clipboard!</span>
  </div>

  <!-- Footer -->
  <footer class="bg-black border-t border-[#d4af37]/20 py-8 px-4 text-center text-xs text-gray-400 mt-12">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 font-medium">
      <p>&copy; 2026 BlackRoots Creator Portal. Managed by Admin.</p>
      <div class="flex items-center gap-4 text-amber-300 font-semibold">
        <a href="./index.html" class="hover:underline">Main Store</a>
        <a href="./product.html" class="hover:underline">Buy Shampoo</a>
      </div>
    </div>
  </footer>

  <script>
    let activeUserObj = null;

    function getAccountsDB() {
      const stored = localStorage.getItem('blackroots_accounts_db');
      if (stored) {
        try { return JSON.parse(stored); } catch(e) {}
      }
      return {};
    }

    function getPayoutsDB() {
      const stored = localStorage.getItem('blackroots_payouts_db');
      if (stored) {
        try { return JSON.parse(stored); } catch(e) {}
      }
      return [];
    }

    function savePayoutsDB(list) {
      localStorage.setItem('blackroots_payouts_db', JSON.stringify(list));
    }

    document.addEventListener('DOMContentLoaded', function() {
      const loggedUser = localStorage.getItem('blackroots_influencer_userid');
      const db = getAccountsDB();

      if (loggedUser && db[loggedUser]) {
        activeUserObj = db[loggedUser];
        activeUserObj.userId = loggedUser;
        renderDashboard(activeUserObj);
      } else {
        renderLoginGate();
      }
    });

    function togglePasswordVisibility() {
      const passInput = document.getElementById('LoginPassword');
      if (passInput) {
        passInput.type = passInput.type === 'password' ? 'text' : 'password';
      }
    }

    function handleLoginSubmit(e) {
      e.preventDefault();
      const userId = document.getElementById('LoginUserID').value.trim().toLowerCase();
      const pass = document.getElementById('LoginPassword').value.trim();
      const errBanner = document.getElementById('LoginErrorBanner');

      const db = getAccountsDB();

      if (db[userId] && db[userId].pass.trim() === pass) {
        if (errBanner) errBanner.classList.add('hidden');
        localStorage.setItem('blackroots_influencer_userid', userId);
        activeUserObj = db[userId];
        activeUserObj.userId = userId;
        renderDashboard(activeUserObj);
        showToast('Login Successful! Welcome to your Creator Dashboard.');
      } else {
        if (errBanner) errBanner.classList.remove('hidden');
      }
    }

    function handleLogout() {
      localStorage.removeItem('blackroots_influencer_userid');
      activeUserObj = null;
      renderLoginGate();
      showToast('Logged out successfully.');
    }

    function renderDashboard(userObj) {
      const loginGate = document.getElementById('LoginGateSection');
      const dash = document.getElementById('DashboardSection');
      const headerLoginBtn = document.getElementById('HeaderLoginBtn');
      const headerProfileGroup = document.getElementById('HeaderProfileGroup');

      if (loginGate) loginGate.classList.add('hidden');
      if (dash) dash.classList.remove('hidden');
      if (headerLoginBtn) headerLoginBtn.classList.add('hidden');
      if (headerProfileGroup) headerProfileGroup.classList.remove('hidden'), headerProfileGroup.classList.add('flex');

      const nameEl = document.getElementById('DashCreatorName');
      const userIdEl = document.getElementById('DashUserID');
      const codeEl = document.getElementById('DashCodeDisplay');
      const tableCodeEl = document.getElementById('DashTableCode');
      const refInput = document.getElementById('RefLinkInput');
      const rateEl = document.getElementById('DashCommissionRate');

      if (nameEl) nameEl.innerText = userObj.name;
      if (userIdEl) userIdEl.innerText = userObj.userId;
      if (codeEl) codeEl.innerText = userObj.code;
      if (tableCodeEl) tableCodeEl.innerText = userObj.code;
      if (rateEl) rateEl.innerText = userObj.rate + '%';
      if (refInput) refInput.value = `https://blackroots.in/?ref=${userObj.code}`;

      document.getElementById('CopyCodeBtn').onclick = () => copyToClipboard(userObj.code, `Code ${userObj.code} Copied!`);
      document.getElementById('CopyLinkBtn').onclick = () => copyToClipboard(`https://blackroots.in/?ref=${userObj.code}`, `Referral Link Copied!`);

      renderMyPayoutHistory(userObj.userId);
    }

    function renderMyPayoutHistory(uId) {
      const historyBody = document.getElementById('MyPayoutHistoryBody');
      const payouts = getPayoutsDB();
      const myPayouts = payouts.filter(p => p.userId === uId);

      if (myPayouts.length === 0) {
        historyBody.innerHTML = `
          <tr>
            <td colspan="5" class="py-6 text-center text-gray-400 text-xs font-medium">
              No payout requests submitted yet. Click "Request Payout" above when your balance reaches ₹1,000!
            </td>
          </tr>`;
      } else {
        historyBody.innerHTML = myPayouts.map(p => `
          <tr class="hover:bg-white/5 transition-colors">
            <td class="py-3.5 px-4 font-mono text-amber-300 font-bold">${p.id}</td>
            <td class="py-3.5 px-4 font-extrabold text-emerald-400">${p.amount}</td>
            <td class="py-3.5 px-4 font-mono text-gray-300 bg-white/5 px-2 py-1 rounded">${p.upi}</td>
            <td class="py-3.5 px-4 text-gray-400">${p.date || 'Today'}</td>
            <td class="py-3.5 px-4 text-right">
              ${p.status === 'Paid' 
                ? '<span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-3 py-1 rounded-full text-[10px] font-bold">✓ Paid & Settled</span>' 
                : '<span class="bg-amber-500/20 text-amber-300 border border-amber-500/30 px-3 py-1 rounded-full text-[10px] font-bold">⌛ Pending Approval</span>'}
            </td>
          </tr>
        `).join('');
      }
    }

    function renderLoginGate() {
      const loginGate = document.getElementById('LoginGateSection');
      const dash = document.getElementById('DashboardSection');
      const headerLoginBtn = document.getElementById('HeaderLoginBtn');
      const headerProfileGroup = document.getElementById('HeaderProfileGroup');

      if (loginGate) loginGate.classList.remove('hidden');
      if (dash) dash.classList.add('hidden');
      if (headerLoginBtn) headerLoginBtn.classList.remove('hidden');
      if (headerProfileGroup) headerProfileGroup.classList.add('hidden');
    }

    function showAuthSection() {
      renderLoginGate();
    }

    function copyToClipboard(text, msg) {
      navigator.clipboard.writeText(text);
      showToast(msg || 'Copied to Clipboard!');
    }

    function showToast(msg) {
      const toast = document.getElementById('Toast');
      const toastMsg = document.getElementById('ToastMsg');
      if (toast && toastMsg) {
        toastMsg.innerText = msg;
        toast.classList.remove('translate-y-20', 'opacity-0');
        setTimeout(() => {
          toast.classList.add('translate-y-20', 'opacity-0');
        }, 2500);
      }
    }

    function openPayoutModal() {
      const currentUnpaid = activeUserObj ? (activeUserObj.unpaid || 0) : 0;
      if (currentUnpaid < 1000) {
        showToast('⚠️ Minimum payout threshold is ₹1,000. Earn at least ₹1,000 to request withdrawal.');
      }
      const modal = document.getElementById('PayoutModal');
      const unpaidSpan = document.getElementById('ModalUnpaidBalance');
      if (unpaidSpan) unpaidSpan.innerText = `₹${currentUnpaid.toFixed(2)}`;
      if (modal) modal.classList.remove('hidden'), modal.classList.add('flex');
    }

    function closePayoutModal() {
      const modal = document.getElementById('PayoutModal');
      if (modal) modal.classList.add('hidden'), modal.classList.remove('flex');
    }

    function handlePayoutSubmit(e) {
      e.preventDefault();
      const amountVal = parseFloat(document.getElementById('PayoutAmountInput').value);
      const upiVal = document.getElementById('PayoutUPIInput').value.trim();

      if (amountVal < 1000) {
        showToast('⚠️ Minimum payout limit is ₹1,000.00!');
        return;
      }

      if (!activeUserObj) return;

      const payouts = getPayoutsDB();
      const todayDate = new Date().toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
      payouts.push({
        id: 'PAY-' + Math.floor(1000 + Math.random() * 9000),
        name: activeUserObj.name,
        userId: activeUserObj.userId,
        amount: '₹' + amountVal.toFixed(2),
        upi: upiVal,
        date: todayDate,
        status: 'Pending'
      });
      savePayoutsDB(payouts);

      closePayoutModal();
      renderMyPayoutHistory(activeUserObj.userId);
      showToast(`Payout Request for ₹${amountVal} Submitted To Admin! UPI: ${upiVal}`);
    }
  </script>
</body>
</html>
"""

# 2. REWRITE ADMIN PANEL WITH SETTLED PAYOUTS HISTORY TABLE (admin-influencer.html)
admin_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Store Owner Admin Panel &mdash; BlackRoots</title>
  <meta name="description" content="Store Owner Panel for BlackRoots. Assign User IDs, Passwords, track real sales, and settle payouts (Min ₹1,000). Full payout history.">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brandDark: '#0a0b0e',
            brandCard: '#12151c',
            brandEmerald: '#123824',
            brandGold: '#d4af37',
          },
          fontFamily: {
            sans: ['Plus Jakarta Sans', 'system-ui', '-apple-system', 'sans-serif'],
          }
        }
      }
    }
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./assets/theme.css">
  <script src="./assets/theme.js" defer></script>
</head>
<body class="bg-[#0a0b0e] text-white font-sans antialiased selection:bg-[#d4af37] selection:text-black min-h-screen flex flex-col justify-between">

  <!-- Top Admin Bar -->
  <div class="bg-[#12151c] border-b border-[#d4af37]/30 py-2.5 px-4 text-xs font-bold text-gray-300">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-3">
      <div class="flex items-center gap-2">
        <span class="bg-red-500 text-white font-extrabold text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">STORE OWNER CONTROL</span>
        <span>BlackRoots Live Influencer Management Panel</span>
      </div>
      <a href="./index.html" class="text-amber-300 hover:underline font-semibold">Go to Main Store &rarr;</a>
    </div>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-50 bg-[#0a0b0e]/95 backdrop-blur-xl border-b border-[#d4af37]/20 py-4 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="text-2xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-[#d4af37] to-amber-500 tracking-tight">BlackRoots Admin</span>
        <span class="text-[10px] font-bold text-emerald-400 bg-emerald-500/20 px-2.5 py-0.5 rounded-full border border-emerald-500/30">PAYOUT HISTORY ACTIVE</span>
      </div>

      <button type="button" onclick="openAddInfluencerModal()" class="bg-[#d4af37] hover:bg-amber-400 text-black font-extrabold text-xs px-5 py-2.5 rounded-full shadow-lg transition-all transform hover:scale-105 cursor-pointer">
        + Add New Influencer (User ID & Password)
      </button>
    </div>
  </header>

  <!-- Main Body -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">

    <!-- 3 Simple Stat Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-xl space-y-1.5">
        <div class="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Sales From Influencers</div>
        <div id="StatTotalSales" class="text-3xl font-extrabold text-amber-300 tracking-tight">₹0.00</div>
        <p id="StatTotalOrders" class="text-xs text-gray-400 font-medium">0 Total Orders Driven</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-xl space-y-1.5">
        <div class="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Influencers Joined</div>
        <div id="StatTotalInfluencers" class="text-3xl font-extrabold text-white tracking-tight">0 Influencers</div>
        <p class="text-xs text-gray-400 font-medium">User IDs Created By You</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border-2 border-emerald-500/30 bg-emerald-500/5 shadow-xl space-y-1.5">
        <div class="text-emerald-300 text-xs font-bold uppercase tracking-wider">Pending Payout Requests (Min ₹1,000)</div>
        <div id="StatPendingPayouts" class="text-3xl font-extrabold text-emerald-400 tracking-tight">₹0.00</div>
        <p id="StatPendingCount" class="text-xs text-emerald-300 font-semibold">0 Pending Payments</p>
      </div>
    </div>

    <!-- SECTION 1: PENDING PAYOUTS TO APPROVE -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-lg font-bold text-white tracking-tight">💸 Step 1: Pay Influencers & Mark Paid</h2>
          <p class="text-xs text-gray-400 font-medium">When creators request payouts (Min ₹1,000), their UPI ID will appear here for 1-click settlement.</p>
        </div>
        <span id="BadgePendingCount" class="text-xs bg-emerald-500/20 text-emerald-300 font-bold px-3 py-1 rounded-full border border-emerald-500/30">
          0 Pending Payments
        </span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3.5 px-4">Influencer Name</th>
              <th class="py-3.5 px-4">User ID</th>
              <th class="py-3.5 px-4">Amount To Pay</th>
              <th class="py-3.5 px-4">Influencer UPI ID (Pay Here)</th>
              <th class="py-3.5 px-4 text-right">Action</th>
            </tr>
          </thead>
          <tbody id="PayoutsTableBody" class="divide-y divide-white/5 font-medium text-gray-300">
            <tr id="EmptyPayoutRow">
              <td colspan="5" class="py-8 text-center text-gray-400 text-xs font-medium">
                ✨ No pending payout requests. All payouts are 100% settled!
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SECTION 2: SETTLED PAYOUTS HISTORY (ADMIN LEDGER) -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-lg font-bold text-white tracking-tight">📜 Settled Payouts History (Completed Transactions)</h2>
          <p class="text-xs text-gray-400 font-medium">Historical audit record of all paid out creator withdrawals</p>
        </div>
        <span class="text-xs bg-amber-500/20 text-amber-300 font-bold px-3 py-1 rounded-full border border-amber-500/30">
          Master Payment Ledger
        </span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3.5 px-4">Request ID</th>
              <th class="py-3.5 px-4">Influencer Name</th>
              <th class="py-3.5 px-4">User ID</th>
              <th class="py-3.5 px-4">Paid Amount</th>
              <th class="py-3.5 px-4">UPI ID</th>
              <th class="py-3.5 px-4 text-right">Status</th>
            </tr>
          </thead>
          <tbody id="SettledPayoutsBody" class="divide-y divide-white/5 font-medium text-gray-300">
            <tr>
              <td colspan="6" class="py-6 text-center text-gray-400 text-xs font-medium">
                No past settled payouts recorded yet.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SECTION 3: MY INFLUENCERS LIST & CREDENTIALS -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-lg font-bold text-white tracking-tight">👥 Step 2: My Influencers List & Credentials</h2>
          <p class="text-xs text-gray-400 font-medium">Share User ID & Password with influencers so they can log in.</p>
        </div>
        <button type="button" onclick="openAddInfluencerModal()" class="bg-[#d4af37] text-black font-extrabold text-xs px-4 py-2 rounded-xl cursor-pointer hover:bg-amber-400 transition-all shadow-md">
          + Add New Influencer
        </button>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3.5 px-4">Influencer Name</th>
              <th class="py-3.5 px-4">User ID</th>
              <th class="py-3.5 px-4">Password</th>
              <th class="py-3.5 px-4">Promo Code</th>
              <th class="py-3.5 px-4">Commission %</th>
              <th class="py-3.5 px-4">Total Sales Brought</th>
              <th class="py-3.5 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody id="InfluencersTableBody" class="divide-y divide-white/5 font-medium text-gray-300">
            <tr id="EmptyInfluencerRow">
              <td colspan="7" class="py-10 text-center text-gray-400 text-xs font-medium space-y-2">
                <div class="text-amber-300 text-xl font-bold">✨</div>
                <div>No Influencers added yet. Click <strong class="text-amber-300 font-bold">'+ Add New Influencer'</strong> above to create your first User ID & Password!</div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- Modal 1: Add New Influencer Form -->
  <div id="AddInfluencerModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-md w-full p-6 shadow-2xl relative space-y-4">
      <button type="button" onclick="closeAddInfluencerModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 class="text-xl font-bold text-amber-300 tracking-tight">Add New Influencer</h3>
        <p class="text-xs text-gray-400 font-medium">Create User ID & Password to share with Influencer</p>
      </div>

      <form onsubmit="handleAddSubmit(event)" class="space-y-3 text-xs">
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Influencer Name</label>
          <input id="AddName" type="text" required placeholder="demo khan" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white focus:outline-none focus:border-[#d4af37]">
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">User ID</label>
            <input id="AddUserID" type="text" required placeholder="demobhai123" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono lowercase focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Password</label>
            <input id="AddPass" type="text" required placeholder="demo khan" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Promo Code</label>
            <input id="AddCode" type="text" required placeholder="DEMO10" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono uppercase focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Commission %</label>
            <input id="AddRate" type="number" value="15" min="5" max="30" required class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-sm py-3.5 rounded-2xl shadow-xl hover:brightness-110 transition-all cursor-pointer mt-2 tracking-wide uppercase">
          Save & Create Influencer
        </button>
      </form>
    </div>
  </div>

  <!-- Modal 2: View Sales Orders -->
  <div id="InspectSalesModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-xl w-full p-6 shadow-2xl relative space-y-4">
      <button type="button" onclick="closeInspectSalesModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 id="InspectTitle" class="text-xl font-bold text-amber-300 tracking-tight">Sales Brought By Influencer</h3>
        <p class="text-xs text-gray-400 font-medium">Orders placed using promo code <strong id="InspectCode" class="text-amber-300 font-mono">CODE</strong></p>
      </div>

      <div class="overflow-x-auto max-h-56">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-2.5 px-3">Order ID</th>
              <th class="py-2.5 px-3">Customer Name</th>
              <th class="py-2.5 px-3">Amount</th>
              <th class="py-2.5 px-3">Commission</th>
            </tr>
          </thead>
          <tbody id="InspectTableBody" class="divide-y divide-white/5 text-gray-300 font-medium">
            <tr>
              <td colspan="4" class="py-6 text-center text-gray-400">No orders recorded yet for this code.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="flex justify-end">
        <button type="button" onclick="closeInspectSalesModal()" class="bg-white/10 hover:bg-white/20 text-white font-bold text-xs px-4 py-2 rounded-xl cursor-pointer">Close</button>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div id="Toast" class="fixed bottom-6 right-6 z-50 bg-emerald-500 text-black font-extrabold text-xs px-5 py-3 rounded-2xl shadow-2xl transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none">
    <span id="ToastMsg">Success!</span>
  </div>

  <!-- Footer -->
  <footer class="bg-black border-t border-[#d4af37]/20 py-6 px-4 text-center text-xs text-gray-400 mt-12 font-medium">
    <p>&copy; 2026 BlackRoots Store Owner Panel. Shared Database Sync Active.</p>
  </footer>

  <script>
    function getAccountsDB() {
      const stored = localStorage.getItem('blackroots_accounts_db');
      if (stored) {
        try { return JSON.parse(stored); } catch(e) {}
      }
      return {};
    }

    function saveAccountsDB(db) {
      localStorage.setItem('blackroots_accounts_db', JSON.stringify(db));
    }

    function getPayoutsDB() {
      const stored = localStorage.getItem('blackroots_payouts_db');
      if (stored) {
        try { return JSON.parse(stored); } catch(e) {}
      }
      return [];
    }

    function savePayoutsDB(list) {
      localStorage.setItem('blackroots_payouts_db', JSON.stringify(list));
    }

    document.addEventListener('DOMContentLoaded', function() {
      renderTables();
    });

    function renderTables() {
      // 1. Render Influencers Table
      const infTable = document.getElementById('InfluencersTableBody');
      const statInf = document.getElementById('StatTotalInfluencers');
      const db = getAccountsDB();
      const userIds = Object.keys(db);

      if (userIds.length === 0) {
        infTable.innerHTML = `
          <tr id="EmptyInfluencerRow">
            <td colspan="7" class="py-10 text-center text-gray-400 text-xs font-medium space-y-2">
              <div class="text-amber-300 text-xl font-bold">✨</div>
              <div>No Influencers added yet. Click <strong class="text-amber-300 font-bold">'+ Add New Influencer'</strong> above to create your first User ID & Password!</div>
            </td>
          </tr>`;
        if (statInf) statInf.innerText = '0 Influencers';
      } else {
        if (statInf) statInf.innerText = `${userIds.length} Influencers`;
        infTable.innerHTML = userIds.map(uId => {
          const inf = db[uId];
          return `
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-bold text-white">${inf.name}</td>
              <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300">${uId}</td>
              <td class="py-3.5 px-4 font-mono text-gray-300 bg-white/5 px-2.5 py-1 rounded">${inf.pass}</td>
              <td class="py-3.5 px-4 font-mono font-bold text-amber-400">${inf.code}</td>
              <td class="py-3.5 px-4 font-bold text-emerald-400">${inf.rate}%</td>
              <td class="py-3.5 px-4 font-bold text-white">₹0.00</td>
              <td class="py-3.5 px-4 text-right space-x-1">
                <button type="button" onclick="deleteInfluencer('${uId}')" class="bg-red-500/20 text-red-300 hover:bg-red-500/40 border border-red-500/40 font-bold text-[10px] px-2.5 py-1 rounded-lg cursor-pointer">
                  Delete
                </button>
              </td>
            </tr>`;
        }).join('');
      }

      // 2. Render Pending Payouts Table
      const payoutsTable = document.getElementById('PayoutsTableBody');
      const payouts = getPayoutsDB();
      const statPayoutVal = document.getElementById('StatPendingPayouts');
      const statPayoutCnt = document.getElementById('StatPendingCount');
      const badgePayoutCnt = document.getElementById('BadgePendingCount');

      const pendingList = payouts.filter(p => p.status === 'Pending');

      if (pendingList.length === 0) {
        payoutsTable.innerHTML = `
          <tr id="EmptyPayoutRow">
            <td colspan="5" class="py-8 text-center text-gray-400 text-xs font-medium">
              ✨ No pending payout requests. All payouts are 100% settled!
            </td>
          </tr>`;
        if (statPayoutVal) statPayoutVal.innerText = '₹0.00';
        if (statPayoutCnt) statPayoutCnt.innerText = '0 Pending Payments';
        if (badgePayoutCnt) badgePayoutCnt.innerText = '0 Pending Payments';
      } else {
        let totalPendingSum = 0;
        payoutsTable.innerHTML = pendingList.map(p => {
          const numVal = parseFloat(p.amount.replace('₹','')) || 0;
          totalPendingSum += numVal;
          return `
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-bold text-white">${p.name}</td>
              <td class="py-3.5 px-4 font-mono text-amber-300">${p.userId}</td>
              <td class="py-3.5 px-4 font-extrabold text-emerald-400 text-sm">${p.amount}</td>
              <td class="py-3.5 px-4 font-mono text-amber-300 bg-white/5 px-2.5 py-1 rounded">${p.upi}</td>
              <td class="py-3.5 px-4 text-right">
                <button type="button" onclick="approvePayout('${p.id}', '${p.name}', '${p.amount}')" class="bg-emerald-500 hover:bg-emerald-400 text-black font-extrabold text-xs px-4 py-2 rounded-xl shadow-md transition-all cursor-pointer">
                  ✓ Mark Paid
                </button>
              </td>
            </tr>`;
        }).join('');
        if (statPayoutVal) statPayoutVal.innerText = `₹${totalPendingSum.toFixed(2)}`;
        if (statPayoutCnt) statPayoutCnt.innerText = `${pendingList.length} Pending Payments`;
        if (badgePayoutCnt) badgePayoutCnt.innerText = `${pendingList.length} Pending Payments`;
      }

      // 3. Render Settled Payouts History Table
      const settledTable = document.getElementById('SettledPayoutsBody');
      const paidList = payouts.filter(p => p.status === 'Paid');

      if (paidList.length === 0) {
        settledTable.innerHTML = `
          <tr>
            <td colspan="6" class="py-6 text-center text-gray-400 text-xs font-medium">
              No past settled payouts recorded yet.
            </td>
          </tr>`;
      } else {
        settledTable.innerHTML = paidList.map(p => `
          <tr class="hover:bg-white/5 transition-colors">
            <td class="py-3.5 px-4 font-mono text-amber-300 font-bold">${p.id}</td>
            <td class="py-3.5 px-4 font-bold text-white">${p.name}</td>
            <td class="py-3.5 px-4 font-mono text-amber-300">${p.userId}</td>
            <td class="py-3.5 px-4 font-extrabold text-emerald-400">${p.amount}</td>
            <td class="py-3.5 px-4 font-mono text-gray-300 bg-white/5 px-2 py-1 rounded">${p.upi}</td>
            <td class="py-3.5 px-4 text-right">
              <span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-3 py-1 rounded-full text-[10px] font-bold">✓ Paid & Settled</span>
            </td>
          </tr>
        `).join('');
      }
    }

    function approvePayout(payoutId, name, amount) {
      let payouts = getPayoutsDB();
      payouts = payouts.map(p => {
        if (p.id === payoutId) p.status = 'Paid';
        return p;
      });
      savePayoutsDB(payouts);
      renderTables();
      showToast(`Approved & Marked ${amount} Paid to ${name}! Settlement recorded.`);
    }

    function deleteInfluencer(uId) {
      const db = getAccountsDB();
      delete db[uId];
      saveAccountsDB(db);
      renderTables();
      showToast(`Deleted Creator Account ${uId}!`);
    }

    function showToast(msg) {
      const toast = document.getElementById('Toast');
      const toastMsg = document.getElementById('ToastMsg');
      if (toast && toastMsg) {
        toastMsg.innerText = msg;
        toast.classList.remove('translate-y-20', 'opacity-0');
        setTimeout(() => {
          toast.classList.add('translate-y-20', 'opacity-0');
        }, 2500);
      }
    }

    function openAddInfluencerModal() {
      const modal = document.getElementById('AddInfluencerModal');
      if (modal) modal.classList.remove('hidden'), modal.classList.add('flex');
    }

    function closeAddInfluencerModal() {
      const modal = document.getElementById('AddInfluencerModal');
      if (modal) modal.classList.add('hidden'), modal.classList.remove('flex');
    }

    function inspectSales(name, code) {
      const modal = document.getElementById('InspectSalesModal');
      const title = document.getElementById('InspectTitle');
      const codeEl = document.getElementById('InspectCode');
      if (title) title.innerText = `Sales Brought By ${name}`;
      if (codeEl) codeEl.innerText = code;
      if (modal) modal.classList.remove('hidden'), modal.classList.add('flex');
    }

    function closeInspectSalesModal() {
      const modal = document.getElementById('InspectSalesModal');
      if (modal) modal.classList.add('hidden'), modal.classList.remove('flex');
    }

    function handleAddSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('AddName').value.trim();
      const userId = document.getElementById('AddUserID').value.trim().toLowerCase();
      const pass = document.getElementById('AddPass').value.trim();
      const code = document.getElementById('AddCode').value.trim().toUpperCase();
      const rate = document.getElementById('AddRate').value;

      const db = getAccountsDB();
      db[userId] = { name, pass, code, rate, unpaid: 0, sales: 0, orders: 0 };
      saveAccountsDB(db);

      renderTables();
      closeAddInfluencerModal();
      showToast(`Influencer ${name} Saved! User ID: ${userId} | Password: ${pass}`);
    }
  </script>
</body>
</html>
"""

# Write to root, demo_lab, and preview directories
target_dirs = [
    r"c:\Users\moham\Downloads\blackroots website",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab",
    r"c:\Users\moham\Downloads\blackroots website\preview"
]

for d in target_dirs:
    if os.path.exists(d):
        with open(os.path.join(d, "influencer.html"), "w", encoding="utf-8") as f:
            f.write(influencer_html)
        with open(os.path.join(d, "admin-influencer.html"), "w", encoding="utf-8") as f:
            f.write(admin_html)
        print(f"REMOVED HEADER BADGE AND ADDED LIVE PAYOUT HISTORY TO: {d}")

