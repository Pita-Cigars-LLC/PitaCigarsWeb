---
name: GitHub Actions organization policy
description: Organization-level PR creation policy and workflow approval behavior for Actions bots.
---

GitHub's organization-level "Allow GitHub Actions to create and approve pull requests" setting is a ceiling on the repository setting. When the organization disallows it, enabling the repository setting fails; repository token permissions alone cannot make a `GITHUB_TOKEN` workflow open a PR. GitHub can also require manual workflow-run approval for PRs created by `GITHUB_TOKEN`, which conflicts with a requirement for completely automatic PR checks.

**Why:** An attempted automated release PR was blocked by the organization policy despite successful CI and repository administration access. A human collaborator opening the PR avoids both the policy change and bot-created PR run approval.

**How to apply:** Before promising bot-opened release PRs, check the organization Actions policy and whether PR workflow runs will require manual approval. Do not assume a repository-level permission can override the organization restriction.