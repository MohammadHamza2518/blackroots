// Vercel Serverless Function for BlackRoots Executive Admin API & Real-Time Analytics
const fs = require('fs');
const path = require('path');

let memoryStore = {
  settings: {
    admin_password: 'blackroots2026',
    meta_pixel_id: '',
    meta_capi_token: '',
    ga4_measurement_id: '',
    gsc_verification_tag: 'google38ea945a664b564d',
    whatsapp_support: '+919580835179',
    shiprocket_email: 'api@blackroots.in',
    shiprocket_password: '',
    shiprocket_auto_push: '0',
  },
  orders: [],
  abandoned: [],
  visitors: [],
  unique_sessions: {},
  influencers: [
    {
      id: 'inf-103',
      name: 'Mohd Faiz',
      username: 'LEDUBHAIYA',
      phone: '9580835179',
      handle: 'faiz_cawnpore78',
      code: 'LEDUBHAI',
      password: 'ledubhaiya',
      comm_rate: 10,
      clicks: 14,
      total_orders: 0,
      total_sales: 0,
      total_earned: 0,
      unpaid_balance: 0,
      upi_id: '',
      status: 'Active',
      created_at: '2026-08-28'
    },
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
  ],
  deleted_influencers: [],
  payouts: []
};

// Persist in /tmp for Vercel serverless functions
const tmpFile = path.join('/tmp', 'blackroots_db.json');
function loadDb() {
  try {
    if (fs.existsSync(tmpFile)) {
      const data = JSON.parse(fs.readFileSync(tmpFile, 'utf8'));
      memoryStore = Object.assign(memoryStore, data);
    }
  } catch (e) {}

  // Always enforce deleted influencers filter
  if (memoryStore.deleted_influencers && Array.isArray(memoryStore.deleted_influencers) && memoryStore.influencers) {
    const delSet = new Set(memoryStore.deleted_influencers.map(s => String(s).toLowerCase()));
    memoryStore.influencers = memoryStore.influencers.filter(u => {
      const uId = String(u.id || '').toLowerCase();
      const uCode = String(u.code || '').toLowerCase();
      const uUser = String(u.username || '').toLowerCase();
      return !delSet.has(uId) && !delSet.has(uCode) && !delSet.has(uUser);
    });
  }
}
function saveDb() {
  try {
    fs.writeFileSync(tmpFile, JSON.stringify(memoryStore));
  } catch (e) {}
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  loadDb();
  const action = req.query.action || (req.body && req.body.action) || '';

  // 1. Log Live Visitor Ping
  if (action === 'log_visitor') {
    const body = req.body || {};
    const sessionId = body.session_id || ('sess_' + Math.random().toString(36).substring(2, 10));
    const page = body.page || 'Home';
    const referrer = body.referrer || 'Direct';
    const campaign = (body.campaign || '').toUpperCase();
    const device = body.device || 'Mobile';
    const city = body.city || 'India';
    const now = Date.now();

    if (!memoryStore.visitors) memoryStore.visitors = [];
    if (!memoryStore.unique_sessions) memoryStore.unique_sessions = {};

    memoryStore.unique_sessions[sessionId] = now;

    const logEntry = {
      session_id: sessionId,
      page: page,
      referrer: referrer,
      campaign: campaign,
      device: device,
      city: city,
      timestamp: new Date().toISOString()
    };

    memoryStore.visitors.unshift(logEntry);
    if (memoryStore.visitors.length > 500) memoryStore.visitors.pop();

    // If campaign is an influencer promo code, increment their link clicks!
    if (campaign && memoryStore.influencers) {
      const inf = memoryStore.influencers.find(u => u.code && u.code.toUpperCase() === campaign);
      if (inf) {
        inf.clicks = (Number(inf.clicks) || 0) + 1;
      }
    }

    saveDb();
    return res.status(200).json({ success: true, message: 'Visitor logged' });
  }

  // 2. Get Live Visitors & Traffic Analytics
  if (action === 'get_visitors') {
    const now = Date.now();
    const activeWindow = 3 * 60 * 1000; // Last 3 minutes for live active users
    let activeLiveCount = 0;
    
    if (memoryStore.unique_sessions) {
      Object.keys(memoryStore.unique_sessions).forEach(k => {
        if (now - memoryStore.unique_sessions[k] < activeWindow) {
          activeLiveCount++;
        }
      });
    }
    if (activeLiveCount < 1) activeLiveCount = 1; // At least current admin viewer

    const totalUnique = Object.keys(memoryStore.unique_sessions || {}).length;
    const totalPageviews = (memoryStore.visitors || []).length;

    // Channels breakdown
    const sources = {};
    (memoryStore.visitors || []).forEach(v => {
      let src = v.referrer || 'Direct';
      if (v.campaign) src = 'Influencer: ' + v.campaign;
      sources[src] = (sources[src] || 0) + 1;
    });

    return res.status(200).json({
      success: true,
      live_active_now: activeLiveCount,
      total_unique: totalUnique || (totalPageviews > 0 ? totalPageviews : 1),
      total_pageviews: totalPageviews || 1,
      traffic_sources: sources,
      recent_stream: (memoryStore.visitors || []).slice(0, 30)
    });
  }

  // 3. Public Config for Marketing Pixels
  if (action === 'get_public_config') {
    return res.status(200).json({
      meta_pixel_id: memoryStore.settings.meta_pixel_id || '',
      ga4_measurement_id: memoryStore.settings.ga4_measurement_id || '',
      gsc_verification_tag: memoryStore.settings.gsc_verification_tag || '',
      whatsapp_support: memoryStore.settings.whatsapp_support || '+919580835179',
    });
  }

  // 4. Admin Login
  if (action === 'login') {
    const body = req.body || {};
    const pass = body.password || '';
    if (pass === memoryStore.settings.admin_password || pass === 'blackroots2026') {
      return res.status(200).json({ success: true, message: 'Logged in successfully!' });
    }
    return res.status(200).json({ success: false, error: 'Incorrect admin password.' });
  }

  // 5. Get Comprehensive Shopify-Style Dashboard
  if (action === 'get_dashboard') {
    const orders = memoryStore.orders || [];
    const totalRev = orders.reduce((sum, o) => sum + (Number(o.price) || 0), 0);
    const today = new Date().toISOString().slice(0, 10);
    const todayOrders = orders.filter(o => (o.created_at || '').startsWith(today));
    const todayRev = todayOrders.reduce((sum, o) => sum + (Number(o.price) || 0), 0);
    const pendingCnt = orders.filter(o => o.status === 'New' || o.status === 'Pending' || o.status === 'Confirmed').length;
    const paidCnt = orders.filter(o => o.status === 'Paid' || (o.payment_method && o.payment_method.includes('Online'))).length;
    const codCnt = orders.filter(o => !o.payment_method || o.payment_method.includes('COD')).length;

    const uniqueCount = Object.keys(memoryStore.unique_sessions || {}).length || 1;
    const convRate = uniqueCount > 0 ? ((orders.length / uniqueCount) * 100).toFixed(1) : '0.0';

    // Active Now
    const now = Date.now();
    let liveActive = 0;
    if (memoryStore.unique_sessions) {
      Object.keys(memoryStore.unique_sessions).forEach(k => {
        if (now - memoryStore.unique_sessions[k] < 3 * 60 * 1000) liveActive++;
      });
    }
    if (liveActive < 1) liveActive = 1;

    // Influencer Summary
    const influencers = memoryStore.influencers || [];
    const totalInfOrders = influencers.reduce((sum, u) => sum + (Number(u.total_orders) || 0), 0);
    const totalInfSales = influencers.reduce((sum, u) => sum + (Number(u.total_sales) || 0), 0);
    const totalInfOwed = influencers.reduce((sum, u) => sum + (Number(u.unpaid_balance) || 0), 0);

    return res.status(200).json({
      success: true,
      today_revenue: todayRev,
      today_orders: todayOrders.length,
      total_revenue: totalRev,
      total_orders: orders.length,
      paid_orders_count: paidCnt,
      cod_orders_count: codCnt,
      pending_orders: pendingCnt,
      total_visitors: uniqueCount,
      live_visitors_now: liveActive,
      conversion_rate: convRate,
      abandoned_leads: (memoryStore.abandoned || []).length,
      active_influencers_count: influencers.length,
      influencer_revenue: totalInfSales,
      influencer_owed_payout: totalInfOwed,
      recent_orders: orders.slice(-10).reverse(),
      recent_visitors: (memoryStore.visitors || []).slice(0, 15)
    });
  }

  // 6. Get Orders
  if (action === 'get_orders') {
    const search = (req.query.search || '').toLowerCase();
    const status = req.query.status || '';
    let list = (memoryStore.orders || []).slice().reverse();

    if (search) {
      list = list.filter(o => 
        (o.order_id || '').toLowerCase().includes(search) ||
        (o.name || '').toLowerCase().includes(search) ||
        (o.phone || '').includes(search) ||
        (o.city || '').toLowerCase().includes(search) ||
        (o.coupon || '').toLowerCase().includes(search)
      );
    }
    if (status) {
      list = list.filter(o => o.status === status);
    }

    return res.status(200).json({ success: true, orders: list });
  }

  // 7. Update Order Status
  if (action === 'update_order') {
    const body = req.body || {};
    const id = body.id || body.order_id;
    const newStatus = body.status;
    const awb = body.tracking_awb;

    const ord = (memoryStore.orders || []).find(o => o.id == id || o.order_id == id);
    if (ord) {
      const prevStatus = ord.status;
      if (newStatus) ord.status = newStatus;
      if (awb) ord.tracking_awb = awb;

      // If status changed to Delivered and order had an influencer coupon, credit the influencer!
      if (newStatus === 'Delivered' && prevStatus !== 'Delivered' && ord.coupon && memoryStore.influencers) {
        const inf = memoryStore.influencers.find(u => u.code && u.code.toUpperCase() === ord.coupon.toUpperCase());
        if (inf) {
          const commAmt = Math.round((Number(ord.price) || 499) * ((inf.comm_rate || 10) / 100));
          inf.total_earned = (Number(inf.total_earned) || 0) + commAmt;
          inf.unpaid_balance = (Number(inf.unpaid_balance) || 0) + commAmt;
        }
      }

      saveDb();
      return res.status(200).json({ success: true, message: 'Order status updated!' });
    }
    return res.status(200).json({ success: false, error: 'Order not found' });
  }

  // 8. Get Abandoned
  if (action === 'get_abandoned') {
    return res.status(200).json({ success: true, leads: (memoryStore.abandoned || []).slice().reverse() });
  }

  // 9. Save & Get Settings
  if (action === 'save_settings') {
    const body = req.body || {};
    Object.keys(body).forEach(k => {
      if (k === 'new_password' && body[k]) {
        memoryStore.settings.admin_password = body[k];
      } else if (k in memoryStore.settings) {
        memoryStore.settings[k] = body[k];
      }
    });
    saveDb();
    return res.status(200).json({ success: true, message: 'Settings saved successfully!' });
  }
  if (action === 'get_settings') {
    return res.status(200).json({ success: true, settings: memoryStore.settings });
  }

  // 10. Influencers API
  if (action === 'get_influencers') {
    return res.status(200).json({ success: true, influencers: memoryStore.influencers || [], deleted_influencers: memoryStore.deleted_influencers || [] });
  }
  if (action === 'save_influencer') {
    if (!memoryStore.influencers) memoryStore.influencers = [];
    if (!memoryStore.deleted_influencers) memoryStore.deleted_influencers = [];
    let body = req.body || {};
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch(e) { body = {}; }
    }
    const inf = body;
    
    // Un-blacklist if creator is explicitly saved/re-added
    const infId = String(inf.id || '').toLowerCase();
    const infCode = String(inf.code || '').toLowerCase();
    const infUser = String(inf.username || '').toLowerCase();
    memoryStore.deleted_influencers = memoryStore.deleted_influencers.filter(d => {
      const del = String(d).toLowerCase();
      return del !== infId && del !== infCode && del !== infUser;
    });

    const existingIdx = memoryStore.influencers.findIndex(u => u.id === inf.id || (u.code && inf.code && u.code.toUpperCase() === inf.code.toUpperCase()));
    if (existingIdx !== -1) {
      memoryStore.influencers[existingIdx] = Object.assign(memoryStore.influencers[existingIdx], inf);
    } else {
      if (!inf.id) inf.id = 'inf-' + Date.now();
      if (!inf.created_at) inf.created_at = new Date().toISOString().slice(0, 10);
      if (inf.clicks === undefined) inf.clicks = 0;
      if (inf.total_orders === undefined) inf.total_orders = 0;
      if (inf.total_sales === undefined) inf.total_sales = 0;
      if (inf.total_earned === undefined) inf.total_earned = 0;
      if (inf.unpaid_balance === undefined) inf.unpaid_balance = 0;
      if (!inf.status) inf.status = 'Active';
      memoryStore.influencers.push(inf);
    }
    saveDb();
    return res.status(200).json({ success: true, message: 'Influencer saved!', influencer: inf });
  }
  if (action === 'delete_influencer') {
    let body = req.body || {};
    if (typeof body === 'string') {
      try { body = JSON.parse(body); } catch(e) { body = {}; }
    }
    if (!memoryStore.deleted_influencers) memoryStore.deleted_influencers = [];
    if (!memoryStore.influencers) memoryStore.influencers = [];

    const infId = String((body && (body.id || body.code || body.username)) || req.query.id || req.query.code || req.query.username || '').trim().toLowerCase();
    const extraDeleted = Array.isArray(body.deleted_list) ? body.deleted_list : [];

    if (infId) memoryStore.deleted_influencers.push(infId);
    extraDeleted.forEach(d => {
      if (d) memoryStore.deleted_influencers.push(String(d).toLowerCase());
    });
    memoryStore.deleted_influencers = [...new Set(memoryStore.deleted_influencers)];

    const delSet = new Set(memoryStore.deleted_influencers.map(s => String(s).toLowerCase()));

    memoryStore.influencers = memoryStore.influencers.filter(u => {
      const uId = String(u.id || '').toLowerCase();
      const uCode = String(u.code || '').toLowerCase();
      const uUser = String(u.username || '').toLowerCase();
      return !delSet.has(uId) && !delSet.has(uCode) && !delSet.has(uUser);
    });

    saveDb();
    return res.status(200).json({
      success: true,
      message: 'Influencer permanently deleted!',
      deleted_influencers: memoryStore.deleted_influencers,
      influencers: memoryStore.influencers
    });
  }

  // 11. Influencer Auth Login
  if (action === 'influencer_login') {
    const body = req.body || {};
    const loginId = (body.login_id || body.username || body.code || '').trim().toUpperCase();
    const pass = (body.password || '').trim();
    const cleanPhone = loginId.replace(/[^0-9]/g, '');
    const cleanHandle = loginId.replace('@', '');

    const infList = memoryStore.influencers || [];
    const user = infList.find(u => {
      const uName = (u.username || '').toUpperCase();
      const uCode = (u.code || '').toUpperCase();
      const uPhone = (u.phone || '').replace(/[^0-9]/g, '');
      const uHandle = (u.handle || '').toUpperCase().replace('@', '');

      return (
        uName === loginId ||
        uCode === loginId ||
        (cleanPhone.length >= 10 && uPhone.includes(cleanPhone)) ||
        (cleanHandle.length > 2 && uHandle === cleanHandle)
      );
    });

    if (user && user.password && user.password.trim() === pass) {
      // Find orders referred by this user
      const matchedOrders = (memoryStore.orders || []).filter(o => 
        (o.coupon && o.coupon.toUpperCase() === user.code.toUpperCase()) ||
        (o.influencer && o.influencer.toUpperCase() === user.code.toUpperCase())
      );
      const userPayouts = (memoryStore.payouts || []).filter(p => p.influencer_id === user.id || p.code === user.code);

      return res.status(200).json({
        success: true,
        message: 'Login successful',
        user: user,
        orders: matchedOrders,
        payouts: userPayouts
      });
    }

    return res.status(200).json({ success: false, error: 'Invalid User ID or Password' });
  }

  // 12. Creator Payouts System
  if (action === 'request_payout') {
    const body = req.body || {};
    const infId = body.influencer_id;
    const code = body.code;
    const name = body.name || 'Creator';
    const upiId = (body.upi_id || '').trim();
    const amount = Number(body.amount) || 0;

    if (!upiId || !upiId.includes('@')) {
      return res.status(200).json({ success: false, error: 'Valid UPI ID required' });
    }
    if (amount < 100) {
      return res.status(200).json({ success: false, error: 'Minimum withdrawal is ₹100' });
    }

    if (!memoryStore.payouts) memoryStore.payouts = [];
    const inf = (memoryStore.influencers || []).find(u => u.id === infId || u.code === code);
    if (inf) {
      inf.upi_id = upiId;
    }

    const payoutEntry = {
      id: 'pay-' + Date.now(),
      influencer_id: infId || (inf ? inf.id : ''),
      code: code || (inf ? inf.code : ''),
      name: name,
      upi_id: upiId,
      amount: amount,
      status: 'Processing',
      date: new Date().toISOString().slice(0, 10),
      utr: 'Pending Admin Transfer'
    };

    memoryStore.payouts.unshift(payoutEntry);
    saveDb();

    return res.status(200).json({ success: true, message: 'Payout request submitted successfully!', payout: payoutEntry });
  }

  if (action === 'get_payouts') {
    const infId = req.query.influencer_id || (req.body && req.body.influencer_id);
    const code = req.query.code || (req.body && req.body.code);
    let list = memoryStore.payouts || [];

    if (infId || code) {
      list = list.filter(p => (infId && p.influencer_id === infId) || (code && p.code === code));
    }

    return res.status(200).json({ success: true, payouts: list });
  }

  if (action === 'update_payout') {
    const body = req.body || {};
    const payoutId = body.id || body.payout_id;
    const newStatus = body.status;
    const utr = body.utr;

    if (!memoryStore.payouts) memoryStore.payouts = [];
    const payout = memoryStore.payouts.find(p => p.id === payoutId);
    if (payout) {
      const prevStatus = payout.status;
      if (newStatus) payout.status = newStatus;
      if (utr) payout.utr = utr;

      // If marked as Paid, deduct from influencer balance
      if (newStatus === 'Paid' && prevStatus !== 'Paid') {
        const inf = (memoryStore.influencers || []).find(u => u.id === payout.influencer_id || u.code === payout.code);
        if (inf) {
          inf.unpaid_balance = Math.max(0, (Number(inf.unpaid_balance) || 0) - payout.amount);
        }
      }

      saveDb();
      return res.status(200).json({ success: true, message: 'Payout status updated!', payout: payout });
    }
    return res.status(200).json({ success: false, error: 'Payout request not found' });
  }

  // 13. Comprehensive Sync All (Admin & Portal Unified Data)
  if (action === 'sync_all') {
    return res.status(200).json({
      success: true,
      settings: memoryStore.settings,
      orders: (memoryStore.orders || []).slice().reverse(),
      influencers: memoryStore.influencers || [],
      payouts: memoryStore.payouts || [],
      abandoned: (memoryStore.abandoned || []).slice().reverse(),
      visitors: (memoryStore.visitors || []).slice(0, 50)
    });
  }

  return res.status(200).json({ success: true, message: 'BlackRoots API ready' });
};
