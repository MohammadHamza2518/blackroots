import os, shutil

uploaded_src = r"C:\Users\moham\.gemini\antigravity\brain\b4fb9873-4d37-42bd-ae35-964df1e66b68\.user_uploaded\media_1786626043016.png"

dest_main = r"c:\Users\moham\Downloads\blackroots website\assets\blackroots-bottle-single.png"
dest_demo = r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\blackroots-bottle-single.png"
dest_prev = r"c:\Users\moham\Downloads\blackroots website\preview\assets\blackroots-bottle-single.png"

shutil.copy2(uploaded_src, dest_main)
if os.path.exists(os.path.dirname(dest_demo)):
    shutil.copy2(uploaded_src, dest_demo)
if os.path.exists(os.path.dirname(dest_prev)):
    shutil.copy2(uploaded_src, dest_prev)

print("COPIED NEW SINGLE BOTTLE PHOTO TO ASSETS!")

files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\contact.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update video reel overlay thumbnail & order modals
        content = content.replace('./assets/blackroots-bottles-trio.jpg', './assets/blackroots-bottle-single.png')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED REEL OVERLAY THUMBNAIL IN: {fpath}")

