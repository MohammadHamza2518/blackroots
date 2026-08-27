import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\product.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

footer_links_snippet = """<div class="flex items-center justify-center gap-4 text-xs font-semibold text-amber-300 my-3 flex-wrap">
  <a href="./influencer.html" class="hover:underline flex items-center gap-1"><span>💎</span> Influencer Creator Program</a>
  <span>&bull;</span>
  <a href="./admin-influencer.html" class="hover:underline flex items-center gap-1"><span>👑</span> Store Admin Panel</a>
</div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if footer_links_snippet in content:
            content = content.replace(f"{footer_links_snippet}\n", "")
            content = content.replace(footer_links_snippet, "")
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"REMOVED PUBLIC FOOTER LINKS FROM: {fpath}")

