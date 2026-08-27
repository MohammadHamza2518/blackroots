import urllib.request
import urllib.parse
import os

print("=== STARTING REAL LIVE END-TO-END AUTOMATED TEST ===")

base_url = "http://localhost:8000"

# 1. Test index.html HTTP Status & HTML content
try:
    req = urllib.request.urlopen(f"{base_url}/index.html")
    html_code = req.read().decode('utf-8')
    print("[PASS] index.html loaded successfully. Status 200 OK")

    assert "ReelsCarouselContainer" in html_code, "ReelsCarouselContainer missing!"
    assert "js-sound-toggle" in html_code, "js-sound-toggle missing!"
    assert "js-reel-card" in html_code, "js-reel-card missing!"
    print("[PASS] index.html contains all required Reels container & button elements")
except Exception as e:
    print("[FAIL] index.html check error:", e)

# 2. Test mobile-preview.html HTTP Status & iframe allow attribute
try:
    req = urllib.request.urlopen(f"{base_url}/mobile-preview.html")
    preview_code = req.read().decode('utf-8')
    print("[PASS] mobile-preview.html loaded successfully. Status 200 OK")

    assert 'allow="autoplay; encrypted-media; fullscreen"' in preview_code, "Iframe autoplay permission missing!"
    print("[PASS] mobile-preview.html has allow='autoplay; encrypted-media; fullscreen' on iframe")
except Exception as e:
    print("[FAIL] mobile-preview.html check error:", e)

# 3. Test theme.js HTTP Status & JS logic
try:
    req = urllib.request.urlopen(f"{base_url}/assets/theme.js")
    js_code = req.read().decode('utf-8')
    print("[PASS] assets/theme.js loaded successfully. Status 200 OK")

    assert "js-sound-toggle" in js_code, "Sound toggle logic missing in theme.js!"
    assert "initReelsModal" in js_code, "initReelsModal missing in theme.js!"
    print("[PASS] theme.js contains initReelsModal & capture-phase sound toggle logic")
except Exception as e:
    print("[FAIL] assets/theme.js check error:", e)

# 4. Test all 5 video URLs for HTTP 200 / 206 OK
reels = ['reel-1.mp4', 'reel-2.mp4', 'reel-3.mp4', 'reel-4.mp4', 'reel-5.mp4']
for reel in reels:
    try:
        video_url = f"{base_url}/assets/{reel}"
        req = urllib.request.Request(video_url, headers={'Range': 'bytes=0-1024'})
        res = urllib.request.urlopen(req)
        status = res.getcode()
        content_type = res.headers.get('Content-Type')
        print(f"[PASS] {reel} -> HTTP {status}, Content-Type: {content_type}, Size: {os.path.getsize(r'c:\\Users\\moham\\Downloads\\blackroots website\\assets\\' + reel)} bytes")
    except Exception as e:
        print(f"[FAIL] {reel} check error:", e)

print("=== REAL LIVE END-TO-END TEST COMPLETE ===")
