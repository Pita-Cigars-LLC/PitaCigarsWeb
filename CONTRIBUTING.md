# Contributing

- Create a feature branch and open its pull request against `development`, not `main`.
- Changes normally require passing site checks and an approving code-owner review from `@ed1868`. The pull request author cannot approve their own PR.
- Release pull requests must go from this repository's `development` branch to `main`. For independent review, a collaborator other than `@ed1868` opens the PR and `@ed1868` approves it after the required checks pass.
- `@ed1868` alone has an explicit review-requirement bypass on `development` and `main`. This permits merging a self-authored PR without a recorded approving review; it does not enable GitHub self-approval. Required status checks remain configured. Other users do not have this review bypass.
- The site checks run automatically on pull requests and again after changes reach `development` or `main`. Do not bypass required status checks or use the review exception unintentionally.

For review requests, CI alerts, and notification settings, see [NOTIFICATIONS.md](NOTIFICATIONS.md).