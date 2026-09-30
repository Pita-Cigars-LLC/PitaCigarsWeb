#!/usr/bin/env bash
set -euo pipefail

# This project is served as static HTML and has no dependency or migration step.
test -f index.html
printf 'Static site is ready; no install or build step is required.\n'