import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# 1. Clean track-order.html (Remove any "Quick Test" / "Demo" pills)
track_files = [
    os.path.join(root_dir, "track-order.html"),
    os.path.join(root_dir, "demo_lab", "track-order.html"),
    os.path.join(root_dir, "preview", "track-order.html")
]

for tf in track_files:
    if not os.path.exists(tf):
        continue
    with open(tf, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove demo pills block
    new_content = re.sub(
        r'<!-- Quick Demo Pills for Instant 1-Tap Test -->[\s\S]*?<\/div>\s*(?=<form)',
        '',
        content
    )
    # Also remove any other demo buttons if present
    new_content = re.sub(
        r'<div class="flex items-center gap-2 flex-wrap text-xs">[\s\S]*?<\/div>\s*(?=<form)',
        '',
        new_content
    )

    with open(tf, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Removed all demo test pills from:", tf)

# 2. Re-verify reviews.html sort row for ultra-clean mobile containment
reviews_files = [
    os.path.join(root_dir, "reviews.html"),
    os.path.join(root_dir, "demo_lab", "reviews.html"),
    os.path.join(root_dir, "preview", "reviews.html")
]

for rf in reviews_files:
    if not os.path.exists(rf):
        continue
    with open(rf, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean double </div> if present
    content = content.replace('        </div>\n      </div>\n      </div>\n\n    </div>\n  </section>', '        </div>\n      </div>\n\n    </div>\n  </section>')

    with open(rf, "w", encoding="utf-8") as f:
        f.write(content)
    print("Cleaned reviews layout in:", rf)

