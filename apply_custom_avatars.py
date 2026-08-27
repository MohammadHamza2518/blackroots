import re

avatar_map = {
    'Aarav Sharma': './assets/reviews/custom-avatar-1.jpg',
    'Fatima Rizvi': './assets/reviews/custom-avatar-2.jpg',
    'Rajesh K. Verma': './assets/reviews/custom-avatar-3.jpg',
    'Sunita Verma': './assets/reviews/custom-avatar-12.jpg',
    'Zaid Mansuri': './assets/reviews/custom-avatar-7.jpg',
    'Imran Khan': './assets/reviews/custom-avatar-5.jpg',
    'Pooja Sharma': './assets/reviews/custom-avatar-6.jpg',
    'Farhan Ahmed': './assets/reviews/custom-avatar-9.jpg',
    'Neha Joshi': './assets/reviews/custom-avatar-8.jpg',
    'Tariq Siddiqui': './assets/reviews/custom-avatar-11.jpg',
    'Meenakshi Iyer': './assets/reviews/custom-avatar-10.jpg',
    'Sameer Sheikh': './assets/reviews/custom-avatar-20.jpg',
}

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for name, img_path in avatar_map.items():
        # Match the avatar block for this name
        pattern = r'<div class="w-12 h-12 rounded-full p-0\.5 bg-gradient-to-tr from-\[#d4af37\] via-\[#f3e5ab\] to-\[#d4af37\] shadow-lg shrink-0 overflow-hidden"><img src="[^"]*" alt="' + re.escape(name) + r'" class="w-full h-full rounded-full object-cover"></div>'
        new_block = f'<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="{img_path}" alt="{name}" class="w-full h-full rounded-full object-cover"></div>'
        content = re.sub(pattern, new_block, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated 100% matched face avatars in {filepath}')

update_file('demo_lab/reviews.html')
update_file('reviews.html')
update_file('preview/reviews.html')
