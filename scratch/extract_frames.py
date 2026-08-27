import cv2
import os

cap = cv2.VideoCapture(r"c:\Users\moham\Downloads\blackroots website\edited 6.mp4")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Grab 3 frames at different points
for i, pos in enumerate([0.1, 0.4, 0.7]):
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_count * pos))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"scratch/frame_{i+1}.jpg", frame)
print("Extracted preview frames")
cap.release()
