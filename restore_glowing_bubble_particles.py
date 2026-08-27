import os

theme_js_files = [
    r"c:\Users\moham\Downloads\blackroots website\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\assets\theme.js",
    r"c:\Users\moham\Downloads\blackroots website\preview\assets\theme.js"
]

glowing_particles_js = """/* ✨ Rich Floating Golden Bubble Particle Engine */
function initParticleCanvas() {
  const canvas = document.getElementById('ParticleCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  function resize() {
    canvas.width = canvas.parentElement ? canvas.parentElement.offsetWidth : window.innerWidth;
    canvas.height = canvas.parentElement ? canvas.parentElement.offsetHeight : window.innerHeight;
  }

  resize();
  window.addEventListener('resize', resize);

  const particles = [];
  const particleCount = 45;

  const colors = ['#d4af37', '#f3e5ab', '#34d399', '#fbbf24'];

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * (canvas.width || window.innerWidth),
      y: Math.random() * (canvas.height || window.innerHeight),
      radius: Math.random() * 5 + 2,
      speedY: Math.random() * 0.7 + 0.2,
      speedX: (Math.random() - 0.5) * 0.4,
      color: colors[Math.floor(Math.random() * colors.length)],
      opacity: Math.random() * 0.6 + 0.25,
      pulse: Math.random() * 0.02 + 0.005
    });
  }

  function animate() {
    const width = canvas.width || window.innerWidth;
    const height = canvas.height || window.innerHeight;
    
    ctx.clearRect(0, 0, width, height);

    particles.forEach(p => {
      p.y -= p.speedY; // Float upwards softly
      p.x += p.speedX;
      p.opacity += Math.sin(Date.now() * p.pulse) * 0.005;

      if (p.y < -20) {
        p.y = height + 20;
        p.x = Math.random() * width;
      }
      if (p.x > width + 20) p.x = -10;
      if (p.x < -20) p.x = width + 10;

      // Draw Glowing Particle Bubble
      ctx.save();
      ctx.beginPath();
      
      const grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius * 2);
      grad.addColorStop(0, p.color);
      grad.addColorStop(1, 'transparent');
      
      ctx.fillStyle = grad;
      ctx.globalAlpha = Math.max(0.1, Math.min(0.9, p.opacity));
      ctx.arc(p.x, p.y, p.radius * 2.5, 0, Math.PI * 2);
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
                print(f"UPGRADED BUBBLE PARTICLES JS IN: {jspath}")

# Ensure ParticleCanvas tag in HTML has z-15 and w-full h-full
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

        if 'id="ParticleCanvas"' in content:
            content = content.replace('id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-10"', 'id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-15 w-full h-full"')
            content = content.replace('id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-0"', 'id="ParticleCanvas" class="absolute inset-0 pointer-events-none z-15 w-full h-full"')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"UPDATED PARTICLE CANVAS TAG IN: {fpath}")
