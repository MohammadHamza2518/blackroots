// Shiprocket Fastrr Order Webhook & Real-Time Sync Endpoint
const fs = require('fs');
const path = require('path');

const tmpFile = path.join(require('os').tmpdir(), 'blackroots_db.json');
function getDb() {
  let db = { orders: [], influencers: [], deleted_influencers: [], abandoned: [], settings: {} };
  try {
    if (fs.existsSync(tmpFile)) db = Object.assign(db, JSON.parse(fs.readFileSync(tmpFile, 'utf8')));
  } catch (e) {}
  return db;
}
function saveDb(db) {
  try { fs.writeFileSync(tmpFile, JSON.stringify(db)); } catch (e) {}
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Api-Key, X-Api-HMAC-SHA256');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const payload = req.body || {};
  console.log("Received Shiprocket Fastrr Order Webhook:", payload);

  try {
    const db = getDb();
    if (!db.orders) db.orders = [];

    const orderId = payload.order_id || payload.order_number || payload.id || ('#BR-' + (1025 + db.orders.length));
    const customerName = payload.customer_name || (payload.billing_address && ((payload.billing_address.first_name || '') + ' ' + (payload.billing_address.last_name || '')).trim()) || payload.name || 'Valued Customer';
    const phone = (payload.phone || (payload.billing_address && payload.billing_address.phone) || payload.customer_phone || '').replace(/[^0-9]/g, '');
    const cleanPhone = (phone.length > 10 && phone.startsWith('91')) ? phone.slice(2) : phone;
    const address = payload.address || (payload.shipping_address && payload.shipping_address.address1) || (payload.billing_address && payload.billing_address.address1) || 'India';
    const city = payload.city || (payload.shipping_address && payload.shipping_address.city) || (payload.billing_address && payload.billing_address.city) || 'India';
    const pincode = (payload.pincode || (payload.shipping_address && payload.shipping_address.pincode) || (payload.billing_address && payload.billing_address.pincode) || '').replace(/[^0-9]/g, '');
    const price = Number(payload.total_price || payload.price || payload.amount || payload.total) || 499;
    const coupon = (payload.coupon || payload.coupon_code || (payload.discount_codes && payload.discount_codes[0] && payload.discount_codes[0].code) || '').trim().toUpperCase();
    const isPaid = (payload.is_paid || payload.payment_status === 'PAID' || (payload.payment_method && payload.payment_method.toLowerCase().includes('prepaid')));
    const paymentMethod = payload.payment_method || (isPaid ? 'Online Paid (Shiprocket Fastrr)' : 'Cash on Delivery (COD)');
    const awb = payload.awb || payload.tracking_number || ('8839' + Math.floor(100000 + Math.random() * 900000));

    const existingIdx = db.orders.findIndex(o => o.order_id === orderId);
    const orderRecord = {
      id: db.orders.length + 1,
      order_id: orderId,
      name: customerName,
      phone: cleanPhone,
      address: address,
      city: city,
      pincode: pincode,
      product_bundle: payload.bundle || (price >= 700 ? '2 Bottles Pack (500ml)' : '1 Bottle (250ml)'),
      price: price,
      payment_method: paymentMethod,
      coupon: coupon,
      status: isPaid ? 'Paid' : 'New',
      tracking_awb: awb,
      courier: 'Delhivery Express Air',
      created_at: new Date().toISOString().replace('T', ' ').slice(0, 19)
    };

    if (existingIdx !== -1) {
      db.orders[existingIdx] = Object.assign(db.orders[existingIdx], orderRecord);
    } else {
      db.orders.push(orderRecord);
    }

    // Attribute to influencer if coupon applied
    if (coupon && db.influencers) {
      const inf = db.influencers.find(u => 
        (u.code && u.code.toUpperCase() === coupon) ||
        (u.username && u.username.toUpperCase() === coupon) ||
        (u.id && u.id.toUpperCase() === coupon)
      );
      if (inf) {
        inf.total_orders = (Number(inf.total_orders) || 0) + 1;
        inf.total_sales = (Number(inf.total_sales) || 0) + price;
        if (isPaid) {
          const commAmt = Math.round(price * ((inf.comm_rate || 10) / 100));
          inf.total_earned = (Number(inf.total_earned) || 0) + commAmt;
          inf.unpaid_balance = (Number(inf.unpaid_balance) || 0) + commAmt;
        }
      }
    }

    saveDb(db);

    return res.status(200).json({
      success: true,
      message: "Order successfully recorded and tracked",
      order_id: orderId,
      awb: awb
    });
  } catch(e) {
    return res.status(200).json({
      success: true,
      message: "Webhook acknowledged",
      error: e.message
    });
  }
};
