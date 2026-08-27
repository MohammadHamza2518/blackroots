import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\influencer.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\influencer.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\influencer.html"
]

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove header admin link
        target_header_link = """        <a href="./admin-influencer.html" class="hidden sm:inline-flex text-xs font-bold text-gray-400 hover:text-amber-300 border border-white/10 hover:border-amber-400/50 px-3.5 py-1.5 rounded-full transition-all no-underline">
          👑 Store Admin Panel
        </a>"""
        content = content.replace(target_header_link, "")

        # Flexible replace for any variant
        if "admin-influencer.html" in content:
            # Find and remove header link block
            idx = content.find('href="./admin-influencer.html"')
            if idx != -1:
                link_start = content.rfind('<a', 0, idx)
                link_end = content.find('</a>', idx)
                if link_start != -1 and link_end != -1:
                    content = content[:link_start] + content[link_end+4:]

        # Remove footer admin link
        content = content.replace('<a href="./admin-influencer.html" class="hover:underline">Store Admin Panel</a>', '')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REMOVED ADMIN LINK FROM INFLUENCER PORTAL IN: {fpath}")

