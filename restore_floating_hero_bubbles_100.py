import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

glowing_particles_js = """/* ✨ Guaranteed Rich Floating Golden Bubble Particle Engine */
function initParticleCanvas() {
  const canvas = document.getElementById('ParticleCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  function resize() {
    if (!canvas.parentElement) return;
    const w = canvas.parentElement.offsetWidth || window.innerWidth || 393;
    const h = canvas.parentElement.offsetHeight || window.innerHeight || 600;
    canvas.width = w;
    canvas.height = h;
  }

  resize();
  setTimeout(resize, 100);
  setTimeout(resize, 500);
  window.addEventListener('resize', resize);

  const particles = [];
  const particleCount = 40;
  const colors = ['#d4af37', '#f3e5ab', '#34d399', '#fbbf24'];

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * (canvas.width || 400),
      y: Math.random() * (canvas.height || 600),
      radius: Math.random() * 4 + 2,
      speedY: Math.random() * 0.6 + 0.2,
      speedX: (Math.random() - 0.5) * 0.4,
      color: colors[Math.floor(Math.random() * colors.length)],
      opacity: Math.random() * 0.7 + 0.2,
      pulse: Math.random() * 0.02 + 0.005
    });
  }

  function animate() {
    const width = canvas.width || window.innerWidth || 400;
    const height = canvas.height || window.innerHeight || 600;
    
    ctx.clearRect(0, 0, width, height);

    particles.forEach(p => {
      p.y -= p.speedY;
      p.x += p.speedX;
      p.opacity += Math.sin(Date.now() * p.pulse) * 0.005;

      if (p.y < -15) {
        p.y = height + 15;
        p.x = Math.random() * width;
      }
      if (p.x > width + 15) p.x = -10;
      if (p.x < -15) p.x = width + 10;

      ctx.save();
      ctx.beginPath();
      const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius * 2);
      grad.addColorStop(0, p.color);
      grad.addColorStop(1, 'transparent');
      ctx.fillStyle = grad;
      ctx.globalAlpha = Math.max(0.2, Math.min(0.9, p.opacity));
      ctx.arc(p.x, p.y, p.radius * 2.2, 0, Math.PI * 2);
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
                content = content[:p_idx] + glowing_particles_js + "\n\n" + content[e_idx:]
                with open(jspath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"UPGRADED GUARANTEED BUBBLE PARTICLES JS IN: {jspath}")

# HTML Files Update
html_files = [
    r"c:\Users\moham\Downloads\blackroots website\index.html",
    r"c:\Users\moham\Downloads\blackroots website\product.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\index.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\index.html"
]

hero_bubbles_html = """    <!-- Glowing Floating Golden Bubbles Overlay -->
    <div class="absolute inset-0 z-10 pointer-events-none overflow-hidden">
      <div class="absolute top-1/4 left-8 w-4 h-4 rounded-full bg-[#d4af37]/60 blur-[1px] animate-bounce duration-[3000ms]"></div>
      <div class="absolute top-1/3 right-12 w-6 h-6 rounded-full bg-emerald-400/50 blur-[2px] animate-pulse duration-[2500ms]"></div>
      <div class="absolute bottom-1/4 left-1/5 w-5 h-5 rounded-full bg-amber-300/60 blur-[1px] animate-bounce duration-[4000ms]"></div>
      <div class="absolute bottom-1/3 right-1/4 w-3 h-3 rounded-full bg-[#d4af37]/70 blur-none animate-pulse duration-[2000ms]"></div>
      <div class="absolute top-1/2 left-1/3 w-7 h-7 rounded-full bg-[#d4af37]/30 blur-[2px] animate-pulse duration-[3500ms]"></div>
      <div class="absolute top-1/5 right-1/3 w-4 h-4 rounded-full bg-emerald-500/50 blur-[1px] animate-bounce duration-[2800ms]"></div>
    </div>
    
    <canvas id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-15 w-full h-full"></canvas>"""

for fpath in html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'id="ParticleCanvas"' in content:
            c_start = content.find('<canvas id="ParticleCanvas"')
            c_end = content.find('</canvas>', c_start)
            if c_start != -1 and c_end != -1:
                content = content[:c_start] + hero_bubbles_html + content[c_end+9:]
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"ADDED GUARANTEED HERO BUBBLES TO: {fpath}")
