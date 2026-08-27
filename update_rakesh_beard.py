import re

def update_beard_comment(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_text = '''            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Hair fall reduced by 80% in week 2!"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light">
              Not only did greys darken naturally, but my hair fall stopped significantly in week 2. Hair feels fuller, soft, and full of healthy natural black shine!
            </p>'''

    new_text = '''            <h4 class="font-serif text-lg font-bold text-white leading-snug">"Beard greys completely gone in 3 washes!"</h4>
            
            <p class="text-xs text-gray-300 leading-relaxed font-light">
              Bhai beard & patch greys par try kiya tha and 3rd wash tak natural dark shade aa gaya! Zero skin staining, zero itching and hair fall also reduced significantly. 100% recommended for men!
            </p>'''

    content = content.replace(old_text, new_text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated Rakesh Gupta beard comment in {filepath}')

update_beard_comment('demo_lab/reviews.html')
update_beard_comment('reviews.html')
update_beard_comment('preview/reviews.html')
