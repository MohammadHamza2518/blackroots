// Vercel Serverless Function & Node.js API: Send Real SMS OTP to Indian Mobile
const https = require('https');

const FAST2SMS_API_KEY = process.env.FAST2SMS_API_KEY || 'VTaUKw2Jbklt3D7miYnxIOXfsg4dv9eZuM0HSzpQ1GqCNAFPo6Rwn4McpoXZrLNOA3hUyqa7CVFPgk0H';

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, message: 'Method Not Allowed' });
  }

  try {
    const { phone, otp } = req.body || {};
    const cleanPhone = (phone || '').replace(/[^0-9]/g, '').slice(-10);

    if (cleanPhone.length !== 10 || !otp) {
      return res.status(400).json({ success: false, message: 'Valid 10-digit phone and OTP required' });
    }

    // Dispatch via Fast2SMS OTP & Quick Route
    const payload = JSON.stringify({
      route: 'otp',
      variables_values: otp,
      numbers: cleanPhone
    });

    const options = {
      hostname: 'www.fast2sms.com',
      path: '/dev/bulkV2',
      method: 'POST',
      headers: {
        'authorization': FAST2SMS_API_KEY,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload)
      }
    };

    const smsReq = https.request(options, (smsRes) => {
      let data = '';
      smsRes.on('data', chunk => data += chunk);
      smsRes.on('end', () => {
        return res.status(200).json({ success: true, provider: 'Fast2SMS', response: data, otp: otp });
      });
    });

    smsReq.on('error', (err) => {
      return res.status(200).json({ success: true, simulated: true, error: err.message, otp: otp });
    });

    smsReq.write(payload);
    smsReq.end();

  } catch (err) {
    return res.status(500).json({ success: false, error: err.message });
  }
};
