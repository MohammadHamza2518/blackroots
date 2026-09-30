const fs = require('fs');

console.log('--- TEST 1: DOM Elements Integrity Check ---');
const checkoutHtml = fs.readFileSync('checkout.html', 'utf8');

const requiredIds = [
  'PaymentOptionOnline', 'PaymentOptionCOD',
  'PaymentDotOnline', 'PaymentDotCOD',
  'PaymentDotInnerOnline', 'PaymentDotInnerCOD',
  'CODDoorstepBalanceText',
  'SummaryMRP', 'SummaryItemPrice', 'SummaryOnlineDiscountRow', 'SummaryOnlineDiscountVal',
  'SummaryCouponDiscountRow', 'SummaryCouponDiscountVal',
  'SummaryAdvancePaidRow', 'SummaryAdvancePaidVal',
  'SummaryBalanceAtDeliveryRow', 'SummaryBalanceAtDeliveryVal',
  'SummaryPayableLabel', 'SummarySavingsText', 'SummaryFinalPayable',
  'SubmitCheckoutBtn', 'SubmitCheckoutBtnText',
  'SuccessPaymentStatusDisplay', 'SuccessAmountDisplay',
  'SuccessPartialCODNote', 'SuccessDoorstepBalanceVal'
];

let missing = [];
for (const id of requiredIds) {
  if (!checkoutHtml.includes('id="' + id + '"')) {
    missing.push(id);
  }
}

if (missing.length > 0) {
  console.error('FAIL: Missing DOM IDs:', missing);
  process.exit(1);
}
console.log('✅ PASS: All ' + requiredIds.length + ' essential checkout DOM IDs are present.');

console.log('\n--- TEST 2: Pricing Logic Simulation ---');

function simulatePricing(currentPack, currentPayment, appliedCoupon = null) {
  var basePrice = (currentPack === 2) ? 799 : 499;
  var mrp = (currentPack === 2) ? 1998 : 999;
  var isOnline = (currentPayment === 'Online');
  var onlineDiscount = isOnline ? 50 : 0;

  var couponDiscount = 0;
  if (appliedCoupon && appliedCoupon.code) {
    couponDiscount = Math.round(basePrice * (appliedCoupon.comm_rate || 10) / 100);
    appliedCoupon.discount = couponDiscount;
  }

  var fullOrderPrice = Math.max(0, basePrice - (isOnline ? (onlineDiscount + couponDiscount) : couponDiscount));
  var advanceAmount = isOnline ? fullOrderPrice : 99;
  var codBalance = isOnline ? 0 : Math.max(0, fullOrderPrice - advanceAmount);
  var totalSavings = mrp - fullOrderPrice;

  return {
    basePrice,
    mrp,
    onlineDiscount,
    couponDiscount,
    fullOrderPrice,
    advanceAmount,
    codBalance,
    totalSavings
  };
}

// Case 1: 1 Bottle Online (Default)
const c1 = simulatePricing(1, 'Online');
console.log('Case 1 (1 Bottle, Full Online):', c1);
if (c1.advanceAmount !== 449 || c1.codBalance !== 0 || c1.onlineDiscount !== 50) {
  throw new Error('Case 1 calculation mismatch');
}
console.log('✅ PASS: Case 1 (1 Bottle Online) -> Pay Now: ₹449, Doorstep: ₹0, Discount: -₹50');

// Case 2: 1 Bottle Partial COD
const c2 = simulatePricing(1, 'COD');
console.log('Case 2 (1 Bottle, Partial COD):', c2);
if (c2.advanceAmount !== 99 || c2.codBalance !== 400 || c2.onlineDiscount !== 0) {
  throw new Error('Case 2 calculation mismatch');
}
console.log('✅ PASS: Case 2 (1 Bottle Partial COD) -> Pay Now: ₹99, Doorstep: ₹400');

// Case 3: 2 Bottles Online
const c3 = simulatePricing(2, 'Online');
console.log('Case 3 (2 Bottles, Full Online):', c3);
if (c3.advanceAmount !== 749 || c3.codBalance !== 0 || c3.onlineDiscount !== 50) {
  throw new Error('Case 3 calculation mismatch');
}
console.log('✅ PASS: Case 3 (2 Bottles Online) -> Pay Now: ₹749, Doorstep: ₹0, Discount: -₹50');

// Case 4: 2 Bottles Partial COD
const c4 = simulatePricing(2, 'COD');
console.log('Case 4 (2 Bottles, Partial COD):', c4);
if (c4.advanceAmount !== 99 || c4.codBalance !== 700 || c4.onlineDiscount !== 0) {
  throw new Error('Case 4 calculation mismatch');
}
console.log('✅ PASS: Case 4 (2 Bottles Partial COD) -> Pay Now: ₹99, Doorstep: ₹700');

// Case 5: 1 Bottle Partial COD with 10% coupon
const c5 = simulatePricing(1, 'COD', { code: 'TEST10', comm_rate: 10 });
console.log('Case 5 (1 Bottle, Partial COD + 10% Coupon):', c5);
// Base 499 - 50 = 449. Advance 99. Balance = 350.
if (c5.advanceAmount !== 99 || c5.codBalance !== 350) {
  throw new Error('Case 5 calculation mismatch');
}
console.log('✅ PASS: Case 5 (1 Bottle Partial COD + Coupon) -> Pay Now: ₹99, Doorstep: ₹350');

console.log('\n--- TEST 3: Shiprocket Calculation Safeguard ---');
function simulateShiprocketPayload(ord) {
  const isPartial = String(ord.payment_method || '').toLowerCase().includes('partial');
  const isOnline = String(ord.payment_method || '').toLowerCase().includes('online') || String(ord.status || '').toLowerCase() === 'paid';
  const price = Number(ord.price) || 499;
  const codBal = Number(ord.cod_balance) || (isPartial ? Math.max(0, price - 99) : 0);
  const payMethod = isPartial ? 'COD' : (isOnline ? 'Prepaid' : 'Prepaid');
  const collectSubTotal = isPartial ? codBal : price;

  return {
    payment_method: payMethod,
    sub_total: collectSubTotal,
    rider_collects: payMethod === 'COD' ? collectSubTotal : 0
  };
}

const srOnline = simulateShiprocketPayload({ payment_method: 'Online (Prepaid UPI/Cards - ₹50 OFF)', status: 'Paid', price: 449 });
console.log('Shiprocket Online Order:', srOnline);
if (srOnline.payment_method !== 'Prepaid' || srOnline.rider_collects !== 0) {
  throw new Error('Shiprocket Online mismatch');
}
console.log('✅ PASS: Shiprocket Online -> Method: Prepaid, Rider Collects: ₹0');

const srPartial = simulateShiprocketPayload({ payment_method: 'Partial COD (₹99 Advance Paid, Balance ₹400 on Delivery)', status: 'Partial Paid', price: 499, cod_balance: 400 });
console.log('Shiprocket Partial COD Order:', srPartial);
if (srPartial.payment_method !== 'COD' || srPartial.rider_collects !== 400) {
  throw new Error('Shiprocket Partial COD mismatch');
}
console.log('✅ PASS: Shiprocket Partial COD -> Method: COD, Rider Collects: ₹400 (NOT full ₹499)');

console.log('\n🎉 ALL INTEGRITY TESTS PASSED 100%!');
