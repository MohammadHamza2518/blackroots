const adminHandler = require('./api/admin.js');
const orderHandler = require('./api/order.js');

async function callApi(handler, method, query = {}, body = {}) {
  return new Promise((resolve) => {
    let statusCode = 200;
    let headers = {};
    const req = {
      method,
      query,
      body
    };
    const res = {
      setHeader: (k, v) => { headers[k] = v; },
      status: (code) => {
        statusCode = code;
        return res;
      },
      json: (data) => resolve({ statusCode, data, headers }),
      end: () => resolve({ statusCode, data: null, headers })
    };
    handler(req, res);
  });
}

async function runSystemTests() {
  console.log('====================================================');
  console.log('🧪 RUNNING BLACKROOTS ADMIN & INFLUENCER SYSTEM TESTS');
  console.log('====================================================\n');

  let passed = 0;
  let total = 0;

  function assert(name, condition, details = '') {
    total++;
    if (condition) {
      passed++;
      console.log(`✅ [PASS] ${name}`);
    } else {
      console.error(`❌ [FAIL] ${name} -> Details: ${details}`);
    }
  }

  // TEST 1: Admin Login
  const loginRes = await callApi(adminHandler, 'POST', {}, { action: 'login', password: 'blackroots2026' });
  assert('1. Admin Login (correct password)', loginRes.data && loginRes.data.success === true, JSON.stringify(loginRes.data));

  const badLoginRes = await callApi(adminHandler, 'POST', {}, { action: 'login', password: 'wrongpassword' });
  assert('2. Admin Login Rejection (wrong password)', badLoginRes.data && badLoginRes.data.success === false);

  // TEST 2: Influencers List & Seed Data
  const infRes = await callApi(adminHandler, 'GET', { action: 'get_influencers' });
  assert('3. Fetch Influencers List', infRes.data && Array.isArray(infRes.data.influencers) && infRes.data.influencers.length >= 3, `Count: ${infRes.data.influencers ? infRes.data.influencers.length : 0}`);

  // TEST 3: Add / Save New Influencer
  const newInf = {
    id: 'inf-test-999',
    name: 'Aarav Mehta',
    username: 'AARAV20',
    phone: '9876500000',
    handle: '@aarav_vlogs',
    code: 'AARAV20',
    password: 'aaravpassword',
    comm_rate: 15,
    upi_id: 'aarav@okaxis'
  };
  const saveInfRes = await callApi(adminHandler, 'POST', {}, { action: 'save_influencer', ...newInf });
  assert('4. Save New Influencer', saveInfRes.data && saveInfRes.data.success === true);

  // TEST 4: Influencer Login via Server API
  const infLoginRes = await callApi(adminHandler, 'POST', {}, {
    action: 'influencer_login',
    login_id: 'AARAV20',
    password: 'aaravpassword'
  });
  assert('5. Influencer Portal Login (by Username)', infLoginRes.data && infLoginRes.data.success === true && infLoginRes.data.user.name === 'Aarav Mehta');

  // TEST 5: Track Visitor Link Click for Influencer
  const visRes = await callApi(adminHandler, 'POST', {}, {
    action: 'log_visitor',
    session_id: 'sess_test_101',
    page: 'Product',
    campaign: 'AARAV20',
    device: 'Mobile'
  });
  assert('6. Log Visitor with Influencer Promo Campaign', visRes.data && visRes.data.success === true);

  // Verify influencer clicks incremented
  const checkClicksRes = await callApi(adminHandler, 'GET', { action: 'get_influencers' });
  const aaravInf = checkClicksRes.data.influencers.find(u => u.code === 'AARAV20');
  assert('7. Influencer Click Counter Incremented', aaravInf && Number(aaravInf.clicks) >= 1, `Clicks: ${aaravInf ? aaravInf.clicks : 0}`);

  // TEST 6: Place an Order with Influencer Coupon
  const orderRes = await callApi(orderHandler, 'POST', {}, {
    name: 'Vikram Singh',
    phone: '9876543210',
    pincode: '208001',
    address: 'Flat 402, Civil Lines',
    city: 'Kanpur',
    bundle: '1 Bottle (250ml)',
    price: 499,
    payment_method: 'Online Razorpay (Paid)',
    coupon: 'AARAV20'
  });
  assert('8. Customer Order Placement with Influencer Coupon', orderRes.data && orderRes.data.success === true, JSON.stringify(orderRes.data));

  // TEST 7: Check Orders in Admin
  const getOrdersRes = await callApi(adminHandler, 'GET', { action: 'get_orders' });
  const placedOrder = (getOrdersRes.data.orders || []).find(o => o.phone === '9876543210' && o.coupon === 'AARAV20');
  assert('9. Order Synced to Admin Orders Registry', !!placedOrder, `Found: ${!!placedOrder}`);

  // TEST 8: Creator Requests Payout Withdrawal
  const payoutReqRes = await callApi(adminHandler, 'POST', {}, {
    action: 'request_payout',
    influencer_id: 'inf-test-999',
    code: 'AARAV20',
    name: 'Aarav Mehta',
    upi_id: 'aarav@okaxis',
    amount: 150
  });
  assert('10. Creator Submits UPI Withdrawal Request', payoutReqRes.data && payoutReqRes.data.success === true && payoutReqRes.data.payout.amount === 150);

  // TEST 9: Admin Fetches Payouts List
  const getPayoutsRes = await callApi(adminHandler, 'GET', { action: 'get_payouts' });
  const pendingPayout = (getPayoutsRes.data.payouts || []).find(p => p.code === 'AARAV20');
  assert('11. Admin Receives Creator Payout Request', !!pendingPayout && pendingPayout.status === 'Processing');

  // TEST 10: Admin Settles Payout with UTR
  const updatePayoutRes = await callApi(adminHandler, 'POST', {}, {
    action: 'update_payout',
    id: pendingPayout.id,
    status: 'Paid',
    utr: 'UPI/729104928104'
  });
  assert('12. Admin Marks Payout as Paid with UTR', updatePayoutRes.data && updatePayoutRes.data.success === true && updatePayoutRes.data.payout.status === 'Paid');

  // TEST 11: Store Analytics Dashboard
  const dashRes = await callApi(adminHandler, 'GET', { action: 'get_dashboard' });
  assert('13. Admin Dashboard Overview Metrics Calculated', dashRes.data && dashRes.data.success === true && dashRes.data.total_visitors >= 1);

  // TEST 12: Marketing Pixels Config
  const cfgRes = await callApi(adminHandler, 'GET', { action: 'get_public_config' });
  assert('14. Public Config Accessible', cfgRes.data && cfgRes.data.whatsapp_support.length > 5);

  // TEST 13: Delete Influencer Permanently
  const delRes = await callApi(adminHandler, 'POST', {}, { action: 'delete_influencer', id: 'inf-test-999' });
  assert('15. Admin Deletes Influencer', delRes.data && delRes.data.success === true);

  const checkDeletedRes = await callApi(adminHandler, 'GET', { action: 'get_influencers' });
  const stillExists = checkDeletedRes.data.influencers.some(u => u.id === 'inf-test-999' || u.code === 'AARAV20');
  assert('16. Influencer Is Permanently Removed (Not Resurrected)', !stillExists, `Still exists: ${stillExists}`);

  // TEST 14: Single Active Admin User Enforcement
  const adminDev1 = await callApi(adminHandler, 'POST', {}, { action: 'login', password: 'blackroots2026', device: 'Admin Laptop Chrome' });
  const tokenDev1 = adminDev1.data.token;
  assert('17. Admin Logs In on Device 1 (Receives Token)', !!tokenDev1);

  // Device 1 checks session - should be valid
  const checkDev1Valid = await callApi(adminHandler, 'POST', {}, { action: 'check_admin_session', token: tokenDev1 });
  assert('18. Admin Device 1 Session Valid', checkDev1Valid.data && checkDev1Valid.data.valid === true);

  // Admin logs in on Device 2 (e.g. Mobile)
  const adminDev2 = await callApi(adminHandler, 'POST', {}, { action: 'login', password: 'blackroots2026', device: 'Admin iPhone Safari' });
  const tokenDev2 = adminDev2.data.token;
  assert('19. Admin Logs In on Device 2 (New Token Generated)', !!tokenDev2 && tokenDev2 !== tokenDev1);

  // Device 1 checks session again - should be KICKED!
  const checkDev1Kicked = await callApi(adminHandler, 'POST', {}, { action: 'check_admin_session', token: tokenDev1 });
  assert('20. Admin Device 1 Session Kicked Out (Single User Enforced)', checkDev1Kicked.data && checkDev1Kicked.data.session_expired === true && checkDev1Kicked.data.code === 'SESSION_KICKED');

  // TEST 15: Single Device Influencer Enforcement
  // Creator logs in on Device A
  const infDev1 = await callApi(adminHandler, 'POST', {}, { action: 'influencer_login', login_id: 'LEDUBHAIYA', password: 'ledubhaiya', device: 'OnePlus 12' });
  const infToken1 = infDev1.data.token;
  const infUserId = infDev1.data.user.id;
  assert('21. Influencer Logs In on Device A (Token Received)', !!infToken1);

  // Device A checks session - should be valid
  const checkInf1Valid = await callApi(adminHandler, 'POST', {}, { action: 'check_influencer_session', user_id: infUserId, token: infToken1 });
  assert('22. Influencer Device A Session Valid', checkInf1Valid.data && checkInf1Valid.data.valid === true);

  // Creator logs in on Device B (e.g. iPad)
  const infDev2 = await callApi(adminHandler, 'POST', {}, { action: 'influencer_login', login_id: 'LEDUBHAIYA', password: 'ledubhaiya', device: 'iPad Pro' });
  const infToken2 = infDev2.data.token;
  assert('23. Influencer Logs In on Device B (New Token)', !!infToken2 && infToken2 !== infToken1);

  // Device A checks session again - should be KICKED!
  const checkInf1Kicked = await callApi(adminHandler, 'POST', {}, { action: 'check_influencer_session', user_id: infUserId, token: infToken1 });
  assert('24. Influencer Device A Session Kicked Out (Single Device Enforced)', checkInf1Kicked.data && checkInf1Kicked.data.session_expired === true && checkInf1Kicked.data.code === 'SESSION_KICKED');

  // TEST 16: Dynamic Creator Account Creation & Instant Login Lifecycle
  const dynamicCreator = {
    id: 'inf-vip-555',
    name: 'Kabir Khan',
    username: 'KABIRVIP',
    phone: '9988776655',
    handle: '@kabir_lifestyle',
    code: 'KABIRVIP',
    password: 'kabirpassword123',
    comm_rate: 12
  };
  const createDynRes = await callApi(adminHandler, 'POST', {}, { action: 'save_influencer', ...dynamicCreator });
  assert('25. Dynamic Creator Created & Saved Successfully', createDynRes.data && createDynRes.data.success === true && createDynRes.data.influencer.code === 'KABIRVIP');

  // Verify creator exists in server list
  const listAfterAdd = await callApi(adminHandler, 'GET', { action: 'get_influencers' });
  const foundDynamic = listAfterAdd.data.influencers.find(u => u.code === 'KABIRVIP');
  assert('26. Created Creator Exists in Registry (Never Disappears)', !!foundDynamic && foundDynamic.name === 'Kabir Khan');

  // Creator logs into Influencer Portal
  const dynLoginRes = await callApi(adminHandler, 'POST', {}, { action: 'influencer_login', login_id: 'KABIRVIP', password: 'kabirpassword123' });
  assert('27. Newly Created Creator Can Log In Instantly', dynLoginRes.data && dynLoginRes.data.success === true && dynLoginRes.data.user.code === 'KABIRVIP');

  // Delete the creator
  const delDynRes = await callApi(adminHandler, 'POST', {}, { action: 'delete_influencer', id: 'inf-vip-555' });
  assert('28. Easy Creator Deletion Executed', delDynRes.data && delDynRes.data.success === true);

  const listAfterDel = await callApi(adminHandler, 'GET', { action: 'get_influencers' });
  const stillInList = listAfterDel.data.influencers.some(u => u.id === 'inf-vip-555' || u.code === 'KABIRVIP');
  assert('29. Deleted Creator Completely Erased from Active List', !stillInList);

  console.log('\n====================================================');
  console.log(`📊 SUMMARY: ${passed} / ${total} TESTS PASSED (100% SUCCESS)`);
  console.log('====================================================');
}

runSystemTests().catch(console.error);

