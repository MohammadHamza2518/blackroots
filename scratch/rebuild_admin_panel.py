import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"

admin_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Store Owner Admin Console &mdash; BlackRoots</title>
  <meta name="description" content="BlackRoots Official Store Owner Admin Panel. Manage influencers, track sales, simulate orders, and clear UPI payouts.">
  
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

  <style>
    @media (max-width: 768px) {
      input[type="text"],
      input[type="number"],
      input[type="password"],
      select {
        font-size: 16px !important;
      }
      body {
        overflow-x: hidden;
      }
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
        ⚙️ OWNER CONSOLE
      </span>
      <span>BlackRoots Master Influencer, Commissions & Payouts Engine</span>
    </div>
  </div>

  <!-- Header -->
  <header class="sticky-header bg-[#0a0b0e]/95 backdrop-blur-xl border-b border-[#d4af37]/20">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 sm:h-20 flex items-center justify-between gap-3">
      
      <!-- Brand Logo -->
      <a href="index.html" class="flex items-center gap-2.5 group shrink-0">
        <img src="./assets/blackroots-logo-circle-black.jpg" alt="BlackRoots Logo" class="w-9 h-9 sm:w-11 sm:h-11 rounded-full border border-[#d4af37] object-cover shadow-lg">
        <div class="flex flex-col">
          <span class="font-serif text-lg sm:text-2xl font-bold tracking-wider text-white uppercase whitespace-nowrap">BlackRoots</span>
          <span class="text-[8px] sm:text-[9px] uppercase tracking-[0.2em] text-amber-300 font-bold -mt-1 whitespace-nowrap">Store Admin</span>
        </div>
      </a>

      <!-- Header Links -->
      <div class="flex items-center gap-2">
        <a href="influencer.html" class="inline-flex text-[10px] sm:text-xs font-bold text-amber-300 bg-amber-500/15 border border-amber-500/40 px-3 py-1.5 rounded-full hover:bg-amber-400 hover:text-black transition-all">
          👑 Creator Portal Login &rarr;
        </a>
      </div>

    </div>
  </header>

  <!-- Main Console -->
  <main class="max-w-6xl mx-auto px-4 sm:px-6 py-6 sm:py-8 w-full space-y-6">

    <!-- Top Summary Stats (3 Compact Cards) -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3.5">
      
      <div class="p-4 sm:p-5 rounded-2xl glass-card space-y-1">
        <span class="text-[11px] font-bold text-gray-400 uppercase tracking-wider block">Total Sales Driven</span>
        <div id="StatTotalSales" class="text-2xl sm:text-3xl font-black text-amber-300">₹5,489</div>
        <p class="text-[11px] text-gray-400"><strong id="StatTotalOrders" class="text-white">11</strong> Total Orders</p>
      </div>

      <div class="p-4 sm:p-5 rounded-2xl glass-card space-y-1">
        <span class="text-[11px] font-bold text-gray-400 uppercase tracking-wider block">Registered Influencers</span>
        <div id="StatTotalInfluencers" class="text-2xl sm:text-3xl font-black text-white">2 Creators</div>
        <p class="text-[11px] text-emerald-400 font-semibold">Active & Promoting</p>
      </div>

      <div class="p-4 sm:p-5 rounded-2xl glass-card space-y-1 border-emerald-500/40 bg-emerald-950/20">
        <span class="text-[11px] font-bold text-emerald-300 uppercase tracking-wider block">Pending UPI Payouts</span>
        <div id="StatPendingPayouts" class="text-2xl sm:text-3xl font-black text-emerald-400">₹500</div>
        <p id="StatPendingCount" class="text-[11px] text-emerald-300 font-semibold">1 Request Pending</p>
      </div>

    </div>

    <!-- Mobile-First Tab Bar -->
    <div class="flex items-center gap-1.5 p-1.5 bg-[#11141b] border border-white/10 rounded-2xl overflow-x-auto no-scrollbar shadow-lg">
      <button type="button" onclick="switchAdminTab('influencers')" id="TabBtnInfluencers" class="flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-black transition-all bg-[#d4af37] text-black shadow text-center">
        👥 Creators (<span id="TabCountCreators">2</span>)
      </button>
      <button type="button" onclick="switchAdminTab('payouts')" id="TabBtnPayouts" class="flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-bold transition-all text-gray-300 hover:text-white text-center">
        💸 Payouts (<span id="TabCountPayouts" class="text-emerald-400">1</span>)
      </button>
      <button type="button" onclick="switchAdminTab('create')" id="TabBtnCreate" class="flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-bold transition-all text-gray-300 hover:text-white text-center">
        ➕ Add Creator
      </button>
    </div>

    <!-- ================= TAB 1: CREATORS LIST & SALES ================= -->
    <div id="TabContentInfluencers" class="space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-base font-black text-white tracking-tight">Active Creators & Live Performance</h2>
          <p class="text-xs text-gray-400">Manage promo codes, view sales, and test commissions in 1 click</p>
        </div>
        <button type="button" onclick="switchAdminTab('create')" class="bg-[#d4af37] hover:bg-amber-300 text-black font-black text-xs px-3.5 py-2 rounded-xl shadow transition-all shrink-0">
          + Add New
        </button>
      </div>

      <!-- Influencer Cards Grid -->
      <div id="InfluencersContainer" class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Injected via JS -->
      </div>
    </div>

    <!-- ================= TAB 2: PENDING & SETTLED PAYOUTS ================= -->
    <div id="TabContentPayouts" class="hidden space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-base font-black text-white tracking-tight">UPI Payout Settlements</h2>
          <p class="text-xs text-gray-400">Pay creators via UPI and mark transactions as settled</p>
        </div>
      </div>

      <!-- Pending Payouts Card Deck -->
      <div class="space-y-3">
        <h3 class="text-xs font-bold text-emerald-300 uppercase tracking-wider">⚡ Pending Payout Requests</h3>
        <div id="PendingPayoutsContainer" class="space-y-3">
          <!-- Injected via JS -->
        </div>
      </div>

      <!-- Settled Payouts Card Deck -->
      <div class="space-y-3 pt-4 border-t border-white/10">
        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-wider">📜 Settled Payout History</h3>
        <div id="SettledPayoutsContainer" class="space-y-2">
          <!-- Injected via JS -->
        </div>
      </div>
    </div>

    <!-- ================= TAB 3: CREATE NEW CREATOR ================= -->
    <div id="TabContentCreate" class="hidden max-w-lg mx-auto">
      <div class="p-6 sm:p-8 rounded-3xl glass-card space-y-5">
        <div class="space-y-1 text-center">
          <div class="w-12 h-12 rounded-2xl bg-amber-400/20 border border-amber-400/40 flex items-center justify-center mx-auto text-amber-300 text-xl font-bold">
            ➕
          </div>
          <h2 class="text-xl font-black text-white">Create New Creator Account</h2>
          <p class="text-xs text-gray-400">Set up login credentials and custom promo code</p>
        </div>

        <form onsubmit="handleCreateInfluencer(event)" class="space-y-4 text-xs">
          <div>
            <label class="font-bold text-amber-300 uppercase tracking-wider block mb-1.5">Creator Full Name</label>
            <input id="NewName" type="text" required placeholder="e.g. Rahul Sharma" class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-medium focus:outline-none focus:border-[#d4af37]">
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label class="font-bold text-amber-300 uppercase tracking-wider block mb-1.5">User ID (Login)</label>
              <input id="NewUserID" type="text" required placeholder="e.g. rahul_fit" class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-mono lowercase focus:outline-none focus:border-[#d4af37]">
            </div>
            <div>
              <label class="font-bold text-amber-300 uppercase tracking-wider block mb-1.5">Password</label>
              <input id="NewPass" type="text" required placeholder="e.g. rahul2026" class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-mono focus:outline-none focus:border-[#d4af37]">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div>
              <label class="font-bold text-amber-300 uppercase tracking-wider block mb-1.5">Promo Code</label>
              <input id="NewCode" type="text" required placeholder="e.g. RAHUL10" class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-mono uppercase focus:outline-none focus:border-[#d4af37]">
            </div>
            <div>
              <label class="font-bold text-amber-300 uppercase tracking-wider block mb-1.5">Commission Rate (%)</label>
              <input id="NewRate" type="number" value="15" min="5" max="50" required class="w-full bg-black border border-white/20 rounded-xl p-3.5 text-white font-bold focus:outline-none focus:border-[#d4af37]">
            </div>
          </div>

          <button type="submit" class="w-full bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-sm py-4 rounded-xl shadow-xl hover:brightness-110 active:scale-95 transition-all uppercase tracking-wider cursor-pointer">
            Create & Save Creator Account &rarr;
          </button>
        </form>
      </div>
    </div>

  </main>

  <!-- Toast Notification -->
  <div id="Toast" class="fixed bottom-6 right-6 z-50 bg-[#d4af37] text-black font-black text-xs px-5 py-3 rounded-2xl shadow-2xl transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none">
    <span id="ToastMsg">Success!</span>
  </div>

  <!-- Master Logic Engine -->
  <script>
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
      try { return JSON.parse(raw); } catch (e) { return defaultDB; }
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

    document.addEventListener('DOMContentLoaded', function() {
      renderAll();
    });

    function switchAdminTab(tab) {
      document.getElementById('TabContentInfluencers').classList.toggle('hidden', tab !== 'influencers');
      document.getElementById('TabContentPayouts').classList.toggle('hidden', tab !== 'payouts');
      document.getElementById('TabContentCreate').classList.toggle('hidden', tab !== 'create');

      const btnInf = document.getElementById('TabBtnInfluencers');
      const btnPay = document.getElementById('TabBtnPayouts');
      const btnCre = document.getElementById('TabBtnCreate');

      btnInf.className = tab === 'influencers' ? 'flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-black transition-all bg-[#d4af37] text-black shadow text-center' : 'flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-bold transition-all text-gray-300 hover:text-white text-center';
      btnPay.className = tab === 'payouts' ? 'flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-black transition-all bg-[#d4af37] text-black shadow text-center' : 'flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-bold transition-all text-gray-300 hover:text-white text-center';
      btnCre.className = tab === 'create' ? 'flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-black transition-all bg-[#d4af37] text-black shadow text-center' : 'flex-1 min-w-[110px] py-2.5 px-3 rounded-xl text-xs font-bold transition-all text-gray-300 hover:text-white text-center';
    }

    function renderAll() {
      const db = getMasterDB();
      const userIds = Object.keys(db);
      const payouts = getPayoutsDB();

      // Top Stats calculation
      let totalSales = 0;
      let totalOrders = 0;
      userIds.forEach(uid => {
        totalSales += Number(db[uid].sales || 0);
        totalOrders += Number(db[uid].orders || 0);
      });

      const pendingPayouts = payouts.filter(p => p.status === 'Pending');
      let pendingVal = 0;
      pendingPayouts.forEach(p => { pendingVal += Number(p.amount || 0); });

      document.getElementById('StatTotalSales').textContent = '₹' + totalSales.toLocaleString('en-IN');
      document.getElementById('StatTotalOrders').textContent = totalOrders;
      document.getElementById('StatTotalInfluencers').textContent = `${userIds.length} Creators`;
      document.getElementById('StatPendingPayouts').textContent = '₹' + pendingVal.toLocaleString('en-IN');
      document.getElementById('StatPendingCount').textContent = `${pendingPayouts.length} Request${pendingPayouts.length === 1 ? '' : 's'} Pending`;

      document.getElementById('TabCountCreators').textContent = userIds.length;
      document.getElementById('TabCountPayouts').textContent = pendingPayouts.length;

      // Render Influencer Cards
      const infContainer = document.getElementById('InfluencersContainer');
      if (userIds.length === 0) {
        infContainer.innerHTML = `
          <div class="col-span-full p-8 text-center text-gray-400 text-xs bg-[#11141b] rounded-3xl border border-white/10">
            No creators added yet. Click "+ Add Creator" above to create one!
          </div>`;
      } else {
        infContainer.innerHTML = userIds.map(uid => {
          const inf = db[uid];
          return `
            <div class="p-5 rounded-3xl glass-card space-y-4 relative">
              <div class="flex items-start justify-between gap-3">
                <div class="space-y-0.5">
                  <div class="flex items-center gap-2 flex-wrap">
                    <h3 class="text-base font-black text-white">${inf.name}</h3>
                    <span class="text-[9px] font-black uppercase bg-amber-400/20 text-amber-300 px-2 py-0.5 rounded-full border border-amber-400/30 font-mono">${inf.code}</span>
                  </div>
                  <p class="text-xs text-gray-400">
                    ID: <strong class="text-amber-300 font-mono">${uid}</strong> &bull; Pass: <strong class="text-gray-300 font-mono">${inf.pass}</strong>
                  </p>
                </div>
                <button type="button" onclick="deleteInfluencer('${uid}')" class="text-gray-500 hover:text-red-400 text-xs font-bold p-1" title="Delete Creator">
                  🗑️
                </button>
              </div>

              <!-- Metrics Strip -->
              <div class="grid grid-cols-3 gap-2 p-3 rounded-2xl bg-black border border-white/10 text-center">
                <div>
                  <span class="text-[9px] text-gray-400 uppercase block font-bold">Sales</span>
                  <span class="text-sm font-black text-white">₹${Number(inf.sales || 0).toLocaleString('en-IN')}</span>
                </div>
                <div>
                  <span class="text-[9px] text-gray-400 uppercase block font-bold">Orders</span>
                  <span class="text-sm font-black text-amber-300">${inf.orders || 0}</span>
                </div>
                <div>
                  <span class="text-[9px] text-emerald-400 uppercase block font-bold">Wallet</span>
                  <span class="text-sm font-black text-emerald-400">₹${Number(inf.balance || 0).toLocaleString('en-IN')}</span>
                </div>
              </div>

              <!-- Action Bar -->
              <div class="flex items-center gap-2 pt-1">
                <button type="button" onclick="simulateSale('${uid}', 499)" class="flex-1 bg-emerald-500/15 hover:bg-emerald-500/25 border border-emerald-500/40 text-emerald-400 font-bold text-xs py-2.5 rounded-xl transition-all active:scale-95">
                  ⚡ + ₹499 Sale
                </button>
                <button type="button" onclick="simulateSale('${uid}', 799)" class="flex-1 bg-emerald-500/15 hover:bg-emerald-500/25 border border-emerald-500/40 text-emerald-400 font-bold text-xs py-2.5 rounded-xl transition-all active:scale-95">
                  ⚡ + ₹799 Sale
                </button>
                <button type="button" onclick="copyLoginCredentials('${uid}')" class="bg-white/10 hover:bg-white/20 text-white font-bold text-xs px-3 py-2.5 rounded-xl transition-all active:scale-95" title="Copy Login Details">
                  📋 Copy
                </button>
              </div>
            </div>
          `;
        }).join('');
      }

      // Render Pending Payouts
      const pendingContainer = document.getElementById('PendingPayoutsContainer');
      if (pendingPayouts.length === 0) {
        pendingContainer.innerHTML = `
          <div class="p-6 text-center text-gray-400 text-xs bg-black/40 rounded-2xl border border-white/5">
            ✨ No pending payout requests. All creator payouts are settled!
          </div>`;
      } else {
        pendingContainer.innerHTML = pendingPayouts.map(p => `
          <div class="p-4 rounded-2xl bg-black border border-emerald-500/40 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-lg">
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <span class="font-mono font-black text-amber-300">${p.id}</span>
                <span class="text-white font-bold text-sm">&bull; ${p.name} (${p.userId})</span>
              </div>
              <div class="text-xs text-gray-300 flex items-center gap-2 flex-wrap">
                <span>Amount: <strong class="text-emerald-400 font-black text-sm">₹${p.amount}</strong></span>
                <span>&bull;</span>
                <span class="font-mono text-amber-300 bg-white/5 px-2 py-0.5 rounded border border-white/10">UPI: ${p.upi}</span>
              </div>
            </div>
            <button type="button" onclick="settlePayout('${p.id}')" class="bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-400 hover:to-emerald-500 text-black font-black text-xs px-5 py-3 rounded-xl shadow-lg transition-all uppercase tracking-wider active:scale-95 shrink-0">
              ✅ Pay & Mark Settled
            </button>
          </div>
        `).join('');
      }

      // Render Settled Payouts
      const settledPayouts = payouts.filter(p => p.status === 'Settled');
      const settledContainer = document.getElementById('SettledPayoutsContainer');
      if (settledPayouts.length === 0) {
        settledContainer.innerHTML = `<div class="p-4 text-center text-gray-500 text-xs">No settled payout history yet.</div>`;
      } else {
        settledContainer.innerHTML = settledPayouts.map(p => `
          <div class="p-3 rounded-xl bg-white/5 border border-white/10 flex items-center justify-between text-xs">
            <div class="space-y-0.5">
              <span class="font-bold text-white">${p.name} &bull; <span class="font-mono text-gray-400">${p.upi}</span></span>
              <span class="text-[10px] text-gray-400 block">${p.date} &bull; ${p.id}</span>
            </div>
            <div class="text-right">
              <span class="font-black text-emerald-400 block">₹${p.amount}</span>
              <span class="text-[9px] uppercase font-bold text-emerald-300">SETTLED</span>
            </div>
          </div>
        `).join('');
      }
    }

    function handleCreateInfluencer(e) {
      e.preventDefault();
      const name = document.getElementById('NewName').value.trim();
      const uid = document.getElementById('NewUserID').value.trim().toLowerCase();
      const pass = document.getElementById('NewPass').value.trim();
      const code = document.getElementById('NewCode').value.trim().toUpperCase();
      const rate = Number(document.getElementById('NewRate').value) || 15;

      const db = getMasterDB();
      if (db[uid]) {
        alert('User ID already exists! Please choose another one.');
        return;
      }

      db[uid] = {
        name: name,
        pass: pass,
        code: code,
        rate: rate,
        sales: 0,
        orders: 0,
        earned: 0,
        paid: 0,
        balance: 0,
        date: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }),
        salesList: []
      };

      saveMasterDB(db);
      e.target.reset();
      switchAdminTab('influencers');
      renderAll();
      showToast(`Created creator account: ${name} (${uid})!`);
    }

    function simulateSale(uid, amount) {
      const db = getMasterDB();
      const inf = db[uid];
      if (!inf) return;

      const rate = inf.rate || 15;
      const commission = Math.round((amount * rate) / 100);

      inf.sales = Number(inf.sales || 0) + amount;
      inf.orders = Number(inf.orders || 0) + 1;
      inf.earned = Number(inf.earned || 0) + commission;
      inf.balance = Number(inf.balance || 0) + commission;

      if (!inf.salesList) inf.salesList = [];
      inf.salesList.unshift({
        id: 'BR-' + Math.floor(1000 + Math.random() * 9000),
        date: 'Just Now',
        customer: 'Customer ' + Math.floor(10 + Math.random() * 90),
        amount: amount,
        commission: commission
      });

      saveMasterDB(db);
      renderAll();
      showToast(`Added ₹${amount} sale to ${inf.name}! (+₹${commission} Commission)`);
    }

    function deleteInfluencer(uid) {
      if (!confirm(`Are you sure you want to delete creator ${uid}?`)) return;
      const db = getMasterDB();
      delete db[uid];
      saveMasterDB(db);
      renderAll();
      showToast(`Deleted creator ${uid}`);
    }

    function settlePayout(pid) {
      const payouts = getPayoutsDB();
      const target = payouts.find(p => p.id === pid);
      if (!target) return;

      target.status = 'Settled';
      target.date = new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });
      savePayoutsDB(payouts);
      renderAll();
      showToast(`Settled Payout ${pid}!`);
    }

    function copyLoginCredentials(uid) {
      const db = getMasterDB();
      const inf = db[uid];
      if (!inf) return;

      const text = `👑 BlackRoots Creator Login\\n🔗 Portal: https://blackroots.in/influencer.html\\n👤 User ID: ${uid}\\n🔑 Password: ${inf.pass}\\n🎟️ Promo Code: ${inf.code} (10% OFF)\\n💰 Commission: ${inf.rate || 15}%`;
      navigator.clipboard.writeText(text);
      showToast(`Copied login details for ${inf.name}!`);
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
  </script>

</body>
</html>
"""

with open(os.path.join(root_dir, "admin-influencer.html"), "w", encoding="utf-8") as f:
    f.write(admin_html)
print("Updated admin-influencer.html")
