<?php
require_once __DIR__ . '/db.php';

function trigger_meta_capi_purchase($order_id, $amount, $customer_data = []) {
    $pixel_id = get_setting('meta_pixel_id', '');
    $access_token = get_setting('meta_capi_token', '');

    if (empty($pixel_id) || empty($access_token)) {
        return ['success' => false, 'message' => 'Meta Pixel ID or Access Token not configured'];
    }

    $client_ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? '';
    $user_agent = $_SERVER['HTTP_USER_AGENT'] ?? '';

    $phone = preg_replace('/[^0-9]/', '', $customer_data['phone'] ?? '');
    if (strlen($phone) === 10) {
        $phone = '91' . $phone;
    }
    $hashed_phone = !empty($phone) ? hash('sha256', $phone) : null;
    $hashed_email = !empty($customer_data['email']) ? hash('sha256', strtolower(trim($customer_data['email']))) : null;
    $hashed_fn = !empty($customer_data['name']) ? hash('sha256', strtolower(trim(explode(' ', $customer_data['name'])[0]))) : null;
    $hashed_city = !empty($customer_data['city']) ? hash('sha256', strtolower(trim($customer_data['city']))) : null;
    $hashed_zip = !empty($customer_data['pincode']) ? hash('sha256', trim($customer_data['pincode'])) : null;
    $hashed_country = hash('sha256', 'in');

    $event_data = [
        'event_name' => 'Purchase',
        'event_time' => time(),
        'event_id' => 'order_' . str_replace('#', '', $order_id),
        'event_source_url' => $_SERVER['HTTP_REFERER'] ?? 'https://' . ($_SERVER['HTTP_HOST'] ?? 'blackroots.in') . '/product.html',
        'action_source' => 'website',
        'user_data' => array_filter([
            'ph' => $hashed_phone ? [$hashed_phone] : null,
            'em' => $hashed_email ? [$hashed_email] : null,
            'fn' => $hashed_fn ? [$hashed_fn] : null,
            'ct' => $hashed_city ? [$hashed_city] : null,
            'zp' => $hashed_zip ? [$hashed_zip] : null,
            'country' => [$hashed_country],
            'client_ip_address' => $client_ip,
            'client_user_agent' => $user_agent,
        ]),
        'custom_data' => [
            'currency' => 'INR',
            'value' => (float)$amount,
            'order_id' => $order_id,
            'content_name' => 'BlackRoots Herbal Hair Dye Shampoo',
            'content_type' => 'product',
        ]
    ];

    $payload = json_encode(['data' => [$event_data]]);

    $ch = curl_init("https://graph.facebook.com/v19.0/{$pixel_id}/events?access_token={$access_token}");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
    curl_setopt($ch, CURLOPT_TIMEOUT, 5);

    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    return ['success' => $http_code >= 200 && $http_code < 300, 'response' => $response];
}
