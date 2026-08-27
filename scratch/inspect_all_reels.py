import cv2
import os

assets_dir = r"c:\Users\moham\Downloads\blackroots website\assets"
reels = ["reel-6.mp4", "reel-3.mp4", "reel-2.mp4", "reel-4.mp4", "reel-1.mp4"]

for r in reels:
    rpath = os.path.join(assets_dir, r)
    if os.path.exists(rpath):
        cap = cv2.VideoCapture(rpath)
        fps = cap.get(cv2.CAP_PROP_FPS)
        fc = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        dur = fc / fps if fps > 0 else 0
        print(f"{r}: {w}x{h}, {dur:.1f}s, frames: {fc}")
        cap.release()
    else:
        print(f"{r}: NOT FOUND")
