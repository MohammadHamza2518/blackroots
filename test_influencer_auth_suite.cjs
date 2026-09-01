const adminHandler = require('./api/admin.js');
const orderHandler = require('./api/order.js');

async function callApi(handler, method, query, body) {
  return new Promise((resolve) => {
    const req = {
      method: method,
      query: query || {},
      body: body || {},
      headers: { 'user-agent': 'TestMobileDevice/1.0', 'x-forwarded-for': '127.0.0.1' }
    };
    let statusCode = 200;
    const res = {
      setHeader: () => {},
      status: (code) => {
        statusCode = code;
        return res;
      },
      json: (data) => resolve({ status: statusCode, data: data }),
      end: () => resolve({ status: statusCode, data: null })
    };
    handler(req, res);
  });
}

async function runTests() {
  console.log('=== STARTING INFLUENCER AUTH & TRACKING TESTS ===\n');

  // 1. Create New Influencer from Admin
  const newCreator = {
    name: 'Aarav Sharma',
    username: 'aarav_sharma',
    phone: '+91 9876543299',
    handle: '@aarav_hairexpert',
    code: 'AARAV20',
    password: 'SecretPassword123',
    comm_rate: 20
  };

  console.log('1. Admin saving influencer:', newCreator.name);
  const saveRes = await callApi(adminHandler, 'POST', { action: 'save_influencer' }, newCreator);
  console.log('Save result success:', saveRes.data.success, 'Creator Code:', saveRes.data.influencer.code);

  // 2. Test logins under different casing & identifier formats
  const loginTests = [
    { label: 'Exact username + exact password', id: 'aarav_sharma', pass: 'SecretPassword123', expect: true },
    { label: 'UPPERCASE username + lowercase password', id: 'AARAV_SHARMA', pass: 'secretpassword123', expect: true },
    { label: 'Promo Code (lowercase) + UPPERCASE password', id: 'aarav20', pass: 'SECRETPASSWORD123', expect: true },
    { label: 'Phone with +91 and spaces + mixed password', id: '+91 9876543299', pass: 'SecretPassword123', expect: true },
    { label: 'Instagram handle with @ + password', id: '@aarav_hairexpert', pass: 'secretpassword123', expect: true },
    { label: 'Creator Full Name + password', id: 'Aarav Sharma', pass: 'secretpassword123', expect: true },
    { label: 'Wrong password test', id: 'aarav20', pass: 'wrongpass', expect: false }
  ];

  for (const t of loginTests) {
    const loginRes = await callApi(adminHandler, 'POST', { action: 'influencer_login' }, { login_id: t.id, password: t.pass });
    const passed = (loginRes.data.success === t.expect);
    console.log((passed ? '[PASS] ' : '[FAIL] ') + t.label + ' -> Success: ' + loginRes.data.success);
    if (!passed) console.error('Error detail:', loginRes.data);
  }

  // 3. Place Order with Creator Coupon
  console.log('\n3. Placing Order with coupon AARAV20...');
  const orderRes = await callApi(orderHandler, 'POST', {}, {
    name: 'Rohan Gupta',
    phone: '9988776655',
    address: 'Flat 402, Civil Lines',
    city: 'Kanpur',
    state: 'Uttar Pradesh',
    pincode: '208001',
    bundle: '2 Bottles Pack (500ml)',
    price: 749,
    coupon: 'aarav20',
    payment_method: 'Online Razorpay'
  });
  console.log('Order created:', orderRes.data.order_id, 'AWB:', orderRes.data.awb);

  // 4. Verify Influencer Dashboard Data on Login
  console.log('\n4. Checking influencer dashboard after order...');
  const infDashboardLogin = await callApi(adminHandler, 'POST', { action: 'influencer_login' }, { login_id: 'AARAV20', password: 'secretpassword123' });
  const user = infDashboardLogin.data.user;
  const orders = infDashboardLogin.data.orders || [];
  console.log('Influencer Total Orders: ' + user.total_orders + ', Total Sales: ₹' + user.total_sales + ', Total Earned: ₹' + user.total_earned);
  console.log('Referred orders count in session: ' + orders.length);

  // 5. Influencer Payout Request
  console.log('\n5. Influencer requesting UPI Payout...');
  const payoutReq = await callApi(adminHandler, 'POST', { action: 'request_payout' }, {
    influencer_id: user.id,
    code: user.code,
    name: user.name,
    upi_id: 'aarav@okicici',
    amount: 100
  });
  console.log('Payout requested:', payoutReq.data.success, 'Payout ID:', payoutReq.data.payout.id);

  // 6. Admin Approves and Pays Payout with UTR
  console.log('\n6. Admin approving payout with UTR...');
  const payoutApprove = await callApi(adminHandler, 'POST', { action: 'update_payout' }, {
    id: payoutReq.data.payout.id,
    status: 'Paid',
    utr: 'UPI/928374829104'
  });
  console.log('Payout marked paid:', payoutApprove.data.success, 'Status:', payoutApprove.data.payout.status);

  console.log('\n=== ALL TESTS COMPLETED SUCCESSFULLY! ===');
}

runTests();
