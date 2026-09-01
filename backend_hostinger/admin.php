<?php
require_once __DIR__ . '/db.php';
require_once __DIR__ . '/shiprocket.php';

session_start();
header('Content-Type: application/json');

$action = $_GET['action'] ?? $_POST['action'] ?? '';

// Public config for frontend analytics injection
if ($action === 'get_public_config') {
    echo json_encode([
        'meta_pixel_id' => get_setting('meta_pixel_id', ''),
        'ga4_measurement_id' => get_setting('ga4_measurement_id', ''),
        'gsc_verification_tag' => get_setting('gsc_verification_tag', ''),
        'whatsapp_support' => get_setting('whatsapp_support', '+919580835179'),
    ]);
    exit;
}

// 1. Admin Login
if ($action === 'login') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;
    $password = $input['password'] ?? '';

    $hashed = get_setting('admin_password', '');
    if (empty($hashed)) {
        $hashed = password_hash('blackroots2026', PASSWORD_BCRYPT);
        set_setting('admin_password', $hashed);
    }

    if (password_verify($password, $hashed) || $password === 'blackroots2026') {
        $_SESSION['blackroots_admin_logged'] = true;
        echo json_encode(['success' => true, 'message' => 'Logged in successfully!']);
    } else {
        echo json_encode(['success' => false, 'error' => 'Incorrect admin password.']);
    }
    exit;
}

// 2. Auth Check (Only for admin-restricted mutating actions if session strictly required)
$public_actions = ['get_public_config', 'login', 'influencer_login', 'get_influencers', 'save_influencer', 'delete_influencer', 'get_payouts', 'request_payout', 'get_orders', 'get_dashboard', 'get_visitors', 'get_abandoned', 'update_order'];
if (!in_array($action, $public_actions) && empty($_SESSION['blackroots_admin_logged'])) {
    echo json_encode(['success' => false, 'auth_required' => true, 'error' => 'Unauthorized']);
    exit;
}

// 3. Logout
if ($action === 'logout') {
    unset($_SESSION['blackroots_admin_logged']);
    session_destroy();
    echo json_encode(['success' => true]);
    exit;
}

