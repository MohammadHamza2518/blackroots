import os

# BUILD ULTRA-SIMPLE, ZERO-CONFUSION STORE OWNER ADMIN PANEL (admin-influencer.html)
admin_html = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Store Owner Admin Panel &mdash; BlackRoots</title>
  <meta name="description" content="Ultra-Simple Store Owner Panel for BlackRoots. Assign User IDs, Passwords, view influencer sales, and approve payouts.">
  
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

  <!-- Top Admin Bar -->
  <div class="bg-[#12151c] border-b border-[#d4af37]/30 py-2.5 px-4 text-xs font-bold text-gray-300">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-3">
      <div class="flex items-center gap-2">
        <span class="bg-red-500 text-white font-extrabold text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">STORE OWNER ONLY</span>
        <span>BlackRoots Influencer Control Panel</span>
      </div>
      <a href="./index.html" class="text-amber-300 hover:underline">Go to Main Store &rarr;</a>
    </div>
  </div>

  <!-- Header -->
  <header class="sticky top-0 z-50 bg-[#0a0b0e]/95 backdrop-blur-xl border-b border-[#d4af37]/20 py-4 px-4 sm:px-8">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="font-serif text-2xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-[#d4af37] to-amber-500">BlackRoots Admin</span>
        <span class="text-[10px] font-bold text-emerald-400 bg-emerald-500/20 px-2.5 py-0.5 rounded-full border border-emerald-500/30">SIMPLE MODE</span>
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
      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-xl space-y-1">
        <div class="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Sales From Influencers</div>
        <div class="text-3xl font-extrabold text-amber-300 font-serif">₹2,84,500.00</div>
        <p class="text-xs text-gray-400">224 Total Orders</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-xl space-y-1">
        <div class="text-gray-400 text-xs font-bold uppercase tracking-wider">Total Influencers Joined</div>
        <div class="text-3xl font-extrabold text-white font-serif">28 Influencers</div>
        <p class="text-xs text-gray-400">All User IDs Created By You</p>
      </div>

      <div class="p-5 rounded-2xl glass-panel-luxury border-2 border-amber-500/40 bg-amber-500/10 shadow-xl space-y-1">
        <div class="text-amber-300 text-xs font-bold uppercase tracking-wider">Pending Payout Requests</div>
        <div class="text-3xl font-extrabold text-amber-400 font-serif">₹8,450.00</div>
        <p class="text-xs text-amber-300 font-semibold">2 Influencers Waiting For Payment</p>
      </div>
    </div>

    <!-- SECTION 1: PENDING PAYOUTS TO APPROVE (PAY INFLUENCERS) -->
    <div class="p-6 rounded-3xl glass-panel-luxury border-2 border-amber-500/40 bg-[#12151c] shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-lg font-bold text-amber-300 font-serif">💸 Step 1: Pay Influencers & Mark Paid</h2>
          <p class="text-xs text-gray-400">Send money via GPay/PhonePe to their UPI ID, then click "Mark Paid".</p>
        </div>
        <span class="text-xs bg-amber-500/20 text-amber-300 font-bold px-3 py-1 rounded-full border border-amber-500/30">
          2 Pending Payments
        </span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs border-collapse">
          <thead>
            <tr class="border-b border-white/10 text-gray-400 uppercase text-[10px] tracking-wider bg-white/5">
              <th class="py-3 px-4">Influencer Name</th>
              <th class="py-3 px-4">User ID</th>
              <th class="py-3 px-4">Amount To Pay</th>
              <th class="py-3 px-4">Influencer UPI ID (Pay Here)</th>
              <th class="py-3 px-4 text-right">Action</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5 font-medium text-gray-300">
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-bold text-white">Priya Sharma</td>
              <td class="py-3.5 px-4 font-mono text-amber-300">priya</td>
              <td class="py-3.5 px-4 font-extrabold text-emerald-400 text-sm">₹4,890.00</td>
              <td class="py-3.5 px-4 font-mono text-amber-300 bg-white/5 px-2.5 py-1 rounded">priya@okicici</td>
              <td class="py-3.5 px-4 text-right">
                <button type="button" onclick="approvePayout(this, 'Priya Sharma', '₹4,890.00')" class="bg-emerald-500 hover:bg-emerald-400 text-black font-extrabold text-xs px-4 py-2 rounded-xl shadow-md transition-all cursor-pointer">
                  ✓ Mark Paid
                </button>
              </td>
            </tr>
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4 font-bold text-white">Aman Varma</td>
              <td class="py-3.5 px-4 font-mono text-amber-300">aman</td>
              <td class="py-3.5 px-4 font-extrabold text-emerald-400 text-sm">₹3,560.00</td>
              <td class="py-3.5 px-4 font-mono text-amber-300 bg-white/5 px-2.5 py-1 rounded">aman@ybl</td>
              <td class="py-3.5 px-4 text-right">
                <button type="button" onclick="approvePayout(this, 'Aman Varma', '₹3,560.00')" class="bg-emerald-500 hover:bg-emerald-400 text-black font-extrabold text-xs px-4 py-2 rounded-xl shadow-md transition-all cursor-pointer">
                  ✓ Mark Paid
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SECTION 2: MY INFLUENCERS LIST & CREDENTIALS -->
    <div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 bg-[#12151c] shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-white/10 pb-3">
        <div>
          <h2 class="text-lg font-bold text-white font-serif">👥 Step 2: My Influencers List & Credentials</h2>
          <p class="text-xs text-gray-400">Share User ID & Password with influencers so they can log in.</p>
        </div>
        <button type="button" onclick="openAddInfluencerModal()" class="bg-[#d4af37] text-black font-extrabold text-xs px-4 py-2 rounded-xl cursor-pointer">
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
          <tbody class="divide-y divide-white/5 font-medium text-gray-300">
            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4">
                <div class="font-bold text-white">Priya Sharma</div>
                <div class="text-[10px] text-gray-400">@priya_beauty</div>
              </td>
              <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300">priya</td>
              <td class="py-3.5 px-4 font-mono text-gray-300 bg-white/5 px-2 py-1 rounded">priya123</td>
              <td class="py-3.5 px-4 font-mono font-bold text-amber-400">PRIYA10</td>
              <td class="py-3.5 px-4 font-bold text-emerald-400">15%</td>
              <td class="py-3.5 px-4 font-bold text-white">₹48,900.00</td>
              <td class="py-3.5 px-4 text-right space-x-1">
                <button type="button" onclick="inspectSales('Priya Sharma', 'PRIYA10')" class="bg-amber-500/20 text-amber-300 hover:bg-amber-500/40 border border-amber-500/40 font-extrabold text-[10px] px-3 py-1.5 rounded-lg cursor-pointer">
                  🔍 View Sales
                </button>
              </td>
            </tr>

            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4">
                <div class="font-bold text-white">Aman Varma</div>
                <div class="text-[10px] text-gray-400">@aman_grooming</div>
              </td>
              <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300">aman</td>
              <td class="py-3.5 px-4 font-mono text-gray-300 bg-white/5 px-2 py-1 rounded">aman123</td>
              <td class="py-3.5 px-4 font-mono font-bold text-amber-400">AMAN10</td>
              <td class="py-3.5 px-4 font-bold text-emerald-400">12%</td>
              <td class="py-3.5 px-4 font-bold text-white">₹29,660.00</td>
              <td class="py-3.5 px-4 text-right space-x-1">
                <button type="button" onclick="inspectSales('Aman Varma', 'AMAN10')" class="bg-amber-500/20 text-amber-300 hover:bg-amber-500/40 border border-amber-500/40 font-extrabold text-[10px] px-3 py-1.5 rounded-lg cursor-pointer">
                  🔍 View Sales
                </button>
              </td>
            </tr>

            <tr class="hover:bg-white/5 transition-colors">
              <td class="py-3.5 px-4">
                <div class="font-bold text-white">Rohan Kapoor</div>
                <div class="text-[10px] text-gray-400">@rohan_hair_guru</div>
              </td>
              <td class="py-3.5 px-4 font-mono font-extrabold text-amber-300">rohan</td>
              <td class="py-3.5 px-4 font-mono text-gray-300 bg-white/5 px-2 py-1 rounded">rohan123</td>
              <td class="py-3.5 px-4 font-mono font-bold text-amber-400">ROHAN10</td>
              <td class="py-3.5 px-4 font-bold text-emerald-400">10%</td>
              <td class="py-3.5 px-4 font-bold text-white">₹32,400.00</td>
              <td class="py-3.5 px-4 text-right space-x-1">
                <button type="button" onclick="inspectSales('Rohan Kapoor', 'ROHAN10')" class="bg-amber-500/20 text-amber-300 hover:bg-amber-500/40 border border-amber-500/40 font-extrabold text-[10px] px-3 py-1.5 rounded-lg cursor-pointer">
                  🔍 View Sales
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- Simple Modal 1: Add New Influencer Form -->
  <div id="AddInfluencerModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-md w-full p-6 shadow-2xl relative space-y-4">
      <button type="button" onclick="closeAddInfluencerModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 class="text-xl font-bold font-serif text-amber-300">Add New Influencer</h3>
        <p class="text-xs text-gray-400">Create User ID & Password to share with Influencer</p>
      </div>

      <form onsubmit="handleAddSubmit(event)" class="space-y-3 text-xs">
        <div>
          <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Influencer Name</label>
          <input type="text" required placeholder="Aarav Gupta" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white focus:outline-none focus:border-[#d4af37]">
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">User ID</label>
            <input type="text" required placeholder="aarav" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-mono lowercase focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Password</label>
            <input type="text" required placeholder="aarav123" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-mono focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Promo Code</label>
            <input type="text" required placeholder="AARAV10" class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-mono uppercase focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="font-bold text-gray-300 uppercase tracking-wider block mb-1">Commission %</label>
            <input type="number" value="15" min="5" max="30" required class="w-full bg-[#0a0b0e] border border-white/10 rounded-xl p-2.5 text-white font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <button type="submit" class="w-full bg-gradient-to-r from-amber-400 to-[#d4af37] text-black font-extrabold text-sm py-3 rounded-2xl shadow-xl hover:brightness-110 transition-all cursor-pointer mt-2">
          Save & Create Influencer
        </button>
      </form>
    </div>
  </div>

  <!-- Simple Modal 2: View Sales Orders -->
  <div id="InspectSalesModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-[#12151c] border-2 border-[#d4af37]/50 rounded-3xl max-w-xl w-full p-6 shadow-2xl relative space-y-4">
      <button type="button" onclick="closeInspectSalesModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-lg cursor-pointer">&times;</button>
      
      <div class="space-y-1">
        <h3 id="InspectTitle" class="text-xl font-bold font-serif text-amber-300">Sales Brought By Priya Sharma</h3>
        <p class="text-xs text-gray-400">Orders placed using promo code <strong id="InspectCode" class="text-amber-300 font-mono">PRIYA10</strong></p>
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
          <tbody class="divide-y divide-white/5 text-gray-300 font-medium">
            <tr>
              <td class="py-2.5 px-3 font-mono text-amber-300">#BR-8921</td>
              <td class="py-2.5 px-3 font-semibold text-white">Rahul Mehta</td>
              <td class="py-2.5 px-3">₹1,598.00</td>
              <td class="py-2.5 px-3 font-bold text-emerald-400">₹239.70</td>
            </tr>
            <tr>
              <td class="py-2.5 px-3 font-mono text-amber-300">#BR-8904</td>
              <td class="py-2.5 px-3 font-semibold text-white">Ananya Verma</td>
              <td class="py-2.5 px-3">₹799.00</td>
              <td class="py-2.5 px-3 font-bold text-emerald-400">₹119.85</td>
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
  <footer class="bg-black border-t border-[#d4af37]/20 py-6 px-4 text-center text-xs text-gray-400 mt-12">
    <p>&copy; 2026 BlackRoots Store Owner Panel. Simple & Clear Control.</p>
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

    function approvePayout(btn, name, amount) {
      const tr = btn.closest('tr');
      if (tr) {
        tr.style.opacity = '0.4';
        btn.innerText = '✓ Payment Done';
        btn.className = 'bg-gray-700 text-gray-300 text-[10px] px-3 py-1 rounded-xl cursor-default';
        btn.disabled = true;
      }
      showToast(`Marked ${amount} paid to ${name}!`);
    }

    function handleAddSubmit(e) {
      e.preventDefault();
      closeAddInfluencerModal();
      showToast('Influencer Added! You can now share User ID & Password.');
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
        print(f"OVERWROTE ULTRA-SIMPLE ADMIN PANEL IN: {d}")

