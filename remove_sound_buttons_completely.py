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

        # Remove all sound button markup
        lines = content.splitlines()
        new_lines = []
        skip_next = False

        for line in lines:
            if 'js-sound-toggle' in line or 'id="ReelSoundToggle"' in line:
                continue
            if '<span>🔇</span>' in line or '<span>🔊</span>' in line:
                continue
            new_lines.append(line)

        new_content = '\n'.join(new_lines)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"REMOVED SOUND BUTTONS FROM: {fpath}")
