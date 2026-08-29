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

$selectedItem = $body['items'][0] ?? [
    'name' => 'BlackRoots Herbal Hair Darkening Shampoo (250ml)',
    'price' => 499,
    'quantity' => 1,
    'sku' => 'BR-250ML'
];

$payload = [
    'cart' => [
        'items' => [
            [
                'name' => $selectedItem['name'],
                'sku' => $selectedItem['sku'] ?? 'BR-250ML',
                'unit_price' => (int)($selectedItem['price'] ?? 499),
                'quantity' => (int)($selectedItem['quantity'] ?? 1)
            ]
        ]
    ],
    'redirect_url' => 'https://blackroots.in/track-order.html',
    'cancel_url' => 'https://blackroots.in/product.html'
];

$payloadString = json_encode($payload);
$hmac = base64_encode(hash_hmac('sha256', $payloadString, $API_SECRET, true));

$ch = curl_init('https://checkout-api.shiprocket.com/v1/checkout/create');
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

if ($httpCode >= 200 && $httpCode < 300 && (!empty($data['checkout_url']) || !empty($data['url']))) {
    echo json_encode([
        'success' => true,
        'checkout_url' => $data['checkout_url'] ?? $data['url'],
        'token' => $data['token'] ?? null
    ]);
} else {
    echo json_encode([
        'success' => false,
        'fallback' => true,
        'raw' => $data
    ]);
}
?>