import os

# 1. BUILD INFLUENCER PORTAL (influencer.html)
influencer_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Influencer Partner Portal &mdash; BlackRoots Herbal Hair Dye Shampoo</title>
  <meta name="description" content="BlackRoots Influencer & Affiliate Partner Dashboard. Track sales, discount codes, commission earnings, and request instant payouts.">
  
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
            serif: ['Cormorant Garamond', 'Georgia', 'serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
          }
        }
      }
    }
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./assets/theme.css">
  <script src="./assets/theme.js" defer></script>
</head>
<body class="bg-[#0a0b0e] text-white font-sans antialiased selection:bg-[#d4af37] selection:text-black min-h-screen flex flex-col justify-between">

  <!-- Top Announcement Bar -->
  <div class="bg-gradient-to-r from-[#123824] via-[#0d2a1c] to-[#123824] text-[#f5e4ab] border-b border-[#d4af37]/30 py-2 px-4 text-center text-xs md:text-sm font-semibold tracking-wide">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-3 flex-wrap">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-bold text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
          PARTNER PROGRAM
        </span>
        <span>Earn up to 15% Commission + Give 10% OFF to Followers</span>
      </div>
      <a href="./index.html" class="text-xs text-amber-300 underline hover:text-white transition-colors">Back to Main Store &rarr;</a>
    </div>
  </div>

  <!-- Header / Navigation Bar -->
  <header class="sticky top-0 z-50 bg-[#0a0b0e]/90 backdrop-blur-xl border-b border-[#d4af37]/20 py-3.5 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <a href="./index.html" class="flex items-center gap-2 no-underline">
        <span class="font-serif text-2xl sm:text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-[#d4af37] to-amber-500 tracking-wider">BlackRoots</span>
        <span class="text-[10px] uppercase font-bold text-amber-300 bg-amber-500/20 px-2 py-0.5 rounded-full border border-amber-500/30">VIP CREATOR</span>
      </a>

      <div class="flex items-center gap-3">
        <a href="./admin-influencer.html" class="hidden sm:inline-flex text-xs font-bold text-gray-400 hover:text-amber-300 border border-white/10 hover:border-amber-400/50 px-3.5 py-1.5 rounded-full transition-all no-underline">
          👑 Store Admin Panel
        </a>
        <button type="button" onclick="toggleAuthModal()" class="bg-[#d4af37] hover:bg-amber-400 text-black font-extrabold text-xs px-4 py-2 rounded-full shadow-lg transition-all transform hover:scale-105 cursor-pointer">
          Login / Register
        </button>
      </div>
    </div>
  </header>

  <!-- Main Portal Body -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">

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
              <h1 class="text-xl sm:text-3xl font-extrabold text-white font-serif tracking-wide">Priya Sharma</h1>
              <span class="text-[10px] font-extrabold uppercase bg-amber-500/20 text-amber-300 border border-amber-500/40 px-2.5 py-0.5 rounded-full">GOLD CREATOR</span>
            </div>
            <p class="text-xs sm:text-sm text-gray-400 mt-1">@priya_beauty_lifestyle &bull; <span class="text-emerald-400 font-semibold">15% Commission Rate</span></p>
          </div>
        </div>

        <div class="flex items-center gap-3">
          <button type="button" onclick="openPayoutModal()" class="w-full md:w-auto bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-xs sm:text-sm px-6 py-3 rounded-2xl shadow-xl hover:brightness-110 transition-all flex items-center justify-center gap-2 cursor-pointer">
            <span>💸 Request Payout (₹4,890)</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Key Performance Indicators (KPI Cards Grid) -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      
      <!-- Card 1: Total Sales Driven -->
      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-2">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Total Sales Driven</span>
          <span class="text-amber-400 text-base">🛍️</span>
        </div>
        <div class="text-2xl sm:text-3xl font-extrabold text-white font-serif">₹48,900.00</div>
        <p class="text-[11px] text-emerald-400 font-semibold flex items-center gap-1">
          <span>↑ 24% this month</span>
        </p>
      </div>

      <!-- Card 2: Total Orders Referred -->
      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-2">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Orders Referred</span>
          <span class="text-amber-400 text-base">📦</span>
        </div>
        <div class="text-2xl sm:text-3xl font-extrabold text-white font-serif">38 Orders</div>
        <p class="text-[11px] text-gray-400">Avg. Order Value: ₹1,286</p>
      </div>

      <!-- Card 3: Total Earnings (15%) -->
      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-2">
        <div class="flex items-center justify-between text-gray-400 text-xs font-bold uppercase tracking-wider">
          <span>Total Earnings</span>
          <span class="text-amber-400 text-base">💰</span>
        </div>
        <div class="text-2xl sm:text-3xl font-extrabold text-amber-300 font-serif">₹7,335.00</div>
        <p class="text-[11px] text-gray-400">₹2,445 Paid Out</p>
      </div>

      <!-- Card 4: Available for Withdrawal -->
      <div class="p-5 rounded-2xl glass-panel-luxury border-2 border-emerald-500/40 bg-[#123824]/30 shadow-xl space-y-2 relative overflow-hidden">
        <div class="flex items-center justify-between text-emerald-300 text-xs font-bold uppercase tracking-wider">
          <span>Unpaid Balance</span>
          <span class="text-emerald-400 text-base">💳</span>
        </div>
        <div class="text-2xl sm:text-3xl font-extrabold text-emerald-400 font-serif">₹4,890.00</div>
        <p class="text-[11px] text-emerald-300 font-semibold">Ready for Withdrawal</p>
      </div>

    </div>

    <!-- Referral Code & Share Link Generator Box -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-white/10 pb-4">
        <div>
          <h2 class="text-lg font-bold text-white font-serif">Your Unique Coupon Code & Link</h2>
          <p class="text-xs text-gray-400">Share this code with your followers. They get 10% OFF & you earn 15% Commission on every sale!</p>
        </div>
        <span class="text-xs bg-amber-500/20 text-amber-300 font-bold px-3 py-1 rounded-full border border-amber-500/30 self-start sm:self-auto">
          ⚡ Active & Verified
        </span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        
        <!-- Code Copy Box -->
        <div class="space-y-2">
          <label class="text-xs font-bold text-gray-300 uppercase tracking-wider block">Your Promo Code (10% OFF For Followers)</label>
          <div class="flex items-center gap-2 bg-[#0a0b0e] border-2 border-[#d4af37]/60 rounded-2xl p-2 shadow-inner">
            <span class="font-mono text-lg font-extrabold text-amber-300 px-3 tracking-widest uppercase">PRIYA10</span>
            <button type="button" onclick="copyToClipboard('PRIYA10', 'Promo Code Copied!')" class="ml-auto bg-[#d4af37] hover:bg-amber-400 text-black font-extrabold text-xs px-4 py-2 rounded-xl transition-all shadow-md cursor-pointer">
              Copy Code
            </button>
          </div>
        </div>

        <!-- Direct Link Copy Box -->
        <div class="space-y-2">
          <label class="text-xs font-bold text-gray-300 uppercase tracking-wider block">Direct Shopping Referral Link</label>
          <div class="flex items-center gap-2 bg-[#0a0b0e] border border-white/10 rounded-2xl p-2 shadow-inner">
            <input id="RefLinkInput" type="text" readonly value="https://blackroots.in/?ref=PRIYA10" class="bg-transparent text-xs text-gray-300 font-mono px-3 w-full focus:outline-none">
            <button type="button" onclick="copyToClipboard('https://blackroots.in/?ref=PRIYA10', 'Referral Link Copied!')" class="ml-auto bg-white/10 hover:bg-white/20 text-white font-bold text-xs px-4 py-2 rounded-xl transition-all cursor-pointer">
              Copy Link
            </button>
          </div>
        </div>

      </div>
    </div>

    <!-- Live Sales & Commission Ledger Table -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 class="text-lg font-bold text-white font-serif">Referral Sales & Commission History</h2>
          <p class="text-xs text-gray-400">Real-time ledger of orders completed using your code PRIYA10</p>
        </div>
        <div class="flex items-center gap-2">
          <input type="text" placeholder="Search order ID..." class="bg-[#0a0b0e] border border-white/10 text-xs px-3.5 py-2 rounded-xl text-white focus:outline-none focus:border-[#d4af37]">
        </div>
      </div>

      <!-- Responsive Table -->
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3.5 px-4 rounded-l-xl">Order ID</th>
              <th class="py-3.5 px-4">Date</th>
              <th class="py-3.5 px-4">Customer</th>
              <th class="py-3.5 px-4">Order Value</th>
              <th class="py-3.5 px-4">Discount</th>
              <th class="py-3.5 px-4">Your Commission (15%)</th>
              <th class="py-3.5 px-4 rounded-r-xl">Status</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5 font-medium text-gray-300">
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-mono font-bold text-amber-300">#BR-8921</td>
              <td class="py-3.5 px-4">Today, 06:42 PM</td>
              <td class="py-3.5 px-4 font-semibold text-white">Rahul Mehta</td>
              <td class="py-3.5 px-4">₹1,598.00 (2 Bottles)</td>
              <td class="py-3.5 px-4 text-emerald-400">-₹160.00</td>
              <td class="py-3.5 px-4 font-extrabold text-amber-300">₹239.70</td>
              <td class="py-3.5 px-4"><span class="bg-amber-500/20 text-amber-300 border border-amber-500/30 px-2.5 py-0.5 rounded-full text-[10px] font-bold">Unpaid</span></td>
            </tr>
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-mono font-bold text-amber-300">#BR-8904</td>
              <td class="py-3.5 px-4">Yesterday, 02:15 PM</td>
              <td class="py-3.5 px-4 font-semibold text-white">Ananya Verma</td>
              <td class="py-3.5 px-4">₹799.00 (1 Bottle)</td>
              <td class="py-3.5 px-4 text-emerald-400">-₹80.00</td>
              <td class="py-3.5 px-4 font-extrabold text-amber-300">₹119.85</td>
              <td class="py-3.5 px-4"><span class="bg-amber-500/20 text-amber-300 border border-amber-500/30 px-2.5 py-0.5 rounded-full text-[10px] font-bold">Unpaid</span></td>
            </tr>
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-mono font-bold text-amber-300">#BR-8872</td>
              <td class="py-3.5 px-4">11 Aug 2026</td>
              <td class="py-3.5 px-4 font-semibold text-white">Vikram Malhotra</td>
              <td class="py-3.5 px-4">₹2,397.00 (3 Bottles)</td>
              <td class="py-3.5 px-4 text-emerald-400">-₹240.00</td>
              <td class="py-3.5 px-4 font-extrabold text-amber-300">₹359.55</td>
              <td class="py-3.5 px-4"><span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2.5 py-0.5 rounded-full text-[10px] font-bold">Paid</span></td>
            </tr>
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-mono font-bold text-amber-300">#BR-8810</td>
              <td class="py-3.5 px-4">09 Aug 2026</td>
              <td class="py-3.5 px-4 font-semibold text-white">Neha Kapoor</td>
              <td class="py-3.5 px-4">₹1,598.00 (2 Bottles)</td>
              <td class="py-3.5 px-4 text-emerald-400">-₹160.00</td>
              <td class="py-3.5 px-4 font-extrabold text-amber-300">₹239.70</td>
              <td class="py-3.5 px-4"><span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2.5 py-0.5 rounded-full text-[10px] font-bold">Paid</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Creator Resources & Media Kit Box -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-gradient-to-r from-[#12151c] via-[#0d2a1c] to-[#12151c] shadow-2xl flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="space-y-1">
        <h3 class="text-base font-bold text-white font-serif">🎬 Creator Marketing Assets & Reels Kit</h3>
        <p class="text-xs text-gray-300">Download high-res BlackRoots video reels, story templates, and caption hooks to boost your conversions.</p>
      </div>
      <a href="./assets/blackroots-bottle-single.png" download class="bg-white/10 hover:bg-white/20 text-amber-300 font-bold text-xs px-5 py-2.5 rounded-xl border border-amber-400/40 transition-all no-underline flex items-center gap-2 whitespace-nowrap">
        <span>📥 Download Media Kit</span>
      </a>
    </div>

  </main>

  <!-- Payout Request Modal -->
  <div id="PayoutModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-md w-full p-6 shadow-2xl relative space-y-5 animate-fade-in">
      <button type="button" onclick="closePayoutModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 class="text-xl font-bold font-serif text-amber-300">Request Commission Payout</h3>
        <p class="text-xs text-gray-400">Available Unpaid Balance: <strong class="text-emerald-400 font-extrabold">₹4,890.00</strong></p>
      </div>

      <form onsubmit="handlePayoutSubmit(event)" class="space-y-4 text-xs">
        <div class="space-y-1.5">
          <label class="font-bold text-gray-300 uppercase tracking-wider block">Withdrawal Amount (₹)</label>
          <input type="number" value="4890" max="4890" required class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono text-base font-extrabold focus:outline-none focus:border-[#d4af37]">
        </div>

        <div class="space-y-1.5">
          <label class="font-bold text-gray-300 uppercase tracking-wider block">Payout Method</label>
          <select id="PayoutMethodSelect" onchange="togglePayoutFields()" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white focus:outline-none focus:border-[#d4af37]">
            <option value="upi">UPI ID (GPay / PhonePe / Paytm)</option>
            <option value="bank">Bank Account Transfer (NEFT/IMPS)</option>
          </select>
        </div>

        <div id="UPIFieldGroup" class="space-y-1.5">
          <label class="font-bold text-gray-300 uppercase tracking-wider block">Enter Your UPI ID</label>
          <input type="text" placeholder="priya@okicici or 9876543210@paytm" required class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono focus:outline-none focus:border-[#d4af37]">
        </div>

        <div id="BankFieldGroup" class="space-y-3 hidden">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Account Holder Name</label>
            <input type="text" placeholder="Priya Sharma" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white focus:outline-none focus:border-[#d4af37]">
          </div>
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Account Number</label>
              <input type="text" placeholder="501002938102" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-mono focus:outline-none focus:border-[#d4af37]">
            </div>
            <div>
              <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">IFSC Code</label>
              <input type="text" placeholder="HDFC0001234" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-mono focus:outline-none focus:border-[#d4af37]">
            </div>
          </div>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-sm py-3 rounded-2xl shadow-xl hover:brightness-110 transition-all cursor-pointer">
          Confirm & Submit Payout Request
        </button>
      </form>
    </div>
  </div>

  <!-- Authentication Modal (Login / Register Tabs) -->
  <div id="AuthModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-md w-full p-6 shadow-2xl relative space-y-5">
      <button type="button" onclick="toggleAuthModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <!-- Tab Controls -->
      <div class="flex items-center border-b border-white/10">
        <button id="TabLoginBtn" type="button" onclick="switchAuthTab('login')" class="w-1/2 py-2.5 text-center font-bold text-sm text-amber-300 border-b-2 border-[#d4af37] cursor-pointer">Influencer Login</button>
        <button id="TabRegisterBtn" type="button" onclick="switchAuthTab('register')" class="w-1/2 py-2.5 text-center font-bold text-sm text-gray-400 border-b-2 border-transparent hover:text-white cursor-pointer">Join As Creator</button>
      </div>

      <!-- Login Form -->
      <form id="LoginForm" onsubmit="handleAuthSubmit(event, 'login')" class="space-y-4 text-xs">
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Email Address</label>
          <input type="email" required placeholder="priya@instagram.com" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Password</label>
          <input type="password" required placeholder="••••••••" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <button type="submit" class="w-full bg-[#d4af37] text-black font-extrabold text-sm py-3 rounded-2xl shadow-xl hover:bg-amber-400 transition-all cursor-pointer">
          Login to Dashboard
        </button>
      </form>

      <!-- Register Form -->
      <form id="RegisterForm" onsubmit="handleAuthSubmit(event, 'register')" class="space-y-3 text-xs hidden">
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Full Name</label>
          <input type="text" required placeholder="Priya Sharma" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Instagram / YouTube Handle</label>
          <input type="text" required placeholder="@priya_beauty_lifestyle" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Email Address</label>
          <input type="email" required placeholder="priya@gmail.com" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Desired Coupon Code (e.g. PRIYA10)</label>
          <input type="text" required placeholder="PRIYA10" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-mono uppercase focus:outline-none focus:border-[#d4af37]">
        </div>
        <button type="submit" class="w-full bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-sm py-3 rounded-2xl shadow-xl hover:brightness-110 transition-all cursor-pointer">
          Apply For Creator Account
        </button>
      </form>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div id="Toast" class="fixed bottom-6 right-6 z-50 bg-[#d4af37] text-black font-extrabold text-xs px-5 py-3 rounded-2xl shadow-2xl transform translate-y-20 opacity-0 transition-all duration-300 flex items-center gap-2 pointer-events-none">
    <span id="ToastMsg">Copied to Clipboard!</span>
  </div>

  <!-- Footer -->
  <footer class="bg-black border-t border-[#d4af37]/20 py-8 px-4 text-center text-xs text-gray-400 mt-12">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
      <p>&copy; 2026 BlackRoots Herbal Hair Dye Shampoo. VIP Influencer Affiliate Engine.</p>
      <div class="flex items-center gap-4 text-amber-300 font-semibold">
        <a href="./index.html" class="hover:underline">Main Store</a>
        <a href="./product.html" class="hover:underline">Buy Shampoo</a>
        <a href="./admin-influencer.html" class="hover:underline">Store Admin Panel</a>
      </div>
    </div>
  </footer>

  <script>
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
      const modal = document.getElementById('PayoutModal');
      if (modal) modal.classList.remove('hidden'), modal.classList.add('flex');
    }

    function closePayoutModal() {
      const modal = document.getElementById('PayoutModal');
      if (modal) modal.classList.add('hidden'), modal.classList.remove('flex');
    }

    function toggleAuthModal() {
      const modal = document.getElementById('AuthModal');
      if (modal) {
        if (modal.classList.contains('hidden')) {
          modal.classList.remove('hidden');
          modal.classList.add('flex');
        } else {
          modal.classList.add('hidden');
          modal.classList.remove('flex');
        }
      }
    }

    function switchAuthTab(tab) {
      const loginBtn = document.getElementById('TabLoginBtn');
      const regBtn = document.getElementById('TabRegisterBtn');
      const loginForm = document.getElementById('LoginForm');
      const regForm = document.getElementById('RegisterForm');

      if (tab === 'login') {
        loginBtn.className = 'w-1/2 py-2.5 text-center font-bold text-sm text-amber-300 border-b-2 border-[#d4af37] cursor-pointer';
        regBtn.className = 'w-1/2 py-2.5 text-center font-bold text-sm text-gray-400 border-b-2 border-transparent hover:text-white cursor-pointer';
        loginForm.classList.remove('hidden');
        regForm.classList.add('hidden');
      } else {
        regBtn.className = 'w-1/2 py-2.5 text-center font-bold text-sm text-amber-300 border-b-2 border-[#d4af37] cursor-pointer';
        loginBtn.className = 'w-1/2 py-2.5 text-center font-bold text-sm text-gray-400 border-b-2 border-transparent hover:text-white cursor-pointer';
        regForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
      }
    }

    function togglePayoutFields() {
      const select = document.getElementById('PayoutMethodSelect');
      const upiGrp = document.getElementById('UPIFieldGroup');
      const bankGrp = document.getElementById('BankFieldGroup');
      if (select.value === 'bank') {
        upiGrp.classList.add('hidden');
        bankGrp.classList.remove('hidden');
      } else {
        upiGrp.classList.remove('hidden');
        bankGrp.classList.add('hidden');
      }
    }

    function handlePayoutSubmit(e) {
      e.preventDefault();
      closePayoutModal();
      showToast('Payout Request Submitted Successfully! Admin approval pending.');
    }

    function handleAuthSubmit(e, type) {
      e.preventDefault();
      toggleAuthModal();
      showToast(type === 'login' ? 'Logged In Successfully!' : 'Creator Application Submitted! Pending Admin Approval.');
    }
  </script>
</body>
</html>
"""

# 2. BUILD STORE OWNER ADMIN CONTROL PANEL (admin-influencer.html)
admin_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Store Admin &mdash; Influencer Affiliate Management System</title>
  <meta name="description" content="BlackRoots Store Owner Admin Dashboard. Manage influencers, custom promo codes, commission rates, and approve payout requests.">
  
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
            serif: ['Cormorant Garamond', 'Georgia', 'serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
          }
        }
      }
    }
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./assets/theme.css">
  <script src="./assets/theme.js" defer></script>
</head>
<body class="bg-[#0a0b0e] text-white font-sans antialiased selection:bg-[#d4af37] selection:text-black min-h-screen flex flex-col justify-between">

  <!-- Admin Top Bar -->
  <div class="bg-[#12151c] border-b border-[#d4af37]/30 py-2.5 px-4 text-xs font-semibold text-gray-300">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-3 flex-wrap">
      <div class="flex items-center gap-2">
        <span class="bg-red-500 text-white font-extrabold text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">STORE ADMIN</span>
        <span>BlackRoots Influencer Commission & Payout Management Panel</span>
      </div>
      <div class="flex items-center gap-4 text-amber-300">
        <a href="./influencer.html" class="hover:underline">Influencer Portal &rarr;</a>
        <a href="./index.html" class="hover:underline">Main Store &rarr;</a>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-50 bg-[#0a0b0e]/90 backdrop-blur-xl border-b border-[#d4af37]/20 py-3.5 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="font-serif text-2xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-[#d4af37] to-amber-500 tracking-wider">BlackRoots Admin</span>
        <span class="text-[10px] uppercase font-bold text-emerald-400 bg-emerald-500/20 px-2.5 py-0.5 rounded-full border border-emerald-500/30">MASTER CONTROL</span>
      </div>

      <button type="button" onclick="openAddInfluencerModal()" class="bg-[#d4af37] hover:bg-amber-400 text-black font-extrabold text-xs px-4 py-2 rounded-full shadow-lg transition-all transform hover:scale-105 cursor-pointer">
        + Add New Influencer
      </button>
    </div>
  </header>

  <!-- Main Body -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">

    <!-- Overview Stats Grid -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-2">
        <div class="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Affiliate Revenue</div>
        <div class="text-2xl sm:text-3xl font-extrabold text-amber-300 font-serif">₹2,84,500.00</div>
        <p class="text-[11px] text-emerald-400 font-semibold">224 Total Orders</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-2">
        <div class="text-gray-400 text-xs font-bold uppercase tracking-wider">Active Influencers</div>
        <div class="text-2xl sm:text-3xl font-extrabold text-white font-serif">28 Creators</div>
        <p class="text-[11px] text-gray-400">12 Gold Tier (15%)</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c]/80 shadow-xl space-y-2">
        <div class="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Commission Paid</div>
        <div class="text-2xl sm:text-3xl font-extrabold text-emerald-400 font-serif">₹36,675.00</div>
        <p class="text-[11px] text-gray-400">Settled via UPI / Bank</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border-2 border-amber-500/40 bg-amber-500/10 shadow-xl space-y-2">
        <div class="text-amber-300 text-xs font-bold uppercase tracking-wider">Pending Payouts</div>
        <div class="text-2xl sm:text-3xl font-extrabold text-amber-400 font-serif">₹8,450.00</div>
        <p class="text-[11px] text-amber-300 font-semibold">2 Requests Awaiting Approval</p>
      </div>
    </div>

    <!-- Section 1: Pending Payout Requests Settlement -->
    <div class="p-6 rounded-3xl glass-panel-luxury border-2 border-amber-500/30 bg-[#12151c] shadow-2xl space-y-5">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-lg font-bold text-amber-300 font-serif">⌛ Pending Payout Requests (Approval Needed)</h2>
          <p class="text-xs text-gray-400">Approve influencer withdrawal requests and mark as paid after transferring funds via UPI/Bank.</p>
        </div>
        <span class="text-xs bg-amber-500/20 text-amber-300 font-bold px-3 py-1 rounded-full border border-amber-500/30">
          2 Pending Requests
        </span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3 px-4 rounded-l-xl">Influencer</th>
              <th class="py-3 px-4">Handle / Email</th>
              <th class="py-3 px-4">Amount</th>
              <th class="py-3 px-4">Payout Method</th>
              <th class="py-3 px-4">UPI / Bank Detail</th>
              <th class="py-3 px-4 rounded-r-xl text-right">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5 font-medium text-gray-300">
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-bold text-white">Priya Sharma</td>
              <td class="py-3.5 px-4 text-gray-400">@priya_beauty &bull; priya@gmail.com</td>
              <td class="py-3.5 px-4 font-extrabold text-emerald-400 text-sm">₹4,890.00</td>
              <td class="py-3.5 px-4"><span class="bg-blue-500/20 text-blue-300 px-2 py-0.5 rounded text-[10px] font-bold">UPI ID</span></td>
              <td class="py-3.5 px-4 font-mono text-amber-300">priya@okicici</td>
              <td class="py-3.5 px-4 text-right">
                <button type="button" onclick="approvePayout(this, 'Priya Sharma', '₹4,890.00')" class="bg-emerald-500 hover:bg-emerald-400 text-black font-extrabold text-[11px] px-3.5 py-1.5 rounded-xl shadow-md transition-all cursor-pointer">
                  ✓ Approve & Mark Paid
                </button>
              </td>
            </tr>
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-bold text-white">Aman Varma</td>
              <td class="py-3.5 px-4 text-gray-400">@aman_grooming &bull; aman@gmail.com</td>
              <td class="py-3.5 px-4 font-extrabold text-emerald-400 text-sm">₹3,560.00</td>
              <td class="py-3.5 px-4"><span class="bg-purple-500/20 text-purple-300 px-2 py-0.5 rounded text-[10px] font-bold">Bank Transfer</span></td>
              <td class="py-3.5 px-4 font-mono text-gray-300">HDFC AC: 5010029810 &bull; IFSC: HDFC0001234</td>
              <td class="py-3.5 px-4 text-right">
                <button type="button" onclick="approvePayout(this, 'Aman Varma', '₹3,560.00')" class="bg-emerald-500 hover:bg-emerald-400 text-black font-extrabold text-[11px] px-3.5 py-1.5 rounded-xl shadow-md transition-all cursor-pointer">
                  ✓ Approve & Mark Paid
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Section 2: All Registered Influencers Management Directory -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-5">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 class="text-lg font-bold text-white font-serif">👥 Influencer & Creator Directory</h2>
          <p class="text-xs text-gray-400">Manage promo codes, commission rates, and status for active creators.</p>
        </div>
        <div class="flex items-center gap-2">
          <input type="text" placeholder="Search creator or code..." class="bg-[#0a0b0e] border border-white/10 text-xs px-3.5 py-2 rounded-xl text-white focus:outline-none focus:border-[#d4af37]">
        </div>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3.5 px-4 rounded-l-xl">Creator Name</th>
              <th class="py-3.5 px-4">Coupon Code</th>
              <th class="py-3.5 px-4">Commission %</th>
              <th class="py-3.5 px-4">Total Sales</th>
              <th class="py-3.5 px-4">Total Earned</th>
              <th class="py-3.5 px-4">Status</th>
              <th class="py-3.5 px-4 rounded-r-xl text-right">Actions</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5 font-medium text-gray-300">
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4">
                <div class="font-bold text-white">Priya Sharma</div>
                <div class="text-[10px] text-gray-400">@priya_beauty_lifestyle</div>
              </td>
              <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300 text-sm">PRIYA10</td>
              <td class="py-3.5 px-4 font-bold text-emerald-400">15% Per Sale</td>
              <td class="py-3.5 px-4 font-bold text-white">₹48,900 (38 orders)</td>
              <td class="py-3.5 px-4 font-bold text-amber-300">₹7,335.00</td>
              <td class="py-3.5 px-4"><span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded-full text-[10px] font-bold">Active</span></td>
              <td class="py-3.5 px-4 text-right space-x-1">
                <button type="button" onclick="editInfluencer('PRIYA10', 15)" class="bg-white/10 hover:bg-white/20 text-white font-bold text-[10px] px-2.5 py-1 rounded-lg transition-all cursor-pointer">Edit Rate</button>
              </td>
            </tr>

            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4">
                <div class="font-bold text-white">Rohan Kapoor</div>
                <div class="text-[10px] text-gray-400">@rohan_hair_guru</div>
              </td>
              <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300 text-sm">ROHAN10</td>
              <td class="py-3.5 px-4 font-bold text-emerald-400">12% Per Sale</td>
              <td class="py-3.5 px-4 font-bold text-white">₹32,400 (25 orders)</td>
              <td class="py-3.5 px-4 font-bold text-amber-300">₹3,888.00</td>
              <td class="py-3.5 px-4"><span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded-full text-[10px] font-bold">Active</span></td>
              <td class="py-3.5 px-4 text-right space-x-1">
                <button type="button" onclick="editInfluencer('ROHAN10', 12)" class="bg-white/10 hover:bg-white/20 text-white font-bold text-[10px] px-2.5 py-1 rounded-lg transition-all cursor-pointer">Edit Rate</button>
              </td>
            </tr>

            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4">
                <div class="font-bold text-white">Kavita Singh</div>
                <div class="text-[10px] text-gray-400">@kavita_herbal_hacks</div>
              </td>
              <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300 text-sm">KAVITA10</td>
              <td class="py-3.5 px-4 font-bold text-emerald-400">10% Per Sale</td>
              <td class="py-3.5 px-4 font-bold text-white">₹18,500 (15 orders)</td>
              <td class="py-3.5 px-4 font-bold text-amber-300">₹1,850.00</td>
              <td class="py-3.5 px-4"><span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded-full text-[10px] font-bold">Active</span></td>
              <td class="py-3.5 px-4 text-right space-x-1">
                <button type="button" onclick="editInfluencer('KAVITA10', 10)" class="bg-white/10 hover:bg-white/20 text-white font-bold text-[10px] px-2.5 py-1 rounded-lg transition-all cursor-pointer">Edit Rate</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- Add Influencer Modal -->
  <div id="AddInfluencerModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-md w-full p-6 shadow-2xl relative space-y-4">
      <button type="button" onclick="closeAddInfluencerModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 class="text-xl font-bold font-serif text-amber-300">Add New Influencer Partner</h3>
        <p class="text-xs text-gray-400">Assign a unique promo code & commission rate</p>
      </div>

      <form onsubmit="handleAddSubmit(event)" class="space-y-3 text-xs">
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Creator Name</label>
          <input type="text" required placeholder="Aarav Gupta" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Social Handle / Email</label>
          <input type="text" required placeholder="@aarav_style • aarav@gmail.com" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white focus:outline-none focus:border-[#d4af37]">
        </div>
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Promo Code</label>
            <input type="text" required placeholder="AARAV10" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-mono uppercase focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Commission Rate (%)</label>
            <input type="number" value="15" min="5" max="30" required class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-sm py-3 rounded-2xl shadow-xl hover:brightness-110 transition-all cursor-pointer mt-2">
          Create & Activate Creator Account
        </button>
      </form>
    </div>
  </div>

  <!-- Toast Container -->
  <div id="Toast" class="fixed bottom-6 right-6 z-50 bg-emerald-500 text-black font-extrabold text-xs px-5 py-3 rounded-2xl shadow-2xl transform translate-y-20 opacity-0 transition-all duration-300 flex items-center gap-2 pointer-events-none">
    <span id="ToastMsg">Success!</span>
  </div>

  <!-- Footer -->
  <footer class="bg-black border-t border-[#d4af37]/20 py-8 px-4 text-center text-xs text-gray-400 mt-12">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
      <p>&copy; 2026 BlackRoots Master Store Owner Control Center.</p>
      <div class="flex items-center gap-4 text-amber-300 font-semibold">
        <a href="./influencer.html" class="hover:underline">Influencer Portal</a>
        <a href="./index.html" class="hover:underline">Main Store</a>
      </div>
    </div>
  </footer>

  <script>
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

    function approvePayout(btn, name, amount) {
      const tr = btn.closest('tr');
      if (tr) {
        tr.style.opacity = '0.4';
        btn.innerText = '✓ Settlement Recorded';
        btn.className = 'bg-gray-700 text-gray-300 text-[10px] px-3 py-1 rounded-xl cursor-default';
        btn.disabled = true;
      }
      showToast(`Approved & Paid ${amount} to ${name}! Settlement recorded.`);
    }

    function editInfluencer(code, rate) {
      showToast(`Editing Commission Rate for ${code}. Current: ${rate}%`);
    }

    function handleAddSubmit(e) {
      e.preventDefault();
      closeAddInfluencerModal();
      showToast('New Influencer Account & Promo Code Created Successfully!');
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
        print(f"CREATED INFLUENCER & ADMIN DASHBOARDS IN: {d}")

