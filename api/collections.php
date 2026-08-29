<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, X-Api-Key, X-Api-HMAC-SHA256');
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$collections = [
    "success" => true,
    "total_collections" => 1,
    "collections" => [
        [
            "id" => "blackroots-all",
            "title" => "All BlackRoots Products",
            "handle" => "all-products",
            "description" => "Ayurvedic Hair Darkening Shampoo & Herbal Care",
            "products_count" => 2,
            "image" => "https://blackroots.in/assets/blackroots-hero-luxury-render.png"
        ]
    ]
];

echo json_encode($collections);
?>