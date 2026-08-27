import shutil

src1 = r"C:\Users\moham\.gemini\antigravity\brain\0219a2fe-4690-4482-9583-96e83a21bc69\.user_uploaded\media_1786435811187.jpg"
src2 = r"C:\Users\moham\.gemini\antigravity\brain\0219a2fe-4690-4482-9583-96e83a21bc69\.user_uploaded\media_1786435811200.jpg"

dirs = ["assets/reviews", "demo_lab/assets/reviews", "preview/assets/reviews"]

for d in dirs:
    shutil.copy(src1, f"{d}/girl-holding-bottle.jpg")
    shutil.copy(src2, f"{d}/table-bottle-hindu.jpg")

print("COPIED 2 NEW REVIEW PHOTOS SUCCESSFULLY!")
