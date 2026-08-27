import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

pages = [
    "index.html",
    "product.html",
    "ingredients.html",
    "how-to-use.html",
    "reviews.html",
    "ai-consultant.html",
    "track-order.html",
    "contact.html",
    "demo_lab/index.html",
    "demo_lab/product.html",
    "demo_lab/ingredients.html",
    "demo_lab/how-to-use.html",
    "demo_lab/reviews.html",
    "demo_lab/ai-consultant.html",
    "demo_lab/track-order.html",
    "demo_lab/contact.html",
    "preview/index.html",
    "preview/product.html",
    "preview/ingredients.html",
    "preview/how-to-use.html",
    "preview/reviews.html",
    "preview/ai-consultant.html",
    "preview/track-order.html",
    "preview/contact.html"
]

for p in pages:
    fp = os.path.join(root_dir, p)
    if not os.path.exists(fp):
        continue

    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    # Find buttons that contain ORDER NOW or BUY NOW but have no onclick
    # Example: <button class="...js-trigger-order...">
    def replace_button(m):
        full_tag = m.group(0)
        tag_attrs = m.group(1)
        inner = m.group(2)
        
        # If it's an order button
        if any(w in inner.lower() for w in ['order now', 'buy now', 'claim offer', 'order today', 'buy ₹']):
            if 'onclick=' not in tag_attrs:
                return f'<button onclick="openQuickOrderModal();"{tag_attrs}>{inner}</button>'
        return full_tag

    new_content = re.sub(r'<button([^>]*?)>(.*?)<\/button>', replace_button, new_content, flags=re.DOTALL | re.IGNORECASE)

    # Find <a> tags with js-trigger-order that have no onclick
    def replace_anchor(m):
        full_tag = m.group(0)
        tag_attrs = m.group(1)
        inner = m.group(2)
        
        if 'js-trigger-order' in tag_attrs and 'onclick=' not in tag_attrs:
            return f'<a onclick="openQuickOrderModal();"{tag_attrs}>{inner}</a>'
        return full_tag

    new_content = re.sub(r'<a([^>]*?)>(.*?)<\/a>', replace_anchor, new_content, flags=re.DOTALL | re.IGNORECASE)

    if new_content != content:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Explicitly bound openQuickOrderModal() to all order buttons in:", p)

