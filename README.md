# Timary privacy and support

Public information site for Timary. The app's source code and configuration are not part of this repository.

- English privacy policy: https://lakkiant.github.io/timary-support/privacy/
- Ukrainian privacy policy: https://lakkiant.github.io/timary-support/uk/privacy/
- Russian privacy policy: https://lakkiant.github.io/timary-support/ru/privacy/
- English support: https://lakkiant.github.io/timary-support/support/
- Ukrainian support: https://lakkiant.github.io/timary-support/uk/support/
- Russian support: https://lakkiant.github.io/timary-support/ru/support/

Contact: anton.andreev.general@gmail.com

## Editing

Edit the English and Ukrainian content in `build.py` and the Russian content in `ru.json`, then run `python3 build.py`. The generated HTML and static assets are committed to `main`. GitHub Pages serves the repository root; `.nojekyll` disables Jekyll processing.

The site has no JavaScript, external fonts, analytics, forms or cookies added by the developer. GitHub Pages performs its own hosting and security logging.

The semantic color values in `assets/theme.css` are copied from Timary's Graphite design system, including light, dark and increased-contrast appearances. The app icon belongs to Timary.

Update the policy and its effective date whenever actual data practices change. Analytics property retention is controlled in Google Analytics; the policy deliberately does not invent a setting.

## Subscriptions

The privacy policy explains on-device StoreKit entitlement checks and the defined purchase/restore analytics events. Support describes the free/Pro boundary, monthly and annual plans, renewal, restoration, offer codes and Apple refund requests in all three languages. Every page links to Apple’s standard EULA; Timary does not provide a custom license agreement. Prices and trial eligibility come from the App Store and are not hard-coded on this site.

After generating, publish these files to the public `timary-support` repository and verify the live privacy/support URLs before submitting the subscription release. Updating this copy does not deploy GitHub Pages or change App Store Connect privacy answers.
