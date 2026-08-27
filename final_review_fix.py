import shutil

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '"Scalp itching thodi kam hui, okay product"',
    '"Scalp irritation reduced after a few washes"'
)
c = c.replace(
    '3rd wash ke baad shade aaya tha noticeable. Koi skin reaction nahi tha. Hair fall bhi thoda kam laga. Theek product hai honestly.',
    '3rd wash ke baad beard mein noticeable change tha. Skin pe koi reaction nahi tha. Hair fall bhi thoda kam laga.'
)
c = c.replace(
    '"Husband ne bhi use karna shuru kiya"',
    '"Husband started using it too after seeing results"'
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)
shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print('All fixed and synced!')
