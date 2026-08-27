with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Rewrite reviews - some pure English, some Hinglish, randomly mixed

replacements = [
    # Review 1: Aarav Sharma - HINGLISH
    (
        '"Greys cover ho gaye, 4-5 washes lage"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Thoda time lagta hai result aane me but aata zaroor hai. Chemical wali dyes se scalp damage ho raha tha, isliye try kiya. Ab greys kaafi cover hain. Smell bhi koi nahi hai.\n            </p>',
        '"Greys cover ho gaye, 4-5 washes lage"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Thoda patience chahiye hota hai but result aata hai. Chemical dyes se scalp damage ho raha tha toh switch kiya. Smell bilkul nahi hai jo achhi baat hai.\n            </p>'
    ),
    # Review 2: Fatima Rizvi - PURE ENGLISH
    (
        '"Hair bahut dry nahi hua, accha laga"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Chemical dyes se hair bahut dry ho jaate the mere. Yahan 3 washes mein roots blend huin. Hair feel bhi soft hai relatively. Smell adjust ho jaata hai.\n            </p>',
        '"Hair didn\'t dry out like other dyes"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Chemical dyes always left my hair feeling rough. After 3 washes the roots started blending nicely. Hair texture feels softer. The herbal smell is a bit strong but fades after rinsing.\n            </p>'
    ),
    # Review 3: Naincy Tiwari - PURE ENGLISH
    (
        '"Scalp itching thodi kam hui, okay product"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Delivery 2 din mein aayi. Packaging sealed thi. Use karne ke baad scalp pe itching band hui. Dandruff bhi thodi kam hua. Overall theek hai product.\n            </p>',
        '"Scalp feels calmer after using this"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Delivery was quick, came in 2 days. Packaging was sealed properly. After a few washes scalp irritation reduced noticeably. Dandruff also seems less. Decent product overall.\n            </p>'
    ),
    # Review 4: Zaid Mansuri - HINGLISH
    (
        '"Beard ke greys pe bhi kaam kiya"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Bhai beard pe bhi try kiya. 4 washes mein shade improve hua. Skin pe koi reaction nahi aaya. Thoda patience chahiye bas, instant nahi hota.\n            </p>',
        '"Beard pe bhi kaam kiya, satisfied hun"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Beard ke greys pe bhi lagaya dekha. 4 washes ke baad shade improve hua. Skin pe koi reaction nahi tha. Instant nahi hota but gradual aata hai jo natural lagta hai.\n            </p>'
    ),
    # Review 5: Rakesh Gupta - HINGLISH short
    (
        '"3 washes mein noticeable change aaya"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              3rd wash ke baad shade aaya tha noticeable. Koi skin reaction nahi tha. Hair fall bhi thoda kam laga. Theek product hai honestly.\n            </p>',
        '"3 washes ke baad farak dikh gaya"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              3rd wash ke baad beard mein visible change tha. Skin pe koi problem nahi aayi. Kafi accha laga result dekh ke.\n            </p>'
    ),
    # Review 6: Imran Khan - PURE ENGLISH
    (
        '"Ghar mein dono use karte hain"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Ghar mein dono use karte hain humlog. Bott',
        '"Both of us use it at home now"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              My wife and I both started using this. She uses it for her root greys, I use it for my scalp. Both of us have seen decent results after 4-5 washes. The 250ml bott'
    ),
    # Review 7: Pooja Sharma - PURE ENGLISH
    (
        '"Simple use, koi jhanjhat nahi"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Normal shampoo ki tarah hi use hota hai, gloves ya mixing ka koi chakar nahi. Roots thodi dark huin hai. Smell herbal type hai, adjust ho jaata hai.\n            </p>',
        '"So easy to use, no mess at all"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Works just like a normal shampoo, no mixing or gloves needed. Roots have gotten slightly darker. The herbal smell takes a bit of getting used to but it\'s fine.\n            </p>'
    ),
    # Review 8: Farhan Ahmed - HINGLISH
    (
        '"Pehle wash mein zyada nahi dikh, baad mein acha hua"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Pehle wash mein toh kuch nahi dikh tha, 3rd ke baad shade aa gaya. Chemical wali instant jet black nahi hai, gradually aata hai jo natural lagta hai.\n            </p>',
        '"Pehle wash mein kuch nahi dikh tha, gradually aaya"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Pehle wash ke baad koi farak nahi tha, 3rd wash mein shade aana shuru hua. Chemical dye jaisa instant black nahi hota, gradually aata hai. Mujhe yahi pasand aaya, natural lagta hai.\n            </p>'
    ),
    # Review 9: Neha Joshi - PURE ENGLISH (short)
    (
        '"Husband ne bhi use karna shuru kiya"</h4>',
        '"Husband started using it too after seeing my results"</h4>'
    ),
    # Review 10: Tariq Siddiqui - HINGLISH
    (
        '"COD mein aaya, packaging sahi thi"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              COD select kiya tha, 3 din mein aa gaya. Box sealed tha. Use kiya toh result aaya but 4-5 washes lagte hain. Chemical smell nahi hai jo achhi baat hai.\n            </p>',
        '"COD pe mangaya, 3 din mein aa gaya"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              COD option choose kiya tha, delivery 3 din mein aayi. Packing sealed thi. 4-5 washes mein result aaya. Koi chemical smell nahi hai.\n            </p>'
    ),
    # Review 11: Meenakshi Iyer - PURE ENGLISH
    (
        '"Roots thodi dark huin, overall okay"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Pehle mujhe doubt tha honestly. 3 washes ke baad greys thodi blend hin. Scalp irritation nahi hua. Smell herbal type hai. Koi side effect nahi mila abhi tak.\n            </p>',
        '"Greys blended after a few washes"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Was skeptical at first honestly. After 3 washes the greys started blending in. No scalp irritation at all. Herbal smell is fine. No side effects so far.\n            </p>'
    ),
    # Review 12: Sameer Sheikh - HINGLISH
    (
        '"2 bottle mangaye the, use ho gaye"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              2 bottle order kiye the ek saath. Pehli khatam ho gayi. Result aaya hai, greys cover hue hain kuch had tak. 250ml mein kaafi washes milte hain. Dobara le lunga.\n            </p>',
        '"2 bottle mangaye the, dobara lunga"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              2 bottles ek saath order kiye the. Pehli khatam ho gayi. Greys kafi cover hue hain. 250ml mein achhe washes milte hain. Dobara order karunga.\n            </p>'
    ),
    # Review 13: Priya Mehta - PURE ENGLISH
    (
        '"2-3 washes mein roots thodi dark lagi"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              2nd wash ke baad thoda farak dikh raha tha roots mein. Simple use hai, normal shampoo ki tarah. Smell strong nahi hai. Saheli ko bhi bata diya.\n            </p>',
        '"Roots noticeably darker after 2 washes"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Could see a visible difference at the roots after the 2nd wash. Easy to use, works like regular shampoo. Smell is mild and herbal. Already told a few friends about it.\n            </p>'
    ),
    # Review 14: Vikram Pandey - HINGLISH
    (
        '"Chemical dye se better laga mujhe"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Chemical dye se jo colour aata tha wo kaafi obvious lagta tha. Yahan gradual aata hai toh natural dikhai deta hai. COD tha delivery 4 din mein aayi. Theek experience raha.\n            </p>',
        '"Chemical dye se zyada natural lagta hai"</h4>\n            \n            <p class="text-xs text-gray-300 leading-relaxed font-light">\n              Chemical dye ka colour kaafi obvious hota tha, logo ko pta chal jaata tha. Yahan gradual color aata hai so natural dikhta hai. COD pe mangaya tha, 4 din mein aa gaya.\n            </p>'
    ),
]

for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
        print(f"Updated: {old[:50]}")
    else:
        print(f"SKIP: {old[:50]}")

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done! Reviews now randomly mixed English & Hinglish')
