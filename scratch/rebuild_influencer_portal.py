import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"

influencer_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Creator & Influencer Portal &mdash; BlackRoots</title>
  <meta name="description" content="BlackRoots Official VIP Creator Login Portal. Access your assigned promo code, track live commission earnings, view payout history, and request payouts.">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brandDark: '#0a0b0e',
            brandCard: '#11141b',
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
  <link rel="stylesheet" href="./assets/theme.css?v=1786809224">
  <script src="./assets/theme.js?v=1786809224" defer></script>

  <!-- Mobile & Touch Responsive Style -->
  <style>
    @media (max-width: 768px) {
      input[type="text"],
      input[type="email"],
      input[type="number"],
      input[type="password"],
      select,
      textarea {
        font-size: 16px !important;
      }
      body {
        overflow-x: hidden;
      }
    }
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
    *, *::before, *::after, html, body, div, section {
      scrollbar-width: none !important;
      -ms-overflow-style: none !important;
      -webkit-overflow-scrolling: touch !important;
    }
    *::-webkit-scrollbar, html::-webkit-scrollbar, body::-webkit-scrollbar {
      display: none !important;
      width: 0px !important;
      height: 0px !important;
    }
    .glass-card {
      background: #11141b !important;
      border: 1px solid rgba(212, 175, 55, 0.45) !important;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7) !important;
    }
  </style>
