import shutil
import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# We need to extract all the 22 review cards and separate them into photo and no-photo
grid_open = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">'
grid_close = '      </div>\n\n      <!-- Bottom Order Callout -->'

start = c.find(grid_open)
end = c.find(grid_close)

if start != -1 and end != -1:
    grid_inner = c[start + len(grid_open):end]
    
    # Split into cards
    cards = re.findall(r'(?s)(\n\s*<div class="p-6 rounded-3xl glass-panel-luxury.*?<!-- Review end or next -->|</div>\n        </div>)', grid_inner)
    
    # Wait, the regex might fail if I don't match properly. Let's split by the card wrapper
    raw_cards = grid_inner.split('<div class="p-6 rounded-3xl glass-panel-luxury')
    
    # raw_cards[0] is just whitespace
    actual_cards = []
    for rc in raw_cards[1:]:
        actual_cards.append('<div class="p-6 rounded-3xl glass-panel-luxury' + rc)
        
    print(f"Found {len(actual_cards)} cards")
    
    photo_cards = []
    text_cards = []
    
    for card in actual_cards:
        # Check if it has a photo
        if 'alt="Review Photo"' in card or 'Customer Photo' in card or 'face-photo' in card or 'review-photo' in card or 'bottle-photo' in card:
            photo_cards.append(card)
        else:
            text_cards.append(card)
            
    print(f"Photo cards: {len(photo_cards)}")
    print(f"Text cards: {len(text_cards)}")
    
    # Rebuild the grid inner HTML with photo cards first, then text cards
    new_grid_inner = ''.join(photo_cards) + ''.join(text_cards)
    
    new_content = c[:start + len(grid_open)] + new_grid_inner + c[end:]
    
    with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    shutil.copy('demo_lab/reviews.html', 'reviews.html')
    shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
    print("Reviews sorted: Photos first, Texts later!")
else:
    print("Could not find grid bounds")
