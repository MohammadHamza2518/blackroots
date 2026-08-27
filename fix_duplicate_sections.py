import os

def cleanup_duplicate_section(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # If there are duplicate Real Reviews Grid Containers:
    marker = '<!-- Real Reviews Grid Container -->'
    count = content.count(marker)
    if count > 1:
        # Keep everything up to first marker
        first_idx = content.find(marker)
        last_idx = content.rfind(marker)
        content = content[:first_idx] + content[last_idx:]

    # Ensure Sunita Verma and Alok Mishra are present right inside grid
    grid_start = '<div class="columns-1 md:columns-2 lg:columns-3 gap-6 space-y-6">'
    if 'id="sunita-verma"' not in content[content.find(grid_start):content.find(grid_start)+2000]:
        print(f"Warning: sunita-verma missing near grid start in {file_path}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Cleaned duplicate sections in {file_path}")

cleanup_duplicate_section('demo_lab/reviews.html')
cleanup_duplicate_section('reviews.html')
if os.path.exists('preview/reviews.html'):
    cleanup_duplicate_section('preview/reviews.html')

print("SECTION DUPLICATION FIX COMPLETE!")
