import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html"),
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html")
]

# Clean, elegant replacement for Option 2 subtext
old_pattern = r'<span class="text-xs text-emerald-400 font-semibold">&#8377;799 \(&#8377;399\/bottle\) &bull; Save &#8377;200 Extra<\/span>'
clean_replacement = '<span class="text-xs text-gray-300">&#8377;799 &bull; <span class="text-amber-300 font-medium">&#8377;399/bottle</span> &bull; <span class="text-emerald-400 font-bold">Save &#8377;200</span></span>'

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(old_pattern, clean_replacement, content)
    
    # In case there's another variant with unicode symbols
    new_content = re.sub(
        r'<span class="text-xs text-emerald-400 font-semibold">₹799 \(₹399\/bottle\) • Save ₹200 Extra<\/span>',
        '<span class="text-xs text-gray-300">₹799 &bull; <span class="text-amber-300 font-medium">₹399/bottle</span> &bull; <span class="text-emerald-400 font-bold">Save ₹200</span></span>',
        new_content
    )

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Cleaned bundle option text in", fpath)

