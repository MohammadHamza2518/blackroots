import os

html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Removing MobileStickyBuyBar completely across {len(html_files)} HTML files...")

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'MobileStickyBuyBar' in content:
            start_bar = content.find('<!-- Mobile Floating Sticky Buy Bar')
            if start_bar == -1:
                start_bar = content.find('<div id="MobileStickyBuyBar"')
            
            end_bar = content.find('</div>\n', content.find('MobileStickyBuyBar'))
            if end_bar == -1:
                end_bar = content.find('</div>\r\n', content.find('MobileStickyBuyBar'))
            if end_bar == -1:
                end_bar = content.find('</div>', content.find('MobileStickyBuyBar'))

            if start_bar != -1 and end_bar != -1:
                # Find the closing tag of the bar container
                container_end = content.find('</div>', content.find('<a href="./product.html"', start_bar))
                if container_end != -1:
                    bar_end = content.find('</div>', container_end + 6)
                    if bar_end != -1:
                        content = content[:start_bar] + content[bar_end+6:]

            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"REMOVED MOBILE STICKY BUY BAR FROM: {fpath}")
    except Exception as e:
        print(f"Error removing bar from {fpath}: {e}")
