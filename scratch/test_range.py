import urllib.request

url = "http://127.0.0.1:8000/assets/reel-6.mp4"
req = urllib.request.Request(url, headers={"Range": "bytes=0-1023"})

try:
    with urllib.request.urlopen(req) as resp:
        print("Status Code:", resp.status)
        print("Content-Range:", resp.headers.get("Content-Range"))
        print("Content-Length:", resp.headers.get("Content-Length"))
        print("Accept-Ranges:", resp.headers.get("Accept-Ranges"))
        data = resp.read()
        print("Received bytes:", len(data))
except Exception as e:
    print("Error:", e)
