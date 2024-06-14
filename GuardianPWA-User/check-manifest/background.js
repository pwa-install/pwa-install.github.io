// Function to fetch and store manifest.json
async function fetchAndStoreManifest() {
  try {
    const response = await fetch(document.location.origin + '/manifest.json');
    if (!response.ok) {
      throw new Error('No manifest.json found');
    }
    const manifest = await response.json();
    const manifestString = JSON.stringify(manifest, null, 2);

    // Get the previously stored manifest
    chrome.storage.local.get(['storedManifest'], function (result) {
      const previousManifest = result.storedManifest;

      // Compare the new manifest with the previous one
      if (previousManifest !== manifestString) {
        // Update the stored manifest
        chrome.storage.local.set({ storedManifest: manifestString });

        // Alert the user about the change
        alert('The manifest.json has changed.');
      }
    });
  } catch (error) {
    console.error('Error fetching manifest:', error);
  }
}

// Set an interval to run the fetchAndStoreManifest function every minute
setInterval(fetchAndStoreManifest, 60000);

// Initial fetch when the extension is loaded
fetchAndStoreManifest();
