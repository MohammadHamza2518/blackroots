import os

# 1. Update theme.js
with open('assets/theme.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

old_order_payload = """        let orderPayload = {
          name: allInputs[0] ? allInputs[0].value.trim() : '',
          phone: allInputs[1] ? allInputs[1].value.trim() : '',
          pincode: allInputs[2] ? allInputs[2].value.trim() : '',
          city: allInputs[3] ? allInputs[3].value.trim() : '',
          address: allInputs[4] ? allInputs[4].value.trim() : '',
          bundle: window.selectedPack ? window.selectedPack.name : '1 Bottle (250ml)',
          price: window.selectedPack ? window.selectedPack.price : 499,
          payment_method: 'COD'
        };"""

new_order_payload = """        let basePrice = window.selectedPack ? window.selectedPack.price : 499;
        let appliedCoupon = window.appliedCouponData ? window.appliedCouponData.code : (localStorage.getItem('br_active_coupon') || '');
        let finalPrice = window.appliedCouponData ? window.appliedCouponData.finalPrice : basePrice;

        let orderPayload = {
          name: allInputs[0] ? allInputs[0].value.trim() : '',
          phone: allInputs[1] ? allInputs[1].value.trim() : '',
          pincode: allInputs[2] ? allInputs[2].value.trim() : '',
          city: allInputs[3] ? allInputs[3].value.trim() : '',
          address: allInputs[4] ? allInputs[4].value.trim() : '',
          bundle: window.selectedPack ? window.selectedPack.name : '1 Bottle (250ml)',
          price: finalPrice,
          payment_method: 'COD',
          coupon: appliedCoupon,
          discount: basePrice - finalPrice
        };"""

if old_order_payload in js_content:
    js_content = js_content.replace(old_order_payload, new_order_payload)

old_local_cache = """          // Local cache for immediate admin view
          try {
            let curOrders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
            curOrders.unshift(orderPayload);
            localStorage.setItem('br_local_orders', JSON.stringify(curOrders.slice(0, 100)));
          } catch(e) {}"""

new_local_cache = """          // Local cache for immediate admin view & Influencer Credit
          try {
            let curOrders = JSON.parse(localStorage.getItem('br_local_orders') || '[]');
            curOrders.unshift(orderPayload);
            localStorage.setItem('br_local_orders', JSON.stringify(curOrders.slice(0, 100)));

            // Credit Commission to Influencer
            if (orderPayload.coupon) {
              let db = JSON.parse(localStorage.getItem('br_influencers_db') || '[]');
              let inf = db.find(u => u.code && u.code.toUpperCase() === orderPayload.coupon.toUpperCase());
              if (inf) {
                let commRate = inf.comm_rate || 10;
                let commAmt = Math.round(orderPayload.price * (commRate / 100));
                inf.total_orders = (Number(inf.total_orders) || 0) + 1;
                inf.total_sales = (Number(inf.total_sales) || 0) + Number(orderPayload.price);
                inf.total_earned = (Number(inf.total_earned) || 0) + commAmt;
                inf.unpaid_balance = (Number(inf.unpaid_balance) || 0) + commAmt;
                orderPayload.influencer = inf.name;
                localStorage.setItem('br_influencers_db', JSON.stringify(db));
              }
            }
          } catch(e) {}"""

if old_local_cache in js_content:
    js_content = js_content.replace(old_local_cache, new_local_cache)

with open('assets/theme.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print("1. theme.js patched successfully")

# 2. Update api/order.js
with open('api/order.js', 'r', encoding='utf-8') as f:
    order_api = f.read()

target_payment = "payment_method: input.payment_method || 'COD',"
replacement_payment = """payment_method: input.payment_method || 'COD',
    coupon: input.coupon || input.coupon_code || '',
    discount: input.discount || 0,
    influencer: input.influencer || '',"""

if target_payment in order_api and "coupon: input.coupon" not in order_api:
    order_api = order_api.replace(target_payment, replacement_payment)
    with open('api/order.js', 'w', encoding='utf-8') as f:
        f.write(order_api)
    print("2. api/order.js patched successfully")
else:
    print("2. api/order.js already updated or target not found")

# 3. Update api/admin.js
with open('api/admin.js', 'r', encoding='utf-8') as f:
    admin_api = f.read()

influencer_api_snippet = """  // 9. Influencer API actions
  if (action === 'get_influencers') {
    return res.status(200).json({ success: true, influencers: memoryStore.influencers || [] });
  }
  if (action === 'save_influencer') {
    if (!memoryStore.influencers) memoryStore.influencers = [];
    const inf = req.body || {};
    const existingIdx = memoryStore.influencers.findIndex(u => u.id === inf.id || u.code === inf.code);
    if (existingIdx !== -1) {
      memoryStore.influencers[existingIdx] = Object.assign(memoryStore.influencers[existingIdx], inf);
    } else {
      memoryStore.influencers.push(inf);
    }
    saveDb();
    return res.status(200).json({ success: true, message: 'Influencer saved!' });
  }
"""

if "action === 'get_influencers'" not in admin_api:
    admin_api = admin_api.replace("return res.status(200).json({ success: true, message: 'BlackRoots API ready' });", influencer_api_snippet + "\n  return res.status(200).json({ success: true, message: 'BlackRoots API ready' });")
    with open('api/admin.js', 'w', encoding='utf-8') as f:
        f.write(admin_api)
    print("3. api/admin.js patched successfully")
else:
    print("3. api/admin.js already has influencer actions")

print("All backend & theme files updated!")
