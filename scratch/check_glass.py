with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.css", "r", encoding="utf-8") as f:
    for i, line in enumerate(f.readlines()):
        if "glass-panel" in line:
            print(f"L{i+1}: {line.strip()}")
