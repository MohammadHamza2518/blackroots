import shutil
import re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

grid_open = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start">'
grid_close = '      </div>\n\n      <!-- Bottom Order Callout -->'

start = c.find(grid_open)
end = c.find(grid_close)

if start != -1 and end != -1:
    grid_inner = c[start + len(grid_open):end]
    
    raw_cards = grid_inner.split('<div class="p-6 rounded-3xl glass-panel-luxury')
    
    actual_cards = []
    for rc in raw_cards[1:]:
        actual_cards.append('<div class="p-6 rounded-3xl glass-panel-luxury' + rc)
        
    print(f"Found {len(actual_cards)} cards")
    
    # Extract likes for each card
    cards_with_likes = []
    for card in actual_cards:
        # Match '&#128077; 23 Helpful' or similar
        like_match = re.search(r'&#128077;\s*(\d+)\s*Helpful', card)
        if like_match:
            likes = int(like_match.group(1))
        else:
            likes = 0
            
        # Give a slight boost to photo cards so they tend to be higher, or just strictly sort by likes?
        # User said "top most like wale rakho", so strictly by likes is fine.
        cards_with_likes.append((likes, card))
        
    # Sort by likes descending
    cards_with_likes.sort(key=lambda x: x[0], reverse=True)
    
    # Rebuild the grid inner HTML
    new_grid_inner = ''.join([card for likes, card in cards_with_likes])
    
    new_content = c[:start + len(grid_open)] + new_grid_inner + c[end:]
    
    with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    shutil.copy('demo_lab/reviews.html', 'reviews.html')
    shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
    print("Reviews sorted globally by likes descending!")
else:
    print("Could not find grid bounds")
