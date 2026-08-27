import re

avatar_map = {
    'Aarav Sharma': './assets/reviews/avatar-1.jpg',
    'Fatima Rizvi': './assets/reviews/avatar-4.jpg',
    'Rajesh K. Verma': './assets/reviews/face-avatar-1.jpg',
    'Zaid Mansuri': './assets/reviews/avatar-7.jpg',
    'Sunita Verma': './assets/reviews/face-avatar-2.jpg',
    'Imran Khan': './assets/reviews/avatar-5.jpg',
    'Pooja Sharma': './assets/reviews/avatar-6.jpg',
    'Farhan Ahmed': './assets/reviews/avatar-9.jpg',
    'Neha Joshi': './assets/reviews/avatar-8.jpg',
    'Tariq Siddiqui': './assets/reviews/face-avatar-3.jpg',
    'Meenakshi Iyer': './assets/reviews/avatar-12.jpg',
    'Sameer Sheikh': './assets/reviews/avatar-13.jpg',
}

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for name, img_path in avatar_map.items():
        # Replace avatar img block for this reviewer name
        pattern = r'(<div class="[^"]*">)?<img src="[^"]*" alt="' + re.escape(name) + r'"[^>]*>(</div>)?'
        new_block = f'<div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden"><img src="{img_path}" alt="{name}" class="w-full h-full rounded-full object-cover"></div>'
        content = re.sub(pattern, new_block, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated avatars in {filepath}')

update_file('demo_lab/reviews.html')
update_file('reviews.html')
update_file('preview/reviews.html')
