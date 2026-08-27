with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.js", "r", encoding="utf-8") as f:
    content = f.read()

print("initAIConsultantChat() call present:", "initAIConsultantChat();" in content or "initAIConsultantChat()" in content)
