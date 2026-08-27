import glob
import time

timestamp = int(time.time())

# Update script tags in all html files
for f in glob.glob('**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Cache bust theme.js
    content = content.replace('src="./assets/theme.js"', f'src="./assets/theme.js?v={timestamp}"')
    content = content.replace('src="assets/theme.js"', f'src="assets/theme.js?v={timestamp}"')
    
    # If it already had a ?v= parameter
    import re
    content = re.sub(r'src="\./assets/theme\.js\?v=\d+"', f'src="./assets/theme.js?v={timestamp}"', content)
    content = re.sub(r'src="assets/theme\.js\?v=\d+"', f'src="assets/theme.js?v={timestamp}"', content)
    
    # If inside mobile-preview.html, update iframe src
    if 'mobile-preview.html' in f:
        content = re.sub(r'src="index\.html(?:\?v=\d+)?"', f'src="index.html?v={timestamp}"', content)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Applied timestamp v={timestamp} to {f}")
