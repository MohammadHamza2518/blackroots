import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"

pages = [
    "index.html",
    "product.html",
    "ingredients.html",
    "how-to-use.html",
    "reviews.html",
    "ai-consultant.html",
    "track-order.html",
    "contact.html"
]

for p in pages:
    fp = os.path.join(root_dir, p)
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
        has_modal = 'id="QuickOrderModal"' in content
        print(f"Page: {p.ljust(20)} | Has QuickOrderModal: {has_modal}")

