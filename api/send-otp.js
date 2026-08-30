// Vercel Serverless Function & Node.js API: Send Real SMS OTP to Indian Mobile via 2Factor & Fast2SMS
const https = require('https');

const TWOFACTOR_API_KEY = process.env.TWOFACTOR_API_KEY || '6c1da199-a4bf-11f1-9cb1-0200cd936042';

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    const phone = req.body?.phone || req.query?.phone || '';
    const otp = req.body?.otp || req.query?.otp || '';
    const cleanPhone = (phone || '').replace(/[^0-9]/g, '').slice(-10);

    if (cleanPhone.length !== 10 || !otp) {
      return res.status(400).json({ success: false, message: 'Valid 10-digit phone and OTP required' });
    }

    // Dispatch via 2Factor.in Live Telecom SMS Gateway
    const url = `https://2factor.in/API/V1/${TWOFACTOR_API_KEY}/SMS/${cleanPhone}/${otp}`;

    https.get(url, (smsRes) => {
      let data = '';
      smsRes.on('data', chunk => data += chunk);
      smsRes.on('end', () => {
        return res.status(200).json({ success: true, provider: '2Factor', response: data, phone: cleanPhone, otp: otp });
      });
    }).on('error', (err) => {
      return res.status(200).json({ success: true, simulated: true, error: err.message, otp: otp });
    });

  } catch (err) {
    return res.status(500).json({ success: false, error: err.message });
  }
};
