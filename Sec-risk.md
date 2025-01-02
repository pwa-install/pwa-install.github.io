### Security Risks Categorized by Lifecycle Phases

#### 1. Pre-installation Phase

1. **Security Risk**: Inconsistent profile leads to user confusion
   - **Issue**: Inconsistent profile behavior across browsers can confuse users.
   - **Consequences**: Users can inadvertently install unwanted or malicious PWAs, leading to potential security breaches.
   - **Violates**: Confidentiality
   - **Affected Browsers**:
     - Android: Firefox, Chrome, Edge

2. **Security Risk**: Private mode PWA allowed and used in normal mode
   - **Issue**: PWAs installed in private mode can be used in normal mode.
   - **Consequences**: Users' private data can be exposed or tracked without their consent.
   - **Violates**: Confidentiality
   - **Affected Browsers**:
     - Android: Firefox

3. **Security Risk**: Discrepancies in PWA installation requirements
   - **Issue**: Different browsers have varying requirements for PWA installation.
   - **Consequences**: Users can install insecure PWAs over HTTP, exposing them to man-in-the-middle attacks.
   - **Violates**: Integrity
   - **Affected Browsers**:
     - Android: Firefox (requires HTTPS for manual installation), Chrome, Edge, Opera, Brave, Samsung Internet (allow HTTP PWA installation)
     - iOS: Firefox, Chrome, Edge, Safari (allow HTTP PWA installation)
     - Desktop (Linux, MacOS, Windows): Edge, Chrome

4. **Security Risk**: Name and icon duplication causing user confusion and increasing phishing risks
   - **Issue**: Duplicate names and icons for PWAs can confuse users.
   - **Consequences**: Phishing attacks can increase as users trust and interact with malicious PWAs.
   - **Violates**: Confidentiality
   - **Affected Browsers**:
     - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
     - iOS: Firefox, Chrome, Edge, Safari
     - Desktop (Linux, MacOS, Windows): Edge, Chrome

5. **Security Risk**: ID can be duplicated and multiple PWAs in the same origin are not distinguishable by browsers
   - **Issue**: Browsers cannot distinguish between multiple PWAs from the same origin with duplicated IDs.
   - **Consequences**: Users can access or install malicious PWAs mistakenly believing them to be legitimate.
   - **Violates**: Integrity
   - **Affected Browsers**:
     - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
     - iOS: Firefox, Chrome, Edge, Safari
     - Desktop (Linux, MacOS, Windows): Edge, Chrome

6. **Security Risk**: `start_url` and scope can be a relative path or third-party URL, leading to PWAs out of scope and causing users to install PWAs out of scope
   - **Issue**: `start_url` and scope can lead to external sites.
   - **Consequences**: Users can install and interact with PWAs that can redirect them to malicious sites.
   - **Violates**: Integrity
   - **Affected Browsers**:
     - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
     - iOS: Firefox, Chrome, Edge, Safari
     - Desktop (Linux, MacOS, Windows): Edge, Chrome

7. **Security Risk**: Icon can be a third-party URL, leading to PWA phishing
   - **Issue**: PWAs can use icons hosted on third-party URLs.
   - **Consequences**: Malicious actors can change the icon to mislead users into phishing attacks.
   - **Violates**: Confidentiality
   - **Affected Browsers**:
     - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
     - iOS: Firefox, Chrome, Edge, Safari
     - Desktop (Linux, MacOS, Windows): Edge, Chrome

8. **Security Risk**: Display fullscreen mode will not show URLs to users and take up the whole screen, making it easy for PWA phishing attacks
   - **Issue**: Fullscreen mode hides the URL bar.
   - **Consequences**: Users can be tricked into believing they are on a legitimate site when they are on a phishing site.
   - **Violates**: Confidentiality
   - **Affected Browsers**:
     - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
     - iOS: Firefox, Chrome, Edge, Safari
     - Desktop (Linux, MacOS, Windows): Edge, Chrome

9. **Security Risk**: Related applications and preferred related applications fields can lead to installing other third-party native apps without confirmation
   - **Issue**: PWAs can suggest and lead to the installation of third-party apps.
   - **Consequences**: Users can inadvertently install malicious applications.
   - **Violates**: Confidentiality
   - **Affected Browsers**:
     - Android: Chrome

10. **Security Risk**: Manifest allows arbitrary self-defined fields and values, no semantic and syntactic checks like Chrome extension manifests, leading to user tracking and resource unavailability due to developer mistakes
    - **Issue**: Lack of checks on manifest fields.
    - **Consequences**: User tracking can occur, and application failures can result.
    - **Violates**: Integrity
    - **Affected Browsers**:
      - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
      - iOS: Firefox, Chrome, Edge, Safari
      - Desktop (Linux, MacOS, Windows): Edge, Chrome

