import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\ingredients.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\ingredients.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\ingredients.html"
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Fix broken symbols
    new_content = new_content.replace('œ•', '✕')
    new_content = new_content.replace('œ“', '✓')
    new_content = new_content.replace('&#8377;yurveda', 'Ayurveda')
    new_content = new_content.replace('&#8377;yurvedic', 'Ayurvedic')
    
    # Ensure script tag is present
    if 'src="./assets/theme.js"' not in new_content and 'src="assets/theme.js"' not in new_content:
        new_content = new_content.replace('</body>', '  <script src="./assets/theme.js"></script>\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {fpath}")
