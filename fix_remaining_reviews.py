"""
Fix remaining reviews that use &amp; instead of & in HTML
"""

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remaining ones that have HTML entities
replacements = [
    (
        '"Soft silk hair feel, zero ammonia smell!"',
        '"Hair bahut dry nahi hua, accha laga"'
    ),
    (
        'As a woman, chemical dyes always made my hair dry like straw. BlackRoots is so gentle! My front root greys blended into shiny natural black after 3 washes. My hair feels nourished &amp; silky soft.',
        'Chemical dyes se hair bahut dry ho jaate the mere. Yahan 3 washes mein roots blend huin. Hair feel bhi soft hai relatively. Smell adjust ho jaata hai.'
    ),
    (
        '"Scalp irritation &amp; dandruff completely gone"',
        '"Scalp itching thodi kam hui, okay product"'
    ),
    (
        'Shuklaganj UP warehouse se dispatch fast hua tha 2 din me Kanpur mil gaya. Scalp itchiness complete band ho gayi aur flakes khatam ho gaye. 100% genuine herbal shampoo!',
        'Delivery 2 din mein aayi. Packaging sealed thi. Use karne ke baad scalp pe thodi relief mili. Dandruff bhi kuch kam hua. Overall theek experience raha.'
    ),
    (
        '"Great for men\'s hair &amp; beard greys"',
        '"Beard ke greys pe bhi use kiya"'
    ),
    (
        'Bhai beard greys par bhi use karke dekha &amp; natural dark black tone aaya without any skin staining. Simple 3 minute shower massage method works effortlessly.',
        'Beard mein bhi laga ke dekha. Kuch washes mein shade improve hua. Skin pe koi problem nahi aayi. Thoda patience chahiye results ke liye.'
    ),
    (
        '"Beard greys completely gone in 3 washes!"',
        '"3 washes mein noticeable change aaya"'
    ),
    (
        'Bhai beard &amp; patch greys par try kiya tha and 3rd wash tak natural dark shade aa gaya! Zero skin staining, zero itching and hair fall also reduced significantly. 100% recommended for men!',
        '3rd wash ke baad shade aaya tha noticeable. Koi skin reaction nahi tha. Hair fall bhi thoda kam laga. Theek product hai honestly.'
    ),
    (
        'We bought the 250ml bott',
        'Ghar mein dono use karte hain humlog. Bott'
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Fixed: {old[:60]}")
    else:
        print(f"Skip: {old[:60]}")

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nRemaining reviews fixed!")
