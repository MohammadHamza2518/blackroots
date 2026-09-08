// Vercel Serverless Function for Abandoned Cart Lead Capture with MongoDB Atlas
const { getCollections } = require('./lib/db');

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(200).json({ success: true });

  try {
    const input = req.body || {};
    const phone = (input.phone || '').trim().replace(/[^0-9]/g, '');

    if (phone.length >= 10) {
      const { abandoned } = await getCollections();
      const cleanPhone = phone.slice(-10);

      const updateData = {
        name: input.name || 'Visitor',
        phone: cleanPhone,
        product_bundle: input.bundle || '1 Bottle (250ml)',
        price: Number(input.price) || 499,
        recovered: 0,
        updated_at: new Date().toISOString().replace('T', ' ').slice(0, 19)
      };

      await abandoned.updateOne(
        { phone: cleanPhone },
        { 
          $set: updateData,
          $setOnInsert: { created_at: new Date().toISOString().replace('T', ' ').slice(0, 19) }
        },
        { upsert: true }
      );
    }
  } catch (e) {
    console.error('Abandoned cart lead error:', e);
  }

  return res.status(200).json({ success: true });
};
