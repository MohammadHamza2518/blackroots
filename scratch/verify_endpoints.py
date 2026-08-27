import urllib.request

base_url = "https://handbook-revolutionary-prayers-pockets.trycloudflare.com"

endpoints = [
    "/index.html",
    "/product.html",
    "/ingredients.html",
    "/how-to-use.html",
    "/reviews.html",
    "/ai-consultant.html",
    "/track-order.html",
    "/contact.html",
    "/influencer.html",
    "/admin-influencer.html",
    "/privacy-policy.html",
    "/terms.html",
    "/refund-policy.html",
    "/shipping-policy.html"
]

print("=== VERIFYING LIVE CLOUDFLARE ENDPOINTS ===")
for ep in endpoints:
    url = base_url + ep
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[{resp.status}] {ep}")
    except Exception as e:
        print(f"[FAIL] {ep}: {e}")
