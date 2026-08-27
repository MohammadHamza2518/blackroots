import os
import re

root_dir = r"c:\Users\moham\Downloads\blackroots website"

estimator_script = """
  <!-- ⚡ Interactive Live Result Timeline Estimator Engine -->
  <script>
    (function() {
      let selectedAge = 'mid';
      let selectedGrey = 'moderate';

      const timelineData = {
        'young': {
          'light': {
            days: '3 – 5 Days',
            text: 'Younger hair follicles actively absorb Japanese Indigo Leaf & Amla extract instantly. You will notice visible deep black roots within just <strong>3–5 shower applications</strong>.'
          },
          'moderate': {
            days: '7 – 10 Days',
            text: 'Active herbal nourishment deeply coats emerging greys. Within <strong>7–10 days</strong>, your entire hair transitions into a uniform, natural glossy black tone.'
          },
          'heavy': {
            days: '10 – 14 Days',
            text: 'High concentration of botanical pigment penetrates denser grey strands. Complete natural black coverage achieved within <strong>10–14 days</strong>.'
          }
        },
        'mid': {
          'light': {
            days: '5 – 7 Days',
            text: 'Direct herbal pigmentation targets early silver strands. Melanin revitalizes roots within <strong>5–7 daily shower washes</strong>.'
          },
          'moderate': {
            days: '10 – 14 Days',
            text: 'Japanese Indigo Leaf & Amla melanin boost karenge. Regular shower washes ke sath <strong>10–14 days</strong> me roots naturally dark black shade me convert ho jayengi.'
          },
          'heavy': {
            days: '14 – 18 Days',
            text: 'Deep root penetration strengthens mature hair shafts. Natural jet-black coverage with zero ammonia within <strong>14–18 days</strong>.'
          }
        },
        'senior': {
          'light': {
            days: '7 – 10 Days',
            text: 'Gentle botanical conditioning restores youthful luster to grey patches within <strong>7–10 days</strong>.'
          },
          'moderate': {
            days: '12 – 16 Days',
            text: 'Deep herbal saturation replenishes natural shine and deposits rich black pigment within <strong>12–16 days</strong>.'
          },
          'heavy': {
            days: '16 – 21 Days',
            text: 'Comprehensive follicular nourishment. Even stubborn, coarse grey hair turns rich natural black within <strong>16–21 days</strong> with daily 3-min shower massage.'
          }
        }
      };

      const activeClasses = ['bg-gradient-to-r', 'from-[#d4af37]', 'to-[#aa7c11]', 'text-black', 'border-[#fff3b0]', 'font-black', 'shadow-lg'];
      const inactiveClasses = ['bg-white/5', 'border-white/15', 'text-white', 'font-bold'];

      function updateEstimatorUI() {
        // Update Age Pills
        ['young', 'mid', 'senior'].forEach(function(ageKey) {
          const btn = document.getElementById('AgePill_' + ageKey);
          if (!btn) return;
          if (ageKey === selectedAge) {
            btn.className = 'js-age-pill py-2.5 px-2 rounded-xl bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black border border-[#fff3b0] text-center text-xs font-black shadow-lg transition-all cursor-pointer transform scale-[1.02]';
          } else {
            btn.className = 'js-age-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer';
          }
        });

        // Update Grey Pills
        ['light', 'moderate', 'heavy'].forEach(function(greyKey) {
          const btn = document.getElementById('GreyPill_' + greyKey);
          if (!btn) return;
          if (greyKey === selectedGrey) {
            btn.className = 'js-grey-pill py-2.5 px-2 rounded-xl bg-gradient-to-r from-[#d4af37] to-[#aa7c11] text-black border border-[#fff3b0] text-center text-xs font-black shadow-lg transition-all cursor-pointer transform scale-[1.02]';
          } else {
            btn.className = 'js-grey-pill py-2.5 px-2 rounded-xl bg-white/5 border border-white/15 text-center text-xs font-bold text-white hover:border-[#d4af37]/60 transition-all cursor-pointer';
          }
        });

        // Update Result Display with subtle animation
        const res = (timelineData[selectedAge] && timelineData[selectedAge][selectedGrey]) || timelineData['mid']['moderate'];
        const badge = document.getElementById('SimpleDaysBadge');
        const text = document.getElementById('SimpleResultText');

        if (badge) {
          badge.style.opacity = '0.5';
          setTimeout(function() {
            badge.textContent = res.days;
            badge.style.opacity = '1';
          }, 100);
        }
        if (text) {
          text.style.opacity = '0.5';
          setTimeout(function() {
            text.innerHTML = res.text;
            text.style.opacity = '1';
          }, 100);
        }
      }

      window.pickAge = function(age) {
        selectedAge = age;
        updateEstimatorUI();
      };

      window.pickGrey = function(grey) {
        selectedGrey = grey;
        updateEstimatorUI();
      };

      document.addEventListener('DOMContentLoaded', function() {
        updateEstimatorUI();
      });
    })();
  </script>
"""

files = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "demo_lab", "index.html"),
    os.path.join(root_dir, "preview", "index.html")
]

for fpath in files:
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any old estimator script if present
    content = re.sub(r'<!-- ⚡ Interactive Live Result Timeline Estimator Engine -->.*?<\/script>', '', content, flags=re.DOTALL)

    new_content = content.replace('</body>', estimator_script + '\n</body>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Injected Live Result Estimator Engine into", fpath)

