document.addEventListener('DOMContentLoaded', function () {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.scripting.executeScript(
      {
        target: { tabId: tabs[0].id },
        func: checkForFunctions,
      },
      (results) => {
        const resultContainer = document.getElementById('resultContainer');
        if (
          chrome.runtime.lastError ||
          !results ||
          !results[0] ||
          !results[0].result
        ) {
          resultContainer.textContent = 'Unable to check the page.';
          return;
        }
        const foundFunctions = results[0].result;
        if (foundFunctions.length > 0) {
          resultContainer.textContent = `Found the following functions: ${foundFunctions.join(
            ', '
          )}`;
        } else {
          resultContainer.textContent =
            'No alert, confirm, or prompt functions found.';
        }
      }
    );
  });
});

function checkForFunctions() {
  const scripts = document.getElementsByTagName('script');
  const functionNames = ['alert', 'confirm', 'prompt'];
  let foundFunctions = [];

  const checkScriptContent = (scriptContent) => {
    functionNames.forEach((func) => {
      if (scriptContent.includes(func)) {
        if (!foundFunctions.includes(func)) {
          foundFunctions.push(func);
        }
      }
    });
  };

  const promises = [];

  for (let script of scripts) {
    if (script.src) {
      // Fetch external script content
      const promise = fetch(script.src)
        .then((response) => response.text())
        .then((text) => checkScriptContent(text))
        .catch((error) =>
          console.error('Error fetching external script:', error)
        );
      promises.push(promise);
    } else {
      // Inline script content
      checkScriptContent(script.innerHTML);
    }
  }

  return Promise.all(promises).then(() => foundFunctions);
}