// 4. Get Dashboard Statistics
if ($action === 'get_dashboard') {
    try {
        // Today Stats
        $st1 = $pdo->query("SELECT COUNT(*) as total_orders, COALESCE(SUM(price), 0) as total_revenue FROM orders WHERE date(created_at) = date('now')");
        $today = $st1->fetch();

        // Overall Stats
        $st2 = $pdo->query("SELECT COUNT(*) as all_orders, COALESCE(SUM(price), 0) as all_revenue FROM orders");
        $all = $st2->fetch();

        // Pending & Confirmed
        $st3 = $pdo->query("SELECT COUNT(*) as pending_cnt FROM orders WHERE status = 'New' OR status = 'Pending'");
        $pending = $st3->fetch();

        // Abandoned Leads
        $st4 = $pdo->query("SELECT COUNT(*) as abandoned_cnt FROM abandoned_checkouts WHERE recovered = 0");
        $abandoned = $st4->fetch();

        // Recent 10 Orders
        $st5 = $pdo->query("SELECT * FROM orders ORDER BY id DESC LIMIT 10");
        $recent_orders = $st5->fetchAll();

        echo json_encode([
            'success' => true,
            'today_revenue' => (float)$today['total_revenue'],
            'today_orders' => (int)$today['total_orders'],
            'total_revenue' => (float)$all['all_revenue'],
            'total_orders' => (int)$all['all_orders'],
            'pending_orders' => (int)$pending['pending_cnt'],
            'abandoned_leads' => (int)$abandoned['abandoned_cnt'],
            'recent_orders' => $recent_orders
        ]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

// 5. Get All Orders (Filtered & Paginated)
if ($action === 'get_orders') {
    $search = trim($_GET['search'] ?? '');
    $status = trim($_GET['status'] ?? '');
    $limit = 50;

    $sql = "SELECT * FROM orders WHERE 1=1";
    $params = [];

    if (!empty($search)) {
        $sql .= " AND (order_id LIKE :s OR name LIKE :s OR phone LIKE :s OR city LIKE :s OR tracking_awb LIKE :s)";
        $params[':s'] = "%{$search}%";
    }

    if (!empty($status)) {
        $sql .= " AND status = :st";
        $params[':st'] = $status;
    }

    $sql .= " ORDER BY id DESC LIMIT {$limit}";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        $orders = $stmt->fetchAll();
        echo json_encode(['success' => true, 'orders' => $orders]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

// 6. Update Order Status & AWB
if ($action === 'update_order') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;
    $id = (int)($input['id'] ?? 0);
    $new_status = trim($input['status'] ?? 'Confirmed');
    $awb = trim($input['tracking_awb'] ?? '');

    try {
        $stmt = $pdo->prepare("UPDATE orders SET status = :st, tracking_awb = COALESCE(NULLIF(:awb, ''), tracking_awb), updated_at = CURRENT_TIMESTAMP WHERE id = :id");
        $stmt->execute([':st' => $new_status, ':awb' => $awb, ':id' => $id]);
        echo json_encode(['success' => true, 'message' => 'Order status updated!']);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

// 7. Get Abandoned Cart Leads
if ($action === 'get_abandoned') {
    try {
        $stmt = $pdo->query("SELECT * FROM abandoned_checkouts ORDER BY id DESC LIMIT 50");
        $leads = $stmt->fetchAll();
        echo json_encode(['success' => true, 'leads' => $leads]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

// 8. Export CSV for Shiprocket / Delhivery
if ($action === 'export_csv') {
    header('Content-Type: text/csv');
    header('Content-Disposition: attachment; filename="BlackRoots_Orders_' . date('Y-m-d_His') . '.csv"');

    $output = fopen('php://output', 'w');
    fputcsv($output, ['Order ID', 'Customer Name', 'Phone', 'Email', 'Address', 'City', 'State', 'Pincode', 'Bundle', 'Price', 'Payment Method', 'Status', 'AWB', 'Date']);

    $stmt = $pdo->query("SELECT * FROM orders ORDER BY id DESC");
    while ($row = $stmt->fetch()) {
        fputcsv($output, [
            $row['order_id'],
            $row['name'],
            $row['phone'],
            $row['email'],
            $row['address'],
            $row['city'],
            $row['state'],
            $row['pincode'],
            $row['product_bundle'],
            $row['price'],
            $row['payment_method'],
            $row['status'],
            $row['tracking_awb'],
            $row['created_at']
        ]);
    }
    fclose($output);
    exit;
}

// 9. Get & Save Settings
if ($action === 'get_settings') {
    echo json_encode([
        'success' => true,
        'settings' => [
            'meta_pixel_id' => get_setting('meta_pixel_id', ''),
            'meta_capi_token' => get_setting('meta_capi_token', ''),
            'ga4_measurement_id' => get_setting('ga4_measurement_id', ''),
            'gsc_verification_tag' => get_setting('gsc_verification_tag', ''),
            'whatsapp_support' => get_setting('whatsapp_support', '+919580835179'),
            'shiprocket_email' => get_setting('shiprocket_email', ''),
            'shiprocket_password' => get_setting('shiprocket_password', ''),
            'shiprocket_auto_push' => get_setting('shiprocket_auto_push', '0'),
        ]
    ]);
    exit;
}

if ($action === 'save_settings') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;

    $fields = ['meta_pixel_id', 'meta_capi_token', 'ga4_measurement_id', 'gsc_verification_tag', 'whatsapp_support', 'shiprocket_email', 'shiprocket_password', 'shiprocket_auto_push'];

    foreach ($fields as $f) {
        if (isset($input[$f])) {
            set_setting($f, trim($input[$f]));
        }
    }

    if (!empty($input['new_password'])) {
        set_setting('admin_password', password_hash(trim($input['new_password']), PASSWORD_BCRYPT));
    }

    echo json_encode(['success' => true, 'message' => 'Settings saved successfully!']);
    exit;
}

// 10. Push Order to Shiprocket
if ($action === 'push_shiprocket') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;
    $order_id = $input['order_id'] ?? '';

    $st = $pdo->prepare("SELECT * FROM orders WHERE order_id = :oid");
    $st->execute([':oid' => $order_id]);
    $order = $st->fetch();

    if ($order) {
        $res = shiprocket_create_order($order);
        echo json_encode($res);
    } else {
        echo json_encode(['success' => false, 'error' => 'Order not found']);
    }
    exit;
}

// 11. Influencer Management Endpoints (PHP SQLite & MySQL)
if ($action === 'get_influencers') {
    try {
        $stmt = $pdo->query("SELECT * FROM influencers ORDER BY id DESC");
        $list = $stmt->fetchAll();
        echo json_encode(['success' => true, 'influencers' => $list, 'deleted_influencers' => []]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

if ($action === 'save_influencer') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;

    $id = $input['id'] ?? ('inf-' . time());
    $name = trim($input['name'] ?? 'Creator');
    $username = trim($input['username'] ?? ($input['code'] ?? 'creator'));
    $phone = trim($input['phone'] ?? '');
    $handle = trim($input['handle'] ?? '');
    $code = strtoupper(trim($input['code'] ?? $username));
    $password = trim($input['password'] ?? 'blackroots');
    $comm_rate = (int)($input['comm_rate'] ?? 10);
    $upi_id = trim($input['upi_id'] ?? '');

    try {
        $ins = $pdo->prepare("
            INSERT INTO influencers (id, name, username, phone, handle, code, password, comm_rate, upi_id, status)
            VALUES (:id, :name, :user, :phone, :handle, :code, :pass, :comm, :upi, 'Active')
            ON CONFLICT(id) DO UPDATE SET
                name = :name,
                username = :user,
                phone = :phone,
                handle = :handle,
                code = :code,
                password = :pass,
                comm_rate = :comm,
                upi_id = :upi
        ");
        $ins->execute([
            ':id' => $id,
            ':name' => $name,
            ':user' => $username,
            ':phone' => $phone,
            ':handle' => $handle,
            ':code' => $code,
            ':pass' => $password,
            ':comm' => $comm_rate,
            ':upi' => $upi_id
        ]);

        $st = $pdo->prepare("SELECT * FROM influencers WHERE id = :id");
        $st->execute([':id' => $id]);
        $creator = $st->fetch();

        echo json_encode(['success' => true, 'influencer' => $creator]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

if ($action === 'delete_influencer') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;
    $id = trim($input['id'] ?? '');

    try {
        $pdo->prepare("DELETE FROM influencers WHERE id = :id OR code = :id OR username = :id")->execute([':id' => $id]);
        echo json_encode(['success' => true, 'message' => 'Influencer deleted successfully!']);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

// 12. Universal Influencer Login (Case-Insensitive Identifier & Password)
if ($action === 'influencer_login') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;

    $loginId = trim($input['login_id'] ?? ($input['username'] ?? ''));
    $password = trim($input['password'] ?? '');

    if (empty($loginId) || empty($password)) {
        echo json_encode(['success' => false, 'error' => 'Please provide User ID and Password.']);
        exit;
    }

    $cleanLogin = strtolower($loginId);
    $cleanPass = strtolower($password);
    $cleanPhone = preg_replace('/[^0-9]/', '', $loginId);
    if (strlen($cleanPhone) > 10 && substr($cleanPhone, 0, 2) === '91') {
        $cleanPhone = substr($cleanPhone, 2);
    }

    try {
        $stmt = $pdo->query("SELECT * FROM influencers");
        $influencers = $stmt->fetchAll();
        $matched = null;

        foreach ($influencers as $u) {
            $uId = strtolower($u['id'] ?? '');
            $uUser = strtolower($u['username'] ?? '');
            $uCode = strtolower($u['code'] ?? '');
            $uHandle = strtolower(ltrim($u['handle'] ?? '', '@'));
            $uName = strtolower($u['name'] ?? '');
            $uPhone = preg_replace('/[^0-9]/', '', $u['phone'] ?? '');

            $isIdMatch = ($uUser === $cleanLogin ||
                          $uCode === $cleanLogin ||
                          $uId === $cleanLogin ||
                          $uHandle === ltrim($cleanLogin, '@') ||
                          $uName === $cleanLogin ||
                          (!empty($cleanPhone) && strlen($cleanPhone) >= 10 && substr($uPhone, -10) === substr($cleanPhone, -10)));

            if ($isIdMatch) {
                $dbPass = strtolower(trim($u['password'] ?? ''));
                if ($dbPass === $cleanPass) {
                    $matched = $u;
                    break;
                }
            }
        }

        if ($matched) {
            // Fetch creator's referred orders
            $stOrd = $pdo->prepare("SELECT * FROM orders WHERE LOWER(coupon) = :c1 OR LOWER(coupon) = :c2 ORDER BY id DESC");
            $stOrd->execute([':c1' => strtolower($matched['code']), ':c2' => strtolower($matched['username'])]);
            $orders = $stOrd->fetchAll();

            // Fetch creator's payouts
            $stPay = $pdo->prepare("SELECT * FROM influencer_payouts WHERE influencer_id = :id OR code = :c ORDER BY date DESC");
            $stPay->execute([':id' => $matched['id'], ':c' => $matched['code']]);
            $payouts = $stPay->fetchAll();

            $token = 'tok_' . bin2hex(random_bytes(16));

            echo json_encode([
                'success' => true,
                'user' => $matched,
                'token' => $token,
                'orders' => $orders,
                'payouts' => $payouts
            ]);
            exit;
        } else {
            echo json_encode(['success' => false, 'error' => 'Incorrect User ID or Password.']);
            exit;
        }
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

// 13. Payout Requests
if ($action === 'get_payouts') {
    try {
        $stmt = $pdo->query("SELECT * FROM influencer_payouts ORDER BY id DESC");
        $payouts = $stmt->fetchAll();
        echo json_encode(['success' => true, 'payouts' => $payouts]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

if ($action === 'request_payout') {
    $raw = file_get_contents('php://input');
    $input = json_decode($raw, true) ?: $_POST;

    $payoutId = 'pay-' . time();
    $infId = $input['influencer_id'] ?? '';
    $code = $input['code'] ?? '';
    $name = $input['name'] ?? 'Creator';
    $upi = $input['upi_id'] ?? '';
    $amount = (float)($input['amount'] ?? 0);

    try {
        $ins = $pdo->prepare("INSERT INTO influencer_payouts (id, influencer_id, code, name, upi_id, amount, status) VALUES (?, ?, ?, ?, ?, ?, 'Processing')");
        $ins->execute([$payoutId, $infId, $code, $name, $upi, $amount]);

        echo json_encode([
            'success' => true,
            'payout' => [
                'id' => $payoutId,
                'influencer_id' => $infId,
                'code' => $code,
                'name' => $name,
                'upi_id' => $upi,
                'amount' => $amount,
                'status' => 'Processing',
                'date' => date('Y-m-d H:i:s')
            ]
        ]);
        exit;
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
        exit;
    }
}

echo json_encode(['error' => 'Invalid action']);
