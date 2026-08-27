import cv2

cap = cv2.VideoCapture(r"c:\Users\moham\Downloads\blackroots website\assets\reel-1.mp4")
fc = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for i, pos in enumerate([0.1, 0.5, 0.8]):
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(fc * pos))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"scratch/reel1_frame_{i+1}.jpg", frame)
print("Reel 1 frames extracted")
cap.release()
