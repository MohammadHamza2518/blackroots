import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# 1. Update theme.css
theme_css_path = os.path.join(root_dir, "assets", "theme.css")
with open(theme_css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace scrollbar rules with universal zero scrollbar
scrollbar_replacement = """/* Universal Complete Scrollbar Elimination across all viewports & elements */
*::-webkit-scrollbar,
::-webkit-scrollbar,
html::-webkit-scrollbar,
body::-webkit-scrollbar,
iframe::-webkit-scrollbar {
  display: none !important;
  width: 0px !important;
  height: 0px !important;
  background: transparent !important;
}

*, html, body, iframe {
  -ms-overflow-style: none !important;
  scrollbar-width: none !important;
}"""

css = re.sub(r'\/\* Hide scrollbar for Chrome.*?scrollbar-width: none !important;\s*}', scrollbar_replacement, css, flags=re.DOTALL)

# Solidify glass-panel-luxury border
css = re.sub(
    r'\.glass-panel-luxury\s*\{[^}]*\}',
    """.glass-panel-luxury {
  background: rgba(18, 21, 28, 0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(212, 175, 55, 0.4) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}""",
    css
)

with open(theme_css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Updated theme.css with universal scrollbar removal & crisp uniform border!")

# 2. Update reviews.html files
files = [
    os.path.join(root_dir, "reviews.html"),
    os.path.join(root_dir, "demo_lab", "reviews.html"),
    os.path.join(root_dir, "preview", "reviews.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    # Ensure uniform border on all review cards
    new_content = new_content.replace('border-[#d4af37]/30', 'border-[#d4af37]/45')
    new_content = new_content.replace('border-[#d4af37]/35', 'border-[#d4af37]/45')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated card borders in {fpath}")

