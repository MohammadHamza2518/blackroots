import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('</span>\n              </button>', '</span>')
        content = content.replace('</span>\r\n              </button>', '</span>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEANED CLOSING BUTTON TAG IN: {fpath}")
