import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"

files = [
    os.path.join(root_dir, "reviews.html"),
    os.path.join(root_dir, "demo_lab", "reviews.html"),
    os.path.join(root_dir, "preview", "reviews.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean double </div></div> after Sort & Count Clean Row
    new_content = content.replace('        </div>\n      </div>\n      </div>\n\n    </div>\n  </section>', '        </div>\n      </div>\n\n    </div>\n  </section>')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Cleaned closing div tag in:", fpath)

