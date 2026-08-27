import shutil

src = r"c:\Users\moham\Downloads\blackroots website\assets\theme.css"
targets = [
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.css",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.css"
]

for t in targets:
    shutil.copy2(src, t)
    print("Synced theme.css to", t)
