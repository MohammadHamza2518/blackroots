// Centralized MongoDB Atlas Connection for BlackRoots Vercel Serverless Architecture
const { MongoClient } = require('mongodb');

const MONGODB_URI = process.env.MONGODB_URI || 'mongodb+srv://kitchenheritage3_db_user:ECpJjtyKwkMR2lZB@cluster0.1fjikit.mongodb.net/blackroots?retryWrites=true&w=majority&appName=Cluster0';

let cachedClient = null;
let cachedDb = null;
let isInitialized = false;

const DEFAULT_INITIAL_INFLUENCERS = [
  {
    id: 'inf-104',
    name: 'Airam',
    username: 'airam',
    phone: '9876543210',
    handle: '@airam_beauty',
    code: 'AIRAM10',
    password: 'airam',
    comm_rate: 10,
    clicks: 0,
    total_orders: 0,
    total_sales: 0,
    total_earned: 0,
    unpaid_balance: 0,
    upi_id: '',
    status: 'Active',
    created_at: '2026-09-01'
  },
  {
    id: 'inf-105',
    name: 'Ilma',
    username: 'ilma',
    phone: '9876543211',
    handle: '@ilma_care',
    code: 'ILMA10',
    password: 'ilma',
    comm_rate: 10,
    clicks: 0,
    total_orders: 0,
    total_sales: 0,
    total_earned: 0,
    unpaid_balance: 0,
    upi_id: '',
    status: 'Active',
    created_at: '2026-09-01'
  }
];

async function connectToDatabase() {
  if (cachedClient && cachedDb) {
    return { client: cachedClient, db: cachedDb };
  }

  const client = new MongoClient(MONGODB_URI, {
    maxPoolSize: 10,
    minPoolSize: 1,
    serverSelectionTimeoutMS: 5000,
    socketTimeoutMS: 15000,
  });

  await client.connect();
  const db = client.db('blackroots');

  cachedClient = client;
  cachedDb = db;

  if (!isInitialized) {
    try {
      const infCol = db.collection('influencers');
      const infCount = await infCol.countDocuments();
      if (infCount === 0) {
        await infCol.insertMany(DEFAULT_INITIAL_INFLUENCERS);
        console.log('[MongoDB] Seeded default influencers');
      }

      const ordersCol = db.collection('orders');
      await ordersCol.createIndex({ order_id: 1 }).catch(() => {});
      await ordersCol.createIndex({ phone: 1 }).catch(() => {});
      await ordersCol.createIndex({ tracking_awb: 1 }).catch(() => {});
      await ordersCol.createIndex({ created_at: -1 }).catch(() => {});

      await infCol.createIndex({ code: 1 }).catch(() => {});
      await infCol.createIndex({ username: 1 }).catch(() => {});

      isInitialized = true;
    } catch (e) {
      console.warn('[MongoDB] Init warning:', e.message);
    }
  }

  return { client, db };
}

async function getCollections() {
  const { client, db } = await connectToDatabase();
  return {
    client,
    db,
    orders: db.collection('orders'),
    influencers: db.collection('influencers'),
    abandoned: db.collection('abandoned'),
    settings: db.collection('settings'),
    payouts: db.collection('payouts'),
    visitors: db.collection('visitors'),
    sessions: db.collection('sessions')
  };
}

module.exports = {
  connectToDatabase,
  getCollections,
  DEFAULT_INITIAL_INFLUENCERS
};
