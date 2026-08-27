import shutil, os

src_path = r"C:\Users\moham\.gemini\antigravity\brain\0219a2fe-4690-4482-9583-96e83a21bc69\.user_uploaded\media_1786435703831.jpg"

dest1 = "assets/reviews/farhan-bottle-photo.jpg"
dest2 = "demo_lab/assets/reviews/farhan-bottle-photo.jpg"
dest3 = "preview/assets/reviews/farhan-bottle-photo.jpg"

shutil.copy(src_path, dest1)
shutil.copy(src_path, dest2)
shutil.copy(src_path, dest3)

print("COPIED FARHAN BOTTLE PHOTO SUCCESSFULLY!")
