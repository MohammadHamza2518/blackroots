import urllib.request
import re

for page in ["product.html", "index.html"]:
    url = f"http://localhost:8000/{page}"
    req = urllib.request.urlopen(url)
    headers = dict(req.headers)
    html = req.read().decode('utf-8')
    
    print(f"=== {page} ===")
    print("Status:", req.status)
    print("Cache-Control:", headers.get('Cache-Control'))
    
    # Check announcement bar tag
    match = re.search(r'(<div class="announcement-bar-solid[^>]*>)', html)
    if match:
        print("Announcement Tag:", match.group(1))
    else:
        print("ERROR: Announcement tag not found!")

    # Check for any remaining gradient classes on announcement bar
    if 'from-[#123824]' in html:
        print("WARNING: from-[#123824] still found in HTML!")
    else:
        print("PASS: No gradient found in announcement bar HTML!")
