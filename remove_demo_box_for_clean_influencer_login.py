import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\influencer.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\influencer.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\influencer.html"
]

demo_box_snippet = """      <!-- Quick Demo Credentials Hint Box -->
      <div class="p-3.5 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-xs space-y-1.5">
        <div class="font-bold text-amber-300 flex items-center justify-between">
          <span>⚡ Demo Creator Account:</span>
          <button type="button" onclick="fillDemoCredentials()" class="text-[10px] uppercase font-extrabold bg-[#d4af37] text-black px-2.5 py-1 rounded cursor-pointer hover:bg-amber-400 shadow-md">Auto Fill Login</button>
        </div>
        <div class="text-[11px] text-gray-300 font-mono flex items-center gap-3">
          <span>User ID: <strong class="text-white">priya</strong></span>
          <span>Password: <strong class="text-white">priya123</strong></span>
          <span>Code: <strong class="text-amber-300">PRIYA10</strong></span>
        </div>
      </div>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if demo_box_snippet in content:
            content = content.replace(f"{demo_box_snippet}\n", "")
            content = content.replace(demo_box_snippet, "")

        # Also fallback regex or clean string replace
        if "⚡ Demo Creator Account:" in content:
            idx = content.find('<!-- Quick Demo Credentials Hint Box -->')
            if idx != -1:
                end_idx = content.find('</div>\n\n      <!-- Login Form -->', idx)
                if end_idx != -1:
                    content = content[:idx] + content[end_idx + 6:]
                else:
                    end_idx2 = content.find('</div>', content.find('PRIYA10', idx))
                    if end_idx2 != -1:
                        content = content[:idx] + content[end_idx2 + 6:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"REMOVED DEMO CREATOR HINT BOX FROM: {fpath}")