11. **Security Risk**: History sniffing via Chrome Mini-Infobar
    - **Issue**: Chrome’s Mini-Infobar can expose history data.
    - **Consequences**: Malicious actors can access browsing history and track user activities.
    - **Violates**: Confidentiality
    - **Affected Browsers**:
      - Android: Chrome

#### 2. Installation Phase

12. **Security Risk**: Alert, Confirm, Prompt banner overlap with PWA installation banner leads to phishing attacks
    - **Issue**: Overlapping banners can confuse users.
    - **Consequences**: Users can click on malicious prompts, leading to phishing attacks.
    - **Violates**: Confidentiality
    - **Affected Browsers**:
      - Desktop (Linux, MacOS, Windows): Chrome, Edge

13. **Security Risk**: Lack of confirmation steps leading to accidental PWA installations
    - **Issue**: Insufficient confirmation steps.
    - **Consequences**: Users can unintentionally install PWAs, including malicious ones.
    - **Violates**: Integrity
    - **Affected Browsers**:
      - Desktop (Linux, MacOS, Windows): Chrome, Edge
      - Android: Chrome

14. **Security Risk**: Automatic prompt installation banner to users leads to accidental installations
    - **Issue**: Automatic installation prompts.
    - **Consequences**: Users can accidentally install unwanted PWAs.
    - **Violates**: Availability
    - **Affected Browsers**:
      - Android: Chrome, Edge

15. **Security Risk**: Even though users have already installed PWAs, the browser still prompts installation banners automatically
    - **Issue**: Redundant installation prompts.
    - **Consequences**: Users can get confused and install multiple instances of the same PWA.
    - **Violates**: Availability
    - **Affected Browsers**:
      - Android: Edge

16. **Security Risk**: Lack of visibility of the PWA’s origin facilitating phishing attacks
    - **Issue**: Origin information is not visible.
    - **Consequences**: Users can be tricked into trusting and using malicious PWAs.
    - **Violates**: Confidentiality
    - **Affected Browsers**:
      - Android: Firefox

17. **Security Risk**: Allowing multiple identical PWAs increases the attack surface
    - **Issue**: Multiple identical PWAs can be installed.
    - **Consequences**: Increases the risk of users installing and interacting with malicious PWAs.
    - **Violates**: Integrity
    - **Affected Browsers**:
      - Android: Chrome, Edge, Opera, Brave, Samsung Internet
      - iOS: Firefox, Chrome, Edge, Safari

#### 3. Post-installation Phase

18. **Security Risk**: No PWA manifest update leading to outdated and vulnerable PWAs
    - **Issue**: PWAs do not receive manifest updates.
    - **Consequences**: Users can continue to use outdated and potentially vulnerable PWAs.
    - **Violates**: Integrity
    - **Affected Browsers**:
      - Android: Edge, Opera, Brave, Samsung Internet, Firefox
      - iOS: Firefox, Chrome, Edge, Safari

19. **Security Risk**: Inconsistent PWA manifest update detection leading to outdated and vulnerable PWAs
    - **Issue**: Inconsistent update detection mechanisms.
    - **Consequences**: Some PWAs can fail to update, leaving users exposed to security vulnerabilities.
    - **Violates**: Integrity
    - **Affected Browsers**:
      - Desktop (Linux, MacOS, Windows): Chrome, Edge
      - Mobile: Chrome on Android

20. **Security Risk**: Navigate to third-party scopes without user awareness, leading to phishing and data theft
    - **Issue**: PWAs can navigate to third-party sites without user consent.
    - **Consequences**: Users can unknowingly provide sensitive information to malicious sites.
    - **Violates**: Confidentiality
    - **Affected Browsers**:
      - Android: Samsung Internet

21. **Security Risk**: Service worker cache-only strategies lead to PWAs never updating unless the user deletes the cache, leading to outdated and vulnerable PWAs or user tracking
    - **Issue**: Cache-only strategies prevent updates.
    - **Consequences**: Users can use outdated PWAs, increasing the risk of vulnerabilities and tracking.
    - **Violates**: Integrity
    - **Affected Browsers**:
      - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
      - iOS: Firefox, Chrome, Edge, Safari
      - Desktop (Linux, MacOS, Windows): Chrome, Edge

#### 4. Uninstallation Phase

