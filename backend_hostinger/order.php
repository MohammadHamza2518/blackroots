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

// Check for duplicate spam submissions within last 2 minutes
try {
    $stmt = $pdo->prepare("SELECT id, order_id FROM orders WHERE phone = :ph AND created_at >= datetime('now', '-2 minutes')");
    $stmt->execute([':ph' => $clean_phone]);
    $dup = $stmt->fetch();
    if ($dup) {
        echo json_encode([
            'success' => true,
            'order_id' => $dup['order_id'],
            'message' => 'Your order is already registered! Our logistics team will call you before delivery.',
            'is_duplicate' => true
        ]);
        exit;
    }
} catch (Exception $e) {}

// Generate Order ID: #BR-XXXX
$stmt = $pdo->query("SELECT MAX(id) as max_id FROM orders");
$row = $stmt->fetch();
$next_num = ($row && $row['max_id']) ? ($row['max_id'] + 1025) : 1025;
$order_id = '#BR-' . $next_num;
$default_awb = '8839' . rand(100000, 999999);

try {
    $ins = $pdo->prepare("
        INSERT INTO orders (order_id, name, phone, email, address, city, state, pincode, product_bundle, price, payment_method, status, tracking_awb, courier)
        VALUES (:oid, :name, :phone, :email, :addr, :city, :state, :pin, :bundle, :price, :pm, 'New', :awb, 'Delhivery Express Air')
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
        ':awb' => $default_awb
    ]);

    // Mark from abandoned leads as recovered if exists
    try {
        $pdo->prepare("UPDATE abandoned_checkouts SET recovered = 1 WHERE phone = :ph")->execute([':ph' => $clean_phone]);
    } catch (Exception $e) {}

    // Trigger Meta Conversions API (CAPI) Server-side
    trigger_meta_capi_purchase($order_id, $price, [
        'phone' => $clean_phone,
        'name' => $name,
        'email' => $email,
        'city' => $city,
        'state' => $state,
        'pincode' => $clean_pincode
    ]);

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
