import os

html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

desktop_clean_head_css = """
  <!-- Mobile-Only Responsive Adjustments (Desktop Untouched) -->
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

        modified = False

        # 1. Restore standard viewport meta tag
        old_vp = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
        clean_vp = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        if old_vp in content:
            content = content.replace(old_vp, clean_vp)
            modified = True

        # 2. Restore clean body tag
        if 'overflow-x-hidden w-full max-w-full' in content:
            content = content.replace('overflow-x-hidden w-full max-w-full ', '')
            content = content.replace('overflow-x-hidden w-full max-w-full', '')
            modified = True

        # 3. Replace mobile style block with desktop-safe media-query scoped block
        if '/* Mobile & Touch Optimization (Android & iOS) */' in content:
            start_style = content.find('<!-- Mobile & Touch Optimization')
            end_style = content.find('</style>', start_style)
            if start_style != -1 and end_style != -1:
                content = content[:start_style] + desktop_clean_head_css + content[end_style+8:]
                modified = True
        elif '/* Mobile-Only Responsive Adjustments (Desktop Untouched) */' not in content:
            head_end = content.find('</head>')
            if head_end != -1:
                content = content[:head_end] + desktop_clean_head_css + '\n' + content[head_end:]
                modified = True

        if modified:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"RESTORED DESKTOP PERFECTION IN: {fpath}")
    except Exception as e:
        print(f"Error restoring {fpath}: {e}")
