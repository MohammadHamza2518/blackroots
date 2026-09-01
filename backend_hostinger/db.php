<?php
// BlackRoots D2C E-Commerce Database Connection Engine
// Automatic Dual Mode: SQLite (0-Config Out of the Box) / MySQL (Enterprise)

error_reporting(0);
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$config_file = __DIR__ . '/config.php';
$use_mysql = false;
$db_host = 'localhost';
$db_user = '';
$db_pass = '';
$db_name = '';

if (file_exists($config_file)) {
    include_once $config_file;
    if (!empty($db_name) && !empty($db_user)) {
        $use_mysql = true;
    }
}

try {
    if ($use_mysql) {
        $pdo = new PDO("mysql:host={$db_host};dbname={$db_name};charset=utf8mb4", $db_user, $db_pass, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]);
    } else {
        // SQLite: Zero configuration instant plug & play on Hostinger
        $db_path = __DIR__ . '/blackroots.sqlite';
        $pdo = new PDO("sqlite:" . $db_path);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    }

    // Initialize Tables automatically
    $pdo->exec("
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT UNIQUE,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            pincode TEXT NOT NULL,
            product_bundle TEXT NOT NULL,
            price REAL NOT NULL,
            payment_method TEXT DEFAULT 'COD',
            status TEXT DEFAULT 'New',
            tracking_awb TEXT,
            courier TEXT DEFAULT 'Delhivery Express Air',
            shiprocket_order_id TEXT,
            shiprocket_shipment_id TEXT,
            meta_pixel_tracked INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS abandoned_checkouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT NOT NULL,
            product_bundle TEXT,
            price REAL,
            recovered INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS settings (
            key_name TEXT PRIMARY KEY,
            key_val TEXT
        );

        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            page_url TEXT,
            user_agent TEXT,
            city TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS influencers (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            phone TEXT,
            handle TEXT,
            code TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            comm_rate INTEGER DEFAULT 10,
            clicks INTEGER DEFAULT 0,
            total_orders INTEGER DEFAULT 0,
            total_sales REAL DEFAULT 0,
            total_earned REAL DEFAULT 0,
            unpaid_balance REAL DEFAULT 0,
            upi_id TEXT,
            status TEXT DEFAULT 'Active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS influencer_payouts (
            id TEXT PRIMARY KEY,
            influencer_id TEXT,
            code TEXT,
            name TEXT,
            upi_id TEXT,
            amount REAL,
            status TEXT DEFAULT 'Processing',
            utr TEXT,
            date DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    ");

    // Seed default influencers if empty
    $stInf = $pdo->query("SELECT COUNT(*) as cnt FROM influencers");
    $rInf = $stInf->fetch();
    if ($rInf && $rInf['cnt'] == 0) {
        $insInf = $pdo->prepare("INSERT OR IGNORE INTO influencers (id, name, username, phone, handle, code, password, comm_rate, clicks, total_orders, total_sales, total_earned, unpaid_balance, upi_id, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        $insInf->execute(['inf-104', 'Airam', 'airam', '9876543210', '@airam_beauty', 'AIRAM10', 'airam', 10, 0, 0, 0, 0, 0, '', 'Active']);
        $insInf->execute(['inf-105', 'Ilma', 'ilma', '9876543211', '@ilma_care', 'ILMA10', 'ilma', 10, 0, 0, 0, 0, 0, '', 'Active']);
    }

    // Seed initial default settings if empty
    $stmt = $pdo->query("SELECT COUNT(*) as cnt FROM settings");
    $res = $stmt->fetch();
    if ($res && $res['cnt'] == 0) {
        $defaults = [
            'admin_password' => password_hash('blackroots2026', PASSWORD_BCRYPT),
            'meta_pixel_id' => '',
            'meta_capi_token' => '',
            'ga4_measurement_id' => '',
            'gsc_verification_tag' => '',
            'whatsapp_support' => '+919580835179',
            'razorpay_key_id' => 'rzp_live_TV9VNPhiYYbB07',
            'razorpay_key_secret' => 'ianPeeSx3gMvq2OZk8TUW0sz',
            'razorpay_enabled' => '1',
            'shiprocket_email' => 'api@blackroots.in',
            'shiprocket_password' => 'S1bSO*3&H1fHiBC@!b7lqEsTI#Nwm8mt',
            'shiprocket_pickup_location' => 'Home',
            'shiprocket_auto_push' => '1',
            'store_currency' => 'INR',
        ];
        $ins = $pdo->prepare("INSERT INTO settings (key_name, key_val) VALUES (:k, :v)");
        foreach ($defaults as $k => $v) {
            $ins->execute([':k' => $k, ':v' => $v]);
        }
    }

} catch (Exception $e) {
    header('Content-Type: application/json');
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
}

function get_setting($key, $default = '') {
    global $pdo;
    try {
        $stmt = $pdo->prepare("SELECT key_val FROM settings WHERE key_name = :k");
        $stmt->execute([':k' => $key]);
        $row = $stmt->fetch();
        return $row ? $row['key_val'] : $default;
    } catch (Exception $e) {
        return $default;
    }
}

function set_setting($key, $val) {
    global $pdo;
    try {
        $stmt = $pdo->prepare("INSERT INTO settings (key_name, key_val) VALUES (:k, :v) ON CONFLICT(key_name) DO UPDATE SET key_val = :v");
        $stmt->execute([':k' => $key, ':v' => $val]);
        return true;
    } catch (Exception $e) {
        try {
            $stmt = $pdo->prepare("REPLACE INTO settings (key_name, key_val) VALUES (:k, :v)");
            $stmt->execute([':k' => $key, ':v' => $val]);
            return true;
        } catch(Exception $ex) {
            return false;
        }
    }
}
