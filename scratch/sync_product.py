import shutil

src = r"c:\Users\moham\Downloads\blackroots website\product.html"
for target in [r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html", r"c:\Users\moham\Downloads\blackroots website\preview\product.html"]:
    shutil.copy2(src, target)
    print("Synced product.html to", target)
