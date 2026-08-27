import os

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# Update product-mobile-preview.html and mobile-preview.html
simulator_files = [
    os.path.join(root_dir, "product-mobile-preview.html"),
    os.path.join(root_dir, "mobile-preview.html")
]

for sf in simulator_files:
    if os.path.exists(sf):
        with open(sf, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix broken iframe tag and ensure fresh dynamic loading
        content = content.replace('src="product.html"?v=1786734717"', 'src="product.html"')
        content = content.replace('src="index.html?v=1786738172"', 'src="index.html"')

        # Add auto cache bust script on DOMContentLoaded
        cache_script = """
    // Auto-bust cache on every initial load to always display latest live edits
    window.addEventListener('DOMContentLoaded', () => {
      const iframe = document.getElementById('SimulatedIframe');
      const pageSelector = document.getElementById('PageSelector');
      if (iframe && pageSelector) {
        const target = pageSelector.value || 'product.html';
        iframe.src = target + '?v=' + Date.now();
      }
    });
  </script>"""

        if 'window.addEventListener(\'DOMContentLoaded\'' not in content:
            content = content.replace('</script>', cache_script)

        with open(sf, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"FIXED & OPTIMIZED SIMULATOR: {sf}")
