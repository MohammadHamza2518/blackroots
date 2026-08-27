import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

index_file = os.path.join(root_dir, "index.html")

with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all video tags and sources
videos = re.findall(r'<video[^>]*>.*?<\/video>', content, re.DOTALL)
print(f"Total video elements in index.html: {len(videos)}")

for i, v in enumerate(videos):
    src_match = re.search(r'src=["\']([^"\']+)["\']', v)
    src = src_match.group(1) if src_match else "No src"
    poster_match = re.search(r'poster=["\']([^"\']+)["\']', v)
    poster = poster_match.group(1) if poster_match else "No poster"
    print(f"Video {i+1}: src={src}, poster={poster}")
