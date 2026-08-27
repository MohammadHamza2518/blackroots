import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

html_files = [
    "index.html",
    "product.html",
    "ingredients.html",
    "how-to-use.html",
    "reviews.html",
    "ai-consultant.html",
    "track-order.html",
    "contact.html"
]

print("================================================================================")
print("            AUDITING ALL ORDER / BUY NOW BUTTONS ACROSS WEBSITE")
print("================================================================================")

for hf in html_files:
    fpath = os.path.join(root_dir, hf)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"\n--- [{hf}] ---")
    
    # Find all <button> and <a> tags
    tags = re.findall(r'<(button|a)\s+([^>]*?)>(.*?)<\/\1>', content, re.DOTALL | re.IGNORECASE)
    
    order_elements = []
    for tag_name, attrs, inner_text in tags:
        clean_text = re.sub(r'<[^>]+>', '', inner_text).strip()
        
        is_order = False
        if any(w in clean_text.lower() for w in ['buy', 'order', 'cart', 'checkout', 'claim']) or 'js-trigger-order' in attrs:
            is_order = True
        
        if is_order:
            href_m = re.search(r'href=["\']([^"\']+)["\']', attrs)
            href = href_m.group(1) if href_m else ''
            onclick_m = re.search(r'onclick=["\']([^"\']+)["\']', attrs)
            onclick = onclick_m.group(1) if onclick_m else ''
            class_m = re.search(r'class=["\']([^"\']+)["\']', attrs)
            classes = class_m.group(1) if class_m else ''

            order_elements.append({
                'tag': tag_name,
                'text': clean_text[:45],
                'href': href,
                'onclick': onclick,
                'classes': classes
            })

    print(f"Total Order/Buy elements found: {len(order_elements)}")
    for i, oe in enumerate(order_elements):
        print(f"  {i+1}. <{oe['tag']}> Text: '{oe['text']}' | href: '{oe['href']}' | onclick: '{oe['onclick']}'")

