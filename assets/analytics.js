/**
 * BlackRoots Unified Analytics & Marketing Pixel Engine
 * Auto-injects Google Analytics 4 (GA4), Search Console, and Meta Pixel
 */
(function() {
  'use strict';

  function initMarketingStack(config) {
    if (!config) return;

    // 1. Google Search Console Meta Verification Tag
    if (config.gsc_verification_tag) {
      let gscTag = document.querySelector('meta[name="google-site-verification"]');
      if (!gscTag) {
        gscTag = document.createElement('meta');
        gscTag.name = 'google-site-verification';
        document.head.appendChild(gscTag);
      }
      gscTag.content = config.gsc_verification_tag;
    }

    // 2. Google Analytics 4 (GA4)
    if (config.ga4_measurement_id && !window.gtag_loaded) {
      window.gtag_loaded = true;
      const gaScript = document.createElement('script');
      gaScript.async = true;
      gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=' + config.ga4_measurement_id;
      document.head.appendChild(gaScript);

      window.dataLayer = window.dataLayer || [];
      function gtag(){ dataLayer.push(arguments); }
      window.gtag = gtag;
      gtag('js', new Date());
      gtag('config', config.ga4_measurement_id, {
        page_path: window.location.pathname
      });
    }

    // 3. Meta Pixel (Facebook & Instagram Ads)
    if (config.meta_pixel_id && !window.fbq_loaded) {
      window.fbq_loaded = true;
      !function(f,b,e,v,n,t,s)
      {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};
      if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
      n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t,s)}(window, document,'script',
      'https://connect.facebook.net/en_US/fbevents.js');
      
      fbq('init', config.meta_pixel_id);
      fbq('track', 'PageView');
    }
  }

  // Fetch public config from API or local cache
  function loadConfig() {
    fetch('/api/admin?action=get_public_config')
      .then(res => res.json())
      .then(config => {
        if (config) {
          localStorage.setItem('br_analytics_config', JSON.stringify(config));
          initMarketingStack(config);
        }
      })
      .catch(() => {
        const cached = localStorage.getItem('br_analytics_config');
        if (cached) {
          try { initMarketingStack(JSON.parse(cached)); } catch(e) {}
        }
      });
  }

  // Track standard E-Commerce Events Helper
  window.trackD2CEvent = function(eventName, data) {
    // GA4
    if (window.gtag) {
      window.gtag('event', eventName, data || {});
    }
    // Meta Pixel
    if (window.fbq) {
      window.fbq('track', eventName, data || {});
    }
  };

  // Automatic Real-Time Live Visitor Logger (Ultra Light-Speed sendBeacon & keepalive)
  function logLiveVisitor() {
    let sessionId = localStorage.getItem('br_session_id');
    if (!sessionId) {
      sessionId = 'br_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
      localStorage.setItem('br_session_id', sessionId);
      
      // Increment local total unique visitors
      let count = Number(localStorage.getItem('br_visitor_count') || 0) + 1;
      localStorage.setItem('br_visitor_count', count);
    }

    // Detect referrer or campaign
    const urlParams = new URLSearchParams(window.location.search);
    const refCode = urlParams.get('ref') || urlParams.get('coupon') || urlParams.get('utm_source') || '';
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    let pageName = 'Home';
    if (window.location.pathname.includes('product')) pageName = 'Product Page';
    else if (window.location.pathname.includes('reviews')) pageName = 'Customer Reviews';
    else if (window.location.pathname.includes('influencer')) pageName = 'Creator Portal';
    else if (window.location.pathname.includes('track')) pageName = 'Track Order';
    else if (window.location.pathname.includes('ingredients')) pageName = 'Ingredients';

    const payload = {
      session_id: sessionId,
      page: pageName,
      referrer: document.referrer ? (document.referrer.includes('instagram') ? 'Instagram' : (document.referrer.includes('google') ? 'Google Search' : document.referrer.split('/')[2])) : 'Direct Store Visit',
      campaign: refCode,
      device: isMobile ? 'Mobile' : 'Desktop',
      timestamp: new Date().toISOString()
    };

    const payloadStr = JSON.stringify(payload);

    // 1. Try Navigator sendBeacon (0ms main thread blocking)
    if (navigator.sendBeacon) {
      const blob = new Blob([payloadStr], { type: 'application/json' });
      navigator.sendBeacon('/api/admin?action=log_visitor', blob);
      return;
    }

    // 2. Fetch fallback with keepalive
    try {
      fetch('/api/admin?action=log_visitor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payloadStr,
        keepalive: true
      }).catch(function() {});
    } catch(e) {}
  }

  // Periodic lightweight heartbeat (every 20 seconds) for accurate live active traffic
  setInterval(function() {
    let sessionId = localStorage.getItem('br_session_id');
    if (sessionId && document.visibilityState === 'visible') {
      try {
        fetch('/api/admin?action=log_visitor', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ session_id: sessionId, page: 'Active Session' }),
          keepalive: true
        }).catch(function() {});
      } catch(e) {}
    }
  }, 20000);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      loadConfig();
      logLiveVisitor();
    });
  } else {
    loadConfig();
    logLiveVisitor();
  }
})();
