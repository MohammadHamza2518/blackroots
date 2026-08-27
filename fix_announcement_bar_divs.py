import os

html_files = []
for root, dirs, files in os.walk(r"c:\Users\moham\Downloads\blackroots website"):
    for f in files:
        if f.endswith('.html') and f != 'mobile-preview.html':
            html_files.append(os.path.join(root, f))

print(f"Fixing announcement bar HTML structure across {len(html_files)} HTML files...")

clean_top_announcement_bar = """  <!-- Top Announcement Bar (Mobile & Desktop Optimized) -->
  <div class="bg-gradient-to-r from-[#123824] via-[#0d2a1c] to-[#123824] text-[#f5e4ab] border-b border-[#d4af37]/30 py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap">
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        SPECIAL OFFER
      </span>
      <span>FREE Express Delivery Across India &bull; Introductory Price ₹499.00</span>
    </div>
  </div>"""

for fpath in html_files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find start of body tag and start of header tag
        body_idx = content.find('<body')
        header_idx = content.find('<header')

        if body_idx != -1 and header_idx != -1 and header_idx > body_idx:
            body_close = content.find('>', body_idx)
            body_content = content[body_close+1:header_idx]
            
            # Replace whatever comments or announcement bar divs are between <body> and <header> with clean single announcement bar
            new_content = content[:body_close+1] + "\n\n" + clean_top_announcement_bar + "\n\n  " + content[header_idx:]
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"CLEANED ANNOUNCEMENT BAR STRUCTURE IN: {fpath}")
    except Exception as e:
        print(f"Error cleaning {fpath}: {e}")
