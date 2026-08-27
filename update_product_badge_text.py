import os

product_files = [
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html"
]

old_text = "🌿 250ml Official Edition"
new_text = "🌿 250ML Bottle"

for fpath in product_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace("🌿 250ml Official Edition", "🌿 250ML Bottle")
        content = content.replace("250ml Official Edition", "250ML Bottle")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED PRODUCT BADGE IN: {fpath}")
