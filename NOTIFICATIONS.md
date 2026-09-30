# Notifications

This repository uses GitHub notifications for code reviews and workflow runs. The website itself does **not** send email, text messages, browser push notifications, or in-app alerts. Its contact email link opens the visitor's own email application; it does not submit a form or subscribe anyone to updates.

GitHub delivers notifications according to **each person's** watch and notification settings. A check appearing on a pull request is not a promise that every collaborator will receive an email. The website and its workflow files do not implement Slack, Teams, webhooks, or a mailing list; any integrations configured outside this repository are not covered here.

## Repository activity

| Activity | What happens | Where to look |
| --- | --- | --- |
| Feature PR into `development` | `site-checks` runs automatically. Request a review from `@ed1868` if GitHub has not already done so from `CODEOWNERS`. | PR **Checks** and **Reviewers**; GitHub notifications for requested reviewers and subscribers. |
| Push or merge into `development` | `site-checks` and `release-source` run. The latter checks the release source policy; it does not open a PR. | Repository **Actions** tab and commit checks. |
| Collaborator opens `development` → `main` PR | `site-checks` tests the PR and `release-source` verifies that its head is this repository's `development` branch. `@ed1868` reviews and merges once required checks pass. | PR **Checks**, **Reviewers**, and subscribed PR activity. |
| Push or merge into `main` | `site-checks` runs again on the merged branch. There is no separate release-announcement service or automatic GitHub Release. | Repository **Actions** tab and commit checks. |
| Comments, mentions, issues, or releases (if used) | GitHub may notify participants or watchers according to their personal settings. | [GitHub notifications inbox](https://github.com/notifications). |

The current branch-protection rules require `site-checks` on `development`, and both `site-checks` and `release-source` on `main`, normally plus an approving code-owner review. `@ed1868` alone has a review-requirement bypass and can merge without a recorded approval; GitHub still does not allow the PR author to approve their own PR. A bypassed review does not produce an approving-review notification. Checks control **whether a PR may merge**; notification preferences control **who hears about it**. See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch, reviewer, and bypass process.

## Set up your own GitHub alerts

1. On the [repository page](https://github.com/Pita-Cigars-LLC/PitaCigarsWeb), use **Watch** to subscribe. Choose **Custom** if you only want selected activity, such as pull requests, releases, or security alerts. Watching is optional; it can produce more messages than a specific review request.
2. In [GitHub notification settings](https://github.com/settings/notifications), choose **On GitHub** and/or **Email** for participating and watching activity. Email requires a verified address on your GitHub account. You can also use the GitHub Mobile inbox if you have its notifications enabled.
3. To hear about workflow runs, under **System → Actions** in those settings, select **On GitHub** or **Email**. For less noise, choose **Only notify for failed workflows**. GitHub's workflow notifications include runs you trigger and can be customized for repositories you watch; they are not a team-wide failure broadcast.
4. To follow a particular PR, subscribe to it or participate in its conversation. The person opening a PR should check its **Reviewers** sidebar and explicitly request `@ed1868` if needed. Being required for merge does not replace checking that the review request was delivered.

## When you expected a notification but did not get one

- Check the PR's **Checks** tab or the repository's **Actions** tab first. A run can be pending, failed, or absent without having sent an email to you.
- Check your [notifications inbox](https://github.com/notifications), repository watch mode, **System → Actions** setting, email delivery preference, and verified email address. Check mail filters if you chose email.
- For a missing review request, inspect the PR's **Reviewers** sidebar and request `@ed1868`. For a wrong-source release PR, open a new PR from this repository's `development` branch.
- For visitor-facing alerts, there is nothing to troubleshoot yet: no visitor notification or subscription feature has been implemented.

GitHub references: [configuring notifications](https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications), [managing Actions notifications](https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-github-actions-notifications), and [workflow-run notifications](https://docs.github.com/en/actions/concepts/workflows-and-actions/notifications-for-workflow-runs).