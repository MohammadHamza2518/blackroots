import os
import glob
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Short, crisp, 1-line professional announcement copy
short_page_configs = {
    "index.html": {
        "pill": "50% OFF",
        "text": "Free Express Delivery Across India &bull; ₹499"
    },
    "product.html": {
        "pill": "50% OFF",
        "text": "Free Express Delivery &bull; COD Available &bull; ₹499"
    },
    "reviews.html": {
        "pill": "4.9 ★ RATED",
        "text": "1,280+ Verified Customer Results"
    },
    "ingredients.html": {
        "pill": "100% BOTANICAL",
        "text": "Japanese Herbal Actives &bull; Zero Ammonia"
    },
    "how-to-use.html": {
        "pill": "10-MIN RITUAL",
        "text": "Quick 5-Step Application Guide"
    },
    "ai-consultant.html": {
        "pill": "AI DOCTOR",
        "text": "Instant Hair Consultation by Dr. Kuroki"
    },
    "track-order.html": {
        "pill": "LIVE TRACKING",
        "text": "Real-Time Order & Courier Updates"
    },
    "contact.html": {
        "pill": "24/7 SUPPORT",
        "text": "Dedicated Hair Care Assistance"
    },
    "influencer.html": {
        "pill": "PARTNER WITH US",
        "text": "Earn 15% Lifetime Commissions"
    },
    "admin-influencer.html": {
        "pill": "ADMIN CONSOLE",
        "text": "Affiliate & Order Dashboard"
    },
    "privacy-policy.html": {
        "pill": "100% SECURE",
        "text": "Authentic Japanese Herbal Formula"
    },
    "refund-policy.html": {
        "pill": "100% SECURE",
        "text": "Easy Support & Satisfaction Guaranteed"
    },
    "shipping-policy.html": {
        "pill": "EXPRESS SHIPPING",
        "text": "All-India Delivery &bull; COD Available"
    },
    "terms.html": {
        "pill": "100% SECURE",
        "text": "Authentic Japanese Herbal Formula"
    }
}

def generate_short_announcement_html(pill, text):
    return f"""  <!-- Top Announcement Bar (Short, Crisp, Luxury 1-Line) -->
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
            if fname in short_page_configs:
                cfg = short_page_configs[fname]
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8') as file:
                    content = file.read()

                new_bar = generate_short_announcement_html(cfg['pill'], cfg['text'])
                
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
    liquid_announcement = """<div class="announcement-bar-solid py-2 px-3 text-center text-[11px] sm:text-xs font-bold tracking-wide" style="background: #133e28 !important; background-color: #133e28 !important; background-image: none !important;">
  <div class="max-w-7xl mx-auto flex items-center justify-center gap-2 flex-wrap whitespace-nowrap">
    {% if template contains 'product' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        50% OFF
      </span>
      <span>Free Express Delivery &bull; COD Available &bull; ₹499</span>
    {% elsif template contains 'reviews' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        4.9 ★ RATED
      </span>
      <span>1,280+ Verified Customer Results</span>
    {% elsif template contains 'ingredient' %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        100% BOTANICAL
      </span>
      <span>Japanese Herbal Actives &bull; Zero Ammonia</span>
    {% else %}
      <span class="inline-flex items-center gap-1 bg-[#d4af37] text-black font-extrabold text-[9px] sm:text-[10px] px-2.5 py-0.5 rounded-full uppercase tracking-wider">
        50% OFF
      </span>
      <span>Free Express Delivery Across India &bull; ₹499</span>
    {% endif %}
  </div>
</div>"""

    with open(header_liquid_path, 'r', encoding='utf-8') as f:
        l_content = f.read()

    pattern_l = r'<div class="announcement-bar-solid.*?<\/div>\s*<\/div>'
    new_l_content = re.sub(pattern_l, liquid_announcement, l_content, flags=re.DOTALL)

    with open(header_liquid_path, 'w', encoding='utf-8') as f:
        f.write(new_l_content)

print(f"SUCCESS: Applied short, crisp, luxury copy across {updated_count} HTML files & header.liquid!")
