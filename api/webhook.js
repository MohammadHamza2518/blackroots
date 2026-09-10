// Shiprocket Fastrr Order Webhook & Real-Time Sync Endpoint with MongoDB Atlas
const { getCollections } = require('./lib/db');

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
    const { orders, influencers } = await getCollections();
    const totalCount = await orders.countDocuments();

    const orderId = payload.order_id || payload.order_number || payload.id || ('#BR-' + (1025 + totalCount));
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

    const orderRecord = {
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

    // Check if this is a Tracking Status Event (e.g. from Shiprocket Tracking Webhook)
    const rawStatus = (payload.current_status || payload.shipment_status || payload.order_status || '').toUpperCase();
    if (rawStatus) {
      const targetAwborId = payload.awb || payload.tracking_number || payload.order_id || payload.order_number;
      if (targetAwborId) {
        const ord = await orders.findOne({
          $or: [{ order_id: targetAwborId }, { tracking_awb: targetAwborId }]
        });
        if (ord) {
          const prevStatus = ord.status;
          let newStatus = ord.status;
          if (rawStatus.includes('DELIVERED') && !rawStatus.includes('RTO')) {
            newStatus = 'Delivered';
          } else if (rawStatus.includes('RTO') || rawStatus.includes('CANCEL') || rawStatus.includes('UNDELIVERED')) {
            newStatus = 'Cancelled';
          }

          if (newStatus !== prevStatus) {
            await orders.updateOne({ _id: ord._id }, { $set: { status: newStatus } });

            const couponTag = (ord.coupon || ord.influencer || '').trim().toUpperCase();
            if (couponTag) {
              const inf = await influencers.findOne({
                $or: [
                  { code: { $regex: new RegExp('^' + couponTag + '$', 'i') } },
                  { username: { $regex: new RegExp('^' + couponTag + '$', 'i') } },
                  { id: { $regex: new RegExp('^' + couponTag + '$', 'i') } }
                ]
              });
              if (inf) {
                const commAmt = ord.comm || Math.round((Number(ord.price) || 499) * ((Number(inf.comm_rate) || 10) / 100));
                if (newStatus === 'Delivered' && prevStatus !== 'Delivered') {
                  await influencers.updateOne(
                    { _id: inf._id },
                    { $inc: { total_earned: commAmt, unpaid_balance: commAmt } }
                  );
                } else if (prevStatus === 'Delivered' && newStatus === 'Cancelled') {
                  await influencers.updateOne(
                    { _id: inf._id },
                    { $inc: { total_earned: -commAmt, unpaid_balance: -commAmt } }
                  );
                  await influencers.updateOne(
                    { _id: inf._id, unpaid_balance: { $lt: 0 } },
                    { $set: { unpaid_balance: 0 } }
                  );
                }
              }
            }
          }

          return res.status(200).json({
            success: true,
            message: `Order status updated to ${newStatus} based on webhook`
          });
        }
      }
    }

    // Otherwise, treat as new Order placement webhook
    let calculatedComm = 0;
    if (coupon) {
      const inf = await influencers.findOne({
        $or: [
          { code: { $regex: new RegExp('^' + coupon + '$', 'i') } },
          { username: { $regex: new RegExp('^' + coupon + '$', 'i') } },
          { id: { $regex: new RegExp('^' + coupon + '$', 'i') } }
        ]
      });

      if (inf) {
        calculatedComm = Math.round(price * ((Number(inf.comm_rate) || 10) / 100));
        // Anti-Fraud Safeguard: Commission is locked until verified customer delivery.
        // Record referral counts only.
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

    orderRecord.comm = calculatedComm;

    await orders.updateOne(
      { order_id: orderId },
      { $set: orderRecord },
      { upsert: true }
    );

    return res.status(200).json({
      success: true,
      message: "Order successfully recorded and tracked in MongoDB",
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
