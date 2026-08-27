import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace("src=\"./assets/reel-1.mp4\"", "src=\"./assets/reel-2.mp4\"")
        content = content.replace("changeMainProductImage(this, './assets/reel-1.mp4', true)", "changeMainProductImage(this, './assets/reel-2.mp4', true)")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SWITCHED GALLERY REEL VIDEO TO REEL-2 IN: {fpath}")

