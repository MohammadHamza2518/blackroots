<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, X-Api-Key, X-Api-HMAC-SHA256');
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$input = file_get_contents('php://input');
$payload = json_decode($input, true) ?? [];

echo json_encode([
    "success" => true,
    "message" => "Webhook processed successfully",
    "order_id" => $payload['order_id'] ?? $payload['order_number'] ?? ("BR-" . time())
]);
?>