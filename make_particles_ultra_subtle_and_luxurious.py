import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

ultra_subtle_particles_js = """/* ✨ Luxury Ultra-Subtle Golden Dust Micro-Particles (Behind Text, Pure Ambient) */
function initParticleCanvas() {
  const canvas = document.getElementById('ParticleCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  function resize() {
    if (!canvas.parentElement) return;
    canvas.width = canvas.parentElement.offsetWidth || window.innerWidth || 393;
    canvas.height = canvas.parentElement.offsetHeight || window.innerHeight || 600;
  }

  resize();
  setTimeout(resize, 100);
  setTimeout(resize, 400);
  window.addEventListener('resize', resize);

  const particles = [];
  const particleCount = 35;
  const colors = ['#d4af37', '#f5e4ab', '#fbbf24'];

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * (canvas.width || 400),
      y: Math.random() * (canvas.height || 600),
      radius: Math.random() * 2 + 1, // Tiny micro-orbs (1px to 3px)
      speedY: Math.random() * 0.4 + 0.1,
      speedX: (Math.random() - 0.5) * 0.2,
      color: colors[Math.floor(Math.random() * colors.length)],
      opacity: Math.random() * 0.35 + 0.1 // Very soft, non-intrusive ambient glow
    });
  }

  function animate() {
    const width = canvas.width || window.innerWidth || 400;
    const height = canvas.height || window.innerHeight || 600;
    
    ctx.clearRect(0, 0, width, height);

    particles.forEach(p => {
      p.y -= p.speedY;
      p.x += p.speedX;

      if (p.y < -10) {
        p.y = height + 10;
        p.x = Math.random() * width;
      }
      if (p.x > width + 10) p.x = -5;
      if (p.x < -10) p.x = width + 5;

      ctx.save();
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.opacity;
      ctx.fill();
      ctx.restore();
    });

    requestAnimationFrame(animate);
  }

  animate();
}"""

for jspath in theme_js_files:
    if os.path.exists(jspath):
        with open(jspath, 'r', encoding='utf-8') as f:
            content = f.read()

        p_idx = content.find('function initParticleCanvas()')
        if p_idx != -1:
            e_idx = content.find('function ', p_idx + 30)
            if e_idx == -1:
                e_idx = content.find('/* ', p_idx + 30)
            if e_idx != -1:
                content = content[:p_idx] + ultra_subtle_particles_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED ULTRA-SUBTLE PARTICLES JS IN: {jspath}")

# Remove harsh CSS HTML blobs and keep clean Canvas behind text
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove harsh CSS overlay blobs
        b_start = content.find('<!-- Glowing Floating Golden Bubbles Overlay -->')
        if b_start != -1:
            b_end = content.find('<canvas id="ParticleCanvas"', b_start)
            if b_end != -1:
                content = content[:b_start] + content[b_end:]

        # Set canvas to z-0 so it sits BEHIND text
        content = content.replace('id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-15 w-full h-full"', 'id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-0 w-full h-full"')
        content = content.replace('id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-10 w-full h-full"', 'id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-0 w-full h-full"')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"CLEANED HARSH BLOBS AND MOVED CANVAS BEHIND TEXT IN: {fpath}")
