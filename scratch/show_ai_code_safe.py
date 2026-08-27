with open(r"c:\Users\moham\Downloads\blackroots website\assets\theme.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "AIChatForm" in line:
        start = max(0, i - 10)
        end = min(len(lines), i + 60)
        for idx in range(start, end):
            print(f"{idx+1}: {lines[idx].encode('ascii', 'replace').decode()}")
        break