22. **Security Risk**: Complexity and lack of intuitiveness in the uninstallation process for PWAs, leading to residual data
    - **Issue**: Uninstallation process is complex and unintuitive.
    - **Consequences**: Residual data can remain, potentially exposing users’ private information.
    - **Violates**: Confidentiality
    - **Affected Browsers**:
      - Android: Chrome, Edge, Opera, Brave, Samsung Internet, Firefox
      - iOS: Firefox, Chrome, Edge, Safari
      - Desktop (Linux, MacOS, Windows): Chrome, Edge

23. **Security Risk**: Uninstalled PWAs retaining the ability to send notification requests
    - **Issue**: Uninstalled PWAs can still send notifications.
    - **Consequences**: Users can receive unwanted notifications, leading to confusion or potential phishing attacks.
    - **Violates**: Availability
    - **Affected Browsers**:
      - Android: Chrome, Samsung Internet

24. **Security Risk**: Chrome’s PWA management affecting PWAs across different profiles
    - **Issue**: PWA management across profiles is inconsistent.
    - **Consequences**: Users can face confusion and potential unauthorized access to their data.
    - **Violates**: Confidentiality
    - **Affected Browsers**:
      - Desktop (Linux, MacOS, Windows): Chrome
     

25. **Security Risk**: Difficulties in managing and uninstalling PWAs across profiles in Edge
    - **Issue**: Management and uninstallation of PWAs across profiles are difficult.
    - **Consequences**: Users can get confused and risk unauthorized access to their data.
    - **Violates**: Confidentiality
    - **Affected Browsers**:
      - Desktop (Linux, MacOS, Windows): Edge

### Overview
#### Security Risk Overview
| Security Risk                                                   | CIA   | Browser Count |
|------------------------------------------------------------------|-------|---------------|
| Inconsistent profile leads to user confusion                    | C     | 3             |
| Private mode PWA allowed and used in normal mode                | C     | 1             |
| Discrepancies in PWA installation requirements                  | I     | 16            |
| Name and icon duplication causing user confusion and phishing   | C     | 16            |
| ID can be duplicated and multiple PWAs not distinguishable      | I     | 16            |
| `start_url` and scope leading to external sites                 | I     | 16            |
| Icon can be a third-party URL, leading to phishing              | C     | 16            |
| Display fullscreen mode hides URLs, enabling phishing attacks   | C     | 16            |
| Related applications can lead to third-party app installations  | C     | 1             |
| Manifest allows arbitrary fields, leading to tracking           | I     | 16            |
| History sniffing via Chrome Mini-Infobar                        | C     | 1             |
| Alert, Confirm, Prompt banners overlap with installation banner | C     | 6             |
| Lack of confirmation steps leading to accidental installations  | I     | 7             |
| Automatic prompt installation banners                           | A     | 2             |
| Redundant installation prompts after PWA installation           | A     | 1             |
| Lack of visibility of PWA’s origin                              | C     | 1             |
| Allowing multiple identical PWAs increases attack surface       | I     | 10            |
| No PWA manifest update                                           | I     | 10            |
| Inconsistent PWA manifest update detection                      | I     | 7             |
| Navigation to third-party scopes without awareness              | C     | 1             |
| Service worker cache-only strategies prevent updates            | I     | 16            |
| Complexity in PWA uninstallation process                        | C     | 16            |
| Uninstalled PWAs can still send notifications                   | A     | 2             |
| Chrome’s PWA management causing confusion across profiles       | C     | 3             |
| Difficulties in managing PWAs across profiles in Edge           | C     | 3             |
| **Total**                                                       |       | **203**       |

#### Security Violations per “Operating System + Browser” Combination
| #  | Operating System + Browser | Cumulative Security Risk Count |
|:--:|:--------------------------:|:------------------------------:|
| 1  | Android Firefox           | 13                            |
| 2  | Android Chrome            | 17                            |
| 3  | Android Edge              | 14                            |
| 4  | Android Opera             | 11                            |
| 5  | Android Brave             | 11                            |
| 6  | Android Samsung           | 13                            |
| 7  | iOS Safari                | 11                            |
| 8  | iOS Firefox               | 11                            |
| 9  | iOS Chrome                | 11                            |
| 10 | iOS Edge                  | 11                            |
| 11 | Windows Chrome            | 14                            |
| 12 | macOS Chrome              | 13                            |
| 13 | Linux Chrome              | 13                            |
| 14 | Windows Edge              | 14                            |
| 15 | macOS Edge                | 13                            |
| 16 | Linux Edge                | 13                            |
|    | **Total**                 | **203**                       |

#### Risk Breakdown by CIA Dimensions
| CIA Dimension  | Risk Count |
|:-------------:|-----------:|
| **C**         | 84         |
| **I**         | 114        |
| **A**         | 5          |
| **Total**     | **203**    |
