import os

html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix extra </div></div> at line 197
        content = content.replace('</div></div>\n\n    </div>\n  </section>', '</div>\n\n    </div>\n  </section>')
        content = content.replace('</div></div>\r\n\r\n    </div>\r\n  </section>', '</div>\r\n\r\n    </div>\r\n  </section>')
        content = content.replace('</div></div>', '</div>')

        # Remove duplicate comments
        content = content.replace('<!-- Before / After Authentic Photo Comparison Slider Section -->\n                      <!-- Watch Reels Section', '<!-- Watch Reels Section')
        content = content.replace('<!-- Before / After Authentic Photo Comparison Slider Section -->\r\n                      <!-- Watch Reels Section', '<!-- Watch Reels Section')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED DOM DIV TREE IN: {fpath}")

# Verify DOM div counts after fix
for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"{fpath} -> <div: {content.count('<div')}, </div>: {content.count('</div>')}")
