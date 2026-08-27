import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Page-specific definitions
page_configs = {
    "index.html": {
        "pill": "50% OFFER",
        "text": "FREE Express Delivery Across India &bull; Introductory Price ₹499.00"
    },
    "product.html": {
        "pill": "⚡ HIGH DEMAND",
        "text": "Only 31 Bottles Left in Stock &bull; Special Launch Offer ₹499.00"
    },
    "reviews.html": {
        "pill": "★ 4.9 RATED",
        "text": "1,280+ Verified Indian Customer Transformations & Photos"
    },
    "ingredients.html": {
        "pill": "🌿 100% BOTANICAL",
        "text": "Japanese Formulation &bull; Zero Ammonia &bull; Pure Herbal Extracts"
    },
    "how-to-use.html": {
        "pill": "⏱️ 10-MIN RITUAL",
        "text": "Simple 5-Step Application for Natural Long-Lasting Black Hair"
    },
    "ai-consultant.html": {
        "pill": "✨ AI TRICHOLOGIST",
        "text": "Instant Personalized Hair Care Analysis by Dr. Kuroki"
    },
    "track-order.html": {
        "pill": "📦 LIVE TRACKING",
        "text": "Real-Time Courier Updates via Delhivery, Bluedart & XpressBees"
    },
    "contact.html": {
        "pill": "💬 24/7 SUPPORT",
        "text": "Dedicated Hair Specialist Assistance & WhatsApp Support"
    },
    "influencer.html": {
        "pill": "🤝 PARTNER WITH US",
        "text": "Earn 15% Lifetime Commissions &bull; Instant Weekly Payouts"
    },
    "admin-influencer.html": {
        "pill": "⚙️ ADMIN PORTAL",
        "text": "BlackRoots Affiliate & Payout Management Console"
    },
    "privacy-policy.html": {
        "pill": "🛡️ 100% TRUSTED",
        "text": "100% Authentic Japanese Formula &bull; Safe & Secure Checkout"
    },
    "refund-policy.html": {
        "pill": "🛡️ 100% TRUSTED",
        "text": "100% Authentic Japanese Formula &bull; Safe & Secure Checkout"
    },
    "shipping-policy.html": {
        "pill": "🚚 EXPRESS DELIVERY",
        "text": "Dispatch in 24 Hours &bull; Cash On Delivery Available Across India"
    },
    "terms.html": {
        "pill": "🛡️ 100% TRUSTED",
        "text": "100% Authentic Japanese Formula &bull; Safe & Secure Checkout"
    }
}

def generate_announcement_html(pill, text):
    return f"""  <!-- Top Announcement Bar (Mobile & Desktop Optimized • Solid Emerald) -->
  <div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important; background-color: #133e28 !important; background-image: none !important;">
    <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap">
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
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
            if fname in page_configs:
                cfg = page_configs[fname]
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8') as file:
                    content = file.read()

                new_bar = generate_announcement_html(cfg['pill'], cfg['text'])
                
                # Replace announcement bar
                pattern = r'<!-- Top Announcement Bar.*?<\/div>\s*<\/div>'
                new_content = re.sub(pattern, new_bar, content, flags=re.DOTALL)

                if new_content == content:
                    pattern2 = r'<div class="announcement-bar-solid.*?<\/div>\s*<\/div>'
                    new_content = re.sub(pattern2, new_bar, content, flags=re.DOTALL)

                with open(fpath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                updated_count += 1

# Also update sections/header.liquid
header_liquid_path = os.path.join(root_dir, "sections", "header.liquid")
if os.path.exists(header_liquid_path):
    with open(header_liquid_path, 'r', encoding='utf-8') as f:
        l_content = f.read()

    liquid_announcement = """<div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important; background-color: #133e28 !important; background-image: none !important;">
  <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap">
    {% if template contains 'product' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        ⚡ HIGH DEMAND
      </span>
      <span>Only 31 Bottles Left in Stock &bull; Special Launch Offer ₹499.00</span>
    {% elsif template contains 'reviews' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        ★ 4.9 RATED
      </span>
      <span>1,280+ Verified Indian Customer Transformations & Photos</span>
    {% elsif template contains 'ingredient' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        🌿 100% BOTANICAL
      </span>
      <span>Japanese Formulation &bull; Zero Ammonia &bull; Pure Herbal Extracts</span>
    {% else %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        50% OFFER
      </span>
      <span>FREE Express Delivery Across India &bull; Introductory Price ₹499.00</span>
    {% endif %}
  </div>
</div>"""

    pattern_l = r'<div class="[^"]*from-\[#123824\].*?<\/div>\s*<\/div>'
    new_l_content = re.sub(pattern_l, liquid_announcement, l_content, flags=re.DOTALL)
    if new_l_content == l_content:
        pattern_l2 = r'<div class="announcement-bar-solid.*?<\/div>\s*<\/div>'
        new_l_content = re.sub(pattern_l2, liquid_announcement, l_content, flags=re.DOTALL)

    with open(header_liquid_path, 'w', encoding='utf-8') as f:
        f.write(new_l_content)

print(f"SUCCESS: Updated {updated_count} HTML files and sections/header.liquid!")
