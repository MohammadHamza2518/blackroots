import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

# 1. Update videos in index.html
files = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html"),
    os.path.join(root_dir, "product.html"),
    os.path.join(root_dir, "demo_lab", "product.html"),
    os.path.join(root_dir, "preview", "product.html")
]

poster_map = {
    'reel-6.mp4': './assets/reel-thumb-6.jpg',
    'reel-3.mp4': './assets/reel-thumb-3.jpg',
    'reel-2.mp4': './assets/reel-thumb-2.jpg',
    'reel-4.mp4': './assets/reel-thumb-4.jpg',
    'reel-1.mp4': './assets/reel-thumb-1.jpg',
    'reel-5.mp4': './assets/reel-thumb-5.jpg',
    '360 shampoo.mp4': './assets/blackroots-bottles-trio-hd.jpg'
}

video_recovery_script = """
  <!-- 🎬 High-Performance Zero-Blank Video & Poster Recovery Engine -->
  <script>
    (function() {
      function ensureVideosPlay() {
        const videos = document.querySelectorAll('video');
        videos.forEach(function(v) {
          v.muted = true;
          v.setAttribute('playsinline', '');
          v.setAttribute('webkit-playsinline', '');
          
          // Auto play on load & resume smoothly
          const playPromise = v.play();
          if (playPromise !== undefined) {
            playPromise.catch(function() {
              // If browser restricts autoplay, the poster remains crisp & visible
            });
          }
        });
      }

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', ensureVideosPlay);
      } else {
        ensureVideosPlay();
      }

      // Resume videos when tab becomes visible or on mobile touch
      document.addEventListener('visibilitychange', function() {
        if (!document.hidden) ensureVideosPlay();
      });
      window.addEventListener('pageshow', ensureVideosPlay);
    })();
  </script>
"""

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content
    
    # Attach posters for all reels
    for video_name, poster_path in poster_map.items():
        # Case 1: <video ...><source src="...reel-X.mp4"...></video>
        pattern = rf'(<video(?![^>]*poster=)[^>]*?>)(\s*<source[^>]*{video_name})'
        replacement = rf'\1 poster="{poster_path}"\2'
        new_content = re.sub(pattern, replacement, new_content)

        # Case 2: <video ... src="...reel-X.mp4" ...>
        pattern2 = rf'(<video(?![^>]*poster=)[^>]*?src=["\'][^"\']*{video_name}["\'][^>]*?>)'
        replacement2 = rf'\1'
        # inject poster attribute
        new_content = re.sub(
            rf'<video(?![^>]*poster=)([^>]*?src=["\'][^"\']*{video_name}["\'][^>]*?)>',
            rf'<video\1 poster="{poster_path}">',
            new_content
        )

    # Append zero-blank video engine before closing body
    new_content = re.sub(r'<!-- 🎬 High-Performance Zero-Blank Video & Poster Recovery Engine -->.*?<\/script>', '', new_content, flags=re.DOTALL)
    new_content = new_content.replace('</body>', video_recovery_script + '\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed video posters & recovery in", fpath)

