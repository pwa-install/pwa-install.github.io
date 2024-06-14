document.addEventListener('DOMContentLoaded', function () {
  // Fetch the current tab and execute the script to get the manifest
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

        if (manifest) {
          outputElement.textContent = JSON.stringify(manifest, null, 2);

          // Compare with the stored manifest
          chrome.storage.local.get('manifest', function (data) {
            if (data.manifest) {
              if (JSON.stringify(data.manifest) !== JSON.stringify(manifest)) {
                alert('The new manifest is different from the stored manifest');
              }
            }

            // Store the new manifest in chrome.storage
            chrome.storage.local.set({ manifest: manifest }, function () {
              console.log('Manifest saved to chrome.storage');
            });
          });
        } else {
          outputElement.textContent = 'No manifest.json detected';
        }
      }
    );
  });

  // Add event listener to the fetch button
  document.getElementById('fetchButton').addEventListener('click', function () {
    chrome.storage.local.get('manifest', function (data) {
      const outputElement = document.getElementById('output');
      if (data.manifest) {
        outputElement.textContent = JSON.stringify(data.manifest, null, 2);
      } else {
        outputElement.textContent = 'No manifest found in storage';
      }
    });
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
      .catch(() => null);
  } else {
    return null;
  }
}
