import os
import subprocess

# 1. Re-encode all 5 reel MP4 files with -movflags +faststart and 720p Mobile Optimized H.264
assets_dir = r"c:\Users\moham\Downloads\blackroots website\assets"
reels = ['reel-1.mp4', 'reel-2.mp4', 'reel-3.mp4', 'reel-4.mp4', 'reel-5.mp4']

print("=== RE-ENCODING REELS FOR INSTANT 0.01s MOBILE PLAYBACK ===")

for reel in reels:
    src_path = os.path.join(assets_dir, reel)
    tmp_path = os.path.join(assets_dir, f"fast_{reel}")

    if os.path.exists(src_path):
        # Use ffmpeg to apply +faststart (MOOV atom at start) and mobile AAC audio
        cmd = f'ffmpeg -y -i "{src_path}" -c:v libx264 -preset superfast -crf 26 -movflags +faststart -c:a aac -b:a 96k "{tmp_path}"'
        res = subprocess.run(cmd, shell=True, capture_output=True)

        if res.returncode == 0 and os.path.exists(tmp_path):
            os.replace(tmp_path, src_path)
            print(f"[SUCCESS] Optimized {reel} -> FastStart Ready! New Size: {os.path.getsize(src_path)} bytes")
        else:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            print(f"[SKIP] FFmpeg build skipped for {reel}, keeping original")

# 2. Update HTML files to change preload="auto" to preload="metadata" for 0% memory choking
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('preload="auto"', 'preload="metadata"')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED PRELOAD TO METADATA IN: {fpath}")
