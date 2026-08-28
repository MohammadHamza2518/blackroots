// Vercel Serverless Function for Order Placement
const fs = require('fs');
const path = require('path');

const defaultInfluencers = [
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
];

const tmpFile = path.join('/tmp', 'blackroots_db.json');
function getDb() {
  let db = { orders: [], abandoned: [], settings: {}, influencers: defaultInfluencers, visitors: [], unique_sessions: {} };
  try {
    if (fs.existsSync(tmpFile)) {
      const parsed = JSON.parse(fs.readFileSync(tmpFile, 'utf8'));
      db = Object.assign(db, parsed);
    }
  } catch (e) {}
  return db;
}
function saveDb(db) {
  try {
    fs.writeFileSync(tmpFile, JSON.stringify(db));
  } catch (e) {}
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method Not Allowed' });
  }

  const input = req.body || {};
  const name = (input.name || '').trim();
  const phone = (input.phone || '').trim().replace(/[^0-9]/g, '');
  const cleanPhone = (phone.length > 10 && phone.startsWith('91')) ? phone.slice(2) : phone;
  const pincode = (input.pincode || '').trim().replace(/[^0-9]/g, '');
  const address = (input.address || '').trim();
  const city = (input.city || '').trim();
  const bundle = input.bundle || '1 Bottle (250ml)';
  const price = Number(input.price) || 499;

  if (cleanPhone.length !== 10) {
    return res.status(200).json({ success: false, error: 'Please enter a valid 10-digit Indian mobile number.' });
  }
  if (pincode.length !== 6) {
    return res.status(200).json({ success: false, error: 'Please enter a valid 6-digit delivery pincode.' });
  }
  if (!name || !address) {
    return res.status(200).json({ success: false, error: 'Full Name and Address are required.' });
  }

  const db = getDb();
  if (!db.orders) db.orders = [];

  const orderNum = 1025 + db.orders.length;
  const orderId = '#BR-' + orderNum;
  const awb = '8839' + Math.floor(100000 + Math.random() * 900000);

  const newOrder = {
    id: db.orders.length + 1,
    order_id: orderId,
    name: name,
    phone: cleanPhone,
    email: input.email || '',
    address: address,
    city: city || 'India',
    state: input.state || 'Uttar Pradesh',
    pincode: pincode,
    product_bundle: bundle,
    price: price,
    payment_method: input.payment_method || 'COD',
    payment_id: input.payment_id || '',
    coupon: input.coupon || input.coupon_code || '',
    discount: input.discount || 0,
    influencer: input.influencer || '',
    status: (input.payment_method && (input.payment_method.toLowerCase().includes('online') || input.payment_method.toLowerCase().includes('razorpay') || input.payment_method.toLowerCase().includes('paid'))) ? 'Paid' : 'New',
    tracking_awb: awb,
    courier: 'Delhivery Express Air',
    created_at: new Date().toISOString().replace('T', ' ').slice(0, 19)
  };

  db.orders.push(newOrder);

  // If coupon was used, attribute to creator on server
  if (newOrder.coupon && db.influencers) {
    const inf = db.influencers.find(u => u.code && u.code.toUpperCase() === newOrder.coupon.toUpperCase());
    if (inf) {
      inf.total_orders = (Number(inf.total_orders) || 0) + 1;
      inf.total_sales = (Number(inf.total_sales) || 0) + price;
      if (newOrder.status === 'Paid') {
        const commAmt = Math.round(price * ((inf.comm_rate || 10) / 100));
        inf.total_earned = (Number(inf.total_earned) || 0) + commAmt;
        inf.unpaid_balance = (Number(inf.unpaid_balance) || 0) + commAmt;
      }
    }
  }

  saveDb(db);

  return res.status(200).json({
    success: true,
    order_id: orderId,
    awb: awb,
    courier: 'Delhivery Express Air',
    message: 'Order placed successfully! Dispatched from Shuklaganj UP central warehouse.',
    estimated_delivery: 'Within 48-72 Hours',
    customer: { name: name, phone: cleanPhone, city: city }
  });
};
