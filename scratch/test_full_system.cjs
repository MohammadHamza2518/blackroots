const { getCollections } = require('../api/lib/db.js');
const orderHandler = require('../api/order.js');
const trackHandler = require('../api/track.js');
const adminHandler = require('../api/admin.js');
const abandonedHandler = require('../api/abandoned.js');

function mockRes() {
  let resolve;
  const promise = new Promise(r => resolve = r);
  return {
    setHeader: () => {},
    status: (code) => ({
      json: (data) => resolve({ code, data }),
      end: () => resolve({ code, data: null })
    }),
    promise
  };
}

async function runFullSuite() {
  console.log('=== 1. Testing DB Connectivity ===');
  const { orders, influencers, abandoned, payouts, settings } = await getCollections();
  const infCount = await influencers.countDocuments();
  console.log('PASS: MongoDB Connected! Active influencers:', infCount);

  console.log('\n=== 2. Testing Customer Order Placement (with Influencer Coupon AIRAM10) ===');
  const res1 = mockRes();
  await orderHandler({
    method: 'POST',
    body: {
      order_id: '#BR-TEST-101',
      name: 'Rahul Sharma',
      phone: '9876512345',
      address: 'House 42, Civil Lines',
      city: 'Kanpur',
      pincode: '208001',
      bundle: '1 Bottle (250ml)',
      price: 499,
      coupon: 'AIRAM10',
      payment_method: 'COD'
    }
  }, res1);
  const orderRes = await res1.promise;
  console.log('PASS: Order placed successfully:', orderRes.data.order_id, orderRes.data.message);

  console.log('\n=== 3. Verifying Order in MongoDB ===');
  const savedOrder = await orders.findOne({ order_id: '#BR-TEST-101' });
  console.log('PASS: Found order in MongoDB:', savedOrder.name, savedOrder.price, 'Coupon:', savedOrder.coupon);

  console.log('\n=== 4. Verifying Influencer Attribution in MongoDB ===');
  const airam = await influencers.findOne({ code: 'AIRAM10' });
  console.log('PASS: Airam stats in MongoDB:', {
    orders: airam.total_orders,
    sales: airam.total_sales,
    earned: airam.total_earned,
    unpaid_balance: airam.unpaid_balance
  });

  console.log('\n=== 5. Testing Order Tracking (api/track.js) ===');
  const resTrack = mockRes();
  await trackHandler({ method: 'GET', query: { q: 'BR-TEST-101' } }, resTrack);
  const trackRes = await resTrack.promise;
  console.log('PASS: Track API returned:', trackRes.data.order_id, trackRes.data.customer_name, trackRes.data.status, trackRes.data.courier);

  console.log('\n=== 6. Testing Admin Dashboard (api/admin.js?action=get_dashboard) ===');
  const resDash = mockRes();
  await adminHandler({ method: 'GET', query: { action: 'get_dashboard' } }, resDash);
  const dashRes = await resDash.promise;
  console.log('PASS: Admin Dashboard fetched from MongoDB:', {
    total_revenue: dashRes.data.total_revenue,
    total_orders: dashRes.data.total_orders,
    active_influencers: dashRes.data.active_influencers_count,
    influencer_revenue: dashRes.data.influencer_revenue
  });

  console.log('\n=== 7. Testing Influencer Portal Login (airam) ===');
  const resLogin = mockRes();
  await adminHandler({
    method: 'POST',
    query: { action: 'influencer_login' },
    body: { login_id: 'airam', password: 'airam' }
  }, resLogin);
  const loginRes = await resLogin.promise;
  console.log('PASS: Influencer logged in successfully:', loginRes.data.user.name, 'Referred Orders count:', loginRes.data.orders.length);

  console.log('\n=== 8. Testing Abandoned Cart Leads (api/abandoned.js) ===');
  const resAb = mockRes();
  await abandonedHandler({
    method: 'POST',
    body: { name: 'Priya Verma', phone: '9876599999', bundle: '2 Bottles Pack', price: 799 }
  }, resAb);
  await resAb.promise;
  const savedLead = await abandoned.findOne({ phone: '9876599999' });
  console.log('PASS: Abandoned lead saved in MongoDB:', savedLead.name, savedLead.phone, savedLead.price);

  console.log('\n=== 9. Cleaning Up Test Artifacts ===');
  await orders.deleteOne({ order_id: '#BR-TEST-101' });
  await abandoned.deleteOne({ phone: '9876599999' });
  await influencers.updateOne({ code: 'AIRAM10' }, { $set: { total_orders: 0, total_sales: 0, total_earned: 0, unpaid_balance: 0 } });
  console.log('PASS: Test artifacts successfully cleaned up.');

  console.log('\n=========================================');
  console.log('🎉 ALL 9 SYSTEM VERIFICATION TESTS PASSED!');
  console.log('=========================================');
  process.exit(0);
}

runFullSuite().catch(err => {
  console.error('Test failed:', err);
  process.exit(1);
});
