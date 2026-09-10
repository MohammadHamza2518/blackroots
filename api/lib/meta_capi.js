// Meta Conversions API (CAPI) Engine for BlackRoots Vercel Serverless Architecture
const crypto = require('crypto');
const https = require('https');

function hashSha256(str) {
  if (!str) return null;
  return crypto.createHash('sha256').update(String(str).trim().toLowerCase()).digest('hex');
}

async function triggerMetaCapiPurchase(order, settings, req) {
  try {
    const pixelId = settings.meta_pixel_id;
    const accessToken = settings.meta_capi_token;

    if (!pixelId || !accessToken) {
      return { success: false, message: 'Meta Pixel ID or Access Token not configured' };
    }

    const headers = (req && req.headers) || {};
    const clientIp = String(headers['x-forwarded-for'] || (req && req.socket && req.socket.remoteAddress) || '127.0.0.1').split(',')[0].trim();
    const userAgent = headers['user-agent'] || 'Mozilla/5.0';

    let phone = String(order.phone || '').replace(/[^0-9]/g, '');
    if (phone.length === 10) {
      phone = '91' + phone;
    }

    const userData = {
      ph: phone ? [hashSha256(phone)] : undefined,
      em: order.email ? [hashSha256(order.email)] : undefined,
      fn: order.name ? [hashSha256(order.name.split(' ')[0])] : undefined,
      ct: order.city ? [hashSha256(order.city)] : undefined,
      zp: order.pincode ? [hashSha256(order.pincode)] : undefined,
      country: [hashSha256('in')],
      client_ip_address: clientIp,
      client_user_agent: userAgent
    };

    if (order.fbclid) {
      userData.fbc = 'fb.1.' + Date.now() + '.' + order.fbclid;
    }

    // Clean undefined fields
    Object.keys(userData).forEach(k => {
      if (userData[k] === undefined) delete userData[k];
    });

    const eventId = order.event_id || ('order_' + String(order.order_id || '').replace(/[^a-zA-Z0-9]/g, ''));

    const eventPayload = {
      event_name: 'Purchase',
      event_time: Math.floor(Date.now() / 1000),
      event_id: eventId,
      event_source_url: headers.referer || 'https://blackroots.in/checkout.html',
      action_source: 'website',
      user_data: userData,
      custom_data: {
        currency: 'INR',
        value: Number(order.price) || 499,
        order_id: order.order_id,
        content_name: 'BlackRoots Herbal Hair Darkening Shampoo',
        content_type: 'product'
      }
    };

    const requestBody = {
      data: [eventPayload]
    };

    if (settings.meta_test_code) {
      requestBody.test_event_code = settings.meta_test_code;
    }

    const bodyString = JSON.stringify(requestBody);

    return new Promise((resolve) => {
      const options = {
        hostname: 'graph.facebook.com',
        port: 443,
        path: `/v19.0/${pixelId}/events?access_token=${encodeURIComponent(accessToken)}`,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(bodyString)
        },
        timeout: 5000
      };

      const request = https.request(options, (response) => {
        let data = '';
        response.on('data', (chunk) => { data += chunk; });
        response.on('end', () => {
          const success = response.statusCode >= 200 && response.statusCode < 300;
          console.log('[Meta CAPI Result]', response.statusCode, data);
          resolve({ success, response: data, statusCode: response.statusCode });
        });
      });

      request.on('error', (err) => {
        console.error('[Meta CAPI Request Error]', err.message);
        resolve({ success: false, error: err.message });
      });

      request.on('timeout', () => {
        request.destroy();
        resolve({ success: false, error: 'Request timeout' });
      });

      request.write(bodyString);
      request.end();
    });
  } catch (err) {
    console.error('[Meta CAPI Fatal Error]', err.message);
    return { success: false, error: err.message };
  }
}

module.exports = {
  triggerMetaCapiPurchase,
  hashSha256
};
