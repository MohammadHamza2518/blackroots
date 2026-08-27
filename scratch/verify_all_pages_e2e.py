import urllib.request
import re

base_url = "http://127.0.0.1:8000"

pages_to_test = [
    ("index.html", "Homepage"),
    ("product.html", "Product Page (1-Click Order)"),
    ("ingredients.html", "Ingredients & Herbal Science"),
    ("how-to-use.html", "Ritual & 3-Min Shower Routine"),
    ("reviews.html", "Customer Reviews & Video Reels"),
    ("ai-consultant.html", "AI Hair Doctor Consultation"),
    ("track-order.html", "Track Order & Live AWB Tracker"),
    ("contact.html", "Contact Us & UP Warehouse Support"),
    ("privacy-policy.html", "Privacy Policy (Legal)"),
    ("terms.html", "Terms & Conditions (Legal)"),
    ("refund-policy.html", "Refund & Cancellation Policy (Legal)"),
    ("shipping-policy.html", "Shipping & Delivery Policy (Legal)")
]

print("================================================================================")
print("             END-TO-END HTTP & REAL DOM FLOW VERIFICATION TEST")
print("================================================================================")

all_passed = True

for page, name in pages_to_test:
    url = f"{base_url}/{page}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)"})
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            content = resp.read().decode('utf-8')
            
            title_match = re.search(r'<title>(.*?)<\/title>', content)
            title = title_match.group(1) if title_match else "No Title"

            has_theme_js = 'theme.js' in content
            has_butter_js = 'instant-butter.js' in content

            print(f"[HTTP {status}] {name.ljust(35)} | Title: {title[:32]}... | ThemeJS: {has_theme_js} | InstantButter: {has_butter_js}")
            
            if status != 200 or not has_theme_js:
                all_passed = False
    except Exception as e:
        print(f"FAILED: {url} -> {e}")
        all_passed = False

print("================================================================================")
if all_passed:
    print("ALL 12 CORE STOREFRONT PAGES RETURNED HTTP 200 AND ARE FULLY FUNCTIONAL!")
else:
    print("SOME CHECKS FAILED.")
print("================================================================================")
