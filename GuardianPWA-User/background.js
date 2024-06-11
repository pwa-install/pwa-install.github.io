chrome.action.onClicked.addListener((tab) => {
  // Fetch the manifest.json from the current tab's URL
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: fetchManifestAndCheckName,
  });
});

async function fetchManifestAndCheckName() {
  try {
    const response = await fetch(document.location.origin + '/manifest.json');
    if (!response.ok) {
      throw new Error('No manifest.json found');
    }
    const manifest = await response.json();
    chrome.storage.local.set({ manifest: JSON.stringify(manifest, null, 2) });

    const namesResponse = await fetch(chrome.runtime.getURL('name_val.txt'));
    const namesText = await namesResponse.text();
    const namesList = namesText.split('\n').map((name) => name.trim());

    if (namesList.includes(manifest.name)) {
      alert('Name is duplicate to other PWAs, be cautious of phishing attacks');
    }
  } catch (error) {
    chrome.storage.local.set({ manifest: 'No manifest.json detected' });
    console.error('Error fetching manifest:', error);
  }
}
