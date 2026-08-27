with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.js", "r", encoding="utf-8") as f:
    content = f.read()

print("initAIChat in theme.js:", "initAIChat" in content)
print("AIChatForm in theme.js:", "AIChatForm" in content)
