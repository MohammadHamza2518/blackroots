import os

with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "ingredient" in line.lower():
        print(f"L{i+1}: {line.strip()}")
