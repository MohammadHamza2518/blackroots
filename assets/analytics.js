/**
 * BlackRoots Unified Analytics & Marketing Pixel Engine
 * Auto-injects Google Analytics 4 (GA4), Search Console, Meta Pixel & Conversions API
 */
(function() {
  'use strict';

  // 1. Initialize Meta Pixel queue stub immediately so calls never fail
  if (!window.fbq) {
    var fbq = function() {
      if (fbq.callMethod) {
        fbq.callMethod.apply(fbq, arguments);
      } else {
        fbq.queue.push(arguments);
      }
    };
    if (!window._fbq) window._fbq = fbq;
    fbq.push = fbq;
    fbq.loaded = false;
    fbq.version = '2.0';
    fbq.queue = [];
    window.fbq = fbq;
  }

  // 2. Capture & Persist Meta Ads Attribution (fbclid & UTMs)
  function captureAttribution() {
    try {
      var params = new URLSearchParams(window.location.search);
      var fbclid = params.get('fbclid');
      var utmSource = params.get('utm_source');
      var utmMedium = params.get('utm_medium');
      var utmCampaign = params.get('utm_campaign');
      var utmContent = params.get('utm_content');
      var utmTerm = params.get('utm_term');

      var attr = JSON.parse(localStorage.getItem('br_meta_attr') || '{}');
      if (fbclid) attr.fbclid = fbclid;
      if (utmSource) attr.utm_source = utmSource;
      if (utmMedium) attr.utm_medium = utmMedium;
      if (utmCampaign) attr.utm_campaign = utmCampaign;
      if (utmContent) attr.utm_content = utmContent;
      if (utmTerm) attr.utm_term = utmTerm;
      attr.last_touch = new Date().toISOString();

      if (Object.keys(attr).length > 1) {
        localStorage.setItem('br_meta_attr', JSON.stringify(attr));
        sessionStorage.setItem('br_meta_attr', JSON.stringify(attr));
      }
    } catch(e) {}
  }
  captureAttribution();

  var DEFAULT_PIXEL_ID = '4485707268411631';

  function initMarketingStack(config) {
    if (!config) config = { meta_pixel_id: DEFAULT_PIXEL_ID };

    // A. Meta Domain Verification Tag
    if (config.meta_domain_verification) {
      var metaTag = document.querySelector('meta[name="facebook-domain-verification"]');
      if (!metaTag) {
        metaTag = document.createElement('meta');
        metaTag.name = 'facebook-domain-verification';
        document.head.appendChild(metaTag);
      }
      metaTag.content = config.meta_domain_verification;
    }

    // B. Google Search Console Verification Tag
    if (config.gsc_verification_tag) {
      var gscTag = document.querySelector('meta[name="google-site-verification"]');
      if (!gscTag) {
        gscTag = document.createElement('meta');
        gscTag.name = 'google-site-verification';
        document.head.appendChild(gscTag);
      }
      gscTag.content = config.gsc_verification_tag;
    }

    // C. Google Analytics 4 (GA4)
    if (config.ga4_measurement_id && !window.gtag_loaded) {
      window.gtag_loaded = true;
      var gaScript = document.createElement('script');
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

    // D. Meta Pixel (Facebook & Instagram Ads)
    var pixelId = (config && config.meta_pixel_id) || DEFAULT_PIXEL_ID;
    if (pixelId && !window.fbq_script_loaded) {
      window.fbq_script_loaded = true;
      
      var script = document.createElement('script');
      script.async = true;
      script.src = 'https://connect.facebook.net/en_US/fbevents.js';
      var firstScript = document.getElementsByTagName('script')[0];
      if (firstScript && firstScript.parentNode) {
        firstScript.parentNode.insertBefore(script, firstScript);
      } else {
        document.head.appendChild(script);
      }

      // Noscript image beacon
      try {
        var noscript = document.createElement('noscript');
        noscript.innerHTML = '<img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=' + pixelId + '&ev=PageView&noscript=1" />';
        (document.body || document.head).appendChild(noscript);
      } catch(e) {}

      window.fbq('init', pixelId);
      window.fbq('track', 'PageView');
      console.log('🎯 [Meta Pixel Initialized] ID: ' + pixelId);
    }
  }

  // Multi-tier config loader (localStorage -> Vercel API -> Hostinger PHP API)
  function loadConfig() {
    var config = { meta_pixel_id: DEFAULT_PIXEL_ID };
    var cached = localStorage.getItem('br_analytics_config');
    if (cached) {
      try {
        config = Object.assign(config, JSON.parse(cached));
      } catch(e) {}
    }
    initMarketingStack(config);

    var isSubdir = window.location.pathname.includes('/preview/') || window.location.pathname.includes('/demo_lab/');
    var prefix = isSubdir ? '../' : '';
    var endpoints = [
      '/api/admin?action=get_public_config',
      prefix + 'api/admin?action=get_public_config',
      '/backend_hostinger/admin.php?action=get_public_config',
      prefix + 'backend_hostinger/admin.php?action=get_public_config'
    ];

    function fetchNext(idx) {
      if (idx >= endpoints.length) return;
      fetch(endpoints[idx])
        .then(function(res) {
          if (!res.ok) throw new Error('Not ok');
          return res.json();
        })
        .then(function(config) {
          if (config && (config.meta_pixel_id || config.ga4_measurement_id || config.meta_domain_verification)) {
            var existing = {};
            try { existing = JSON.parse(localStorage.getItem('br_analytics_config') || '{}'); } catch(e) {}
            var merged = Object.assign({}, existing, config);
            localStorage.setItem('br_analytics_config', JSON.stringify(merged));
            initMarketingStack(merged);
          }
        })
        .catch(function() {
          fetchNext(idx + 1);
        });
    }

    fetchNext(0);
  }

  // Track Meta Pixel Event with CAPI Deduplication event_id support
  window.trackMetaEvent = function(eventName, data, eventId) {
    if (window.fbq) {
      if (eventId) {
        window.fbq('track', eventName, data || {}, { eventID: eventId });
      } else {
        window.fbq('track', eventName, data || {});
      }
      console.log('🎯 [Meta Pixel Tracked]', eventName, data, eventId ? ('(EventID: ' + eventId + ')') : '');
    }
  };

  // Unified D2C Event Tracker (Meta + GA4)
  window.trackD2CEvent = function(eventName, data, eventId) {
    if (window.gtag) {
      window.gtag('event', eventName, data || {});
    }
    window.trackMetaEvent(eventName, data, eventId);
  };

  // Automatic Real-Time Live Visitor Logger
  function logLiveVisitor() {
    var sessionId = localStorage.getItem('br_session_id');
    if (!sessionId) {
      sessionId = 'br_' + Date.now() + '_' + Math.random().toString(36).substring(2, 9);
      localStorage.setItem('br_session_id', sessionId);
      
      var count = Number(localStorage.getItem('br_visitor_count') || 0) + 1;
      localStorage.setItem('br_visitor_count', count);
    }

    var urlParams = new URLSearchParams(window.location.search);
    var refCode = urlParams.get('ref') || urlParams.get('coupon') || urlParams.get('utm_source') || '';
    var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
    var pageName = 'Home';
    var path = window.location.pathname;
    if (path.includes('product')) pageName = 'Product Page';
    else if (path.includes('checkout')) pageName = 'Checkout Page';
    else if (path.includes('reviews')) pageName = 'Customer Reviews';
    else if (path.includes('influencer')) pageName = 'Creator Portal';
    else if (path.includes('track')) pageName = 'Track Order';
    else if (path.includes('ingredients')) pageName = 'Ingredients';

    var referrer = 'Direct Store Visit';
    if (document.referrer) {
      if (document.referrer.includes('instagram')) referrer = 'Instagram';
      else if (document.referrer.includes('facebook')) referrer = 'Facebook';
      else if (document.referrer.includes('google')) referrer = 'Google Search';
      else {
        try { referrer = new URL(document.referrer).hostname; } catch(e) { referrer = 'Referral'; }
      }
    }

    var payload = {
      session_id: sessionId,
      page: pageName,
      referrer: referrer,
      campaign: refCode,
      device: isMobile ? 'Mobile' : 'Desktop',
      timestamp: new Date().toISOString()
    };

    var payloadStr = JSON.stringify(payload);

    if (navigator.sendBeacon) {
      var blob = new Blob([payloadStr], { type: 'application/json' });
      navigator.sendBeacon('/api/admin?action=log_visitor', blob);
      return;
    }

    try {
      fetch('/api/admin?action=log_visitor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payloadStr,
        keepalive: true
      }).catch(function() {});
    } catch(e) {}
  }

  // Periodic heartbeat (every 20s)
  setInterval(function() {
    var sessionId = localStorage.getItem('br_session_id');
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
