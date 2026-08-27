import os
import time

preview_file = r"c:\Users\moham\Downloads\blackroots website\mobile-preview.html"

timestamp = int(time.time())

if os.path.exists(preview_file):
    with open(preview_file, 'r', encoding='utf-8') as f:
        content = f.read()

    old_iframe = '<iframe id="SimulatedIframe" src="index.html" title="Live Mobile Website Preview" allow="autoplay; encrypted-media; fullscreen"></iframe>'
    new_iframe = f'<iframe id="SimulatedIframe" src="index.html?v={timestamp}" title="Live Mobile Website Preview" allow="autoplay; encrypted-media; fullscreen"></iframe>'

    content = content.replace(old_iframe, new_iframe)
    content = content.replace('src="index.html"', f'src="index.html?v={timestamp}"')

    with open(preview_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"ADDED CACHE BUSTER TIMESTAMP v={timestamp} TO mobile-preview.html")
