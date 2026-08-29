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
    const { items, customer, payment_method, coupon } = req.body || {};
    const selectedItem = (items && items[0]) || {
      name: 'BlackRoots Herbal Hair Darkening Shampoo (250ml)',
      price: 499,
      quantity: 1,
      sku: 'BR-250ML'
    };

    const payload = {
      cart: {
        items: [
          {
            name: selectedItem.name,
            sku: selectedItem.sku || 'BR-250ML',
            unit_price: Number(selectedItem.price) || 499,
            quantity: Number(selectedItem.quantity) || 1
          }
        ]
      },
      redirect_url: 'https://blackroots.in/track-order.html',
      cancel_url: 'https://blackroots.in/product.html'
    };

    const payloadString = JSON.stringify(payload);
    const hmac = crypto.createHmac('sha256', API_SECRET).update(payloadString).digest('base64');

    // Call Shiprocket Checkout API
    const response = await fetch('https://checkout-api.shiprocket.com/v1/checkout/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Api-Key': API_KEY,
        'X-Api-HMAC-SHA256': hmac
      },
      body: payloadString
    });

    const data = await response.json().catch(() => null);

    if (response.ok && data && (data.checkout_url || data.url || data.token)) {
      return res.status(200).json({
        success: true,
        checkout_url: data.checkout_url || data.url,
        token: data.token
      });
    } else {
      // Fallback
      return res.status(200).json({
        success: false,
        fallback: true,
        message: (data && data.message) || 'Fastrr checkout processing',
        raw: data
      });
    }
  } catch (err) {
    return res.status(200).json({
      success: false,
      fallback: true,
      error: err.message
    });
  }
};
