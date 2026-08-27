import urllib.request

endpoints = [
    "http://localhost:3000/index.html",
    "http://localhost:3000/product.html",
    "http://localhost:3000/reviews.html",
    "http://localhost:3000/cart.html",
    "http://localhost:3000/checkout.html",
    "http://localhost:3000/faq.html",
    "http://localhost:3000/contact.html",
    "http://localhost:3000/privacy-policy.html",
    "http://localhost:3000/terms.html",
    "http://localhost:3000/refund-policy.html",
    "http://localhost:3000/shipping-policy.html"
]

print("=== DEEP SCAN 4: LOCALHTTP SERVER ENDPOINT AUDIT (PORT 3000) ===")

all_pass = True
for url in endpoints:
    try:
        req = urllib.request.urlopen(url)
        status = req.getcode()
        size = len(req.read())
        print(f"  [HTTP {status} OK] -> {url} ({size} bytes)")
    except Exception as e:
        print(f"  [FAIL] -> {url}: {e}")
        all_pass = False

if all_pass:
    print("SUCCESS: ALL 11 WEBSITE ENDPOINTS RETURN 200 OK WITH ZERO ERRORS!")

