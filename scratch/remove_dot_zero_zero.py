import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Find all text files
extensions = ('*.html', '*.liquid', '*.json', '*.js', '*.css')
files_to_check = []
for ext in extensions:
    files_to_check.extend(glob.glob(os.path.join(root_dir, '**', ext), recursive=True))

updated_files = []

for filepath in files_to_check:
    # Skip build artifacts or scratch scripts
    if 'scratch' in filepath or '.git' in filepath:
        continue
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content

        # Replace variations of prices with .00
        # 1. HTML entities: &#8377;499.00 -> &#8377;499, &#8377; 499.00 -> &#8377; 499
        new_content = re.sub(r'(&#8377;\s*\d[\d,]*)\.00', r'\1', new_content)

        # 2. Rupee symbol: ₹499.00 -> ₹499, ₹ 499.00 -> ₹ 499, ₹1,499.00 -> ₹1,499
        new_content = re.sub(r'(₹\s*\d[\d,]*)\.00', r'\1', new_content)

        # 3. Rs. or INR: Rs. 499.00 -> Rs. 499, Rs 499.00 -> Rs 499, INR 499.00 -> INR 499
        new_content = re.sub(r'((?:Rs\.?|INR)\s*\d[\d,]*)\.00', r'\1', new_content)

        # 4. In JS / text where it says "499.00" or "799.00" or "999.00" or "1499.00"
        new_content = new_content.replace('499.00', '499')
        new_content = new_content.replace('799.00', '799')
        new_content = new_content.replace('899.00', '899')
        new_content = new_content.replace('999.00', '999')
        new_content = new_content.replace('1299.00', '1299')
        new_content = new_content.replace('1499.00', '1499')
        new_content = new_content.replace('1,499.00', '1,499')
        new_content = new_content.replace('1,299.00', '1,299')

        # 5. Fix JS price formatting functions like .toFixed(2) in client calculations if they add .00
        # e.g., if code has `price.toFixed(2)` -> `Math.round(price)` or `parseInt(price)`
        new_content = new_content.replace('.toFixed(2)}', '}')
        new_content = new_content.replace('.toFixed(2) +', ' +')

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.append(filepath)
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Cleaned .00 across {len(updated_files)} files:")
for u in updated_files:
    print(" -", u)
