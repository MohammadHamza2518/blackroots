import re

def fix_avatars(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match simple img tag avatar
    pattern = r'<img src="(\./assets/reviews/avatar-\d+\.jpg)" alt="([^"]+)" class="w-10 h-10 rounded-full object-cover border border-\[#d4af37\]">'
    replacement = r'<div class="w-11 h-11 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-md shrink-0"><img src="\1" alt="\2" class="w-full h-full rounded-full object-cover border border-black"></div>'
    
    new_content = re.sub(pattern, replacement, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Updated avatars in {filepath}')

fix_avatars('demo_lab/reviews.html')
fix_avatars('reviews.html')
fix_avatars('preview/reviews.html')
