import os

scrollbar_css = """
/* Custom Luxury Dark Gold Scrollbar - Replaces Ugly White Browser Scrollbars */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgba(10, 11, 14, 0.95);
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, #d4af37, #9e7b26);
  border-radius: 9999px;
  border: 1px solid rgba(212, 175, 55, 0.3);
}

::-webkit-scrollbar-thumb:hover {
  background: #f5e4ab;
}

#modal-card::-webkit-scrollbar {
  width: 6px;
}

#modal-card::-webkit-scrollbar-track {
  background: rgba(18, 21, 28, 0.95);
  border-radius: 9999px;
}

#modal-card::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, #d4af37, #b38f28);
  border-radius: 9999px;
  border: 1px solid rgba(212, 175, 55, 0.4);
}

#modal-card::-webkit-scrollbar-thumb:hover {
  background: #f5e4ab;
}

#modal-card {
  scrollbar-width: thin;
  scrollbar-color: #d4af37 rgba(18, 21, 28, 0.95);
}
"""

def update_css_file(css_path):
    if not os.path.exists(css_path):
        return
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '#modal-card::-webkit-scrollbar' not in content:
        content += '\n' + scrollbar_css
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {css_path} with luxury scrollbar CSS!")

update_css_file('assets/theme.css')
update_css_file('demo_lab/assets/theme.css')
if os.path.exists('preview/assets/theme.css'):
    update_css_file('preview/assets/theme.css')

# Also update add_customer_review_feature.py
with open('add_customer_review_feature.py', 'r', encoding='utf-8') as f:
    py_content = f.read()

old_masonry = """masonry_css = \"\"\"
  <style>
    /* Absolute Masonry Stability Fix - Prevents Layout Shifting & Empty Black Gaps */
    .columns-1 > div, .columns-2 > div, .columns-3 > div {
      break-inside: avoid-column !important;
      -webkit-column-break-inside: avoid !important;
      page-break-inside: avoid !important;
      display: inline-block !important;
      width: 100% !important;
      margin-bottom: 1.5rem !important;
    }
  </style>
\"\"\""""

new_masonry = """masonry_css = \"\"\"
  <style>
    /* Absolute Masonry Stability Fix - Prevents Layout Shifting & Empty Black Gaps */
    .columns-1 > div, .columns-2 > div, .columns-3 > div {
      break-inside: avoid-column !important;
      -webkit-column-break-inside: avoid !important;
      page-break-inside: avoid !important;
      display: inline-block !important;
      width: 100% !important;
      margin-bottom: 1.5rem !important;
    }

    /* Custom Luxury Dark Gold Scrollbar for Modal Card */
    #modal-card::-webkit-scrollbar {
      width: 6px !important;
    }
    #modal-card::-webkit-scrollbar-track {
      background: rgba(18, 21, 28, 0.95) !important;
      border-radius: 9999px !important;
    }
    #modal-card::-webkit-scrollbar-thumb {
      background: linear-gradient(to bottom, #d4af37, #b38f28) !important;
      border-radius: 9999px !important;
      border: 1px solid rgba(212, 175, 55, 0.4) !important;
    }
    #modal-card::-webkit-scrollbar-thumb:hover {
      background: #f5e4ab !important;
    }
    #modal-card {
      scrollbar-width: thin !important;
      scrollbar-color: #d4af37 rgba(18, 21, 28, 0.95) !important;
    }
  </style>
\"\"\""""

if old_masonry in py_content:
    py_content = py_content.replace(old_masonry, new_masonry)
    with open('add_customer_review_feature.py', 'w', encoding='utf-8') as f:
        f.write(py_content)
    print("Updated add_customer_review_feature.py with custom scrollbar CSS!")

print("SCROLLBAR AESTHETIC FIX COMPLETE!")
