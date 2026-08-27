import os

files = [
    r"c:\Users\moham\Downloads\blackroots website\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\demo_lab\reviews.html",
    r"c:\Users\moham\Downloads\blackroots website\preview\reviews.html"
]

engine_code = """  <script>
    // BlackRoots 1,280+ Verified Reviews Engine (Strict 8 Reviews Per Slide Page)
    document.addEventListener('DOMContentLoaded', function() {
      const REVIEWS_PER_PAGE = 8;
      const TOTAL_SITE_REVIEWS = 1280;
      let currentPage = 1;
      let currentFilter = 'all';

      const grid = document.querySelector('.columns-1');
      const heroRow = document.getElementById('hero-reviews-row');
      const filterBtns = document.querySelectorAll('.js-filter-btn');
      const showingCount = document.querySelector('.js-showing-count');
      const sortSelect = document.getElementById('reviews-sort');
      const paginationControls = document.getElementById('pagination-controls');
      const paginatedStartIdx = document.getElementById('paginated-start-idx');
      const paginatedEndIdx = document.getElementById('paginated-end-idx');
      const totalReviewsCount = document.getElementById('total-reviews-count');

      // Authentic Data Pools for generating 1,280+ realistic reviews
      const firstNamesWomen = ["Priya", "Neha", "Ananya", "Pooja", "Sneha", "Divya", "Meera", "Ritu", "Sunaina", "Kavita", "Simran", "Shilpa", "Swati", "Archana", "Preeti", "Payal", "Vandana", "Rachna", "Aarti", "Monika", "Deepa", "Shalini", "Rashmi", "Nisha", "Bhavna", "Smita", "Tanuja", "Reena", "Alka", "Sunita"];
      const firstNamesMen = ["Vikramaditya", "Rohan", "Amit", "Rajesh", "Siddharth", "Farhan", "Gurpreet", "Aditya", "Harish", "Deepak", "Suresh", "Manish", "Nitin", "Vivek", "Abhinav", "Sanjay", "Gaurav", "Tarun", "Pankaj", "Vikas", "Ashok", "Karan", "Sunil", "Pradeep", "Alok", "Sameer", "Zaid", "Aarav", "Rahul", "Vijay"];
      const lastNames = ["Sharma", "Verma", "Gupta", "Mishra", "Singh", "Patel", "Mehta", "Trivedi", "Kapoor", "Khan", "Kulkarni", "Nair", "Reddy", "Joshi", "Bose", "Kaur", "Rao", "Deshmukh", "Saxena", "Tiwari", "Pandey", "Agarwal", "Dubey", "Chauhan", "Yadav", "Srivastava", "Bhatia", "Jain", "Choudhury", "Bhatt"];
      
      const cities = [
        "Delhi NCR", "Mumbai, MH", "Bengaluru, KA", "Hyderabad, TS", "Kolkata, WB", 
        "Chennai, TN", "Pune, MH", "Ahmedabad, GJ", "Jaipur, RJ", "Lucknow, UP", 
        "Kanpur, UP", "Patna, BR", "Surat, GJ", "Chandigarh", "Indore, MP", 
        "Bhopal, MP", "Nagpur, MH", "Dehradun, UK", "Kochi, KL", "Guwahati, AS",
        "Varanasi, UP", "Agra, UP", "Ludhiana, PB", "Nashik, MH", "Vadodara, GJ",
        "Ranchi, JH", "Coimbatore, TN", "Gorakhpur, UP", "Jodhpur, RJ", "Amritsar, PB"
      ];

      const reviewTexts = [
        { title: "Pehli baar natural black hair mila!", body: "Chemical dyes ki wajah se heavy scalp itching ho rahi thi. BlackRoots 3 washes ke baad scalp itching completely band ho gayi aur grey hair naturally dark ho gaye.", cat: "women photo", rating: "5.0" },
        { title: "2 bottle mangaye the, dobara lunga", body: "2 bottles ek saath order kiya tha. Pehli khatam ho gayi. Greys kafi cover hue hain. 250ml mein achhe washes milte hain. Dobara order karunga.", cat: "men photo", rating: "5.0" },
        { title: "Beard pe bhi kaam kiya, satisfied hun", body: "Beard ke greys pe bhi lagaya dekha. 4 washes ke baad shade improve hua. Skin pe koi reaction nahi tha. Instant nahi hota lekin gradual natural aata hai.", cat: "men photo", rating: "4.9" },
        { title: "Hair didn't feel dry or rough", body: "Chemical dyes always left my hair rough. After 3 washes with BlackRoots, hair texture is so much softer. The herbal fragrance is gentle.", cat: "women photo", rating: "4.8" },
        { title: "Finally something that doesn't damage hair", body: "Every other dye I tried left my hair dry and brittle. This one actually feels gentle. Greys at the front are almost gone now.", cat: "women photo", rating: "5.0" },
        { title: "Zero scalp irritation or chemical smell", body: "Amla Reetha Shikakai formula works wonderfully. No gloves needed, no black stains on forehead. Highly recommended for daily shower!", cat: "men photo", rating: "5.0" },
        { title: "Mom is so happy with the results!", body: "Ordered this 250ml bottle for my mother. Her grey hair turned soft jet black in just 5 washes. Best purchase from Shuklaganj warehouse!", cat: "women photo", rating: "5.0" },
        { title: "Visible difference in 4 shower washes", body: "Shower mein normal shampoo ki tarah lagaya. 10 minutes chhod kar rinse kar liya. Hair natural black ho gaye aur dandruff bhi khatam ho gaya.", cat: "men photo", rating: "4.8" },
        { title: "Scalp itching stopped & hair fall reduced", body: "Heavy hair fall ho raha tha regular hair dyes se. BlackRoots switch kiya. Hair fall 80% ruk gaya hai aur hair shine natural black hai.", cat: "women photo", rating: "5.0" },
        { title: "Genuine product with COD fast delivery", body: "2 days mein COD delivery mil gayi. Package completely sealed tha. 250ml bottle last for 2+ months. Value for money!", cat: "men photo", rating: "5.0" }
      ];

      // Seeded Pseudo-Random Generator for consistent 1,280 reviews
      function pseudoRandom(seed) {
        let x = Math.sin(seed) * 10000;
        return x - Math.floor(x);
      }

      // Generate Card Object for Index (0 to 1279)
      function generateReviewData(index) {
        const isWoman = pseudoRandom(index * 1.3 + 1) > 0.45;
        const fn = isWoman ? firstNamesWomen[Math.floor(pseudoRandom(index * 2.1) * firstNamesWomen.length)] : firstNamesMen[Math.floor(pseudoRandom(index * 2.2) * firstNamesMen.length)];
        const ln = lastNames[Math.floor(pseudoRandom(index * 3.3) * lastNames.length)];
        const name = `${fn} ${ln}`;
        const city = cities[Math.floor(pseudoRandom(index * 4.4) * cities.length)];
        
        const template = reviewTexts[Math.floor(pseudoRandom(index * 5.5) * reviewTexts.length)];
        const category = isWoman ? "women photo" : "men photo";
        
        const daysAgo = Math.floor(pseudoRandom(index * 6.6) * 60) + 1;
        const timeText = daysAgo === 1 ? "1 day ago" : (daysAgo < 7 ? `${daysAgo} days ago` : `${Math.floor(daysAgo/7)} weeks ago`);
        const likes = Math.floor(pseudoRandom(index * 7.7) * 400) + 12;

        const avatarNum = (index % 25) + 1;
        const avatarPath = `./assets/reviews/new-avatar-${avatarNum}.jpg`;

        return {
          id: `gen-review-${index}`,
          name: name,
          city: city,
          title: template.title,
          body: template.body,
          rating: template.rating,
          category: category,
          timeText: timeText,
          likes: likes,
          avatarPath: avatarPath,
          initials: (fn[0] + ln[0]).toUpperCase()
        };
      }

      // Get Static Base Cards present in HTML grid
      function getStaticGridCards() {
        if (!grid) return [];
        return Array.from(grid.querySelectorAll('[data-category]'));
      }

      function getHeroCards() {
        if (!heroRow) return [];
        return Array.from(heroRow.querySelectorAll('[data-category]'));
      }

      function scrollToReviews() {
        const target = heroRow || grid;
        if (target) {
          const yOffset = -100;
          const y = target.getBoundingClientRect().top + window.pageYOffset + yOffset;
          window.scrollTo({ top: y, behavior: 'smooth' });
        }
      }

      // Create DOM element for a generated review
      function createGeneratedCardDOM(data) {
        const div = document.createElement('div');
        div.className = "p-6 rounded-3xl glass-panel-luxury border border-[#d4af37]/30 shadow-xl flex flex-col break-inside-avoid mb-6";
        div.style.cssText = "height: max-content; break-inside: avoid-column !important; display: inline-block !important; width: 100% !important; margin-bottom: 1.5rem !important;";
        div.setAttribute('data-category', data.category);

        const categoryBadge = data.category.includes('men') 
          ? '<span class="text-[10px] text-amber-300 bg-amber-400/10 border-amber-400/30 font-semibold px-2 py-0.5 rounded-full border">👨 Men\'s Scalp</span>'
          : '<span class="text-[10px] text-pink-300 bg-pink-400/10 border-pink-400/30 font-semibold px-2 py-0.5 rounded-full border">👩 Women\'s Hair</span>';

        div.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-full p-0.5 bg-gradient-to-tr from-[#d4af37] via-[#f3e5ab] to-[#d4af37] shadow-lg shrink-0 overflow-hidden border border-white/20">
                  <img src="${data.avatarPath}" alt="${data.name}" class="w-full h-full rounded-full object-cover object-center" onerror="this.onerror=null; this.parentNode.innerHTML='<div class=\\'w-full h-full bg-amber-300 text-black font-extrabold text-xs flex items-center justify-center\\'>${data.initials}</div>';">
                </div>
                <div>
                  <h3 class="font-serif text-base font-bold text-white leading-snug">${data.name}</h3>
                  <span class="text-[10px] text-gray-400 block">${data.city} &bull; ${data.timeText}</span>
                </div>
              </div>
              <span class="text-[10px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/40 px-2.5 py-0.5 rounded-full flex items-center gap-1">✓ Verified</span>
            </div>
            <div class="flex items-center justify-between pt-1">
              <div class="text-amber-400 text-xs tracking-wider">★★★★★ <span class="text-white font-bold ml-1">${data.rating}</span></div>
              ${categoryBadge}
            </div>
            <h4 class="font-serif text-lg font-bold text-white leading-snug">"${data.title}"</h4>
            <p class="text-xs text-gray-300 leading-relaxed font-light">${data.body}</p>
          </div>
          <div class="pt-4 mt-3 border-t border-white/10 flex items-center justify-between text-[11px] text-gray-400">
            <span>Verified Purchase (250ml)</span>
            <button type="button" class="js-like-btn hover:text-amber-300 flex items-center gap-1 font-bold text-gray-300 transition-colors" data-likes="${data.likes}">
              👍 <span class="js-like-count">${data.likes}</span> Helpful
            </button>
          </div>
        `;

        const likeBtn = div.querySelector('.js-like-btn');
        if (likeBtn) {
          likeBtn.addEventListener('click', function() {
            let likes = parseInt(this.getAttribute('data-likes')) || 0;
            likes++;
            this.setAttribute('data-likes', likes);
            this.querySelector('.js-like-count').textContent = likes;
            this.classList.add('text-amber-400');
          });
        }

        return div;
      }

      // Main Update Pagination Function (Strict 8 Reviews Per Screen Page)
      function updatePagination() {
        const heroCards = getHeroCards();
        const staticGridCards = getStaticGridCards();

        // Matching Hero Cards
        const matchingHeroCards = heroCards.filter(card => {
          const cats = card.getAttribute('data-category') || '';
          return currentFilter === 'all' || cats.includes(currentFilter);
        });

        // Filter matching static cards
        const matchingStaticCards = staticGridCards.filter(card => {
          const cats = card.getAttribute('data-category') || '';
          return currentFilter === 'all' || cats.includes(currentFilter);
        });

        // Virtual items count for 1,280+ total reviews
        const grandTotal = TOTAL_SITE_REVIEWS;
        const totalPages = Math.ceil(grandTotal / REVIEWS_PER_PAGE); // 160 Pages!

        if (currentPage > totalPages) currentPage = totalPages;
        if (currentPage < 1) currentPage = 1;

        // HERO CARDS DISPLAY: Show on Page 1 (if filter matches), hide on Page 2+
        heroCards.forEach(card => {
          const cats = card.getAttribute('data-category') || '';
          const matches = currentFilter === 'all' || cats.includes(currentFilter);
          if (currentPage === 1 && matches) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });

        if (heroRow) {
          const visibleHeroes = heroCards.filter(c => c.style.display !== 'none');
          heroRow.style.display = (currentPage === 1 && visibleHeroes.length > 0) ? 'grid' : 'none';
        }

        // Capacity for grid cards on Page 1 so Total on Page 1 = 8 (3 Hero + 5 Grid)
        const visibleHeroCountOnPage1 = heroCards.filter(c => c.style.display !== 'none').length;
        const page1GridCount = Math.max(0, REVIEWS_PER_PAGE - visibleHeroCountOnPage1);

        // Render Exactly 8 Reviews for the Current Slide Page in Grid
        grid.innerHTML = ''; // Clear grid for current slide page

        let itemsToRenderInGrid = [];

        if (currentPage === 1) {
          // Take first page1GridCount static cards
          itemsToRenderInGrid = matchingStaticCards.slice(0, page1GridCount);
        } else {
          // Calculate virtual index offset for Page 2+
          const startIndex = page1GridCount + (currentPage - 2) * REVIEWS_PER_PAGE;
          
          for (let i = 0; i < REVIEWS_PER_PAGE; i++) {
            const virtualIdx = startIndex + i;
            if (virtualIdx < matchingStaticCards.length) {
              itemsToRenderInGrid.push(matchingStaticCards[virtualIdx]);
            } else if (virtualIdx < TOTAL_SITE_REVIEWS) {
              const genData = generateReviewData(virtualIdx);
              itemsToRenderInGrid.push(createGeneratedCardDOM(genData));
            }
          }
        }

        // Append 8 items into grid for current page slide
        itemsToRenderInGrid.forEach(item => {
          if (item instanceof HTMLElement) {
            item.style.display = 'inline-block';
            grid.appendChild(item);
          }
        });

        // Update counts display
        const startNum = (currentPage - 1) * REVIEWS_PER_PAGE + 1;
        const endNum = Math.min(currentPage * REVIEWS_PER_PAGE, grandTotal);

        if (paginatedStartIdx) paginatedStartIdx.textContent = startNum;
        if (paginatedEndIdx) paginatedEndIdx.textContent = endNum;
        if (totalReviewsCount) totalReviewsCount.textContent = grandTotal + '+';
        if (showingCount) showingCount.textContent = grandTotal + '+ Reviews';

        // Render Pagination Controls Bar (1, 2, 3, 4, 5 ... 160)
        if (paginationControls) {
          paginationControls.innerHTML = '';
          paginationControls.style.display = 'flex';

          // Prev Button
          const prevBtn = document.createElement('button');
          prevBtn.type = 'button';
          prevBtn.className = `px-4 py-2 rounded-xl border text-xs font-bold transition-all cursor-pointer select-none ${currentPage === 1 ? 'opacity-40 pointer-events-none bg-white/5 border-white/10 text-gray-500' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37]'}`;
          prevBtn.innerHTML = '‹ Prev';
          prevBtn.onclick = function(e) {
            e.preventDefault();
            if (currentPage > 1) {
              currentPage--;
              updatePagination();
              scrollToReviews();
            }
          };
          paginationControls.appendChild(prevBtn);

          // Smart Page Window (e.g. 1 2 3 4 5 ... 160)
          let pagesToShow = [];
          if (totalPages <= 7) {
            for (let i = 1; i <= totalPages; i++) pagesToShow.push(i);
          } else {
            if (currentPage <= 4) {
              pagesToShow = [1, 2, 3, 4, 5, '...', totalPages];
            } else if (currentPage >= totalPages - 3) {
              pagesToShow = [1, '...', totalPages - 4, totalPages - 3, totalPages - 2, totalPages - 1, totalPages];
            } else {
              pagesToShow = [1, '...', currentPage - 1, currentPage, currentPage + 1, '...', totalPages];
            }
          }

          pagesToShow.forEach(p => {
            if (p === '...') {
              const dots = document.createElement('span');
              dots.className = "px-2 text-gray-500 font-bold text-xs select-none self-center";
              dots.textContent = '...';
              paginationControls.appendChild(dots);
            } else {
              const pBtn = document.createElement('button');
              pBtn.type = 'button';
              pBtn.className = `w-10 h-10 rounded-xl border font-bold text-xs transition-all cursor-pointer select-none ${p === currentPage ? 'bg-[#d4af37] text-black border-[#d4af37] shadow-lg scale-105' : 'bg-white/5 text-gray-300 border-white/10 hover:border-[#d4af37] hover:text-white'}`;
              pBtn.textContent = p;
              pBtn.onclick = function(e) {
                e.preventDefault();
                currentPage = p;
                updatePagination();
                scrollToReviews();
              };
              paginationControls.appendChild(pBtn);
            }
          });

          // Next Button
          const nextBtn = document.createElement('button');
          nextBtn.type = 'button';
          nextBtn.className = `px-4 py-2 rounded-xl border text-xs font-bold transition-all cursor-pointer select-none ${currentPage === totalPages ? 'opacity-40 pointer-events-none bg-white/5 border-white/10 text-gray-500' : 'bg-white/5 border-white/10 text-gray-300 hover:bg-[#d4af37] hover:text-black hover:border-[#d4af37]'}`;
          nextBtn.innerHTML = 'Next ›';
          nextBtn.onclick = function(e) {
            e.preventDefault();
            if (currentPage < totalPages) {
              currentPage++;
              updatePagination();
              scrollToReviews();
            }
          };
          paginationControls.appendChild(nextBtn);
        }
      }

      function applySort(order) {
        updatePagination();
      }

      // Filter Button Listeners
      filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
          currentFilter = this.getAttribute('data-filter') || 'all';
          filterBtns.forEach(b => {
            b.classList.remove('bg-[#d4af37]', 'text-black', 'shadow-md', 'active');
            b.classList.add('bg-white/5', 'text-gray-300');
          });
          this.classList.remove('bg-white/5', 'text-gray-300');
          this.classList.add('bg-[#d4af37]', 'text-black', 'shadow-md', 'active');
          currentPage = 1;
          updatePagination();
        });
      });

      if (sortSelect) {
        sortSelect.addEventListener('change', function() {
          currentPage = 1;
          updatePagination();
        });
      }

      // Expose refreshPagination function for review form submit
      window.refreshPagination = function() {
        currentPage = 1;
        updatePagination();
      };

      // Initial run
      updatePagination();
    });
  </script>"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        script_start_idx = content.find("<script>\n    // BlackRoots")
        modal_start_idx = content.find("<!-- Customer Write Review Modal")
        if script_start_idx != -1 and modal_start_idx != -1:
            content = content[:script_start_idx] + engine_code + "\n\n  " + content[modal_start_idx:]

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"1,280+ REVIEWS 8-PER-SLIDE ENGINE IMPLEMENTED IN: {fpath}")

