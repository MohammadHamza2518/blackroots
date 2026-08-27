import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

print("--- AUDITING REVIEW SUBMISSION ENGINE ACROSS ALL FILES ---")

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        has_modal = 'id="add-review-modal"' in content
        has_dp = 'id="review-dp-input"' in content
        has_max_2_photos = 'uploadedPhotosDataUrls' in content
        has_local_storage = 'blackroots_user_reviews' in content
        has_deck_prepend = 'window.addNewReviewToDeck' in content

        print(f"FILE: {fpath}")
        print(f"  - Modal HTML Present: {has_modal}")
        print(f"  - DP Avatar Upload Field: {has_dp}")
        print(f"  - 0/1/2 Photo Upload Engine: {has_max_2_photos}")
        print(f"  - LocalStorage Persistence: {has_local_storage}")
        print(f"  - Slide 1 Prepend Logic: {has_deck_prepend}")

