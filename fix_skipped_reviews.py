with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix remaining skipped ones - find exact text in file
fixes = {
    '"Hair bahut dry nahi hua, accha laga"': '"Hair didn\'t feel dry or rough"',
    'Chemical dyes se hair dry ho jaate the mujhe. 3 washes mein roots blend huin thodi. Hair feel bhi better hai. Smell adjust ho jaata hai.': 
        'Chemical dyes always left my hair rough. After 3 washes roots blended nicely. Hair texture is better. The smell is herbal but okay.',
    
    '"Scalp itching thodi kam hui, okay product"': '"Scalp irritation reduced after using this"',
    'Delivery 2 din mein aayi. Packaging sealed thi. Use karne ke baad scalp pe thodi relief mili. Dandruff bhi kuch kam hua. Overall theek experience raha.':
        'Delivery came in 2 days. Packaging was sealed well. Scalp irritation reduced after a few washes. Dandruff also seems less. Decent product.',

    '"Beard ke greys pe bhi kaam kiya"': '"Beard pe bhi try kiya, kaam kiya"',
    'Beard pe bhi try kiya. 4 washes mein shade improve hua. Skin pe koi reaction nahi aaya. Thoda patience chahiye bas, instant nahi hota.':
        'Beard ke greys pe bhi lagaya. 4 washes ke baad shade improve hua. Skin pe koi reaction nahi tha. Instant nahi hota lekin gradual natural aata hai.',

    '"3 washes mein noticeable change aaya"': '"3rd wash ke baad visible difference tha"',
    '3rd wash ke baad shade aaya tha noticeable. Koi skin reaction nahi tha. Hair fall bhi thoda kam laga. Theek product hai honestly.':
        '3rd wash ke baad beard mein shade aaya. Skin pe koi issue nahi tha. Hair fall bhi thoda kam laga.',

    '"Husband ne bhi use karna shuru kiya"': '"Husband started using it after seeing my results"',
}

for old, new in fixes.items():
    if old in c:
        c = c.replace(old, new)
        print(f"Fixed: {old[:60]}")
    else:
        print(f"SKIP: {old[:60]}")

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done!')
