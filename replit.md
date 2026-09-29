# Running this site on Replit

This is a static, multi-page HTML site. No package installation or build step is required.

The `Start application` workflow serves the project root on port 5000 with Python's built-in HTTP server. To run it manually:

```sh
python3 -m http.server 5000 --bind 0.0.0.0
```

Open the homepage at `/`. The site includes an age-verification gate before the content is available.