import os

# REWRITE ADMIN PANEL WITH FRESH ZERO DATA & CLASSY SANS-SERIF TYPOGRAPHY (admin-influencer.html)
admin_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Store Owner Admin Panel &mdash; BlackRoots</title>
  <meta name="description" content="Clean Fresh Store Owner Panel for BlackRoots. Zero initial state. Add influencers, assign User IDs, Passwords, track real sales, and settle payouts.">
  
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
        <span class="text-[10px] font-bold text-emerald-400 bg-emerald-500/20 px-2.5 py-0.5 rounded-full border border-emerald-500/30">FRESH START (0 DATA)</span>
      </div>

      <button type="button" onclick="openAddInfluencerModal()" class="bg-[#d4af37] hover:bg-amber-400 text-black font-extrabold text-xs px-5 py-2.5 rounded-full shadow-lg transition-all transform hover:scale-105 cursor-pointer">
        + Add New Influencer (User ID & Password)
      </button>
    </div>
  </header>

  <!-- Main Body -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">

    <!-- 3 Simple Fresh Stat Cards (0 Base) -->
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
        <div class="text-emerald-300 text-xs font-bold uppercase tracking-wider">Pending Payout Requests</div>
        <div id="StatPendingPayouts" class="text-3xl font-extrabold text-emerald-400 tracking-tight">₹0.00</div>
        <p id="StatPendingCount" class="text-xs text-emerald-300 font-semibold">0 Pending Payments</p>
      </div>
    </div>

    <!-- SECTION 1: PENDING PAYOUTS TO APPROVE (FRESH STATE) -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-lg font-bold text-white tracking-tight">💸 Step 1: Pay Influencers & Mark Paid</h2>
          <p class="text-xs text-gray-400 font-medium">When creators request payouts, their UPI ID will appear here for 1-click settlement.</p>
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
            <!-- Empty State Row -->
            <tr id="EmptyPayoutRow">
              <td colspan="5" class="py-8 text-center text-gray-400 text-xs font-medium">
                ✨ No pending payout requests. All payouts are 100% settled!
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SECTION 2: MY INFLUENCERS LIST & CREDENTIALS (FRESH STATE) -->
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
            <!-- Empty State Row -->
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
          <input id="AddName" type="text" required placeholder="Priya Sharma" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white focus:outline-none focus:border-[#d4af37]">
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">User ID</label>
            <input id="AddUserID" type="text" required placeholder="priya" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono lowercase focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Password</label>
            <input id="AddPass" type="text" required placeholder="priya123" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Promo Code</label>
            <input id="AddCode" type="text" required placeholder="PRIYA10" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-3 text-white font-mono uppercase focus:outline-none focus:border-[#d4af37]">
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
    <p>&copy; 2026 BlackRoots Store Owner Panel. Fresh State Ready.</p>
  </footer>

  <script>
    let influencers = [];
    let pendingPayouts = [];

    document.addEventListener('DOMContentLoaded', function() {
      renderTables();
    });

    function renderTables() {
      const infTable = document.getElementById('InfluencersTableBody');
      const statInf = document.getElementById('StatTotalInfluencers');
      
      if (influencers.length === 0) {
        infTable.innerHTML = `
          <tr id="EmptyInfluencerRow">
            <td colspan="7" class="py-10 text-center text-gray-400 text-xs font-medium space-y-2">
              <div class="text-amber-300 text-xl font-bold">✨</div>
              <div>No Influencers added yet. Click <strong class="text-amber-300 font-bold">'+ Add New Influencer'</strong> above to create your first User ID & Password!</div>
            </td>
          </tr>`;
        if (statInf) statInf.innerText = '0 Influencers';
      } else {
        if (statInf) statInf.innerText = `${influencers.length} Influencers`;
        infTable.innerHTML = influencers.map((inf, idx) => `
          <tr class="hover:bg-white/5 transition-colors">
            <td class="py-3.5 px-4 font-bold text-white">${inf.name}</td>
            <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300">${inf.userId}</td>
            <td class="py-3.5 px-4 font-mono text-gray-300 bg-white/5 px-2.5 py-1 rounded">${inf.pass}</td>
            <td class="py-3.5 px-4 font-mono font-bold text-amber-400">${inf.code}</td>
            <td class="py-3.5 px-4 font-bold text-emerald-400">${inf.rate}%</td>
            <td class="py-3.5 px-4 font-bold text-white">₹0.00</td>
            <td class="py-3.5 px-4 text-right space-x-1">
              <button type="button" onclick="inspectSales('${inf.name}', '${inf.code}')" class="bg-amber-500/20 text-amber-300 hover:bg-amber-500/40 border border-amber-500/40 font-extrabold text-[10px] px-3 py-1.5 rounded-lg cursor-pointer">
                🔍 View Sales
              </button>
            </td>
          </tr>
        `).join('');
      }
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

      influencers.push({ name, userId, pass, code, rate });
      renderTables();
      closeAddInfluencerModal();
      showToast(`Influencer ${name} Added! User ID: ${userId} | Pass: ${pass}`);
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
        with open(os.path.join(d, "admin-influencer.html"), "w", encoding="utf-8") as f:
            f.write(admin_html)
        print(f"RESET ADMIN PANEL TO FRESH ZERO STATE IN: {d}")

