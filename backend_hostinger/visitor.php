<?php
require_once __DIR__ . '/db.php';

header('Content-Type: application/json');

$ip = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? '';
$page = trim($_GET['page'] ?? $_POST['page'] ?? 'home');
$ua = $_SERVER['HTTP_USER_AGENT'] ?? '';
$city = $_SERVER['HTTP_CF_IPCITY'] ?? 'India';

try {
    // Log visitor
    $ins = $pdo->prepare("INSERT INTO visitors (ip_address, page_url, user_agent, city) VALUES (:ip, :pg, :ua, :ct)");
    $ins->execute([':ip' => $ip, ':pg' => $page, ':ua' => substr($ua, 0, 200), ':ct' => $city]);

    // Get live count (active last 5 minutes)
    $st = $pdo->query("SELECT COUNT(DISTINCT ip_address) as live_cnt FROM visitors WHERE created_at >= datetime('now', '-5 minutes')");
    $row = $st->fetch();
    $live_count = ($row && $row['live_cnt']) ? (int)$row['live_cnt'] : rand(45, 85);

    echo json_encode([
        'success' => true,
        'live_viewers' => max(18, $live_count),
        'city' => $city
    ]);
} catch (Exception $e) {
    echo json_encode(['success' => true, 'live_viewers' => rand(38, 72)]);
}
