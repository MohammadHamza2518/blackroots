import re

# Read mobile-preview.html
with open('mobile-preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make Product Page preview by default
product_preview_html = html.replace('src="index.html', 'src="product.html"')
product_preview_html = product_preview_html.replace('<option value="index.html" selected>', '<option value="index.html">')
product_preview_html = product_preview_html.replace('<option value="product.html">', '<option value="product.html" selected>')

with open('product-mobile-preview.html', 'w', encoding='utf-8') as f:
    f.write(product_preview_html)

print("CREATED product-mobile-preview.html")
