self.addEventListener('install', (event) => {
  console.log('Service Worker installing.');
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  console.log('Service Worker activating.');
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('manifest.json')) {
    event.respondWith(
      fetch(event.request.url, {
        headers: {
          'Cache-Control': 'no-cache',
          Pragma: 'no-cache',
        },
      })
    );
  }
});

function fetchManifestAndNotify() {
  fetch('/fuzzy/manifest.json', {
    headers: {
      'Cache-Control': 'no-cache',
      Pragma: 'no-cache',
    },
  })
    .then((response) => response.json())
    .then((manifest) => {
      self.clients.matchAll().then((clients) => {
        clients.forEach((client) => {
          client.postMessage({ type: 'UPDATE_MANIFEST', manifest });
        });
      });
    })
    .catch((error) => console.error('Error fetching manifest:', error));
}

// Fetch manifest every second
setInterval(fetchManifestAndNotify, 1000);
