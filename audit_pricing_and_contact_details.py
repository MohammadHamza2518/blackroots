import os, re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]

print("=== DEEP SCAN 3: PRICING AND CONTACT DETAILS AUDIT ===")

email_pattern = r'blackroots\.in@gmail\.com'
phone_pattern = r'9580835179'

missing_email = []
missing_phone = []

for page in html_files:
    fpath = os.path.join(root_dir, page)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not re.search(email_pattern, content, re.IGNORECASE):
        missing_email.append(page)
    if not re.search(phone_pattern, content):
        missing_phone.append(page)

print(f"Pages checked: {len(html_files)}")
print(f"Pages with Email verified: {len(html_files) - len(missing_email)} / {len(html_files)}")
print(f"Pages with Phone/WhatsApp verified: {len(html_files) - len(missing_phone)} / {len(html_files)}")

if missing_email:
    print(f"  - Email missing in: {missing_email}")
if missing_phone:
    print(f"  - Phone/WhatsApp missing in: {missing_phone}")

