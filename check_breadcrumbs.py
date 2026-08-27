import glob

for f in glob.glob('*.html') + glob.glob('demo_lab/*.html') + glob.glob('preview/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 'Hair Care' in content or ('Home' in content and '<span>/</span>' in content):
        print(f"Breadcrumb in: {f}")
