with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "DOMContentLoaded" in line or "addEventListener" in line or "init" in line:
        if i < 40 or i > len(lines) - 40:
            print(f"L{i+1}: {line.strip()}")
