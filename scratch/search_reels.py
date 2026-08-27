with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'reel' in line.lower() or 'premature' in line.lower() or 'testimonial' in line.lower():
        print(f"Line {i+1}: {line.strip()[:140]}")
