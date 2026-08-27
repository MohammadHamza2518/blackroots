<?php
require_once __DIR__ . '/db.php';

header('Content-Type: application/json');

$raw = file_get_contents('php://input');
$input = json_decode($raw, true) ?: $_POST;

$phone = trim($input['phone'] ?? '');
$name = trim($input['name'] ?? 'Visitor');
$bundle = trim($input['bundle'] ?? '1 Bottle (250ml)');
$price = floatval($input['price'] ?? 499);

$clean_phone = preg_replace('/[^0-9]/', '', $phone);
if (strlen($clean_phone) > 10 && substr($clean_phone, 0, 2) === '91') {
    $clean_phone = substr($clean_phone, 2);
}

if (strlen($clean_phone) >= 10) {
    try {
        // Check if already ordered recently
        $st = $pdo->prepare("SELECT id FROM orders WHERE phone = :ph");
        $st->execute([':ph' => $clean_phone]);
        if ($st->fetch()) {
            echo json_encode(['success' => true, 'status' => 'already_ordered']);
            exit;
        }

        // Upsert into abandoned_checkouts
        $st2 = $pdo->prepare("SELECT id FROM abandoned_checkouts WHERE phone = :ph AND recovered = 0");
        $st2->execute([':ph' => $clean_phone]);
        $row = $st2->fetch();

        if ($row) {
            $upd = $pdo->prepare("UPDATE abandoned_checkouts SET name = :nm, product_bundle = :bd, price = :pr, created_at = CURRENT_TIMESTAMP WHERE id = :id");
            $upd->execute([':nm' => $name, ':bd' => $bundle, ':pr' => $price, ':id' => $row['id']]);
        } else {
            $ins = $pdo->prepare("INSERT INTO abandoned_checkouts (name, phone, product_bundle, price) VALUES (:nm, :ph, :bd, :pr)");
            $ins->execute([':nm' => $name, ':ph' => $clean_phone, ':bd' => $bundle, ':pr' => $price]);
        }

        echo json_encode(['success' => true]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

echo json_encode(['success' => false, 'error' => 'Invalid phone']);
