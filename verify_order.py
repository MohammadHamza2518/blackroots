import re

content = open('index.html', 'r', encoding='utf-8').read()

cards = content.split('class="js-reel-card')[1:]
for idx, card in enumerate(cards, 1):
    link_m = re.search(r'href="(https://www\.instagram\.com/reel/[^"]+)"', card)
    video_m = re.search(r'<source src="([^"]+)"', card)
    title_m = re.search(r'<h4[^>]*>([^<]+)</h4>', card)
    
    link = link_m.group(1) if link_m else 'N/A'
    video = video_m.group(1) if video_m else 'N/A'
    title = title_m.group(1) if title_m else 'N/A'
    
    print(f"POSITION {idx}:")
    print(f"  - Video File : {video}")
    print(f"  - Title      : {title}")
    print(f"  - IG Link    : {link}\n")
