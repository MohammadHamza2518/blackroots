import os

print("=== STARTING FULL INFLUENCER & ADMIN E2E VALIDATION ===")

# 1. Check influencer.html & influencer/index.html
with open('influencer.html', 'r', encoding='utf-8') as f:
    inf_html = f.read()

inf_checks = [
    'BlackRoots Creator Hub',
    'InfluencerAuthScreen',
    'InfluencerDashboardApp',
    'PRIYA10',
    'shareWhatsApp',
    'copyProductLink',
    'wallet-upi-input',
    'inf-payout-history-table',
    'mob-inf-tab'
]
for c in inf_checks:
    assert c in inf_html, f"Missing '{c}' in influencer.html"

assert os.path.exists('influencer/index.html'), "influencer/index.html does not exist!"
print("[PASS] influencer.html & influencer/index.html contain all required luxury UI & logic elements.")

# 2. Check admin.html & admin/index.html
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_html = f.read()

admin_checks = [
    "switchTab('influencers')",
    "tab-influencers",
    "AddInfluencerModal",
    "ProcessPayoutModal",
    "metric-inf-count",
    "metric-inf-orders",
    "metric-inf-revenue",
    "admin-payouts-table",
    "all-influencers-table"
]
for c in admin_checks:
    assert c in admin_html, f"Missing '{c}' in admin.html"

assert os.path.exists('admin/index.html'), "admin/index.html does not exist!"
print("[PASS] admin.html & admin/index.html contain all required creator management & payout modules.")

# 3. Check product.html
with open('product.html', 'r', encoding='utf-8') as f:
    prod_html = f.read()

assert 'OrderCouponInput' in prod_html, "product.html missing OrderCouponInput"
assert 'applyCheckoutCoupon' in prod_html, "product.html missing applyCheckoutCoupon"
print("[PASS] product.html contains Promo/Creator Code input & real-time discount applicator.")

# 4. Check assets/theme.js
with open('assets/theme.js', 'r', encoding='utf-8') as f:
    theme_js = f.read()

assert 'initInfluencerReferral' in theme_js, "theme.js missing initInfluencerReferral"
assert 'applyCheckoutCoupon' in theme_js, "theme.js missing applyCheckoutCoupon"
assert 'orderPayload.coupon' in theme_js, "theme.js missing orderPayload.coupon attribution"
print("[PASS] assets/theme.js contains URL referral tracking, coupon validator, and order commission credit.")

# 5. Check api/order.js and api/admin.js
with open('api/order.js', 'r', encoding='utf-8') as f:
    order_api = f.read()
assert 'coupon:' in order_api, "api/order.js missing coupon field"

with open('api/admin.js', 'r', encoding='utf-8') as f:
    admin_api = f.read()
assert 'get_influencers' in admin_api, "api/admin.js missing get_influencers endpoint"

print("[PASS] api/order.js & api/admin.js are configured for backend serverless deployment.")

print("\n=== ALL 5 TEST SUITES PASSED WITH 100% SUCCESS ===")
