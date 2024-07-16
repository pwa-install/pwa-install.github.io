# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Security Risk](#security-risk)
  - [Data Collections](#data-collections)
  - [Fuzzer Program Guide](#fuzzer-program-guide)
    - [Introduction](#introduction)
    - [How to Run the Program](#how-to-run-the-program)
    - [Program Parameters and Configuration](#program-parameters-and-configuration)
    - [Modifying Fields](#modifying-fields)
    - [Script Workflow](#script-workflow)
    - [Observing Results](#observing-results)
  - [Experiment PWA](#experiment-pwa)
    - [Download Browsers](#download-browsers)
    - [Redirect to 3party with no origin show](#redirect-to-3party-with-no-origin-show)
    - [Manifest Update experiment](#manifest-update-experiment)
    - [Popup overlap experiment](#popup-overlap-experiment)
    - [Service Worker Cache-only Example](#service-worker-cache-only-example)
    - [Overview](#overview)
    - [How to Use](#how-to-use)
      - [Step 1: Prepare Your Manifests](#step-1-prepare-your-manifests)
      - [Step 2: Run the Analysis](#step-2-run-the-analysis)
      - [Step 3: Review the Output](#step-3-review-the-output)
      - [Example output:](#example-output)
      - [Recommendations](#recommendations)
  - [GuardianPWA-User](#guardianpwa-user)
    - [Overview](#overview-1)
  - [How to Install](#how-to-install)
    - [Step 1: Prepare the Extension](#step-1-prepare-the-extension)
    - [Step 2: Install the Extension in Chrome](#step-2-install-the-extension-in-chrome)
  - [How to Use](#how-to-use-1)
    - [Step 1: Visit a PWA](#step-1-visit-a-pwa)
    - [Step 2: Activate the Extension](#step-2-activate-the-extension)
    - [Step 3: Review Warnings and Manifest](#step-3-review-warnings-and-manifest)
  - [Responsible Disclosure](#responsible-disclosure)
  - [Contact](#contact)
  - [Acknowledge](#acknowledge)
## Security Risk
- Please check Sec-risk.md for details

## Data Collections
Refer to the `analysis` directory for scripts and instructions on collecting data related to Progressive Web Apps (PWAs). 

## Fuzzer Program Guide

### Introduction

This guide describes how to use our fuzzer program, which is designed to test various fields in the `manifest.json` file of a Progressive Web App (PWA). The fuzzer automates the generation, submission, and deletion of manifest files to observe how changes affect the behavior of the web application.

### How to Run the Program

1. **Ensure Python Environment:**
  Make sure you have Python installed on your system. This script uses the `json`, `os`, `random`, `string`, `subprocess`, and `time` modules, which are all part of the standard library.

2. **Clone the Repository:**
  Clone the repository where your PWA is hosted, and navigate to the directory `fuzzy`.

3. **Run the Script:**
Execute the script using Python:
  ```bash
  python fuzz.py
  ```
### Program Parameters and Configuration
*	Fields: You can define the fields and their possible values that the fuzzer will test in the fields dictionary.
*	Random String Length: The length of randomly generated strings can be adjusted by changing the random_string_length variable.
*	Number of Random Tests: Set the number of random tests by modifying the num_random_tests variable.
*	Sleep Duration: Adjust the sleep duration between commits by changing the sleep_duration variable (in seconds).

### Modifying Fields
You can add or modify the fields and their values in the fields dictionary at the beginning of the script:

```javascript
fields = {
    "name": ["TestName1", "TestName2", "TestName3", "Starbucks"],
    "short_name": ["Short1", "Short2", "Short3"],
    "scope": ["/fuzzy1/", "/no/", "/plus/"],
    "start_url": ["/start1/", "/start2/", "/start3/"],
    "background_color": ["#000000", "#111111", "#222222"],
    "dir": ["ltr", "rtl"],
    "id": ["ID1", "ID2", "ID3"],
    "theme_color": ["#ffffff", "#eeeeee", "#dddddd"],
    "display": ["standalone", "fullscreen", "minimal-ui"],
}
```
You can also add more fields as needed by following the same format.


### Script Workflow

1.	Generate Manifest File:
The generate_manifest function creates a manifest.json file with the specified fields and values.
2.	Submit Changes to GitHub:
The submit2github function stages, commits, and pushes changes to the GitHub repository. It then sleeps for a specified duration to allow time for changes to take effect.
3.	Delete Manifest File:
The delete_manifest function deletes the generated manifest.json file to prepare for the next test.
4.	Fuzz Specific Field:
The fuzz_field function iterates over the values of a specified field, generating, submitting, and deleting the manifest file for each value. It also performs random tests by generating random strings.
5.	Fuzz All Fields:
The fuzz_all_fields function calls fuzz_field for each field defined in the fields dictionary, ensuring comprehensive testing of all fields.

### Observing Results
1.	View PWA on Browser:
Navigate to pwa-install.github.io/fuzzy to view the PWA and observe the changes.
2.	Install on Various Platforms:
Manually install the PWA on different platforms (iOS, Android, desktop browsers) and monitor for any abnormal behaviors or inconsistencies caused by the changes in the manifest file.


Feel free to customize the fields and parameters to suit your testing needs. 

## Experiment PWA
### Download Browsers
- Visit [Prepare](https://pwa-install.github.io/prepare)
### Redirect to 3party with no origin show
Check below link
- [pwa-install.github.io/redirect1](https://pwa-install.github.io/redirect1)
- [pwa-install.github.io/redirect2](https://pwa-install.github.io/redirect2)
- - [pwa-install.github.io/redirect3](https://pwa-install.github.io/redirect3)
- [pwa-install.github.io/redirect4](https://pwa-install.github.io/redirect4)
- [pwa-install.github.io/redirect5](https://pwa-install.github.io/redirect5)

### Manifest Update experiment
Check below link for the experiment on manifest update:
- [pwa-install.github.io/manifest-display](https://pwa-install.github.io/manifest-display)
- [pwa-install.github.io/manifest-icon](https://pwa-install.github.io/manifest-icon)
- [pwa-install.github.io/manifest-name](https://pwa-install.github.io/manifest-name)
- [pwa-install.github.io/manifest-scope](https://pwa-install.github.io/manifest-scope)
- [pwa-install.github.io/manifest-url](https://pwa-install.github.io/manifest-url)
- [pwa-install.github.io/manifest-theme](https://pwa-install.github.io/manifest-theme)

### Popup overlap experiment
Check below link for the experiment on popup overlap:
- [pwa-install.github.io/alert](https://pwa-install.github.io/alert)
- [pwa-install.github.io/modal](https://pwa-install.github.io/modal)
- [pwa-install.github.io/popover](https://pwa-install.github.io/popover)
- [pwa-install.github.io/popup](https://pwa-install.github.io/popup)
- [pwa-install.github.io/tooltip](https://pwa-install.github.io/tooltip)

### Service Worker Cache-only Example
Please vist [pwa-install.github.io/cache-only](https://pwa-install.github.io/cache-only) for the service worker cache-only example.

### Overview
GuardianPWA-Developer is a tool designed to analyze and identify issues in the manifests of Progressive Web Apps (PWAs). It evaluates the manifest files placed in the `files2analyze` directory and provides recommendations for correcting any issues found.

### How to Use

#### Step 1: Prepare Your Manifests
Place the manifest files you want to analyze in the `files2analyze` directory.

#### Step 2: Run the Analysis
Navigate to the `src` directory and execute the main script using Python:
```sh
cd src/
python main.py
```

#### Step 3: Review the Output

The script will analyze the manifest files and summarize any issues found. For each URL, it will detail which field(s) have problems and provide recommended values to correct them.

#### Example output:
```
Invalid name value: Blessed@1B7.com 
 for ../files2analyze/1b7_com.json
, someone is using this name already, please change to another name
```

#### Recommendations
Based on the analysis output, you can modify your manifest files according to the provided recommendations. This will help ensure your PWA manifests adhere to best practices and standards.

## GuardianPWA-User

### Overview
GuardianPWA-User is a Chrome extension designed to enhance the security of Progressive Web App (PWA) users. It provides warnings for potentially dangerous situations such as incorrect `start_url`, `scope`, or `name` in the PWA manifest, and helps protect against phishing attempts by displaying the full manifest and the current URL.

## How to Install

### Step 1: Prepare the Extension
Ensure you have the `extension` folder ready, which contains all the necessary files for the Chrome extension.

### Step 2: Install the Extension in Chrome
1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable "Developer mode" by clicking the toggle switch in the top right corner.
3. Click the "Load unpacked" button and select the `extension` folder.

For detailed steps on installing a Chrome extension, refer to [this guide](https://developer.chrome.com/docs/extensions/mv3/getstarted/).

## How to Use

### Step 1: Visit a PWA
Navigate to any Progressive Web App using Chrome.

### Step 2: Activate the Extension
Click on the GuardianPWA-User extension icon in the Chrome toolbar.

### Step 3: Review Warnings and Manifest
The extension will analyze the current PWA and display warnings if there are issues such as:
- `start_url` or `scope` not matching the current PWA.
- Problems with the `name` field.


## Responsible Disclosure
We have disclosed selected security risks to browser vendors. We will hide these urls because of the anonymous policy. If you need the full list, please contact the project maintainer.

- Chrome has acknowledged the security risks that we proposed and doubt that they will fix it in the future.
- Firefox has acknowledged the security risks that we proposed and fix two of them and still working on the rest.
- Samsung Internet implies that they are intended behaviors and won't fix them.
- Brave are waiting for Chrome's action.
- Other browsers have not responded yet.


For the browsers that we tested, we use Safari (Safari 17), Chrome (117), Firefox (118), Edge (117), Samsung Internet (22), Opera (77), Brave (1).


## Contact
Because of the limited space, we can't put all the experiment setup and results in this repository.
If you need more experiment setup or results, please contact the project maintainer.
For any questions or support, please contact the project maintainer or make a PR.

## Acknowledge
Thanks to [Thomas Steiner](https://github.com/google/service-worker-detector), [Petr Gajdosik](https://github.com/Tarasa24/PWA-Store/blob/master/ManifestCrawler)!
