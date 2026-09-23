# UnicLife Key Cabinet legal site

Static, dependency-free public pages for App Store Connect and Google Play Console. The pages do not contain forms, trackers, analytics or user-submitted data. Requests are sent by the visitor's own email app.

## Pages and store fields

After GitHub Pages is enabled for `ytwl1013/uniclife-legal`, use:

| Store field | URL |
| --- | --- |
| App Store Connect → App Privacy → Privacy Policy URL | `https://ytwl1013.github.io/uniclife-legal/privacy/` |
| App Store Connect → App Privacy → User Privacy Choices URL (optional) | `https://ytwl1013.github.io/uniclife-legal/privacy-choices/` |
| App Store Connect → App Information → Support URL | `https://ytwl1013.github.io/uniclife-legal/support/` |
| Google Play Console → Store listing → Privacy policy | `https://ytwl1013.github.io/uniclife-legal/privacy/` |
| Google Play Console → App content → Data safety → Account deletion URL | `https://ytwl1013.github.io/uniclife-legal/delete-account/` |

These URLs are **expected**, not live until Pages has deployed and each link has been checked without signing in.

## Publish with GitHub Pages

1. Confirm that the GitHub repository `ytwl1013/uniclife-legal` is public and that the intended legal operator name and contact details on every page are accurate.
2. In this folder, run `git status`, `git add .`, `git commit -m "Add app privacy and support pages"`, then `git push -u origin main`. This folder is its own Git repository; run these commands inside `uniclife-legal`, not in the app repository.
3. Open the GitHub repository → **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/(root)**, then **Save**.
4. Wait for the Pages deployment to finish. GitHub says publication can take up to about 10 minutes. Open all five URLs in a signed-out/incognito browser; check page content, navigation and email links. Only then paste them into the store consoles.

GitHub Pages setup: <https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site>

## Before store submission

- Confirm and name the actual legal entity or individual operating the service. The current privacy text refers to the service provider in the order form or service agreement; that is not enough where no such agreement exists. Add the exact operator identity and usable contact details before public launch.
- Verify the published contact mailbox is monitored and can handle privacy/deletion requests. The site currently uses `ytwl1013@gmail.com`, based on the app-store metadata working document.
- Check the production hosting region, vendors and international transfer safeguards. The policy describes US hosting based on the app's existing privacy text; do not claim a transfer mechanism that has not been put in place.
- Compare this policy with the in-app text in the app repository. Align the effective date, operator, contact route, categories and retention wording before submitting a release.
- Complete the App Store privacy questionnaire and Google Play Data safety form from the final app binary and service behavior, including SDKs. The published pages are not substitutes for those declarations.
- Check the real account-deletion process, including the Super Admin handoff and retained historical records. The external support mailbox must process requests from people who cannot access the app.
- If offering the app in non-English EU markets, arrange a legal review of local-language privacy notices and any applicable EU/UK representative or transfer requirements.

Official policy references: [Apple App Privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy), [Apple Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [Google Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en), [Google Play account deletion](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en).
