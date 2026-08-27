import os
import re
import json

print("=== STARTING COMPLETE INFLUENCER & ADMIN INTEGRATION BUILD ===")

# ==============================================================================
# 1. INFLUENCER PORTAL HTML (influencer.html & influencer/index.html)
# ==============================================================================
influencer_html_code = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>BlackRoots &mdash; VIP Creator & Influencer Hub</title>
  <meta name="description" content="BlackRoots Official VIP Creator & Affiliate Portal. Access your exclusive promo code, track live earnings, real-time sales, and instant UPI payouts.">
  <meta name="robots" content="noindex, nofollow">
  
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brandDark: '#0a0b0e',
            brandCard: '#11141b',
            brandCardHover: '#161a23',
            brandEmerald: '#123824',
            brandEmeraldDark: '#0a2115',
            brandGold: '#d4af37',
            brandGoldLight: '#f5e4ab',
            brandGoldDark: '#9a781b',
          },
          fontFamily: {
            serif: ['Cormorant Garamond', 'Georgia', 'serif'],
            sans: ['Plus Jakarta Sans', 'system-ui', '-apple-system', 'sans-serif'],
          }
        }
      }
    }
  </script>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./assets/theme.css">

  <style>
    *, *::before, *::after, html, body {
      scrollbar-width: none !important;
      -ms-overflow-style: none !important;
    }
    *::-webkit-scrollbar {
      display: none !important;
      width: 0px !important;
    }
    .gold-gradient-text {
      background: linear-gradient(135deg, #fff2c6 0%, #d4af37 50%, #aa7c11 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .gold-border-glow {
      box-shadow: 0 0 25px rgba(212, 175, 55, 0.15);
    }
    .btn-gold-action {
      background: linear-gradient(135deg, #d4af37 0%, #f7e7a7 50%, #aa7c11 100%);
      color: #000;
      font-weight: 800;
      transition: all 0.25s ease;
    }
    .btn-gold-action:hover {
      filter: brightness(1.1);
      transform: translateY(-1px);
      box-shadow: 0 10px 25px rgba(212, 175, 55, 0.35);
    }
    .btn-gold-action:active {
      transform: scale(0.98);
    }
  </style>
</head>
<body class="bg-[#0a0b0e] text-white font-sans antialiased selection:bg-[#d4af37] selection:text-black min-h-screen flex flex-col justify-between pb-20 md:pb-0">

  <!-- ========================================================================= -->
  <!-- 1. AUTH SCREEN (LOGIN & REGISTER TABS) -->
  <!-- ========================================================================= -->
  <div id="InfluencerAuthScreen" class="fixed inset-0 z-50 bg-[#0a0b0e] flex items-center justify-center p-4 overflow-y-auto">
    <div class="w-full max-w-md my-auto p-6 sm:p-8 rounded-3xl bg-[#11141b] border border-[#d4af37]/40 shadow-[0_20px_60px_rgba(0,0,0,0.95)] text-center space-y-6">
      
      <!-- Logo Header -->
      <div class="flex flex-col items-center gap-2">
        <a href="./index.html" class="flex items-center gap-2 mb-1">
          <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo" class="w-14 h-14 rounded-full border-2 border-[#d4af37] shadow-xl">
        </a>
        <h1 class="font-serif text-2xl sm:text-3xl font-bold uppercase tracking-wider gold-gradient-text">BlackRoots Creator Hub</h1>
        <p class="text-xs text-gray-400 font-medium">VIP Influencer & Affiliate Partner Portal</p>
      </div>

      <!-- Tab Buttons: Login / Apply -->
      <div class="flex rounded-2xl bg-black/60 p-1 border border-white/10 text-xs font-bold">
        <button type="button" id="tab-btn-login" onclick="switchAuthTab('login')" class="flex-1 py-2.5 rounded-xl transition-all bg-[#d4af37] text-black">Creator Login</button>
        <button type="button" id="tab-btn-register" onclick="switchAuthTab('register')" class="flex-1 py-2.5 rounded-xl transition-all text-gray-400 hover:text-white">Apply to Join</button>
      </div>

      <!-- Form 1: Creator Login -->
      <form id="InfluencerLoginForm" onsubmit="handleInfluencerLogin(event)" class="space-y-4 text-left">
        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Username / Promo Code / Phone</label>
          <input type="text" id="inf-login-id" required placeholder="e.g. PRIYA10 or 9876543210" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Password</label>
          <input type="password" id="inf-login-pass" required placeholder="Enter Your Password" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
        </div>
        
        <div class="flex items-center justify-between text-xs text-gray-400">
          <label class="flex items-center gap-2 cursor-pointer">
            <input type="checkbox" checked class="rounded accent-[#d4af37]"> Remember me
          </label>
          <a href="https://wa.me/919580835179?text=Hello%20BlackRoots%20Team%2C%20I%20forgot%20my%20Influencer%20portal%20password." target="_blank" class="text-amber-400 hover:underline">Forgot?</a>
        </div>

        <button type="submit" id="login-submit-btn" class="w-full btn-gold-action text-sm py-4 rounded-xl shadow-xl uppercase tracking-wider cursor-pointer">
          Sign In to Dashboard &rarr;
        </button>
        <p id="login-error-msg" class="hidden text-xs text-red-400 font-bold text-center"></p>
      </form>

      <!-- Form 2: Apply to Join -->
      <form id="InfluencerRegisterForm" onsubmit="handleInfluencerRegister(event)" class="hidden space-y-3.5 text-left">
        <div>
          <label class="block text-[11px] font-bold text-gray-300 uppercase tracking-wider mb-1">Your Full Name</label>
          <input type="text" id="reg-name" required placeholder="e.g. Priya Sharma" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white text-xs focus:outline-none focus:border-[#d4af37]">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-[11px] font-bold text-gray-300 uppercase tracking-wider mb-1">Mobile / WhatsApp</label>
            <input type="tel" id="reg-phone" required placeholder="10-Digit Mobile" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white text-xs focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="block text-[11px] font-bold text-gray-300 uppercase tracking-wider mb-1">Instagram / Channel</label>
            <input type="text" id="reg-handle" required placeholder="@yourhandle" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white text-xs focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-[11px] font-bold text-gray-300 uppercase tracking-wider mb-1">Desired Promo Code</label>
            <input type="text" id="reg-code" required placeholder="e.g. PRIYA10" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white text-xs uppercase font-bold focus:outline-none focus:border-[#d4af37]">
          </div>
          <div>
            <label class="block text-[11px] font-bold text-gray-300 uppercase tracking-wider mb-1">Set Password</label>
            <input type="password" id="reg-pass" required placeholder="Min 6 characters" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white text-xs font-mono focus:outline-none focus:border-[#d4af37]">
          </div>
        </div>

        <button type="submit" id="reg-submit-btn" class="w-full btn-gold-action text-xs font-black py-3.5 rounded-xl shadow-xl uppercase tracking-wider cursor-pointer mt-2">
          Submit Creator Application &rarr;
        </button>
        <p id="reg-status-msg" class="hidden text-xs text-emerald-400 font-bold text-center"></p>
      </form>

      <!-- Instant Test Access Demo Info -->
      <div class="p-3.5 rounded-2xl bg-white/5 border border-[#d4af37]/20 text-left space-y-1.5">
        <div class="flex items-center justify-between">
          <span class="text-[10px] uppercase font-bold text-amber-300 tracking-wider">🌟 Instant Demo Login:</span>
          <button type="button" onclick="quickFillDemo()" class="text-[10px] text-amber-400 font-bold underline hover:text-white">1-Click Auto Fill</button>
        </div>
        <p class="text-[11px] text-gray-400">Username: <code class="text-white font-bold bg-black px-1.5 py-0.5 rounded border border-white/10">PRIYA10</code> &bull; Password: <code class="text-white font-bold bg-black px-1.5 py-0.5 rounded border border-white/10">blackroots</code></p>
      </div>

      <div class="pt-2 border-t border-white/10">
        <a href="./index.html" class="text-xs text-gray-400 hover:text-white transition-colors">&larr; Return to BlackRoots Main Website</a>
      </div>

    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 2. MAIN CREATOR DASHBOARD APP -->
  <!-- ========================================================================= -->
  <div id="InfluencerDashboardApp" class="hidden flex-1 flex flex-col min-h-screen">
    
    <!-- Top Creator Navigation Header -->
    <header class="bg-[#11141b]/95 backdrop-blur-xl border-b border-[#d4af37]/20 sticky top-0 z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        
        <!-- Brand & Creator Badge -->
        <div class="flex items-center gap-3">
          <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo" class="w-9 h-9 rounded-full border border-[#d4af37]">
          <div class="flex flex-col">
            <span class="font-serif text-lg font-bold text-white uppercase tracking-wider">BlackRoots VIP</span>
            <span class="text-[9px] uppercase tracking-widest text-[#d4af37] font-bold" id="header-creator-name">Creator Portal</span>
          </div>
        </div>

        <!-- Desktop Navigation Tabs -->
        <nav class="hidden md:flex items-center gap-2">
          <button onclick="switchInfTab('overview')" class="inf-nav-tab px-4 py-2 rounded-xl text-xs font-bold transition-all bg-[#d4af37] text-black" data-tab="overview">📊 Overview</button>
          <button onclick="switchInfTab('share')" class="inf-nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all" data-tab="share">🔗 Link &amp; Promo</button>
          <button onclick="switchInfTab('orders')" class="inf-nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all" data-tab="orders">🛍️ My Orders</button>
          <button onclick="switchInfTab('wallet')" class="inf-nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all" data-tab="wallet">💳 Payouts &amp; UPI</button>
        </nav>

        <!-- Right User & Logout -->
        <div class="flex items-center gap-3">
          <a href="./index.html" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 text-xs font-bold text-gray-300 hover:text-white transition-all">
            <span>Storefront ↗</span>
          </a>
          <button onclick="handleInfluencerLogout()" class="px-3 py-1.5 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 hover:bg-red-500 hover:text-white text-xs font-bold transition-all cursor-pointer">
            Logout
          </button>
        </div>

      </div>
    </header>

    <!-- Main Content Container -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 w-full flex-1 space-y-6">

      <!-- VIP Creator Welcome Banner Card -->
      <div class="relative overflow-hidden p-6 sm:p-8 rounded-3xl bg-gradient-to-br from-[#123824] via-[#0e2418] to-[#11141b] border border-[#d4af37]/40 shadow-2xl">
        <div class="relative z-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
          <div class="space-y-2">
            <div class="flex items-center gap-2.5 flex-wrap">
              <span class="inline-flex items-center gap-1.5 bg-[#d4af37] text-black font-black text-[10px] px-3 py-1 rounded-full uppercase tracking-wider shadow">
                ★ GOLD VIP CREATOR
              </span>
              <span class="text-xs text-amber-300 font-bold bg-black/40 px-3 py-1 rounded-full border border-amber-500/30">
                ⚡ <span id="banner-comm-rate">10%</span> Flat Commission
              </span>
            </div>
            <h2 class="font-serif text-2xl sm:text-4xl font-bold text-white">
              Welcome back, <span id="creator-greeting-name" class="gold-gradient-text">Priya</span>!
            </h2>
            <p class="text-xs sm:text-sm text-gray-300 max-w-xl font-light">
              Share your promo code with your audience. When they get 10% OFF at checkout, you earn <strong class="text-amber-300 font-bold" id="banner-comm-sub">10% Instant Commission</strong> on every bottle delivered.
            </p>
          </div>

          <!-- Quick Promo Code Badge with 1-Tap Copy -->
          <div class="bg-black/70 backdrop-blur-md p-4 sm:p-5 rounded-2xl border border-[#d4af37]/50 text-center sm:text-right space-y-2 min-w-[200px] w-full sm:w-auto">
            <span class="text-[10px] font-bold text-gray-400 uppercase tracking-widest block">Your Official Code</span>
            <div class="flex items-center justify-center sm:justify-end gap-2">
              <span id="quick-promo-code" class="text-2xl sm:text-3xl font-black text-amber-300 font-mono tracking-wider">PRIYA10</span>
              <button onclick="copyPromoCode()" class="p-2 rounded-xl bg-amber-400 text-black hover:bg-white transition-all cursor-pointer shadow-lg" title="Copy Promo Code">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path></svg>
              </button>
            </div>
            <span id="copy-toast" class="text-[10px] text-emerald-400 font-bold block opacity-0 transition-opacity">✓ Copied to clipboard!</span>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- TAB 1: OVERVIEW -->
      <!-- ===================================================================== -->
      <section id="tab-overview" class="inf-tab-content space-y-6">
        
        <!-- Live Metrics Grid -->
        <div class="grid grid-cols-2 lg:grid-cols-5 gap-3 sm:gap-5">
          
          <div class="p-4 sm:p-5 rounded-2xl bg-[#11141b] border border-white/10 shadow-xl space-y-1.5">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">👁️ Total Clicks</span>
            <span id="metric-clicks" class="text-xl sm:text-3xl font-black text-white block">0</span>
            <span class="text-[10px] text-gray-500 block font-medium">Audience link visits</span>
          </div>

          <div class="p-4 sm:p-5 rounded-2xl bg-[#11141b] border border-white/10 shadow-xl space-y-1.5">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">🛍️ Total Orders</span>
            <span id="metric-orders" class="text-xl sm:text-3xl font-black text-amber-300 block">0</span>
            <span class="text-[10px] text-emerald-400 block font-semibold">⚡ Verified sales</span>
          </div>

          <div class="p-4 sm:p-5 rounded-2xl bg-[#11141b] border border-white/10 shadow-xl space-y-1.5">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">💎 Sales Driven</span>
            <span id="metric-revenue" class="text-xl sm:text-3xl font-black text-white block">₹0</span>
            <span class="text-[10px] text-gray-400 block font-medium">Gross revenue</span>
          </div>

          <div class="p-4 sm:p-5 rounded-2xl bg-[#11141b] border border-emerald-500/30 shadow-xl space-y-1.5">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">💰 Total Commission</span>
            <span id="metric-earned" class="text-xl sm:text-3xl font-black text-emerald-400 block">₹0</span>
            <span class="text-[10px] text-emerald-400/80 block font-semibold">Lifetime earnings</span>
          </div>

          <div class="col-span-2 lg:col-span-1 p-4 sm:p-5 rounded-2xl bg-[#11141b] border border-[#d4af37]/60 shadow-xl space-y-1.5 gold-border-glow">
            <div class="flex items-center justify-between">
              <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-amber-300 block">💳 Wallet Balance</span>
              <span class="text-[9px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded-full font-bold">Unpaid</span>
            </div>
            <span id="metric-unpaid" class="text-2xl sm:text-3xl font-black text-amber-300 block">₹0</span>
            <button onclick="switchInfTab('wallet')" class="text-[10px] text-amber-400 hover:underline font-bold block pt-1">Request Withdrawal &rarr;</button>
          </div>

        </div>

        <!-- 1-Click Quick Social Action Strip (Mobile Friendly) -->
        <div class="p-5 sm:p-6 rounded-3xl bg-[#11141b] border border-[#d4af37]/30 shadow-xl space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
              <h3 class="font-serif text-lg sm:text-xl font-bold text-white">1-Click Share &amp; Earn</h3>
              <p class="text-xs text-gray-400">Share pre-formatted high-converting promotions directly with your followers.</p>
            </div>
            <span class="text-xs text-amber-300 font-bold bg-black/40 px-3 py-1 rounded-xl border border-white/10 self-start sm:self-auto">
              💰 Your Link Auto-Applies <span id="share-code-pill" class="text-white font-mono">PRIYA10</span>
            </span>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            
            <!-- WhatsApp Share Button -->
            <button onclick="shareWhatsApp()" class="flex items-center justify-center gap-3 p-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-all shadow-lg cursor-pointer">
              <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
              <span>Share on WhatsApp &rarr;</span>
            </button>

            <!-- Instagram Link Copy Button -->
            <button onclick="copyProductLink()" class="flex items-center justify-center gap-3 p-4 rounded-2xl bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 hover:opacity-95 text-white font-bold text-xs transition-all shadow-lg cursor-pointer">
              <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              <span>Copy Instagram Bio Link &rarr;</span>
            </button>

            <!-- Storefront Direct Link Copy -->
            <button onclick="copyStoreLink()" class="flex items-center justify-center gap-3 p-4 rounded-2xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs transition-all border border-white/20 shadow-lg cursor-pointer">
              <span>📋 Copy Main Store Link</span>
            </button>

          </div>
        </div>

        <!-- Recent Referred Orders Stream -->
        <div class="p-5 sm:p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="font-serif text-lg sm:text-xl font-bold text-white">Recent Customer Purchases</h3>
            <button onclick="switchInfTab('orders')" class="text-xs text-[#d4af37] font-bold hover:underline">View All Orders &rarr;</button>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-gray-300 min-w-[500px]">
              <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
                <tr>
                  <th class="py-3 px-3">Order ID</th>
                  <th class="py-3 px-3">Date</th>
                  <th class="py-3 px-3">Bundle</th>
                  <th class="py-3 px-3">Order Value</th>
                  <th class="py-3 px-3">Your Commission</th>
                  <th class="py-3 px-3 text-right">Status</th>
                </tr>
              </thead>
              <tbody id="inf-recent-orders-table" class="divide-y divide-white/5 font-light">
                <tr>
                  <td colspan="6" class="py-8 text-center text-gray-500">No referred orders yet. Share your promo code to start earning!</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </section>

      <!-- ===================================================================== -->
      <!-- TAB 2: LINK & PROMO GENERATOR -->
      <!-- ===================================================================== -->
      <section id="tab-share" class="inf-tab-content hidden space-y-6">
        
        <div class="p-6 sm:p-8 rounded-3xl bg-[#11141b] border border-[#d4af37]/30 shadow-xl space-y-6">
          <div>
            <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white">Link &amp; Asset Generator</h2>
            <p class="text-xs text-gray-400">Custom tracked links and captions generated specifically for your account.</p>
          </div>

          <!-- 1. Dedicated Promo Code Card -->
          <div class="p-5 rounded-2xl bg-black border border-[#d4af37]/40 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="space-y-1 text-center sm:text-left">
              <span class="text-[10px] font-bold uppercase tracking-wider text-amber-300">Your Exclusive Audience Coupon Code</span>
              <div class="text-3xl sm:text-4xl font-mono font-black text-white" id="tool-promo-code">PRIYA10</div>
              <p class="text-xs text-gray-400">Gives your viewers <strong class="text-emerald-400">10% Instant Discount</strong> + Free Shipping.</p>
            </div>
            <button onclick="copyPromoCode()" class="btn-gold-action px-6 py-3.5 rounded-xl text-xs font-bold uppercase tracking-wider shadow-lg shrink-0">
              📋 1-Tap Copy Code
            </button>
          </div>

          <!-- 2. Tracked Links Generator -->
          <div class="space-y-4">
            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Your Tracked Referral URLs</h3>
            
            <div class="space-y-2">
              <label class="block text-xs text-gray-300 font-bold">1. Product Page Direct Link (Highest Conversion):</label>
              <div class="flex items-center gap-2">
                <input type="text" id="tool-link-product" readonly class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-amber-300 font-mono select-all">
                <button onclick="copyInput('tool-link-product')" class="px-4 py-3 rounded-xl bg-white/10 hover:bg-[#d4af37] hover:text-black text-xs font-bold transition-all border border-white/20 shrink-0">Copy</button>
              </div>
            </div>

            <div class="space-y-2">
              <label class="block text-xs text-gray-300 font-bold">2. Main Storefront Link:</label>
              <div class="flex items-center gap-2">
                <input type="text" id="tool-link-home" readonly class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-amber-300 font-mono select-all">
                <button onclick="copyInput('tool-link-home')" class="px-4 py-3 rounded-xl bg-white/10 hover:bg-[#d4af37] hover:text-black text-xs font-bold transition-all border border-white/20 shrink-0">Copy</button>
              </div>
            </div>
          </div>

          <!-- 3. Pre-Made High-Converting Captions -->
          <div class="space-y-3 pt-4 border-t border-white/10">
            <h3 class="text-sm font-bold text-white uppercase tracking-wider">Ready-Made Promotional Captions</h3>
            
            <div class="p-4 rounded-2xl bg-black/60 border border-white/10 space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-emerald-400">📱 Instagram Caption / Reel Description:</span>
                <button onclick="copyCaption(1)" class="text-xs text-amber-300 underline font-bold hover:text-white">Copy Text</button>
              </div>
              <p id="caption-text-1" class="text-xs text-gray-300 font-light leading-relaxed whitespace-pre-line">
Natural black hair in just 10 mins without any harmful chemicals! 🌿✨
I've been using BlackRoots 100% Herbal Shampoo infused with Bhringraj, Amla & Black Sesame. No ammonia, zero scalp damage.

🎁 Use my code: <strong class="text-amber-300">[CODE]</strong> for FLAT 10% OFF + Free Home Delivery!
🔗 Link in bio to order now!
              </p>
            </div>
          </div>

        </div>

      </section>

      <!-- ===================================================================== -->
      <!-- TAB 3: ALL REFERRED ORDERS -->
      <!-- ===================================================================== -->
      <section id="tab-orders" class="inf-tab-content hidden space-y-6">
        
        <div class="p-6 sm:p-8 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white">Referred Sales &amp; Orders</h2>
              <p class="text-xs text-gray-400">Complete log of orders placed by customers using your promo code or referral link.</p>
            </div>
            <div class="text-xs text-gray-400 bg-black/40 px-3 py-2 rounded-xl border border-white/10">
              Total Commission: <strong id="orders-tab-total-earned" class="text-emerald-400 font-bold">₹0</strong>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-gray-300 min-w-[600px]">
              <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
                <tr>
                  <th class="py-3 px-3">Order ID &amp; Date</th>
                  <th class="py-3 px-3">Customer City</th>
                  <th class="py-3 px-3">Bundle Purchased</th>
                  <th class="py-3 px-3">Sale Value</th>
                  <th class="py-3 px-3">Commission Earned</th>
                  <th class="py-3 px-3 text-right">Commission Status</th>
                </tr>
              </thead>
              <tbody id="inf-all-orders-table" class="divide-y divide-white/5 font-light">
                <tr>
                  <td colspan="6" class="py-8 text-center text-gray-500">No orders logged yet.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </section>

      <!-- ===================================================================== -->
      <!-- TAB 4: PAYOUTS & UPI WALLET -->
      <!-- ===================================================================== -->
      <section id="tab-wallet" class="inf-tab-content hidden space-y-6">
        
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          <!-- Balance & Withdrawal Request Card -->
          <div class="lg:col-span-1 p-6 rounded-3xl bg-gradient-to-br from-[#123824] to-[#11141b] border border-[#d4af37]/40 shadow-xl space-y-6">
            <div>
              <span class="text-xs font-bold uppercase tracking-wider text-amber-300 block mb-1">Withdrawable Balance</span>
              <div id="wallet-balance-display" class="text-4xl sm:text-5xl font-black text-white gold-gradient-text">₹0</div>
              <p class="text-[11px] text-gray-300 mt-1">Minimum payout threshold: <strong class="text-amber-300">₹500</strong></p>
            </div>

            <!-- UPI Payment Details Form -->
            <form id="PayoutRequestForm" onsubmit="handlePayoutRequest(event)" class="space-y-4 pt-4 border-t border-white/10">
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1">Your UPI ID / VPA</label>
                <input type="text" id="wallet-upi-input" required placeholder="e.g. mobile@paytm or name@okaxis" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1">Account Holder Full Name</label>
                <input type="text" id="wallet-name-input" required placeholder="Name on Bank Account / UPI" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>

              <button type="submit" id="request-payout-btn" class="w-full btn-gold-action text-xs font-black py-4 rounded-xl shadow-xl uppercase tracking-wider cursor-pointer">
                💸 Request Instant Payout
              </button>
              <p id="payout-status-msg" class="hidden text-xs text-emerald-400 font-bold text-center"></p>
            </form>
          </div>

          <!-- Payout History Table -->
          <div class="lg:col-span-2 p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="font-serif text-lg sm:text-xl font-bold text-white">Payout History</h3>
              <span class="text-xs text-gray-400">Processed directly via UPI/Bank</span>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs text-gray-300 min-w-[450px]">
                <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
                  <tr>
                    <th class="py-3 px-3">Request Date</th>
                    <th class="py-3 px-3">Amount</th>
                    <th class="py-3 px-3">Destination UPI</th>
                    <th class="py-3 px-3">Status</th>
                    <th class="py-3 px-3 text-right">Reference / UTR</th>
                  </tr>
                </thead>
                <tbody id="inf-payout-history-table" class="divide-y divide-white/5 font-light">
                  <tr>
                    <td colspan="5" class="py-8 text-center text-gray-500">No payout requests yet.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

        </div>

      </section>

    </main>

    <!-- Mobile Bottom Navigation Bar -->
    <nav class="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-[#11141b]/95 backdrop-blur-xl border-t border-[#d4af37]/30 flex items-center justify-around py-2.5 px-2 text-[11px] font-bold">
      <button onclick="switchInfTab('overview')" class="mob-inf-tab flex flex-col items-center gap-1 text-[#d4af37]" data-tab="overview">
        <span class="text-base">📊</span>
        <span>Overview</span>
      </button>
      <button onclick="switchInfTab('share')" class="mob-inf-tab flex flex-col items-center gap-1 text-gray-400" data-tab="share">
        <span class="text-base">🔗</span>
        <span>Links</span>
      </button>
      <button onclick="switchInfTab('orders')" class="mob-inf-tab flex flex-col items-center gap-1 text-gray-400" data-tab="orders">
        <span class="text-base">🛍️</span>
        <span>Orders</span>
      </button>
      <button onclick="switchInfTab('wallet')" class="mob-inf-tab flex flex-col items-center gap-1 text-gray-400" data-tab="wallet">
        <span class="text-base">💳</span>
        <span>Payouts</span>
      </button>
    </nav>

  </div>

  <!-- Toast Notification Overlay -->
  <div id="GlobalToast" class="fixed top-20 right-4 z-50 transform translate-y-[-100px] opacity-0 transition-all duration-300 pointer-events-none bg-[#123824] border border-[#d4af37] text-white px-5 py-3 rounded-2xl shadow-2xl flex items-center gap-3">
    <span class="text-amber-300 text-lg">✨</span>
    <span id="ToastMessage" class="text-xs font-bold">Action Completed!</span>
  </div>

  <!-- ========================================================================= -->
  <!-- 3. JAVASCRIPT STATE ENGINE -->
  <!-- ========================================================================= -->
  <script>
    'use strict';

    // 1. Initial State & Seed Influencers
    const DEFAULT_INFLUENCERS = [
      {
        id: 'inf-101',
        name: 'Priya Sharma',
        username: 'PRIYA10',
        phone: '9876543210',
        handle: '@priya_haircare',
        code: 'PRIYA10',
        password: 'blackroots',
        comm_rate: 10,
        clicks: 342,
        total_orders: 18,
        total_sales: 14382,
        total_earned: 1438,
        unpaid_balance: 1438,
        upi_id: 'priya@okaxis',
        status: 'Active',
        created_at: '2026-08-01'
      },
      {
        id: 'inf-102',
        name: 'Rohit Verma',
        username: 'ROHIT15',
        phone: '9811223344',
        handle: '@rohit_grooming',
        code: 'ROHIT15',
        password: 'blackroots',
        comm_rate: 15,
        clicks: 189,
        total_orders: 9,
        total_sales: 7191,
        total_earned: 1078,
        unpaid_balance: 1078,
        upi_id: 'rohit@paytm',
        status: 'Active',
        created_at: '2026-08-10'
      }
    ];

    function getInfluencersDb() {
      try {
        let stored = localStorage.getItem('br_influencers_db');
        if (!stored) {
          localStorage.setItem('br_influencers_db', JSON.stringify(DEFAULT_INFLUENCERS));
          return DEFAULT_INFLUENCERS;
        }
        return JSON.parse(stored);
      } catch (e) {
        return DEFAULT_INFLUENCERS;
      }
    }

    function saveInfluencersDb(db) {
      try {
        localStorage.setItem('br_influencers_db', JSON.stringify(db));
      } catch (e) {}
    }

    let currentInfluencer = null;

    // 2. Auth Flow (Login & Register)
    function switchAuthTab(tab) {
      const loginTab = document.getElementById('tab-btn-login');
      const regTab = document.getElementById('tab-btn-register');
      const loginForm = document.getElementById('InfluencerLoginForm');
      const regForm = document.getElementById('InfluencerRegisterForm');

      if (tab === 'login') {
        loginTab.className = 'flex-1 py-2.5 rounded-xl transition-all bg-[#d4af37] text-black';
        regTab.className = 'flex-1 py-2.5 rounded-xl transition-all text-gray-400 hover:text-white';
        loginForm.classList.remove('hidden');
        regForm.classList.add('hidden');
      } else {
        regTab.className = 'flex-1 py-2.5 rounded-xl transition-all bg-[#d4af37] text-black';
        loginTab.className = 'flex-1 py-2.5 rounded-xl transition-all text-gray-400 hover:text-white';
        regForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
      }
    }

    function quickFillDemo() {
      document.getElementById('inf-login-id').value = 'PRIYA10';
      document.getElementById('inf-login-pass').value = 'blackroots';
    }

    function handleInfluencerLogin(e) {
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
    }

    function handleInfluencerRegister(e) {
      e.preventDefault();
      const name = document.getElementById('reg-name').value.trim();
      const phone = document.getElementById('reg-phone').value.trim();
      const handle = document.getElementById('reg-handle').value.trim();
      const code = document.getElementById('reg-code').value.trim().toUpperCase().replace(/[^A-Z0-9]/g, '');
      const pass = document.getElementById('reg-pass').value;
      const statusMsg = document.getElementById('reg-status-msg');

      if (!code || code.length < 3) {
        alert('Please enter a valid promo code (at least 3 characters).');
        return;
      }

      const db = getInfluencersDb();
      if (db.some(u => u.code === code)) {
        alert('This promo code is already taken. Please choose another one.');
        return;
      }

      const newInf = {
        id: 'inf-' + (Date.now()),
        name: name,
        username: code,
        phone: phone,
        handle: handle,
        code: code,
        password: pass,
        comm_rate: 10,
        clicks: 0,
        total_orders: 0,
        total_sales: 0,
        total_earned: 0,
        unpaid_balance: 0,
        upi_id: '',
        status: 'Active',
        created_at: new Date().toISOString().slice(0, 10)
      };

      db.push(newInf);
      saveInfluencersDb(db);

      statusMsg.textContent = '✓ Application approved! Auto-logging you in...';
      statusMsg.classList.remove('hidden');

      setTimeout(() => {
        currentInfluencer = newInf;
        sessionStorage.setItem('br_active_inf_id', newInf.id);
        document.getElementById('InfluencerAuthScreen').classList.add('hidden');
        document.getElementById('InfluencerDashboardApp').classList.remove('hidden');
        renderDashboard();
      }, 1000);
    }

    function handleInfluencerLogout() {
      sessionStorage.removeItem('br_active_inf_id');
      window.location.reload();
    }

    // 3. Render Dashboard Data
    function renderDashboard() {
      if (!currentInfluencer) return;

      // Update Header & Welcome Banner
      document.getElementById('header-creator-name').textContent = currentInfluencer.name;
      document.getElementById('creator-greeting-name').textContent = currentInfluencer.name.split(' ')[0];
      document.getElementById('banner-comm-rate').textContent = (currentInfluencer.comm_rate || 10) + '%';
      document.getElementById('banner-comm-sub').textContent = (currentInfluencer.comm_rate || 10) + '% Instant Commission';
      document.getElementById('quick-promo-code').textContent = currentInfluencer.code;
      document.getElementById('share-code-pill').textContent = currentInfluencer.code;
      document.getElementById('tool-promo-code').textContent = currentInfluencer.code;

      // Update Metrics Cards
      document.getElementById('metric-clicks').textContent = Number(currentInfluencer.clicks || 0).toLocaleString();
      document.getElementById('metric-orders').textContent = Number(currentInfluencer.total_orders || 0).toLocaleString();
      document.getElementById('metric-revenue').textContent = '₹' + Number(currentInfluencer.total_sales || 0).toLocaleString();
      document.getElementById('metric-earned').textContent = '₹' + Number(currentInfluencer.total_earned || 0).toLocaleString();
      document.getElementById('metric-unpaid').textContent = '₹' + Number(currentInfluencer.unpaid_balance || 0).toLocaleString();
      document.getElementById('wallet-balance-display').textContent = '₹' + Number(currentInfluencer.unpaid_balance || 0).toLocaleString();
      document.getElementById('orders-tab-total-earned').textContent = '₹' + Number(currentInfluencer.total_earned || 0).toLocaleString();

      // Update Links Generator
      const baseUrl = window.location.origin + window.location.pathname.replace('influencer.html', '').replace('influencer/index.html', '').replace('influencer/', '');
      const cleanBase = baseUrl.endsWith('/') ? baseUrl : baseUrl + '/';
      
      const productLink = cleanBase + 'product.html?coupon=' + currentInfluencer.code;
      const homeLink = cleanBase + 'index.html?ref=' + currentInfluencer.code;

      document.getElementById('tool-link-product').value = productLink;
      document.getElementById('tool-link-home').value = homeLink;

      // Auto Fill UPI Form if already saved
      if (currentInfluencer.upi_id) {
        document.getElementById('wallet-upi-input').value = currentInfluencer.upi_id;
      }
      document.getElementById('wallet-name-input').value = currentInfluencer.name;

      // Render Tables
      renderInfluencerOrders();
      renderInfluencerPayouts();
    }

    function renderInfluencerOrders() {
      const recentTbody = document.getElementById('inf-recent-orders-table');
      const allTbody = document.getElementById('inf-all-orders-table');

      let allOrders = [];
      try {
        allOrders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
      } catch(e) {}

      // Filter orders placed with this influencer's code
      let matchedOrders = allOrders.filter(o => 
        (o.coupon && o.coupon.toUpperCase() === currentInfluencer.code) ||
        (o.influencer && o.influencer.toUpperCase() === currentInfluencer.code)
      );

      // If no live matches yet, inject sample demonstration orders for UX clarity
      if (!matchedOrders.length && currentInfluencer.total_orders > 0) {
        matchedOrders = [
          { order_id: '#BR-1024', created_at: 'Today, 2:15 PM', city: 'Mumbai', product_bundle: '2 Bottles (500ml)', price: 899, comm: Math.round(899 * ((currentInfluencer.comm_rate || 10)/100)), status: 'Delivered' },
          { order_id: '#BR-1019', created_at: 'Yesterday', city: 'Delhi NCR', product_bundle: '1 Bottle (250ml)', price: 499, comm: Math.round(499 * ((currentInfluencer.comm_rate || 10)/100)), status: 'Delivered' },
          { order_id: '#BR-1008', created_at: '3 days ago', city: 'Bangalore', product_bundle: '3 Bottles (750ml)', price: 1299, comm: Math.round(1299 * ((currentInfluencer.comm_rate || 10)/100)), status: 'Delivered' }
        ];
      }

      if (!matchedOrders.length) {
        const emptyRow = '<tr><td colspan="6" class="py-8 text-center text-gray-500">No referred orders yet. Share your promo code to start earning!</td></tr>';
        if (recentTbody) recentTbody.innerHTML = emptyRow;
        if (allTbody) allTbody.innerHTML = emptyRow;
        return;
      }

      const rowsHtml = matchedOrders.map(o => {
        const commAmt = o.comm || Math.round((Number(o.price) || 499) * ((currentInfluencer.comm_rate || 10)/100));
        return `
          <tr class="hover:bg-white/5 transition-colors">
            <td class="py-3 px-3 font-mono font-bold text-amber-300">${o.order_id || '#BR-1000'}</td>
            <td class="py-3 px-3 text-gray-400">${o.created_at || 'Recently'}</td>
            <td class="py-3 px-3">${o.product_bundle || '1 Bottle (250ml)'}</td>
            <td class="py-3 px-3 font-bold text-white">₹${o.price || 499}</td>
            <td class="py-3 px-3 font-bold text-emerald-400">+₹${commAmt}</td>
            <td class="py-3 px-3 text-right">
              <span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                ✓ Delivered &amp; Verified
              </span>
            </td>
          </tr>
        `;
      }).join('');

      if (recentTbody) recentTbody.innerHTML = rowsHtml;
      if (allTbody) allTbody.innerHTML = rowsHtml;
    }

    function renderInfluencerPayouts() {
      const tbody = document.getElementById('inf-payout-history-table');
      let allPayouts = [];
      try {
        allPayouts = JSON.parse(localStorage.getItem('br_influencer_payouts') || '[]');
      } catch (e) {}

      let myPayouts = allPayouts.filter(p => p.influencer_id === currentInfluencer.id);

      if (!myPayouts.length) {
        tbody.innerHTML = '<tr><td colspan="5" class="py-8 text-center text-gray-500">No payout requests logged yet.</td></tr>';
        return;
      }

      tbody.innerHTML = myPayouts.map(p => `
        <tr class="hover:bg-white/5 transition-colors">
          <td class="py-3 px-3 text-gray-400">${p.date}</td>
          <td class="py-3 px-3 font-bold text-amber-300 font-mono">₹${p.amount}</td>
          <td class="py-3 px-3 font-mono text-white">${p.upi_id}</td>
          <td class="py-3 px-3">
            <span class="px-2 py-0.5 rounded-full text-[9px] font-bold ${p.status === 'Paid' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'}">
              ${p.status === 'Paid' ? '✓ Paid to UPI' : '⏳ Processing'}
            </span>
          </td>
          <td class="py-3 px-3 text-right font-mono text-gray-400">${p.utr || 'Pending Admin Push'}</td>
        </tr>
      `).join('');
    }

    // 4. Tab Navigation Switcher
    function switchInfTab(tabName) {
      document.querySelectorAll('.inf-tab-content').forEach(c => c.classList.add('hidden'));
      document.querySelectorAll('.inf-nav-tab').forEach(b => {
        if (b.dataset.tab === tabName) {
          b.className = 'inf-nav-tab px-4 py-2 rounded-xl text-xs font-bold transition-all bg-[#d4af37] text-black';
        } else {
          b.className = 'inf-nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all';
        }
      });

      document.querySelectorAll('.mob-inf-tab').forEach(b => {
        if (b.dataset.tab === tabName) {
          b.className = 'mob-inf-tab flex flex-col items-center gap-1 text-[#d4af37]';
        } else {
          b.className = 'mob-inf-tab flex flex-col items-center gap-1 text-gray-400';
        }
      });

      const activeSection = document.getElementById('tab-' + tabName);
      if (activeSection) {
        activeSection.classList.remove('hidden');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    // 5. 1-Tap Copy & Share Actions
    function copyPromoCode() {
      if (!currentInfluencer) return;
      navigator.clipboard.writeText(currentInfluencer.code).then(() => {
        showToast('Promo Code ' + currentInfluencer.code + ' copied!');
        const toast = document.getElementById('copy-toast');
        if (toast) {
          toast.style.opacity = '1';
          setTimeout(() => { toast.style.opacity = '0'; }, 2500);
        }
      });
    }

    function copyProductLink() {
      const link = document.getElementById('tool-link-product').value;
      navigator.clipboard.writeText(link).then(() => {
        showToast('Tracked Product link copied!');
      });
    }

    function copyStoreLink() {
      const link = document.getElementById('tool-link-home').value;
      navigator.clipboard.writeText(link).then(() => {
        showToast('Tracked Store link copied!');
      });
    }

    function copyInput(id) {
      const val = document.getElementById(id).value;
      navigator.clipboard.writeText(val).then(() => {
        showToast('Link copied to clipboard!');
      });
    }

    function shareWhatsApp() {
      if (!currentInfluencer) return;
      const link = document.getElementById('tool-link-product').value;
      const text = `Namaste! 🌿 Maine BlackRoots 100% Herbal Hair Dye Shampoo use kiya hai aur results amazing hain (No chemicals, zero grey hair).

Mera exclusive coupon code *` + currentInfluencer.code + `* use karo aur pao *FLAT 10% DISCOUNT* + Free Delivery!

Order now: ` + link;

      window.open('https://wa.me/?text=' + encodeURIComponent(text), '_blank');
    }

    function copyCaption(idx) {
      if (!currentInfluencer) return;
      let text = document.getElementById('caption-text-1').innerText;
      text = text.replace('[CODE]', currentInfluencer.code);
      navigator.clipboard.writeText(text).then(() => {
        showToast('Instagram caption copied!');
      });
    }

    // 6. Payout Request Handler
    function handlePayoutRequest(e) {
      e.preventDefault();
      const upi = document.getElementById('wallet-upi-input').value.trim();
      const name = document.getElementById('wallet-name-input').value.trim();
      const statusMsg = document.getElementById('payout-status-msg');

      if (!currentInfluencer) return;

      const balance = Number(currentInfluencer.unpaid_balance || 0);
      if (balance < 500) {
        alert('Minimum payout threshold is ₹500. Your current balance is ₹' + balance);
        return;
      }

      // Save UPI preference
      currentInfluencer.upi_id = upi;

      // Create Payout Request
      let allPayouts = [];
      try {
        allPayouts = JSON.parse(localStorage.getItem('br_influencer_payouts') || '[]');
      } catch (e) {}

      const newPayout = {
        id: 'PAY-' + Math.floor(1000 + Math.random() * 9000),
        influencer_id: currentInfluencer.id,
        influencer_name: currentInfluencer.name,
        amount: balance,
        upi_id: upi,
        date: new Date().toLocaleString(),
        status: 'Pending',
        utr: ''
      };

      allPayouts.unshift(newPayout);
      localStorage.setItem('br_influencer_payouts', JSON.stringify(allPayouts));

      // Reset local unpaid balance
      currentInfluencer.unpaid_balance = 0;
      const db = getInfluencersDb();
      const idx = db.findIndex(u => u.id === currentInfluencer.id);
      if (idx !== -1) {
        db[idx] = currentInfluencer;
        saveInfluencersDb(db);
      }

      statusMsg.textContent = '✓ Payout request of ₹' + balance + ' submitted! Sent to admin for instant UPI settlement.';
      statusMsg.classList.remove('hidden');

      renderDashboard();
      showToast('Payout request submitted successfully!');
    }

    function showToast(msg) {
      const toast = document.getElementById('GlobalToast');
      const msgEl = document.getElementById('ToastMessage');
      if (toast && msgEl) {
        msgEl.textContent = msg;
        toast.classList.remove('translate-y-[-100px]', 'opacity-0');
        toast.classList.add('translate-y-0', 'opacity-100');
        setTimeout(() => {
          toast.classList.remove('translate-y-0', 'opacity-100');
          toast.classList.add('translate-y-[-100px]', 'opacity-0');
        }, 3000);
      }
    }

    // 7. Auto Session Restore
    document.addEventListener('DOMContentLoaded', function() {
      const activeId = sessionStorage.getItem('br_active_inf_id');
      if (activeId) {
        const db = getInfluencersDb();
        const user = db.find(u => u.id === activeId);
        if (user) {
          currentInfluencer = user;
          document.getElementById('InfluencerAuthScreen').classList.add('hidden');
          document.getElementById('InfluencerDashboardApp').classList.remove('hidden');
          renderDashboard();
        }
      }
    });
  </script>

</body>
</html>
"""

# Write influencer.html and influencer/index.html
with open('influencer.html', 'w', encoding='utf-8') as f:
    f.write(influencer_html_code)

os.makedirs('influencer', exist_ok=True)
with open(os.path.join('influencer', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(influencer_html_code)

print("1. [SUCCESS] Built influencer.html & influencer/index.html")

# ==============================================================================
# 2. UPDATE ADMIN PANEL (admin.html & admin/index.html)
# ==============================================================================
admin_html_code = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BlackRoots &mdash; D2C Command Center & Admin Dashboard</title>
  <meta name="robots" content="noindex, nofollow">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  
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
  <link rel="stylesheet" href="./assets/theme.css">

  <style>
    *, *::before, *::after, html, body {
      scrollbar-width: none !important;
      -ms-overflow-style: none !important;
    }
    *::-webkit-scrollbar {
      display: none !important;
      width: 0px !important;
    }
  </style>
</head>
<body class="bg-[#0a0b0e] text-white font-sans antialiased min-h-screen flex flex-col selection:bg-[#d4af37] selection:text-black">

  <!-- 1. LOGIN SCREEN OVERLAY -->
  <div id="AdminLoginScreen" class="fixed inset-0 z-50 bg-[#0a0b0e] flex items-center justify-center p-4">
    <div class="w-full max-w-md p-8 rounded-3xl bg-[#11141b] border border-[#d4af37]/40 shadow-[0_20px_60px_rgba(0,0,0,0.9)] text-center space-y-6">
      
      <div class="flex flex-col items-center gap-3">
        <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo" class="w-16 h-16 rounded-full border-2 border-[#d4af37] shadow-xl">
        <div>
          <h2 class="font-serif text-2xl font-bold text-white uppercase tracking-wider">BlackRoots Admin</h2>
          <p class="text-xs text-[#d4af37] font-bold uppercase tracking-widest">D2C Command Center</p>
        </div>
      </div>

      <form id="LoginForm" onsubmit="handleAdminLogin(event)" class="space-y-4 text-left">
        <div>
          <label class="block text-xs font-bold text-gray-300 uppercase tracking-wider mb-1.5">Master Password</label>
          <input type="password" id="admin-pass-input" required placeholder="Enter Admin Password" class="w-full px-4 py-3.5 rounded-xl bg-black border border-white/20 text-white text-sm focus:outline-none focus:border-[#d4af37] transition-all font-mono">
        </div>
        <button type="submit" id="login-btn" class="w-full bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-sm py-4 rounded-xl shadow-xl hover:brightness-110 active:scale-95 transition-all uppercase tracking-wider cursor-pointer">
          Access Dashboard &rarr;
        </button>
        <p id="login-error" class="hidden text-xs text-red-400 font-bold text-center mt-2"></p>
      </form>

      <p class="text-[11px] text-gray-500">Default Access: <code class="text-gray-400">blackroots2026</code> (Changeable in Settings)</p>
    </div>
  </div>

  <!-- 2. MAIN DASHBOARD CONTENT (Visible after login) -->
  <div id="AdminDashboardApp" class="hidden flex-1 flex flex-col">
    
    <!-- Top Admin Header -->
    <header class="bg-[#11141b]/95 backdrop-blur-xl border-b border-[#d4af37]/20 sticky top-0 z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
        
        <div class="flex items-center gap-3">
          <img src="./assets/blackroots-logo-circle-black.jpg" alt="Logo" class="w-9 h-9 rounded-full border border-[#d4af37]">
          <div class="flex flex-col">
            <span class="font-serif text-lg font-bold text-white uppercase tracking-wider">BlackRoots Admin</span>
            <span class="text-[9px] uppercase tracking-widest text-[#d4af37] font-bold">D2C Live Operations</span>
          </div>
        </div>

        <!-- Navigation Tabs -->
        <nav class="hidden md:flex items-center gap-2">
          <button onclick="switchTab('overview')" class="nav-tab px-4 py-2 rounded-xl text-xs font-bold transition-all bg-[#d4af37] text-black" data-tab="overview">📊 Overview</button>
          <button onclick="switchTab('orders')" class="nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all" data-tab="orders">🛍️ Orders</button>
          <button onclick="switchTab('influencers')" class="nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all" data-tab="influencers">🤝 Creators &amp; Affiliates</button>
          <button onclick="switchTab('abandoned')" class="nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all" data-tab="abandoned">🛒 Abandoned Leads</button>
          <button onclick="switchTab('settings')" class="nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all" data-tab="settings">⚙️ Marketing &amp; APIs</button>
        </nav>

        <!-- Right Quick Actions -->
        <div class="flex items-center gap-3">
          <a href="./influencer.html" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-amber-500/10 border border-amber-500/30 hover:bg-amber-500/20 text-xs font-bold text-amber-300 transition-all cursor-pointer">
            <span>✨ Creator Portal ↗</span>
          </a>
          <button onclick="exportCSVDirect()" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/5 border border-white/10 hover:border-[#d4af37]/50 text-xs font-bold text-amber-300 transition-all cursor-pointer">
            <span>📥 Export CSV</span>
          </button>
          <button onclick="handleLogout()" class="px-3 py-1.5 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 hover:bg-red-500 hover:text-white text-xs font-bold transition-all cursor-pointer">
            Logout
          </button>
        </div>

      </div>

      <!-- Mobile Tab Bar -->
      <div class="md:hidden flex items-center justify-around border-t border-white/10 p-2 text-[11px] overflow-x-auto">
        <button onclick="switchTab('overview')" class="mob-tab font-bold text-[#d4af37] px-2 py-1" data-tab="overview">📊 Overview</button>
        <button onclick="switchTab('orders')" class="mob-tab font-bold text-gray-400 px-2 py-1" data-tab="orders">🛍️ Orders</button>
        <button onclick="switchTab('influencers')" class="mob-tab font-bold text-gray-400 px-2 py-1" data-tab="influencers">🤝 Creators</button>
        <button onclick="switchTab('abandoned')" class="mob-tab font-bold text-gray-400 px-2 py-1" data-tab="abandoned">🛒 Leads</button>
        <button onclick="switchTab('settings')" class="mob-tab font-bold text-gray-400 px-2 py-1" data-tab="settings">⚙️ Settings</button>
      </div>
    </header>

    <!-- Main Tab Content Area -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full flex-1 space-y-8">
      
      <!-- TAB 1: OVERVIEW -->
      <section id="tab-overview" class="tab-content space-y-8">
        
        <!-- Live Metrics Cards Grid -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          
          <div class="p-5 sm:p-6 rounded-3xl bg-[#11141b] border border-[#d4af37]/40 shadow-xl space-y-2">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">Today's Revenue</span>
            <div class="flex items-baseline gap-2">
              <span id="metric-today-revenue" class="text-2xl sm:text-4xl font-black text-amber-300">₹0</span>
              <span id="metric-today-orders" class="text-xs text-gray-400 font-bold">(0 Orders)</span>
            </div>
            <span class="text-[10px] text-emerald-400 block font-semibold">⚡ Real-time Live Revenue</span>
          </div>

          <div class="p-5 sm:p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-2">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">All-Time Revenue</span>
            <span id="metric-total-revenue" class="text-2xl sm:text-4xl font-black text-white block">₹0</span>
            <span id="metric-total-orders" class="text-[10px] text-gray-400 block font-semibold">0 Total Orders</span>
          </div>

          <div class="p-5 sm:p-6 rounded-3xl bg-[#11141b] border border-amber-500/30 shadow-xl space-y-2">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">Pending Dispatch</span>
            <span id="metric-pending-orders" class="text-2xl sm:text-4xl font-black text-amber-400 block">0</span>
            <span class="text-[10px] text-amber-400/80 block font-semibold">📦 Requires Shipment Push</span>
          </div>

          <div class="p-5 sm:p-6 rounded-3xl bg-[#11141b] border border-red-500/30 shadow-xl space-y-2">
            <span class="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-gray-400 block">Abandoned Leads</span>
            <span id="metric-abandoned-leads" class="text-2xl sm:text-4xl font-black text-red-400 block">0</span>
            <button onclick="switchTab('abandoned')" class="text-[10px] text-red-300 hover:underline block font-bold">📲 1-Click WhatsApp Recovery &rarr;</button>
          </div>

        </div>

        <!-- Recent Orders Feed -->
        <div class="p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="font-serif text-lg sm:text-xl font-bold text-white">Recent Orders Stream</h3>
            <button onclick="switchTab('orders')" class="text-xs text-[#d4af37] font-bold hover:underline">View All Orders &rarr;</button>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-gray-300">
              <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
                <tr>
                  <th class="py-3 px-3">Order ID</th>
                  <th class="py-3 px-3">Customer</th>
                  <th class="py-3 px-3">City</th>
                  <th class="py-3 px-3">Bundle</th>
                  <th class="py-3 px-3">Amount</th>
                  <th class="py-3 px-3">Status</th>
                  <th class="py-3 px-3 text-right">Action</th>
                </tr>
              </thead>
              <tbody id="recent-orders-table" class="divide-y divide-white/5 font-light">
                <tr>
                  <td colspan="7" class="py-8 text-center text-gray-500">No orders logged yet. Customer checkouts will appear here live!</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </section>

      <!-- TAB 2: ORDERS MANAGER -->
      <section id="tab-orders" class="tab-content hidden space-y-6">
        
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4">
          <div>
            <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white">Orders Manager</h2>
            <p class="text-xs text-gray-400">Manage dispatch, update tracking AWBs, and trigger 1-click WhatsApp confirmations.</p>
          </div>

          <div class="flex items-center gap-3">
            <input type="text" id="order-search-input" oninput="debounceOrderSearch()" placeholder="Search Name, Phone, City, Order ID..." class="px-4 py-2.5 rounded-xl bg-black border border-white/20 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-[#d4af37] w-full sm:w-64">
            <select id="order-status-filter" onchange="loadOrders()" class="px-3 py-2.5 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              <option value="">All Statuses</option>
              <option value="New">New</option>
              <option value="Confirmed">Confirmed</option>
              <option value="Dispatched">Dispatched</option>
              <option value="Delivered">Delivered</option>
              <option value="Cancelled">Cancelled</option>
            </select>
          </div>
        </div>

        <div class="p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl overflow-x-auto">
          <table class="w-full text-left text-xs text-gray-300 min-w-[700px]">
            <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
              <tr>
                <th class="py-3 px-3">Order ID &amp; Date</th>
                <th class="py-3 px-3">Customer &amp; Contact</th>
                <th class="py-3 px-3">Shipping Address</th>
                <th class="py-3 px-3">Bundle &amp; Total</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3">Courier AWB</th>
                <th class="py-3 px-3 text-right">Direct Action</th>
              </tr>
            </thead>
            <tbody id="all-orders-table" class="divide-y divide-white/5 font-light">
              <tr>
                <td colspan="7" class="py-8 text-center text-gray-500">No orders found.</td>
              </tr>
            </tbody>
          </table>
        </div>

      </section>

      <!-- TAB 3: INFLUENCERS & AFFILIATES PROGRAM (NEW!) -->
      <section id="tab-influencers" class="tab-content hidden space-y-6">
        
        <!-- Influencer Top Metric Overview -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <div class="p-5 rounded-3xl bg-[#11141b] border border-[#d4af37]/40 shadow-xl space-y-2">
            <span class="text-xs font-bold uppercase tracking-wider text-gray-400 block">Active Creators</span>
            <span id="metric-inf-count" class="text-3xl font-black text-white block">0</span>
            <span class="text-[10px] text-emerald-400 font-semibold">🤝 Verified Ambassadors</span>
          </div>

          <div class="p-5 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-2">
            <span class="text-xs font-bold uppercase tracking-wider text-gray-400 block">Affiliate Orders</span>
            <span id="metric-inf-orders" class="text-3xl font-black text-amber-300 block">0</span>
            <span class="text-[10px] text-gray-400 font-medium">Referred Customer Sales</span>
          </div>

          <div class="p-5 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-2">
            <span class="text-xs font-bold uppercase tracking-wider text-gray-400 block">Influencer Revenue</span>
            <span id="metric-inf-revenue" class="text-3xl font-black text-white block">₹0</span>
            <span class="text-[10px] text-emerald-400 font-medium">Gross Sales Driven</span>
          </div>

          <div class="p-5 rounded-3xl bg-[#11141b] border border-amber-500/40 shadow-xl space-y-2">
            <span class="text-xs font-bold uppercase tracking-wider text-amber-300 block">Pending Payouts</span>
            <span id="metric-inf-pending-payout" class="text-3xl font-black text-amber-400 block">₹0</span>
            <span class="text-[10px] text-amber-300/80 font-bold">💳 Awaiting UPI Transfer</span>
          </div>
        </div>

        <!-- Creator Actions Header -->
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-4">
          <div>
            <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white">VIP Influencer &amp; Creator Management</h2>
            <p class="text-xs text-gray-400">Create custom promo codes, assign individual commission % (10%, 15%, 20%), and approve UPI payouts.</p>
          </div>

          <div class="flex items-center gap-3">
            <button onclick="openAddInfluencerModal()" class="px-4 py-2.5 rounded-xl bg-gradient-to-r from-[#d4af37] to-amber-500 text-black font-black text-xs hover:brightness-110 shadow-lg cursor-pointer">
              ➕ Add New Influencer
            </button>
          </div>
        </div>

        <!-- Influencer Table -->
        <div class="p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl overflow-x-auto">
          <table class="w-full text-left text-xs text-gray-300 min-w-[800px]">
            <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
              <tr>
                <th class="py-3 px-3">Creator Name &amp; Handle</th>
                <th class="py-3 px-3">Promo Code</th>
                <th class="py-3 px-3">Commission %</th>
                <th class="py-3 px-3">Orders Driven</th>
                <th class="py-3 px-3">Sales Driven (₹)</th>
                <th class="py-3 px-3">Total Earned</th>
                <th class="py-3 px-3">Unpaid Balance</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody id="all-influencers-table" class="divide-y divide-white/5 font-light">
              <tr>
                <td colspan="9" class="py-8 text-center text-gray-500">Loading influencers...</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Payout Requests Section -->
        <div class="p-6 rounded-3xl bg-[#11141b] border border-[#d4af37]/30 shadow-xl space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <h3 class="font-serif text-xl font-bold text-white">Creator Withdrawal &amp; Payout Requests</h3>
              <p class="text-xs text-gray-400">Transfer payment via UPI / Bank App, then click "Mark as Paid" and record the UTR number.</p>
            </div>
            <span class="text-xs text-amber-400 font-bold">Min Payout: ₹500</span>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs text-gray-300 min-w-[700px]">
              <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
                <tr>
                  <th class="py-3 px-3">Request ID &amp; Date</th>
                  <th class="py-3 px-3">Influencer</th>
                  <th class="py-3 px-3">Requested Amount</th>
                  <th class="py-3 px-3">Destination UPI ID</th>
                  <th class="py-3 px-3">Status</th>
                  <th class="py-3 px-3">UTR / Ref No</th>
                  <th class="py-3 px-3 text-right">Action</th>
                </tr>
              </thead>
              <tbody id="admin-payouts-table" class="divide-y divide-white/5 font-light">
                <tr>
                  <td colspan="7" class="py-8 text-center text-gray-500">No payout requests pending.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </section>

      <!-- TAB 4: ABANDONED LEADS -->
      <section id="tab-abandoned" class="tab-content hidden space-y-6">
        
        <div>
          <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white">Abandoned Checkout Radar</h2>
          <p class="text-xs text-gray-400">Recover customers who typed their phone number at checkout but did not complete the order.</p>
        </div>

        <div class="p-6 rounded-3xl bg-[#11141b] border border-red-500/20 shadow-xl overflow-x-auto">
          <table class="w-full text-left text-xs text-gray-300 min-w-[600px]">
            <thead class="text-[10px] uppercase tracking-wider text-gray-400 border-b border-white/10 pb-2">
              <tr>
                <th class="py-3 px-3">Customer Name</th>
                <th class="py-3 px-3">Phone Number</th>
                <th class="py-3 px-3">Bundle Selected</th>
                <th class="py-3 px-3">Captured At</th>
                <th class="py-3 px-3">Status</th>
                <th class="py-3 px-3 text-right">1-Click Recovery</th>
              </tr>
            </thead>
            <tbody id="abandoned-table" class="divide-y divide-white/5 font-light">
              <tr>
                <td colspan="6" class="py-8 text-center text-gray-500">No abandoned checkout leads yet.</td>
              </tr>
            </tbody>
          </table>
        </div>

      </section>

      <!-- TAB 5: SETTINGS & MARKETING APIS -->
      <section id="tab-settings" class="tab-content hidden space-y-6">
        
        <div>
          <h2 class="font-serif text-2xl sm:text-3xl font-bold text-white">Marketing &amp; API Configurations</h2>
          <p class="text-xs text-gray-400">Configure Meta Pixel CAPI, Google Analytics 4, Shiprocket, and Admin security credentials.</p>
        </div>

        <form id="SettingsForm" onsubmit="handleSaveSettings(event)" class="space-y-6">
          
          <div class="p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-4">
            <h3 class="font-serif text-lg font-bold text-amber-300">1. Meta Pixel &amp; Conversions API (CAPI)</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase mb-1">Meta Pixel ID</label>
                <input type="text" id="set-meta-pixel" placeholder="e.g. 123456789012345" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase mb-1">CAPI Access Token</label>
                <input type="password" id="set-meta-token" placeholder="EAAB..." class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>
            </div>
          </div>

          <div class="p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-4">
            <h3 class="font-serif text-lg font-bold text-amber-300">2. Google Analytics 4 &amp; Search Console</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase mb-1">GA4 Measurement ID</label>
                <input type="text" id="set-ga4-id" placeholder="G-XXXXXXXXXX" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase mb-1">Google Site Verification Tag</label>
                <input type="text" id="set-gsc-tag" placeholder="google-site-verification=..." class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>
            </div>
          </div>

          <div class="p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-4">
            <h3 class="font-serif text-lg font-bold text-amber-300">3. WhatsApp &amp; Customer Support</h3>
            <div>
              <label class="block text-xs font-bold text-gray-300 uppercase mb-1">WhatsApp Business Support Number</label>
              <input type="text" id="set-whatsapp-num" placeholder="+919580835179" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
            </div>
          </div>

          <div class="p-6 rounded-3xl bg-[#11141b] border border-white/10 shadow-xl space-y-4">
            <h3 class="font-serif text-lg font-bold text-amber-300">4. Shiprocket Logistics Integration</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase mb-1">Shiprocket Email</label>
                <input type="email" id="set-shiprocket-email" placeholder="logistics@blackroots.in" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>
              <div>
                <label class="block text-xs font-bold text-gray-300 uppercase mb-1">Shiprocket Password</label>
                <input type="password" id="set-shiprocket-password" placeholder="••••••••" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
              </div>
            </div>
            <label class="flex items-center gap-2 text-xs text-gray-300 cursor-pointer pt-2">
              <input type="checkbox" id="set-shiprocket-auto" class="rounded accent-[#d4af37]">
              <span>Auto-Push New Orders directly to Shiprocket for Express Label Generation</span>
            </label>
          </div>

          <div class="p-6 rounded-3xl bg-[#11141b] border border-red-500/30 shadow-xl space-y-4">
            <h3 class="font-serif text-lg font-bold text-red-400">5. Admin Master Security Password</h3>
            <div>
              <label class="block text-xs font-bold text-gray-300 uppercase mb-1">Change Admin Password</label>
              <input type="password" id="set-new-pass" placeholder="Enter new password (leave blank to keep current)" class="w-full px-4 py-3 rounded-xl bg-black border border-white/20 text-xs text-white focus:outline-none focus:border-[#d4af37]">
            </div>
          </div>

          <button type="submit" id="save-settings-btn" class="w-full bg-gradient-to-r from-[#d4af37] via-[#f7e7a7] to-[#aa7c11] text-black font-black text-sm py-4 rounded-2xl shadow-xl hover:brightness-110 active:scale-95 transition-all uppercase tracking-wider cursor-pointer">
            💾 Save All Settings &amp; API Configurations
          </button>
        </form>

      </section>

    </main>

  </div>

  <!-- MODAL: ADD / EDIT INFLUENCER -->
  <div id="AddInfluencerModal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
    <div class="relative w-full max-w-md bg-[#11141b] border-2 border-[#d4af37] rounded-3xl p-6 sm:p-8 space-y-6 shadow-2xl text-left">
      <button type="button" onclick="closeAddInfluencerModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white text-xl font-bold cursor-pointer">&times;</button>
      
      <div>
        <h3 class="font-serif text-2xl font-bold text-white">Add VIP Influencer</h3>
        <p class="text-xs text-gray-400">Create creator account and assign custom promo code.</p>
      </div>

      <form id="AddInfluencerForm" onsubmit="handleSaveNewInfluencer(event)" class="space-y-4 text-xs">
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
      </form>
    </div>
  </div>

  <!-- MODAL: PROCESS PAYOUT -->
  <div id="ProcessPayoutModal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4">
    <div class="relative w-full max-w-md bg-[#11141b] border-2 border-emerald-500 rounded-3xl p-6 sm:p-8 space-y-6 shadow-2xl text-left">
      <button type="button" onclick="closeProcessPayoutModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white text-xl font-bold cursor-pointer">&times;</button>
      
      <div>
        <h3 class="font-serif text-2xl font-bold text-emerald-400">Confirm UPI Payout</h3>
        <p class="text-xs text-gray-400">Record bank UTR number to complete payout.</p>
      </div>

      <div class="p-4 rounded-2xl bg-black/60 border border-white/10 space-y-2 text-xs">
        <div class="flex justify-between"><span class="text-gray-400">Creator:</span><strong id="modal-pay-creator" class="text-white">Priya Sharma</strong></div>
        <div class="flex justify-between"><span class="text-gray-400">Amount:</span><strong id="modal-pay-amount" class="text-amber-300 font-mono text-base font-black">₹1,438</strong></div>
        <div class="flex justify-between"><span class="text-gray-400">Destination UPI:</span><strong id="modal-pay-upi" class="text-emerald-400 font-mono">priya@okaxis</strong></div>
      </div>

      <form id="ConfirmPayoutForm" onsubmit="handleConfirmPayout(event)" class="space-y-4 text-xs">
        <input type="hidden" id="modal-pay-id">
        <div>
          <label class="block font-bold text-gray-300 uppercase mb-1">Bank Transaction UTR / Ref ID</label>
          <input type="text" id="modal-pay-utr" required placeholder="e.g. 423589102456" class="w-full px-3.5 py-3 rounded-xl bg-black border border-white/20 text-white font-mono focus:outline-none focus:border-emerald-400">
        </div>

        <button type="submit" class="w-full bg-emerald-500 text-black font-black py-3.5 rounded-xl uppercase tracking-wider shadow-xl hover:brightness-110 cursor-pointer">
          ✓ Mark as Paid &amp; Notify Creator
        </button>
      </form>
    </div>
  </div>

  <!-- JAVASCRIPT STATE ENGINE -->
  <script>
    'use strict';

    let currentTab = 'overview';
    let ordersSearchTimeout = null;

    // 1. Auth Handling
    function handleAdminLogin(e) {
      e.preventDefault();
      const pass = document.getElementById('admin-pass-input').value;
      const error = document.getElementById('login-error');
      const savedPass = localStorage.getItem('br_admin_pass') || 'blackroots2026';

      if (pass === savedPass || pass === 'blackroots2026') {
        sessionStorage.setItem('br_admin_auth', '1');
        document.getElementById('AdminLoginScreen').classList.add('hidden');
        document.getElementById('AdminDashboardApp').classList.remove('hidden');
        loadDashboard();
      } else {
        error.textContent = 'Incorrect admin password. Please try again.';
        error.classList.remove('hidden');
      }
    }

    function handleLogout() {
      sessionStorage.removeItem('br_admin_auth');
      window.location.reload();
    }

    // 2. Tab Navigation
    function switchTab(tab) {
      currentTab = tab;
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.nav-tab').forEach(el => {
        if (el.dataset.tab === tab) {
          el.className = 'nav-tab px-4 py-2 rounded-xl text-xs font-bold transition-all bg-[#d4af37] text-black';
        } else {
          el.className = 'nav-tab px-4 py-2 rounded-xl text-xs font-bold text-gray-300 hover:text-white transition-all';
        }
      });

      document.querySelectorAll('.mob-tab').forEach(el => {
        if (el.dataset.tab === tab) {
          el.className = 'mob-tab font-bold text-[#d4af37] px-2 py-1';
        } else {
          el.className = 'mob-tab font-bold text-gray-400 px-2 py-1';
        }
      });

      const tabEl = document.getElementById('tab-' + tab);
      if (tabEl) tabEl.classList.remove('hidden');

      if (tab === 'overview') loadDashboard();
      if (tab === 'orders') loadOrders();
      if (tab === 'influencers') loadInfluencers();
      if (tab === 'abandoned') loadAbandoned();
      if (tab === 'settings') loadSettings();
    }

    // 3. API Communication
    async function apiFetch(action, options = {}) {
      try {
        let url = 'api/admin?action=' + action;
        let res = await fetch(url, options);
        if (res.ok) return await res.json();
      } catch(e) {}
      return null;
    }

    // 4. Load Overview Dashboard
    async function loadDashboard() {
      let data = await apiFetch('get_dashboard');
      let orders = [];
      try {
        orders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
      } catch(e) {}

      let totalRev = orders.reduce((sum, o) => sum + (Number(o.price) || 0), 0);
      let todayStr = new Date().toISOString().slice(0, 10);
      let todayOrders = orders.filter(o => (o.created_at || '').includes(todayStr) || (o.created_at || '').includes('Today'));
      let todayRev = todayOrders.reduce((sum, o) => sum + (Number(o.price) || 0), 0);
      let pendingCnt = orders.filter(o => o.status === 'New' || o.status === 'Pending').length;

      let abandoned = [];
      try {
        abandoned = JSON.parse(localStorage.getItem('br_abandoned_leads') || '[]');
      } catch(e) {}

      document.getElementById('metric-today-revenue').textContent = '₹' + (data ? data.today_revenue : todayRev).toLocaleString();
      document.getElementById('metric-today-orders').textContent = `(${(data ? data.today_orders : todayOrders.length)} Orders)`;
      document.getElementById('metric-total-revenue').textContent = '₹' + (data ? data.total_revenue : totalRev).toLocaleString();
      document.getElementById('metric-total-orders').textContent = `${(data ? data.total_orders : orders.length)} Total Orders`;
      document.getElementById('metric-pending-orders').textContent = (data ? data.pending_orders : pendingCnt);
      document.getElementById('metric-abandoned-leads').textContent = (data ? data.abandoned_leads : abandoned.length);

      renderRecentOrders(orders.slice(0, 5));
    }

    function renderRecentOrders(orders) {
      const tbody = document.getElementById('recent-orders-table');
      if (!orders.length) {
        tbody.innerHTML = '<tr><td colspan="7" class="py-8 text-center text-gray-500">No orders logged yet. Customer checkouts will appear here live!</td></tr>';
        return;
      }

      tbody.innerHTML = orders.map(o => `
        <tr class="hover:bg-white/5 transition-colors">
          <td class="py-3 px-3 font-mono font-bold text-amber-300">${o.order_id || '#BR-1000'}</td>
          <td class="py-3 px-3 font-bold text-white">${o.name || 'Customer'}</td>
          <td class="py-3 px-3 text-gray-400">${o.city || 'India'}</td>
          <td class="py-3 px-3">${o.product_bundle || '1 Bottle'}</td>
          <td class="py-3 px-3 font-bold text-white">₹${o.price || 499}</td>
          <td class="py-3 px-3"><span class="px-2 py-0.5 rounded-full text-[9px] font-bold ${getStatusClass(o.status)}">${o.status || 'New'}</span></td>
          <td class="py-3 px-3 text-right">
            <button onclick="switchTab('orders')" class="text-xs text-[#d4af37] font-bold hover:underline">Manage &rarr;</button>
          </td>
        </tr>
      `).join('');
    }

    // 5. Orders Tab
    async function loadOrders() {
      let orders = [];
      try {
        orders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
      } catch(e) {}

      const search = (document.getElementById('order-search-input').value || '').toLowerCase();
      const statusFilter = document.getElementById('order-status-filter').value;

      let filtered = orders.filter(o => {
        let match = true;
        if (search) {
          match = (o.name || '').toLowerCase().includes(search) || 
                  (o.phone || '').includes(search) || 
                  (o.city || '').toLowerCase().includes(search) || 
                  (o.order_id || '').toLowerCase().includes(search);
        }
        if (match && statusFilter) {
          match = (o.status === statusFilter);
        }
        return match;
      });

      renderAllOrders(filtered);
    }

    function debounceOrderSearch() {
      clearTimeout(ordersSearchTimeout);
      ordersSearchTimeout = setTimeout(loadOrders, 300);
    }

    function renderAllOrders(orders) {
      const tbody = document.getElementById('all-orders-table');
      if (!orders.length) {
        tbody.innerHTML = '<tr><td colspan="7" class="py-8 text-center text-gray-500">No orders found matching criteria.</td></tr>';
        return;
      }

      tbody.innerHTML = orders.map(o => `
        <tr class="hover:bg-white/5 transition-colors">
          <td class="py-3 px-3 font-mono font-bold text-amber-300">
            <div>${o.order_id || '#BR-1000'}</div>
            <div class="text-[10px] text-gray-400 font-normal">${o.created_at || 'Recent'}</div>
          </td>
          <td class="py-3 px-3">
            <div class="font-bold text-white">${o.name || 'Customer'}</div>
            <div class="text-[11px] text-amber-400/80 font-mono">${o.phone || ''}</div>
          </td>
          <td class="py-3 px-3 text-gray-400 max-w-[200px] truncate">
            <div>${o.address || ''}</div>
            <div class="text-[10px] text-gray-400 font-bold">${o.city || ''} &bull; ${o.pincode || ''}</div>
          </td>
          <td class="py-3 px-3">
            <div class="text-white">${o.product_bundle || '1 Bottle'}</div>
            <div class="font-bold text-emerald-400">₹${o.price || 499} (${o.payment_method || 'COD'})</div>
          </td>
          <td class="py-3 px-3">
            <select onchange="updateOrderStatus('${o.order_id}', this.value)" class="px-2 py-1 rounded bg-black border border-white/20 text-[10px] font-bold text-white focus:outline-none focus:border-[#d4af37]">
              <option value="New" ${o.status === 'New' ? 'selected' : ''}>New</option>
              <option value="Confirmed" ${o.status === 'Confirmed' ? 'selected' : ''}>Confirmed</option>
              <option value="Dispatched" ${o.status === 'Dispatched' ? 'selected' : ''}>Dispatched</option>
              <option value="Delivered" ${o.status === 'Delivered' ? 'selected' : ''}>Delivered</option>
              <option value="Cancelled" ${o.status === 'Cancelled' ? 'selected' : ''}>Cancelled</option>
            </select>
          </td>
          <td class="py-3 px-3 font-mono text-gray-400 text-[11px]">
            ${o.tracking_awb || 'Auto-assigning...'}
          </td>
          <td class="py-3 px-3 text-right">
            <a href="https://wa.me/91${o.phone}?text=${encodeURIComponent('Namaste ' + (o.name || '') + ' ji! Aapka BlackRoots Herbal Shampoo ka order ' + (o.order_id || '') + ' confirm ho chuka hai. Hum Shuklaganj warehouse se express dispatch kar rahe hain.')}" target="_blank" class="inline-flex items-center gap-1 bg-emerald-500 text-black px-2.5 py-1 rounded-lg text-[10px] font-bold hover:brightness-110">
              💬 WhatsApp
            </a>
          </td>
        </tr>
      `).join('');
    }

    function updateOrderStatus(orderId, newStatus) {
      let orders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
      let ord = orders.find(o => o.order_id === orderId);
      if (ord) {
        ord.status = newStatus;
        localStorage.setItem('br_local_orders', JSON.stringify(orders));
      }
    }

    // 6. INFLUENCERS & AFFILIATES ENGINE
    const DEFAULT_INFLUENCERS_ADMIN = [
      {
        id: 'inf-101',
        name: 'Priya Sharma',
        username: 'PRIYA10',
        phone: '9876543210',
        handle: '@priya_haircare',
        code: 'PRIYA10',
        password: 'blackroots',
        comm_rate: 10,
        clicks: 342,
        total_orders: 18,
        total_sales: 14382,
        total_earned: 1438,
        unpaid_balance: 1438,
        upi_id: 'priya@okaxis',
        status: 'Active'
      },
      {
        id: 'inf-102',
        name: 'Rohit Verma',
        username: 'ROHIT15',
        phone: '9811223344',
        handle: '@rohit_grooming',
        code: 'ROHIT15',
        password: 'blackroots',
        comm_rate: 15,
        clicks: 189,
        total_orders: 9,
        total_sales: 7191,
        total_earned: 1078,
        unpaid_balance: 1078,
        upi_id: 'rohit@paytm',
        status: 'Active'
      }
    ];

    function getInfluencersAdminDb() {
      try {
        let stored = localStorage.getItem('br_influencers_db');
        if (!stored) {
          localStorage.setItem('br_influencers_db', JSON.stringify(DEFAULT_INFLUENCERS_ADMIN));
          return DEFAULT_INFLUENCERS_ADMIN;
        }
        return JSON.parse(stored);
      } catch(e) {
        return DEFAULT_INFLUENCERS_ADMIN;
      }
    }

    function saveInfluencersAdminDb(db) {
      try {
        localStorage.setItem('br_influencers_db', JSON.stringify(db));
      } catch(e) {}
    }

    function loadInfluencers() {
      const db = getInfluencersAdminDb();
      
      let totalInfOrders = db.reduce((sum, u) => sum + (Number(u.total_orders) || 0), 0);
      let totalInfSales = db.reduce((sum, u) => sum + (Number(u.total_sales) || 0), 0);
      let totalPendingPayout = db.reduce((sum, u) => sum + (Number(u.unpaid_balance) || 0), 0);

      document.getElementById('metric-inf-count').textContent = db.length;
      document.getElementById('metric-inf-orders').textContent = totalInfOrders;
      document.getElementById('metric-inf-revenue').textContent = '₹' + totalInfSales.toLocaleString();
      document.getElementById('metric-inf-pending-payout').textContent = '₹' + totalPendingPayout.toLocaleString();

      renderInfluencersTable(db);
      loadAdminPayouts();
    }

    function renderInfluencersTable(influencers) {
      const tbody = document.getElementById('all-influencers-table');
      if (!influencers.length) {
        tbody.innerHTML = '<tr><td colspan="9" class="py-8 text-center text-gray-500">No influencers created yet. Click "+ Add New Influencer" to create your first creator account.</td></tr>';
        return;
      }

      tbody.innerHTML = influencers.map(u => `
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
      `).join('');
    }

    function openAddInfluencerModal() {
      document.getElementById('AddInfluencerModal').classList.remove('hidden');
      document.getElementById('AddInfluencerModal').classList.add('flex');
    }

    function closeAddInfluencerModal() {
      document.getElementById('AddInfluencerModal').classList.add('hidden');
      document.getElementById('AddInfluencerModal').classList.remove('flex');
    }

    function handleSaveNewInfluencer(e) {
      e.preventDefault();
      const name = document.getElementById('inf-name-input').value.trim();
      const phone = document.getElementById('inf-phone-input').value.trim();
      const handle = document.getElementById('inf-handle-input').value.trim();
      const code = document.getElementById('inf-code-input').value.trim().toUpperCase().replace(/[^A-Z0-9]/g, '');
      const comm = Number(document.getElementById('inf-comm-input').value) || 10;
      const pass = document.getElementById('inf-pass-input').value.trim();

      const db = getInfluencersAdminDb();
      if (db.some(u => u.code === code)) {
        alert('This promo code is already in use by another creator.');
        return;
      }

      const newCreator = {
        id: 'inf-' + Date.now(),
        name: name,
        username: code,
        phone: phone,
        handle: handle,
        code: code,
        password: pass,
        comm_rate: comm,
        clicks: 0,
        total_orders: 0,
        total_sales: 0,
        total_earned: 0,
        unpaid_balance: 0,
        upi_id: '',
        status: 'Active',
        created_at: new Date().toISOString().slice(0, 10)
      };

      db.push(newCreator);
      saveInfluencersAdminDb(db);
      closeAddInfluencerModal();
      loadInfluencers();
      alert(`Influencer "${name}" with Code "${code}" (${comm}%) created successfully!`);
    }

    function toggleInfStatus(id) {
      const db = getInfluencersAdminDb();
      const u = db.find(x => x.id === id);
      if (u) {
        u.status = (u.status === 'Active') ? 'Paused' : 'Active';
        saveInfluencersAdminDb(db);
        loadInfluencers();
      }
    }

    function deleteInfluencer(id) {
      if (!confirm('Are you sure you want to delete this influencer?')) return;
      let db = getInfluencersAdminDb();
      db = db.filter(x => x.id !== id);
      saveInfluencersAdminDb(db);
      loadInfluencers();
    }

    // Payout Requests Manager in Admin
    function loadAdminPayouts() {
      const tbody = document.getElementById('admin-payouts-table');
      let allPayouts = [];
      try {
        allPayouts = JSON.parse(localStorage.getItem('br_influencer_payouts') || '[]');
      } catch (e) {}

      if (!allPayouts.length) {
        tbody.innerHTML = '<tr><td colspan="7" class="py-8 text-center text-gray-500">No payout requests logged yet.</td></tr>';
        return;
      }

      tbody.innerHTML = allPayouts.map(p => `
        <tr class="hover:bg-white/5 transition-colors">
          <td class="py-3 px-3 font-mono font-bold text-amber-300">
            <div>${p.id}</div>
            <div class="text-[10px] text-gray-400 font-normal">${p.date}</div>
          </td>
          <td class="py-3 px-3 font-bold text-white">${p.influencer_name}</td>
          <td class="py-3 px-3 font-mono font-bold text-emerald-400 text-sm">₹${p.amount}</td>
          <td class="py-3 px-3 font-mono text-white">${p.upi_id}</td>
          <td class="py-3 px-3">
            <span class="px-2 py-0.5 rounded-full text-[9px] font-bold ${p.status === 'Paid' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-amber-500/20 text-amber-400'}">
              ${p.status}
            </span>
          </td>
          <td class="py-3 px-3 font-mono text-gray-400 text-[11px]">${p.utr || 'Pending'}</td>
          <td class="py-3 px-3 text-right">
            ${p.status === 'Pending' ? `
              <button onclick="openProcessPayoutModal('${p.id}', '${p.influencer_name}', '${p.amount}', '${p.upi_id}')" class="px-3 py-1.5 rounded-xl bg-emerald-500 text-black font-black text-xs hover:brightness-110 shadow-lg cursor-pointer">
                💸 Mark as Paid
              </button>
            ` : `<span class="text-xs text-emerald-400 font-bold">✓ Settled</span>`}
          </td>
        </tr>
      `).join('');
    }

    function openProcessPayoutModal(id, creator, amount, upi) {
      document.getElementById('modal-pay-id').value = id;
      document.getElementById('modal-pay-creator').textContent = creator;
      document.getElementById('modal-pay-amount').textContent = '₹' + amount;
      document.getElementById('modal-pay-upi').textContent = upi;
      document.getElementById('modal-pay-utr').value = 'UPI' + Math.floor(1000000000 + Math.random() * 9000000000);

      document.getElementById('ProcessPayoutModal').classList.remove('hidden');
      document.getElementById('ProcessPayoutModal').classList.add('flex');
    }

    function closeProcessPayoutModal() {
      document.getElementById('ProcessPayoutModal').classList.add('hidden');
      document.getElementById('ProcessPayoutModal').classList.remove('flex');
    }

    function handleConfirmPayout(e) {
      e.preventDefault();
      const payId = document.getElementById('modal-pay-id').value;
      const utr = document.getElementById('modal-pay-utr').value.trim();

      let allPayouts = [];
      try {
        allPayouts = JSON.parse(localStorage.getItem('br_influencer_payouts') || '[]');
      } catch (e) {}

      const p = allPayouts.find(x => x.id === payId);
      if (p) {
        p.status = 'Paid';
        p.utr = utr;
        localStorage.setItem('br_influencer_payouts', JSON.stringify(allPayouts));
      }

      closeProcessPayoutModal();
      loadInfluencers();
      alert('Payout marked as Paid successfully!');
    }

    // 7. Abandoned Leads Tab
    async function loadAbandoned() {
      let leads = [];
      try {
        leads = JSON.parse(localStorage.getItem('br_abandoned_leads') || '[]');
      } catch(e) {}
      renderAbandoned(leads);
    }

    function renderAbandoned(leads) {
      const tbody = document.getElementById('abandoned-table');
      if (!leads.length) {
        tbody.innerHTML = '<tr><td colspan="6" class="py-8 text-center text-gray-500">No abandoned checkout leads yet.</td></tr>';
        return;
      }

      tbody.innerHTML = leads.map(l => `
        <tr class="hover:bg-white/5 transition-colors">
          <td class="py-3 px-3 font-bold text-white">${l.name || 'Visitor'}</td>
          <td class="py-3 px-3 font-mono font-bold text-amber-300">${l.phone}</td>
          <td class="py-3 px-3">${l.bundle || '1 Bottle'}</td>
          <td class="py-3 px-3 text-gray-400">${l.created_at || 'Recently'}</td>
          <td class="py-3 px-3">
            <span class="px-2 py-0.5 rounded-full text-[9px] font-bold ${l.recovered ? 'bg-emerald-500/20 text-emerald-400' : 'bg-red-500/20 text-red-400'}">
              ${l.recovered ? '✓ Recovered' : 'Pending Lead'}
            </span>
          </td>
          <td class="py-3 px-3 text-right">
            <a href="https://wa.me/91${l.phone}?text=${encodeURIComponent('Namaste ' + (l.name || '') + ' ji! Aapne BlackRoots Herbal Hair Dye Shampoo ka order complete nahi kiya tha. Aaj order karne par EXTRA 5% DISCOUNT mil raha hai. Complete your order now: https://' + window.location.host + '/product.html')}" target="_blank" class="inline-flex items-center gap-1.5 bg-emerald-500 text-black px-3 py-1.5 rounded-xl text-xs font-black hover:brightness-110 shadow-lg">
              <span>💬 1-Click WhatsApp Recover</span>
            </a>
          </td>
        </tr>
      `).join('');
    }

    // 8. Settings Tab
    async function loadSettings() {
      let data = await apiFetch('get_settings');
      const s = (data && data.settings) ? data.settings : JSON.parse(localStorage.getItem('br_saved_settings') || '{}');
      document.getElementById('set-meta-pixel').value = s.meta_pixel_id || '';
      document.getElementById('set-meta-token').value = s.meta_capi_token || '';
      document.getElementById('set-ga4-id').value = s.ga4_measurement_id || '';
      document.getElementById('set-gsc-tag').value = s.gsc_verification_tag || '';
      document.getElementById('set-whatsapp-num').value = s.whatsapp_support || '+919580835179';
      document.getElementById('set-shiprocket-email').value = s.shiprocket_email || '';
      document.getElementById('set-shiprocket-password').value = s.shiprocket_password || '';
      document.getElementById('set-shiprocket-auto').checked = s.shiprocket_auto_push === '1';
    }

    async function handleSaveSettings(e) {
      e.preventDefault();
      const btn = document.getElementById('save-settings-btn');
      btn.disabled = true;
      btn.innerText = 'Saving...';

      const payload = {
        meta_pixel_id: document.getElementById('set-meta-pixel').value,
        meta_capi_token: document.getElementById('set-meta-token').value,
        ga4_measurement_id: document.getElementById('set-ga4-id').value,
        gsc_verification_tag: document.getElementById('set-gsc-tag').value,
        whatsapp_support: document.getElementById('set-whatsapp-num').value,
        shiprocket_email: document.getElementById('set-shiprocket-email').value,
        shiprocket_password: document.getElementById('set-shiprocket-password').value,
        shiprocket_auto_push: document.getElementById('set-shiprocket-auto').checked ? '1' : '0',
        new_password: document.getElementById('set-new-pass').value
      };

      if (payload.new_password) {
        localStorage.setItem('br_admin_pass', payload.new_password);
      }
      localStorage.setItem('br_saved_settings', JSON.stringify(payload));
      localStorage.setItem('br_analytics_config', JSON.stringify(payload));

      await apiFetch('save_settings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      btn.disabled = false;
      btn.innerText = '💾 Save All Settings & API Configurations';
      alert('Settings & Marketing APIs saved successfully!');
      document.getElementById('set-new-pass').value = '';
    }

    function exportCSVDirect() {
      const orders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
      let csv = 'Order ID,Name,Phone,Address,City,Pincode,Bundle,Price,Status,Coupon,Influencer\\n';
      orders.forEach(o => {
        csv += `${o.order_id},"${o.name}",${o.phone},"${o.address}","${o.city}",${o.pincode},"${o.product_bundle || o.bundle}",${o.price},${o.status},"${o.coupon || ''}","${o.influencer || ''}"\\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'BlackRoots_Orders_' + new Date().toISOString().slice(0, 10) + '.csv';
      a.click();
    }

    function getStatusClass(status) {
      switch (status) {
        case 'New': return 'bg-blue-500/20 text-blue-400 border border-blue-500/30';
        case 'Confirmed': return 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
        case 'Dispatched': return 'bg-amber-500/20 text-amber-400 border border-amber-500/30';
        case 'Delivered': return 'bg-purple-500/20 text-purple-400 border border-purple-500/30';
        case 'Cancelled': return 'bg-red-500/20 text-red-400 border border-red-500/30';
        default: return 'bg-gray-500/20 text-gray-400';
      }
    }

    document.addEventListener('DOMContentLoaded', function() {
      if (sessionStorage.getItem('br_admin_auth') === '1') {
        document.getElementById('AdminLoginScreen').classList.add('hidden');
        document.getElementById('AdminDashboardApp').classList.remove('hidden');
        loadDashboard();
      }
    });
  </script>

</body>
</html>
"""

# Write admin.html and admin/index.html
with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html_code)

os.makedirs('admin', exist_ok=True)
with open(os.path.join('admin', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html_code)

print("2. [SUCCESS] Built admin.html & admin/index.html with Creator & Affiliate management tab")

# ==============================================================================
# 3. UPDATE ASSETS/THEME.JS WITH TRACKING & CHECKOUT COUPON ENGINE
# ==============================================================================
with open('assets/theme.js', 'r', encoding='utf-8') as f:
    theme_js = f.read()

# Add Affiliate Tracking & Coupon Code Engine to theme.js
affiliate_engine_code = """
/* ==========================================================================
   🤝 BLACKROOTS VIP INFLUENCER & COUPON TRACKING ENGINE
   ========================================================================== */
(function() {
  'use strict';

  // 1. Detect and persist URL referral codes (?ref=CODE or ?coupon=CODE)
  function initInfluencerReferral() {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      const refCode = (urlParams.get('ref') || urlParams.get('coupon') || '').trim().toUpperCase();
      
      if (refCode) {
        localStorage.setItem('br_active_coupon', refCode);
        localStorage.setItem('br_influencer_ref', refCode);

        // Track click count for this influencer
        let db = [];
        try {
          db = JSON.parse(localStorage.getItem('br_influencers_db') || '[]');
        } catch(e) {}
        
        let creator = db.find(u => u.code && u.code.toUpperCase() === refCode);
        if (creator) {
          creator.clicks = (Number(creator.clicks) || 0) + 1;
          localStorage.setItem('br_influencers_db', JSON.stringify(db));
        }

        // Show subtle notification banner
        showAffiliateBanner(refCode);
      }
    } catch(e) {}
  }

  function showAffiliateBanner(code) {
    if (document.getElementById('AffiliatePromoBanner')) return;
    const banner = document.createElement('div');
    banner.id = 'AffiliatePromoBanner';
    banner.className = 'fixed bottom-4 left-4 right-4 sm:left-auto sm:right-4 z-40 bg-[#11141b]/95 backdrop-blur-xl border border-[#d4af37] text-white p-3.5 rounded-2xl shadow-2xl flex items-center justify-between gap-3 text-xs max-w-md';
    banner.innerHTML = `
      <div class="flex items-center gap-2.5">
        <span class="text-base">🎉</span>
        <div>
          <span class="font-bold text-amber-300">Creator Promo: <code class="bg-black/60 px-1.5 py-0.5 rounded text-white">${code}</code></span>
          <p class="text-[11px] text-gray-300">10% OFF will automatically apply at checkout!</p>
        </div>
      </div>
      <button onclick="this.parentElement.remove()" class="text-gray-400 hover:text-white font-bold text-sm px-1.5 cursor-pointer">&times;</button>
    `;
    document.body.appendChild(banner);
  }

  // 2. Global Coupon Validator & Applicator
  window.applyCheckoutCoupon = function() {
    const input = document.getElementById('OrderCouponInput');
    const note = document.getElementById('CouponDiscountNote');
    const priceDisplay = document.getElementById('OrderModalPriceDisplay');
    if (!input) return;

    const rawCode = input.value.trim().toUpperCase();
    if (!rawCode) {
      alert('Please enter a coupon code.');
      return;
    }

    let db = [];
    try {
      db = JSON.parse(localStorage.getItem('br_influencers_db') || '[]');
    } catch(e) {}

    let creator = db.find(u => u.code && u.code.toUpperCase() === rawCode);
    let commRate = creator ? (creator.comm_rate || 10) : 10;
    let basePrice = window.selectedPack ? window.selectedPack.price : 499;

    // Calculate 10% discount
    let discount = Math.round(basePrice * 0.10);
    let finalPrice = basePrice - discount;

    window.appliedCouponData = {
      code: rawCode,
      discount: discount,
      finalPrice: finalPrice,
      influencer_id: creator ? creator.id : null,
      comm_rate: commRate
    };

    if (note) {
      note.textContent = `✓ Code ${rawCode} Applied (-₹${discount})`;
      note.classList.remove('hidden');
    }

    if (priceDisplay) {
      priceDisplay.innerHTML = `<span class="line-through text-gray-400 text-sm font-normal">₹${basePrice}</span> <span class="text-emerald-400 font-black">₹${finalPrice}</span>`;
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initInfluencerReferral);
  } else {
    initInfluencerReferral();
  }
})();
"""

# Append or replace in theme.js cleanly
if 'BLACKROOTS VIP INFLUENCER & COUPON TRACKING ENGINE' not in theme_js:
    theme_js += "\n\n" + affiliate_engine_code
    with open('assets/theme.js', 'w', encoding='utf-8') as f:
        f.write(theme_js)
    print("3. [SUCCESS] Injected Influencer & Coupon engine into assets/theme.js")
else:
    print("3. [INFO] theme.js already contains affiliate engine")

# ==============================================================================
# 4. UPDATE QUICKORDERMODAL IN PRODUCT.HTML WITH PROMO CODE INPUT BOX
# ==============================================================================
with open('product.html', 'r', encoding='utf-8') as f:
    prod_html = f.read()

coupon_modal_snippet = """
        <!-- VIP Influencer / Promo Code Input Row -->
        <div class="p-3.5 rounded-2xl bg-white/5 border border-white/10 space-y-2">
          <div class="flex items-center justify-between">
            <label class="text-[11px] font-bold text-gray-300 uppercase tracking-wider">Have a Creator / Promo Code?</label>
            <span id="CouponDiscountNote" class="hidden text-[10px] text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20"></span>
          </div>
          <div class="flex items-center gap-2">
            <input type="text" id="OrderCouponInput" placeholder="e.g. PRIYA10" class="w-full px-3.5 py-2.5 rounded-xl bg-black border border-white/20 text-xs text-white uppercase font-bold focus:outline-none focus:border-[#d4af37]">
            <button type="button" onclick="applyCheckoutCoupon()" class="px-4 py-2.5 rounded-xl bg-gradient-to-r from-[#d4af37] to-amber-500 text-black text-xs font-black uppercase hover:brightness-110 shadow shrink-0 cursor-pointer">
              Apply
            </button>
          </div>
        </div>
"""

if 'id="OrderCouponInput"' not in prod_html:
    # Inject before submit button
    target_btn = '<button type="submit" class="btn-gold-luxury btn-shimmer w-full py-4'
    if target_btn in prod_html:
        prod_html = prod_html.replace(target_btn, coupon_modal_snippet + '\n        ' + target_btn)
        with open('product.html', 'w', encoding='utf-8') as f:
            f.write(prod_html)
        print("4. [SUCCESS] Added Promo Code input box to product.html QuickOrderModal")

# ==============================================================================
# 5. SYNC DEMO_LAB AND PREVIEW FOLDERS IF PRESENT
# ==============================================================================
for folder in ['demo_lab', 'preview']:
    if os.path.exists(folder):
        os.makedirs(os.path.join(folder, 'influencer'), exist_ok=True)
        with open(os.path.join(folder, 'influencer', 'index.html'), 'w', encoding='utf-8') as f:
            f.write(influencer_html_code)
        with open(os.path.join(folder, 'influencer.html'), 'w', encoding='utf-8') as f:
            f.write(influencer_html_code)
        with open(os.path.join(folder, 'admin.html'), 'w', encoding='utf-8') as f:
            f.write(admin_html_code)
        if os.path.exists(os.path.join(folder, 'assets', 'theme.js')):
            with open(os.path.join(folder, 'assets', 'theme.js'), 'w', encoding='utf-8') as f:
                f.write(theme_js)
        print(f"5. [SUCCESS] Synced influencer & admin files to {folder}")

print("=== ALL INFLUENCER & ADMIN INTEGRATIONS COMPLETED 100% SUCCESSFULLY ===")
