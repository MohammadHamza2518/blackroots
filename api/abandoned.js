// Vercel Serverless Function for Abandoned Cart Lead Capture
const fs = require('fs');
const path = require('path');

const tmpFile = path.join(require('os').tmpdir(), 'blackroots_db.json');
function getDb() {
  let db = { abandoned: [] };
  try {
    if (fs.existsSync(tmpFile)) db = JSON.parse(fs.readFileSync(tmpFile, 'utf8'));
  } catch (e) {}
  return db;
}
function saveDb(db) {
  try { fs.writeFileSync(tmpFile, JSON.stringify(db)); } catch (e) {}
}

module.exports = async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  if (req.method !== 'POST') return res.status(200).json({ success: true });

  const input = req.body || {};
  const phone = (input.phone || '').trim().replace(/[^0-9]/g, '');
  if (phone.length >= 10) {
    const db = getDb();
    if (!db.abandoned) db.abandoned = [];

    const existing = db.abandoned.find(a => a.phone === phone);
    if (existing) {
      existing.name = input.name || existing.name;
      existing.price = input.price || existing.price;
      existing.created_at = new Date().toISOString().replace('T', ' ').slice(0, 19);
    } else {
      db.abandoned.push({
        id: db.abandoned.length + 1,
        name: input.name || 'Visitor',
        phone: phone,
        product_bundle: input.bundle || '1 Bottle',
        price: input.price || 499,
        recovered: 0,
        created_at: new Date().toISOString().replace('T', ' ').slice(0, 19)
      });
    }
    saveDb(db);
  }
  return res.status(200).json({ success: true });
};
