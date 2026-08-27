import os

target_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

print("Removing duplicate Reels section from all HTML files...")

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        d_idx = content.find('<!-- REELS STUDIO 2.0: ROYAL THEATER SHOWCASE -->')
        if d_idx == -1:
            d_idx = content.find('🎬 BlackRoots Reels Studio &bull; Real Results')
            if d_idx != -1:
                d_idx = content.rfind('<section', 0, d_idx)

        if d_idx != -1:
            end_d = content.find('</section>', d_idx)
            if end_d != -1:
                content = content[:d_idx] + content[end_d+10:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"REMOVED DUPLICATE REELS SECTION FROM: {fpath}")
