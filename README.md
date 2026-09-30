# Pita Cigars website

A static, multi-page HTML website for Pita Cigars. No package installation or build step is required to serve the site.

## Documentation

- [Contributing and releases](CONTRIBUTING.md): branches, required checks, code-owner review, and the `@ed1868` review-bypass exception.
- [Notifications](NOTIFICATIONS.md): GitHub review requests, CI alerts, notification preferences, and the website's notification limitations.
- [Running on Replit](replit.md): the preview server and project instructions.

## Run the site

From the repository root:

```sh
python3 -m http.server 5000 --bind 0.0.0.0
```

Open the homepage at `/`. The site includes an age-verification gate.

## Checks

GitHub Actions checks JavaScript syntax and tests the static pages and asset references. To run those checks locally, with Node.js and Python installed:

```sh
node --check js/main.js
python3 -m unittest discover -s tests -v
```

Feature PRs target `development`. Release PRs go from this repository's `development` branch to `main`; see the contribution guide before opening or merging a PR.