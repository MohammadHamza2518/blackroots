<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, X-Api-Key, X-Api-HMAC-SHA256');
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$API_KEY = 'hl7tTx1OioeJn0KS';
$API_SECRET = 'SX9xl506RtMcE6761XJgkzhJOl1QCUW6';

$input = file_get_contents('php://input');
$body = json_decode($input, true) ?? [];

$qty = (int)($body['qty'] ?? 1);
$basePrice = (float)($body['price'] ?? ($qty === 2 ? 799 : 499));
$title = $body['title'] ?? ($qty === 2 ? 'BlackRoots Herbal Shampoo (Duo Pack - 500ml)' : 'BlackRoots Herbal Shampoo (250ml)');
$isOnline = $body['isOnline'] ?? true;
$coupon = $body['coupon'] ?? '';

$discountAmt = $isOnline ? 50.0 : 0.0;
$variantId = ($qty === 2) ? '1002' : '1001';
$imgUrl = ($qty === 2) 
    ? 'https://blackroots.in/assets/blackroots-bottle-duo.png' 
    : 'https://blackroots.in/assets/blackroots-bottle-single.png';

$now = new DateTime('now', new DateTimeZone('UTC'));
$timestamp = $now->format('Y-m-d\TH:i:s.u\Z');

$payload = [
    'cart_data' => [
        'items' => [
            [
                'variant_id' => $variantId,
                'quantity' => $qty,
                'catalog_data' => [
                    'price' => $basePrice,
                    'name' => $title,
                    'image_url' => $imgUrl
                ]
            ]
        ],
        'mobile_app' => false
    ],
    'redirect_url' => 'https://blackroots.in/track-order.html',
    'timestamp' => $timestamp
];

if ($discountAmt > 0) {
    $payload['cart_data']['cart_discount'] = [
        'coupon_code' => !empty($coupon) ? $coupon : 'PREPAID50',
        'amount' => $discountAmt
    ];
}

$payloadString = json_encode($payload);
$hmac = base64_encode(hash_hmac('sha256', $payloadString, $API_SECRET, true));

$ch = curl_init('https://checkout-api.shiprocket.com/api/v1/access-token/checkout');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payloadString);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'X-Api-Key: ' . $API_KEY,
    'X-Api-HMAC-SHA256: ' . $hmac
]);
curl_setopt($ch, CURLOPT_TIMEOUT, 8);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$data = json_decode($response, true) ?? [];

if ($httpCode >= 200 && $httpCode < 300 && !empty($data['ok']) && !empty($data['result']['token'])) {
    echo json_encode([
        'success' => true,
        'token' => $data['result']['token'],
        'order_id' => $data['result']['data']['order_id'] ?? null
    ]);
} else {
    echo json_encode([
        'success' => false,
        'error' => $data['error']['message'] ?? 'Unable to generate Fastrr token',
        'raw' => $data
    ]);
}
?>