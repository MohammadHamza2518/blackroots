import shutil

src = r"c:\Users\moham\Downloads\blackroots website\mobile-preview.html"
for target in [r"c:\Users\moham\Downloads\blackroots website\demo_lab\mobile-preview.html", r"c:\Users\moham\Downloads\blackroots website\preview\mobile-preview.html"]:
    shutil.copy2(src, target)
    print("Synced mobile-preview.html to", target)
