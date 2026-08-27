import shutil

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace Rakesh Gupta's DP with initials 'RG'
# Let's find Rakesh Gupta's current avatar.
# It should be an img tag inside a div next to his name.
import re
# Rakesh Gupta might have different avatar paths, let's just use regex to replace the whole div.
rakesh_pattern = r'<div class="w-12 h-12 rounded-full p-0\.5 bg-gradient-to-tr from-\[#d4af37\] via-\[#f3e5ab\] to-\[#d4af37\] shadow-lg shrink-0 overflow-hidden"><img src="[^"]+" alt="Rakesh Gupta" class="w-full h-full rounded-full object-cover object-top"></div>'
rakesh_new = '<div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">RG</div>'

c = re.sub(rakesh_pattern, rakesh_new, c)

# Replace Tariq Siddiqui's DP with initials 'TS'
tariq_pattern = r'<div class="w-12 h-12 rounded-full p-0\.5 bg-gradient-to-tr from-\[#d4af37\] via-\[#f3e5ab\] to-\[#d4af37\] shadow-lg shrink-0 overflow-hidden"><img src="[^"]+" alt="Tariq Siddiqui" class="w-full h-full rounded-full object-cover object-top"></div>'
tariq_new = '<div class="w-12 h-12 rounded-full bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] text-black font-extrabold text-sm flex items-center justify-center shadow-lg shrink-0 border border-white/20" title="User Has No Profile Photo Set">TS</div>'

c = re.sub(tariq_pattern, tariq_new, c)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print("Removed DPs for Rakesh Gupta and Tariq Siddiqui!")
