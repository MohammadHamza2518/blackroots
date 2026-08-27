import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"
tfile = os.path.join(root_dir, "assets", "theme.js")

with open(tfile, "r", encoding="utf-8") as f:
    content = f.read()

print("Is 'function initIngredientFilters' in theme.js?", "function initIngredientFilters" in content)
