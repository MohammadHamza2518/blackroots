with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.js", "r", encoding="utf-8") as f:
    for i, line in enumerate(f.readlines()):
        if "AIChat" in line or "Kuroki" in line or "consultant" in line or "ai" in line.lower():
            print(f"L{i+1}: {line.strip()}")
