/**
 * BlackRoots Ultra-Smooth "Butter" Instant Navigation & Pre-fetch Engine
 * 0-Lag Mobile & Desktop Page Transition Booster
 */
(function() {
  'use strict';

  // 1. In-memory prefetch cache
  const prefetchedUrls = new Set();

  function prefetchUrl(url) {
    if (!url || prefetchedUrls.has(url)) return;
    if (url.startsWith('#') || url.startsWith('javascript:') || url.startsWith('mailto:') || url.startsWith('tel:') || url.startsWith('http://') || url.startsWith('https://')) {
      return;
    }
    
    prefetchedUrls.add(url);

    // High performance link prefetch tag
    const link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = url;
    link.as = 'document';
    document.head.appendChild(link);

    // Warm up HTTP cache with low-priority fetch
    if (window.fetch) {
      try {
        fetch(url, { priority: 'low', credentials: 'same-origin' }).catch(function() {});
      } catch (e) {}
    }
  }

  // 2. Pre-warm key core pages when idle
  function prewarmCorePages() {
    const corePages = ['product.html', 'reviews.html', 'ingredients.html', 'how-to-use.html', 'ai-consultant.html', 'track-order.html', 'contact.html', 'index.html'];
    const current = window.location.pathname.split('/').pop() || 'index.html';
    
    corePages.forEach(function(page) {
      if (page !== current) {
        if ('requestIdleCallback' in window) {
          requestIdleCallback(function() { prefetchUrl(page); }, { timeout: 2000 });
        } else {
          setTimeout(function() { prefetchUrl(page); }, 800);
        }
      }
    });
  }

  // 3. Instant Touch & Hover Listeners
  function initInstantListeners() {
    // Touchstart: user finger touches the screen (gives ~150ms-300ms headstart before click)
    document.addEventListener('touchstart', function(e) {
      const a = e.target.closest('a');
      if (a && a.getAttribute('href')) {
        prefetchUrl(a.getAttribute('href'));
      }
    }, { passive: true, capture: true });

    // Mouseover / Pointerenter on desktop (gives ~100ms headstart)
    document.addEventListener('pointerenter', function(e) {
      const a = e.target.closest('a');
      if (a && a.getAttribute('href')) {
        prefetchUrl(a.getAttribute('href'));
      }
    }, { passive: true, capture: true });

    // 4. Viewport Intersection Observer: prefetch links as they scroll into view
    if ('IntersectionObserver' in window) {
      const linkObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            const href = entry.target.getAttribute('href');
            if (href) prefetchUrl(href);
            linkObserver.unobserve(entry.target);
          }
        });
      }, { rootMargin: '100px' });

      document.querySelectorAll('a[href]:not([href^="#"]):not([href^="http"]):not([href^="mailto"])').forEach(function(el) {
        linkObserver.observe(el);
      });
    }
  }

  // 5. CSS Hardware-accelerated Smooth Page Transition & View Transition API
  const style = document.createElement('style');
  style.textContent = `
    @view-transition {
      navigation: auto;
    }
    html {
      scroll-behavior: smooth;
    }
    body {
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      animation: smoothPageFadeIn 0.18s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes smoothPageFadeIn {
      0% {
        opacity: 0.88;
        transform: translateZ(0);
      }
      100% {
        opacity: 1;
        transform: translateZ(0);
      }
    }
  `;
  document.head.appendChild(style);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initInstantListeners();
      prewarmCorePages();
    });
  } else {
    initInstantListeners();
    prewarmCorePages();
  }

})();
