---
name: GitHub repository ownership
description: Verify canonical repository ownership after transfers before publishing code.
---

GitHub repository transfers can leave redirects from a previous owner URL. A successful read from an old URL does not prove that the repository is still owned by the requested account.

**Why:** During the Pita site upload, the repository moved between a personal account and the organization; reads followed redirects while pushes to the former location were denied.

**How to apply:** Before future pushes, compare the API's canonical `full_name` with the requested owner and repository. Disable HTTP redirects for the Git write operation so it cannot follow an old URL to a different owner.