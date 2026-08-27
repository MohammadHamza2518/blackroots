import shutil, re

with open('demo_lab/reviews.html', 'r', encoding='utf-8') as f:
    c = f.read()

# ---- 2 Tamil Reviews ----
# Meenakshi Iyer (Chennai, TN) -> Tamil
c = c.replace(
    '"Greys blended after a few washes"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">Was skeptical at first honestly. After 3 washes the greys started blending in. No scalp irritation at all. Herbal smell is fine. No side effects so far.</p>',
    '"3 முறை கழுவிய பிறகு வேர்கள் கருமையாயின"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">இந்த தயாரிப்பை பற்றி சந்தேகமாக இருந்தது. ஆனால் 3 முறை கழுவிய பிறகு சாம்பல் முடி இயற்கையாக கருமையாக மாறியது. தலையில் எந்த எரிச்சலும் இல்லை. மூலிகை வாசனை பழகிவிட்டது.</p>'
)

# Deepak Nair (Kochi) -> change to Tamil reviewer Selvam from Coimbatore
c = c.replace(
    '<h3 class="font-serif text-base font-bold text-white leading-snug">Deepak Nair</h3>\n                  <span class="text-[10px] text-gray-400 block">Kochi, KL &bull; 6 days ago</span>',
    '<h3 class="font-serif text-base font-bold text-white leading-snug">Selvam Krishnan</h3>\n                  <span class="text-[10px] text-gray-400 block">Coimbatore, TN &bull; 6 days ago</span>'
)
c = c.replace(
    '"Surprisingly gentle on scalp"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">Was not expecting much honestly. But after 4 washes my grey patches have darkened quite a bit. No irritation at all. Will continue using.</p>',
    '"மென்மையாக இருக்கிறது, பக்க விளைவு இல்லை"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">4 முறை தேய்த்த பிறகு சாம்பல் பகுதிகள் கருமையாகி விட்டன. தலையில் எந்த எரிச்சலும் இல்லை. இயற்கையான மூலிகை வாசனை. தொடர்ந்து பயன்படுத்துவேன்.</p>'
)

# ---- 3 Hindi Reviews (Devanagari) ----
# Ritu Sharma (Indore, MP) -> pure Hindi
c = c.replace(
    '"Roots darken ho gayi, satisfied hun"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">Kuch expectations ke saath mangaya tha. 4 washes ke baad roots mein farak dikh raha hai. Scalp pe koi problem nahi. Thoda time lagta hai but worth it hai.</p>',
    '"4 बार धोने के बाद जड़ें काली हो गईं"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">थोड़ी उम्मीद के साथ मंगाया था। 4 बार धोने के बाद जड़ों में फ़र्क़ दिखने लगा। खोपड़ी पर कोई जलन नहीं हुई। थोड़ा समय लगता है पर काम करता है।</p>'
)

# Suresh Yadav (Agra, UP) -> pure Hindi
c = c.replace(
    '"Greys kaafi kam dikh rahe hain ab"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">Pehle zyada greys dikhte the, ab natural lag raha hai. Koi chemical smell nahi hai. COD milta hai jo achha laga. Delivery bhi time pe aayi thi.</p>',
    '"सफ़ेद बाल अब बहुत कम दिखते हैं"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">पहले ज़्यादा सफ़ेद बाल दिखते थे, अब काफ़ी कम हो गए हैं। कोई केमिकल गंध नहीं है। COD पर मंगाया, डिलीवरी भी समय पर आई।</p>'
)

# Naincy Tiwari (Kanpur, UP) -> pure Hindi
c = c.replace(
    '"Scalp feels calmer after using this"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">Delivery was quick, came in 2 days. Packaging was sealed properly. After a few washes scalp irritation reduced noticeably. Dandruff also seems less. Decent product.</p>',
    '"खुजली कम हुई, ठीक प्रोडक्ट है"</h4>\n            <p class="text-xs text-gray-300 leading-relaxed font-light">2 दिन में डिलीवरी आ गई। पैकेजिंग बंद थी। कुछ बार इस्तेमाल करने के बाद खोपड़ी पर खुजली कम हुई। रूसी भी थोड़ी कम लगी। कुल मिलाकर ठीक है।</p>'
)

with open('demo_lab/reviews.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copy('demo_lab/reviews.html', 'reviews.html')
shutil.copy('demo_lab/reviews.html', 'preview/reviews.html')
print('Done! 2 Tamil + 3 Hindi reviews updated and synced!')
