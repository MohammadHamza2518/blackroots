import os

def clean_file(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Anita end marker
    anita_end_marker = '👍 <span class="js-like-count">760</span> Helpful\n            </button>\n          </div>\n        </div>'
    rakesh_start_marker = '<div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col break-inside-avoid mb-6" style="height: max-content;" data-category="men photo" data-date="20260804">'

    if anita_end_marker in content and rakesh_start_marker in content:
        start_idx = content.find(anita_end_marker) + len(anita_end_marker)
        end_idx = content.find(rakesh_start_marker)
        content = content[:start_idx] + '\n\n        ' + content[end_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleaned {file_path} successfully!")

clean_file('demo_lab/reviews.html')
clean_file('reviews.html')
if os.path.exists('preview/reviews.html'):
    clean_file('preview/reviews.html')

print("ANITA PATEL CLEAN COMPLETE!")
