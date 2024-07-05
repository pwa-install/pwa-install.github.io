/**
 * Copyright 2017 Google Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

window.browser = window.browser || window.chrome;

browser.runtime.onMessage.addListener((request, sender) => {
  if (request) {
    browser.pageAction.setIcon({
      tabId: sender.tab.id,
      path: `assets/icon-${["male", "female"][Math.round(Math.random())]}.png`,
    });
    browser.pageAction.setTitle({
      tabId: sender.tab.id,
      title: `✅👷‍♀️ Active Service Worker found at ${request.scriptUrl}.`,
    });
    browser.pageAction.show(sender.tab.id);
  } else {
    browser.pageAction.setIcon({
      tabId: sender.tab.id,
      path: `assets/icon.png`,
    });
    browser.pageAction.setTitle({
      tabId: sender.tab.id,
      title: "❌👷‍♀️ No active Service Worker found.",
    });
    browser.pageAction.hide(sender.tab.id);
  }
});
