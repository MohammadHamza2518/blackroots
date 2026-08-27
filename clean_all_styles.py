import os

html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

clean_head_css = """
  <!-- Mobile & Touch Responsive Style -->
  <style>
    @media (max-width: 768px) {
      input[type="text"],
      input[type="email"],
      input[type="number"],
      input[type="password"],
      input[type="search"],
      select,
      textarea {
        font-size: 16px !important;
      }
      body {
        overflow-x: hidden;
      }
    }
    @media (min-width: 640px) {
      #MobileStickyBuyBar {
        display: none !important;
      }
    }
    .no-scrollbar::-webkit-scrollbar {
      display: none;
    }
    .no-scrollbar {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
  </style>
"""

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove duplicate style blocks
        while '<!-- Mobile & Touch Optimization (Android & iOS) -->' in content:
            s_idx = content.find('<!-- Mobile & Touch Optimization (Android & iOS) -->')
            e_idx = content.find('</style>', s_idx)
            if s_idx != -1 and e_idx != -1:
                content = content[:s_idx] + content[e_idx+8:]
            else:
                break

        while '<!-- Mobile-Only Responsive Adjustments (Desktop Untouched) -->' in content:
            s_idx = content.find('<!-- Mobile-Only Responsive Adjustments (Desktop Untouched) -->')
            e_idx = content.find('</style>', s_idx)
            if s_idx != -1 and e_idx != -1:
                content = content[:s_idx] + content[e_idx+8:]
            else:
                break

        while '<!-- Mobile & Touch Responsive Style -->' in content:
            s_idx = content.find('<!-- Mobile & Touch Responsive Style -->')
            e_idx = content.find('</style>', s_idx)
            if s_idx != -1 and e_idx != -1:
                content = content[:s_idx] + content[e_idx+8:]
            else:
                break

        # Clean up body tag
        content = content.replace('overflow-x-hidden w-full max-w-full ', '')
        content = content.replace('overflow-x-hidden w-full max-w-full', '')

        # Add clean single style block in head
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + clean_head_css + '\n' + content[head_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEANED AND FIXED STYLES IN: {fpath}")
    except Exception as e:
        print(f"Error cleaning {fpath}: {e}")
