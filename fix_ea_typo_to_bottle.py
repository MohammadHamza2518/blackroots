import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_text = '&#8377;799 (&#8377;399/ea) &bull; Save &#8377;200 Extra'
new_text = '&#8377;799 (&#8377;399/bottle) &bull; Save &#8377;200 Extra'

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_text in content:
            content = content.replace(old_text, new_text)
        elif '399/ea' in content:
            content = content.replace('399/ea', '399/bottle')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED /ea TYPO TO /bottle IN: {fpath}")

