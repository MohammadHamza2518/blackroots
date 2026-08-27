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

        # Update initial viewport image src to bathroom counter photo
        content = content.replace(
            'id="ProductMainImage" src="./assets/blackroots-bottle-single.png"',
            'id="ProductMainImage" src="./assets/blackroots-bathroom-counter.jpg"'
        )
        content = content.replace(
            'class="w-full h-full object-contain p-4 transition-all duration-300 group-hover:scale-105"',
            'class="w-full h-full object-cover transition-all duration-300 group-hover:scale-105"'
        )

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"SET 1ST IMAGE TO BATHROOM COUNTER PHOTO IN: {fpath}")

