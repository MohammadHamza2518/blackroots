import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\ai-consultant.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\ai-consultant.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\ai-consultant.html"
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<script src="./assets/theme.js' not in content[-500:]:
        content = content.replace('</body>', '  <script src="./assets/theme.js?v=1786809224"></script>\n</body>')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Injected theme.js script at bottom of", fpath)
