import os
import glob
import re
import time

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Global timestamp for cache-busting
cache_v = int(time.time())

strict_head_css = f"""  <!-- Strict Zero-Scrollbar & Solid High-Definition Card Borders -->
  <style>
    /* Universal Mobile Scrollbar Complete Kill */
    *, *::before, *::after, html, body, div, section, iframe {{
      scrollbar-width: none !important;
      -ms-overflow-style: none !important;
      -webkit-overflow-scrolling: touch !important;
    }}
    *::-webkit-scrollbar, html::-webkit-scrollbar, body::-webkit-scrollbar {{
      display: none !important;
      width: 0px !important;
      height: 0px !important;
      background: transparent !important;
      opacity: 0 !important;
    }}
    
    /* 100% Solid Crisp Luxury Card Border (Zero Faint / Invisible Light Effect) */
    .glass-panel-luxury {{
      background: #11141b !important;
      border: 1px solid rgba(212, 175, 55, 0.65) !important;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6) !important;
    }}
    .review-card-solid {{
      background: #11141b !important;
      border: 1px solid rgba(212, 175, 55, 0.65) !important;
      border-radius: 1.25rem !important;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6) !important;
    }}
  </style>"""

html_files = glob.glob(os.path.join(root_dir, "**", "*.html"), recursive=True)

count = 0
for hf in html_files:
    if 'scratch' in hf or '.git' in hf:
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # 1. Update CSS & JS cache busters
    new_content = re.sub(r'theme\.css(\?v=\d+)?', f'theme.css?v={cache_v}', new_content)
    new_content = re.sub(r'theme\.js(\?v=\d+)?', f'theme.js?v={cache_v}', new_content)

    # 2. Inject strict_head_css if not present
    if '</head>' in new_content:
        # Remove old injected style if exists
        new_content = re.sub(r'<!-- Strict Zero-Scrollbar.*?<\/style>', '', new_content, flags=re.DOTALL)
        new_content = new_content.replace('</head>', f'{strict_head_css}\n</head>')

    if new_content != content:
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} HTML files with Cache-Buster v={cache_v} and Strict CSS!")
