import os
import sys

video_path = r"c:\Users\moham\Downloads\blackroots website\edited 6.mp4"
print(f"Checking video file: {video_path}")
print(f"Exists: {os.path.exists(video_path)}, Size: {os.path.getsize(video_path)} bytes")

try:
    import cv2
    print("OpenCV is available")
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = frame_count / fps if fps > 0 else 0
    print(f"Video resolution: {width}x{height}, FPS: {fps}, Frames: {frame_count}, Duration: {duration:.2f}s")
    
    # Grab frame at 2 seconds or 20%
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_count * 0.2))
    ret, frame = cap.read()
    if ret:
        thumb_path = r"c:\Users\moham\Downloads\blackroots website\assets\reel-thumb-6.jpg"
        cv2.imwrite(thumb_path, frame)
        print(f"Saved thumbnail to {thumb_path}")
    cap.release()
except ImportError:
    print("OpenCV not installed, checking alternatives...")
