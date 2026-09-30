---
name: Pita reference synchronization
description: Which upstream version to use when syncing the alternate Pita Cigars site.
---

When syncing the alternate Pita Cigars site, its published pages match the repository's `main` branch; the default branch may be an older prototype.

**Why:** The published site included newer product categories, detail pages, and optimized images that were absent from the default branch.

**How to apply:** Check the deployed routes and the `main` branch before importing an update; do not assume a default-branch clone matches the published site.