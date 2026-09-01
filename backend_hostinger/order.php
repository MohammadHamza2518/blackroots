<?php
require_once __DIR__ . '/db.php';
require_once __DIR__ . '/meta_capi.php';
require_once __DIR__ . '/shiprocket.php';

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'error' => 'Invalid request method']);
    exit;
}

$raw = file_get_contents('php://input');
$input = json_decode($raw, true);
if (!$input) {
    $input = $_POST;
}

$name = trim($input['name'] ?? '');
$phone = trim($input['phone'] ?? '');
$email = trim($input['email'] ?? '');
$address = trim($input['address'] ?? '');
$city = trim($input['city'] ?? '');
$state = trim($input['state'] ?? '');
$pincode = trim($input['pincode'] ?? '');
$bundle = trim($input['bundle'] ?? '1 Bottle (250ml)');
$price = floatval($input['price'] ?? 499);
$payment_method = trim($input['payment_method'] ?? 'COD');
$payment_id = trim($input['payment_id'] ?? '');
$status = (stripos($payment_method, 'online') !== false || stripos($payment_method, 'prepaid') !== false || stripos($payment_method, 'razorpay') !== false || stripos($payment_method, 'paid') !== false) ? 'Paid' : 'New';

$clean_phone = preg_replace('/[^0-9]/', '', $phone);
if (strlen($clean_phone) > 10 && substr($clean_phone, 0, 2) === '91') {
    $clean_phone = substr($clean_phone, 2);
}
if (strlen($clean_phone) !== 10) {
    echo json_encode(['success' => false, 'error' => 'Please enter a valid 10-digit Indian mobile number.']);
    exit;
}

$clean_pincode = preg_replace('/[^0-9]/', '', $pincode);
if (strlen($clean_pincode) !== 6) {
    echo json_encode(['success' => false, 'error' => 'Please enter a valid 6-digit delivery pincode.']);
    exit;
}

if (empty($name) || empty($address)) {
    echo json_encode(['success' => false, 'error' => 'Full Name and Delivery Address are required.']);
    exit;
}

// Generate / Accept Order ID: #BR-XXXX
$client_oid = trim($input['order_id'] ?? '');
if (!empty($client_oid)) {
    $order_id = $client_oid;
} else {
    $stmt = $pdo->query("SELECT MAX(id) as max_id FROM orders");
    $row = $stmt->fetch();
    $next_num = ($row && $row['max_id']) ? ($row['max_id'] + 1025) : 1025;
    $order_id = '#BR-' . $next_num;
}
$default_awb = trim($input['tracking_awb'] ?? ('8839' . rand(100000, 999999)));
$coupon = trim($input['coupon'] ?? ($input['coupon_code'] ?? ''));
$nowStr = date('Y-m-d H:i:s');

try {
    $ins = $pdo->prepare("
        INSERT INTO orders (order_id, name, phone, email, address, city, state, pincode, product_bundle, price, payment_method, status, tracking_awb, courier, coupon, created_at)
        VALUES (:oid, :name, :phone, :email, :addr, :city, :state, :pin, :bundle, :price, :pm, :status, :awb, 'Delhivery Express Air', :coupon, :created)
    ");
    $ins->execute([
        ':oid' => $order_id,
        ':name' => $name,
        ':phone' => $clean_phone,
        ':email' => $email,
        ':addr' => $address,
        ':city' => $city,
        ':state' => $state,
        ':pin' => $clean_pincode,
        ':bundle' => $bundle,
        ':price' => $price,
        ':pm' => $payment_method,
        ':status' => $status,
        ':awb' => $default_awb,
        ':coupon' => $coupon,
        ':created' => $nowStr
    ]);

    // Real-time Influencer Attribution
    if (!empty($coupon)) {
        $cClean = strtoupper($coupon);
        $infSt = $pdo->prepare("SELECT * FROM influencers WHERE UPPER(code) = ? OR UPPER(username) = ? OR UPPER(code) = ? OR UPPER(username) = ? LIMIT 1");
        $infSt->execute([$cClean, $cClean, $cClean . '10', $cClean . '10']);
        $inf = $infSt->fetch();
        if ($inf) {
            $comm = round($price * (($inf['comm_rate'] ?? 10) / 100));
            $upInf = $pdo->prepare("
                UPDATE influencers 
                SET total_orders = COALESCE(total_orders, 0) + 1,
                    total_sales = COALESCE(total_sales, 0) + ?,
                    total_earned = COALESCE(total_earned, 0) + ?,
                    unpaid_balance = COALESCE(unpaid_balance, 0) + ?
                WHERE id = ?
            ");
            $upInf->execute([$price, $comm, $comm, $inf['id']]);
        }
    }

    // Mark from abandoned leads as recovered if exists
    try {
        $pdo->prepare("UPDATE abandoned_checkouts SET recovered = 1 WHERE phone = :ph")->execute([':ph' => $clean_phone]);
    } catch (Exception $e) {}

    // Auto-Push to Shiprocket if configured
    try {
        require_once __DIR__ . '/shiprocket.php';
        $srEmail = get_setting('shiprocket_email', '');
        $srPass = get_setting('shiprocket_password', '');
        if (!empty($srEmail) && !empty($srPass)) {
            shiprocket_create_order([
                'order_id' => $order_id,
                'name' => $name,
                'phone' => $clean_phone,
                'email' => $email,
                'address' => $address,
                'city' => $city,
                'state' => $state,
                'pincode' => $clean_pincode,
                'price' => $price,
                'payment_method' => $payment_method,
                'bundle' => $bundle
            ]);
        }
    } catch (Exception $e) {}

    // Trigger Meta Conversions API (CAPI) Server-side
    try {
        trigger_meta_capi_purchase($order_id, $price, [
            'phone' => $clean_phone,
            'name' => $name,
            'email' => $email,
            'city' => $city,
            'state' => $state,
            'pincode' => $clean_pincode
        ]);
    } catch (Exception $e) {}

    // Check Shiprocket Auto Push
    $sr_auto = get_setting('shiprocket_auto_push', '0');
    if ($sr_auto === '1') {
        shiprocket_create_order([
            'order_id' => $order_id,
            'name' => $name,
            'phone' => $clean_phone,
            'email' => $email,
            'address' => $address,
            'city' => $city,
            'state' => $state,
            'pincode' => $clean_pincode,
            'price' => $price,
            'payment_method' => $payment_method,
            'bundle' => $bundle
        ]);
    }

    echo json_encode([
        'success' => true,
        'order_id' => $order_id,
        'awb' => $default_awb,
        'courier' => 'Delhivery Express Air',
        'message' => 'Order placed successfully! Dispatched from Shuklaganj UP central warehouse.',
        'estimated_delivery' => 'Within 48-72 Hours',
        'customer' => [
            'name' => $name,
            'phone' => $clean_phone,
            'city' => $city
        ]
    ]);

} catch (Exception $e) {
    echo json_encode(['success' => false, 'error' => 'Failed to save order: ' . $e->getMessage()]);
}
