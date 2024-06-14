document.addEventListener('DOMContentLoaded', function () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.scripting.executeScript(
      {
        target: { tabId: tabs[0].id },
        function: findAndFetchManifest,
      },
      (injectionResults) => {
        const [result] = injectionResults;
        const manifest = result.result;
        const outputElement = document.getElementById('output');
        const currentUrl = new URL(tabs[0].url);

        if (manifest) {
          outputElement.textContent = JSON.stringify(manifest, null, 2);
          const name = manifest.name || 'No name property';

          // Check for '..' in start_url or scope
          const startUrl = manifest.start_url || 'No start_url property';
          const scope = manifest.scope || 'No scope property';

          if (startUrl.includes('..') || scope.includes('..')) {
            alert(
              'Warning: The start_url or scope contains "..", which may indicate that the installed PWA is not the current PWA.'
            );
          }

          // Check if start_url or scope differ from the current URL
          if (
            (startUrl !== '/' &&
              new URL(startUrl, currentUrl.origin).origin !==
                currentUrl.origin) ||
            (scope !== '/' &&
              new URL(scope, currentUrl.origin).origin !== currentUrl.origin)
          ) {
            alert(
              'Warning: The start_url or scope is different from the current URL, which may indicate that the installed PWA is not the current PWA.'
            );
          }

          // Alert the current URL and manifest name
          alert(`Current URL: ${currentUrl.href}\nManifest Name: ${name}`);

          const id = manifest.id || 'No id property';
          const shortName = manifest.short_name || 'No short_name property';
          const display = manifest.display || 'No display property';
          const themeColor = manifest.theme_color || 'No theme_color property';
          const backgroundColor =
            manifest.background_color || 'No background_color property';
          const description = manifest.description || 'No description property';
          const icons = manifest.icons || 'No icons property';
          const categories = manifest.categories || 'No categories property';
          const screenshots = manifest.screenshots || 'No screenshots property';
          const orientation = manifest.orientation || 'No orientation property';
          const prefer_related_applications =
            manifest.prefer_related_applications ||
            'No prefer_related_applications property';
          const related_applications =
            manifest.related_applications || 'No related_applications property';
        } else {
          outputElement.textContent = 'No manifest.json detected';
        }
      }
    );
  });
});

function findAndFetchManifest() {
  const link = document.querySelector('link[rel="manifest"]');
  if (link && link.href) {
    // Fetch the manifest file
    return fetch(link.href)
      .then((response) =>
        response.ok
          ? response.json()
          : Promise.reject('Failed to load manifest')
      )
      .then((manifest) => manifest)
      .catch((error) => null);
  } else {
    return null;
  }
}
