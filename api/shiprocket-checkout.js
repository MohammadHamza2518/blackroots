const crypto = require('crypto');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-Api-Key, X-Api-HMAC-SHA256');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const API_KEY = 'hl7tTx1OioeJn0KS';
  const API_SECRET = 'SX9xl506RtMcE6761XJgkzhJOl1QCUW6';

  try {
    const { qty = 1, price = 499, title = 'BlackRoots Herbal Hair Darkening Shampoo (250ml)', coupon = '' } = req.body || {};

    const basePrice = Number(price) || (qty === 2 ? 799 : 499);
    const variantId = qty === 2 ? "1002" : "1001";
    const imgUrl = qty === 2 
      ? "https://blackroots.in/assets/blackroots-bottle-duo.png" 
      : "https://blackroots.in/assets/blackroots-bottle-single.png";

    const payload = {
      cart_data: {
        items: [
          {
            variant_id: variantId,
            quantity: Number(qty) || 1,
            catalog_data: {
              price: Number(basePrice),
              name: title,
              image_url: imgUrl
            }
          }
        ],
        mobile_app: false
      },
      redirect_url: "https://blackroots.in/track-order.html",
      timestamp: new Date().toISOString()
    };

    if (coupon && typeof coupon === 'string' && coupon.trim()) {
      payload.cart_data.cart_discount = {
        coupon_code: coupon.trim().toUpperCase(),
        amount: 50.0
      };
    }

    const payloadString = JSON.stringify(payload);
    const hmac = crypto.createHmac('sha256', API_SECRET).update(payloadString).digest('base64');

    const srResponse = await fetch('https://checkout-api.shiprocket.com/api/v1/access-token/checkout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Api-Key': API_KEY,
        'X-Api-HMAC-SHA256': hmac
      },
      body: payloadString
    });

    const data = await srResponse.json().catch(() => null);

    if (srResponse.ok && data && data.ok && data.result && data.result.token) {
      return res.status(200).json({
        success: true,
        token: data.result.token,
        order_id: data.result.data ? data.result.data.order_id : null
      });
    } else {
      return res.status(200).json({
        success: false,
        error: (data && data.error) ? data.error.message : 'Unable to generate Fastrr token',
        raw: data
      });
    }
  } catch (err) {
    return res.status(500).json({
      success: false,
      error: err.message
    });
  }
};
