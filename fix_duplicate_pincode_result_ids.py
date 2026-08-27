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

        # Remove duplicate HomePincodeResult card at bottom
        s_idx = content.find('<!-- Pincode Estimator Result Card -->')
        if s_idx != -1:
            e_idx = content.find('</div>', s_idx)
            if e_idx != -1:
                e_end = content.find('</div>', e_idx + 6) + 6
                if e_end != -1:
                    content = content[:s_idx] + content[e_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REMOVED DUPLICATE PINCODE RESULT ID FROM: {fpath}")
