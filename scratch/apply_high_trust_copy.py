import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Page-specific high-trust luxury announcement definitions
page_configs = {
    "index.html": {
        "pill": "50% OFFER",
        "text": "FREE Express Delivery Across India &bull; Cash On Delivery (COD) Available &bull; ₹499"
    },
    "product.html": {
        "pill": "⭐ 100% AUTHENTIC",
        "text": "Japanese Herbal Formula &bull; FREE Express COD Delivery Across India &bull; ₹499"
    },
    "reviews.html": {
        "pill": "★ 4.9 / 5.0",
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

# Find all files with text extensions
extensions = ('*.html', '*.liquid', '*.json', '*.js')
all_files = []
for ext in extensions:
    all_files.extend(glob.glob(os.path.join(root_dir, '**', ext), recursive=True))

updated_files = []

for fpath in all_files:
    if 'scratch' in fpath or '.git' in fpath:
        continue
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        fname = os.path.basename(fpath)

        # 1. Update announcement bars if it's an HTML page in page_configs
        if fname in page_configs:
            cfg = page_configs[fname]
            new_bar = generate_announcement_html(cfg['pill'], cfg['text'])
            pattern = r'<!-- Top Announcement Bar.*?<\/div>\s*<\/div>'
            new_content = re.sub(pattern, new_bar, new_content, flags=re.DOTALL)
            if new_content == content:
                pattern2 = r'<div class="announcement-bar-solid.*?<\/div>\s*<\/div>'
                new_content = re.sub(pattern2, new_bar, new_content, flags=re.DOTALL)

        # 2. Clean drawer promo banners: "50% Launch Offer" / "Special Launch Offer" -> "Free Express COD Delivery Across India"
        new_content = new_content.replace('50% Launch Offer', 'Free Express Delivery')
        new_content = new_content.replace('Special Launch Offer', 'Free Express Delivery')
        new_content = new_content.replace('SPECIAL LAUNCH OFFER', 'FREE EXPRESS DELIVERY')
        new_content = new_content.replace('Introductory Price', 'Special Offer')
        new_content = new_content.replace('introductory price', 'special offer')
        new_content = new_content.replace('Introductory price', 'Special offer')

        # 3. Clean any remaining "Launch Offer"
        new_content = new_content.replace('Launch Offer', 'Special Offer')
        new_content = new_content.replace('launch offer', 'special offer')
        new_content = new_content.replace('LAUNCH OFFER', 'SPECIAL OFFER')

        # 4. If announcement bar in header.liquid:
        if fname == 'header.liquid':
            liquid_announcement = """<div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important; background-color: #133e28 !important; background-image: none !important;">
  <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap">
    {% if template contains 'product' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        ⭐ 100% AUTHENTIC
      </span>
      <span>Japanese Herbal Formula &bull; FREE Express COD Delivery Across India &bull; ₹499</span>
    {% elsif template contains 'reviews' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2 py-0.5 rounded-full uppercase tracking-wider">
        ★ 4.9 / 5.0
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
      <span>FREE Express Delivery Across India &bull; Cash On Delivery (COD) Available &bull; ₹499</span>
    {% endif %}
  </div>
</div>"""
            pattern_l = r'<div class="announcement-bar-solid.*?<\/div>\s*<\/div>'
            new_content = re.sub(pattern_l, liquid_announcement, new_content, flags=re.DOTALL)

        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.append(fpath)
    except Exception as e:
        print(f"Error processing {fpath}: {e}")

print(f"SUCCESS: High-trust luxury copy applied across {len(updated_files)} files!")
