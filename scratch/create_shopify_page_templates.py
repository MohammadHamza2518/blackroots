import os
import json

root_dir = r"c:\Users\moham\Downloads\blackroots website"
templates_dir = os.path.join(root_dir, "templates")

# 1. page.ingredients.json
ingredients_tpl = {
    "sections": {
        "main": {
            "type": "main-page",
            "settings": {}
        },
        "ingredients": {
            "type": "ingredients-grid",
            "settings": {}
        }
    },
    "order": ["main", "ingredients"]
}

# 2. page.how-to-use.json
how_to_use_tpl = {
    "sections": {
        "main": {
            "type": "main-page",
            "settings": {}
        },
        "ritual": {
            "type": "how-to-use",
            "settings": {}
        }
    },
    "order": ["main", "ritual"]
}

# 3. page.reviews.json
reviews_tpl = {
    "sections": {
        "main": {
            "type": "main-page",
            "settings": {}
        },
        "reviews": {
            "type": "reviews-carousel",
            "settings": {}
        }
    },
    "order": ["main", "reviews"]
}

# 4. page.ai-doctor.json
ai_doctor_tpl = {
    "sections": {
        "main": {
            "type": "main-page",
            "settings": {}
        }
    },
    "order": ["main"]
}

# 5. page.influencer.json
influencer_tpl = {
    "sections": {
        "main": {
            "type": "main-page",
            "settings": {}
        }
    },
    "order": ["main"]
}

tpl_map = {
    "page.ingredients.json": ingredients_tpl,
    "page.how-to-use.json": how_to_use_tpl,
    "page.reviews.json": reviews_tpl,
    "page.ai-doctor.json": ai_doctor_tpl,
    "page.influencer.json": influencer_tpl
}

for fname, data in tpl_map.items():
    fpath = os.path.join(templates_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Created template: templates/{fname}")

