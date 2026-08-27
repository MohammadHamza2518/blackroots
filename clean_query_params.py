import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\product.html"
]

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('.mp4?v=5', '.mp4')
        content = content.replace('.js?v=7', '.js')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEANED QUERY PARAMS IN: {fpath}")

