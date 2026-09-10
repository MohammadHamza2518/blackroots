// Vercel Serverless Function for Order Placement with MongoDB Atlas
const { getCollections } = require('./lib/db');
const { triggerMetaCapiPurchase } = require('./lib/meta_capi');

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

  try {
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

    const { orders, influencers, settings } = await getCollections();
    const totalOrders = await orders.countDocuments();

    const orderId = input.order_id || ('#BR-' + (1025 + totalOrders));
    const awb = input.tracking_awb || ('8839' + Math.floor(100000 + Math.random() * 900000));
    const eventId = input.event_id || ('order_' + String(orderId).replace(/[^a-zA-Z0-9]/g, ''));

    const newOrder = {
      order_id: orderId,
      event_id: eventId,
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
      fbclid: input.fbclid || '',
      utm_source: input.utm_source || '',
      utm_medium: input.utm_medium || '',
      utm_campaign: input.utm_campaign || '',
      utm_content: input.utm_content || '',
      utm_term: input.utm_term || '',
      status: (input.payment_method && (input.payment_method.toLowerCase().includes('online') || input.payment_method.toLowerCase().includes('razorpay') || input.payment_method.toLowerCase().includes('paid'))) ? 'Paid' : 'New',
      tracking_awb: awb,
      courier: 'Delhivery Express Air',
      created_at: new Date().toISOString().replace('T', ' ').slice(0, 19)
    };

    // Save or update order in MongoDB
    await orders.updateOne(
      { order_id: orderId },
      { $set: newOrder },
      { upsert: true }
    );

    // Trigger Meta Conversions API (CAPI) Server-Side Purchase Event
    try {
      const curSettings = (await settings.findOne({ id: 'main_settings' })) || {};
      triggerMetaCapiPurchase(newOrder, curSettings, req).catch(() => {});
    } catch(capiErr) {
      console.warn('[Meta CAPI Dispatch Warning]', capiErr.message);
    }

    // If coupon was used, atomically attribute to creator in MongoDB
    const couponUsed = String(newOrder.coupon || newOrder.influencer || '').trim().toUpperCase();
    if (couponUsed) {
      const inf = await influencers.findOne({
        $or: [
          { code: { $regex: new RegExp('^' + couponUsed + '$', 'i') } },
          { username: { $regex: new RegExp('^' + couponUsed + '$', 'i') } },
          { code: { $regex: new RegExp('^' + couponUsed + '10$', 'i') } },
          { id: { $regex: new RegExp('^' + couponUsed + '$', 'i') } }
        ]
      });

      if (inf) {
        const commRate = Number(inf.comm_rate) || 10;
        const commAmt = Math.round(price * (commRate / 100));
        // Attach comm amount to the order record for delivery verification
        await orders.updateOne({ order_id: orderId }, { $set: { comm: commAmt, influencer_id: inf.id || inf.code } });

        // Anti-Fraud Safeguard: Commission unlocks into withdrawable balance ONLY upon verified customer delivery.
        // On placement, record referral sales count and volume without unlocking premature payouts.
        await influencers.updateOne(
          { _id: inf._id },
          {
            $inc: {
              total_orders: 1,
              total_sales: price
            }
          }
        );
      }
    }

    return res.status(200).json({
      success: true,
      order_id: orderId,
      awb: awb,
      courier: 'Delhivery Express Air',
      message: 'Order placed successfully! Dispatched from Shuklaganj UP central warehouse.',
      estimated_delivery: 'Within 48-72 Hours',
      customer: { name: name, phone: cleanPhone, city: city }
    });

  } catch (err) {
    console.error('Order placement error:', err);
    return res.status(500).json({
      success: false,
      error: 'Order could not be saved: ' + err.message
    });
  }
};
