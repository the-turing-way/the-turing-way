/**
 * This file contains the tracking code that allows analytics to work on The Turing Way using Matomo
*/

var _paq = window._paq = window._paq || [];
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
  var u="https://theturingwaynetlifyapp.matomo.cloud/";
  _paq.push(['setTrackerUrl', u+'matomo.php']);
  _paq.push(['setSiteId', '1']);
  var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
  g.type='text/javascript'; g.async=true; g.src='//cdn.matomo.cloud/theturingwaynetlifyapp.matomo.cloud/matomo.js'; s.parentNode.insertBefore(g,s);
})();
