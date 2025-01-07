self.addEventListener('install', function (e) {
  // 空的 install 事件
  console.log('Service Worker installed.');
});

self.addEventListener('fetch', function (event) {
  console.log(event.request.url);

  event.respondWith(
    fetch(event.request).catch(function (error) {
      console.error('Fetch failed:', error);
      throw error;
    })
  );
});
