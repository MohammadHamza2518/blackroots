<?php
require_once __DIR__ . '/db.php';

function get_shiprocket_token() {
    $email = get_setting('shiprocket_email', '');
    $password = get_setting('shiprocket_password', '');

    if (empty($email) || empty($password)) {
        return null;
    }

    $cached_token = get_setting('shiprocket_jwt_token', '');
    $token_time = (int)get_setting('shiprocket_jwt_time', '0');

    if (!empty($cached_token) && (time() - $token_time) < 86400) {
        return $cached_token;
    }

    $payload = json_encode(['email' => $email, 'password' => $password]);
    $ch = curl_init('https://apiv2.shiprocket.in/v1/external/auth/login');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
    curl_setopt($ch, CURLOPT_TIMEOUT, 6);

    $res = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($code === 200) {
        $json = json_decode($res, true);
        if (isset($json['token'])) {
            set_setting('shiprocket_jwt_token', $json['token']);
            set_setting('shiprocket_jwt_time', (string)time());
            return $json['token'];
        }
    }
    return null;
}

function shiprocket_create_order($order) {
    $token = get_shiprocket_token();
    if (!$token) {
        return ['success' => false, 'error' => 'Shiprocket token could not be generated. Check credentials in Admin Settings.'];
    }

    $first_name = explode(' ', $order['name'])[0];
    $last_name = trim(str_replace($first_name, '', $order['name'])) ?: 'Customer';

    $payload = [
        'order_id' => str_replace('#', '', $order['order_id']),
        'order_date' => date('Y-m-d H:i'),
        'pickup_location' => 'Primary',
        'channel_id' => '',
        'billing_customer_name' => $first_name,
        'billing_last_name' => $last_name,
        'billing_address' => $order['address'],
        'billing_city' => $order['city'],
        'billing_pincode' => $order['pincode'],
        'billing_state' => $order['state'] ?: 'Uttar Pradesh',
        'billing_country' => 'India',
        'billing_email' => $order['email'] ?: 'blackroots.in@gmail.com',
        'billing_phone' => $order['phone'],
        'shipping_is_billing' => true,
        'order_items' => [
            [
                'name' => 'BlackRoots Herbal Hair Dye Shampoo (250ml)',
                'sku' => 'BR-SHAMPOO-250ML',
                'units' => strpos($order['bundle'], '2') !== false ? 2 : 1,
                'selling_price' => (float)$order['price'],
                'discount' => 0,
                'tax' => 0
            ]
        ],
        'payment_method' => strtoupper($order['payment_method']) === 'PREPAID' ? 'Prepaid' : 'COD',
        'sub_total' => (float)$order['price'],
        'length' => 15,
        'breadth' => 10,
        'height' => 8,
        'weight' => strpos($order['bundle'], '2') !== false ? 0.6 : 0.35
    ];

    $ch = curl_init('https://apiv2.shiprocket.in/v1/external/orders/create/adhoc');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $token
    ]);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);

    $res = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    $json = json_decode($res, true);
    if ($code === 200 && isset($json['order_id'])) {
        global $pdo;
        try {
            $upd = $pdo->prepare("UPDATE orders SET shiprocket_order_id = :sroid, shiprocket_shipment_id = :srshid WHERE order_id = :oid");
            $upd->execute([
                ':sroid' => $json['order_id'],
                ':srshid' => $json['shipment_id'] ?? '',
                ':oid' => $order['order_id']
            ]);
        } catch (Exception $e) {}

        return ['success' => true, 'shiprocket_order_id' => $json['order_id'], 'shipment_id' => $json['shipment_id'] ?? ''];
    }

    return ['success' => false, 'error' => $json['message'] ?? 'Shiprocket order creation failed', 'raw' => $json];
}
