import os

target_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

story_pills_html = """          <!-- Story 1 Pill (Fix Grey Hair, Dandruff, Fall - Reel 01) -->
          <button type="button" class="js-select-reel text-left w-full flex-shrink-0 sm:w-auto lg:w-full p-4 rounded-2xl bg-[#d4af37]/10 border-2 border-[#d4af37] transition-all flex items-center gap-3 group shadow-xl focus:outline-none" data-reel-index="0" data-title="Fix Grey Hair, Dandruff, Fall" data-views="29.8K Views" data-tag="🛡️ Scalp Solution" data-video="./assets/reel-4.mp4">
            <div class="w-12 h-12 rounded-xl overflow-hidden border border-[#d4af37] shrink-0 relative bg-black">
              <img src="./assets/reel-icon-4.jpg" alt="Icon 4" class="w-full h-full object-cover group-hover:scale-110 transition-transform">
              <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                <svg class="w-4 h-4 text-amber-300 drop-shadow-md" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
            </div>
            <div>
              <span class="text-[10px] text-amber-300 font-bold uppercase tracking-wider block">Reel 01 &bull; 29.8K Views</span>
              <strong class="text-xs sm:text-sm text-white font-bold block group-hover:text-amber-300 transition-colors">Fix Grey Hair, Dandruff, Fall</strong>
            </div>
          </button>

          <!-- Story 2 Pill -->
          <button type="button" class="js-select-reel text-left w-full flex-shrink-0 sm:w-auto lg:w-full p-4 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/60 transition-all flex items-center gap-3 group focus:outline-none" data-reel-index="1" data-title="Say No To Flaky Dandruff" data-views="38.9K Views" data-tag="🌿 Anti-Dandruff Solution" data-video="./assets/reel-2.mp4">
            <div class="w-12 h-12 rounded-xl overflow-hidden border border-white/20 shrink-0 relative bg-black">
              <img src="./assets/reel-icon-2.jpg" alt="Icon 2" class="w-full h-full object-cover group-hover:scale-110 transition-transform">
              <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                <svg class="w-4 h-4 text-amber-300 drop-shadow-md" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
            </div>
            <div>
              <span class="text-[10px] text-gray-400 font-bold uppercase tracking-wider block">Reel 02 &bull; 38.9K Views</span>
              <strong class="text-xs sm:text-sm text-white font-bold block group-hover:text-amber-300 transition-colors">Say No To Flaky Dandruff</strong>
            </div>
          </button>

          <!-- Story 3 Pill -->
          <button type="button" class="js-select-reel text-left w-full flex-shrink-0 sm:w-auto lg:w-full p-4 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/60 transition-all flex items-center gap-3 group focus:outline-none" data-reel-index="2" data-title="Results Are 100% Real" data-views="61.2K Views" data-tag="⚡ Proven Results" data-video="./assets/reel-3.mp4">
            <div class="w-12 h-12 rounded-xl overflow-hidden border border-white/20 shrink-0 relative bg-black">
              <img src="./assets/reel-icon-3.jpg" alt="Icon 3" class="w-full h-full object-cover group-hover:scale-110 transition-transform">
              <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                <svg class="w-4 h-4 text-amber-300 drop-shadow-md" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
            </div>
            <div>
              <span class="text-[10px] text-gray-400 font-bold uppercase tracking-wider block">Reel 03 &bull; 61.2K Views</span>
              <strong class="text-xs sm:text-sm text-white font-bold block group-hover:text-amber-300 transition-colors">Results Are 100% Real</strong>
            </div>
          </button>

          <!-- Story 4 Pill -->
          <button type="button" class="js-select-reel text-left w-full flex-shrink-0 sm:w-auto lg:w-full p-4 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/60 transition-all flex items-center gap-3 group focus:outline-none" data-reel-index="3" data-title="Stop Premature Greying, Feel Confident" data-views="84.1K Views" data-tag="❤️ Real Testimonial" data-video="./assets/reel-5.mp4">
            <div class="w-12 h-12 rounded-xl overflow-hidden border border-white/20 shrink-0 relative bg-black">
              <img src="./assets/reel-icon-5.jpg" alt="Icon 5" class="w-full h-full object-cover group-hover:scale-110 transition-transform">
              <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                <svg class="w-4 h-4 text-amber-300 drop-shadow-md" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
            </div>
            <div>
              <span class="text-[10px] text-gray-400 font-bold uppercase tracking-wider block">Reel 04 &bull; 84.1K Views</span>
              <strong class="text-xs sm:text-sm text-white font-bold block group-hover:text-amber-300 transition-colors">Stop Premature Greying, Feel Confident</strong>
            </div>
          </button>

          <!-- Story 5 Pill -->
          <button type="button" class="js-select-reel text-left w-full flex-shrink-0 sm:w-auto lg:w-full p-4 rounded-2xl bg-white/5 border border-white/10 hover:border-[#d4af37]/60 transition-all flex items-center gap-3 group focus:outline-none" data-reel-index="4" data-title="Your Roots, Naturally Reborn Black" data-views="52.4K Views" data-tag="✨ Product Application" data-video="./assets/reel-1.mp4">
            <div class="w-12 h-12 rounded-xl overflow-hidden border border-white/20 shrink-0 relative bg-black">
              <img src="./assets/reel-icon-1.jpg" alt="Icon 1" class="w-full h-full object-cover group-hover:scale-110 transition-transform">
              <div class="absolute inset-0 bg-black/30 flex items-center justify-center">
                <svg class="w-4 h-4 text-amber-300 drop-shadow-md" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              </div>
            </div>
            <div>
              <span class="text-[10px] text-gray-400 font-bold uppercase tracking-wider block">Reel 05 &bull; 52.4K Views</span>
              <strong class="text-xs sm:text-sm text-white font-bold block group-hover:text-amber-300 transition-colors">Your Roots, Naturally Reborn Black</strong>
            </div>
          </button>"""

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        start_pill = content.find('<!-- Story 1 Pill')
        end_pill = content.find('<!-- Center Column')
        if end_pill != -1:
            end_pill = content.rfind('</div>', 0, end_pill)

        if start_pill != -1 and end_pill != -1:
            content = content[:start_pill] + story_pills_html + '\n\n        ' + content[end_pill:]

        # Update stage video initial src to reel-4.mp4
        stage_vid_idx = content.find('<video id="StageReelVideo"')
        if stage_vid_idx != -1:
            src_start = content.find('<source src=', stage_vid_idx)
            src_end = content.find('>', src_start)
            content = content[:src_start] + '<source src="./assets/reel-4.mp4" type="video/mp4"' + content[src_end:]

        # Update initial stage tag to 🛡️ Scalp Solution
        tag_start = content.find('<span id="ReelStageTag"')
        if tag_start != -1:
            tag_end = content.find('</span>', tag_start)
            content = content[:tag_start] + '<span id="ReelStageTag" class="bg-black/70 backdrop-blur-md text-amber-300 text-[10px] font-bold uppercase px-3 py-1 rounded-full border border-amber-500/30 shadow">\n                🛡️ Scalp Solution\n              ' + content[tag_end:]

        # Update initial stage title to Fix Grey Hair, Dandruff, Fall
        title_start = content.find('<h4 id="ReelStageTitle"')
        if title_start != -1:
            title_end = content.find('</h4>', title_start)
            content = content[:title_start] + '<h4 id="ReelStageTitle" class="text-xs font-bold text-white line-clamp-1">Fix Grey Hair, Dandruff, Fall' + content[title_end:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('SET FIX GREY HAIR AS REEL 01 IN:', fpath)
