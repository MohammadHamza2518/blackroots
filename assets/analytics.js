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
    fetch('api/admin.php?action=get_public_config')
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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadConfig);
  } else {
    loadConfig();
  }
})();
