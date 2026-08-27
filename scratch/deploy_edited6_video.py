import os
import shutil
import cv2

root_dir = r"c:\Users\moham\Downloads\blackroots website"
src_video = os.path.join(root_dir, "edited 6.mp4")
dest_video = os.path.join(root_dir, "assets", "reel-6.mp4")
dest_thumb = os.path.join(root_dir, "assets", "reel-thumb-6.jpg")

# 1. Copy video to assets/reel-6.mp4
print(f"Copying {src_video} -> {dest_video}")
shutil.copy2(src_video, dest_video)
print(f"Video copied successfully: {os.path.getsize(dest_video)} bytes")

# 2. Extract best thumbnail frame (at approx 20-30% or when hair/wash is clear)
cap = cv2.VideoCapture(dest_video)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_count * 0.25))
ret, frame = cap.read()
if ret:
    cv2.imwrite(dest_thumb, frame)
    print(f"Thumbnail extracted and saved to: {dest_thumb}")
cap.release()

# 3. Update product.html files
product_files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

for pf in product_files:
    if os.path.exists(pf):
        with open(pf, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update Slide 6 video source
        content = content.replace('src="./assets/reel-2.mp4"', 'src="./assets/reel-6.mp4"')
        content = content.replace('src="./assets/reel-thumb-2.jpg"', 'src="./assets/reel-thumb-6.jpg"')

        with open(pf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated product file: {pf}")

# 4. Update index.html files
index_files = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html")
]

for inf in index_files:
    if os.path.exists(inf):
        with open(inf, 'r', encoding='utf-8') as f:
            content = f.read()

        # In Card 4 (reel-5.mp4): update to reel-6.mp4 and update title to "Grey To Naturally Black Hair"
        content = content.replace('<source src="./assets/reel-5.mp4" type="video/mp4">', '<source src="./assets/reel-6.mp4" type="video/mp4">')
        content = content.replace('Stop Premature Greying</h4>', 'Grey To Naturally Black Hair</h4>')

        with open(inf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated index file: {inf}")

print("ALL UPDATES COMPLETED SUCCESSFULLY!")
