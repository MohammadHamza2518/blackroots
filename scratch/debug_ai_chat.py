with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.js", "r", encoding="utf-8") as f:
    content = f.read()

for i, line in enumerate(content.splitlines()):
    if "initAIConsultantChat" in line or "AIChatForm" in line:
        print(f"L{i+1}: {line}")
