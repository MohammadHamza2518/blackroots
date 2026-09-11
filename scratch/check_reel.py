import urllib.request
import re
import json

url = "https://www.instagram.com/reel/DdHmN4_SeUV/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        
    title = re.search(r'<title>(.*?)</title>', html)
    og_title = re.search(r'<meta property="og:title" content="(.*?)"', html)
    og_desc = re.search(r'<meta property="og:description" content="(.*?)"', html)
    og_video = re.search(r'<meta property="og:video" content="(.*?)"', html) or re.search(r'<meta property="og:video:secure_url" content="(.*?)"', html)
    
    print("Title:", title.group(1) if title else "N/A")
    print("OG Title:", og_title.group(1) if og_title else "N/A")
    print("OG Desc:", og_desc.group(1) if og_desc else "N/A")
    print("OG Video URL:", og_video.group(1) if og_video else "N/A")
except Exception as e:
    print("Error:", e)
