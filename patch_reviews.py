with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    'chemical dyes always made my hair dry like straw. BlackRoots is so gentle! My front root greys blended into shiny natural black after 3 washes. My hair feels nourished & silky soft.',
    'Chemical dyes se hair dry ho jaate the mujhe. 3 washes mein roots blend huin thodi. Hair feel bhi better hai. Smell adjust ho jaata hai.'
)

c = c.replace(
    "\"Great for men's hair & beard greys\"</h4>",
    '"Beard ke greys pe bhi kaam kiya"</h4>'
)

c = c.replace(
    'Bhai beard greys par bhi use karke dekha & natural dark black tone aaya without any skin staining. Simple 3 minute shower massage method works effortlessly.',
    'Beard pe bhi try kiya. 4 washes mein shade improve hua. Skin pe koi reaction nahi aaya. Thoda patience chahiye bas, instant nahi hota.'
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('All remaining stale reviews fixed!')
