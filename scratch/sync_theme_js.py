import shutil

src = r"c:\Users\moham\Downloads\blackroots website\assets\theme.js"
targets = [
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

for t in targets:
    shutil.copy2(src, t)
    print("Synced theme.js to", t)
