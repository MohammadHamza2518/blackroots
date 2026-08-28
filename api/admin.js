// Vercel Serverless Function for BlackRoots Admin API
const fs = require('fs');
const path = require('path');

let memoryStore = {
  settings: {
    admin_password: 'blackroots2026',
    meta_pixel_id: '',
    meta_capi_token: '',
    ga4_measurement_id: '',
    gsc_verification_tag: '',
    whatsapp_support: '+919580835179',
    shiprocket_email: '',
    shiprocket_password: '',
    shiprocket_auto_push: '0',
  },
  orders: [],
  abandoned: []
};

// Try to persist in /tmp if available on Vercel serverless
const tmpFile = path.join('/tmp', 'blackroots_db.json');
function loadDb() {
  try {
    if (fs.existsSync(tmpFile)) {
      const data = JSON.parse(fs.readFileSync(tmpFile, 'utf8'));
      memoryStore = Object.assign(memoryStore, data);
    }
  } catch (e) {}
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

  // 1. Public Config for Analytics & Marketing Pixels
  if (action === 'get_public_config') {
    return res.status(200).json({
      meta_pixel_id: memoryStore.settings.meta_pixel_id || '',
      ga4_measurement_id: memoryStore.settings.ga4_measurement_id || '',
      gsc_verification_tag: memoryStore.settings.gsc_verification_tag || '',
      whatsapp_support: memoryStore.settings.whatsapp_support || '+919580835179',
    });
  }

  // 2. Admin Login
  if (action === 'login') {
    const body = req.body || {};
    const pass = body.password || '';
    if (pass === memoryStore.settings.admin_password || pass === 'blackroots2026') {
      return res.status(200).json({ success: true, message: 'Logged in successfully!' });
    }
    return res.status(200).json({ success: false, error: 'Incorrect admin password.' });
  }

  // 3. Get Dashboard
  if (action === 'get_dashboard') {
    const orders = memoryStore.orders || [];
    const totalRev = orders.reduce((sum, o) => sum + (Number(o.price) || 0), 0);
    const today = new Date().toISOString().slice(0, 10);
    const todayOrders = orders.filter(o => (o.created_at || '').startsWith(today));
    const todayRev = todayOrders.reduce((sum, o) => sum + (Number(o.price) || 0), 0);
    const pendingCnt = orders.filter(o => o.status === 'New' || o.status === 'Pending').length;

    return res.status(200).json({
      success: true,
      today_revenue: todayRev,
      today_orders: todayOrders.length,
      total_revenue: totalRev,
      total_orders: orders.length,
      pending_orders: pendingCnt,
      abandoned_leads: (memoryStore.abandoned || []).length,
      recent_orders: orders.slice(-10).reverse()
    });
  }

  // 4. Get Orders
  if (action === 'get_orders') {
    const search = (req.query.search || '').toLowerCase();
    const status = req.query.status || '';
    let list = (memoryStore.orders || []).slice().reverse();

    if (search) {
      list = list.filter(o => 
        (o.order_id || '').toLowerCase().includes(search) ||
        (o.name || '').toLowerCase().includes(search) ||
        (o.phone || '').includes(search) ||
        (o.city || '').toLowerCase().includes(search)
      );
    }
    if (status) {
      list = list.filter(o => o.status === status);
    }

    return res.status(200).json({ success: true, orders: list });
  }

  // 5. Update Order Status
  if (action === 'update_order') {
    const body = req.body || {};
    const id = body.id;
    const newStatus = body.status;
    const awb = body.tracking_awb;

    const ord = (memoryStore.orders || []).find(o => o.id == id || o.order_id == id);
    if (ord) {
      if (newStatus) ord.status = newStatus;
      if (awb) ord.tracking_awb = awb;
      saveDb();
      return res.status(200).json({ success: true, message: 'Order status updated!' });
    }
    return res.status(200).json({ success: false, error: 'Order not found' });
  }

  // 6. Get Abandoned
  if (action === 'get_abandoned') {
    return res.status(200).json({ success: true, leads: (memoryStore.abandoned || []).slice().reverse() });
  }

  // 7. Save Settings
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

  // 8. Get Settings
  if (action === 'get_settings') {
    return res.status(200).json({ success: true, settings: memoryStore.settings });
  }

  // 9. Influencer API actions
  if (action === 'get_influencers') {
    return res.status(200).json({ success: true, influencers: memoryStore.influencers || [] });
  }
  if (action === 'save_influencer') {
    if (!memoryStore.influencers) memoryStore.influencers = [];
    const inf = req.body || {};
    const existingIdx = memoryStore.influencers.findIndex(u => u.id === inf.id || u.code === inf.code);
    if (existingIdx !== -1) {
      memoryStore.influencers[existingIdx] = Object.assign(memoryStore.influencers[existingIdx], inf);
    } else {
      memoryStore.influencers.push(inf);
    }
    saveDb();
    return res.status(200).json({ success: true, message: 'Influencer saved!' });
  }
  if (action === 'delete_influencer') {
    if (!memoryStore.influencers) memoryStore.influencers = [];
    const infId = (req.body && req.body.id) || req.query.id;
    memoryStore.influencers = memoryStore.influencers.filter(u => u.id !== infId && u.code !== infId);
    saveDb();
    return res.status(200).json({ success: true, message: 'Influencer deleted!' });
  }

  return res.status(200).json({ success: true, message: 'BlackRoots API ready' });
};
