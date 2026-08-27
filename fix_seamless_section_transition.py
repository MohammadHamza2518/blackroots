import os

target_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

old_sec_tag = '<section class="py-20 bg-gradient-to-b from-[#0a0b0e] via-[#151922] to-[#0a0b0e] border-b border-[#d4af37]/20 relative overflow-hidden">'
new_sec_tag = '<section class="py-10 sm:py-16 bg-[#0a0b0e] border-b border-[#d4af37]/20 relative overflow-hidden">'

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_sec_tag in content:
            content = content.replace(old_sec_tag, new_sec_tag)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"MADE SECTION TRANSITION 100% SEAMLESS IN: {fpath}")
        else:
            # try finding by comment
            s_idx = content.find('<!-- Before / After Authentic Photo Comparison Slider Section -->')
            if s_idx != -1:
                sec_idx = content.find('<section', s_idx)
                sec_close = content.find('>', sec_idx)
                if sec_idx != -1 and sec_close != -1:
                    content = content[:sec_idx] + new_sec_tag + content[sec_close+1:]
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"SEAMLESS SECTION FIX APPLIED TO: {fpath}")
