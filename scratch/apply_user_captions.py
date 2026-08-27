import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Precise mapping using the user's provided captions with professional matching symbols
user_captions_map = {
    "index.html": {
        "pill": "✨ 50% OFF",
        "text": "One Shampoo, Complete Hair Solution &bull; ₹499"
    },
    "product.html": {
        "pill": "🔥 50% OFF",
        "text": "Grey To Black, Just Shampoo &bull; Free Delivery"
    },
    "reviews.html": {
        "pill": "★ 4.9 RATED",
        "text": "Black Hair, Healthy Hair Guaranteed"
    },
    "ingredients.html": {
        "pill": "🌿 BOTANICAL",
        "text": "No Grey, No Fall, No Dandruff"
    },
    "how-to-use.html": {
        "pill": "⏱️ 10 MINUTES",
        "text": "Grey Hair Ends, Black Begins"
    },
    "ai-consultant.html": {
        "pill": "🩺 AI DOCTOR",
        "text": "Healthy Black Hair Starts Here"
    },
    "track-order.html": {
        "pill": "🚚 DISPATCHED",
        "text": "Grey Hair? Turns Black Instantly"
    },
    "contact.html": {
        "pill": "💬 24/7 HELP",
        "text": "Say Bye To Grey Hair"
    },
    "influencer.html": {
        "pill": "🤝 PARTNER",
        "text": "Stop Hair Fall, Go Black &bull; Earn 15%"
    },
    "admin-influencer.html": {
        "pill": "⚙️ ADMIN",
        "text": "BlackRoots Affiliate & Orders Console"
    },
    "shipping-policy.html": {
        "pill": "📦 EXPRESS",
        "text": "Dandruff Free, Fall Free, Black"
    },
    "privacy-policy.html": {
        "pill": "🛡️ AUTHENTIC",
        "text": "Dandruff Free, Fall Free, Black"
    },
    "refund-policy.html": {
        "pill": "🛡️ GUARANTEE",
        "text": "Black Hair, Healthy Hair Guaranteed"
    },
    "terms.html": {
        "pill": "🛡️ 100% SAFE",
        "text": "Dandruff Free, Fall Free, Black"
    }
}

def generate_custom_announcement(pill, text):
    return f"""  <!-- Top Announcement Bar (Curated User Captions • Crisp & Luxury) -->
  <div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important; background-color: #133e28 !important; background-image: none !important;">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap whitespace-nowrap">
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        {pill}
      </span>
      <span>{text}</span>
    </div>
  </div>"""

updated_count = 0
for root, dirs, files in os.walk(root_dir):
    for f in files:
        if f.endswith('.html'):
            fname = f
            if fname in user_captions_map:
                cfg = user_captions_map[fname]
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8') as file:
                    content = file.read()

                new_bar = generate_custom_announcement(cfg['pill'], cfg['text'])
                
                # Replace announcement bar
                pattern = r'<!-- Top Announcement Bar.*?<\/div>\s*<\/div>'
                new_content = re.sub(pattern, new_bar, content, flags=re.DOTALL)

                if new_content == content:
                    pattern2 = r'<div class="announcement-bar-solid.*?<\/div>\s*<\/div>'
                    new_content = re.sub(pattern2, new_bar, content, flags=re.DOTALL)

                with open(fpath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                updated_count += 1

# Also update sections/header.liquid with the matching captions for Shopify
header_liquid_path = os.path.join(root_dir, "sections", "header.liquid")
if os.path.exists(header_liquid_path):
    liquid_announcement = """<div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important; background-color: #133e28 !important; background-image: none !important;">
  <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap whitespace-nowrap">
    {% if template contains 'product' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        🔥 50% OFF
      </span>
      <span>Grey To Black, Just Shampoo &bull; Free Delivery</span>
    {% elsif template contains 'reviews' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        ★ 4.9 RATED
      </span>
      <span>Black Hair, Healthy Hair Guaranteed</span>
    {% elsif template contains 'ingredient' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        🌿 BOTANICAL
      </span>
      <span>No Grey, No Fall, No Dandruff</span>
    {% else %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        ✨ 50% OFF
      </span>
      <span>One Shampoo, Complete Hair Solution &bull; ₹499</span>
    {% endif %}
  </div>
</div>"""

    with open(header_liquid_path, 'r', encoding='utf-8') as f:
        l_content = f.read()

    pattern_l = r'<div class="announcement-bar-solid.*?<\/div>\s*<\/div>'
    new_l_content = re.sub(pattern_l, liquid_announcement, l_content, flags=re.DOTALL)

    with open(header_liquid_path, 'w', encoding='utf-8') as f:
        f.write(new_l_content)

print(f"SUCCESS: Applied user-selected curated captions across {updated_count} HTML files & sections/header.liquid!")