</head>
<body class="bg-[#0a0b0e] text-white font-sans antialiased selection:bg-[#d4af37] selection:text-black min-h-screen flex flex-col justify-between">

  <!-- Top Announcement Bar -->
  <div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important;">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap whitespace-nowrap">
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        🤝 PARTNER
      </span>
      <span>Stop Hair Fall, Go Black &bull; Earn 15% Lifetime Commissions</span>
    </div>
  </div>

  <!-- Header -->
  <header class="sticky-header bg-[#0a0b0e]/95 backdrop-blur-xl border-b border-[#d4af37]/20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between gap-3">
      
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center gap-2.5 sm:gap-3 group shrink-0">
        <img src="./assets/blackroots-logo-circle-black.jpg" alt="BlackRoots Logo" class="w-9 h-9 sm:w-11 sm:h-11 rounded-full border border-[#d4af37] object-cover shadow-lg group-hover:scale-105 transition-transform">
        <div class="flex flex-col">
          <span class="font-serif text-lg sm:text-2xl font-bold tracking-wider text-white group-hover:text-[#d4af37] transition-colors uppercase whitespace-nowrap">BlackRoots</span>
          <span class="text-[8px] sm:text-[9px] uppercase tracking-[0.2em] text-[#d4af37] font-bold -mt-1 whitespace-nowrap">Creator Hub</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden lg:flex items-center gap-4 xl:gap-6">
        <a href="index.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors">Home</a>
        <a href="product.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors">Product (&#8377;499)</a>
        <a href="reviews.html" class="text-xs font-semibold text-gray-300 hover:text-[#d4af37] uppercase tracking-wider transition-colors">Reviews</a>
        <a href="admin-influencer.html" class="text-xs font-bold text-amber-300 bg-amber-500/10 border border-amber-500/30 px-3 py-1 rounded-full hover:bg-amber-400 hover:text-black transition-all">⚙️ Store Admin</a>
      </nav>

      <!-- Right Header Actions -->
      <div class="flex items-center gap-2">
        <a href="admin-influencer.html" class="inline-flex text-[10px] sm:text-xs font-bold text-amber-300 bg-amber-500/15 border border-amber-500/40 px-3 py-1.5 rounded-full hover:bg-amber-400 hover:text-black transition-all">
          ⚙️ Admin Panel
        </a>
        <button type="button" onclick="openMobileNavDrawer()" class="lg:hidden p-2 rounded-xl bg-black border border-[#d4af37]/60 text-amber-300" aria-label="Open Menu">
          <svg class="w-5 h-5 text-amber-300" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24">
            <line x1="4" y1="6" x2="20" y2="6"></line>
            <line x1="4" y1="12" x2="20" y2="12"></line>
            <line x1="4" y1="18" x2="20" y2="18"></line>
          </svg>
        </button>
      </div>

    </div>
  </header>

  <!-- ================= STATE 1: LOGIN GATE ================= -->
  <section id="LoginGateSection" class="max-w-md mx-auto px-4 py-8 sm:py-12 w-full my-auto space-y-6">
    <div class="p-6 sm:p-8 rounded-3xl glass-card relative overflow-hidden space-y-6">
      
      <div class="text-center space-y-2 relative z-10">
        <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-[#123824] to-[#d4af37]/40 border border-[#d4af37]/60 flex items-center justify-center mx-auto text-amber-300 text-2xl font-bold shadow-lg">
          🔑
        </div>
        <h1 class="text-2xl font-black text-white tracking-tight">Creator Portal Login</h1>
        <p class="text-xs text-gray-400 font-medium">Enter your assigned User ID & Password to access your live commissions & coupon code.</p>
      </div>

      <!-- Quick Demo Credentials Pill -->
      <div class="p-3 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-1 text-center">
        <span class="text-[10px] text-gray-400 block uppercase font-bold tracking-wider">Demo Creator Credentials:</span>
        <div class="flex items-center justify-center gap-2 font-mono text-amber-300 font-bold">
          <span>User: <strong class="text-white">rohit_fit</strong></span>
          <span>&bull;</span>
          <span>Pass: <strong class="text-white">blackroots2026</strong></span>
        </div>
        <button type="button" onclick="fillDemoCredentials()" class="text-[10px] text-emerald-400 hover:underline font-bold pt-1 inline-block">
          ⚡ 1-Click Auto Fill Demo Login
        </button>
      </div>

      <!-- Login Form -->
      <form onsubmit="handleLoginSubmit(event)" class="space-y-4 text-xs relative z-10">
        <div id="LoginErrorBanner" class="p-3.5 rounded-xl bg-red-500/20 border border-red-500/40 text-red-300 text-xs font-semibold hidden">
          ⚠️ Invalid User ID or Password! Please check credentials or contact Store Admin.
        </div>

        <div class="space-y-1.5">
          <label class="font-bold text-amber-300 uppercase tracking-wider block text-[11px]">Assigned User ID</label>
          <input id="LoginUserID" type="text" required placeholder="e.g. rohit_fit" class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-mono text-sm focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-all">
        </div>

        <div class="space-y-1.5">
          <label class="font-bold text-amber-300 uppercase tracking-wider block text-[11px]">Password</label>
          <div class="relative flex items-center">
            <input id="LoginPassword" type="password" required placeholder="••••••••" class="w-full bg-black border border-white/20 rounded-xl p-3.5 pr-10 text-white font-mono text-sm focus:outline-none focus:border-[#d4af37] focus:ring-1 focus:ring-[#d4af37] transition-all">
            <button type="button" onclick="togglePasswordVisibility()" class="absolute right-3 text-gray-400 hover:text-amber-300 text-sm cursor-pointer p-1" title="Show/Hide Password">
              👁️
            </button>
          </div>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-sm py-4 rounded-xl shadow-xl hover:brightness-110 active:scale-95 transition-all cursor-pointer tracking-wider uppercase mt-2">
          Unlock Creator Dashboard &rarr;
        </button>
      </form>

      <div class="text-center pt-3 border-t border-white/10 text-[11px] text-gray-400">
        Need creator access? <a href="https://wa.me/919580835179?text=Hello%20BlackRoots%20Admin%2C%20I%20want%20to%20join%20the%20Creator%20Affiliate%20Program" target="_blank" class="text-amber-300 font-bold hover:underline">Apply via WhatsApp Support &rarr;</a>
      </div>
    </div>
  </section>

  <!-- ================= STATE 2: AUTHENTICATED DASHBOARD ================= -->
  <main id="DashboardSection" class="hidden max-w-5xl mx-auto px-4 sm:px-6 py-6 sm:py-8 w-full space-y-6">

    <!-- Top Creator Welcome Header -->
    <div class="p-5 sm:p-6 rounded-3xl glass-card flex flex-col sm:flex-row sm:items-center justify-between gap-4">
      <div class="flex items-center gap-3.5">
        <div class="w-14 h-14 sm:w-16 sm:h-16 rounded-2xl bg-gradient-to-tr from-[#123824] to-[#d4af37]/40 border-2 border-[#d4af37] p-1 flex items-center justify-center text-2xl shadow-xl shrink-0">
          👑
        </div>
        <div>
          <div class="flex items-center gap-2 flex-wrap">
            <h1 id="DashCreatorName" class="text-lg sm:text-2xl font-black text-white tracking-tight">Rohit Verma</h1>
            <span class="text-[9px] font-black uppercase bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 px-2 py-0.5 rounded-full tracking-wider">
              ACTIVE CREATOR
            </span>
          </div>
          <p class="text-xs text-gray-400 mt-0.5">
            User ID: <strong id="DashUserID" class="text-amber-300 font-mono">rohit_fit</strong> &bull; <span class="text-emerald-400 font-bold"><span id="DashCommissionRate">15</span>% Commission</span>
          </p>
        </div>
      </div>

      <div class="flex items-center gap-2 self-end sm:self-center">
        <button type="button" onclick="handleLogout()" class="text-xs bg-white/10 hover:bg-white/20 text-gray-300 px-3.5 py-2 rounded-xl font-bold transition-all">
          🚪 Logout
        </button>
      </div>
    </div>

    <!-- 3 Core KPI Metric Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3.5">
      
      <!-- KPI 1: Total Sales -->
      <div class="p-4 sm:p-5 rounded-2xl glass-card space-y-1">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Total Sales Brought</span>
          <span class="text-base">🛍️</span>
        </div>
        <div id="DashTotalSalesVal" class="text-2xl sm:text-3xl font-black text-white">₹3,493</div>
        <p class="text-[11px] text-gray-400"><strong id="DashTotalOrdersCount" class="text-amber-300">7</strong> Orders Generated</p>
      </div>

      <!-- KPI 2: Total Commission Earned -->
      <div class="p-4 sm:p-5 rounded-2xl glass-card space-y-1">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Commission Earned</span>
          <span class="text-base">💎</span>
        </div>
        <div id="DashEarnedVal" class="text-2xl sm:text-3xl font-black text-amber-300">₹524</div>
        <p class="text-[11px] text-emerald-400 font-semibold">15% of all orders</p>
      </div>

      <!-- KPI 3: Unpaid Balance & Payout CTA -->
      <div class="p-4 sm:p-5 rounded-2xl glass-card space-y-2 border-emerald-500/40 bg-emerald-950/20">
        <div class="flex items-center justify-between text-emerald-300 text-xs font-bold uppercase tracking-wider">
          <span>Available Wallet Balance</span>
          <span class="text-base">💸</span>
        </div>
        <div id="DashBalanceVal" class="text-2xl sm:text-3xl font-black text-emerald-400">₹524</div>
        
        <button type="button" onclick="openPayoutModal()" class="w-full bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 hover:to-emerald-500 text-black font-black text-xs py-2.5 rounded-xl shadow-lg transition-all uppercase tracking-wider active:scale-95">
          Request UPI Payout &rarr;
        </button>
      </div>

    </div>

    <!-- 1-Click Promotional Tools: Coupon Code & Direct Link -->
    <div class="p-5 sm:p-6 rounded-3xl glass-card space-y-4">
      <h2 class="text-sm font-black text-amber-300 uppercase tracking-wider flex items-center gap-2">
        <span>🚀</span> <span>Your 1-Click Creator Sharing Tools</span>
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        
        <!-- Promo Code Box -->
        <div class="p-4 rounded-2xl bg-black border border-white/10 space-y-2">
          <span class="text-[11px] font-bold text-gray-400 uppercase block">Your 10% Discount Promo Code</span>
          <div class="flex items-center justify-between gap-2 p-2 bg-[#12151c] rounded-xl border border-[#d4af37]/40">
            <span id="DashPromoCode" class="font-mono text-base font-black text-amber-300 tracking-wider px-2">ROHIT10</span>
            <button type="button" onclick="copyPromoCode()" class="bg-[#d4af37] hover:bg-amber-300 text-black font-black text-xs px-4 py-2 rounded-lg transition-all active:scale-95">
              Copy Code
            </button>
          </div>
          <p class="text-[10px] text-gray-400">Followers get 10% OFF at checkout &bull; You get 15% commission!</p>
        </div>

        <!-- Direct Referral Link Box -->
        <div class="p-4 rounded-2xl bg-black border border-white/10 space-y-2">
          <span class="text-[11px] font-bold text-gray-400 uppercase block">Direct Shopping Referral Link</span>
          <div class="flex items-center justify-between gap-2 p-2 bg-[#12151c] rounded-xl border border-white/10">
            <input id="DashRefLink" type="text" readonly value="https://blackroots.in/?ref=ROHIT10" class="bg-transparent font-mono text-xs text-gray-300 px-2 w-full focus:outline-none truncate">
            <button type="button" onclick="copyRefLink()" class="bg-white/10 hover:bg-white/20 text-white font-bold text-xs px-4 py-2 rounded-lg transition-all active:scale-95 shrink-0">
              Copy Link
            </button>
          </div>
          <p class="text-[10px] text-gray-400">Share this link directly in Instagram Bio or YouTube Description.</p>
        </div>

      </div>
    </div>

    <!-- Recent Order Commissions Ledger -->
    <div class="p-5 sm:p-6 rounded-3xl glass-card space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-sm sm:text-base font-bold text-white tracking-tight">Recent Order Commissions</h2>
          <p class="text-xs text-gray-400">Live automatic breakdown of sales driven by your code</p>
        </div>
        <span class="text-[10px] font-mono bg-amber-400/20 text-amber-300 px-2.5 py-1 rounded-full border border-amber-400/30">
          LIVE LEDGER
        </span>
      </div>

      <!-- Mobile Cards / Desktop Table Container -->
      <div id="SalesCardsContainer" class="space-y-2.5">
        <!-- Injected dynamically -->
      </div>
    </div>

    <!-- Payout Withdrawal History -->
    <div class="p-5 sm:p-6 rounded-3xl glass-card space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-sm sm:text-base font-bold text-white tracking-tight">My UPI Payout History</h2>
          <p class="text-xs text-gray-400">History of your withdrawal requests and settlements</p>
        </div>
      </div>

      <div id="PayoutsCardsContainer" class="space-y-2.5">
        <!-- Injected dynamically -->
      </div>
    </div>

  </main>

  <!-- Payout Modal -->
  <div id="PayoutModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#11141b] border-2 border-[#d4af37]/60 rounded-3xl max-w-md w-full p-6 shadow-2xl relative space-y-5">
      <button type="button" onclick="closePayoutModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 class="text-xl font-black text-amber-300 tracking-tight">Request UPI Payout</h3>
        <p class="text-xs text-gray-300">Available Wallet Balance: <strong id="ModalBalanceText" class="text-emerald-400 font-black">₹524</strong></p>
      </div>

      <form onsubmit="handlePayoutSubmit(event)" class="space-y-4 text-xs">
        <div>
          <label class="font-bold text-amber-300 uppercase tracking-wider block mb-1.5">Requested Amount (₹)</label>
          <input id="PayoutAmount" type="number" value="500" min="100" required class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-mono text-base font-black focus:outline-none focus:border-[#d4af37]">
        </div>

        <div>
          <label class="font-bold text-amber-300 uppercase tracking-wider block mb-1.5">Enter Your UPI ID (GPay / PhonePe / Paytm)</label>
          <input id="PayoutUPI" type="text" placeholder="e.g. 9876543210@paytm or rohit@okhdfcbank" required class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-mono text-sm focus:outline-none focus:border-[#d4af37]">
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-emerald-500 to-emerald-600 text-black font-black text-sm py-4 rounded-xl shadow-xl hover:brightness-110 active:scale-95 transition-all uppercase tracking-wider cursor-pointer">
          Submit Payout Request &rarr;
        </button>
      </form>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="Toast" class="fixed bottom-6 right-6 z-50 bg-[#d4af37] text-black font-black text-xs px-5 py-3 rounded-2xl shadow-2xl transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none flex items-center gap-2">
    <span id="ToastMsg">Copied!</span>
  </div>

  <!-- Mobile Drawer -->
  <div id="MobileNavBackdrop" onclick="closeMobileNavDrawer()" class="fixed inset-0 bg-black/80 backdrop-blur-md z-50 opacity-0 pointer-events-none transition-opacity duration-300"></div>
  <div id="MobileNavDrawer" class="fixed top-0 right-0 bottom-0 w-[85%] max-w-sm bg-[#0e1017] border-l border-[#d4af37]/30 z-50 shadow-2xl transform translate-x-full transition-transform duration-300 p-5 space-y-4">
    <div class="flex items-center justify-between border-b border-white/10 pb-4">
      <span class="font-serif font-bold text-white text-lg uppercase">BlackRoots</span>
      <button type="button" onclick="closeMobileNavDrawer()" class="text-amber-300 font-bold">✕</button>
    </div>
    <div class="space-y-2 text-xs uppercase font-bold">
      <a href="index.html" class="block p-3 rounded-xl hover:bg-white/5 text-gray-300">Home</a>
      <a href="product.html" class="block p-3 rounded-xl hover:bg-white/5 text-gray-300">Product (&#8377;499)</a>
      <a href="reviews.html" class="block p-3 rounded-xl hover:bg-white/5 text-gray-300">Reviews</a>
      <a href="admin-influencer.html" class="block p-3 rounded-xl bg-amber-500/10 text-amber-300">⚙️ Store Admin</a>
    </div>
  </div>

  <!-- Unified Database & Portal Logic Engine -->
  <script>
    // Shared Master Database Initializer
    function getMasterDB() {
      const defaultDB = {
        "rohit_fit": {
          name: "Rohit Verma",
          pass: "blackroots2026",
          code: "ROHIT10",
          rate: 15,
          sales: 3493,
          orders: 7,
          earned: 524,
          paid: 0,
          balance: 524,
          date: "15 Aug 2026",
          salesList: [
            { id: "BR-9012", date: "15 Aug 2026", customer: "Aman S.", amount: 499, commission: 75 },
            { id: "BR-9018", date: "15 Aug 2026", customer: "Pooja K.", amount: 799, commission: 120 },
            { id: "BR-9024", date: "14 Aug 2026", customer: "Vikram R.", amount: 499, commission: 75 },
            { id: "BR-9031", date: "14 Aug 2026", customer: "Neha M.", amount: 499, commission: 75 }
          ]
        },
        "priya_hair": {
          name: "Priya Sharma",
          pass: "priya2026",
          code: "PRIYA15",
          rate: 15,
          sales: 1996,
          orders: 4,
          earned: 299,
          paid: 0,
          balance: 299,
          date: "14 Aug 2026",
          salesList: [
            { id: "BR-8821", date: "14 Aug 2026", customer: "Deepak M.", amount: 499, commission: 75 },
            { id: "BR-8829", date: "13 Aug 2026", customer: "Simran G.", amount: 499, commission: 75 }
          ]
        }
      };

      const raw = localStorage.getItem('blackroots_influencers_master_db');
      if (!raw) {
        localStorage.setItem('blackroots_influencers_master_db', JSON.stringify(defaultDB));
        return defaultDB;
      }
      try {
        return JSON.parse(raw);
      } catch (e) {
        return defaultDB;
      }
    }

    function saveMasterDB(db) {
      localStorage.setItem('blackroots_influencers_master_db', JSON.stringify(db));
    }

    function getPayoutsDB() {
      const raw = localStorage.getItem('blackroots_payouts_master_db');
      if (!raw) {
        const defaultPayouts = [
          { id: "PAY-1001", userId: "rohit_fit", name: "Rohit Verma", amount: 500, upi: "rohit@okhdfcbank", date: "15 Aug 2026", status: "Pending" }
        ];
        localStorage.setItem('blackroots_payouts_master_db', JSON.stringify(defaultPayouts));
        return defaultPayouts;
      }
      try { return JSON.parse(raw); } catch (e) { return []; }
    }

    function savePayoutsDB(list) {
      localStorage.setItem('blackroots_payouts_master_db', JSON.stringify(list));
    }

    let currentLoggedInUser = null;

    document.addEventListener('DOMContentLoaded', function() {
      // Check if session is already active
      const savedSession = sessionStorage.getItem('blackroots_active_creator_session');
      if (savedSession) {
        const db = getMasterDB();
        if (db[savedSession]) {
          renderCreatorDashboard(savedSession);
          return;
        }
      }
    });

    function fillDemoCredentials() {
      document.getElementById('LoginUserID').value = 'rohit_fit';
      document.getElementById('LoginPassword').value = 'blackroots2026';
    }

    function togglePasswordVisibility() {
      const pInput = document.getElementById('LoginPassword');
      if (pInput.type === 'password') {
        pInput.type = 'text';
      } else {
        pInput.type = 'password';
      }
    }

    function handleLoginSubmit(e) {
      e.preventDefault();
      const uId = document.getElementById('LoginUserID').value.trim().toLowerCase();
      const pass = document.getElementById('LoginPassword').value.trim();
      const errBanner = document.getElementById('LoginErrorBanner');

      const db = getMasterDB();
      if (db[uId] && db[uId].pass === pass) {
        if (errBanner) errBanner.classList.add('hidden');
        sessionStorage.setItem('blackroots_active_creator_session', uId);
        renderCreatorDashboard(uId);
      } else {
        if (errBanner) {
          errBanner.classList.remove('hidden');
          errBanner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }
    }

    function renderCreatorDashboard(uId) {
      currentLoggedInUser = uId;
      const db = getMasterDB();
      const creator = db[uId];
      if (!creator) return;

      document.getElementById('LoginGateSection').classList.add('hidden');
      document.getElementById('DashboardSection').classList.remove('hidden');

      // Populate Headers & Metrics
      document.getElementById('DashCreatorName').textContent = creator.name;
      document.getElementById('DashUserID').textContent = uId;
      document.getElementById('DashCommissionRate').textContent = creator.rate || 15;
      document.getElementById('DashTotalSalesVal').textContent = '₹' + Number(creator.sales || 0).toLocaleString('en-IN');
      document.getElementById('DashTotalOrdersCount').textContent = creator.orders || 0;
      document.getElementById('DashEarnedVal').textContent = '₹' + Number(creator.earned || 0).toLocaleString('en-IN');
      document.getElementById('DashBalanceVal').textContent = '₹' + Number(creator.balance || 0).toLocaleString('en-IN');
      
      // Promo Tools
      document.getElementById('DashPromoCode').textContent = creator.code;
      document.getElementById('DashRefLink').value = `https://blackroots.in/?ref=${creator.code}`;

      // Render Sales Cards
      const salesContainer = document.getElementById('SalesCardsContainer');
      const salesList = creator.salesList || [];
      if (salesList.length === 0) {
        salesContainer.innerHTML = `
          <div class="p-6 text-center text-gray-400 text-xs bg-black/40 rounded-2xl border border-white/5">
            ✨ No sales recorded yet. Share your code <strong>${creator.code}</strong> to start earning!
          </div>`;
      } else {
        salesContainer.innerHTML = salesList.map(s => `
          <div class="p-3.5 rounded-2xl bg-black border border-white/10 flex items-center justify-between text-xs gap-3">
            <div class="space-y-0.5">
              <div class="flex items-center gap-2">
                <span class="font-mono font-bold text-white">${s.id}</span>
                <span class="text-[10px] text-gray-400">&bull; ${s.date}</span>
              </div>
              <p class="text-[11px] text-gray-300">Customer: <strong>${s.customer}</strong> &bull; Total: <strong>₹${s.amount}</strong></p>
            </div>
            <div class="text-right shrink-0">
              <span class="text-xs font-black text-emerald-400 block">+₹${s.commission}</span>
              <span class="text-[9px] uppercase font-bold text-emerald-500 bg-emerald-500/10 px-2 py-0.5 rounded-full">Credited</span>
            </div>
          </div>
        `).join('');
      }

      // Render Payouts
      renderPayoutsList(uId);
    }

    function renderPayoutsList(uId) {
      const payoutsContainer = document.getElementById('PayoutsCardsContainer');
      const allPayouts = getPayoutsDB();
      const myPayouts = allPayouts.filter(p => p.userId === uId);

      if (myPayouts.length === 0) {
        payoutsContainer.innerHTML = `
          <div class="p-6 text-center text-gray-400 text-xs bg-black/40 rounded-2xl border border-white/5">
            No payout requests submitted yet.
          </div>`;
      } else {
        payoutsContainer.innerHTML = myPayouts.map(p => `
          <div class="p-3.5 rounded-2xl bg-black border border-white/10 flex items-center justify-between text-xs gap-3">
            <div class="space-y-0.5">
              <div class="flex items-center gap-2">
                <span class="font-mono font-bold text-amber-300">${p.id}</span>
                <span class="text-[10px] text-gray-400">&bull; ${p.date}</span>
              </div>
              <p class="text-[11px] text-gray-300 font-mono">UPI: ${p.upi}</p>
            </div>
            <div class="text-right shrink-0">
              <span class="text-sm font-black text-white block">₹${p.amount}</span>
              <span class="text-[9px] uppercase font-bold px-2 py-0.5 rounded-full ${p.status === 'Settled' ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40' : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'}">
                ${p.status}
              </span>
            </div>
          </div>
        `).join('');
      }
    }

    function copyPromoCode() {
      const code = document.getElementById('DashPromoCode').textContent.trim();
      navigator.clipboard.writeText(code);
      showToast(`Copied Promo Code: ${code}!`);
    }

    function copyRefLink() {
      const link = document.getElementById('DashRefLink').value.trim();
      navigator.clipboard.writeText(link);
      showToast(`Copied Referral Link!`);
    }

    function showToast(msg) {
      const toast = document.getElementById('Toast');
      const toastMsg = document.getElementById('ToastMsg');
      if (!toast || !toastMsg) return;

      toastMsg.textContent = msg;
      toast.classList.remove('translate-y-20', 'opacity-0');
      toast.classList.add('translate-y-0', 'opacity-100');

      setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-20', 'opacity-0');
      }, 2500);
    }

    function openPayoutModal() {
      const db = getMasterDB();
      const creator = db[currentLoggedInUser];
      if (!creator) return;

      document.getElementById('ModalBalanceText').textContent = '₹' + (creator.balance || 0);
      document.getElementById('PayoutAmount').value = Math.max(100, creator.balance || 100);
      document.getElementById('PayoutModal').classList.remove('hidden');
      document.getElementById('PayoutModal').classList.add('flex');
    }

    function closePayoutModal() {
      document.getElementById('PayoutModal').classList.add('hidden');
      document.getElementById('PayoutModal').classList.remove('flex');
    }

    function handlePayoutSubmit(e) {
      e.preventDefault();
      const amount = Number(document.getElementById('PayoutAmount').value);
      const upi = document.getElementById('PayoutUPI').value.trim();

      const db = getMasterDB();
      const creator = db[currentLoggedInUser];
      if (!creator) return;

      if (amount <= 0 || amount > creator.balance) {
        alert('Invalid amount! You cannot request more than your available wallet balance.');
        return;
      }

      // Deduct balance and record payout
      creator.balance -= amount;
      saveMasterDB(db);

      const payouts = getPayoutsDB();
      payouts.unshift({
        id: 'PAY-' + Math.floor(1000 + Math.random() * 9000),
        userId: currentLoggedInUser,
        name: creator.name,
        amount: amount,
        upi: upi,
        date: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }),
        status: 'Pending'
      });
      savePayoutsDB(payouts);

      closePayoutModal();
      renderCreatorDashboard(currentLoggedInUser);
      showToast('Payout request submitted to Store Owner!');
    }

    function handleLogout() {
      sessionStorage.removeItem('blackroots_active_creator_session');
      window.location.reload();
    }
  </script>

</body>
</html>
"""

with open(os.path.join(root_dir, "influencer.html"), "w", encoding="utf-8") as f:
    f.write(influencer_html)
print("Updated influencer.html")
