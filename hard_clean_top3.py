import os

def hard_clean_top3(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find masonry grid start: <div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">
    grid_start_marker = '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">'
    rakesh_start_marker = '<div class="p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col break-inside-avoid mb-6" style="height: max-content;" data-category="men photo" data-date="20260804">'

    if grid_start_marker in content and rakesh_start_marker in content:
        start_idx = content.find(grid_start_marker) + len(grid_start_marker)
        end_idx = content.find(rakesh_start_marker)

        # Replace everything between masonry grid start and Rakesh Gupta start with clean spacing
        content = content[:start_idx] + '\n\n        ' + content[end_idx:]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Purged orphan fragments from {file_path}")

hard_clean_top3('demo_lab/reviews.html')
hard_clean_top3('reviews.html')
if os.path.exists('preview/reviews.html'):
    hard_clean_top3('preview/reviews.html')

print("TOP 3 HARD CLEAN COMPLETE!")
